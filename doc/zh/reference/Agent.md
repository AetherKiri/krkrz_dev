# Agent

!!! warning "实验中 ( 不在稳定性保证范围内 )"
    这个 API 的形式尚未固定。**有可能在无预告的情况下被更改或删除**
    ( 即使是非兼容更改，主版本号也不会提升 )。
    关于版本提升方式，请参阅 [版本管理](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)。

    这是用于开发、验证的 API。会随着 REPL / 调试窗口的完善而变化。

Agent 类是提供 agent 驱动 ( 测试 / 自动化 ) 用 API 的类。不能从这个类创建对象。与 System 一样，用 `Agent.click(...)` 这样的方式直接调用使用。

这个类提供用于注入输入事件 ( 鼠标 / 键 / 滚轮 )、捕获实际画面、观测与操作 Elements 对话框的功能。设想用于从外部 agent 驱动吉里吉里来验证运行情况。

这个类仅在 REPL 功能有效时 ( 命令行选项的 `-repl` / `-replfile` / `-replweb` 之一 ) 且启用了 Elements 的构建中可用 ( 关于 REPL 驱动请参阅 REPL.md )。

坐标全部以逻辑坐标指定。`shift` 参数是 Shift 状态的位标志，默认值为 0。`button` 参数为 0 = 左键 / 1 = 右键 / 2 = 中键。`vk` 参数是虚拟键码的数值。对话框系列的方法 ( `dialogs` / `dialogTree` / `closeDialog` / `closeAllDialogs` / `dialogClick` / `dialogFocus` / `text` ) 仅在启用了 Elements 的构建中运行。

## 成员列表

### 属性

