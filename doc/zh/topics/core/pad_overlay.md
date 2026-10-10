# 手柄状态的观察 (PadOverlay)

SDL3 构建的引擎中内置了调试用的覆盖层，可在画面左上角实时显示手柄的状态
( 16 个按钮的 ON/OFF 与 6 轴的模拟值 )。在实机 ( 例如 Switch ) 上做
控制器相关的运行确认时可以使用。

详细的显示规格与内部结构请参照 src/core 侧的指南：

- [doc/PadOverlay.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/PadOverlay.md)
- [doc/Gamepad.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Gamepad.md)

---

## 显示示例

```
+--------------------------------+
| Pad: Xbox Series X Controller  |
| [A ][B ][X ][Y ]               |
| [L1][R1][L2][R2]               |
| [BK][ST][LS][RS]               |
| [Lf][Up][Rt][Dn]               |
| LX +0.45 LY -0.32              |
| RX +0.00 RY +0.00              |
| LT +0.00 RT +0.80              |
+--------------------------------+
```

- 头部：SDL 手柄名 ( 未连接时为 `(none)` )
- 单元格：按下中为绿色，未按下为暗灰
- 轴：摇杆轴为 `-1.00 ~ +1.00`，扳机轴为 `0.00 ~ +1.00`

WINVER 构建没有手柄抽象 API，因此通过 OGLDrawDevice 路径输出
时，会显示为全部 OFF、所有轴 +0.00。

---

## 覆盖层的启用

- 从启动时起：[`-padoverlay=1`](../../guide/CommandLine.md)
- 运行中切换：[System.setPadOverlay](../../reference/System.md#setpadoverlay)
- 从 [REPL](repl.md)：`.padoverlay [on|off]`

[`-memoverlay=1`](../../guide/CommandLine.md) ( 画面右上 ) 独立工作，
两者可以同时显示。

---

## 从 TJS2 直接获取轴

覆盖层用于观察，若要从脚本获取轴的模拟值，请使用
[System.getPadAxis](../../reference/System.md#getpadaxis)。

```tjs
var v = System.getPadAxis(0, System.padAxisLeftX);
// v は -1.0 〜 +1.0 の実数 (未接続/無効値で 0.0)
```

轴 ID 常量准备了 [System.padAxisLeftX](../../reference/System.md#padaxisleftx)
等 6 种。

振动控制可以通过 [System.rumblePad](../../reference/System.md#rumblepad) /
[System.stopRumblePad](../../reference/System.md#stoprumblepad) 进行。
手柄的连接数、存在确认请使用
[System.getJoypadCount](../../reference/System.md#getjoypadcount) /
[System.hasJoypad](../../reference/System.md#hasjoypad)。
