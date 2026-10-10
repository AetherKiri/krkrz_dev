# 手柄

总结吉里吉里Z 的手柄 ( 摇杆 ) 输入的用法。各 API 的详情
请参照 [System 类参考文档](../../reference/System.md)。

## 手柄编号 (逻辑索引)

所有手柄 API 都接受手柄编号 `no`。编号的含义是共通的。

- **`0`** … 指“**最后操作过的手柄**”的特殊编号。会自动跟随实际触碰的手柄。
- **`1` 以上** … 按连接顺序的实际手柄 ( `1` = 第 1 台，`2` = 第 2 台，… )。连接台数
  可以用 `System.getJoypadCount()` 获取。

**按钮按下的键事件 ( 后述 ) 总是以 `0` 号 = 最后操作过的手柄为发生源**。
只连接 1 台时，`0` 与 `1` 指向同一个手柄。

“最后操作过的手柄”的切换通过按钮 / 十字键的按下来判定
( 摇杆的微小漂移不会引起切换 )。

## 按钮输入 ( 键事件 )

按钮会作为键事件送达。用 `Window.onKeyDown` / `onKeyUp` 接收
`VK_PAD1`~`VK_PAD12` / `VK_PADLEFT`~`VK_PADDOWN` / `VK_PAD_L_*` / `VK_PAD_R_*`
( 键码列表请参照 [键码表](../../guide/KeyCodes.md) )。
当前的按下状态也可以用 `System.getKeyState(VK_PADn)` 获取。

```tjs
// Window を継承したクラスで
function onKeyDown(key, shift) {
    if (key == VK_PAD1) {  /* A ボタン */ }
    if (key == VK_PADLEFT) { /* 十字左 */ }
}
```

十字键、左右摇杆方向会被量化为 8 个方向，作为上述方向键送达
( 需要原始摇杆值时见下一节 )。

### `VK_PAD1`~`VK_PAD4` 由按钮的**标识**决定 ( SDL3 / 通用构建 )

`VK_PAD1` = 标识 **A** ( 在 PlayStation 上为 **✕** )、`VK_PAD2` = **B** ( **○** )、
`VK_PAD3` = **X** ( **□** )、`VK_PAD4` = **Y** ( **△** )。

任天堂系手柄的 A/B、X/Y 的**位置**与 Xbox 系互换，因此
按位置分配时会出现“画面上显示‘用 A 确定’，却由标识为 B 的按钮确定”
这样的错位。以标识为基准后，无论哪个厂商的手柄，
显示与实际按下的按钮都会一致。

| | Xbox 系 | PlayStation 系 | 任天堂系 |
|---|---|---|---|
| `VK_PAD1` | A ( 下 ) | ✕ ( 下 ) | **A ( 右 )** |
| `VK_PAD2` | B ( 右 ) | ○ ( 右 ) | **B ( 下 )** |
| `VK_PAD3` | X ( 左 ) | □ ( 左 ) | **X ( 上 )** |
| `VK_PAD4` | Y ( 上 ) | △ ( 上 ) | **Y ( 左 )** |

Windows 原生 ( WINVER ) 构建的手柄输入基于 XInput，按钮标识固定为
Xbox 系，因此位置与标识不会产生分歧 ( 下述设置在 WINVER 中也
不存在 )。

