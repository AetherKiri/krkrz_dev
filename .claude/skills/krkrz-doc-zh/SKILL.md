---
name: krkrz-doc-zh
description: krkrz_dev の doc/（日本語）を簡体字中国語へ翻訳し、doc/zh/ ミラーへ配置して mkdocs-static-i18n の日中二言語サイトを維持するためのリポジトリ内スキル。中文说明：把 doc/ 日文文档翻译为简体中文、维护 doc/zh/ 译文、保证术语一致、集成与验证 mkdocs 中日双语站点、检查译文与日文原文的漂移时使用。触发词：翻译文档、中文译文、doc/zh、双语站点、术语统一、译文校对、翻訳。
---

# krkrz 文档中文化（doc/ → doc/zh/）

把 `doc/` 下的日文文档（MkDocs 站点，311 个 md）翻译为**简体中文**，译文镜像放在 `doc/zh/`，
用 mkdocs-static-i18n 的 **folder 模式**构建中日双语站点（日文在 `/`，中文在 `/zh/`）。

> 本 skill 是**仓库内专用**，不进 `tools/skills/install.sh` 的分发清单（它依赖本仓库的
> `doc/`、`mkdocs.yml`、`tools/docgen/`）。

## 适用范围

- ✅ 翻译 / 校对 `doc/**/*.md`（guide・topics・tjs2・specification・reference・index・demos）
- ✅ 维护 `doc/zh/` 与 `mkdocs.yml` 的 i18n 配置（见 `i18n-setup.md`）
- ❌ 不用于：`doc/manual/*.manual.tjs`（生成源，见下）、`doc/_missing.md` / `_inventory.json`（生成报告）、
  `doc/_assets/`（图片）、源码注释、把日文翻成英文

## 硬规则（翻译前必读）

1. **目录镜像**：`doc/<相对路径>` ↔ `doc/zh/<相对路径>`。**文件名、大小写完全不变**。
2. **相对链接、图片路径与日文原文保持同一写法**。插件会"当前语言优先 → 回退日文根"自动解析（已实测），
   **不要自作主张加 `../`**。示例：日文 `../../reference/Layer.md`，译文照抄 `../../reference/Layer.md`；
   日文 `../_assets/x.png`，译文照抄。链接目标必须真实存在（构建 `--strict` 会检查译文页里的死链）。
3. **代码块（``` 围栏内）逐字节原样**：不翻译、不重排、不改缩进、**连注释也不改**（v1 硬规则，
   `check_pair.py` 强制）。
4. **行内代码与标识符不译**：`` `Layer` ``、`loadImages`、`dfBoth`、`-repl`、`data/`、`System.exe`
   ……原样。首次出现可括注中文，如 `存储（Storages）`。
5. **标题**：
   - `reference/` 的 API 名称标题（`### face`、`### loadImages`）**原样保留**——跨页锚点依赖它。
   - 其他标题翻译。**锚点链接（`(#...)`）指向被译标题时**会因 slug 变化而失效：优先改为指向
     保留 ASCII 的标题，或在标题上用 attr_list 固定锚点（`## 启动 {#startup}`），或同步改写所有引用。
     集成 i18n 后构建启用 `validation.anchors: warn`（见 `i18n-setup.md`），坏锚点会让 `--strict`
     失败；集成前用 `check_pair.py` 的 `[W] 锚点` 检查。
6. **不摘要、不删节、不合并**：1:1 逐段翻译；表格逐行、单元格逐个翻；admonition 的标记与类型词
   （`!!! note` / `??? tip`）保留，只翻正文与 advisory title（`!!! note "标题"`）。
7. **引用运行时的日文字符串 / 控制台输出**：保留日文原文（那是用户实际看到的内容），
   必要时在正文补中文说明。
8. **标点与文体**：见 `glossary.md` 的「文体与标点」。术语一律以 `glossary.md` 为准，
   新术语**先补表再使用**。
9. **不加戏**：不添加原文没有的说明、例子、链接、徽章；不加机器翻译痕迹（"非常棒的"之类）。
10. **禁止项目/客户识别信息**（沿袭 CLAUDE.md）：译文里不得出现具体的案件名、客户名、游戏名、issue key。

## 工作流（逐文件）

1. **选文件**。优先级建议：`doc/index.md`（双语站点首页，最先）→ `guide/` → `topics/` →
   `tjs2/` → `specification/` → `reference/`（生成物，量大且可回退，最后做）。
2. **通读日文原文全文**（不要只看开头再凭感觉补）。
3. 在 `doc/zh/` 建立镜像路径，逐块翻译：frontmatter（若有，键不动、标题类值可译）→ 正文 →
   表格 → 列表 → 代码块（原样）。
4. **自检**：

   ```bash
   python3 .claude/skills/krkrz-doc-zh/scripts/check_pair.py doc/guide/Startup.md
   python3 .claude/skills/krkrz-doc-zh/scripts/check_pair.py --all            # 全部已有译文
   python3 .claude/skills/krkrz-doc-zh/scripts/check_pair.py --untranslated   # 还剩哪些没翻
   ```

   必须 0 ERROR；WARNING 逐条判断（假名残留多半是漏译，也可能是刻意保留的引文）。
5. **nav 标题**：翻到某个页面时，把该页在 `mkdocs.yml` nav 上的**标题链**补进
   `languages[zh].nav_translations`（键 = 日文标题原文；路径式条目用其 H1 作键，已实测可用）。
6. **构建验证**（改了 `doc/zh/index.md`、nav、链接后至少做一次）：

   ```bash
   pip install -r tools/docgen/requirements.txt
   mkdocs build --strict
   mkdocs serve   # / = 日文，/zh/ = 中文，页头可切换语言
   ```

## 生成物与特殊文件（重要）

| 对象 | 处理 |
|---|---|
| `doc/reference/<Class>.md` | **由 `tools/docgen/tjsdoc.py` 从 `doc/manual/*.manual.tjs` 生成**。翻译放 `doc/zh/reference/`，不影响生成；但日文侧重新生成后译文会**漂移**——重生成后跑 `check_pair.py --all` 检结构（代码块/标题/链接），再补译变更内容 |
| `doc/manual/**` | 生成 SSOT（日文），**不翻译** |
| `doc/_missing.md`、`doc/_inventory.json` | 生成报告，**不翻译** |
| `doc/_assets/**` | 图片不处理；图内日文为已知限制。译文按硬规则 2 引用原图 |
| `doc/demos.md` | iframe 嵌 wasm 演示，演示本身不译；正文可翻（低优先） |
| `doc/coi-serviceworker.js` | 站点运行所需，不动 |

## 文件索引

- `glossary.md` — **术语表 + 文体标点规则**（每篇翻译前对照）
- `i18n-setup.md` — mkdocs 双语站点集成方案（requirements / mkdocs.yml 具体改法 / 已验证行为与限制）
- `scripts/check_pair.py` — 成对自检（代码块一致 / 标题结构一致 / 链接可达 / 假名残留 / 锚点）
- `agent-brief.md` — 多 Agent 批量翻译时发给每个翻译 agent 的标准作业指导

## 提交注意

- 译文提交只碰 `doc/zh/**`（必要时加 `mkdocs.yml`）；**不要混入日文原文改动**。
- `doc/**` 的 push 会触发 `.github/workflows/docs-pages.yml`（`mkdocs build --strict` → Pages）。
  译文进默认分支前，确保本地 `--strict` 通过。
- 翻译分支/fork 上先落地；是否把 i18n 配置合入上游是单独决策（见 `i18n-setup.md` 末尾）。
