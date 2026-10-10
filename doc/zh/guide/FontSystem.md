# 字体系统

这是吉里吉里Z 中围绕字体 (注册、名称解析、绘制、检索) 的综合指南。
从字体的准备到注册步骤、各 API 的区分使用，都在这里汇总。

## 整体结构

```
  フォントファイル (.ttf/.otf/.ttc)
    │  ①exe 埋め込み (resource/)      ②data 外だし + fonts.json (宣言・遅延)
    │  ③実行時登録 (Font.addFont 等)  ④システムフォント (Windows GDI)
    ▼
  ┌───────────────────────────────────────────────┐
  │ FontSystem (名前→ストレージ対応・遅延ロード)  │←─ fonts.json
  │ FontStream (共有オンメモリバッファ / 1フォント1部) │
  └───────────────┬───────────────────────────────┘
                  ▼
  ┌───────────────────────────────────────────────┐
  │ glyphware (統一フォントエンジン:               │
  │  FreeType + HarfBuzz + BiDi / レジストリ・検索) │
  └───┬───────────────┬───────────────┬───────────┘
      ▼               ▼               ▼
  Layer.drawText   Layer.draw     ThorVG テキスト
  (ラスタライザ     GlyphwareText  (Elements UI /
   3種切替)        (シェイピング)   layerExVector)
```

- 字体的字节数据只在 **`FontStream` 共享缓冲区中加载 1 个字体 1 份**，
  drawText、Elements UI、layerExVector、插件全部共享同一个
  缓冲区 (支持 XP3 内字体、内存中)。
- 字形生成、文本整形、元数据检索都集中到统一字体引擎
  **glyphware**。传统的 GDI / FreeType 光栅化器也为
  兼容而原样保留。

## 光栅化器

