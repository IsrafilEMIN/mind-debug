"""Offline packaging/contract checks; these do not test agent behavior."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/prioritization/SKILL.md"


class RepositoryTests(unittest.TestCase):
    def test_frontmatter(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        _, header, body = text.split("---\n", 2)
        for key in ("name", "description", "version", "author", "license", "platforms", "metadata"):
            self.assertRegex(header, rf"(?m)^{key}: .+|^{key}:$")
        self.assertIn("name: prioritization\n", header)
        match = re.search(r'^description: "(.+)"$', header, re.M)
        self.assertIsNotNone(match)
        assert match is not None
        description = match.group(1)
        self.assertLessEqual(len(description), 60)
        self.assertTrue(description.endswith("."))
        self.assertTrue(body.strip())
        self.assertLessEqual(len(text), 100_000)

    def test_relative_markdown_links_resolve(self):
        for source in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(source=source, target=target):
                    destination = (source.parent / target.split("#")[0]).resolve()
                    self.assertTrue(destination.is_relative_to(ROOT))
                    self.assertTrue(destination.is_file())

    def test_skill_has_required_sections(self):
        text = SKILL.read_text(encoding="utf-8")
        for title in ("When to Use", "Prerequisites", "Procedure", "Pitfalls", "Verification"):
            self.assertIn(f"## {title}\n", text)

    def test_brief_contract(self):
        text = (SKILL.parent / "templates/priority-brief.md").read_text(encoding="utf-8")
        for field in ("Baseline:", "Facts and sources:", "Assumptions:", "Current blocker hypothesis:",
                      "Evidence that would disprove it:", "Reversal condition:", "## Now", "Owner (confirmed or proposed):",
                      "Timebox:", "Observable artifact:", "Acceptance criterion:", "Stop / pivot condition:",
                      "Revisit trigger", "## Review", "Execution authorization:"):
            with self.subTest(field=field):
                self.assertIn(field, text)

    def test_no_machine_local_paths_or_secret_tokens(self):
        for source in ROOT.rglob("*.md"):
            text = source.read_text(encoding="utf-8")
            with self.subTest(source=source):
                self.assertNotRegex(text, r"/Users/|/home/|[A-Z]:\\Users\\")
                self.assertNotRegex(text, r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}")

    def test_behavioral_suite_is_explicitly_unrun(self):
        text = (ROOT / "evals/scenarios.md").read_text(encoding="utf-8")
        self.assertIn("not executed in Hermes or OMP", text)
        ids = re.findall(r"^\| ([A-J]):", text, re.M)
        self.assertEqual(ids, list("ABCDEFGHIJ"))
        self.assertIn("Hard failure", text)


if __name__ == "__main__":
    unittest.main()
