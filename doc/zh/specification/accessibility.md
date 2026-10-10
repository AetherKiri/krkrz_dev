# 无障碍 (屏幕阅读器) 支持设计 — 吉里吉里Z 接入

状态: **Phase A / B 已实现 (2026-10-04)**。输入框的字符、单词、行单位的朗读 (Elements 侧 Phase 5) 也已加入。已在 Windows (SDL3 / WINVER)、macOS、Linux 的实机上确认。下面的“使用方法”才是实际的入口。之后的章节是设计时的记录，细节与实现有出入 (差异列在“使用方法”之下)。Elements 侧的设计在 `external/elements/docs/accessibility.md` (本文档中称为“本体设计”)。本文档只处理 krkrz 侧的接入与 REPL / Agent 的扩展。路径以 `src/core/` 为起点。

使用指南: [朗读 (屏幕阅读器)](../guide/Accessibility.md)。可运行的示例在核心演示 `data/a11y`。

API 参考: [ElementsDialog](../reference/ElementsDialog.md) (`announce` / `setGameA11y` / `a11yLayers` 等)、[Agent](../reference/Agent.md) (`a11yTree` / `a11yLog` / `a11yAction`)、[Layer](../reference/Layer.md) (添加到 Layer 上的成员)。

## 使用方法 (已实现)

| 入口 | 内容 |
|---|---|
| 构建 | `KRKRZ_USE_A11Y` (桌面 = Windows / macOS / Linux 的常规构建默认为 ON)。链接 Elements 的 `elements_a11y_accesskit`，并定义 `KRKRZ_HAS_A11Y`。即使为 OFF，朗读树的获取 / 操作 / 朗读日志仍可使用 (只是不输出到 OS) |
| 窗口 | 在最初的 `PaintOverlay` (主窗口的设备) 时挂到主窗口上。SDL3 版是 `accesskit_host::attach_sdl`，WINVER 是向 HWND `attach` (两者都是 `SetWindowSubclass` / 显示后追加挂载)。在屏幕阅读器连接之前什么都不做 |
| 游戏本体的槽位 | 在打开通向 OS 的入口的时点放置 (常设)。位于对话框之下，模态对话框显示期间会隐藏。从一开始就放置空的 live region (status)，用 `announce` 改变其内容 (如果带文字的 live region 是之后才出现的，屏幕阅读器有时不会朗读) |
| 对话框 | `ElementsDialogManager` 的每个实例成为槽位。层叠顺序、模态、位置 (`present_scale` / `present_off_x/y`) 在 `PaintOverlay` 末尾同步。画面 JSON 的 `"a11y"` (本体设计 §4) 直接生效 |
| `ElementsDialog.announce(text[, assertive])` | 让它朗读 (最前面对话框的 live region。没有对话框时是游戏本体槽位的 live region)。assertive=true 是表示中断的指定 (朗读侧如何处理取决于屏幕阅读器)。连续传入相同的句子也会朗读。即使屏幕阅读器没有连接也接受 (连接后会传递最新状态) |
| `ElementsDialog.setGameA11y(nodes[, focus])` | 把游戏本体 (绘制在 Layer 上的选项、菜单、设置画面) 加入朗读树。参照下面的“游戏本体的节点” |
| `ElementsDialog.clearGameA11y()` | 移除游戏本体的所有节点 (槽位与 live region 保留) |
| `ElementsDialog.onGameA11yAction(id, action, arg)` | 接收对游戏本体节点的 AT 操作的事件 (在脚本中代入函数) |
| `ElementsDialog.a11yLayers` | 把主窗口的 Layer 自动加入朗读树 (默认 false)。参照下面的“Layer 的自动” |
| `ElementsDialog.a11yActive` | OS 的屏幕阅读器等是否已连接 (只读)。在屏幕阅读器首次查询树的时点变为真 (Windows 是在窗口位于前台 / 获得焦点时。刚启动后仍为假) |
| `ElementsDialog.onA11yActiveChanged(active)` | `a11yActive` 改变时被调用 (在脚本中代入函数。在绘制之外，WINVER 的静止画面中也会即时触发)。“如果已连接就朗读正文”的判定不做缓存，用这个或朗读前一刻的 `a11yActive` 进行 |
| `ElementsDialog.a11yMode` | `"auto"` (默认) / `"off"` (不输出到 OS) |
| `ElementsDialog.a11yLabel` | 朗读树的根 (窗口) 的名称。为空时采用最前面画面的名称 |
| `Agent.a11yTree()` | 朗读树 (JSON 字符串)。`{"dialogs":[{"index","screen","modal","tree"}],"game":{"hidden","tree"}}`。`game` 是游戏本体的槽位 (没有则为 `null`，`hidden` 表示是否隐藏在模态对话框之下) |
| `Agent.a11yLog([since])` | 朗读日志 `%[lines, next]`。仅在 REPL 运行时积累。announce 也会留在其中 |
| `Agent.a11yAction(node, action[, arg])` | 通过与屏幕阅读器相同的路径进行操作 (click / focus / increment / decrement / set_value)。从最前面的对话框开始查找，如果没有模态对话框，也会查找游戏本体的节点 |
| REPL | `.a11y` / `.a11ylog [N]` / `.a11ydo <node> <action> [arg]` / `.say <text>` (file / web / socket / console 共通) |