用于生成 `Layer.drawText` 字符图像的引擎可以通过 [Font.rasterizer](../reference/Font.md#rasterizer)
(静态属性) 切换。

| 值 | Windows 原生版 (WINVER) | SDL 版等 |
|---|---|---|
| 0 | FreeType | FreeType **(默认)** |
| 1 | GDI **(默认)** | glyphware |
| 2 | glyphware | - |

- 默认值保持与以往兼容 (WINVER=GDI / 其他=FreeType)。
- **glyphware 光栅化器**在保持与 classic 的布局兼容 (字格步进、阴影、描边、
  下划线/删除线、VS15/16 等) 的同时，支持回退链、彩色 emoji、
  合成 bold/italic。已知差异: 即使指定关闭抗锯齿，
  也始终以 AA 绘制 (`font.hinting` / `font.antialiased` 被忽略)。

## 字体的准备与注册步骤

### ① exe 内嵌 (resource/)

放在引擎 `resource/` 文件夹中的 `.ttf/.otf` 会在构建时内嵌到
可执行文件中，启动时即可使用。这里不是由游戏侧增补字体之处，而是引擎默认
字体的存放位置。内嵌字体也可以通过存储名
`resource://./ファイル名` 访问。

**默认内嵌的只有 Roboto (拉丁字母) 与 elements_basic (Elements 的图标)**。
日语 (Noto Sans JP 4.3MB) 与 emoji (Noto Emoji 1.9MB) 占
可执行文件体积的大部分，因此默认不内嵌。日语可以在游戏侧
声明到 `fonts.json` 中 (②)，或使用 OS 的字体 (④)。想与以前一样
内嵌时，请在构建时传递 `-DKRKRZ_EMBED_BUNDLED_FONTS=ON`
(可执行文件会增大约 6.2MB)。要排除任意文件，请使用
`-DKRKRZ_RESOURCE_EXCLUDE="ファイル名;ファイル名"`。

引擎随附的演示 (`src/core/data`) 将这 2 款字体放在 `data/fonts/` 中，
并在 `fonts.json` 中声明。它可以作为游戏使用相同字体时的示例。

### ② data 外置 + fonts.json (推荐)

较大的字体 (彩色 emoji、CJK 变体等) 放在 data 文件夹中，
并**在 `fonts.json` 中声明**。启动时只注册名称，实际文件
**在首次使用时延迟加载**，因此不影响启动时间与内存。

```json
{
  "version": 1,
  "fonts": [
    { "file": "fonts/notocoloremoji.ttf",
      "family": "Noto Color Emoji",
      "subfamily": "Regular",
      "aliases": ["Noto Color Emoji Regular"],
      "weight": 400,
      "scripts": ["Zsye"],
      "flags": ["emoji", "color"],
      "ranges": [[9728, 9983], [126976, 129791]] }
  ]
}
```

- `fonts.json` 放在 **data 文件夹 (项目根目录) 正下方**。
- 除 `file` 以外全部可选。可以声明 `subfamily` / `fullName` / `postScriptName` /
  `weight` (100-900) / `width` (1-9) / `italic` / `faceIndex` / `languages` /
  `aliases` / `flags` (`emoji` `color` `monospace`) / `ranges` (收录码点
  区间)。
- **可变字体**可以通过 `instance` (fvar named instance 名) 或 `axes`
  (直接写轴值) 声明“名称 = 特定的轴设置”。同一个文件可以用不同别名 +
  不同轴声明多个 (见下文“可变字体”节)。

```json
{ "file": "myfont.ttf", "family": "MyFont SemiBold", "instance": "SemiBold" }
{ "file": "myfont.ttf", "family": "MyFont Narrow",   "axes": { "wdth": 75 } }
```
- 声明的 `scripts` / `ranges` / 样式会被 [Font.queryFonts](../reference/Font.md#queryfonts)
  **在不打开字体文件的情况下**用于检索。
- 可以用**生成工具**自动生成 (需要 `pip install fonttools`):

```
python tools/fontgen/gen_fonts_json.py \
    --fonts-dir <データ>/fonts --root <データ> --out <データ>/fonts.json
```

生成器会把 family 变为纯粹的 family 名，并将 classic 光栅化器的 face 名规则
(“family subfamily” 拼接，例 "Noto Color Emoji Regular") 输出到 `aliases`，
因此两种名称都可以解析。

随附示例: 核心演示的 `src/core/data/fonts` 中，除 Noto Color Emoji 之外
还随附了用于 RTL 的 **Noto Sans Arabic / Noto Sans Hebrew**
(包括 SDL 版在内的所有平台上，阿拉伯语/希伯来语显示一致)。其他
文字系统也从 Noto 家族 (https://notofonts.github.io/) 获取的话，
外观会与内嵌的 Noto Sans JP / Roboto 保持一致
(候选: Noto Sans Thai / Devanagari / KR / SC / TC 等。详情见
`src/core/data/fonts/README.md`)。

### ③ 运行时注册 (脚本)

- [Font.addFont](../reference/Font.md#addfont)`(storage)` — 立即加载字体文件
  并注册，返回收录的 face 名数组。
- [Font.registerFontFile](../reference/Font.md#registerfontfile)`(storage[, family])`
  — 指定 `family` 时会成为**不打开文件的延迟注册** (相当于 fonts.json 的
  1 个条目)。省略时与 addFont 一样是立即加载。

```tjs
Font.addFont("mygame_font.ttf");                       // 即時ロード
Font.registerFontFile("fonts/big_cjk.ttf", "MyCJK");   // 遅延 (初回使用時に読む)
```

### ④ 系统字体 (已安装到 OS 的字体)

仅凭**字体名**即可使用已安装到 OS 的字体。

- **WINVER** 使用 GDI 的名称解析。在 glyphware 系路径 (rasterizer=2 /
  drawShapedText / Elements) 中，`"メイリオ"` `"MS PGothic"` 等名称也会
  原样解析，TTC 的 face 编号也会被正确选择。用 `addFont`
  插件注册的内嵌字体也同样可以按名称使用。
- **SDL 版等**在启动时只从 OS 的字体列表中注册**名称与文件的对应关系**，
  实际文件在首次使用时读取 (与 fonts.json 相同的延迟加载)。
  列表的获取来源，Windows 是 DirectWrite，Linux 是 fontconfig
  (macOS / Android 不支持)。相同名称存在于 fonts.json 或运行时注册中时，
  优先使用后者。不希望发布物的外观受运行环境影响时，
  可以用启动选项 `-systemfont=no` 禁用。

## 字体名的规则与解析顺序

写在 `Font.face` 或 `fontKey` 中的名称 (以逗号分隔构成**回退链**)
按以下顺序解析:

1. **fonts.json / registerFontFile 的声明名** (family / aliases) → 存储
2. **存储路径** (`fonts/foo.ttf`、`resource://./…` 等实际存在的路径)
3. **OS 的字体名** (WINVER 为 GDI，包括 addFont 注册的部分。SDL 版等为
   启动时注册的 OS 字体列表)
4. 无法解析的名称回退到默认 face

### 默认字体

未指定字体名时的默认字体，如果有启动选项 `-deffont` 则使用它，
否则从与运行环境语言匹配的候选中选择**实际可用者** (SDL 版等)。
日语环境的候选是 `fonts.json` 的 Noto Sans JP，接着是
`Yu Gothic UI` / `メイリオ` / `MS ゴシック` / `ヒラギノ` / `IPA` / `Noto Sans CJK JP`
等 OS 字体。如果启动时这些全部不可用，则之后在
`fonts.json` 或 `Font.registerFontFile` 注册候选名称的时刻重新选择。
WINVER 一如既往是 GDI 的默认字体。

### 任何字体都没有的字符

回退链中任何字体都没有的字符，会用链中拥有该字符的字体以
**U+FFFD (�)** 绘制。连 U+FFFD 也没有时用 `?` (随附的 Roboto
拥有 U+FFFD)。换行、零宽字符、变体选择符等不可见字符
不会绘制任何内容。`Layer.drawText` (FreeType / glyphware 光栅化器)、
`drawShapedText` 系、竖排、Elements 通用 (GDI 光栅化器仍为 GDI 的
替代显示)。

请注意，classic (FreeType) 的 face 名是 “family subfamily” 拼接
(例 "Noto Sans JP Regular")。fonts.json 生成器会把拼接名输出到 alias，
因此通常两种写法都可以工作。

## emoji

用 [Font.emojiMode](../reference/Font.md#emojimode) (0=禁用 / 1=单色 / 2=彩色)
选择 emoji 字形的处理方式。

- 彩色 emoji 字体 (默认 "Noto Color Emoji") 以在 fonts.json 中进行外置声明为
  前提。未配置时会自动回退到随附的单色 emoji (Noto Emoji)
  (不会变成豆腐块)。
- 默认字体名可以通过 `Font.emojiFaceName` / `Font.colorEmojiFaceName` 更改。
- WINVER 的默认光栅化器 (GDI) 没有 emoji 字形，因此需设为
  `Font.rasterizer = 0` (FreeType) 或 `= 2` (glyphware) 使用。
- 支持 VS15 (文本显示) / VS16 (emoji 显示) 的变体选择符。

## 字体检索与元数据

已注册的字体可以用 [Font.queryFonts](../reference/Font.md#queryfonts) 进行
丰富检索 (条件全部可省略，结果是按排名顺序的字典数组):

```tjs
// カラー絵文字フォントを探す
var r = Font.queryFonts(%[ containsText : "😀", color : 1 ]);
// 日本語を収録した太字を探す
var r = Font.queryFonts(%[ containsText : "あ", weight : 700 ]);
```

单个字体的 SFNT 元数据可以用 [Font.getFontInfo](../reference/Font.md#getfontinfo)
获取 (family / subfamily / weight / color 等)。在 fonts.json 中已声明的
信息无需打开字体即可应答。

## 可变字体 (可变轴)

拥有可变轴 (fvar) 的字体，可以从 TJS 的字体参数指定轴。
生效的只有 **glyphware 路径** — [Layer.drawShapedText](../reference/Layer.md#drawshapedtext)
系 (始终) 与 [Font.rasterizer](../reference/Font.md#rasterizer) = 2 时的
[Layer.drawText](../reference/Layer.md#drawtext) — ，旧的 FreeType / GDI
光栅化器会忽略它们 (启动后会警告 1 次)。

```tjs
Font.rasterizer = 2;                     // drawText で使う場合
layer.font.weight = 700;                 // wght 軸 (100-900、void で解除)
layer.font.variations = "wdth=87.5";     // 汎用軸指定 (複数は "wght=700,wdth=75")
var axes = Font.getVarAxes("MyFont");    // 利用できる軸の一覧
Font.defaultUseVarStyle = true;          // bold/italic を軸で表現 (オプトイン)
```

- [Font.weight](../reference/Font.md#weight) 作为 `wght` 轴生效，如果在
  [Font.variations](../reference/Font.md#variations) 中显式写了 `wght`，
  则以那里为优先。由于只会应用于回退链各 face **实际拥有的
  同名轴**，因此对于日语字体 + emoji 字体这类轴构成不同的链也
  是安全的。
- 通过 `fonts.json` 的 `instance` / `axes` 声明可以创建“名称 = 特定的轴设置”
  (上文 fonts.json 节)。只需指定名称即可使用带轴的字体，
  脚本侧无需接触 weight / variations。
- 将 [Font.defaultUseVarStyle](../reference/Font.md#defaultusevarstyle) 设为真时，
  对于能用轴 (wght=700 / slnt=-10 / ital=1) 表现 bold / italic 的字体，
  会用轴代替合成粗体 / 斜体 (默认为假)。
- 轴的查询可以通过 [Font.getVarAxes](../reference/Font.md#getvaraxes) /
  [Font.getFontInfo](../reference/Font.md#getfontinfo) (`axes` /
  `namedInstances`) 进行。
- **`#tag=val` 后缀写法**: 在字体名后追加 `#tag=val[,tag=val...]`，
  表示该名称所指字体的轴实例
  (例 `"MyFont#wght=700"`、`"MyFont#wght=700,wdth=75"`)。
  可统一用于 [Font.face](../reference/Font.md#face) 回退链的各元素、
  Elements 画面 JSON 的 `"font"` (label / text_area 均可用。折行计算也使用相同
  实例)。`Font.variations` 对整个字体 (链的
  全部 face) 生效，而这里则对链的**元素单位**生效。
- **未指定时的默认相当于 wght=400**: 以未指定 wght 的方式引用可变字体时，
  显示为 wght=400 而不是 fvar 的默认实例 (与 CSS 的
  font-weight 默认相同的规则)。默认值为 Thin 的 VF (Noto VF 等)，
  仅注册 1 个 VF，未指定时也能读作相当于 Regular。想更改默认值时，
  用 [Font.setDefaultVariations](../reference/Font.md#setdefaultvariations) 按
  名称单位注册 (显式指定、fonts.json 声明始终优先)。

## 多语言文字整形绘制 (glyphware)

`Layer.drawText` 一如既往是“逐 1 个字符的字格步进”，而
[Layer.drawShapedText](../reference/Layer.md#drawshapedtext) 则进行
基于 **HarfBuzz 整形 + BiDi** 的真正多语言单行绘制:

- 阿拉伯文字的连写、连字、字距调整，希伯来/阿拉伯语的右→左 (BiDi)
- 以码点为单位的回退链 (Font.face 逗号分隔)
- 彩色 emoji、合成 bold/italic、下划线/删除线、旋转 (angle)
- 绘制属性通过 1 个 [Font](../reference/Font.md) 对象传递
  (void = 图层自身的 font / 字符串 = 仅替换 face)

[Layer.drawShapedTextArea](../reference/Layer.md#drawshapedtextarea) 是
向矩形内的**简易折行绘制**。支持 `\n` 显式换行、英语等的按词
折行、日语的按字符折行 (附带行首/行末简易避头尾)、行对齐
(左/居中/右)、行距调整。

向 `count` 参数 (drawShapedText / drawShapedTextArea 共通) 传递 0 以上时，
可以只绘制开头的 count 个“字符”，用于打字机显示。这里的
“字符”是绘制时作为一块处理的**簇单位** (连字、组合字符、
emoji ZWJ 序列算作 1)，总数可以通过
[Layer.shapedTextCount](../reference/Layer.md#shapedtextcount) 获取。
因为先对全文完成整形/折行确定，再只绘制开头部分，所以显示中途
字形与折行位置不会变化 (重排)。

测量通过 [Layer.measureShapedText](../reference/Layer.md#measureshapedtext)
进行 (返回墨水边界与 ascent/descent、簇数)。

运行示例: 在核心演示库 (`src/core/data`) 的
“多言語シェイピング (glyphware)” 场景中，可以确认阿拉伯语/希伯来语 (RTL)、
BiDi 混排、emoji 混排、测量、矩形内折行、打字机显示 (RTL 混排文本的
自动播放 — RTL 区间按逻辑顺序逐 1 簇出现) 的实例。

## 竖排 (日语竖写)

[Layer.drawVerticalTextArea](../reference/Layer.md#drawverticaltextarea) 将
正文以**竖排 (竖写)** 排入矩形。它与横排的
`drawShapedTextArea` 是不同路径，按照日语排版规则 (JLReq) 的间隙量表
进行排版:

- 日文直立、西文/数字横倒，分开排版 (`orientation` 也可改为全部直立/全部横倒)
- 使用纵排字形 (`vert` / `vrt2`) 与纵向步进 (`vmtx` / `VORG`)，因此
  括号、长音符、句读点会变为纵向字形
- 标点符号 (句读点、括号类) 的收紧，日文与西文之间的间隙
- 行首行尾避头尾、挤入 / 挤出、行末对齐、标点符号悬挂 (可选)

列的长度为矩形的 height，列的步进为“字体大小 + lineSpacing”。
默认从右到左 (第 1 列位于矩形右端)，用 `verticalLr` 可以改为从左到右。
放不进矩形的列不会被绘制。字体指定 (`font` 参数) 与颜色的处理与
`drawShapedText` 共通，因此使用与横排相同的 Font 对象即可保持外观一致。

```tjs
var opt = %[ "hanging" => true, "letterSpacing" => 0.05 ];
// (x, y, width, height, text, color, font, count, lineSpacing, options)
var r = layer.drawVerticalTextArea(20, 20, 400, 560, text, 0x000000,
                                   font, -1, 6, opt);
// r.lines = 組んだ列数 / r.width = 使った幅 / r.count = 描いたクラスタ数
```

`options` 的全部键与默认值请参阅
[Layer.drawVerticalTextArea](../reference/Layer.md#drawverticaltextarea)
(`orientation` / `verticalLr` / `punctuation` / `latinGap` /
`hanging` / `justify` / `letterSpacing`)。

`count` 用于打字机显示，与横排一样**在对全文确定行分割之后**
再施加限制，因此中途不会重排。不过计数的单位是“被绘制的字符”，
不把西文的单词间空白计入，所以可能与
[Layer.shapedTextCount](../reference/Layer.md#shapedtextcount) 的值
不一致。总数请使用返回值的 `totalCount`。

不绘制、只想了解列数或所需宽度时，请使用
[Layer.measureVerticalTextArea](../reference/Layer.md#measureverticaltextarea)
(从参数中除去 x / y / color，返回值相同)。

**不支持**: 注音、纵中横、着重号、割注、字距分配、分栏、下划线 / 删除线、
[Font.angle](../reference/Font.md#angle)。目前的适用范围仅限正文排版。

运行示例: 在核心演示库 (`src/core/data`) 的
“縦組み (drawVerticalTextArea)” 场景中，可以确认正文排入、`options` 键切换
(悬挂 / 行末对齐 / 标点收紧 / 列步进方向 / 字距)、按 `orientation` 进行的
日欧排版区分、同一正文并排横排的对比、打字机显示 (count 限制) 的
实例。

## UI 系 (Elements) 与 layerExVector 的字体

- **Elements 对话框** ([对话框](ElementsDialog.md)) 的文本由 glyphware
  绘制。主题字体会自动注册内嵌字体 (默认是 Roboto)，
  其后面连接**引擎的默认字体** (上述“默认字体”: fonts.json 的
  声明字体或 OS 的日语字体，WINVER 为 GDI 的默认值) 作为最后的手段。
  不随附字体的配置也能显示日语，原因就在于此。
  追加字体通过
  `ElementsDialog.registerFont(family, storage[, weight, slant, stretch])` /
  `ElementsDialog.registerFontDir(dir)` 注册。可以直接传递存储路径 (XP3 内、
  包括 `resource://`)。`registerFontDir` 会返回**成功注册的
  数量**，因此可以用 `if (ElementsDialog.registerFontDir(dir) == 0) { ... }`
  检测“打包后一个字体都没有”的事故 (为 0 个时
  引擎也会输出警告日志)。要指向封入 XP3 的字体时，请像
  `"data.xp3>font/"` 这样**显式指定归档**
  (`addAutoPath` 的挂载用于文件检索，不能进行目录枚举)。
  直接传递 OS 路径 (`"D:/game/font/"`) 会得到 0 个。在多语言 UI 中
  想按显示语言自动切换字体 (JP/TC/SC 等) 时，请使用
  [ElementsDialog.fontLanguages](../reference/ElementsDialog.md#fontlanguages)
  (语言联动字体替换)
  (参照 [对话框](ElementsDialog.md) 的“语言联动字体替换”节)。
- 向矩形的排入也**共享折行逻辑**。对话框的
  `text_area` 控件经过与上述 `drawShapedTextArea` 相同的折行、
  行首行尾避头尾、簇单位的字符送进，因此相同正文、相同宽度时，
  图层绘制与 Elements 的**换行位置一致**
  (原有的 `text_box` 为兼容仍为朴素折行)。
- **richtext 插件** ([RichText](../reference/RichText.md)) 的排版是 minikin，
  但字体实体的获取与字形的光栅化会经过引擎本体的 glyphware。
  由于 face 与字体的字节序列和本体共享，因此与 `Layer.drawText` 及 Elements
  是**相同字体、相同外观** (只有使用可变字体的轴时，
  为了不污染共享 face 的状态，会打开专用的 face)。
- **layerExVector 插件** (`GdiPlus.loadFont(storage, name)`) 也共享相同的
  引擎。可以像 `resource://./roboto-regular.ttf` 这样指定
  本体内嵌字体或 fonts.json 的声明名。
- 无论哪条路径，同一字体都使用 FontStream 共享缓冲区的 1 份，
  因此在多个地方使用相同字体也不会增加内存。

## 从插件使用 (C++)

tp_stub 中公开了字体服务 API (`TVPCreateFontStream` / `TVPFontAcquireFace` /
`TVPFontShapeLine` / `TVPFontQueryFaces` 等)，插件也可以
利用共享缓冲区、字形供应、整形、检索。详情请参阅引擎
仓库的 `src/core/doc/FontEngine.md` (内部实现笔记)。

## 故障排查

- **字符显示为 � (U+FFFD)** — 任何地方都没有拥有该字符的字体。
  日语的话，请在 fonts.json 中声明日语字体，或使用 OS 的字体
  (请注意是否加了 `-systemfont=no`，以及 SDL 版的 macOS / Android
  无法使用 OS 字体这一点)。
- **指定了字体名却用默认字体绘制** — 名称未注册。
  请确认 `Font.getFontInfo(名前)` 是否返回 void，并使用 fonts.json 的声明名 /
  aliases，或 `Font.addFont` 返回值中的 face 名。
- **彩色 emoji 变成黑白** — 彩色 emoji 字体未配置 (fonts.json
  未声明) 时会回退到单色。可以用 `Font.queryFonts(%[color:1])`
  确认配置状况。
- **WINVER 中 emoji 不显示** — 默认光栅化器 (GDI) 不支持 emoji。
  请设为 `Font.rasterizer = 2` (或 0)。
- **"MS Gothic" 的宽度因路径而异** — FreeType 的名称解析在英文名 TTC 上
  有时会变成别的 face (PGothic)。使用实际 family 名
  (`"ＭＳ ゴシック"` 等) 的话，所有路径都会一致。

## 相关资料

- 参考文档: [Font](../reference/Font.md) / [Layer](../reference/Layer.md)
- [对话框 (Elements)](ElementsDialog.md)
- 已渲染字体: [FontMaker](FontMaker.md)
- 引擎内部实现 (面向开发者): `src/core/doc/FontEngine.md`