想恢复为以往的位置基准时，请指定
[System.padButtonMapping](../../reference/System.md#padbuttonmapping) `= "position"`
或启动选项 `-padbuttons=position`。无法判定标识的
手柄会自动回退到位置基准。

这个分配在“SDL 的按钮 → `VK_PAD*`”唯一的分支点上进行，因此会
**同时对游戏侧的 `padKeyMap` 和 Elements 对话框的面板操作生效**。
解析结果会按每个手柄在日志中各输出 1 次，可用于实机确认。

### 想按位置指定的按钮是 `VK_PAD_FACE_*`

4 个面键除了标识基准的 `VK_PAD1`~`VK_PAD4` 之外，还有按**位置**指向的
虚拟键。

| 键码 | 位置 | Xbox 系的标识 | 任天堂系的标识 |
|---|---|---|---|
| `VK_PAD_FACE_SOUTH` (0x1D4) | 下 | A | B |
| `VK_PAD_FACE_EAST` (0x1D5) | 右 | B | A |
| `VK_PAD_FACE_WEST` (0x1D6) | 左 | X | Y |
| `VK_PAD_FACE_NORTH` (0x1D7) | 上 | Y | X |

同一个物理按钮的 1 次按下会**同时送达标识侧与位置侧两方的键事件**，因此
分配方可以按每个按钮选择“按标识对齐”或“按位置对齐”
( 例: 确定用标识的 A = `VK_PAD1`，“用上面的按钮打开的菜单”用
`VK_PAD_FACE_NORTH` )。无论 `padButtonMapping` 的设置如何，位置侧始终
指向物理布局。

按键提示的显示侧也有相同的 2 个系统 ( Elements 的 `pad_icon` 接受
`face_north` 和 `y` 两种名称 )。请让分配与显示使用相同基准来
配对。

⚠ **给同一个物理按钮分配两个系统时，1 次按下会触发 2 次。** 因为规格上
两方的键事件都会送达，例如给“确定”同时分配 `VK_PAD1` ( 标识 A ) 和
`VK_PAD_FACE_SOUTH` ( 下面的按钮 ) 时，在 Xbox 系手柄上
两者指向同一个物理按钮，因此会执行 2 次。请按按钮统一为其中一方。
在 Elements 的画面 JSON 中并用两个系统时，画面构建时会
输出注意日志。

### `System.padStyle` — 按钮图用哪个系统

连接的手柄的按钮表记系统可以用
[System.padStyle](../../reference/System.md#padstyle) ( 只读 ) 获取。
为 `"xbox"` / `"ps"` / `"switch"` 中的某一个，无法判定时为
空字符串。可用于选择操作指南中显示的按钮图。给 Elements 的
[ElementsDialog.setPadTheme](../../reference/ElementsDialog.md#setpadtheme) 指定 `"auto"` 后，
会基于这个判定自动选择按钮图主题。判定会监视手柄的
连接数与系统，一旦变化就当场重新决定，因此拔插
手柄后无需重新打开画面 ( 显示中画面的按钮图也会在下次绘制时
被替换 )。在无法判定系统的平台上，只要有 1 个手柄
连着就是 `"xbox"`，1 个都没有则是 `"keyboard"`。

### 与 Elements 对话框的关系

当 [Dialog](../../reference/ElementsDialog.md) 的面板持有键盘焦点时，
`VK_PAD*` 会被面板的控件操作 ( 十字 = 焦点导航 / A = 确定 / B =
cancel ) 消费。对于“只有这个手柄按钮一定要让游戏侧接收”的情况，
用 [ElementsDialog.registerHotKey](../../reference/ElementsDialog.md#registerhotkey) 注册后，
会绕过对话框，直达 `Window.onKeyDown` ( 输入的配送优先级请参照
[Dialog 指南](../../guide/ElementsDialog.md) )。反过来，从画面 JSON 侧
声明“这个输入属于游戏”时，在 `"bindings"` 中指定
`"action": "passthrough"` ( 面板不消费，直接放行。
与 `"none"` 的区别是后者消费之后什么都不做 )。

核心演示 `pad_advanced` 中有用于 ON/OFF 这一预留的复选框，可以当场
比较同一个按钮在“送达游戏”与“被面板吸走”之间的切换。

## 模拟轴

摇杆的倾斜、扳机的按入量用 `System.getPadAxis(no, axisId)` 获取。

```tjs
var x = System.getPadAxis(0, System.padAxisLeftX);       // -1.0 〜 +1.0
var y = System.getPadAxis(0, System.padAxisLeftY);       // -1.0 〜 +1.0 (下が正)
var t = System.getPadAxis(0, System.padAxisLeftTrigger); //  0.0 〜 +1.0
```

轴 ID 有 `System.padAxisLeftX` / `padAxisLeftY` / `padAxisRightX` / `padAxisRightY`
/ `padAxisLeftTrigger` / `padAxisRightTrigger` 6 种。用 TJS 全局常量
`paLeftX` … `paRightTrigger` 也可以指定相同的值。不会应用死区，
因此请根据需要在调用方处理。

!!! tip "无操作时也不会是 0"
    由于未应用死区，即使没有触碰摇杆，实测也会返回 ±0.05 左右的
    值。要避免“明明没碰角色却在动”，请由调用方加入
    丢弃小值的处理。行为可以在核心演示 `pad_advanced`
    ( 摇杆格子 + 原始值显示 ) 中确认。

## 连接的检测 / 振动

- `System.getJoypadCount()` … 连接中的实际手柄台数
- `System.hasJoypad(no)` … 指定编号是否有效
- `System.getJoypadType(no)` … 机型名的字符串 ( 依赖环境。SDL 版为识别名，WINVER 版为
  `"XInput Controller"` )
- `System.padStyle` … 最后操作过的手柄的按钮表记系统 ( `"xbox"` / `"ps"` /
  `"switch"`，不明则为空字符串 )。用于选择按钮图 ( 前一节 )
- `System.onJoypadChange(no, name)` … 最后操作过的手柄的识别名变化时
  被调用的回调 ( 手柄消失时 `name` 为空字符串 )
- `System.rumblePad(no, low, high, durationMs)` / `System.stopRumblePad(no)` …
  振动 ( low/high 为 0~255 )

## 手柄功能的禁用 ( 支持用 )

针对其他设备被错误识别为手柄而导致误动作等情况，
可以把手柄功能整个禁用。禁用时既不会获取状态，也不会生成键事件。

- 运行时: `System.padEnabled = false;` ( 重新启用为 `= true;` )
- 启动时: 命令行选项 `-joypad=no` ( [命令行](../../guide/CommandLine.md) )

用 `System.padEnabled` 显式指定时，优先级高于命令行。

## 平台与实现

手柄输入在全部构建共通的逻辑管理层 ( `tTVPPadManager` ) 之上，
拥有按平台区分的后端。

- **SDL3 / 其他**: 基于 `SDL_Gamepad`。支持多种机型。如果存在随附的
  `gamecontrollerdb.txt`，会在打开手柄之前读取，因此 SDL 标准映射中
  没有的手柄也能识别。
- **WINVER ( Windows 原生 )**: 基于 **XInput** ( 最多 4 台、支持振动 )。对象为 Xbox 系
  手柄，通用 DirectInput 手柄不在对象范围内。

调试显示 ( 按钮矩阵 + 轴值的覆盖层 ) 请参照
[PadOverlay](pad_overlay.md)。引擎内部的设计详情在
`src/core/doc/Gamepad.md` ( SSOT ) 中。