### 输入框

对话框的输入框 (`input_box` / `text_box`) 可以被屏幕阅读器按字符、单词、行单位朗读，也能跟随插入符的移动 (UIA 的 TextPattern / AT-SPI 的 Text、EditableText / macOS 的 AXSelectedTextRange、AXStringForRange)。也可以从屏幕阅读器移动插入符或选择范围。脚本侧不需要做任何事。

- 朗读日志中，值未改变而只有插入符移动时会输出 `[caret] x` (行末为 `(line end)`，末尾为 `(end)`)，进行选择时会输出 `[selected] 文字列`。
- 不处理 IME 转换中的字符串 (确定前)。转换中的字符与候选由 OS 的 IME 自身传给屏幕阅读器，如果应用侧也输出就会被读两遍。输入框持有的只有已确定的字符 (本体设计 §6.5)。
- 游戏本体的 `EditLayer` (`a11yLayers`) 与 `setGameA11y` 的 `text_input` 只朗读值，没有按字符单位的朗读。

### 游戏本体的节点 (`setGameA11y`)

绘制在 Layer 上的 UI 在 Elements 之外，因此由脚本传入节点表。每次调用都整体替换，差异由引擎本体计算。

```
ElementsDialog.onGameA11yAction = function(id, action, arg) {
    // action: "click" / "focus" / "increment" / "decrement" / "set_value" (arg が値)
    // focus を受けたら、 ゲーム側のフォーカスを動かして setGameA11y を呼び直す
};
ElementsDialog.setGameA11y([
    %[ id:"choices", role:"list", name:"選択肢" ],
    %[ id:"c1", role:"list_item", name:"北へ行く", parent:"choices", rect:[100,400,600,48] ],
    %[ id:"c2", role:"list_item", name:"南へ行く", parent:"choices", rect:[100,460,600,48] ],
    %[ id:"vol", role:"slider", name:"音量", value:"50%", num_value:50, num_min:0, num_max:100 ],
], "c1");
```

| 键 | 内容 |
|---|---|
| `id` | 必需。唯一的字符串。`Agent.a11yAction` / `.a11ydo` 也用这个 id 指定 |
| `role` | `button` / `toggle_button` / `check_box` / `radio_button` / `tab` / `menu_item` / `list` / `list_item` / `slider` / `spin_button` / `text_input` / `label` / `heading` / `image` / `status` / `group` (省略时为 group) |
| `name` / `value` / `description` | 朗读的名称 / 值 / 补充说明 |
| `states` | 数组或 `"focusable,checked"`。`focusable` / `disabled` / `checked` / `selected` / `expanded` / `read_only`。`focused` 由第 2 个参数决定 |
| `rect` | primary layer 的坐标 `[x, y, w, h]`。可省略 (省略的节点会成为包围子节点的矩形)。窗口的缩放与黑边 (letterbox) 由引擎本体换算 |
| `parent` | 父节点的 `id`。省略则为最顶层 |
| `num_value` / `num_min` / `num_max` / `num_step` | slider / spin_button 的数值 |

- 操作由角色决定。可按下的角色 (button / check_box / list_item …) 为 click，slider / spin_button 为 increment / decrement / set_value，text_input 为 set_value。它们都接受 focus，`disabled` 时只接受 focus。
- AT 操作在绘制之外到达 `onGameA11yAction` (无论来自哪个线程，都在主线程调用)。引擎本体不会自行移动焦点或值。由脚本改变游戏状态并重新调用 `setGameA11y`。
- 层叠顺序: 游戏本体的槽位在对话框之下。不过，在没有正在接收按键的对话框、且焦点在游戏侧时，会提升到最前面 (因为屏幕阅读器的焦点会采用最上面槽位的)。模态对话框显示期间会隐藏。
- 仅主窗口。

