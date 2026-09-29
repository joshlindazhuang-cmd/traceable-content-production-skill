# Traceable Content Production Skill

一套面向观点、资料包和已有草稿的可追溯 AI 内容生产 Skill。它帮助 Codex 自动识别输入类型，完成事实、逻辑、立场与表达审校，并在安全通过后交付完整成稿。

它不是固定文风模板，也不以“尽快生成一篇看起来完整的文章”为目标。账号定位和个人偏好可以配置，但不能覆盖事实诚信、证据边界和来源归属。

## V0.1.0 能做什么

- 自动路由观点种子、丰富材料包、已有草稿和混合文字输入；
- 区分用户事实、用户观点、第三方材料、外部证据、编辑推演与虚构示例；
- 执行事实证据、逻辑链条、立场边界、表达呈现四项审查；
- 使用 `PASS / REVISE / DISCUSS / BLOCK` 状态门禁；
- 非 `PASS` 时一次说明全部关键问题，只提出一个最高价值问题并暂停；
- `PASS` 时交付完整文章、准确标题和必要的来源或不确定性说明；
- 在本地工作区保存账号档案、经用户确认的表达偏好和结构化运行记录；
- 保留作者声音，同时避免虚构作者经历、心理、数据、案例或权威结论。

## 当前不包含

- 图片分析、图片生成和视觉加工；
- 主动网络搜图；
- 公众号或其他平台的视觉排版；
- 自动发布；
- 对参考文章进行文风迁移或仿写。

这些能力属于后续版本，不计入当前文字版的通过结论。

## 安装

### 让 Codex 安装

把下面的仓库路径交给 Codex，并要求安装其中的 Skill：

```text
https://github.com/joshlindazhuang-cmd/traceable-content-production-skill/tree/main/skills/traceable-content-production
```

### 手动安装

```bash
git clone https://github.com/joshlindazhuang-cmd/traceable-content-production-skill.git
mkdir -p ~/.codex/skills
cp -R traceable-content-production-skill/skills/traceable-content-production ~/.codex/skills/
```

安装后新开一个 Codex 任务，并可明确调用：

```text
使用 $traceable-content-production，把下面的观点和材料发展成一篇可追溯的文章：……
```

## 私有配置

首次在一个内容工作区使用时，Skill 会按需创建：

```text
.content-system/
├── .gitignore
├── user-preferences.md
├── accounts/
│   └── default.md
└── runs/
```

这些文件保存使用者自己的账号信息、写作偏好和运行记录，默认不会进入 Git。仓库中只提供空白模板，不包含作者个人配置。

## 关键交互规则

- `PASS`：自动继续并交付完整正文；
- `REVISE`：实质修订会改变核心立场、论据或目标，暂停等待用户；
- `DISCUSS`：存在多个合理方向且无法可靠替用户选择，暂停等待用户；
- `BLOCK`：内容必须依赖伪造、欺骗、明显错误或污名化才能成立，不生成可发布稿。

系统只在缺失信息会改变核心立场或目标、无法可靠推断且错判会明显失真时提问。其余结构、语气和篇幅由系统结合文章任务、账号策略和已确认偏好自动处理。

## 测试状态

V0.1.0 已完成人工 RED / GREEN / REFACTOR 测试以及一次全新工作区端到端冒烟测试，覆盖偏好确认后持久化、不可信材料边界、暂停与恢复、完整成稿和结构化追溯。详见 [验证记录](docs/verification.md)。

当前结论是“文字主链路可进入外部测试”，不是“所有场景永久无缺陷”。欢迎通过 Issue 提交可复现的输入、实际输出、期望行为和使用环境。

## 文档

- [文字工程契约](docs/text-engineering-contracts.md)
- [验证记录与已知边界](docs/verification.md)

## 许可证

[MIT](LICENSE)
