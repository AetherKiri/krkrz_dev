# BitmapLayerTreeOwner

BitmapLayerTreeOwner 类是持有图层树、并能通过 Bitmap 类获取绘制结果的类。(1.1.0 及以后)

通过在 Layer 类的构造函数的第 1 个参数中代替 window 传入它，即可将这些 Layer 的绘制结果作为 Bitmap 类的图像获取。

## 成员列表

### 构造函数

- [BitmapLayerTreeOwner](#bitmaplayertreeowner)

### 属性

- [bitmap](#bitmap)
- [dirtyRect](#dirtyrect)
- [focusedLayer](#focusedlayer)
- [height](#height)
- [isUpdated](#isupdated)
- [layerEventTargetInterface](#layereventtargetinterface)
- [layerTreeOwnerInterface](#layertreeownerinterface)
- [primaryLayer](#primarylayer)
- [width](#width)

### 方法

- [clearDirtyRect](#cleardirtyrect)
- [fireClick](#fireclick)
- [fireDisplayRotate](#firedisplayrotate)
- [fireDoubleClick](#firedoubleclick)
- [fireKeyDown](#firekeydown)
- [fireKeyPress](#firekeypress)
- [fireKeyUp](#firekeyup)
- [fireMouseDown](#firemousedown)
- [fireMouseMove](#firemousemove)
- [fireMouseOutOfWindow](#firemouseoutofwindow)
- [fireMouseUp](#firemouseup)
- [fireMouseWheel](#firemousewheel)
- [fireMultiTouch](#firemultitouch)
- [fireRecheckInputState](#firerecheckinputstate)
- [fireReleaseCapture](#firereleasecapture)
- [fireTouchDown](#firetouchdown)
- [fireTouchMove](#firetouchmove)
- [fireTouchRotate](#firetouchrotate)
- [fireTouchScaling](#firetouchscaling)
- [fireTouchUp](#firetouchup)
- [update](#update)

### 事件

- [onChangeLayerImage](#onchangelayerimage)
- [onDisableAttentionPoint](#ondisableattentionpoint)
- [onGetCursorPos](#ongetcursorpos)
- [onReleaseMouseCapture](#onreleasemousecapture)
- [onResetImeMode](#onresetimemode)
- [onResizeLayer](#onresizelayer)
- [onSetAttentionPoint](#onsetattentionpoint)
- [onSetCursorPos](#onsetcursorpos)
- [onSetHintText](#onsethinttext)
- [onSetImeMode](#onsetimemode)
- [onSetMouseCursor](#onsetmousecursor)

---

### BitmapLayerTreeOwner

构造函数

**说明**

构建 BitmapLayerTreeOwner 对象

构建 BitmapLayerTreeOwner 类的对象。

---

### bitmap

属性 \ 访问: `r/w`

**说明**

绘制目标 Bitmap 对象

返回该图层树所有者持有的 `Bitmap` 对象。
图层树的内容会被绘制到该 Bitmap 中。只读。

**相关:** [BitmapLayerTreeOwner.update](BitmapLayerTreeOwner.md#update)

---

### dirtyRect

属性 \ 访问: `r/w`

**说明**

脏矩形对象

返回表示最近一次绘制中更新区域的 `Rect` 对象。
只读。

---

### focusedLayer

属性 \ 访问: `r/w`

**说明**

持有焦点的图层

获取 / 设置该树内当前持有焦点的图层。
设置时传入 null 将解除焦点。

**相关:** [Layer.focused](Layer.md#focused)

---

### height

属性 \ 访问: `r/w`

**说明**

高度 (readonly)

---

### isUpdated

属性 \ 访问: `r/w`

**说明**

已更新标志

返回自最近一次调用 `update` 以来图层树是否已被更新。
若为真，则需要重绘。只读。

---

### layerEventTargetInterface

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

LayerEventTarget 接口指针

将图层事件转送目标的 C++ 接口 ( `tTVPLayerTreeOwner` )
指针作为 64bit 整数返回。用于通过插件访问图层事件
分发系统。只读。

---

### layerTreeOwnerInterface

属性 \ 访问: `r/w`

**说明**

LTO 接口，内部使用 (readonly)

---

### primaryLayer

属性 \ 访问: `r/w`

**说明**

主图层 (readonly)

---

### width

属性 \ 访问: `r/w`

**说明**

宽度 (readonly)

---

### clearDirtyRect

方法

**说明**

清除更新矩形信息

---

### fireClick

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 被点击位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 被点击位置的 y 坐标 ( 客户端坐标 ) |

**说明**

向图层通知点击 (已不推荐)

---

### fireDisplayRotate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `orientation` | `&nbsp;` | 画面方向 |
| `rotate` | `&nbsp;` | 角度 |
| `bpp` | `&nbsp;` | bits per pixel |
| `hresolution` | `&nbsp;` | 画面宽度 |
| `vresolution` | `&nbsp;` | 画面高度 |

**说明**

向图层通知画面已旋转

---

### fireDoubleClick

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 被双击位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 被双击位置的 y 坐标 ( 客户端坐标 ) |

**说明**

向图层通知双击 (已不推荐)

---

### fireKeyDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 被按下键的虚拟键码 |
| `shift` | `&nbsp;` | 按键被按下时同时按着的 Shift 类按键及鼠标按钮的状态 |

**说明**

向图层通知按键已被按下

---

### fireKeyPress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 字符 |

**说明**

向图层通知字符已被输入

---

### fireKeyUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 被松开键的虚拟键码 |
| `shift` | `&nbsp;` | 按键被松开时同时按着的 Shift 类按键及鼠标按钮的状态 |

**说明**

向图层通知按键已松开

---

### fireMouseDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标按钮被按下位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 鼠标按钮被按下位置的 y 坐标 ( 客户端坐标 ) |
| `mb` | `&nbsp;` | 被按下的鼠标按钮 |
| `flags` | `&nbsp;` |  |

**说明**

向图层通知鼠标按下

---

### fireMouseMove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标移动位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 鼠标移动位置的 y 坐标 ( 客户端坐标 ) |
| `flags` | `&nbsp;` | 鼠标移动时同时按着的 Shift 类按键及鼠标按钮的状态 |

**说明**

向图层通知鼠标移动

---

### fireMouseOutOfWindow

方法

**说明**

向图层通知鼠标已移到 Window 外

---

### fireMouseUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标按钮被松开位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 鼠标按钮被松开位置的 y 坐标 ( 客户端坐标 ) |
| `mb` | `&nbsp;` | 被松开的鼠标按钮 |
| `flags` | `&nbsp;` | 鼠标按钮被松开时同时按着的 Shift 类按键的状态 |

**说明**

向图层通知鼠标按下

---

### fireMouseWheel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `shift` | `&nbsp;` | 鼠标移动时同时按着的 Shift 类按键及鼠标按钮的状态 |
| `delta` | `&nbsp;` | 滚轮的旋转角度 |
| `x` | `&nbsp;` | 滚轮旋转位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 滚轮旋转位置的 y 坐标 ( 客户端坐标 ) |

**说明**

向图层通知鼠标滚轮旋转

---

### fireMultiTouch

方法

**说明**

向图层通知多点触控状态变化

---

### fireRecheckInputState

方法

**说明**

如有必要，请每隔 1 秒调用一次。

会重新检查当前图层的鼠标位置确认与提示更新、光标类型、图层 Enter/Leave。
在内部会执行鼠标光标移动 0 的调用。

---

### fireReleaseCapture

方法

**说明**

向图层通知解除鼠标捕获

---

### fireTouchDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 被触摸位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 被触摸位置的 y 坐标 ( 客户端坐标 ) |
| `cx` | `&nbsp;` | 手指接触的横向像素数 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数 |
| `id` | `&nbsp;` | 触摸 ID |

**说明**

向图层通知发生了触摸

---

### fireTouchMove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 触摸位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 触摸位置的 y 坐标 ( 客户端坐标 ) |
| `cx` | `&nbsp;` | 手指接触的横向像素数 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数 |
| `id` | `&nbsp;` | 触摸 ID |

**说明**

向图层通知触摸已移动

---

### fireTouchRotate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `startangle` | `&nbsp;` | 多点触控开始时的弧度角 |
| `curangle` | `&nbsp;` | 事件发生时的触摸弧度角 |
| `dist` | `&nbsp;` | 事件发生时的触摸像素距离 |
| `cx` | `&nbsp;` | 中心位置的 x 坐标 ( 客户端坐标 ) |
| `cy` | `&nbsp;` | 中心位置的 y 坐标 ( 客户端坐标 ) |
| `flag` | `&nbsp;` | 多点触控状态标志 |

**说明**

向图层通知进行了旋转操作

---

### fireTouchScaling

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `startdist` | `&nbsp;` | 多点触控开始时的像素距离 |
| `curdist` | `&nbsp;` | 事件发生时的触摸像素距离 |
| `cx` | `&nbsp;` | 中心位置的 x 坐标 ( 客户端坐标 ) |
| `cy` | `&nbsp;` | 中心位置的 y 坐标 ( 客户端坐标 ) |
| `flag` | `&nbsp;` | 多点触控状态标志。 |

**说明**

向图层通知进行了缩放操作

---

### fireTouchUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 手指离开位置的 x 坐标 ( 客户端坐标 ) |
| `y` | `&nbsp;` | 手指离开位置的 y 坐标 ( 客户端坐标 ) |
| `cx` | `&nbsp;` | 手指接触的横向像素数 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数 |
| `id` | `&nbsp;` | 触摸 ID |

**说明**

向图层通知触摸已松开

---

### update

方法

**说明**

图层树的绘制更新

将内部的图层树绘制到 `bitmap` 属性所指向的 Bitmap，并将更新区域反映到 `dirtyRect` 中。

**相关:** [BitmapLayerTreeOwner.bitmap](BitmapLayerTreeOwner.md#bitmap) / [BitmapLayerTreeOwner.dirtyRect](BitmapLayerTreeOwner.md#dirtyrect)

---

### onChangeLayerImage

事件

**说明**

Layer 图像已更新

---

### onDisableAttentionPoint

事件

**说明**

从 Layer 解除了注视位置的指定

---

### onGetCursorPos

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

从 Layer 调用了光标位置获取

如有必要，返回光标位置

---

### onReleaseMouseCapture

事件

**说明**

从 Layer 调用了鼠标捕获解除

如有必要，执行鼠标捕获解除

---

### onResetImeMode

事件

**说明**

IME 模式已被重置

---

### onResizeLayer

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**说明**

主图层的大小已更改

---

### onSetAttentionPoint

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

从 Layer 调用了注视位置的指定

---

### onSetCursorPos

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

从 Layer 调用了光标位置设置

如有必要，设置光标位置

---

### onSetHintText

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sender` | `&nbsp;` |  |
| `hint` | `&nbsp;` |  |

**说明**

从 Layer 调用了提示文本设置

如有必要，执行提示文本设置

---

### onSetImeMode

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

**说明**

IME 模式已被设置

---

### onSetMouseCursor

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `cursor` | `&nbsp;` |  |

**说明**

从 Layer 调用了光标设置

如有必要，更改光标。

---
