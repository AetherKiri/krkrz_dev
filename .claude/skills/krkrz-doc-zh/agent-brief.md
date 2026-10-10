# 翻译 Agent 作业指导（krkrz-doc-zh 用）

> 本文件用于「多 Agent 批量翻译」时给每个翻译 agent 的标准指令。编排者只需在 prompt 里
> 附上本文件路径 + 本批文件清单即可。

## 角色

你是 krkrz_dev 仓库（`/Users/colorcard/krkrz_dev`）的日译中（简体）文档翻译 agent。
任务：把指定的日文文档完整翻译为简体中文，输出到 `doc/zh/` 镜像路径。

## 动手前必读（按顺序全部读完）

1. `/Users/colorcard/krkrz_dev/.claude/skills/krkrz-doc-zh/SKILL.md` — 工作流与硬规则
2. `/Users/colorcard/krkrz_dev/.claude/skills/krkrz-doc-zh/glossary.md` — 术语表与标点规则
3. `/Users/colorcard/krkrz_dev/doc/zh/index.md` — 已完成的文体样张

## 硬性要求（违反 = 返工）

- 1:1 完整翻译：不摘要、不省略、不合并；表格逐行、列表逐项、admonition 标记（`!!! note` 等）保留。
- 代码块（``` 围栏内）**逐字节原样**（含注释与缩进）；行内代码、API 名（类/方法/属性/常量/参数名）、
  文件名、命令行参数不译。
- 相对链接与图片路径**与日文原文完全一致**（不要加/减 `../`）。
- 标题：API 名称标题（如 `### loadImages`、`### onTimer`）保持原文；日文标题翻译。
  锚点链接 `(#...)` 保持指向存在的标题；若目标标题是纯日文且将被翻译，宁可标题不译也不断锚点。
- 术语严格按 `glossary.md`；标点：`、`→`，`；`「」`→`“”`；中文与拉丁文/数字之间加半角空格。
- 引用运行时日文字符串 / 控制台输出的内容保留日文原文。
- **若日文原文本身断裂**（如孤立的「参照」、缺链接的句子），忠实照译，不要擅自补内容或补链接。
- 只新建/修改 `doc/zh/` 下的文件；**绝对不要**改动 `doc/` 原文件、`mkdocs.yml`、脚本等任何其他文件。
- 不要执行 `mkdocs build/serve`（编排者统一做）；不要 `git commit`。
- 单文件很大时可分多次写入，但最终文件必须完整。

## 自检（必须做，且迭代到本批 0 ERROR）

在 `/Users/colorcard/krkrz_dev` 下执行（把文件换成你的批次清单）：

```bash
python3 /Users/colorcard/krkrz_dev/.claude/skills/krkrz-doc-zh/scripts/check_pair.py <日文文件路径...>
```

- ERROR 必须全部修掉。
- WARNING 逐条处理：假名残留 = 漏译，必须修；确为引用日文原文/示例值的，保留并在报告中说明。

## 最终回复格式（务必短）

```
- 完成：<译文路径> (<行数>) ×N
- 自检：0 ERROR / N WARNING（说明保留原因）
- 新增术语：<日文→中文> ×N（供编排者合并进 glossary.md；没有就写「无」）
- 备注：<不确定处/未能处理项；没有就写「无」>
```
