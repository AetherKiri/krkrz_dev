# 朗读 (屏幕阅读器)

## 关于朗读

吉里吉里Z 的游戏画面可以通过 OS 的屏幕阅读器 (Windows 的讲述人、macOS 的 VoiceOver、Linux 的 Orca 等) 朗读。画面的部件的名称、角色、值、状态会传给 OS 的无障碍 API (UI Automation / NSAccessibility / AT-SPI)，因此看不见或看不清的人可以一边听朗读一边用键盘游玩。

支持的是桌面 (Windows / macOS / Linux) 的常规构建。SDL3 版和 Windows 原生 (WINVER) 版都可以运行。浏览器 (Web) 版没有这个入口。

传给屏幕阅读器的内容由以下 3 个来源汇集而成。

| 来源 | 什么都不做时是否会被朗读 | 使用的入口 |
|---|---|---|
| Elements 的对话框 / 面板 | 会被朗读 | 用画面 JSON 的 `"a11y"` 键补充 |
| 绘制在 Layer 上的 UI ( 选项、菜单、设置画面等 ) | 不会被朗读 | [ElementsDialog.setGameA11y](../reference/ElementsDialog.md#setgamea11y) 或 [ElementsDialog.a11yLayers](../reference/ElementsDialog.md#a11ylayers) |
| 任意文本 ( 正文、结果通知等 ) | — | [ElementsDialog.announce](../reference/ElementsDialog.md#announce) |

在屏幕阅读器连接之前不会做任何事。未连接期间的负载几乎没有。

可运行的示例在核心演示 `src/core/data/a11y` ( 画廊中的“読み上げ ( スクリーンリーダー )” ) 中。

## Elements 的对话框

用[对话框](ElementsDialog.md)显示的画面会被原样朗读。名称由按钮的文字、带标签的行、分组的标题等决定，角色 ( 按钮、复选框、滑块…… ) 由部件种类决定，值由当前显示的值决定，这些都由引擎本体自动判定。输入框可以按字符、单词、行的单位朗读，也能跟随插入符的移动。

自动判定不足的地方，通过给部件添加 `"a11y"` 键来补充。字符串表示名称，字典则进行更详细的指定。

```jsonc
{ "type": "sprite_button", "id": "btn_save", "a11y": "セーブ" }
{ "type": "slider", "id": "vol_bgm",
  "a11y": { "label_id": "cfg.bgm", "description_id": "cfg.bgm.help", "value_var": "vol_bgm_disp" } }
{ "type": "label", "text_var": "msg_body", "a11y": { "live": "polite" } }
{ "type": "image", "a11y": { "hidden": true } }
```

| 键 | 含义 |
|---|---|
| `label` / `label_id` | 名称 ( `_id` 从字符串表查找，因此会跟随语言切换 ) |
| `description` / `description_id` | 补充说明 |
| `role` | 角色覆盖 ( `"heading"` / `"status"` 等 ) |
| `value_var` | 持有要显示的值的变量名 |
| `live` | `"polite"` / `"assertive"`。`text_var` 变化时会朗读 |
| `hidden` | 把部件连同子级一起从朗读中排除 ( 装饰性图片等 ) |

在画面的最顶层放置 `"a11y": { "title": "…" }`，进入该画面时就会以该名称被朗读。

只有图形的按钮 ( `sprite_button` / `atlas_*` ) 没有文字，请用 `"a11y"` 为它们添加名称。

## 让绘制在 Layer 上的 UI 被朗读

绘制在 Layer 上的 UI 位于 Elements 之外，什么都不做的话不会被朗读。让它被朗读的方法有 2 种，也可以并用。

| 方法 | 适合的场景 | 工作量 |
|---|---|---|
| [a11yLayers](../reference/ElementsDialog.md#a11ylayers) | 通过 Layer 的焦点链 ( `focusable` ) 操作的 UI。按钮逐个用 Layer 制作的情况 | 小。只要设为真就能加入，通过给 Layer 添加成员来补充 |
| [setGameA11y](../reference/ElementsDialog.md#setgamea11y) | 在 1 个 Layer 上绘制多个项目的 UI ( 选项、列表、菜单 )，以及自行管理焦点的 UI | 用脚本制作节点表并传入 |

### 自动加入焦点链上的 Layer ( a11yLayers )

```tjs
ElementsDialog.a11yLayers = true;
```

这样，进入焦点链的 Layer ( `focusable` 且 `joinFocusChain` ) 就会被加入朗读树。名称取 [hint](../reference/Layer.md#hint)，角色为按钮。焦点遵循 [Window.focusedLayer](../reference/Window.md#focusedlayer)。

在屏幕阅读器中执行“按下”时，引擎本体先把焦点移到该 Layer，然后发送 Enter 键。只要做成可以用 Enter 按下的结构，其他什么都不需要。

朗读方式可以通过给 Layer 添加成员来改变。

```tjs
class AutoModeButton extends Layer
{
    var a11yRole = "check_box";   // クラスで持たせるときは var で宣言する
    var checked = false;          // check_box は checked メンバから状態を読む
    // ...
}

heading.a11yName = "セーブとロード";   // フォーカスできない見出しも載る
heading.a11yRole = "heading";
deco.a11yHidden  = true;               // 飾りは子ごと外す
```

| 成员 | 内容 |
|---|---|
| `a11yName` / `a11yRole` | 名称 / 角色。只要拥有其中之一，无法获得焦点的 Layer 也会被加入 |
| `a11yValue` / `a11yDescription` | 值 / 补充说明 |
| `a11yStates` | 数组或 `"checked,selected"` 形式的状态 |
| `a11yHidden` | 为真时连同子级一起排除 |
| `onA11yAction(action, arg)` | 接收来自屏幕阅读器的操作。返回 false 时也执行默认处理 |

持有值的部件 ( 滑块等 ) 的增减没有默认处理。请用 `onA11yAction` 接收。

```tjs
class VolumeSlider extends Layer
{
    var a11yRole = "slider";
    var value = 50;
    property a11yValue { getter() { return value + "%"; } }

    function onA11yAction(action, arg)
    {
        switch (action) {
        case "increment": setValue(value + 10); return true;
        case "decrement": setValue(value - 10); return true;
        case "set_value": setValue(+arg); return true;
        }
        return false;   // focus は既定の処理 ( focus() ) に任せる
    }
    // ...
}
```

重新朗读最多每 150ms 1 次 ( 焦点变化时立即进行 )。把 `a11yValue` 等做成 property 时请保持轻量。Layer 的 `name` 会成为朗读树的 id ( `layer:<name>` )，加上它可以在确认时更方便地指认。

### 传入节点表 ( setGameA11y )

像选项那样在 1 个 Layer 上绘制多个项目时，由脚本制作每个项目的节点并传入。

```tjs
function pushChoices()
{
    var nodes = [ %[ id:"choices", role:"list", name:"どうする?" ] ];
    for (var i = 0; i < choices.count; i++) {
        nodes.add(%[
            id:"choice" + i, role:"list_item", name:choices[i], parent:"choices",
            states:(i == current) ? "focusable,selected" : "focusable",
            rect:[ 100, 400 + i * 60, 600, 48 ]   // primary layer の座標
        ]);
    }
    // 第 2 引数はフォーカスを置くノード。選択肢を操作している間だけ渡す
    ElementsDialog.setGameA11y(nodes, choiceLayer.focused ? "choice" + current : void);
}

ElementsDialog.onGameA11yAction = function(id, action, arg) {
    var i = +id.substr(6);                       // "choice<N>"
    if (action == "focus") { current = i; redraw(); pushChoices(); }
    else if (action == "click") { current = i; decide(); }
} incontextof this;
```

- 每次调用时表会整体替换。差异由引擎本体计算，因此每次选择变化时传入完整内容也没有问题。
- 引擎本体自身不会移动焦点或值。当从屏幕阅读器收到 `focus` / `click` 时，请在改变游戏状态之后重新调用 `setGameA11y`。
- 添加 `rect` 后，屏幕阅读器会用边框指示该位置 ( 讲述人的蓝色边框等 )。窗口的缩放和黑边 ( letterbox ) 由引擎本体换算。
- 传入第 2 个参数 `focus` 期间，屏幕阅读器的焦点会固定到该节点。与 `a11yLayers` 并用时，请只在操作自己的 UI 期间传入。
- 对于自行加入的 Layer，请设置 `a11yHidden = true`，避免与 `a11yLayers` 的自动加入重复。
- 游戏本体的节点排列在对话框之下。模态对话框显示期间会被隐藏。

可用的角色、状态、键的列表请参照 [setGameA11y](../reference/ElementsDialog.md#setgamea11y)。

## 让任意文本被朗读 ( announce )

```tjs
ElementsDialog.announce("セーブしました");
ElementsDialog.announce("体力が残りわずかです", true);   // 割り込み
```

用于朗读那些不会因焦点移动而被朗读的内容 ( 正文、操作结果、状态变化 )。会进入最前面的对话框，如果没有对话框则进入游戏本体的朗读栏 ( live region )。连续传入相同的文本也会每次都朗读。

想根据屏幕阅读器是否已连接来切换是否朗读正文时，请在即将朗读前查看 [a11yActive](../reference/ElementsDialog.md#a11yactive)，或用 [onA11yActiveChanged](../reference/ElementsDialog.md#ona11yactivechanged) 接收。在 Windows 上，直到窗口位于前台之前都不会变为已连接状态。

KAG3 中没有加入朗读扩展。KAG 系作品需要在作品侧的脚本中把消息正文传给 `announce`，并用 `setGameA11y` 加入选项来支持。

## 确认方法

- **实际听**: 启动游戏后再启动讲述人 ( Windows 为 Win + Ctrl + Enter ) 等屏幕阅读器，并让窗口位于前台。
- **用 REPL 查看**: 用 `-replfile` 等启动 REPL 后，即使没有屏幕阅读器也能确认 ( [REPL](../topics/core/repl.md) )。

| 命令 | 内容 |
|---|---|
| `.a11y` | 以 JSON 显示朗读树 ( 屏幕阅读器可见的内容 ) ( [Agent.a11yTree](../reference/Agent.md#a11ytree) ) |
| `.a11ylog [N]` | 朗读日志。把大致会被读成什么逐行显示 ( [Agent.a11yLog](../reference/Agent.md#a11ylog) ) |
| `.a11ydo <node> <action> [arg]` | 通过与屏幕阅读器相同的路径进行操作 ( [Agent.a11yAction](../reference/Agent.md#a11yaction) ) |
| `.say <text>` | announce |

朗读日志会变成如下行。

```
[focus] 南へ行く, list item, selected
[polite] 「南へ行く」を選びました
[focus] 音量, slider, 50%
[value] 音量, 60%
```

## 注意事项

- `setGameA11y` / `a11yLayers` / `onGameA11yAction` 等是**对整个类生效**的设置。离开场景时请用 `clearGameA11y()` / `a11yLayers = false` 恢复。
- 对象只有主窗口。`showModalJson` 打开的专用窗口以及第 2 个以后的 `Window` 目前尚不支持。
- 输入框转换中 ( 用 IME 确定之前 ) 的文字不会由应用侧输出。转换中的文字和候选由 OS 的 IME 自身传给屏幕阅读器。输入框持有的只有已确定的文字。
- 把构建选项 `KRKRZ_USE_A11Y` ( 桌面常规构建默认为 ON ) 设为 OFF 后，就不会再输出到 OS。REPL 中的确认入口仍会保留。
- 运行时不想输出到 OS 时，设置 `ElementsDialog.a11yMode = "off"`。

完整的规格和设计时的记录在[无障碍 ( 屏幕阅读器 ) 支持](../specification/accessibility.md)中。

## 相关 API

- [ElementsDialog](../reference/ElementsDialog.md): `announce` / `a11yActive` / `onA11yActiveChanged` / `a11yMode` / `a11yLabel` / `setGameA11y` / `clearGameA11y` / `onGameA11yAction` / `a11yLayers`
- [Layer](../reference/Layer.md): 添加到 Layer 上的朗读用成员 ( 类说明 )
- [Agent](../reference/Agent.md): `a11yTree` / `a11yLog` / `a11yAction`
