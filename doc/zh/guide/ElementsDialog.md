# 对话框

## 关于对话框

吉里吉里Z 内置了这样一种机制：根据用 JSON / Dictionary 描述的布局，显示包含按钮、复选框、文本输入等的对话框。在 TJS 中通过 [ElementsDialog](../reference/ElementsDialog.md) 类使用 (旧名 `Dialog`。因为它是个容易与游戏侧脚本类名冲突的通用名，所以被改名了)。

该对话框通过引入 [Elements](https://github.com/wamsoft/elements) (基于 ThorVG 的 C++ GUI 库) 实现。与依赖平台的原生对话框 (Win32 的 WIN32Dialog 等) 不同，它的特点是 SDL3 构建与 Windows 原生 (D3D11) 构建都能从相同的 JSON 定义显示外观相同的对话框。只需传入用 JSON / JSONC (带注释的 JSON) 描述的布局，布局计算、绘制、输入处理都由引擎侧完成。

该机制以不依赖 Windows 标准 GUI 的跨平台 UI 为目的，设计上主要着眼于 SDL3 构建中的使用，但在 WINVER (Windows 原生) 构建中也同样运行。

## 显示模式

对话框有只显示 1 个画面的“单发对话框”，以及包含多个画面迁移的“流程”。两者分别都有模态 (在关闭之前阻塞 TJS 处理) 与非模态 (叠加在游戏画面上显示，不停止主循环) 之分。

### 单发对话框

| 显示模式 | TJS API | 行为 |
|---|---|---|
| 非模态 (覆盖层) | [ElementsDialog.showJson](../reference/ElementsDialog.md#showjson) / [showFile](../reference/ElementsDialog.md#showfile) | 在既有游戏画面上绘制对话框，不停止主循环。值的变化与按钮点击会通过 [onAction](../reference/ElementsDialog.md#onaction) 逐次通知。用 [close](../reference/ElementsDialog.md#close) 结束。 |
| 阻塞式模态 (独立窗口) | [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) (传递 title / w / h) | 打开新的原生窗口，在关闭之前阻塞。关闭后返回 `%[ action, values ]` 形式的 Dictionary。 |
| 阻塞式模态 (覆盖层) | [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) (仅 JSON 1 个参数) | 不创建独立窗口，而是叠加在既有游戏画面上显示，在关闭之前阻塞。返回值与独立窗口版相同。 |
| 宿主图层绘制 (面板) | [ElementsPanel](../reference/ElementsPanel.md) ( `new ElementsPanel(layer)` + [showFile](../reference/ElementsPanel.md#showfile) 等 ) | 不叠加，而是**绘制到指定的 Layer 的位图**。z 顺序、转场、进入截图、输入归属都遵循图层的机制，因此可用于 HUD 或作为游戏画面一部分的 UI。事件 / 变量 API 与 ElementsDialog 同形。 |

`showModalJson` / `showModalFile` 的返回值是以下形式。

```tjs
%[
    action: <閉じた button の id (Esc / × は "")>,
    values: %[ <id>: <値>, ... ]   // state widget の最終値マップ
]
```

模态中 [onAction](../reference/ElementsDialog.md#onaction) 也会触发，但关闭对话框的只有 JSON 侧指定了 `"close_on_click": true` 的按钮 (以及通过 Esc / × 的中断)。

### 多画面流程

也可以定义依次切换多个画面的“流程”。在清单 (或 Dictionary) 中声明多个画面与画面间的迁移。

| 显示模式 | TJS API | 行为 |
|---|---|---|
| 阻塞 (覆盖层) | [ElementsDialog.showFlow](../reference/ElementsDialog.md#showflow) / [showFlowScreens](../reference/ElementsDialog.md#showflowscreens) | 以覆盖层执行多个画面的迁移。阻塞 TJS 直到流程结束，最后返回关闭画面的 `%[ action, values ]`。 |
| 非模态 (常驻) | [ElementsDialog.startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens) | 以非阻塞方式开始相同的流程定义 (常驻于游戏画面)。用 `close` 关闭，teardown (后处理) 是否完成用 [active](../reference/ElementsDialog.md#active) 判断。 |

画面切换的时机触发 [onScreen](../reference/ElementsDialog.md#onscreen) / [onScreenLeave](../reference/ElementsDialog.md#onscreenleave)，控件操作触发 [onAction](../reference/ElementsDialog.md#onaction)。

#### 画面切换特效 ( fade / universal )

将画面 JSON 的 `transitions` 条目写成 object 形式，即可声明画面切换时的过渡特效。由于是 CPU 合成，在 SDL / WINVER / GL 的所有 DrawDevice 中行为一致。

```jsonc
"transitions": {
    "next": { "target": "s2", "effect": "fade", "duration": 300 },
    "back": { "target": "<back>", "effect": "universal",
              "rule": "rule.png", "vague": 64, "duration": 500 }
}
```

| 键 | 含义 |
|---|---|
| `effect` | `"fade"` = 交叉淡入淡出 / `"universal"` = 基于 rule 图像的通用转场。不支持的名称会输出警告日志 + 立即切换 |
| `duration` | 所需时间 ms。省略 / 0 时为 200ms |
| `rule` | universal 的 rule 图像 (灰度。值越小的像素越早切换到下一画面)。解析顺序 = 从声明迁移的画面起的相对路径 → Storages 路径 → autopath 检索 |
| `vague` | 边界模糊宽度 (rule 值刻度 0~255，默认 64) |

#### 与退场 ( exit ) 演出的协调

给元素的 `"animate"` 加上 `"on": "exit"` 后，画面关闭 / 迁移时会先播放退场演出再迁移。除了 close_on_click / Esc 等画面内触发之外，TJS 发起的 [close](../reference/ElementsDialog.md#close) 也会触发 (在演出完成后关闭，流程执行中不解析 transitions，而是随整个流程一起结束)。

想在 GPU (OpenGL 绘制) 侧进行同等转场时，请参阅 [3D 图形系统](Graphic3DSystem.md) 的 Canvas 转场绘制。

## 布局密度的指定 ( gap / style )

默认是 fit-to-content (匹配内容的尺寸) + 紧密堆叠，因此省略显式指定时会呈现拥挤的外观。可以不排列 spacer，而用以下方式集中指定密度。

```jsonc
{
    "style": { "font_scale": 1.25, "row_height": 44, "tile_gap": 8, "padding": 24 },
    "content": { "type": "vtile", "gap": 12, "children": [ ... ] }
}
```

- `vtile` / `htile` 的 `"gap"` — 子元素间的空隙 px (等价于自动插入 spacer)
- top-level `"style"` — 将 `font_scale` (默认字体倍率) / `tile_gap` (未指定 gap 的 tile 的默认值) / `row_height` (button 系 / input_box 的默认最小高度) / `padding` (content 整体的外侧留白) 作为未指定值的默认值应用

任何一项省略时，都与以往完全一致。

## 矩形文本 ( text_area )

字幕或台词窗口这类“将正文排入固定矩形并进行字符送进”的用途，请使用 `text_area`。

```jsonc
{ "type": "text_area",
  "text": "…本文…",
  "size": 36,                    // px
  "font": "Noto Sans JP",        // 省略時はテーマ既定
  "align": "left",               // left / center / right
  "line_spacing": 12,            // 行間追加 px
  "count_var": "sub_count" }     // 文字送り ( -1 = 全部 )
```

- 折行、行首行尾避头尾、字符送进的单位与 [Layer.drawShapedTextArea](../reference/Layer.md#drawshapedtextarea) 是**相同的逻辑**。相同正文、相同宽度、相同字体 / 大小时**换行位置一致** (即使在图层绘制与 Elements 之间分别输出字幕，行的排布也不会错位)。
- 给 `"count_var"` 指定变量名后，宿主只需用 [setVar](../reference/ElementsDialog.md#setvar) 写入数值，字符送进就会推进。**折行是先对全文确定后再应用 count**，因此送进过程中不会重排。计数的单位是与 [Layer.shapedTextCount](../reference/Layer.md#shapedtextcount) 相同的簇 (连字、组合字符、emoji ZWJ 序列算作 1)。
- 正文的替换用 `"text_var"` / `"text_id"`，从列表中显示指定编号用 `"text_list_id"` + `"index_var"`，均与 `label` 的规则相同。
- 将各行固定的 `"index"` 与行间共享的 `"index_offset_var"` (起始位置) 组合起来，就形成“N 行的窗口”。宿主只需通过 [setVar](../reference/ElementsDialog.md#setvar) **移动起始位置的 1 个变量就能滚动列表**，无需为每行准备变量 (列表数据本身的替换用 `"text_list_var"`)。
- 原有的 `text_box` 为兼容而原样保留 (朴素按词折行、无避头尾)。既有画面的换行位置不会改变。

⚠ 以绝对坐标放置 (使用 `floating` 的 `"at"`) 时，请在 top-level 显式指定 `"size": [w, h]`。省略的话，对话框会缩小到内容的最小尺寸，绝对坐标落到其外部，什么都显示不出来。

## 拖拽操作 ( drag_at_var / onDrag )

在控件中写 `"drag_at_var"` 后，拖拽中的位置会以 `"x,y"` 形式写入该变量。在 canvas 的子元素的 `"at_var"` 中插入相同变量，**图像就会跟随拖拽**而无需经过 TJS (在引擎内完结，因此不受事件配送延迟的影响)。可移动范围可以用 `"drag_bounds": [x, y, w, h]` 限制。

想在 TJS 侧进行“在哪里松开”之类的判断时，请为该控件指定 `"drag_events": true` 并实现 [onDrag](../reference/ElementsDialog.md#ondrag)。

```tjs
class DragDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function DragDialog() { super.ElementsDialog(); }
    function onDrag(e) {
        // e.id / e.phase ( "begin" | "move" | "end" ) / e.x / e.y
        // e.dx / e.dy ( 前回からの差分 ) / e.startX / e.startY / e.modifiers
        if (e.phase == "end") {
            // 離した位置で当たり判定を取る、といった判断はここで
        }
    }
}
```

坐标是画面 JSON 中写的坐标系。堆积的 `"move"` 会被合并为最新的 1 条 (`"begin"` / `"end"` 不会被合并)。**只是让外观跟随的话不需要 onDrag**，`drag_at_var` + `at_var` 的组合就足够了。

## 列表与滚动条 ( list / atlas_scrollbar )

排列成行的画面用 `"type": "list"` 构建。它**将 1 行的模板按行数复制**，行位置、命中判定、hover、选择、“数据不足行的善后”都由控件侧承担。TJS 侧只需灌入数据。

```tjs
var layout = %[
  "content" => %[
    "type" => "list", "id" => "files",
    "rows" => 6, "row_size" => [676, 36], "pitch" => [0, 40],
    "index_offset_var" => "top", "count_var" => "n",
    "select_var" => "sel", "row_hover_var" => "rhov#index",
    "row" => %[ "type" => "label", "id" => "row#index",
                "text_list_var" => "items" ]
  ]
];
dlg.showDict(layout);
dlg.setVar("items", "file 0\nfile 1\nfile 2");   // 一覧データ
dlg.setVar("n", "3");                             // 総件数
```

- 字符串中的 `#index` 会被替换为行号 (`"id": "row#index"` → `row0` / `row1` …)。拥有 `text_list_var` 的元素会自动插入行号与起始位置，因此模板中只写 1 行就能成为列表
- 点击行时 [onAction](../reference/ElementsDialog.md#onaction) 会以 **`payload` = 数据 index** 触发 (行内有按钮时以按钮为优先)
- 传递 `count_var` 后，没有数据的行其绘制与命中判定都会消失
- hover / 选择的颜色，可以用每行的标志变量 (`row_hover_var` / `row_select_var` 用 `"visible_var"` 接收)，也可以用 [onVar](../reference/ElementsDialog.md#onvar) 拾取 `hover_var` / `select_var` 后替换宿主侧的图层，两种方式都能构建

滚动条只需在 `"type": "atlas_scrollbar"` 中插入**相同的 `index_offset_var`**。滑块的长度与“可见行数 ÷ 总件数”成比例，连滑块拖拽、点击槽翻页、滚轮都内置其中 (正文放在 `scroller` 上的画面，用 `scroller` 的 `pos_var` 就足够了)。

## 变量的读写与变化通知 ( setVar / getVar / onVar )

画面 JSON 的变量挂在一棵 store 上，不仅可以用 [setVar](../reference/ElementsDialog.md#setvar) 写入，还可以用 [getVar](../reference/ElementsDialog.md#getvar) 读出。能读的不只是自己写入的值 — `"vars_on_hover"` / `"vars_on_focus"`、slider 的 `"value_var"`、`"drag_at_var"`、列表的 `"index_offset_var"` 等**画面侧写入的值也在同一个 store**，因此可以原样读取。

想在变化的那一刻得知时，请实现 [onVar](../reference/ElementsDialog.md#onvar)。

```tjs
class ListDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function ListDialog() { super.ElementsDialog(); }
    function onVar(name, value) {
        if (name == "row_hover") {
            // カーソルが乗っている行が変わった → ホスト側のレイヤを差し替える
            highlightRow(+value);
        }
    }
}
```

这样就能构建“**图像由宿主侧的图层负责，只有命中判定交给对话框**”的构成。例如单张图像太大、无法装进 atlas 的列表画面，可以在对话框中只排列透明按钮以接收 hover，显示则由游戏侧的图层进行，即这种分工。

- 通知会延迟 1 帧，同一变量的连续变化会被合并为最新的 1 条。需要“当前值”时请读取 [getVar](../reference/ElementsDialog.md#getvar)
- **只有实现了 onVar 的对话框才是观测对象** (未实现则不会产生开销)。想收窄接收的变量时，请在 [watchVars](../reference/ElementsDialog.md#watchvars) 中排列名称 — 因为 hover 联动变量与拖拽位置每帧都会被改写
- 画面上有哪些变量，可以用 [listVars](../reference/ElementsDialog.md#listvars) 列出 (变量名、当前值、引用它的控件的 id 与种类)。可用于调试面板或画面 JSON 的验证

## 跨画面保持值 ( shared_vars )

变量 store **会按画面重新创建**，因此浏览设置标签页时，“刚才拖动过的滑块”会回到默认值。想继承的值请在画面 JSON 的 top-level 声明。

```jsonc
"shared_vars": ["cfg_*", "ui_lang"]
```

匹配的变量会与会话共享 store **双向**连接，构建画面时会用共享侧的值初始化 (与画面的 `"vars"` 默认值相比，共享侧优先)，以后每次变化都会写回共享侧。模式是完全匹配或末尾 `*` 的前缀匹配。**要携带哪些值由画面侧决定，因此不需要宿主侧的实现**。

写入游戏存档数据 / 加载后灌入是宿主的工作，因此只为此准备了入口。

```tjs
// セーブ
var cfg = ElementsDialog.getSharedVars();   // %[ "cfg_bgm" => "70", ... ]
// ロード
ElementsDialog.clearSharedVars();
foreach_dict_of(cfg, function(k, v) { ElementsDialog.setSharedVar(k, v); });
```

值以字符串形式进出。会进入共享侧的只有“作为变化写入”的值，控件的初始值 (`"initial"` / `"value"`) 不会送出 — 这是为了避免没人碰过的项目被首个打开画面的默认值固定下来。

## 用变量替换值与图像 ( value_var / image_var / 可替换图集 )

- **2 值开关** (`checkbox` / `toggle_button` / `slide_switch`) 可以通过 `"value_var"` 与变量 store 双向连接 (`""` / `"0"` / `"false"` = off)。点击会写回，用 [setVar](../reference/ElementsDialog.md#setvar) 状态会跟随 (跟随不会触发 `onAction`)。设置画面的 ON/OFF 无需宿主回调即可处理。
- **`image` 控件**可以通过 `"image_var"` 替换图像本身。变量的值会原样成为图像路径 (`"resources/x.png"` / `"mem://thumb_3"` / 空 = 不绘制)，因此像“存档列表翻页时缩略图变化”“CG 浏览器的图像翻页”这样的画面可以**无需重建**地写出。
- 想**整个图集**替换时，请在画面 JSON 中声明 `"atlases": { "cg": { "path": ..., "swappable": true } }`，然后用 [setAtlasImage](../reference/ElementsDialog.md#setatlasimage) 替换。控件不会重新创建，因此布局与焦点都会保留。**替换目标必须具有相同的矩形划分** (frames / rect 不会改变，因此图像位置错开就会显示别的图像)。可替换的图集名可以用 [swappableAtlases](../reference/ElementsDialog.md#swappableatlases) 确认。
- **图集即使关闭画面也不会被释放。** 已解码的图像以“路径 + 倍率”为键缓存，切换画面后也会一直被持有 (这是为了避免长时间游玩导致堆碎片化后取不到大的连续区域、解码失败而组建出没有图像的画面)。持有量可以用 [atlasCacheStats](../reference/ElementsDialog.md#atlascachestats) 读取，在场景分界 (标题 → 正篇等) 处调用 [trimAtlasCache](../reference/ElementsDialog.md#trimatlascache) 即可释放。⚠ **当前显示的画面正在使用的图集由于仍有引用，不会被释放** — 请在关闭画面之后调用。要更改预算本身的话，用 [atlasCacheBudget](../reference/ElementsDialog.md#atlascachebudget)。

## 非模态的多个同时显示与焦点

非模态 (覆盖层) 面板的配置用画面 JSON 的 top-level `"align"` / `"margin"` 指定，配置与缩放的基准区域用 top-level `"base"` 选择 — `"window"` (默认，以窗口全面为基准) / `"content"` (以游戏图像的显示区域为基准。像字幕窗口那样想跟随游戏图像时)。缩放会跟随窗口 (或显示区域) 相对于游戏基准面的比例，因此在全屏等情况下会与游戏以相同比率放大。对于以与游戏画面不同分辨率制作 UI 的作品 (游戏画面 640x400 / UI 1920x1080 等)，将 author 基准面的大小设置到 [ElementsDialog.baseSize](../reference/ElementsDialog.md#basesize) 后，缩放的分母就会变成它，也不会被游戏侧基准面大小的更改所牵连。

非模态对话框 ([showJson](../reference/ElementsDialog.md#showjson) / [startFlow](../reference/ElementsDialog.md#startflow) 系) 作为带 z-order 的实例列表管理，可以同时显示多个。鼠标从最前面开始命中测试，键盘 / 手柄会送达持有焦点的实例 (优先 z-order 末尾)。叠加模态对话框时，下面的实例保持绘制不变，只有输入被阻塞。

非模态开始系 ([startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens)) 有 `grabFocus` 参数，指定为假时会作为“不获取焦点的常驻 HUD”运行。利用它可以防止常驻 UI 连游戏的热键都吞掉。

非模态下，只消费 Elements 侧实际处理过的键，未处理的键会放行给游戏 (handled pass-through)，因此可以实现这样的共存: 菜单保持打开的同时，用游戏本体的热键打开另一个对话框。

### 输入的配送优先顺序与宿主热键

输入按以下优先顺序配送。

1. **最高层热键** ([System.registerHotKey](../reference/System.md#registerhotkey)) — 事件泵的入口。是**模态显示中也有效**的唯一层 (WINVER / SDL3 系构建双方均可运行)
2. **模态对话框** — 独占全部输入 (不向下、也不向游戏放行)
3. **宿主热键** ([registerHotKey](../reference/ElementsDialog.md#registerhotkey)) — 注册的键不会交给对话框，而是直接前往 [Window.onKeyDown](../reference/Window.md#onkeydown) 等
4. **持有焦点的非模态面板** — 接收键 / 手柄，只放行未处理的部分
5. **游戏 / 图层** — 未消费输入的落脚点

单发显示系 ([showJson](../reference/ElementsDialog.md#showjson) / showFile / showDict) 可以通过第 3 个参数 `modal` 指定“非模态 + 有焦点” (`showJson(json, true, false)`)。包含 slider 或 picker 的操作面板以这种形式显示时，可以用手柄的十字键 / A 按钮或键盘操作控件，同时面板不使用的键会流向游戏。在此基础上，用 registerHotKey 确保 ESC (场景返回) 或 PageUp/Down (画面切换) 这类“宿主必须接收的键”，是常规做法 (实例: `data/demolib/demo_common.tjs` 的 DemoShell)。

- 热键在文本输入控件中有插入符期间默认被抑制 (`duringTextInput = true` 可在输入中仍启用)
- 模态显示中热键也无效 (不会夺走确认对话框的 ESC = cancel)
- 鼠标按钮 (VK_RBUTTON 等) 也可以注册，可用于规避全屏透明 HUD 拾取右键而关闭的问题
- 想在最高层热键侧的回调中分支为“模态出现期间什么都不做”时，请查看 [ElementsDialog.modalActive](../reference/ElementsDialog.md#modalactive) (有无模态实例。不包含不取焦点的常驻覆盖层)

### 输入绑定与 named action

在 `"input"` 块的 `"bindings"` 中，可以为键 / 手柄 / 鼠标 / 滚轮分配**命名动作 (named action)**。`"accept"` / `"cancel"` / `"nav_up"` … 这样的**内置名会在对话框内处理**，因此不会到达 TJS。只有写了内置以外的任意名称时，该输入才会通知给宿主。

```jsonc
"input": { "bindings": [
    { "wheel": "up",   "action": "prev_page" },   // 任意名 = ホストへ通知
    { "key": "escape", "action": "cancel" } ] }   // 組込名 = ダイアログ内で処理
```

通知通过 [onAction](../reference/ElementsDialog.md#onaction) 接收，但 **`id` 固定为 `"<action>"`，赋予的名称会进入 `payload`**。

```tjs
function onAction(id, payload) {
    if (id == "<action>") {
        switch (payload) {
        case "prev_page": /* ホイール上で前ページ */ break;
        }
    }
}
```

如果以为 `id` 会传入自己赋予的名称而编写代码，就会**只有该输入默默无反应**，很难发现原因，请注意。

## 最小用例

在继承 [Dialog](../reference/ElementsDialog.md) 的类中实现 [onAction](../reference/ElementsDialog.md#onaction)，传入 JSON 布局并显示。

```tjs
class TestDialog extends ElementsDialog {
    // 明示コンストラクタで super を呼ぶこと ( 省略するとイベントが届かない )
    function TestDialog() { super.ElementsDialog(); }
    function onAction(id, payload) {
        switch (id) {
        case "ok":     System.inform("OK!");  close(); break;
        case "cancel": close(); break;
        }
    }
}

var json = @"
{
    // hspacer で 560 幅を確保 (JSONC コメント可)
    'size': [ 560, 200 ],
    'content': {
        'type': 'vtile',
        'children': [
            { 'type': 'hspacer', 'size': 560 },
            { 'type': 'label', 'text': 'Hello, Elements!' },
            { 'type': 'htile', 'children': [
                { 'type': 'button', 'id': 'ok',     'text': 'OK',     'close_on_click': true },
                { 'type': 'button', 'id': 'cancel', 'text': 'Cancel', 'close_on_click': true }
            ]}
        ]
    }
}";

var dlg = new TestDialog();
dlg.showJson(json);             // 非モーダル
// var r = dlg.showModalJson(json, "Title", 560, 200);   // 独立ウィンドウ
// var r = dlg.showModalJson(json);                       // ゲーム画面オーバーレイ
```

按钮、输入框等控件在 JSON 中如何描述的列表，请参阅 [Dialog](../reference/ElementsDialog.md) 类参考文档。

## 字体的注册

对话框绘制所用的字体会经由 krkrz 的 Storages (包括 XP3) 读取。要从脚本显式注册，请使用 [ElementsDialog.registerFont](../reference/ElementsDialog.md#registerfont) / [ElementsDialog.registerFontDir](../reference/ElementsDialog.md#registerfontdir)；确认、覆盖默认字体家族请使用 [ElementsDialog.defaultFontFamily](../reference/ElementsDialog.md#defaultfontfamily) 属性。

引擎侧也会在启动时自动扫描并注册资源路径下的 `.ttf` / `.otf` (从文件名推测 family / weight / slant / stretch)。

复选框的 ✓ 或 selection_menu 的 ▼ 等图标字形，不是用正文字体，而是用图标字体 `elements_basic.ttf` (随附于 `resource/`) 绘制的。引擎会自动注册，因此通常无需留意，但在替换资源的配置中去掉这个字体的话，就会变成“框会出现，但 ✓ 不出现”的状态。

### 可变字体 ( 带字重指定的注册 )

在 `registerFont` 的路径后加上 `"#tag=val"` 后缀，即可将可变字体的轴实例注册为别名。画面 JSON 侧只需 `"font": "MyFont-Medium"` 这样的名称，实体可以集中到 1 个可变字体上。在控件的 `"font"` 中直接写 `"MyFont#wght=700"` 的指定也是相同写法。

```tjs
ElementsDialog.registerFont("MyFont", "fonts/MyFont-VF.ttf");                   // 素の VF ( 無指定 = wght=400 )
ElementsDialog.registerFont("MyFont-Medium", "fonts/MyFont-VF.ttf#wght=500");   // 別名 = 軸インスタンス
```

### 语言联动字体替换 ( 多语言 UI )

对于日语 / 繁体字 / 简体字这样按文字系统使用不同字体的 UI，预先在 [ElementsDialog.fontLanguages](../reference/ElementsDialog.md#fontlanguages) 中设置语言→家族的替换表后，就会与 [ElementsDialog.language](../reference/ElementsDialog.md#language) 的切换联动，在字体解析时替换家族 (可以用符合显示语言的地区字形绘制共有码点的汉字)。表也可以在画面 JSON 的 top-level `"font_languages"` 中声明，想固定特定控件的语言时，请指定控件的 `"locale"`。

## 朗读 ( 屏幕阅读器 )

当前显示的画面对 OS 的屏幕阅读器可以直接朗读。名称无法自动确定的部件 (只有图像的按钮等) 用画面 JSON 的 `"a11y"` 键补充。详情请参阅 [朗读 (屏幕阅读器)](Accessibility.md)。

## 构建配置

对话框功能可在以 `KRKRZ_USE_ELEMENTS=ON` (默认) 构建的引擎中使用。同时支持 SDL3 构建与 WINVER (Windows 原生 / D3D11) 构建。以 `KRKRZ_USE_ELEMENTS=OFF` 构建时，[ElementsDialog](../reference/ElementsDialog.md) / [ElementsPanel](../reference/ElementsPanel.md) 类不会被注册，对话框相关代码会从链接中排除，可执行文件体积减小。

## 整体图景与设计方针

层结构 (elements / elements_modal / krkrz 本体 / 游戏侧) 与
“**UI 的处理在画面数据侧完结，宿主只负责连接**”这一方针的
说明在 [Elements UI 机制的整体图景](../topics/core/elements.md) 中。
不清楚该修改哪一层时，请先阅读那里。

## 相关 API

- [ElementsDialog](../reference/ElementsDialog.md) — TJS 绑定类
- [ElementsPanel](../reference/ElementsPanel.md) — 绘制到宿主图层的面板 (事件 / 变量 API 同形)
- [ElementsDialog.showJson](../reference/ElementsDialog.md#showjson) / [showFile](../reference/ElementsDialog.md#showfile) — 非模态
- [ElementsDialog.showModalJson](../reference/ElementsDialog.md#showmodaljson) / [showModalFile](../reference/ElementsDialog.md#showmodalfile) — 模态
- [ElementsDialog.showFlow](../reference/ElementsDialog.md#showflow) / [showFlowScreens](../reference/ElementsDialog.md#showflowscreens) — 阻塞式流程
- [ElementsDialog.startFlow](../reference/ElementsDialog.md#startflow) / [startFlowScreens](../reference/ElementsDialog.md#startflowscreens) — 非模态 (常驻) 流程
- [ElementsDialog.onAction](../reference/ElementsDialog.md#onaction) / [onScreen](../reference/ElementsDialog.md#onscreen) / [onScreenLeave](../reference/ElementsDialog.md#onscreenleave) / [onDrag](../reference/ElementsDialog.md#ondrag) — 事件
- [ElementsDialog.active](../reference/ElementsDialog.md#active) — 非模态的 teardown 完成判定 / [modalActive](../reference/ElementsDialog.md#modalactive) — 是否处于模态显示中
- [ElementsDialog.registerHotKey](../reference/ElementsDialog.md#registerhotkey) — 宿主热键 (绕过对话框) / [System.registerHotKey](../reference/System.md#registerhotkey) — 最高层热键 (模态中也有效)
- [ElementsDialog.baseSize](../reference/ElementsDialog.md#basesize) — UI 的 author 基准面大小 / [renderScale](../reference/ElementsDialog.md#renderscale) — 绘制密度
- [ElementsDialog.registerFont](../reference/ElementsDialog.md#registerfont) / [registerFontDir](../reference/ElementsDialog.md#registerfontdir) / [defaultFontFamily](../reference/ElementsDialog.md#defaultfontfamily) — 字体注册
- [ElementsDialog.setVar](../reference/ElementsDialog.md#setvar) / [getVar](../reference/ElementsDialog.md#getvar) / [listVars](../reference/ElementsDialog.md#listvars) / [onVar](../reference/ElementsDialog.md#onvar) / [watchVars](../reference/ElementsDialog.md#watchvars) — 每个画面的变量 store
- [ElementsDialog.getSharedVars](../reference/ElementsDialog.md#getsharedvars) / [setSharedVar](../reference/ElementsDialog.md#setsharedvar) / [clearSharedVars](../reference/ElementsDialog.md#clearsharedvars) — 跨画面的会话共享变量 (存档 / 读档用)
- [ElementsDialog.registerImage](../reference/ElementsDialog.md#registerimage) / [unregisterImage](../reference/ElementsDialog.md#unregisterimage) / [clearImages](../reference/ElementsDialog.md#clearimages) — 运行时图像 (`mem://`)
- [ElementsDialog.setAtlasImage](../reference/ElementsDialog.md#setatlasimage) / [swappableAtlases](../reference/ElementsDialog.md#swappableatlases) — 可替换图集
- [ElementsDialog.language](../reference/ElementsDialog.md#language) / [fontLanguages](../reference/ElementsDialog.md#fontlanguages) — i18n (显示语言与语言联动字体替换)