### Layer 的自动 (`a11yLayers`)

把 `ElementsDialog.a11yLayers` 设为 true 后，会遍历主窗口 primary layer 以下，把节点加入游戏本体的槽位。默认是 false (什么都不做则行为不变)。要更改默认为 true 时，请事先通知那些不使用这个功能、用 `setGameA11y` 自行组装的利用方。

会加入的内容:

- 进入焦点链的 Layer (`focusable` 且 `joinFocusChain`)。名称取 `hint`，角色为 button (`CheckBoxLayer` 为 check_box，`EditLayer` 为 text_input)
- 拥有 `a11yName` 或 `a11yRole` 的 Layer (无法获得焦点也可以。用于标题或说明文)
- 绘制 ElementsPanel 的 Layer。面板中的部件排列在其下，操作也会到达面板

不会加入的内容: `visible` 为 false 的 Layer 及其子级。`a11yHidden` 为真的 Layer 及其子级 (对自行通过 `setGameA11y` 加入的图层设置它)。

添加到 Layer 上使用的成员 (均为可选):

| 成员 | 内容 |
|---|---|
| `a11yName` / `a11yRole` / `a11yValue` / `a11yDescription` | 名称 / 角色 (与 `setGameA11y` 相同的名称) / 值 / 补充说明 |
| `a11yStates` | 数组或 `"checked,selected"`。`disabled` 也可以由 `enabled` 得出 |
| `a11yHidden` | 为真时连同子树一起移除 |
| `onA11yAction(action, arg)` | 接收 AT 的操作。返回 false 时也执行默认处理 |

- 默认处理: focus 为 `layer.focus()`，click 为先聚焦再发送 Enter 键 (可用按键操作的部件借此按下)。值的更改 (increment / set_value 等) 只能通过 `onA11yAction` 接收。
- 焦点: `window.focusedLayer`。不过，向 `setGameA11y` 传入了 focus 时以后者优先。
- 排列顺序: `setGameA11y` 的节点在前，自动加入的 Layer 在后 (按 Layer 的层叠顺序)。id 为 `layer:<Layer.name>` (同名时是 `#2`, `#3` …)。
- 读取频率: 最多 150ms 1 次 (焦点中的 Layer 改变时立即)。读取只发生在 AT 连接期间，或 REPL 正在获取朗读日志期间，且是在绘制之外 (continuous 事件) 进行。如果把 `a11y*` 做成 property 的 getter，请保持轻量。`Agent.a11yTree` / `Agent.a11yAction` 会当场重新读取。
- 在 WINVER 中，AT 连接期间为了这种重新读取，continuous 事件会持续运转 (空闲时也会发生)。

与设计时相比的更改:

- TJS 的入口没有做成新的 `Accessibility` 类，而是做成了既有 `ElementsDialog` 的静态成员 (与 `language` 等相同的形式)。
- WINVER 也不触碰 `TTVPWindowForm::Proc`，而是在之后对 HWND 进行子类化 (Elements 侧的 `accesskit_host::attach`)。
- 坐标: 把绘制面 (renderer 的 surface) 的坐标，按绘制面与窗口实际尺寸之比换算为 OS 的单位。macOS 是点 × `backingScaleFactor` (即使 SDL 的窗口不是高分辨率，只要 Retina 就是 2。Elements 的 `accesskit_host::native_scale`)，Linux 是窗口坐标。
- Phase B 的游戏本体 source 分成了 2 层。由脚本传入节点表的 `setGameA11y`，与自动读取 Layer 焦点链的 `a11yLayers` (包含 ElementsPanel)。Phase C 尚未着手。KAG3 的扩展 (下面的“KAG 联动”) 不进行 (因为方针是今后不再扩展 KAG3 本身。KAG 系作品由作品侧的脚本调用 `setGameA11y` / `announce` 来支持)。

确认 (Layer 的自动): 在 Windows (SDL3 / WINVER) / macOS / Linux 上，确认了焦点链的 Layer、`a11yName` / `a11yRole` 的覆盖、`a11yHidden` 与不显示内容的排除、ElementsPanel 的内容、与 `setGameA11y` 的并用 (排列顺序、focus 的优先)，以及来自 AT / `Agent.a11yAction` 的 click (Enter) 与 `onA11yAction`。

确认: SDL3 版 / WINVER 版都打开 `data/elements_gallery`，用 UI Automation 的外部客户端确认了树 (名称、角色、值、状态) 与 REPL 的 `.a11ydo` / `.say` / `.a11ylog`。游戏本体节点的树与坐标 (含 letterbox)、UIA 的 Invoke / SelectionItem.Select / RangeValue.SetValue → `onGameA11yAction`、模态显示期间隐藏、没有对话框时的 announce、WINVER 中绘制停止的画面上的操作，也同样得到了确认。

