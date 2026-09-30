#!/usr/bin/env python3
"""Static release-contract checks for the portable Skill package."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "traceable-content-production"


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class ReleaseContractTests(unittest.TestCase):
    def test_release_metadata_is_v030(self) -> None:
        skill = read("skills/traceable-content-production/SKILL.md")
        self.assertRegex(skill, r'version:\s*["\']0\.3\.0["\']')

    def test_first_run_guide_contract_is_documented(self) -> None:
        profiles = read(
            "skills/traceable-content-production/references/profiles-and-traces.md"
        )
        for required in (
            "首次启用说明卡",
            "同一轮继续处理",
            "只展示一次",
            "查看使用说明",
            "仅在当前会话有效",
        ):
            self.assertIn(required, profiles)

    def test_first_run_state_and_account_index_templates_exist(self) -> None:
        state = SKILL / "assets" / "system-state-template.md"
        index = SKILL / "assets" / "accounts-index-template.md"
        self.assertTrue(state.is_file())
        self.assertTrue(index.is_file())
        self.assertIn("onboarding-version", state.read_text(encoding="utf-8"))
        self.assertIn("账号索引", index.read_text(encoding="utf-8"))

    def test_standalone_article_does_not_require_account_profile(self) -> None:
        skill = read("skills/traceable-content-production/SKILL.md")
        profiles = read(
            "skills/traceable-content-production/references/profiles-and-traces.md"
        )
        self.assertIn("独立完成", skill)
        self.assertIn("account: none", profiles)
        self.assertIn("不要求先建档", profiles)

    def test_account_and_preference_context_are_scoped_enhancements(self) -> None:
        profiles = read(
            "skills/traceable-content-production/references/profiles-and-traces.md"
        )
        for required in (
            "柔性增强",
            "跨账号个人偏好",
            "账号档案",
            "本篇临时要求",
            "最小适用范围",
            "不得自动持久化",
        ):
            self.assertIn(required, profiles)

    def test_existing_default_profile_has_non_destructive_migration(self) -> None:
        profiles = read(
            "skills/traceable-content-production/references/profiles-and-traces.md"
        )
        self.assertIn("accounts/default.md", profiles)
        self.assertIn("不得覆盖、删除或自动改名", profiles)
        self.assertIn("逐一登记", profiles)

    def test_readme_explains_first_use_and_multi_account_behavior(self) -> None:
        readme = read("README.md")
        for required in (
            "V0.3.0",
            "首次启用说明卡",
            "多个账号",
            "无需先建档",
        ):
            self.assertIn(required, readme)

    def test_all_local_skill_links_resolve(self) -> None:
        for markdown in SKILL.rglob("*.md"):
            content = markdown.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
                if "://" in target or target.startswith("#"):
                    continue
                resolved = (markdown.parent / target.split("#", 1)[0]).resolve()
                self.assertTrue(resolved.exists(), f"Broken link in {markdown}: {target}")


if __name__ == "__main__":
    unittest.main()
