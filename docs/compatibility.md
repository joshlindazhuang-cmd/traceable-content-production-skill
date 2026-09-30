# 跨工具兼容与安装

## 兼容原则

本仓库把可移植能力放在 `skills/traceable-content-production/` 中。该目录遵循 Agent Skills 的通用结构：必需的 `SKILL.md`，以及按需读取的 `references/`、`assets/` 和可选元数据。

GitHub Release 另外提供同一目录的 `.zip` 与 `.skill` 包。压缩包只有一个顶层 `traceable-content-production/` 文件夹，便于只接受单 Skill 包的客户端导入。

首次启用说明卡发生在 Skill 被 AI 实际调用时，而不是安装文件完成时。不同宿主对自动发现和首次调用的处理可能不同；没有自动调用的工具可通过显式命令启动一次。

兼容性分成两层：

1. **格式兼容**：工具能够识别 Agent Skills 标准的 `SKILL.md` 和同目录资源；
2. **运行兼容**：工具还需要具备读取和写入本地 Markdown 文件的能力，网络事实核查则需要搜索或网络访问能力。

如果运行环境不能写入文件，文字审校与成稿仍可在当前会话执行，但账号档案、偏好和追溯记录不能被声称为已经持久化。

## 已有官方支持

| 工具 | 官方支持与推荐入口 | 本仓库建议 |
|---|---|---|
| Codex | 支持项目或用户级 `.agents/skills/`，也可让 `$skill-installer` 从其他仓库下载 | 复制到 `~/.agents/skills/`，或把仓库内 Skill 路径交给安装器 |
| Claude Code | 遵循 Agent Skills 开放标准；个人目录为 `~/.claude/skills/`，项目目录为 `.claude/skills/` | 复制 Skill 文件夹到相应目录 |
| Cursor | 原生发现 `.agents/skills/`、`.cursor/skills/`，也兼容 Claude 和 Codex 的 Skill 目录 | 优先使用 `~/.agents/skills/`，项目级使用 `.agents/skills/` |
| Gemini CLI | 原生支持从 Git 仓库安装并用 `--path` 指定 Skill 子目录；也发现 `~/.agents/skills/` 和项目 `.agents/skills/` | 使用仓库 URL 加 `--path skills/traceable-content-production`，或复制到通用目录 |
| GitHub Copilot | 支持项目 `.github/skills/`、`.claude/skills/`、`.agents/skills/`，个人 `~/.copilot/skills/` 或 `~/.agents/skills/` | 使用 `gh skill install OWNER/REPO`，或复制到通用目录 |

官方文档：

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex: Build skills](https://developers.openai.com/codex/skills)
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [Cursor: Agent Skills](https://cursor.com/docs/skills)
- [Gemini CLI: Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/)
- [GitHub Copilot: Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)

## 通用手动安装

先下载仓库，然后只复制 Skill 目录：

```bash
git clone https://github.com/joshlindazhuang-cmd/traceable-content-production-skill.git
```

通用目录：

```bash
mkdir -p ~/.agents/skills
cp -R traceable-content-production-skill/skills/traceable-content-production ~/.agents/skills/
```

Claude Code 目录：

```bash
mkdir -p ~/.claude/skills
cp -R traceable-content-production-skill/skills/traceable-content-production ~/.claude/skills/
```

项目级安装使用同样的 Skill 文件夹，只把目标改为项目中的 `.agents/skills/` 或 `.claude/skills/`。

Gemini CLI 可直接安装仓库内的 Skill 子目录：

```bash
gemini skills install https://github.com/joshlindazhuang-cmd/traceable-content-production-skill.git --path skills/traceable-content-production
```

GitHub CLI 的最短交互式安装命令为：

```bash
gh skill install joshlindazhuang-cmd/traceable-content-production-skill
```

通过该命令安装的 Skill 会记录来源，但不会实时同步仓库。发布新版本后可运行：

```bash
gh skill update traceable-content-production
```

## 对其他 AI 软件的判断

满足下列任一条件时，可以尝试安装：

- 明确声明支持 Agent Skills 标准；
- 能导入包含 `SKILL.md` 的文件夹或压缩包；
- 允许把 Markdown 规则作为项目级或用户级自定义指令加载。

如果软件只有单个提示词输入框，最多只能迁移 `SKILL.md` 的核心规则，无法保证它会按需读取 `references/`、写入私有档案或正确执行暂停—恢复流程。这种情况应称为“提示词适配”，不能称为完整安装。

## 尚未逐工具实测的边界

V0.2.0 已验证开放规范结构、文件引用、发布压缩包和 Codex 运行链路。V0.3.0 已验证新增文件、引用、安装包和首次说明契约；首次说明、多账号选择和档案持久化在不同客户端中的实际行为仍需分别外测。Claude Code、Cursor、Gemini CLI 与 GitHub Copilot 的安装方式来自各自官方文档。发现差异时，请提交工具名称、版本、安装方式和可复现现象。