## 1. 现状 (调查结果)

- 没有无障碍、UIA、TTS 相关的代码。所有的 WndProc 都不处理 `WM_GETOBJECT`，而是转给 DefWindowProc。
- **Elements 的 UI 全部是离屏**绘制。
  - `ElementsDialog` 由 `tTVPElementsDialogManager` 按 z 顺序管理 `overlay_session`，并在 `PaintOverlay` (`common/visual/elements/ElementsDialogManager.cpp`) 中合成到游戏帧上。
  - `ElementsPanel` 绘制到 Layer 的位图上。
  - 例外只有 `showModalJson(json,title,w,h)`，它会创建专用的 OS 窗口 (SDL: `SDLElementsModalRunner.cpp`、WINVER: `WinElementsModalRunner.cpp` 的 `ModalWndProc`)。
- 连接到原生窗口的入口:
  - WINVER: `TTVPWindowForm::Proc` (`win32/environ/WindowFormUnit.cpp`) 会最先调用 `DeliverMessageToReceiver`。可以在这里捕获 `WM_GETOBJECT`。
  - SDL3: 在 `sdl3/environ/form.cpp` 中创建窗口。HWND 可以通过 `SDL_PROP_WINDOW_WIN32_HWND_POINTER` 获取 (同一文件中有先例)。macOS / Linux 用的属性尚未使用。
- 既有的内部结构观察 (introspection) 作为树的替代并不够用。
  - `Agent.dialogs()` / `Agent.dialogTree(i)` 使用 `overlay_session::list_widgets()`。返回的只是拥有 `id` 的控件的扁平 `(id,type,value)`，没有名称、矩形、层级。
  - 用本体设计的 `a11y_snapshot()` 替换。
- Layer 拥有由 `focusable` / `joinFocusChain` / `focused` / `hint` / `onFocus` 构成的完整焦点链。KAG 的 `ButtonLayer` / `MessageLayer` 的链接 / `CheckBoxLayer` / `EditLayer` 在使用它。这里作为 Phase B 的对象。
- REPL 在 `common/utils/REPL.cpp` 的 `tTVPReplThread::ProcessLine` 中，对 file / web / socket / console 各通道共通。`.dlg` / `.click` 通过重写为 `Agent.*` 的字符串实现。

## 2. 构成

```
             ┌──────────── tTVPAccessibility (新規, common/visual/accessibility/) ─────────────┐
 OS AT  ⇄  accesskit_host (Elements L3)                                                   │
             │  slot 0     : ゲーム本体 source (tTVPGameA11ySource: 場面名・Layer フォーカス連鎖) │
             │  slot 1..N  : ElementsDialogManager の各 overlay_session (z 順, modal 連動)      │
             └──────────────────────────────────────────────────────────────────────────────┘
 TJS:  Accessibility クラス (announce / mode / active / onActive)
 REPL: Agent.a11yTree / a11yLog / a11yAction, .a11y / .a11ylog / .say
```

- 让 `KRKRZ_USE_A11Y` (默认与 `KRKRZ_USE_ELEMENTS` 相同) 与 Elements 的 `ELEMENTS_A11Y_ACCESSKIT` 联动。LIB 变种与 NX 等中为 OFF。
- 即使为 OFF，只有 `Agent.a11yTree()` 能在 Elements 的 L0~L2 上运行 (可以在没有 AccessKit 的情况下验证)。

## 3. 连接到窗口

| 构建 | 连接 |
|---|---|
| SDL3 (Win / mac / Linux) | 在 `form.cpp` 中创建窗口后立即 `accesskit_host::attach_sdl(window)`。面向 Linux 时通过 `SDL_AppEvent` 的窗口事件通知 focus 与 bounds |
| WINVER | 在 `TTVPWindowForm::Proc` 中收到 `WM_GETOBJECT` 时调用 `on_wm_getobject()`。`WM_ACTIVATE` 时调用 `on_window_focus()`。不经由插件的 message receiver，而是在核心内直接处理 |
| `showModalJson` 的专用窗口 | Phase C。专用窗口也挂上另一个 `accesskit_host` (在 `run_modal` 侧使用与本体 Win32 / SDL 宿主相同的处理) |

- 主窗口可能有多个 (可以生成多个 `Window`)。因此 `accesskit_host` 按 Window 分别持有，Elements 的每个实例注册到“绘制该实例的 Window”的 host。
- 根节点的名称使用 `Window.caption`。