- [ignoreRealMouse](#ignorerealmouse)

### 方法

- [mouseMove](#mousemove)
- [mouseDown](#mousedown)
- [mouseUp](#mouseup)
- [click](#click)
- [wheel](#wheel)
- [keyDown](#keydown)
- [keyUp](#keyup)
- [keyPress](#keypress)
- [text](#text)
- [dialogs](#dialogs)
- [imeStatus](#imestatus)
- [dialogTree](#dialogtree)
- [closeDialog](#closedialog)
- [closeAllDialogs](#closealldialogs)
- [dialogClick](#dialogclick)
- [dialogFocus](#dialogfocus)
- [captureScreen](#capturescreen)
- [lastCapture](#lastcapture)
- [a11yTree](#a11ytree)
- [a11yLog](#a11ylog)
- [a11yAction](#a11yaction)

---

### ignoreRealMouse

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

丢弃真实鼠标输入 ( 用于运行测试 )

设为真后，会**丢弃所有真实鼠标输入**，只放行从 Agent 注入的输入。
这是为了在自动测试中建立“输入全部由 Agent 发出”的前提。
即使人不小心动了指针，也不会污染测定。

加上启动选项 `-ignoremouse=yes` 后从一开始就有效。

hover 判定和光标参照会查看**虚拟光标位置**，
该位置会因 Agent 的注入而更新，因此启用后悬停和焦点仍能
照常工作。

⚠ 启用后**将无法用人手进行鼠标操作**。这是用于验证的。

---

### mouseMove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以逻辑坐标指定移动目标的 X 坐标。 |
| `y` | `&nbsp;` | 以逻辑坐标指定移动目标的 Y 坐标。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

鼠标移动的注入

对指定的逻辑坐标注入鼠标移动事件。

---

### mouseDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以逻辑坐标指定 X 坐标。 |
| `y` | `&nbsp;` | 以逻辑坐标指定 Y 坐标。 |
| `button` | `0` | 指定按钮编号 ( 0 = 左键 / 1 = 右键 / 2 = 中键 )。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

鼠标按钮按下的注入

对指定的逻辑坐标注入鼠标按钮按下事件。

---

### mouseUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以逻辑坐标指定 X 坐标。 |
| `y` | `&nbsp;` | 以逻辑坐标指定 Y 坐标。 |
| `button` | `0` | 指定按钮编号 ( 0 = 左键 / 1 = 右键 / 2 = 中键 )。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

鼠标按钮释放的注入

对指定的逻辑坐标注入鼠标按钮释放事件。

---

### click

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以逻辑坐标指定 X 坐标。 |
| `y` | `&nbsp;` | 以逻辑坐标指定 Y 坐标。 |
| `button` | `0` | 指定按钮编号 ( 0 = 左键 / 1 = 右键 / 2 = 中键 )。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

点击的注入

对指定的逻辑坐标，一次性注入 hover ( 移动 ) → 按下 → 释放，
再现 1 次点击操作。

---

### wheel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `delta` | `&nbsp;` | 指定旋转量 ( 1 个刻度 = 120 单位 )。 |
| `x` | `&nbsp;` | 以逻辑坐标指定 X 坐标。 |
| `y` | `&nbsp;` | 以逻辑坐标指定 Y 坐标。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

鼠标滚轮的注入

注入鼠标滚轮的旋转事件。

---

### keyDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vk` | `&nbsp;` | 指定虚拟键码 ( VK_* ) 的数值。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

按键按下的注入

注入按键按下事件。

---

### keyUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vk` | `&nbsp;` | 指定虚拟键码 ( VK_* ) 的数值。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

按键释放的注入

注入按键释放事件。

---

### keyPress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vk` | `&nbsp;` | 指定虚拟键码 ( VK_* ) 的数值。 |
| `shift` | `0` | 指定 Shift 状态的位标志。 |

**说明**

按键按下＋释放的注入

一次性注入按键的按下与释放，再现 1 次按键输入。

注入的**只是按键事件**。文字输入事件
( [Window.onKeyPress](Window.md#onkeypress) ) 通过 OS 的文本输入路径
产生，因此用这个方法不会产生。想在自动测试中输入字符时，
请使用 Elements 的输入框与 [Agent.text](Agent.md#text)。

---

### text

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 指定要发送的 UTF-8 文本。 |

**说明**

文本的发送

向活动的 Elements 对话框的输入框 ( input_box ) 发送 UTF-8 文本。
没有对象的输入框时会被忽略。

---

### dialogs

方法

**返回值**

返回对话框描述符的数组。各元素是
`%[index, modal, active, screen, focused, textFocus, x, y, w, h]` 形式的字典。

`textFocus` 表示“文本输入控件 ( input_box 等 ) 是否持有编辑焦点”，
它正是用于判断是否打开软键盘或 IME 的值本身。
可用于排查日语输入无法开始等问题。

`screen` 是流程 ( navigator ) 的当前画面名，单发对话框中为空。
`focused` 是焦点中的控件 id，但**只有在持有 id 追踪机制的
画面上才会填入**。并不是空就意味着没有焦点
( 想查看焦点有无时，请使用 `textFocus` 或
[Agent.dialogTree](Agent.md#dialogtree) )。

**说明**

获取活动对话框列表

返回当前活动的 Elements 对话框的描述符的数组。

**相关:** [Agent.dialogTree](Agent.md#dialogtree)

---

### imeStatus

方法

**返回值**

返回表示各窗口状态的字典的数组。主要项目如下。

`contextAttached` … 输入上下文是否已绑定。**若为伪则 IME 完全
无效**，[Window.imeMode](Window.md#imemode) 和半角/全角键都不起作用。
`conversion` 也会变成 0。

变为伪的情况是：有焦点的图层的
[imeMode](Layer.md#imemode) 为 `imDisable` 时 ( 默认值 )，
或者被外部用 `Window.resetImeContext(false)` 等切断时。
前者是**正常状态**，只要焦点移到 `imDisable` 以外的图层就会
自动重新绑定。明明已进入文本栏却仍为伪时，请怀疑是后者。

`hasFocus` … 这个窗口是否持有键盘焦点。为伪期间，IME 模式
本身不会被应用。

`keyTrapperIsSelf` … 为伪时，会应用 `trapKey` 为真的其他窗口的模式。

`imeMode` … 实际应用中的模式。`defaultImeMode` 是
[Window.imeMode](Window.md#imemode) 返回的默认值。

`overrideActive` … ElementsDialog 的文本栏是否握着 IME。
`contextForced` 表示是否为此重新绑定了输入上下文。

`areaX` / `areaY` / `areaW` / `areaH` / `areaCursor` … 为了让 IME 的转换 /
转换候选窗口靠近而最后交给宿主的矩形
( 窗口客户区坐标 px ) 与从该矩形左端算起的插入符相对 x。`areaValid` 为伪时，
文本栏没有编辑焦点。

此外还有 `visible` / `trapKeys` / `attentionPoint` / `controlImeState` /
`disabledBySelf` / `imeAvailable` / `open` / `savedImeMode` / `conversion` /
`sentence` / `index` / `isMain`。在 SDL3 构建中，
仅会填入 `textInputActive` 和上述 area 系列。

**说明**

获取 IME 状态

返回每个窗口的 IME 相关状态。用于排查“输入框中虽然出现了
插入符，却无法输入日文”这类故障。

仅在 Windows 原生 ( WINVER ) 构建中才会填入内容。其他构建中
总是返回空数组。

**相关:** [Agent.dialogs](Agent.md#dialogs)

---

### dialogTree

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 指定作为对象的对话框的索引。 |

**返回值**

返回控件的数组。各元素是 `%[id, type, value]`
形式的字典。

**说明**

获取对话框的控件列表

返回指定对话框中持有 id 的控件的列表。

**相关:** [Agent.dialogs](Agent.md#dialogs)

---

### closeDialog

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `0` | 指定作为对象的对话框的索引 ( 目前这个<br>参数会被忽略，总是关闭最前面的对话框 )。 |

**说明**

关闭对话框

关闭最前面的 Elements 对话框。

**相关:** [Agent.closeAllDialogs](Agent.md#closealldialogs)

---

### closeAllDialogs

方法

**说明**

关闭所有对话框

强制关闭所有的 Elements 对话框。

**相关:** [Agent.closeDialog](Agent.md#closedialog)

---

### dialogClick

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 指定作为对象的对话框的索引。 |
| `id` | `&nbsp;` | 指定要执行的控件的 id。 |

**说明**

执行对话框的控件

把焦点移动到指定对话框中持有该 id 的控件，并执行
( 相当于 Enter )。不需要指定坐标。

**相关:** [Agent.dialogFocus](Agent.md#dialogfocus)

---

### dialogFocus

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 指定作为对象的对话框的索引。 |
| `id` | `&nbsp;` | 指定要移动焦点的控件的 id。 |

**说明**

把焦点移动到对话框的控件

把焦点移动到指定对话框中持有该 id 的控件。

**相关:** [Agent.dialogClick](Agent.md#dialogclick)

---

### captureScreen

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定保存目标的统一存储路径 ( .png )。 |
| `x` | `0` | 指定保存范围的左端。 |
| `y` | `0` | 指定保存范围的上端。 |
| `w` | `0` | 指定保存范围的宽度 ( 0 表示整个画面 )。 |
| `h` | `0` | 指定保存范围的高度 ( 0 表示整个画面 )。 |

**返回值**

返回保存目标路径。

**说明**

把实际画面保存为 PNG

把下一帧的 present 也包含在内回读实际画面，建立把 PNG 保存到
path 的请求。可以用 x, y, w, h 指定保存范围，把 w / h 设为 0 时
则为整个画面。

**相关:** [System.captureScreen](System.md#capturescreen) / [Agent.lastCapture](Agent.md#lastcapture)

---

### lastCapture

方法

**返回值**

返回 `%[path, width, height, ok]` 形式的字典。

**说明**

获取最近的捕获结果

返回最近的 [Agent.captureScreen](Agent.md#capturescreen) 的结果。

**相关:** [Agent.captureScreen](Agent.md#capturescreen)

---

### a11yTree

方法

**返回值**

返回朗读树的 JSON 字符串。

**说明**

获取朗读树

以 JSON 字符串返回屏幕阅读器所看到的朗读树。
即使屏幕阅读器没有连接也能获取。

形如 `{"dialogs":[{"index","screen","modal","tree"}],"game":{"hidden","tree"}}`，
`dialogs` 是显示中的对话框，`game` 是游戏本体
( [ElementsDialog.setGameA11y](ElementsDialog.md#setgamea11y) /
[ElementsDialog.a11yLayers](ElementsDialog.md#a11ylayers) ) 的节点
( 没有则为 `null`。`hidden` 表示是否隐藏在模态对话框之下 )。
节点的 `id` 是画面 JSON 的 `"id"` 或 setGameA11y 的 id，没有的则变成
`"#<16 进制>"`。与 REPL 的 `.a11y` 相同。

**相关:** [Agent.a11yAction](Agent.md#a11yaction)

---

### a11yLog

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `since` | `0` | 返回这个位置以后的行 ( 省略时从开头开始 )。 |

**返回值**

返回 `%[lines, next]` 形式的字典。把 `next` 传给下一次的 since，就可以只获取增量。

**说明**

获取朗读日志

返回“屏幕阅读器大致会读成什么”逐行记录的日志。
行以 `[focus]` / `[value]` / `[state]` / `[caret]` / `[selected]` / `[polite]` 等
开头，[ElementsDialog.announce](ElementsDialog.md#announce) 也会保留在这里。
日志只在 REPL 运行时积累。与 REPL 的 `.a11ylog` 相同。

```tjs
var r = Agent.a11yLog(since);
for (var i = 0; i < r.lines.count; i++) Debug.message(r.lines[i]);
since = r.next;   // 次回は差分だけ
```

---

### a11yAction

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `node` | `&nbsp;` | 要操作的节点的 `id`。 |
| `action` | `&nbsp;` | `"click"` / `"focus"` / `"increment"` / `"decrement"` / `"set_value"`。 |
| `arg` | `&nbsp;` | `"set_value"` 时的值。 |

**返回值**

能操作时返回真。

**说明**

通过与屏幕阅读器相同的路径操作

把 [Agent.a11yTree](Agent.md#a11ytree) 的节点，通过与来自屏幕阅读器的操作
相同的路径操作 ( 不是按键输入的合成 )。用于朗读支持的验证。
从最前面的对话框开始查找，没有模态对话框时也会查找游戏本体的
节点。与 REPL 的 `.a11ydo` 相同。

**相关:** [Agent.a11yTree](Agent.md#a11ytree)

---
