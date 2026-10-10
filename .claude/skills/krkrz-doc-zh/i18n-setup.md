# mkdocs 中日双语站点集成（已验证）

> 实测基线：mkdocs 1.6.1 + mkdocs-material 9.7.6 + mkdocs-static-i18n 1.3.1（2026-10，本仓库真实文档树构建验证）。
> 结构：**folder 模式**，`doc/` = 日文（默认语言，站点 `/`），`doc/zh/` = 中文（站点 `/zh/`）。

## 1. requirements.txt

`tools/docgen/requirements.txt`：

```diff
 mkdocs-material>=9.5
 beautifulsoup4>=4.12
+mkdocs-static-i18n>=1.3
```

## 2. mkdocs.yml 修改

```diff
 docs_dir: doc

+validation:
+  anchors: warn
+
 theme:
   name: material
   language: ja
   ...

 plugins:
   - search:
       lang: ja
       separator: '[\s\-,:!=\[\]()"/]+|\.(?!\d)|&[lg]t;'
+  - i18n:
+      docs_structure: folder
+      fallback_to_default: true
+      reconfigure_material: true
+      reconfigure_search: true
+      languages:
+        - locale: ja
+          default: true
+          name: 日本語
+          build: true
+        - locale: zh
+          name: 简体中文
+          build: true
+          site_name: 吉里吉里Z 文档
+          theme:
+            language: zh
+          nav_translations:
+            ホーム: 首页
+            # …（见 §4，边翻边补）

 nav:
+  - ホーム: index.md
   - デモ: demos.md
   ...
```

### 为什么必须把 `index.md` 加进 nav（关键）

mkdocs-static-i18n 会检查 `nav.homepage`，找不到就发 **WARNING**："Could not find a homepage for
locale '…'"。本仓库现有 nav 里没有 `index.md` 条目 → 每个语言的构建都会出这个警告 →
`.github/workflows/docs-pages.yml` 的 `mkdocs build --strict` **直接失败**。

加上 `- ホーム: index.md` 后：
- 日文侧 `/` 的首页被识别为主页；即使 `doc/zh/index.md` 还没翻，中文侧也会用回退页当首页（已实测通过）。
- 副作用：日文站 tab 栏多一个「ホーム」（`navigation.tabs` 开启）。如果不想改日文站外观，
  把 `index.md` 放到某个 section 的子项也能通过检测（页面依然生成，但语义上推荐顶栏）。
- 顶栏标题通过 `nav_translations` 映射：`ホーム: 首页`。

### 其他要点（实测）

- **search 不用改**：插件自动把 `zh` 追加进 `plugins.search.lang`（mkdocs 自带 `lunr.zh.js`，
  多语言索引可用）。现有 `lang: ja` + `separator` 保留即可。
- **不需要 `extra.alternate`**：`reconfigure_material: true` 自动生成语言切换器、hreflang
  `<link rel="alternate">`；`site_url` 已配置（生成绝对 URL 需要）。
- **与 `navigation.instant` 不兼容**：本仓库未启用该 feature，保持现状即可。
- `languages[].theme.language` 逐语言覆盖有效（日志："Overriding 'zh' config 'theme.language' with 'zh'"）。
- `languages[].site_name` / `site_description` 等逐语言覆盖也受支持。
- `validation.anchors: warn`：坏锚点从 INFO 升级为 WARNING（实测），可被 `--strict` 拦截。
  当前日文文档无坏锚点，开启是安全的。

## 3. 构建与验证

```bash
pip install -r tools/docgen/requirements.txt
mkdocs build --strict          # 必须 0 warning
mkdocs serve                   # 浏览器：/ = 日文，/zh/ = 中文（页头语言切换）
```

通过时的日志形态（参考）：

```
INFO - mkdocs_static_i18n: Building 'ja' documentation to directory: .../site
INFO - mkdocs_static_i18n: Building 'zh' documentation to directory: .../site/zh
INFO - mkdocs_static_i18n: Overriding 'zh' config 'theme.language' with 'zh'
INFO - mkdocs_static_i18n: Translated N navigation elements to 'zh'
```

## 4. nav_translations 起步表