## 4. ElementsDialog 的 source 化 (`ElementsDialogManager`)

- 在实例的创建与销毁时调用 `add_source` / `remove_source`。z 顺序的替换、`modal`、`active` 改变时，同步 `set_modal` 与 z。
- 坐标: `PaintOverlay` 确定 surface 逻辑坐标的 `last_rect` 之后，立即用 surface → 客户端像素的变换调用 `set_transform`。这个变换与 `GetTextInputArea` 的 IME 用变换共享同一实现。
- 把 `overlay_session::set_a11y_dirty_callback` 连接到 `invalidate()`。
- `ElementsPanel` (绘制到 Layer) 在 Phase B 中处理。按照 Layer 的坐标与可见性，作为游戏本体 source 的子节点接上。

## 5. TJS API

```
class Accessibility  // static
{
  property mode;        // "auto"(既定: AT 接続時のみ) / "on" / "off"
  property active;      // read-only: OS の AT が接続中か
  property gameLabel;   // ゲーム本体ノードの名前 (場面名など)
  function announce(text, assertive=false, window=void);
  // event
  onActiveChanged(active);   // System.addEventListener 相当で受ける (TVPPostEvent)
}
```

- 写在 ElementsDialog 的 JSON / Dictionary 中的 `"a11y"` 键 (本体设计 §4.1)，什么都不做也会直接生效。
- `active` 为 false 时，`announce` 只向朗读日志记录，然后立即返回。

### KAG 联动 (opt-in 脚本) — 不进行

> 设计时的方案。由于方针变为今后不再扩展 KAG3，因此不放入 `script/KAG3`。KAG 系作品由作品侧的脚本把正文传给 `ElementsDialog.announce`，选项等用 `setGameA11y` 加入 (实际有作品是这样做的)。

不改变 KAG 本体的 .tjs。准备扩展 `system/A11yKAG.tjs`，用 `kag.a11y.messages = true` 启用。

- `MessageLayer` 显示完 1 行或 1 页后，把积累的字符串传给 `Accessibility.announce(name + "「" + text + "」")`。使用的是与积入 `HistoryLayer` 相同的字符串，因此处于去除了注音与标签的状态。
- 焦点移到选项 (链接) 上时，让其朗读该 `hint`。在 Phase B 中把 Layer 的链做成 source 后就会自动朗读，因此这是此前的临时措施。
- 有语音的行根据设置不朗读。`kag.a11y.skipVoiced`

## 6. REPL / Agent

既有的 `dialogTree` 原样保留。

| 追加 | 实现 |
|---|---|
| `Agent.a11yTree([window])` | 以本体设计 §5 形式的 Dictionary 返回 Window 的 host 持有的合成树 (全部槽位)。指定 `index` 时只返回该 dialog 的 source |
| `Agent.a11yLog([since])` | 朗读日志 (focus、value 的变化、live、announce 的近似 1 行) 的数组 |
| `Agent.a11yAction(nodeId, action[, arg])` | 通过与 AT 的动作相同的路径 (`accesskit_host` → `source::perform`) 执行 |
| `.a11y` / `.a11ylog` / `.say <text>` | 添加到 `ProcessLine` 的重写块，并补充到帮助行。可在 file / web / socket / console 的所有通道中使用 |
| web `/a11y`、SSE `/sub/a11y` | `ReplWebServer` 的原生路由。panel 系的 UI 与 elements_console 的 A11y 标签页共享树显示与朗读日志显示 |

`Agent.a11yAction` 与 `Agent.dialogClick` 不同，不经过按键合成直接执行。因此可以验证 AT 的操作路径本身。

## 7. 阶段

| Phase | 内容 |
|---|---|
| A (已完成) | 连接到 SDL3 / WINVER 的主窗口、ElementsDialog 的 source 化、TJS 的入口 (`ElementsDialog` 的静态成员)、REPL 的追加 |
| B (已完成) | 游戏本体的 source (`setGameA11y`，以及读取 Layer 焦点链 / `hint` / `focusedLayer` / `ElementsPanel` 的 `a11yLayers`)。不进行 KAG 扩展脚本 |
| C | `showModalJson` 的专用窗口、多个 Window (macOS / Linux 实机确认已与 A / B 一起完成) |

输入框的字符、单词、行单位的朗读已在 Elements 侧 (本体设计 §6.5) 完成。方针是不处理 IME 的转换中字符串 (上面的“输入框”)。剩下的是 Phase C。索引在 umbrella 的 `TODO.md`。