- 键 = **日文侧 nav 的标题文本**（显式标题如 `デモ:`；路径式条目用页面 H1，如
  `吉里吉里Z について`——已实测可用）。
- 规则：**翻译到哪个页面，就把它 nav 链条上的标题补上**；没翻的页面留着日文标题不影响构建。
- 起步（顶层 + 主要分组）：

```yaml
nav_translations:
  ホーム: 首页
  デモ: 演示
  吉里吉里Z: 吉里吉里Z
  TJS2言語仕様: TJS2 语言规范
  クラスリファレンス: 类参考
  仕様書: 规格文档
  周辺情報: 周边信息
  # 吉里吉里Z 分组
  入門・運用: 入门与运维
  サブシステム: 子系统
  付属ツール: 附带工具
  定数一覧: 常量列表
  # TJS2 分组
  概要: 概要
  構文: 语法
  言語要素: 语言要素
  内部仕様: 内部实现
  # 类参考分组
  吉里吉里Z コアクラス: 吉里吉里Z 核心类
  吉里吉里Z 3D機能クラス: 吉里吉里Z 3D 功能类
  吉里吉里Z 管理機能クラス: 吉里吉里Z 管理功能类
  TJS2 組み込みクラス・型: TJS2 内置类与类型
  プラグイン拡張クラス: 插件扩展类
  # 周边信息分组
  ユーザー向け情報: 面向用户的信息
  TJS2 で利用する機能: TJS2 可用的功能
  ツール: 工具
  本体 (exe) 変更者向け情報: 面向本体（exe）修改者的信息
  ライセンス: 许可证
```

## 5. 已验证的行为（翻译时的预期）

| 行为 | 结论 |
|---|---|
| URL 结构 | 日文 `/…`，中文 `/zh/…`；未翻译页在中文站内**原地回退**（`/zh/…` 下显示日文内容，导航标题为中文） |
| 相对链接 | **与日文原文同写法**即可：先找 `zh/` 译文，找不到自动回退到日文根（含 `_assets` 图片）。不必加 `../` |
| 死链检查 | `mkdocs build --strict` 会校验译文页里的相对链接（找不到 → warning → 失败） |
| 锚点 | 默认 `validation.anchors: warn` 后坏锚点会导致 `--strict` 失败；`reference/` 的 API 标题保持原文即锚点稳定 |
| 语言切换 | 页头自动出现 日本語 / 简体中文；`<link rel="alternate">` 指向同页的对应语言版本 |
| 搜索 | 共享一个索引，按当前页面语言过滤（插件自动处理） |
| 回退页"编辑"链接 | 本仓库未启用 `content.action.edit`，无影响 |

## 6. 已知限制与注意

- **`doc/reference/**` 是生成物**（`tools/docgen/tjsdoc.py` 从 `doc/manual/*.manual.tjs` 生成）。
  `doc/zh/reference/**` 不会被生成器触碰，但日文侧重新生成后译文会漂移。重生成后执行：
  `python3 .claude/skills/krkrz-doc-zh/scripts/check_pair.py --all` 检查结构，再人工补译变更。
- **图内日文**（`doc/_assets/`）不处理，属已知限制；后续可单独实现截图替换。
- 未安装 i18n 插件时直接 `mkdocs build`，`doc/zh/` 会被当成普通页面（CI 始终装 requirements，无影响）。
- GitHub Pages 工作流无需改动：`doc/**` 与 `mkdocs.yml` 变更都会触发；requirements 变更也已在其
  `paths` 中。

## 7. 落地路径（上游 / fork 策略）

本仓库是 wamsoft/krkrz_dev 的 fork。两种做法：

1. **fork 内落地（推荐先做）**：`mkdocs.yml` + `requirements.txt` + `doc/zh/` 都留在 fork，
   部署自己的 Pages。上游不受影响，中文文档先跑起来。
2. **向上游提 PR**：先只提基础设施（requirements + mkdocs.yml + `doc/zh/index.md` + 少量试点页），
   说明「日文站外观变化仅多一个 Home tab」。后续翻译按批 PR。

无论哪种，**先完成 §1–§3 并让 `--strict` 通过**再开始量产翻译。
