# Window

Window 类是管理**窗口**的类。

## 成员列表

### 构造函数

- [Window](#window)

### 属性

- [visible](#visible)
- [caption](#caption)
- [width](#width)
- [height](#height)
- [minWidth](#minwidth)
- [minHeight](#minheight)
- [maxWidth](#maxwidth)
- [maxHeight](#maxheight)
- [left](#left)
- [top](#top)
- [focusable](#focusable)
- [trapKey](#trapkey)
- [innerWidth](#innerwidth)
- [innerHeight](#innerheight)
- [frameWidth](#framewidth)
- [frameHeight](#frameheight)
- [zoomNumer](#zoomnumer)
- [zoomDenom](#zoomdenom)
- [aspectLock](#aspectlock)
- [viewportFit](#viewportfit)
- [viewportZoom](#viewportzoom)
- [viewportAlignX](#viewportalignx)
- [viewportAlignY](#viewportaligny)
- [viewportOffsetX](#viewportoffsetx)
- [viewportOffsetY](#viewportoffsety)
- [viewportBgColor](#viewportbgcolor)
- [drawDevice](#drawdevice)
- [borderStyle](#borderstyle)
- [stayOnTop](#stayontop)
- [imeMode](#imemode)
- [mouseCursorState](#mousecursorstate)
- [useMouseKey](#usemousekey)
- [fullScreen](#fullscreen)
- [mainWindow](#mainwindow)
- [focusedLayer](#focusedlayer)
- [primaryLayer](#primarylayer)
- [HWND](#hwnd)
- [touchScaleThreshold](#touchscalethreshold)
- [touchRotateThreshold](#touchrotatethreshold)
- [touchPointCount](#touchpointcount)
- [enableTouch](#enabletouch)
- [waitVSync](#waitvsync)
- [hintDelay](#hintdelay)
- [displayOrientation](#displayorientation)
- [displayRotate](#displayrotate)
- [displayDensity](#displaydensity)
- [enableTouchMouse](#enabletouchmouse)
- [innerSunken](#innersunken)
- [layerEventTarget](#layereventtarget)
- [layerLeft](#layerleft)
- [layerTop](#layertop)
- [layerTreeOwnerInterface](#layertreeownerinterface)
- [mouseCursor](#mousecursor)
- [showScrollBars](#showscrollbars)
- [GLGetProcAddress](#glgetprocaddress)
- [maximized](#maximized)
- [minimized](#minimized)
- [disableResize](#disableresize)
- [disableMove](#disablemove)

### 方法

- [close](#close)
- [bringToFront](#bringtofront)
- [update](#update)
- [showModal](#showmodal)
- [setMaskRegion](#setmaskregion)
- [removeMaskRegion](#removemaskregion)
- [add](#add)
- [remove](#remove)
- [setSize](#setsize)
- [setMinSize](#setminsize)
- [setMaxSize](#setmaxsize)
- [setPos](#setpos)
- [setInnerSize](#setinnersize)
- [setZoom](#setzoom)
- [setViewport](#setviewport)
- [setViewportWallpaper](#setviewportwallpaper)
- [clearViewportWallpaper](#clearviewportwallpaper)
- [postInputEvent](#postinputevent)
- [hideMouseCursor](#hidemousecursor)
- [registerMessageReceiver](#registermessagereceiver)
- [postMessage](#postmessage)
- [getTouchPoint](#gettouchpoint)
- [getMouseVelocity](#getmousevelocity)
- [getTouchVelocity](#gettouchvelocity)
- [resetMouseVelocity](#resetmousevelocity)
- [beginMove](#beginmove)
- [requestUpdate](#requestupdate)
- [setLayerPos](#setlayerpos)
- [maximize](#maximize)
- [minimize](#minimize)
- [showRestore](#showrestore)
- [getNormalRect](#getnormalrect)
- [getWindowRect](#getwindowrect)
- [getClientRect](#getclientrect)
- [setCursorPos](#setcursorpos)
- [getCursorPos](#getcursorpos)
- [setClientRect](#setclientrect)
- [registerExEvent](#registerexevent)
- [registerDeviceChange](#registerdevicechange)

### 事件

- [onMouseEnter](#onmouseenter)
- [onMouseLeave](#onmouseleave)
- [onClick](#onclick)
- [onDoubleClick](#ondoubleclick)
- [onMouseDown](#onmousedown)
- [onMouseUp](#onmouseup)
- [onMouseMove](#onmousemove)
- [onMouseWheel](#onmousewheel)
- [onTouchDown](#ontouchdown)
- [onTouchUp](#ontouchup)
- [onTouchMove](#ontouchmove)
- [onTouchScaling](#ontouchscaling)
- [onTouchRotate](#ontouchrotate)
- [onMultiTouch](#onmultitouch)
- [onKeyDown](#onkeydown)
- [onKeyUp](#onkeyup)
- [onKeyPress](#onkeypress)
- [onTextInput](#ontextinput)
- [onResize](#onresize)
- [onFileDrop](#onfiledrop)
- [onCloseQuery](#onclosequery)
- [onPopupHide](#onpopuphide)
- [onActivate](#onactivate)
- [onDeactivate](#ondeactivate)
- [onHintChanged](#onhintchanged)
- [onDisplayRotate](#ondisplayrotate)
- [onPointerDown](#onpointerdown)
- [onPointerMove](#onpointermove)
- [onPointerUp](#onpointerup)
- [onMaximizeQuery](#onmaximizequery)
- [onMove](#onmove)
- [onMoving](#onmoving)
- [onResizing](#onresizing)
- [onMoveSizeBegin](#onmovesizebegin)
- [onMoveSizeEnd](#onmovesizeend)
- [onMinimize](#onminimize)
- [onMaximize](#onmaximize)
- [onDPIChanged](#ondpichanged)
- [onDisplayChanged](#ondisplaychanged)
- [onDeviceChanged](#ondevicechanged)
- [onPaste](#onpaste)

---

### Window

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `parent` | `&nbsp;` | 指定父窗口。<br>指定父窗口后，将作为其子窗口创建。<br>不指定时省略。 |

**说明**

Window 对象的构建

构建 Window 类的对象。

窗口以非显示状态创建，位置和大小未定义 ( 位于某处的适当大小 )。

---

### visible

属性 \ 访问: `r/w`

**说明**

窗口是否正在显示

表示窗口是否正在显示。也可以设置值。

真的话窗口正在显示，假的话窗口处于非显示状态。

---

### caption

属性 \ 访问: `r/w`

**说明**

窗口的标题

表示窗口的**标题** ( 标题栏的标题 )。
也可以设置值。

---

### width

属性 \ 访问: `r/w`

**说明**

窗口的宽度

表示窗口的宽度 ( 包含窗口装饰的外形宽度 )。也可以设置值。

!!! tip "推荐使用以内侧 ( 绘制区域 ) 为基准的 API"
    该值是**包含窗口装饰的外形**尺寸。装饰的有无与粗细会随
    平台、OS 主题、[Window.borderStyle](Window.md#borderstyle) 而
    变化，在不带装饰的环境 ( 移动端 / 主机，`bsNone` 时 ) 中
    与内侧尺寸同值。 可移植的代码请使用游戏画面直接对应的
    [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) /
    [Window.setInnerSize](Window.md#setinnersize)。
    需要边框部分时，可以加上 [Window.frameWidth](Window.md#framewidth) /
    [Window.frameHeight](Window.md#frameheight)。

**相关:** [Window.innerWidth](Window.md#innerwidth) / [Window.frameWidth](Window.md#framewidth) / [Window.height](Window.md#height) / [Window.setSize](Window.md#setsize)

---

### height

属性 \ 访问: `r/w`

**说明**

窗口的高度

表示窗口的高度 ( 包含窗口装饰的外形高度 )。也可以设置值。

!!! tip "推荐使用以内侧 ( 绘制区域 ) 为基准的 API"
    该值是**包含窗口装饰的外形**尺寸。装饰的有无与粗细会随
    平台、OS 主题、[Window.borderStyle](Window.md#borderstyle) 而
    变化，在不带装饰的环境 ( 移动端 / 主机，`bsNone` 时 ) 中
    与内侧尺寸同值。 可移植的代码请使用游戏画面直接对应的
    [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) /
    [Window.setInnerSize](Window.md#setinnersize)。
    需要边框部分时，可以加上 [Window.frameWidth](Window.md#framewidth) /
    [Window.frameHeight](Window.md#frameheight)。

**相关:** [Window.innerHeight](Window.md#innerheight) / [Window.frameHeight](Window.md#frameheight) / [Window.width](Window.md#width) / [Window.setSize](Window.md#setsize)

---

### minWidth

属性 \ 访问: `r/w`

**说明**

窗口的最小宽度

表示窗口的最小宽度 ( 内侧 = 绘制区域的宽度 )。也可以设置值。指定 0 时限制将取消。

**相关:** [Window.innerWidth](Window.md#innerwidth) / [Window.minHeight](Window.md#minheight) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### minHeight

属性 \ 访问: `r/w`

**说明**

窗口的最小高度

表示窗口的最小高度 ( 内侧 = 绘制区域的高度 )。也可以设置值。指定 0 时限制将取消。

**相关:** [Window.innerHeight](Window.md#innerheight) / [Window.minWidth](Window.md#minwidth) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxWidth

属性 \ 访问: `r/w`

**说明**

窗口的最大宽度

表示窗口的最大宽度 ( 内侧 = 绘制区域的宽度 )。也可以设置值。指定 0 时限制将取消。

**相关:** [Window.innerWidth](Window.md#innerwidth) / [Window.maxHeight](Window.md#maxheight) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### maxHeight

属性 \ 访问: `r/w`

**说明**

窗口的最大高度

表示窗口的最大高度 ( 内侧 = 绘制区域的高度 )。也可以设置值。指定 0 时限制将取消。

**相关:** [Window.innerHeight](Window.md#innerheight) / [Window.maxWidth](Window.md#maxwidth) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize)

---

### left

属性 \ 访问: `r/w`

**说明**

窗口的左端位置

表示窗口的左端位置。也可以设置值。

左端位置是从屏幕原点 ( 左上角 ) 起的 x 坐标。

**相关:** [Window.top](Window.md#top) / [Window.setPos](Window.md#setpos)

---

### top

属性 \ 访问: `r/w`

**说明**

窗口的上端位置

表示窗口的上端位置。也可以设置值。

上端位置是从屏幕原点 ( 左上角 ) 起的 y 坐标。

**相关:** [Window.left](Window.md#left) / [Window.setPos](Window.md#setpos)

---

### focusable

属性 \ 访问: `r/w`

**说明**

是否可获取焦点

表示是否可获取焦点。也可以设置值。

设置为假时，将无法获取焦点，也就是窗口不再变为活动状态。副作用是无法通过抓住标题栏移动窗口、调整窗口大小，也无法点击“×”按钮关闭窗口。

想要获得键盘输入时，可以使用 [Window.trapKey](Window.md#trapkey) 属性。

通常，这用于实现像弹出菜单那样显示在最前面、但自身不获取焦点的窗口。

在当前版本中，窗口进入全屏或从全屏恢复时，该属性的设置内容可能会丢失。

**相关:** [Window.trapKey](Window.md#trapkey) / [Window.onPopupHide](Window.md#onpopuphide)

---

### trapKey

属性 \ 访问: `r/w`

**说明**

是否拦截键输入

表示是否拦截键输入。也可以设置值。

设置为真时，可以截取其他窗口中发生的键输入事件，使其在此窗口上发生。

当多个窗口的该属性被设置为真时，键输入事件将发生在最后创建的窗口上。

**相关:** [Window.focusable](Window.md#focusable)

---

### innerWidth

属性 \ 访问: `r/w`

**说明**

客户区的宽度

表示客户区的宽度。
也可以设置值。

**相关:** [Window.innerHeight](Window.md#innerheight) / [Window.setInnerSize](Window.md#setinnersize)

---

### innerHeight

属性 \ 访问: `r/w`

**说明**

客户区的高度

表示客户区的高度。
也可以设置值。

**相关:** [Window.innerWidth](Window.md#innerwidth) / [Window.setInnerSize](Window.md#setinnersize)

---

### frameWidth

属性 \ 访问: `r/w`

**说明**

窗口装饰的宽度

表示窗口外形与内侧 ( 绘制区域 ) 的宽度之差 ( = [Window.width](Window.md#width) - [Window.innerWidth](Window.md#innerwidth) )。是左右边框合计的值。

在不带窗口装饰的环境 ( 移动端 / 主机，以及 [Window.borderStyle](Window.md#borderstyle) 为 `bsNone` 时 ) 中为 0。

可用于把以外形为基准编写的代码迁移到以内侧为基准时的换算。是只读的。

**相关:** [Window.frameHeight](Window.md#frameheight) / [Window.width](Window.md#width) / [Window.innerWidth](Window.md#innerwidth)

---

### frameHeight

属性 \ 访问: `r/w`

**说明**

窗口装饰的高度

表示窗口外形与内侧 ( 绘制区域 ) 的高度之差 ( = [Window.height](Window.md#height) - [Window.innerHeight](Window.md#innerheight) )。是标题栏与上下边框合计的值。

在不带窗口装饰的环境 ( 移动端 / 主机，以及 [Window.borderStyle](Window.md#borderstyle) 为 `bsNone` 时 ) 中为 0。

可用于把以外形为基准编写的代码迁移到以内侧为基准时的换算。是只读的。

**相关:** [Window.frameWidth](Window.md#framewidth) / [Window.height](Window.md#height) / [Window.innerHeight](Window.md#innerheight)

---

### zoomNumer

属性 \ 访问: `r/w`

**说明**

图层放大倍率（分子）

表示图层放大倍率的分子。
虽然也可以设置值，但要设置值时请使用 [Window.setZoom](Window.md#setzoom) 方法。

分母由 [Window.zoomDenom](Window.md#zoomdenom) 属性表示。

详情请参阅 [Window.setZoom](Window.md#setzoom) 方法。

**相关:** [Window.setZoom](Window.md#setzoom) / [Window.zoomDenom](Window.md#zoomdenom)

---

### zoomDenom

属性 \ 访问: `r/w`

**说明**

图层放大倍率（分母）

表示图层放大倍率的分母。
虽然也可以设置值，但要设置值时请使用 [Window.setZoom](Window.md#setzoom) 方法。

分子由 [Window.zoomNumer](Window.md#zoomnumer) 属性表示。

详情请参阅 [Window.setZoom](Window.md#setzoom) 方法。

**相关:** [Window.setZoom](Window.md#setzoom) / [Window.zoomNumer](Window.md#zoomnumer)

---

### aspectLock

属性 \ 访问: `r/w`

**说明**

窗口宽高比的固定

固定窗口内侧 ( [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) ) 的宽高比。以 `"16:9"` 这样的 `"幅:高さ"` 形式的字符串指定，设置空字符串 `""` 则解除。默认是 `""` ( 不固定 )。也可以获取值。

在想要**分离**游戏画面 ( primaryLayer ) 的比率与整个窗口的比率时使用。例如，把整个窗口保持为 16:9，并在其中以逐像素 ( `viewportFit = "integer"` ) 或适应 ( `"contain"` ) 的方式放置 640x400 ( 8:5 ) 的游戏画面，就可以形成这样的构成。UI ( Elements 等 ) 以 16:9 的基本大小制作时，如果窗口没有保持为 16:9，UI 与游戏画面的框就会错位。

启用固定后，

- 用户对窗口的调整大小会被约束到该比率 ( 拖拽操作过程中也保持比率 )。
- [Window.setZoom](Window.md#setzoom) 将根据该比率决定高度 ( 以往是“primaryLayer 的大小 × 倍率”，因此每次设置倍率都会回到图层的比率 )。
- 设置时刻的内侧尺寸也会**以宽度为基准**调整到该比率。

游戏画面如何放置到该框中，仍由 [Window.viewportFit](Window.md#viewportfit) 等视口设置负责。本属性只决定“窗口的形状”。

```
window.aspectLock = "16:9";        // ウインドウを 16:9 に固定
window.viewportFit = "integer";    // その中にゲーム画面をドットバイドットで配置
window.aspectLock = "";            // 固定を解除
```

!!! warning "SDL3 / 通用构建专用"
    Windows 原生 ( WINVER ) 构建中**不执行任何操作**。即使设置也会被忽略，读取时始终返回空字符串。

**相关:** [Window.viewportFit](Window.md#viewportfit) / [Window.setZoom](Window.md#setzoom) / [Window.setInnerSize](Window.md#setinnersize)

---

### viewportFit

属性 \ 访问: `r/w`

**说明**

视口的适应方式

表示如何把内侧游戏画面放入外侧窗口 (surface) 的字符串。
也可以设置值。

`"contain"` ( 保持宽高比能容纳的最大、黑边。默认 ) / `"cover"` ( 保持宽高比填满的最小、超出部分 clip ) / `"fill"` ( 无视宽高比拉伸到全面 ) / `"none"` ( 原尺寸 ) / `"integer"` ( 在能容纳的范围内取最大整数倍。最低 1 倍 ) / `"custom"` ( 使用 [Window.viewportZoom](Window.md#viewportzoom) 的倍率 ) 中的某一个。


!!! note "想保持与以往 ( 吉里吉里2 / 吉里吉里Z ) 相同的显示时"
    默认的 `"contain"` 在窗口与内侧游戏画面大小不同时
    会保持宽高比缩放。 想回到即使把窗口拉宽游戏仍保持原尺寸
    放在左上的**以往那样的显示**时，请显式指定
    `viewportFit = "none"` 和 [Window.viewportAlignX](Window.md#viewportalignx) /
    [Window.viewportAlignY](Window.md#viewportaligny) `= 0`。

    另外，只要用 [Window.setInnerSize](Window.md#setinnersize) 把窗口的内侧尺寸
    始终保持为“primaryLayer 的大小 × [Window.setZoom](Window.md#setzoom) 的倍率”，
    无论哪种适应方式都会以等倍 1:1 显示，不会出现差异。
    出现差异的情况是用户调整窗口大小 / 最大化时、移动到放大率不同的
    显示器时，以及无法更改窗口大小的环境
    ( 移动端 / 主机 )。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.setViewport](Window.md#setviewport) / [Window.viewportZoom](Window.md#viewportzoom)

---

### viewportZoom

属性 \ 访问: `r/w`

**说明**

视口的放大倍率

表示 [Window.viewportFit](Window.md#viewportfit) 为 `"custom"` 时使用的放大倍率的实数 ( 例 1.8 = 180% )。默认是 1.0。
也可以设置值。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.viewportFit](Window.md#viewportfit) / [Window.setViewport](Window.md#setviewport)

---

### viewportAlignX

属性 \ 访问: `r/w`

**说明**

视口的水平配置

表示产生余白时内侧游戏画面水平配置的实数。0=左 / 0.5=中央 / 1=右。默认是 0.5。
也可以设置值。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.viewportAlignY](Window.md#viewportaligny) / [Window.setViewport](Window.md#setviewport)

---

### viewportAlignY

属性 \ 访问: `r/w`

**说明**

视口的垂直配置

表示产生余白时内侧游戏画面垂直配置的实数。0=上 / 0.5=中央 / 1=下。默认是 0.5。
也可以设置值。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.viewportAlignX](Window.md#viewportalignx) / [Window.setViewport](Window.md#setviewport)

---

### viewportOffsetX

属性 \ 访问: `r/w`

**说明**

视口的水平偏移

表示在 align 后加算的内侧游戏画面水平偏移的整数 ( px、surface 坐标 )。
也可以设置值。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.viewportOffsetY](Window.md#viewportoffsety) / [Window.setViewport](Window.md#setviewport)

---

### viewportOffsetY

属性 \ 访问: `r/w`

**说明**

视口的垂直偏移

表示在 align 后加算的内侧游戏画面垂直偏移的整数 ( px、surface 坐标 )。
也可以设置值。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.viewportOffsetX](Window.md#viewportoffsetx) / [Window.setViewport](Window.md#setviewport)

---

### viewportBgColor

属性 \ 访问: `r/w`

**说明**

视口余白的背景色

表示用于涂填视口产生的余白的背景色，为 `0xRRGGBB` 形式的整数 ( 高 8 位为 alpha )。默认是黑色。
也可以设置值。设置了壁纸 ( [Window.setViewportWallpaper](Window.md#setviewportwallpaper) ) 时壁纸优先。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.setViewportWallpaper](Window.md#setviewportwallpaper) / [Window.setViewport](Window.md#setviewport)

---

### drawDevice

属性 \ 访问: `r/w`

**说明**

绘制设备

表示绘制设备对象。

也可以设置值。设置值后，之前指定给该窗口的绘制设备会自动
失效 ( 会被 invalidate )。

默认指定的实例因构建而异。Windows 原生 ( WINVER ) 构建中为
[Window.BasicDrawDevice](Window.BasicDrawDevice.md) ( Direct3D 11 )，SDL3 构建中为
[SDLOGLDrawDevice](SDLOGLDrawDevice.md) ( OpenGL 有效构建时。无效构建中为
[SDLDrawDevice](SDLDrawDevice.md) )。可以通过启动选项 `-drawdevice` 选择启动时的默认值
( [命令行选项](../guide/CommandLine.md) )。另外，以 `-drawdevice=sdl` 启动 SDL3 构建时，
无法在运行过程中切换到 OpenGL 系的设备。

想要指定自定义的绘制设备 ( 由插件提供的设备 ) 时，请遵循该插件的文档。

---

### borderStyle

属性 \ 访问: `r/w`

**说明**

窗口外观

表示窗口的外观。也可以设置值。

可以设置以下值。

`**bsDialog**      :` 不可调整大小，具有与对话框相同的外观。

`**bsSingle**      :` 不可调整大小的窗口。

`**bsNone**        :` 没有边框的窗口。

`**bsSizeable**    :` 可调整大小的一般窗口。默认值。

`**bsToolWindow**  :` 不可调整大小的工具窗口 ( 标题较小的窗口 )。

`**bsSizeToolWin** :` 与 bsToolWindow 相似，但可以调整大小。

---

### stayOnTop

属性 \ 访问: `r/w`

**说明**

是否始终显示在最前面

表示窗口是否始终显示在最前面 ( 最前方 )。也可以设置值。

真的话窗口将始终显示在最前面。

在当前版本中，窗口进入全屏或从全屏恢复时，该属性的设置内容可能会丢失。

---

### imeMode

属性 \ 访问: `r/w`

**说明**

默认的 IME 模式

表示默认的 IME 模式。

这里指定的模式，是在任何图层都没有焦点时被设置的模式。

未指定时为 **imClose**，也就是在任何图层都没有焦点的状态下 IME 处于关闭状态 ( 英数输入 )。

可指定的值请参阅 [Layer.imeMode](Layer.md#imemode)。

写入仅在 Windows 原生 ( WINVER ) 构建中有效。在 SDL3 构建中
读写都未实现 ( 异常 )。

设置在任何图层都没有焦点时会立即生效。有持有
焦点的图层时，优先使用该图层的 [Layer.imeMode](Layer.md#imemode)，
失去焦点时会回到这里指定的默认值。

ElementsDialog 的文本输入框持有编辑焦点期间，无论这里的指定如何，
IME 都会打开 ( 失去焦点后会回到这里指定的默认值 )。
在此期间，图层侧 [Layer.imeMode](Layer.md#imemode) 的应用也会被延后，
在失去焦点的时点一并生效。

另外，该属性返回的只是**默认值**。不会返回有焦点的图层或
ElementsDialog 实际应用的 IME 状态，因此
不能用于确认“IME 是否打开”
( 确认请使用 [Agent.dialogs](Agent.md#dialogs) 的 `textFocus` )。

---

### mouseCursorState

属性 \ 访问: `r/w`

**说明**

鼠标光标显示状态

表示鼠标光标的显示状态。也可以设置值。

指定 `**mcsVisible**` 时，鼠标光标变为显示状态。这是默认状态。

指定 `**mcsTempHidden**` 时，鼠标光标变为非显示状态，但只要稍微移动鼠标就会变为 `mcsVisible`，进入显示状态。调用 [Window.hideMouseCursor](Window.md#hidemousecursor) 方法后会变为该状态。

指定 `**mcsHidden**` 时，鼠标光标变为非显示状态。即使移动鼠标也不会变为显示状态。

---

### useMouseKey

属性 \ 访问: `r/w`

**说明**

是否使用鼠标键

表示是否使用鼠标键。也可以设置值。

真的话可以使用鼠标键。

鼠标键有效后，可以使用方向键移动鼠标光标，
但完全不再发生键输入类事件。

---

### fullScreen

属性 \ 访问: `r/w`

**说明**

是否为全屏

表示是否为**全屏**。也可以设置值。

指定真时，当前窗口的客户区将变为全屏。全屏
时的画面分辨率变为客户区的大小。

指定假时变为窗口显示。

---

### mainWindow

属性 \ 访问: `r`

**说明**

主窗口

表示主窗口 ( 最初创建的窗口 )。

---

### focusedLayer

属性 \ 访问: `r/w`

**说明**

持有焦点的图层对象

表示当前持有**焦点**的图层对象。
也可以设置值。

为 null 时，任何图层都不持有焦点。设置图层对象
后，焦点会移动到该图层。

---

### primaryLayer

属性 \ 访问: `r`

**说明**

主图层对象

表示**主图层**对象。

---

### HWND

属性 \ 访问: `r`

**说明**

窗口句柄

表示窗口句柄。

这里得到的是整数，插件等使用该数值时请
强制转换为 HWND 类型后再使用。

**相关:** [Window.registerMessageReceiver](Window.md#registermessagereceiver)

---

### touchScaleThreshold

属性 \ 访问: `r/w`

**说明**

多点触控放大阈值

开始多点触控放大的阈值。

两个触摸位置的距离变化达到该值以上时，会发生放大事件。

一旦超过阈值，放大事件将保持有效，直到手指暂时离开。

**相关:** [Window.onTouchScaling](Window.md#ontouchscaling)

---

### touchRotateThreshold

属性 \ 访问: `r/w`

**说明**

多点触控旋转阈值

开始多点触控旋转的阈值。

各触摸位置的移动距离变化达到该值以上时，会发生旋转事件。

一旦超过阈值，旋转事件将保持有效，直到手指暂时离开。

**相关:** [Window.onTouchRotate](Window.md#ontouchrotate)

---

### touchPointCount

属性 \ 访问: `r`

**说明**

触摸数

被触摸到触摸面板上的数量。

**相关:** [Window.getTouchPoint](Window.md#gettouchpoint)

---

### enableTouch

属性 \ 访问: `r/w`

**说明**

触摸事件有效/无效

表示**触摸事件**是否有效。也可以设置值。

指定真后，[Window.onTouchDown](Window.md#ontouchdown) 等事件变为有效，触摸操作时不再发生 [Window.onMouseDown](Window.md#onmousedown) 等。

存在触摸设备且多点触控有效的环境中，默认为 true。

---

### waitVSync

属性 \ 访问: `r/w`

**说明**

垂直同步等待

设置在进行转场 ( 画面切换 ) 等时是否等待显示器的垂直同步后再绘制。

更改设置有时可以抑制画面闪烁，但也可能降低绘制性能。

默认为真 ( 为了抑制在绘制较轻松的场景中过度重绘、击发过多帧的现象 )。想按以往方式始终重绘时请设置假。

---

### hintDelay

属性 \ 访问: `r/w`

**说明**

提示显示的等待时间

以毫秒为单位表示提示显示的等待时间。也可以设置值。

默认是 500 毫秒。

设置 0 时，会立即调用 [Window.onHintChanged](Window.md#onhintchanged) ( 始终显示状态 )。

设置 -1 时不会显示提示。

**相关:** [Window.onHintChanged](Window.md#onhintchanged)

---

### displayOrientation

属性 \ 访问: `r`

**说明**

显示器的方向 ( 1.1.0 起 )

表示显示器的方向。

为 oriUnknown ( 获取失败/不明 )、oriPortrait ( 纵向 )、oriLandscape ( 横向 ) 中的某一个值。

**相关:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayRotate](Window.md#displayrotate)

---

### displayRotate

属性 \ 访问: `r`

**说明**

显示器的旋转角度 ( 1.1.0 起 )

表示显示器的旋转角度。

为 0、90、180、270、-1 中的某一个，无法获取时为 -1。

**相关:** [Window.onDisplayRotate](Window.md#ondisplayrotate) / [Window.displayOrientation](Window.md#displayorientation)

---

### displayDensity

属性 \ 访问: `r/w`

**说明**

画面密度 (dpi)

返回 dpi 值 ( 96 为等倍 = 100%，192 则为 200% )。
只可读取。

返回窗口所在显示器的值。 在多显示器中
移动到放大率不同的显示器时值会变化。

!!! note "即使移动显示器，窗口的大小也不会变化"
即使移动到放大率不同的显示器，
[Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight)
( 绘制区域的像素大小 ) 会得到保持。变化的只有边框的粗细，
游戏画面的观感也不会改变。 取而代之的是，在放大率高的显示器上
窗口看上去会变小。
Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都会
返回实际值 ( SDL3 侧在 2026-08-17 之前固定为 96 )。

---

### enableTouchMouse

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

触摸操作的鼠标模拟有效/无效

为真时，把触摸事件转换为模拟的鼠标事件并
通知给 `Window.onMouseDown` 系处理器。

!!! note "iOS / iPadOS 的触摸操作 ( 2026-10 起 )"
    iOS 版由引擎独自把触摸转换为鼠标，并追加以下 2 种双指手势。
    把该属性设为假后，包含手势在内都会停止转换。

    | 操作 | 被通知的内容 |
    |---|---|
    | 1 根手指触摸 | 约 100ms 保留后按下左键 ( 开始移动的时点确定 )。以后是通常的拖拽 / 点击 |
    | 2 根手指点击 ( 不移动直接离开 ) | ESC 键 ( “返回”。作为键事件送达，因此可用 `onKeyDown` 或热键接收 ) |
    | 2 根手指上下移动 | 鼠标滚轮 ( 手指向上 = 向下滚动 ) |

    从第 1 根手指触摸起约 100ms 以内第 2 根手指触摸的话会变为双指手势，不发生左键点击。
    坐标以游戏画面 ( 考虑了黑边显示的绘制区域 ) 的坐标送达。

---

### innerSunken

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

内侧凹陷显示的有效/无效 ( 预定废止 )

设为真时，在窗口的客户区显示“凹陷”风格的镶边。
是面向 `USE_OBSOLETE_FUNCTIONS` 有效构建的兼容属性，
不建议在新代码中使用。

---

### layerEventTarget

属性 \ 访问: `r/w`

**说明**

图层事件的转送目标对象

指定接收鼠标、键输入等图层事件的对象。
通常使用 `Window` 自身。设置 null 后返回默认。

---

### layerLeft

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

主图层的 X 位置 ( 预定废止 )

获取 / 设置主图层在窗口客户区内的左端位置。
是面向 `USE_OBSOLETE_FUNCTIONS` 有效构建的兼容属性。
新代码中请使用 `Window.setLayerPos` 的替代途径。

---

### layerTop

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

主图层的 Y 位置 ( 预定废止 )

获取 / 设置主图层在窗口客户区内的上端位置。
是面向 `USE_OBSOLETE_FUNCTIONS` 有效构建的兼容属性。

---

### layerTreeOwnerInterface

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

LayerTreeOwner 接口指针

以 64bit 整数返回 `iTVPLayerTreeOwner` 接口的 C++ 指针。
用于从插件直接访问窗口的图层树所有者。
只读。

---

### mouseCursor

属性 \ 访问: `r/w`

**说明**

鼠标光标的设置

获取 / 设置当前的鼠标光标。

设置时传入字符串的话，将其作为存储名加载光标图像。
传入数值的话，会解释为标准鼠标光标常量 ( `crArrow` 等 )。

**相关:** [Window.mouseCursorState](Window.md#mousecursorstate)

---

### showScrollBars

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

滚动条显示的有效/无效 ( 预定废止 )

在主图层比窗口大的情况下，获取 / 设置是否显示滚动条。
是面向 `USE_OBSOLETE_FUNCTIONS` 有效构建的兼容属性。

---

### GLGetProcAddress

属性 \ 访问: `r`

**类型**: `Integer`

**说明**

指向 GL 入口点解析函数的指针 ( 整数 )

作为 GLES 系插件 ( EffekseerDevice 等 ) 的 oglbase 使用。首次
访问时如果 GL 上下文尚未初始化，则延迟创建并使其成为当前上下文
( 即使使用 OGLDrawDevice / Canvas 也可以从窗口获取 )。在无法
获取 GL 的环境中返回 0 ( null )。

---

### maximized

属性 \ 访问: `r`

**类型**: `Boolean`

**说明**

是否处于最大化

窗口处于最大化时为真。更改通过
[Window.maximize](Window.md#maximize) / [Window.showRestore](Window.md#showrestore) 进行。

WINVER / SDL3 系构建双方都可以使用。

**相关:** [Window.maximize](Window.md#maximize) / [Window.minimized](Window.md#minimized)

---

### minimized

属性 \ 访问: `r`

**类型**: `Boolean`

**说明**

是否处于最小化

窗口处于最小化 ( 图标化 ) 时为真。

**相关:** [Window.minimize](Window.md#minimize) / [Window.maximized](Window.md#maximized)

---

### disableResize

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

禁止更改大小

设为真后，用户无法抓住边框更改窗口大小。
在 SDL3 系构建中也有效。

**相关:** [Window.disableMove](Window.md#disablemove)

---

### disableMove

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

禁止移动

设为真后，用户无法抓住窗口进行移动。
在无边框显示时使用。

仅在 WINVER 构建中有效。SDL3 系构建只是保持值
( 因为 SDL 没有阻止移动的手段 )。

**相关:** [Window.disableResize](Window.md#disableresize)

---

### close

方法

**说明**

关闭窗口

关闭通过 [Window.showModal](Window.md#showmodal) 方法显示的窗口。在关闭窗口之前会发生 [Window.onCloseQuery](Window.md#onclosequery) 事件，可以确认是否能够关闭窗口。

**相关:** [Window.showModal](Window.md#showmodal) / [Window.onCloseQuery](Window.md#onclosequery)

---

### bringToFront

方法

**说明**

将窗口移动到最前面

将窗口移动到最前面。应用程序处于非活动状态时，应用程序
自身也会变为活动状态。

---

### update

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `tutNormal` | 指定窗口绘制类型。<br>指定 `**tutNormal**` 时进行通常的绘制 ( 差分绘制 )，<br>指定 `**tutEntire**` 时绘制窗口内容全体。 |

**说明**

窗口内容的强制绘制

在当前版本中参数被忽略。

tutNormal 和 tutEntire 未实现。

---

### showModal

方法

**说明**

以模态显示窗口

以**模态** ( **带模式** ) 显示窗口。
该方法使窗口进入显示状态，
并且临时禁用其他窗口。因此用户只能
访问该窗口 ( 这称为带模式的状态 )。窗口被关闭后
带模式的状态即被解除。

调用该方法时，窗口必须处于非显示状态。
此外，在只有 1 个窗口的状态下无法调用 ( 会成为异常 )。

窗口在调用 [Window.close](Window.md#close) 或按下窗口的
关闭按钮时退出带模式状态，处理从 `showModal` 返回。

> 在无法创建多个窗口的环境 ( 移动端/主机等 ) 中，
> 由于第 2 个窗口本身无法创建，会成为异常。在这样的环境中
> 请采用不使用模态窗口的设计。

带模式期间内部会运行嵌套的事件循环，因此**绘制、定时器、
Continuous 处理器会持续运行**。停止的只有对其他窗口的用户输入。
Windows 原生 ( WINVER ) 构建与 SDL3 构建双方都可以使用
( SDL3 构建于 2026-08-15 支持 )。

可以确认运行情况的核心演示是 `window_multi`。

---

### setMaskRegion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `threshold` | `1` | 指定遮罩的阈值 ( 门限值 )。<br>主图层的遮罩 ( 图层的不透明度信息 ) 中，大于该值的部分<br>的形状会成为窗口被裁剪后的显示。 |

**说明**

按照遮罩设置窗口区域

按照主图层的遮罩 ( 图层的不透明度信息 ) 设置窗口区域。

可以使窗口变为异形。

为了使显示的窗口与主图层的大小、位置不错位，
需要执行以下操作。

- 将 [Window.borderStyle](Window.md#borderstyle) 设置为 bsNone。
- 将 [Layer.imageLeft](Layer.md#imageleft) 和 [Layer.imageTop](Layer.md#imagetop) 设置为 0。

**相关:** [Window.removeMaskRegion](Window.md#removemaskregion)

---

### removeMaskRegion

方法

**说明**

解除窗口区域

解除通过 [Window.setMaskRegion](Window.md#setmaskregion) 设置的窗口区域，把窗口恢复为矩形。

**相关:** [Window.setMaskRegion](Window.md#setmaskregion)

---

### add

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 指定被管理的对象。 |

**说明**

添加管理对象

添加管理对象。这里指定的对象，将在窗口被无效化
时自动被无效化。

**相关:** [Window.remove](Window.md#remove)

---

### remove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 指定要从管理对象列表中删除的对象。 |

**说明**

删除管理对象

从管理对象列表中删除指定的对象。

**相关:** [Window.add](Window.md#add)

---

### setSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 指定窗口的宽度。 |
| `height` | `&nbsp;` | 指定窗口的高度。 |

**说明**

窗口大小的设置

指定窗口的大小。

指定窗口大小时，使用该方法一次性指定比
分别设置 [Window.width](Window.md#width) 和
[Window.height](Window.md#height) 属性更高效。

!!! tip "推荐使用以内侧 ( 绘制区域 ) 为基准的 API"
    该值是**包含窗口装饰的外形**尺寸。装饰的有无与粗细会随
    平台、OS 主题、[Window.borderStyle](Window.md#borderstyle) 而
    变化，在不带装饰的环境 ( 移动端 / 主机，`bsNone` 时 ) 中
    与内侧尺寸同值。 可移植的代码请使用游戏画面直接对应的
    [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) /
    [Window.setInnerSize](Window.md#setinnersize)。
    需要边框部分时，可以加上 [Window.frameWidth](Window.md#framewidth) /
    [Window.frameHeight](Window.md#frameheight)。

**相关:** [Window.width](Window.md#width) / [Window.height](Window.md#height) / [Window.setPos](Window.md#setpos) / [Window.setInnerSize](Window.md#setinnersize) / [Window.setMinSize](Window.md#setminsize) / [Window.setMaxSize](Window.md#setmaxsize)

---

### setMinSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 指定窗口的最小宽度。指定 0 时限制将取消。 |
| `height` | `&nbsp;` | 指定窗口的最小高度。指定 0 时限制将取消。 |

**说明**

窗口最小大小的设置

指定窗口的最小大小。窗口不能变得比该方法指定的大小更小。

!!! note "基准是内侧 ( 绘制区域 ) 大小"
    指定的值与 [Window.innerWidth](Window.md#innerwidth) /
    [Window.innerHeight](Window.md#innerheight) 同样是“去掉窗口边框的
    绘制区域”的大小 ( 2026-08-17 从外形基准更改。因为在不带装饰的
    平台上无法定义外形基准 )。 需要含边框的值时请加上
    [Window.frameWidth](Window.md#framewidth) / [Window.frameHeight](Window.md#frameheight)。

**相关:** [Window.setMaxSize](Window.md#setmaxsize) / [Window.setSize](Window.md#setsize) / [Window.minWidth](Window.md#minwidth) / [Window.minHeight](Window.md#minheight)

---

### setMaxSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 指定窗口的最大宽度。指定 0 时限制将取消。 |
| `height` | `&nbsp;` | 指定窗口的最大高度。指定 0 时限制将取消。 |

**说明**

窗口最大大小的设置

指定窗口的最大大小。窗口不能变得比该方法指定的大小更大。

!!! note "基准是内侧 ( 绘制区域 ) 大小"
    指定的值与 [Window.innerWidth](Window.md#innerwidth) /
    [Window.innerHeight](Window.md#innerheight) 同样是“去掉窗口边框的
    绘制区域”的大小 ( 2026-08-17 从外形基准更改。因为在不带装饰的
    平台上无法定义外形基准 )。 需要含边框的值时请加上
    [Window.frameWidth](Window.md#framewidth) / [Window.frameHeight](Window.md#frameheight)。

**相关:** [Window.setMinSize](Window.md#setminsize) / [Window.setSize](Window.md#setsize) / [Window.maxWidth](Window.md#maxwidth) / [Window.maxHeight](Window.md#maxheight)

---

### setPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 指定窗口的左端位置。 |
| `top` | `&nbsp;` | 指定窗口的上端位置。 |

**说明**

窗口位置的设置

指定窗口的位置。

指定窗口位置时，使用该方法一次性指定比
分别设置 [Window.left](Window.md#left) 和
[Window.top](Window.md#top) 属性更高效。

**相关:** [Window.left](Window.md#left) / [Window.top](Window.md#top) / [Window.setSize](Window.md#setsize)

---

### setInnerSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 指定客户区的宽度。 |
| `height` | `&nbsp;` | 指定客户区的高度。 |

**说明**

客户区大小的设置

指定窗口的客户区大小。

客户区是可以显示图层的窗口内区域。

设置该大小后，窗口的大小也会相应变化。

指定客户区大小时，使用该方法一次性指定比
分别设置 [Window.innerWidth](Window.md#innerwidth) 和
[Window.innerHeight](Window.md#innerheight) 属性更高效。

**相关:** [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight)

---

### setZoom

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `numer` | `&nbsp;` | 以整数指定倍率的分子。 |
| `denom` | `&nbsp;` | 以整数指定倍率的分母。 |

**说明**

图层放大倍率的设置

指定图层的放大倍率。图像会以分子/分母指定的大小被放大或缩小后显示。

分子、分母存在公约数时会自动约分，因此通过 [Window.zoomNumer](Window.md#zoomnumer) 属性或 [Window.zoomDenom](Window.md#zoomdenom) 属性读取到的值，可能与该方法指定的值不同。

在当前版本的吉里吉里中，放大、缩小时是否进行插值会受到显卡硬件和驱动程序的影响。在不进行插值的硬件或驱动程序中，画质会变得粗糙。

根据选项的不同，吉里吉里会在每次更改倍率时调查可用于放大、缩小的硬件，因此该方法不适合用于连续改变放大率进行演出的用途。

该方法意味着“把窗口的内侧大小 ( [Window.innerWidth](Window.md#innerwidth) /
[Window.innerHeight](Window.md#innerheight) ) 变为图层大小 × 倍率”。
窗口会被调整到该大小，内容按倍率缩放显示。
Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建的行为相同
( WINVER 侧于 2026-08-17 对齐。此前只是记住倍率，
窗口不会被调整大小，需要通过 [Window.setInnerSize](Window.md#setinnersize)
显式指定 )。

!!! note "无法调整大小的情况"
    在无法更改窗口大小的环境 ( 移动端 / 主机等 ) 中，或者
    指定值低于 OS 的最小窗口大小时，内侧尺寸可能
    不会如指定那样。即使在这种情况下，游戏画面也会
    按照 [Window.setViewport](Window.md#setviewport) 的设置被放置到内侧。

**相关:** [Window.zoomNumer](Window.md#zoomnumer) / [Window.zoomDenom](Window.md#zoomdenom)

---

### setViewport

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fit` | `&nbsp;` | 以字符串指定适应方式。`"contain"` ( 保持宽高比能容纳的最大、黑边。默认 ) / `"cover"` ( 保持宽高比填满的最小、超出部分 clip ) / `"fill"` ( 无视宽高比拉伸到全面 ) / `"none"` ( 原尺寸 ) / `"integer"` ( 在能容纳的范围内取最大整数倍。最低 1 倍 ) / `"custom"` ( 使用 [Window.viewportZoom](Window.md#viewportzoom) 的倍率 ) 中的某一个。 |
| `zoom` | `&nbsp;` | 以实数指定 `"custom"` 时的放大倍率 ( 例 1.8 = 180% )。 |
| `alignX` | `&nbsp;` | 以实数指定水平配置。0=左 / 0.5=中央 / 1=右。 |
| `alignY` | `&nbsp;` | 以实数指定垂直配置。0=上 / 0.5=中央 / 1=下。 |
| `offsetX` | `&nbsp;` | 以整数指定在 align 后加算的水平偏移 ( px、surface 坐标 )。 |
| `offsetY` | `&nbsp;` | 以整数指定在 align 后加算的垂直偏移 ( px )。 |

**说明**

视口（显示视野）的批量设置

批量设置如何把内侧游戏画面 ( primaryLayer 的大小 ) 放置在外侧窗口 ( 由 [Window.innerWidth](Window.md#innerwidth) / [Window.innerHeight](Window.md#innerheight) 表示的 surface ) 之中。两者的尺寸一致时按以往方式全面等倍显示，设为不同大小后游戏会按照本设置被放置到 surface 内，并产生余白。余白由 [Window.viewportBgColor](Window.md#viewportbgcolor) 或 [Window.setViewportWallpaper](Window.md#setviewportwallpaper) 填充 ( Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用。WINVER 支持为 2026-08-17 )。

鼠标坐标会根据配置自动校正为游戏逻辑坐标，因此无论哪种设置，输入都会正确送达游戏内部。

各参数与分别设置对应属性 ( [Window.viewportFit](Window.md#viewportfit) 等 ) 相同。省略的参数不会被更改。

想回到与以往 ( 吉里吉里2 / 吉里吉里Z ) 相同的“即使把窗口拉宽，游戏仍保持原尺寸、在左上”的
显示时，请指定 `setViewport("none", 1.0, 0, 0)`
( 详情请参阅 [Window.viewportFit](Window.md#viewportfit) )。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.viewportFit](Window.md#viewportfit) / [Window.viewportZoom](Window.md#viewportzoom) / [Window.viewportAlignX](Window.md#viewportalignx) / [Window.viewportAlignY](Window.md#viewportaligny) / [Window.viewportOffsetX](Window.md#viewportoffsetx) / [Window.viewportOffsetY](Window.md#viewportoffsety) / [Window.setViewportWallpaper](Window.md#setviewportwallpaper)

---

### setViewportWallpaper

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `image` | `&nbsp;` | 指定壁纸图像。传入存储名 ( 字符串 ) 时内部会生成 [Bitmap](Bitmap.md) 并加载。也可以直接传入 [Layer](Layer.md) 或 [Bitmap](Bitmap.md) 对象，这种情况下对象会被引用保持，绘制时获取图像。 |
| `fit` | `"cover"` | 以字符串指定壁纸的适应方式。默认是 `"cover"`。可指定的值与 [Window.setViewport](Window.md#setviewport) 的 fit 相同。 |
| `alignX` | `0.5` | 以实数指定壁纸的水平配置。0=左 / 0.5=中央 / 1=右。默认是 0.5。 |
| `alignY` | `0.5` | 以实数指定壁纸的垂直配置。0=上 / 0.5=中央 / 1=下。默认是 0.5。 |

**说明**

视口余白的壁纸图像设置

设置用于填充视口产生的余白 ( 内侧游戏画面的外侧 ) 的壁纸图像。在游戏绘制之前作为背景被绘制。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.clearViewportWallpaper](Window.md#clearviewportwallpaper) / [Window.viewportBgColor](Window.md#viewportbgcolor) / [Window.setViewport](Window.md#setviewport)

---

### clearViewportWallpaper

方法

**说明**

解除视口余白的壁纸图像

解除通过 [Window.setViewportWallpaper](Window.md#setviewportwallpaper) 设置的壁纸。此后，余白仅用 [Window.viewportBgColor](Window.md#viewportbgcolor) 的背景色涂填。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以使用 ( WINVER 支持为 2026-08-17 )。

**相关:** [Window.setViewportWallpaper](Window.md#setviewportwallpaper) / [Window.viewportBgColor](Window.md#viewportbgcolor)

---

### postInputEvent

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `eventname` | `&nbsp;` | 指定事件名称。用以下字符串指定。<br>- "**onKeyDown**" 生成 [Window.onKeyDown](Window.md#onkeydown) 事件。<br>- "**onKeyPress**" 生成 [Window.onKeyPress](Window.md#onkeypress) 事件。<br>- "**onKeyUp**" 生成 [Window.onKeyUp](Window.md#onkeyup) 事件。onKeyDown 与 onKeyUp 是成对的，因此生成 onKeyDown 后建议也生成对应的 onKeyUp。 |
| `params` | `null` | 指定存有事件参数的字典数组。<br>- "onKeyDown" 事件和 "onKeyUp" 事件中，"key" 存放虚拟键码，"shift" 存放 Shift 状态。省略 "shift" 时视为 0。<br>- "onKeyPress" 事件中 "key" 指定字符。 |

**说明**

输入事件的生成

生成输入事件。在当前版本中可以生成与键输入有关的 3 个事件。

该方法把事件作为异步事件生成。也就是说，该方法不等对应的事件处理器结束就返回。实际调用事件处理器进行处理，是在控制权一度返回吉里吉里之后。

输入事件除了 Window 类之外，与通常的输入事件一样，也会作为 Layer 类的相应事件发生。

postInputEvent('onKeyDown', %[key: VK_UP, shift: ssShift]);

postInputEvent('onKeyUp',   %[key: VK_UP, shift: ssShift]);

// 按下左方向键

---

### hideMouseCursor

方法

**说明**

临时隐藏鼠标光标

临时隐藏鼠标光标。只要稍微移动鼠标，
鼠标光标就会重新显示。

该方法与把 [Window.mouseCursorState](Window.md#mousecursorstate) 设置为 `**mcsTempHidden**` 具有相同的效果。

---

### registerMessageReceiver

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mode` | `&nbsp;` | 指定是注册还是删除注册。<br>指定 **wrmRegister** 则为注册。指定 **wrmUnregister** 则为<br>删除注册。<br>以 wrm 开头的常量定义在 tp_stub.h 中。 |
| `func` | `&nbsp;` | 指定消息接收函数。<br>消息接收函数需要是 bool __stdcall func(void *userdata, tTVPWindowMessage *Message)<br>的形式，在传给该方法时需要把该函数指针强制转换为整数型后传入。<br>结构体 tTVPWindowMessage 定义在 tp_stub.h 中。<br>该函数返回 true 时，吉里吉里本体侧将不再与该窗口消息相关。 |
| `userdata` | `&nbsp;` | 指定要传给 func 参数指定的接收函数的 userdata 参数的数据指针。<br>传给该方法时需要把该指针强制转换为整数型后传入。<br>当 mode 参数不是 wrmRegister 时，该参数被忽略。 |

**说明**

消息接收函数的注册/删除注册

该方法设想由用 C++ 等编写的插件使用。无法从 TJS2
正常使用。

通过该方法，可以注册用于拦截通过该窗口的消息的消息接收函数。在消息接收函数中，除了通常的窗口消息外，
还可以拦截 TVP_WM_DETACH 和 TVP_WM_ATTACH 这 2 个重要消息，
可用于在窗口重建或销毁的时机卸下子窗口
这样的用途。

吉里吉里源码发布包中的 src/plugins/win32/wmrdump 中有简单使用方法的说明。

**相关:** [Window.HWND](Window.md#hwnd)

---

### postMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | 以整数指定要发送的窗口消息 ID。 |
| `wparam` | `&nbsp;` | 以整数指定要传给 wParam 的值。 |
| `lparam` | `&nbsp;` | 以整数指定要传给 lParam 的值。 |

**说明**

窗口消息的投递

向该窗口的原生消息队列异步投入指定的
窗口消息。
主要作为 C++ 插件向窗口发送通知的入口使用。

**相关:** [Window.registerMessageReceiver](Window.md#registermessagereceiver)

---

### getTouchPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 指定触摸坐标数组的索引。 |

**说明**

触摸坐标的获取

从当前的触摸坐标数组中获取指定索引的坐标信息。

坐标数可以通过 [Window.touchPointCount](Window.md#touchpointcount) 属性获取。

坐标信息以包含以下元素的字典返回。

`**startX**     : `该触摸的开始坐标的 x 坐标值 ( 客户端坐标系 )

`**startY**   : `该触摸的开始坐标的 y 坐标值 ( 客户端坐标系 )

`**x**    : `该触摸的当前坐标的 x 坐标值 ( 客户端坐标系 )

`**y**    : `该触摸的当前坐标的 y 坐标值 ( 客户端坐标系 )

`**ID**    : `该触摸的识别用 ID

**相关:** [Window.touchPointCount](Window.md#touchpointcount)

---

### getMouseVelocity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 返回 X 轴方向的鼠标坐标移动速度。 |
| `y` | `&nbsp;` | 返回 Y 轴方向的鼠标坐标移动速度。 |
| `speed` | `&nbsp;` | 返回鼠标坐标移动速度。 |

**返回值**

返回获取成功还是失败

**说明**

鼠标坐标移动速度的获取 ( 1.1.0 起 )

以 pixel / sec 获取当前的鼠标移动速度。

从进入窗口内的瞬间开始计测。

可以使用 [Window.resetMouseVelocity](Window.md#resetmousevelocity) 重置计测，从而能够从任意时机开始计测。

**相关:** [Window.getTouchVelocity](Window.md#gettouchvelocity) / [Window.resetMouseVelocity](Window.md#resetmousevelocity)

---

### getTouchVelocity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 指定触摸 ID。 |
| `x` | `&nbsp;` | 返回 X 轴方向的鼠标坐标移动速度。 |
| `y` | `&nbsp;` | 返回 Y 轴方向的鼠标坐标移动速度。 |
| `speed` | `&nbsp;` | 返回鼠标坐标移动速度。 |

**返回值**

返回获取成功还是失败

**说明**

触摸坐标移动速度的获取 ( 1.1.0 起 )

以 pixel / sec 获取当前的触摸移动速度。

从按下到离开为止的期间被计测。

为了支持多点触控，按 ID 分别计测速度。

[Window.onTouchUp](Window.md#ontouchup) 事件的方法调用结束后，计测中的速度信息会消失，需要注意。

**相关:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### resetMouseVelocity

方法

**说明**

重置鼠标坐标移动速度的计测 ( 1.1.0 起 )

重置鼠标坐标移动速度的计测。

通过重置，可以从任意时机开始速度计测。

**相关:** [Window.getMouseVelocity](Window.md#getmousevelocity)

---

### beginMove

方法

**说明**

窗口的拖拽移动开始 ( 预定废止 )

进行与拖拽窗口标题栏时同等的移动操作，从当前鼠标位置
开始。是面向 `USE_OBSOLETE_FUNCTIONS` 有效构建的兼容方法。

---

### requestUpdate

方法

**说明**

绘制更新的请求

对窗口请求重绘 ( 下一帧的 `Update` )。
不是立即绘制，而是在下一次更新时机统一生效。

**相关:** [Window.update](Window.md#update)

---

### setLayerPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | X 坐标 |
| `top` | `&nbsp;` | Y 坐标 |

**说明**

主图层位置的设置 ( 预定废止 )

设置窗口客户区内的主图层位置 ( 左上 )。
是面向 `USE_OBSOLETE_FUNCTIONS` 有效构建的兼容方法。

---

### maximize

方法

**说明**

最大化

将窗口最大化。
不会经过 [Window.onMaximizeQuery](Window.md#onmaximizequery)
( 来自程序的最大化被视为有意为之 )。

**相关:** [Window.showRestore](Window.md#showrestore) / [Window.maximized](Window.md#maximized)

---

### minimize

方法

**说明**

最小化

将窗口最小化 ( 图标化 )。

**相关:** [Window.showRestore](Window.md#showrestore) / [Window.minimized](Window.md#minimized)

---

### showRestore

方法

**说明**

恢复为原来的大小

把已最大化 / 最小化的窗口恢复为原来的位置和大小。

**相关:** [Window.maximize](Window.md#maximize) / [Window.minimize](Window.md#minimize)

---

### getNormalRect

方法

**返回值**

返回矩形的字典。无法获取时返回 void。

**说明**

原始矩形的获取

以 `%[ x, y, w, h ]` 的字典返回未最大化 / 最小化时的窗口外形矩形 ( 屏幕坐标 )。即使在最大化中也能获取“恢复时的位置和大小”，
可用于下次启动时的恢复等。

**相关:** [Window.getWindowRect](Window.md#getwindowrect)

---

### getWindowRect

方法

**返回值**

返回矩形的字典。

**说明**

窗口矩形的获取

以屏幕坐标的 `%[ x, y, w, h ]` 返回包含边框和标题栏的窗口外形矩形。

**相关:** [Window.getClientRect](Window.md#getclientrect) / [Window.getNormalRect](Window.md#getnormalrect)

---

### getClientRect

方法

**返回值**

返回矩形的字典。

**说明**

客户区矩形的获取

以屏幕坐标的 `%[ x, y, w, h ]` 返回绘制区域 ( 客户区 ) 的矩形。

**相关:** [Window.setClientRect](Window.md#setclientrect) / [Window.getWindowRect](Window.md#getwindowrect)

---

### setCursorPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定绘制区域坐标中的 x 坐标值。 |
| `y` | `&nbsp;` | 以像素为单位指定绘制区域坐标中的 y 坐标值。 |

**说明**

鼠标光标位置的指定 ( 绘制区域坐标 )

以**绘制区域坐标** ( 以绘制区域左上为原点的像素坐标 ) 指定鼠标光标的
位置。

与 [Layer.setCursorPos](Layer.md#setcursorpos) 同名，但**坐标系不同**。
如果持有图层坐标的值，请使用那个。这个方法是为了“想直接填入绘制区域坐标的
值”的情况。

代表性例子是 [Window.onTouchScaling](Window.md#ontouchscaling) 和
[Window.onTouchRotate](Window.md#ontouchrotate) 的 `cx` / `cy`。它们与
鼠标事件不同，不会转换为图层坐标就送达，因此要换算成图层坐标需要
绘制目标的矩形，但该矩形无法从脚本获取。
使用这个方法就可以直接传入。

Windows 原生 ( WINVER ) 构建与 SDL3 / 通用构建双方都可以运行。

**相关:** [Window.getCursorPos](Window.md#getcursorpos) / [Layer.setCursorPos](Layer.md#setcursorpos)

---

### getCursorPos

方法

**说明**

鼠标光标位置的获取 ( 绘制区域坐标 )

以与 [Window.setCursorPos](Window.md#setcursorpos) 相同的**绘制区域坐标**，把当前的
鼠标光标位置以 `%[ x, y ]` 的字典返回。

想以图层坐标读取时，请使用 [Layer.cursorX](Layer.md#cursorx) /
[Layer.cursorY](Layer.md#cursory)。

**相关:** [Window.setCursorPos](Window.md#setcursorpos) / [Layer.cursorX](Layer.md#cursorx)

---

### setClientRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | 指定 `%[ x, y, w, h ]` 的字典。 |

**返回值**

设置成功时返回真。

**说明**

客户区矩形的设置

移动、调整窗口大小，使客户区成为指定的屏幕坐标矩形。
字典中没有的元素保持当前值 ( `%[ w:320 ]` 的话只有宽度变化 )。

**相关:** [Window.getClientRect](Window.md#getclientrect)

---

### registerExEvent

方法

**说明**

扩展事件的有效化

调用后，与窗口边框操作有关的以下事件就会发生。
在调用之前不会发生。

| 事件 | 发生时 | SDL3 系构建 |
|---|---|---|
| [onMove](Window.md#onmove) | 移动了 | ○ |
| [onMoving](Window.md#onmoving) | 移动中 | × |
| [onResizing](Window.md#onresizing) | 大小更改中 | × |
| [onMoveSizeBegin](Window.md#onmovesizebegin) / [onMoveSizeEnd](Window.md#onmovesizeend) | 边框的拖拽开始 / 结束 | × |
| [onMinimize](Window.md#onminimize) / [onMaximize](Window.md#onmaximize) | 进行了最小化 / 最大化 | ○ |
| [onMaximizeQuery](Window.md#onmaximizequery) | 正试图最大化 | × |
| [onDPIChanged](Window.md#ondpichanged) | DPI 变化了 | ○ |
| [onDisplayChanged](Window.md#ondisplaychanged) | 画面构成变化了 | ○ |

SDL3 系构建中 × 的项，因为 SDL 没有拖拽中的问询，
只通知结果，因此不发生。

---

### registerDeviceChange

方法

**返回值**

有效时返回真。

**说明**

启用设备变化的通知

调用后，输入设备的拔出 / 插入会引发 [Window.onDeviceChanged](Window.md#ondevicechanged)。
引擎本体 ( 鼠标 / 手柄 ) 的输入会自行跟踪，
因此用于插件等自行枚举设备的情况。

---

### onMouseEnter

事件

**说明**

鼠标进入

在鼠标进入窗口的客户区内时发生。

**相关:** [Window.onMouseLeave](Window.md#onmouseleave)

---

### onMouseLeave

事件

**说明**

鼠标离开

在鼠标离开窗口的客户区内时发生。

**相关:** [Window.onMouseEnter](Window.md#onmouseenter)

---

### onClick

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 窗口被点击的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 窗口被点击的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |

**说明**

窗口被点击

在窗口被点击时发生。

**相关:** [Window.onMouseDown](Window.md#onmousedown) / [Window.onDoubleClick](Window.md#ondoubleclick)

---

### onDoubleClick

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 窗口被双击的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 窗口被双击的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |

**说明**

窗口被双击

在窗口被双击时发生。

**相关:** [Window.onClick](Window.md#onclick)

---

### onMouseDown

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标按钮被按下的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 鼠标按钮被按下的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |
| `button` | `&nbsp;` | 被按下的鼠标按钮。为以下某一个值。<br>`**mbLeft**    : `按下了鼠标左键<br>`**mbMiddle**  : `按下了鼠标中键<br>`**mbRight**   : `按下了鼠标右键<br>`**mbX1**      : `按下了鼠标侧键第 1 按钮<br>`**mbX2**      : `按下了鼠标侧键第 2 按钮 |
| `shift` | `&nbsp;` | 鼠标按钮被按下时同时按着的 Shift 系键的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键 |

**说明**

鼠标按钮被按下

在鼠标按钮被按下时发生。

**相关:** [Window.onClick](Window.md#onclick)

---

### onMouseUp

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标按钮被松开的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 鼠标按钮被松开的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |
| `button` | `&nbsp;` | 被松开的鼠标按钮。为以下某一个值。<br>`**mbLeft**    : `松开了鼠标左键<br>`**mbMiddle**  : `松开了鼠标中键<br>`**mbRight**   : `松开了鼠标右键<br>`**mbX1**      : `松开了鼠标侧键第 1 按钮<br>`**mbX2**      : `松开了鼠标侧键第 2 按钮 |
| `shift` | `&nbsp;` | 鼠标按钮被松开时同时按着的 Shift 系键的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键 |

**说明**

鼠标按钮被松开

在鼠标按钮被松开时发生。

---

### onMouseMove

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标移动到的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 鼠标移动到的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |
| `shift` | `&nbsp;` | 鼠标移动时同时按着的 Shift 系键或鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键 |

**说明**

鼠标移动了

在鼠标移动时发生。

---

### onMouseWheel

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `shift` | `&nbsp;` | 鼠标移动时同时按着的 Shift 系键或鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键 |
| `delta` | `&nbsp;` | 滚轮的旋转角。向上方向 ( 与用户相反的方向 ) 旋转时为正，<br>向下方向 ( 用户侧的方向 ) 旋转时为负值。通常，最小量为 120<br>。 |
| `x` | `&nbsp;` | 滚轮旋转的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 滚轮旋转的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |

**说明**

鼠标滚轮旋转了

在鼠标滚轮旋转时发生。

---

### onTouchDown

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 被触摸的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 被触摸的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |
| `cx` | `&nbsp;` | 手指接触的横向像素数。<br>设备不支持时始终为 1。 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数。<br>设备不支持时始终为 1。 |
| `id` | `&nbsp;` | 触摸 ID。<br>多点触控时，每个位置会被设置固有的值，通过该 ID 可以识别位置。 |

**说明**

画面被触摸

在触摸面板被触摸时发生。

---

### onTouchUp

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 被松开的位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 被松开的位置的 y 坐标 ( 以客户端坐标 ) 的值。 |
| `cx` | `&nbsp;` | 手指接触的横向像素数。<br>设备不支持时始终为 1。 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数。<br>设备不支持时始终为 1。 |
| `id` | `&nbsp;` | 触摸 ID。<br>多点触控时，每个位置会被设置固有的值，通过该 ID 可以识别位置。 |

**说明**

手指从画面离开

在手指从触摸面板离开时发生。

---

### onTouchMove

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 触摸位置的 x 坐标 ( 以客户端坐标 ) 的值。 |
| `y` | `&nbsp;` | 触摸位置的 y 坐标 ( 以客户端坐标 ) 的值。 |
| `cx` | `&nbsp;` | 手指接触的横向像素数。<br>设备不支持时始终为 1。 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数。<br>设备不支持时始终为 1。 |
| `id` | `&nbsp;` | 触摸 ID。<br>多点触控时，每个位置会被设置固有的值，通过该 ID 可以识别位置。 |

**说明**

手指移动了

在触摸面板上接触的手指移动时发生。

---

### onTouchScaling

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `startdistance` | `&nbsp;` | 多点触控开始时的像素距离。 |
| `currentdistance` | `&nbsp;` | 事件发生时的触摸像素距离。 |
| `cx` | `&nbsp;` | 中心位置的 x 坐标。以**绘制区域坐标** ( 以绘制区域左上为原点的像素坐标 ) 传递<br>( 可以直接传给 [Window.setCursorPos](#setcursorpos) )。需要图层坐标时请使用 [Layer.onTouchScaling](Layer.md#ontouchscaling)。 |
| `cy` | `&nbsp;` | 中心位置的 y 坐标。坐标系与 cx 相同。 |
| `flag` | `&nbsp;` | 多点触控状态标志。<br>`**0x01**     : `被设置在多点触控开始的最初事件上。 |

**说明**

进行了放大操作

在触摸面板上通过多点触控进行放大操作时发生。

---

### onTouchRotate

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `startangle` | `&nbsp;` | 多点触控开始时的弧度角。 |
| `currentangle` | `&nbsp;` | 事件发生时的触摸弧度角。 |
| `distance` | `&nbsp;` | 事件发生时的触摸像素距离。 |
| `cx` | `&nbsp;` | 中心位置的 x 坐标。以**绘制区域坐标** ( 以绘制区域左上为原点的像素坐标 ) 传递<br>( 可以直接传给 [Window.setCursorPos](#setcursorpos) )。需要图层坐标时请使用 [Layer.onTouchRotate](Layer.md#ontouchrotate)。 |
| `cy` | `&nbsp;` | 中心位置的 y 坐标。坐标系与 cx 相同。 |
| `flag` | `&nbsp;` | 多点触控状态标志。<br>`**0x01**     : `被设置在多点触控开始的最初事件上。 |

**说明**

进行了旋转操作

在触摸面板上通过多点触控进行旋转操作时发生。

---

### onMultiTouch

事件

**说明**

多点触控状态发生了变化

在多点触控状态开始、移动或离开时发生。

坐标信息可以通过 [Window.touchPointCount](Window.md#touchpointcount) 属性和 [Window.getTouchPoint](Window.md#gettouchpoint) 方法获取。

**相关:** [Window.getTouchPoint](Window.md#gettouchpoint) / [Window.touchPointCount](Window.md#touchpointcount)

---

### onKeyDown

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 被按下的键的**虚拟键码**的值。 |
| `shift` | `&nbsp;` | 键被按下时同时按着的 Shift 系键或鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键<br>另外，键盘被长时间按下、发生按键重复时，<br>以下值也会被组合。<br>`**ssRepeat**  : `发生了按键重复 |

**说明**

键被按下了

在键被按下时发生。

---

### onKeyUp

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 被松开的键的**虚拟键码**的值。 |
| `shift` | `&nbsp;` | 键被松开时同时按着的 Shift 系键或鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键 |

**说明**

键被松开了

在键被松开时发生。

---

### onKeyPress

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 输入的字符。 |

**说明**

输入了字符

在输入字符时发生。与 [Window.onKeyDown](Window.md#onkeydown) 不同的是，onKeyDown
处理虚拟键码，而该事件处理字符本身。按下的键是
与字符无关的键 ( 功能键等 ) 时，不会发生该事件。

与 Ctrl 键同时按下时，会送来如下所示的控制码。

`0x00 : `Ctrl+@

`0x01 : `Ctrl+A

`0x02 : `Ctrl+B

`0x03 : `Ctrl+C

`0x04 : `Ctrl+D

`0x05 : `Ctrl+E

`0x06 : `Ctrl+F

`0x07 : `Ctrl+G

`0x08 : `Ctrl+H

`0x09 : `Ctrl+I

`0x0A : `Ctrl+J

`0x0B : `Ctrl+K

`0x0C : `Ctrl+L

`0x0D : `Ctrl+M

`0x0E : `Ctrl+N

`0x0F : `Ctrl+O

`0x10 : `Ctrl+P

`0x11 : `Ctrl+Q

`0x12 : `Ctrl+R

`0x13 : `Ctrl+S

`0x14 : `Ctrl+T

`0x15 : `Ctrl+U

`0x16 : `Ctrl+V

`0x17 : `Ctrl+W

`0x18 : `Ctrl+X

`0x19 : `Ctrl+Y

`0x1A : `Ctrl+Z

`0x1B : `Ctrl+[

`0x1C : `Ctrl+\

`0x1D : `Ctrl+]

`0x1E : `Ctrl+^

`0x1F : `Ctrl+_

---

### onTextInput

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 输入的字符串。 |

**说明**

文本输入事件

是确定的输入字符串送达的事件。用 IME 转换确定的字符串会
汇总为 1 次送达，BMP 以外的字符 ( emoji 等 ) 也不会被
分解为代理对，而是 1 次送达。

以往的 [onKeyPress](#onkeypress) 是按 UTF-16 代码单元配送的，
因此**想以字符为单位接收的输入框实现请使用这个**。控制字符
( BS / Enter / Tab / Esc 等 ) 不会流到该事件
( 请用 [onKeyDown](#onkeydown) / onKeyPress 接收 )。

[ElementsDialog](ElementsDialog.md) 的文本输入框持有焦点期间，
对话框侧会消费输入，因此不会发生该事件。

**平台差异**

SDL3 系构建中直接配送 OS 的文本输入事件。
WINVER ( Windows 原生 ) 构建中由于从 `WM_CHAR` 合成，
会与 onKeyPress 并发 ( 内容为相同的字符 )。

向 Layer 侧，为了兼容会像以往一样配送分解为 UTF-16 代码单元的
[Layer.onKeyPress](Layer.md#onkeypress)。

**相关:** [Window.onKeyPress](Window.md#onkeypress)

---

### onResize

事件

**说明**

窗口的大小变化了

在窗口的大小变化时发生。

实际大小请通过 [Window.width](Window.md#width) 属性或 [Window.height](Window.md#height) 属性等获取。

---

### onFileDrop

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `files` | `&nbsp;` | 存放了被拖放文件名的数组 (Array) 对象。 |

**说明**

文件被拖放

在文件从资源管理器等被拖放到窗口时发生。

即使拖放的是单个文件，传给参数的也是数组对象 ( 最初的元素
即为该文件 )。

---

### onCloseQuery

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `canclose` | `&nbsp;` | 传递是否可以关闭窗口。在从下位类向上位类调用事件处理器的<br>过程中，下位类决定的“是否可以关闭窗口”会被传递。 |

**说明**

关闭窗口的确认

用于确认是否可以关闭窗口的事件。在无法关闭窗口的
情况下，请向上位类的同方法传入 false 作为参数。

---

### onPopupHide

事件

**说明**

关闭弹出窗口

在弹出窗口应当关闭时发生的事件。该事件在 [Window.stayOnTop](Window.md#stayontop) 属性为真、且 [Window.focusable](Window.md#focusable) 属性为假时，“其他窗口被点击”或者“其他应用程序变为活动状态”时发生。

通常请在这里进行关闭窗口或设为非显示的处理。

**相关:** [Window.focusable](Window.md#focusable) / [Window.stayOnTop](Window.md#stayontop)

---

### onActivate

事件

**说明**

窗口变为活动状态时

表示窗口变为活动状态时被调用的事件函数。

请注意该事件在窗口已经处于活动状态时也可能发生 ( 不保证完全按照 onActivate → onDeactivate → onActivate → …… 的顺序发生 )。

**相关:** [Window.onDeactivate](Window.md#ondeactivate) / [System.onActivate](System.md#onactivate) / [System.onDeactivate](System.md#ondeactivate)

---

### onDeactivate

事件

**说明**

窗口变为非活动状态时

表示窗口变为非活动状态时被调用的事件函数。

请注意该事件在窗口已经处于非活动状态时也可能发生 ( 不保证完全按照 onActivate → onDeactivate → onActivate → …… 的顺序发生 )。

**相关:** [Window.onActivate](Window.md#onactivate) / [System.onActivate](System.md#onactivate) / [System.onDeactivate](System.md#ondeactivate)

---

### onHintChanged

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 传递要显示在提示上的字符串。 |
| `x` | `&nbsp;` | 传递提示显示 X 轴坐标值。 |
| `y` | `&nbsp;` | 传递提示显示 Y 轴坐标值。 |
| `isshow` | `&nbsp;` | 传递使提示显示还是非显示。 |

**说明**

提示的状态变化时

表示提示的状态变化时被调用的事件函数。

按照显示/非显示进行提示的显示。

在图层上显示提示时，把该图层的 [Layer.hitThreshold](Layer.md#hitthreshold) 设置为 256，以忽略该图层的鼠标消息。

另外，[Layer.ignoreHintSensing](Layer.md#ignorehintsensing) 也指定 true。

**相关:** [Window.hintDelay](Window.md#hintdelay) / [Layer.ignoreHintSensing](Layer.md#ignorehintsensing) / [Layer.hitThreshold](Layer.md#hitthreshold)

---

### onDisplayRotate

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `orientation` | `&nbsp;` | 画面的方向 ( orientation )。<br>为以下某一个值。<br>oriUnknown ( 获取失败/不明 )、oriPortrait ( 纵向 )、oriLandscape ( 横向 ) |
| `angle` | `&nbsp;` | 角度。<br>角度 ( angle ) 为 0、90、180、270、-1 中的某一个，无法获取时为 -1。<br>角度是相对该设备默认方向的旋转角，因此在纵向设备中纵向为 0。<br>通常的设备大多为横向为 0。<br>纵向为 0 的是最近的 8 英寸平板等以纵向为标准方向的设备。 |
| `bpp` | `&nbsp;` | bits per pixel。 |
| `width` | `&nbsp;` | 画面的宽度。 |
| `height` | `&nbsp;` | 画面的高度。 |

**说明**

画面被旋转时 ( 1.1.0 起 )

表示画面被旋转时被调用的事件函数。

**相关:** [Window.displayOrientation](Window.md#displayorientation) / [Window.displayRotate](Window.md#displayrotate)

---

### onPointerDown

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 触摸或鼠标按钮的类型 |
| `x` | `&nbsp;` | X 位置 |
| `y` | `&nbsp;` | Y 位置 |
| `cx` | `&nbsp;` | 接触宽度 ( 像素数 )，鼠标时为 1 |
| `cy` | `&nbsp;` | 接触高度 ( 像素数 )，鼠标时为 1 |
| `shift` | `&nbsp;` | 修饰键状态，触摸时为 0 |
| `id` | `&nbsp;` | 触摸 ID，鼠标时始终为 0 |

**说明**

被某种指针设备按下

---

### onPointerMove

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 触摸或鼠标。不是鼠标按钮的种类，而是作为鼠标通知。 |
| `x` | `&nbsp;` | X 位置 |
| `y` | `&nbsp;` | Y 位置 |
| `cx` | `&nbsp;` | 接触宽度 ( 像素数 )，鼠标时为 1 |
| `cy` | `&nbsp;` | 接触高度 ( 像素数 )，鼠标时为 1 |
| `shift` | `&nbsp;` | 修饰键状态 ( 包含鼠标按下状态 )，触摸时为 0 |
| `id` | `&nbsp;` | 触摸 ID，鼠标时始终为 0 |

**说明**

被某种指针设备移动

---

### onPointerUp

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 触摸或鼠标按钮的类型 |
| `x` | `&nbsp;` | X 位置 |
| `y` | `&nbsp;` | Y 位置 |
| `cx` | `&nbsp;` | 接触宽度 ( 像素数 )，鼠标时为 1 |
| `cy` | `&nbsp;` | 接触高度 ( 像素数 )，鼠标时为 1 |
| `shift` | `&nbsp;` | 修饰键状态，触摸时为 0 |
| `id` | `&nbsp;` | 触摸 ID，鼠标时始终为 0 |

**说明**

被某种指针设备松开

---

### onMaximizeQuery

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `canmaximize` | `true` | 指定是否可以最大化。 |

**说明**

最大化的确认

在用户试图最大化窗口时发生
( [Window.registerExEvent](Window.md#registerexevent) 之后，仅 WINVER 构建 )。
想阻止最大化时，请向上位类的同方法传入 false。
如果不调用，则按默认进行最大化
( 与 [Window.onCloseQuery](Window.md#onclosequery) 相同的做法 )。
```tjs
function onMaximizeQuery() {
goPseudoFullScreen();           // 最大化のかわりに別の処理
super.onMaximizeQuery(false);   // 最大化そのものは止める
}
```
与 windowEx 插件的“处理器返回真则停止”方式不同。

---

### onMove

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 新位置的 X 坐标 |
| `y` | `&nbsp;` | 新位置的 Y 坐标 |

**说明**

移动了

在窗口移动时发生 ( 需要 [Window.registerExEvent](Window.md#registerexevent) )。

---

### onMoving

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | 移动目标的矩形 `%[ x, y, w, h ]` |

**说明**

移动中

在用户正在移动窗口期间发生
( 需要 [Window.registerExEvent](Window.md#registerexevent)，仅 WINVER 构建 )。
改写传递的矩形，可以约束移动目标。

---

### onResizing

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | 更改后的矩形 `%[ x, y, w, h ]` |
| `edge` | `&nbsp;` | 抓着的边 |

**说明**

大小更改中

在用户正在更改窗口大小期间发生
( 需要 [Window.registerExEvent](Window.md#registerexevent)，仅 WINVER 构建 )。
改写传递的矩形，可以约束大小。

---

### onMoveSizeBegin

事件

**说明**

边框的拖拽开始

( 需要 [Window.registerExEvent](Window.md#registerexevent)，仅 WINVER 构建 )

**相关:** [Window.onMoveSizeEnd](Window.md#onmovesizeend)

---

### onMoveSizeEnd

事件

**说明**

边框的拖拽结束

( 需要 [Window.registerExEvent](Window.md#registerexevent)，仅 WINVER 构建 )

**相关:** [Window.onMoveSizeBegin](Window.md#onmovesizebegin)

---

### onMinimize

事件

**说明**

最小化了

( 需要 [Window.registerExEvent](Window.md#registerexevent) )

**相关:** [Window.minimize](Window.md#minimize)

---

### onMaximize

事件

**说明**

最大化了

( 需要 [Window.registerExEvent](Window.md#registerexevent) )

**相关:** [Window.maximize](Window.md#maximize)

---

### onDPIChanged

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dpiX` | `&nbsp;` | 横向 DPI |
| `dpiY` | `&nbsp;` | 纵向 DPI |

**说明**

DPI 变化了

在窗口的 DPI 变化时发生
( 需要 [Window.registerExEvent](Window.md#registerexevent) )。
SDL3 系构建中把显示倍率换算为 `96 × 倍率` 后传递。

---

### onDisplayChanged

事件

**说明**

画面构成变化了

在画面的分辨率或显示器构成变化时发生
( 需要 [Window.registerExEvent](Window.md#registerexevent) )。

---

### onDeviceChanged

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `arrival` | `&nbsp;` | 连接时为真，卸下时为假 |

**说明**

输入设备被拔出 / 插入

( 需要 [Window.registerDeviceChange](Window.md#registerdevicechange) )

---

### onPaste

事件

**说明**

粘贴的指示

在从外部 ( 启动器等 ) 被指示粘贴时 ( `WM_PASTE` ) 发生。
仅 WINVER 构建。

---

## 插件扩展: layerExSave

基于伪代码的手册

窗口扩展

### 成员列表

#### 方法

- [startSaveLayerImage](#startsavelayerimage)
- [cancelSaveLayerImage](#cancelsavelayerimage)
- [stopSaveLayerImage](#stopsavelayerimage)
- [onSaveLayerImageProgress](#onsavelayerimageprogress)
- [onSaveLayerImageDone](#onsavelayerimagedone)

---

### startSaveLayerImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 保存对象的图层 |
| `filename` | `&nbsp;` | 文件名 ( 扩展名为 .png 时仅以 PNG 格式保存，其他情况为 TLG5 ) |
| `tags` | `&nbsp;` | 标签信息 |

**返回值**

处理器

**说明**

以 TLG5/PNG 格式开始保存图像

---

### cancelSaveLayerImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 处理器 |

**说明**

取消图像保存

---

### stopSaveLayerImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 处理器 |

**说明**

停止图像保存 ( 中止时不会收到结束事件 )

---

### onSaveLayerImageProgress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 处理器 |
| `progress` | `&nbsp;` | 进度 (% 表示) |
| `layer` | `&nbsp;` | 图层 |
| `filename` | `&nbsp;` | 文件名 |

**说明**

保存处理执行中事件

---

### onSaveLayerImageDone

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 处理器 |
| `canceled` | `&nbsp;` | 被取消时为 1 |
| `layer` | `&nbsp;` |  |
| `filename` | `&nbsp;` | 文件名 |

**说明**

保存处理执行完成事件

---

## 插件扩展: menu

### 成员列表

#### 属性

- [menu](#menu)

---

### menu

属性 \ 访问: `r`

**说明**

根菜单对象

表示根菜单对象 ( Menu 类的对象 )。
作为该根菜单对象的子项注册的菜单会排列到菜单栏上。

---

## 插件扩展: messenger

基于伪代码的手册

提供在同一台机器上启动的多个吉里吉里之间相互通信的功能，以及
从外部应用进行通信的功能。
交互的数据使用 WM_COPYDATA 转送。

### 成员列表

#### 属性

- [messageEnable](#messageenable)
- [storeHWND](#storehwnd)

#### 方法

- [registerUserMessageReceiver](#registerusermessagereceiver)
- [sendUserMessage](#sendusermessage)
- [sendUserMessageDirect](#sendusermessagedirect)
- [postUserMessage](#postusermessage)
- [postUserMessageDirect](#postusermessagedirect)
- [sendMessage](#sendmessage)
- [sendMessageDirect](#sendmessagedirect)
- [onMessageReceived](#onmessagereceived)

---

### messageEnable

属性 \ 访问: `r/w`

**说明**

指定消息接收功能是否有效。

设为 true 后开始接收消息。
消息接收有效时为 true
--------------------------------------------------- 窗口消息处理扩展 ---------------------------------------------------

---

### storeHWND

属性 \ 访问: `r/w`

**说明**

指定是否保存 HWND 信息。

指定它的值后，会创建名为 可执行文件名.键的值 的
文件，其中会输出当前的 HWND 信息。
外部应用程序想发送消息时，可以参照记录在该文件中的
HWND。
全屏等时，HWND 变化时内容会自动更新。
因此，外部应用程序每次发送时都需要重新参照 HWND 的值。

---

### registerUserMessageReceiver

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mode` | `&nbsp;` | wrmRegister=0:注册 wrmUnRegister=1:解除 |
| `msg` | `&nbsp;` | 数值:消息编号 字符串:进行 RegisterWindowMessage 并决定值 |
| `proc` | `&nbsp;` | 调用的函数 |
| `userdata` | `&nbsp;` | 用户数据参数 |

**返回值**

返回注册的消息编号

**说明**

注册用户定义的消息处理器。

※从 TJS2 注册函数时 ( typeof proc == Object 的情况 )
视为形式为 function receiver(userdata, wparam, lparam)
的函数。
此时，userdata 原样传递传入的值，
wparam、lparam 传递从原消息的数据强制转换为整数的值。

※从 TJS2 注册字符串时 ( typeof proc == String 的情况 )
以 function name(userdata, wparam, lparam)
的参数调用该对象的指定字符串的函数

※从插件侧注册函数时 ( typeof proc == Integer 的情况 )
视为 static bool __stdcall receiver(iTJSDispatch2 *winobj, void *userdata, tTVPWindowMessage *Message)
。设置时请强制转换为整数。
winobj 是相应窗口的对象
userdata 以强制转换为整数的值传递。
---------------------------------------------------

---

### sendUserMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | 消息编号 |
| `wparam` | `&nbsp;` | WPARAM ( 按整数处理 ) |
| `lparam` | `&nbsp;` | LPARAM ( 按整数处理 ) |

**说明**

执行低层级消息发送。

向所有吉里吉里发送指定的消息

---

### sendUserMessageDirect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND 数值 |
| `msg` | `&nbsp;` | 消息编号 |
| `wparam` | `&nbsp;` | WPARAM ( 按整数处理 ) |
| `lparam` | `&nbsp;` | LPARAM ( 按整数处理 ) |

**说明**

指定 HWND 执行低层级消息发送。

向特定的窗口发送指定的消息

---

### postUserMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | 消息编号 |
| `wparam` | `&nbsp;` | WPARAM ( 按整数处理 ) |
| `lparam` | `&nbsp;` | LPARAM ( 按整数处理 ) |

**说明**

投递低层级消息。

向所有吉里吉里投递指定的消息

---

### postUserMessageDirect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND 数值 |
| `msg` | `&nbsp;` | 消息编号 |
| `wparam` | `&nbsp;` | WPARAM ( 按整数处理 ) |
| `lparam` | `&nbsp;` | LPARAM ( 按整数处理 ) |

**说明**

指定 HWND 投递低层级消息。

向特定的窗口投递指定的消息

---

### sendMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 识别键 ( 字符串:最多 256 个字符，请注意 ) |
| `message` | `&nbsp;` | 消息 ( 字符串 ) |

**说明**

进行消息的发送。

向所有已启动的吉里吉里发送 WM_COPYDATA 消息。
识别键与消息的含义请在各应用程序中自行适当定义。
---------------------------------------------------

---

### sendMessageDirect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | HWND 数值 |
| `key` | `&nbsp;` | 识别键 ( 字符串:最多 256 个字符，请注意 ) |
| `message` | `&nbsp;` | 消息 ( 字符串 ) |

**说明**

指定 HWND 进行消息的发送。

向指定的窗口发送 WM_COPYDATA 消息。
接收侧与 sendMessage 是共同的处理，因此请务必指定识别键

---

### onMessageReceived

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 识别键 ( 字符串:最多 256 个字符，请注意 ) |
| `message` | `&nbsp;` | 消息 ( 字符串 ) |

**说明**

事件：消息接收。

在从其他吉里吉里或外部应用收到 WM_COPYDATA 消息时被调用
调用方会一直被锁定到该调用结束为止，因此
请尽快结束处理。

---

## 插件扩展: shellExecute

基于伪代码的手册

提供启动外部应用并等待其结束的机制。
作为窗口消息利用了 WM_APP + 1

### 成员列表

#### 方法

- [shellExecute](#shellexecute)
- [terminateProcess](#terminateprocess)
- [onShellExecuted](#onshellexecuted)
- [commandExecute](#commandexecute)
- [commandSendSignal](#commandsendsignal)
- [onCommandLineOutput](#oncommandlineoutput)

---

### shellExecute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 程序 |
| `param` | `&nbsp;` | 参数 |

**返回值**

进程句柄 ( 失败时为 -1 )。可以传给 terminateProcess。

**说明**

在后台执行外部程序

处理结束后会发生 onShellExecuted 事件。

---

### terminateProcess

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `process` | `&nbsp;` | 进程句柄 |
| `endCode` | `&nbsp;` | 退出代码 |

**说明**

强制结束正在运行的外部程序

---

### onShellExecuted

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `process` | `&nbsp;` | 进程句柄 |
| `endCode` | `&nbsp;` | 退出代码 |

**说明**

事件:shell 执行结束

---

### commandExecute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 程序 |
| `param` | `&nbsp;` | 参数 |

**返回值**

进程句柄 ( 失败时为 -1 )。可以传给 terminateProcess。

**说明**

执行带控制台输出获取的命令行程序

控制台按行输出时会发生 onCommandLineOutput 事件。
处理结束后会发生 onShellExecuted 事件。

---

### commandSendSignal

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `process` | `&nbsp;` | 进程句柄 ( 仅限 commandExecute 过的进程 ) |
| `isBreak` | `&nbsp;` | 发送 Ctrl+Break 而不是 Ctrl+C |

**返回值**

成功时为 true

**说明**

发送 Ctrl+C 事件 ( experimental:并不保证在所有环境中都能工作 )

---

### onCommandLineOutput

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `process` | `&nbsp;` | 进程句柄 |
| `text` | `&nbsp;` | 输出文本 ( 以 1 行为单位 ) |

**说明**

事件:控制台输出

---

## 插件扩展: sigcheck

基于伪代码的手册

在后台进行签名检查。
作为窗口消息利用了 WM_APP + 2 和 WM_APP + 3

### 成员列表

#### 方法

- [checkSignature](#checksignature)
- [cancelCheckSignature](#cancelchecksignature)
- [stopCheckSignature](#stopchecksignature)
- [onCheckSignatureProgress](#onchecksignatureprogress)
- [onCheckSignatureDone](#onchecksignaturedone)

---

### checkSignature

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 确认对象文件 |
| `publickey` | `&nbsp;` | 公钥 |
| `info` | `&nbsp;` | 用户信息 |

**返回值**

handler 识别处理器

**说明**

签名检查的开始

处理中会发生 onCheckSignatureProgress，
结束时会发生 onCheckSignatureDone 事件。
exe 或 dll 的情况下签名内置于文件中。xp3 等情况下，
把原文件加上 .sig 的外部文件作为签名处理。

---

### cancelCheckSignature

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 识别处理器 |

**说明**

取消签名检查

使正在执行的签名检查迅速停止。将以取消结束。

---

### stopCheckSignature

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 识别处理器 |

**说明**

中止签名检查

使正在执行的签名检查迅速停止。不会收到结束事件。

---

### onCheckSignatureProgress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 识别处理器 |
| `info` | `&nbsp;` | 用户信息 |
| `percent` | `&nbsp;` | 进度 0~100% |

**说明**

事件:签名检查进度

---

### onCheckSignatureDone

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 识别处理器 |
| `info` | `&nbsp;` | 用户信息 |
| `result` | `&nbsp;` | 结果 -2:错误 -1:取消 0:检查失败 1:检查成功 |
| `errormsg` | `&nbsp;` | 结果为错误时的错误消息 |

**说明**

事件:签名检查结束

---

## 插件扩展: windowEx

基于伪代码的手册

Window 扩展

※引擎本体的 Window 中也加入了 最大化 / 最小化 / 复归 (maximize / minimize / showRestore /
maximized / minimized)、矩形 (getWindowRect / getClientRect / setClientRect /
getNormalRect)、disableResize / disableMove、registerExEvent / registerDeviceChange
与扩展事件 ( SDL3 系构建中也可用 )。
加载本插件后，这些会被插件版覆盖。
新编写的脚本请以本体版为前提。

### 成员列表

#### 属性

- [maximized](#maximized)
- [minimized](#minimized)
- [disableResize](#disableresize)
- [exSystemMenu](#exsystemmenu)
- [enableNCMouseEvent](#enablencmouseevent)

#### 方法

- [maximize](#maximize)
- [minimize](#minimize)
- [showRestore](#showrestore)
- [resetWindowIcon](#resetwindowicon)
- [setWindowIcon](#setwindowicon)
- [setWindowCornerPreference](#setwindowcornerpreference)
- [getClientRect](#getclientrect)
- [getWindowRect](#getwindowrect)
- [getNormalRect](#getnormalrect)
- [setClientRect](#setclientrect)
- [bringTo](#bringto)
- [sendToBack](#sendtoback)
- [acquireImeControl](#acquireimecontrol)
- [resetImeContext](#resetimecontext)
- [registerExEvent](#registerexevent)
- [onMaximizeQuery](#onmaximizequery)
- [onMaximize](#onmaximize)
- [onMinimize](#onminimize)
- [onShow](#onshow)
- [onHide](#onhide)
- [onMoveSizeBegin](#onmovesizebegin)
- [onMoveSizeEnd](#onmovesizeend)
- [onMoving](#onmoving)
- [onMove](#onmove)
- [onResizing](#onresizing)
- [forceResizeRect](#forceresizerect)
- [onDisplayChanged](#ondisplaychanged)
- [onDPIChanged](#ondpichanged)
- [onEnterMenuLoop](#onentermenuloop)
- [onExitMenuLoop](#onexitmenuloop)
- [onScreenSave](#onscreensave)
- [onMonitorPower](#onmonitorpower)
- [onDeviceChanged](#ondevicechanged)
- [registerDeviceChange](#registerdevicechange)
- [onHotKeyPressed](#onhotkeypressed)
- [registerHotKey](#registerhotkey)
- [onActivateChanged](#onactivatechanged)
- [setOverlayBitmap](#setoverlaybitmap)
- [onNcMouseMove](#onncmousemove)
- [onNcMouseUp](#onncmouseup)
- [onNcMouseDown](#onncmousedown)
- [onNcMouseLeave](#onncmouseleave)
- [ncHitTest](#nchittest)
- [onNonCapMouseEvent](#onnoncapmouseevent)
- [focusMenuByKey](#focusmenubykey)
- [onStartKeyMenu](#onstartkeymenu)
- [onAccelKeyMenu](#onaccelkeymenu)
- [setMessageHook](#setmessagehook)
- [onWindowsMessageHook](#onwindowsmessagehook)
- [getNotificationNum](#getnotificationnum)
- [getNotificationName](#getnotificationname)

#### 常量

- [nchtError](#nchterror)
- [nchtTransparent](#nchttransparent)
- [nchtNoWhere](#nchtnowhere)
- [nchtClient](#nchtclient)
- [nchtCaption](#nchtcaption)
- [nchtSysMenu](#nchtsysmenu)
- [nchtSize](#nchtsize)
- [nchtGrowBox](#nchtgrowbox)
- [nchtMenu](#nchtmenu)
- [nchtHScroll](#nchthscroll)
- [nchtVScroll](#nchtvscroll)
- [nchtMinButton](#nchtminbutton)
- [nchtReduce](#nchtreduce)
- [nchtMaxButton](#nchtmaxbutton)
- [nchtZoom](#nchtzoom)
- [nchtLeft](#nchtleft)
- [nchtRight](#nchtright)
- [nchtTop](#nchttop)
- [nchtTopLeft](#nchttopleft)
- [nchtTopRight](#nchttopright)
- [nchtBottom](#nchtbottom)
- [nchtBottomLeft](#nchtbottomleft)
- [nchtBottomRight](#nchtbottomright)
- [nchtBorder](#nchtborder)

---

### maximized

属性 \ 访问: `r/w`

**说明**

获取窗口是否最大化

虽然也有 setter，但不推荐使用

---

### minimized

属性 \ 访问: `r/w`

**说明**

获取窗口是否最小化

---

### disableResize

属性 \ 访问: `r/w`

**说明**

抑制调整大小

setter 在没有用 registerExEvent() 注册扩展事件时会发生异常
设为 true 后，即使 borderStyle == bsSizeable 也会
・窗口边缘不再出现调整大小光标，无法更改大小
・系统菜单 (Alt+Space) 的调整大小变灰，无法选择
通过最大化等其他方式调整大小仍然有效 ( onResize 也会触发 )

---

### exSystemMenu

属性 \ 访问: `r/w`

**说明**

添加到系统菜单

setter 在没有用 registerExEvent() 注册扩展事件时会发生异常
指定 MenuItem 或字典的数组
选中该菜单时会发生 onExSystemMenuSelected(被选中的对象) 回调

---

### enableNCMouseEvent

属性 \ 访问: `r/w`

**说明**

以下特殊用途 启用 WM_SETCURSOR 的回调 onNonCapMouseEvent ( 默认：false )

---

### maximize

方法

**说明**

窗口的最大化

与按下最大化按钮的动作同等
在固定大小的窗口中不起作用

---

### minimize

方法

**说明**

窗口的最小化（mainWindow 时收纳到任务栏，其他则最小化到画面左下）

与按下最小化按钮的动作同等

---

### showRestore

方法

**说明**

窗口最大化、最小化的恢复

---

### resetWindowIcon

方法

**说明**

重新设置窗口的标题栏图标

※ 对 Vista 中从全屏恢复时图标消失的问题（在吉里吉里 v2.30 中确认）的消极应对方法

---

### setWindowIcon

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` | 图标文件或 void ( void 或 "" 时重置为初始状态 ) |
| `withapp` | `&nbsp;` | 是否也一起更改应用程序窗口的图标 |

**说明**

更改窗口的标题栏图标

※ 不能指定归档内的文件，指定 exe 或 DLL 时会设置最开始的图标

---

### setWindowCornerPreference

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `0` | DWMWCP_* 的值 (0=DEFAULT, 1=DONOTROUND, 2=ROUND, 3=ROUNDSMALL) |

**返回值**

成功时为 true

**说明**

更改窗口的角的形状

※ 可在 Windows 11 Build 22000 以后使用

---

### getClientRect

方法

**返回值**

%[ x, y, w, h ] 或 void ( 获取失败时 )

**说明**

客户区、窗口区域、非最大化通常显示区域的获取

※ 注意 innerSunken 边框部分包含在客户区中
客户区

---

### getWindowRect

方法

**说明**

窗口区域

---

### getNormalRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nofix` | `false` |  |

**说明**

非最大化通常显示区域 (@param nofix true:不进行工作区校正)

---

### setClientRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x,y,w,h ] |

**说明**

客户区的设置

---

### bringTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `win` | `"top"` | Window 对象或规定字符串或数值<br>如果是 Window 对象，则被放置在该窗口的后面<br>字符串的情况下，为 "bottom" "notopmost" "top" "topmost" 之一（相当于 HWND_*）cf. SetWindowPos API<br>数值的情况下，视为窗口句柄，或者直接指定 HWND_* 宏的值<br>#define HWND_TOP        ((HWND)0)<br>#define HWND_BOTTOM     ((HWND)1)<br>#define HWND_TOPMOST    ((HWND)-1)<br>#define HWND_NOTOPMOST  ((HWND)-2) |
| `activate` | `false` | 是否设为活动状态的标志<br>即使设为 true，应用程序自身也不会变为活动状态（不会发生任务栏闪烁等） |

**说明**

更改窗口的 Z 顺序

---

### sendToBack

方法

**说明**

/ alias method

---

### acquireImeControl

方法

**返回值**

成功时为 true

**说明**

重新设置 IME ( 吉里吉里Z 专用 )

执行环境为 吉里吉里Z 时投递 TVP_WM_ACQUIREIMECONTROL

---

### resetImeContext

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `defval` | `true` | true:IACE_DEFAULT, false:NULL |

**返回值**

成功时为 true

**说明**

重新设置 IME 上下文

在 imDisable 被重新实现时或使用多个窗口进行文本输入时，可能与吉里吉里Z 本体侧 (ImeControl.h) 的设置冲突

---

### registerExEvent

方法

**说明**

启用扩展事件

针对该窗口的实例，
说明中写有“■扩展事件：”的回调将变为有效

不过，对于下述回调，
在执行该函数时点上实例中不存在的话就不会发生，请注意
（不存在时，之后即使向实例添加函数也不会被调用）
onMoving      移动中
onMove        移动
onResizing    调整大小中
onNcMouseMove NonClient 区域中的鼠标移动

---

### onMaximizeQuery

方法

**返回值**

返回 true 则不允许最大化

**说明**

■扩展事件：确认是否允许最大化

※本体版的阻止方式不同。本体版调用 super.onMaximizeQuery(false) 就会阻止，
不看返回值 ( 请参阅 [Window.onMaximizeQuery](Window.md#onmaximizequery) )。

---

### onMaximize

方法

**说明**

■扩展事件：窗口最大化

被调用时窗口大小已经最大化

---

### onMinimize

方法

**说明**

■扩展事件：窗口最小化

全屏中用 Alt+Tab 等选择了其他应用时，或 mainWindow 以外被最小化时被调用
收纳到任务栏时会调用 onHide 事件，请注意

---

### onShow

方法

**说明**

■扩展事件：窗口显示

从任务栏恢复时等被调用

---

### onHide

方法

**说明**

■扩展事件：窗口非显示

被收纳到任务栏时等被调用

---

### onMoveSizeBegin

方法

**说明**

■扩展事件：调整大小、移动开始通知/结束

开始拖拽边框或标题栏时，或通过 Alt+Space 选择 S 或 M 时（开始通知），
以及移动或调整大小结束时（结束通知）分别被调用
在 onMoving 或 onResizing 中想参照原来的窗口位置或大小时，在这里保存比较好
是调整大小还是移动，由于 WM_ENTERSIZEMOVE/WM_EXITSIZEMOVE 的关系无法判定

---

### onMoveSizeEnd

方法

**说明**

结束通知

---

### onMoving

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x, y, w, h ] 窗口坐标 |

**说明**

■扩展事件：窗口移动中

※在 Windows 中以显示窗口内容的状态移动的设置（不显示移动框）下，会立即调用 onMove

---

### onMove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

■扩展事件：窗口移动（完成）

---

### onResizing

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | %[ x, y, w, h, type ] 更改中的大小（窗口坐标） |

**返回值**

返回 true 则反映 rect 的更改（强制指定位置、大小）
这种情况下，如果不根据抓住的位置 (rect.type) 妥善调整改写内容，
调整大小中窗口可能会移动，请注意（⇒请参照 forceResizeRect()）

**说明**

■扩展事件：大小更改中

※在 Windows 中以显示窗口内容的状态调整大小的设置（不显示大小框）下，会立即调用 onResize

---

### forceResizeRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

---

### onDisplayChanged

方法

**说明**

■扩展事件：显示器构成更改通知

在分辨率、颜色数、多显示器构成（包括位置更改）更改时被调用

---

### onDPIChanged

方法

**说明**

■扩展事件：窗口的 DPI 更改通知

更改 DPI 设置，或在 DPI 值不同的显示器之间移动时通知

---

### onEnterMenuLoop

方法

**说明**

■扩展事件：菜单处理的开始、结束通知

窗口的菜单处理（点击或按下 F10 等时）的开始和结束的通知事件
WM_ENTERMENULOOP / WM_EXITMENULOOP 通知的回调

※ 全屏时的菜单中不会发生该事件，请注意！

---

### onExitMenuLoop

方法

**说明**

菜单处理结束

---

### onScreenSave

方法

**返回值**

返回 true 则抑制控制

**说明**

■扩展事件：屏幕保护程序开始通知，显示器电源更改通知

---

### onMonitorPower

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### onDeviceChanged

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `arrival` | `&nbsp;` | 为 true 则设备被添加，为 false 则被卸下<br>※ 请注意需要正在用 registerExEvent() 且调用 registerDeviceChange() |

**说明**

■扩展事件：设备添加、移除通知

---

### registerDeviceChange

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `guid` | `GUID_DEVINTERFACE_HID` | 表示 GUID 的 octet 值 ( 省略时为 HID 设备类 )<br>※ 请注意能注册的 GUID 每个窗口最多 1 个 |

**说明**

启用 onDeviceChanged 扩展事件

---

### onHotKeyPressed

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 用 registerHotKey 注册的 ID |
| `mod` | `&nbsp;` | 修饰键 ( ssShift, ssAlt, ssCtrl 等的组合 ) |

**说明**

■扩展事件：热键的输入

---

### registerHotKey

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 要注册的 ID (※0x0000~0xBFFF 为止) |
| `key` | `&nbsp;` |  |
| `mod` | `&nbsp;` | 修饰键 ( ssShift, ssAlt, ssCtrl 等的组合 ) |

**返回值**

注册成功时为 true

**说明**

注册热键

---

### onActivateChanged

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `active` | `&nbsp;` | 0:非活动化 1:通过鼠标点击以外的方式活动化 2:通过鼠标点击活动化 |
| `minimize` | `&nbsp;` | 0:窗口未被最小化 其他:已被最小化 |

**说明**

■扩展事件：活动状态更改通知

※与 Window.onActivate 或 Window.onDeactivate 不同之处在于，（这一点对扩展事件整体都适用）
即使 System.eventDisabled == true 事件回调也会被送来

例如在 System.onDeactivate 时把 System.eventDisabled=true（这样一来 System.onActivate 就
不会被送来），并通过该事件通知使其复归，也许就能添加“非活动时停止工作”这样的功能
（不过这仅仅是停止事件的配送，对于通过时间差进行计时的定时器应用来说没什么意义）
另外，System.eventDisabled=true 时连画面更新都不会运行，因此把其他窗口置前等使
WM_PAINT 发生时会出现画面损坏的问题（可采取使用后述的 OverlayBitmap 等方法）

---

### setOverlayBitmap

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 复制到 bitmap 图像的图层 ( void 或省略时清除覆盖层 ) |

**说明**

显示、清除覆盖层 bitmap

用指定的图像在客户区盖上子窗口（不是吉里吉里的而是 Windows 的）
・扩展事件未有效时会发生异常
・覆盖层显示中，鼠标类消息完全不会到达吉里吉里的图层侧
・实质上是 System.eventDisabled=true 时专用
・会因 TVP_WM_DETACH 被自动清除

---

### onNcMouseMove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `ht` | `&nbsp;` | 区域的种类（NCHITTEST 常量） |

**说明**

■扩展事件：非客户区鼠标事件

---

### onNcMouseUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `btn` | `&nbsp;` |  |
| `ht` | `&nbsp;` |  |

---

### onNcMouseDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `btn` | `&nbsp;` |  |
| `ht` | `&nbsp;` |  |

---

### onNcMouseLeave

方法

---

### ncHitTest

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

非客户区调查

---

### onNonCapMouseEvent

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ht` | `&nbsp;` |  |
| `ev` | `&nbsp;` |  |

**说明**

WM_SETCURSOR 回调：ht=LOWORD(LParam), ev=HIWORD(LParam)

---

### focusMenuByKey

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` |  |

**说明**

发送 SC_KEYMENU

---

### onStartKeyMenu

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` |  |

**说明**

SC_KEYMENU 通知回调

---

### onAccelKeyMenu

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` |  |
| `st` | `&nbsp;` |  |

**说明**

WM_MENUCHAR 通知回调

---

### setMessageHook

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `on` | `&nbsp;` |  |
| `ev` | `&nbsp;` |  |

**说明**

设置消息钩子 ( on:有效, ev:事件编号或事件名字符：省略时为全部 )

---

### onWindowsMessageHook

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wp` | `&nbsp;` |  |
| `lp` | `&nbsp;` |  |

**说明**

用 setMessageHook 指定的事件发生时的回调

---

### getNotificationNum

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**说明**

获取 WM_XXX 事件编号（传入时去掉 WM_）

---

### getNotificationName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `num` | `&nbsp;` |  |

**说明**

从事件编号获取 WM_XXX（返回时去掉 WM_）

---

### nchtError

常量

**说明**

HTERROR

---

### nchtTransparent

常量

**说明**

HTTRANSPARENT

---

### nchtNoWhere

常量

**说明**

HTNOWHERE

---

### nchtClient

常量

**说明**

HTCLIENT

---

### nchtCaption

常量

**说明**

HTCAPTION

---

### nchtSysMenu

常量

**说明**

HTSYSMENU

---

### nchtSize

常量

**说明**

HTSIZE

---

### nchtGrowBox

常量

**说明**

HTGROWBOX

---

### nchtMenu

常量

**说明**

HTMENU

---

### nchtHScroll

常量

**说明**

HTHSCROLL

---

### nchtVScroll

常量

**说明**

HTVSCROLL

---

### nchtMinButton

常量

**说明**

HTMINBUTTON

---

### nchtReduce

常量

**说明**

HTREDUCE

---

### nchtMaxButton

常量

**说明**

HTMAXBUTTON

---

### nchtZoom

常量

**说明**

HTZOOM

---

### nchtLeft

常量

**说明**

HTLEFT

---

### nchtRight

常量

**说明**

HTRIGHT

---

### nchtTop

常量

**说明**

HTTOP

---

### nchtTopLeft

常量

**说明**

HTTOPLEFT

---

### nchtTopRight

常量

**说明**

HTTOPRIGHT

---

### nchtBottom

常量

**说明**

HTBOTTOM

---

### nchtBottomLeft

常量

**说明**

HTBOTTOMLEFT

---

### nchtBottomRight

常量

**说明**

HTBOTTOMRIGHT

---

### nchtBorder

常量

**说明**

HTBORDER

---

## 插件扩展: windowExProgress

基于伪代码的手册

窗口扩展

### 成员列表

#### 方法

- [startProgress](#startprogress)
- [doProgress](#doprogress)
- [setProgressMessage](#setprogressmessage)
- [endProgress](#endprogress)

#### 常量

- [PBS_SMOOTH](#pbs_smooth)
- [PBS_VERTICAL](#pbs_vertical)

---

### startProgress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `init` | `&nbsp;` | 初始化数据 ( 字典 ) |

**说明**

开始进度处理。

即使吉里吉里处于执行阻塞中也会正常持续显示。
进度条初始化参数
progressBarEnable: 是否显示进度条 ( 默认:true )
progressBarStyle: 进度条的样式 ( 默认:无 )
progressBarLeft: 进度条显示位置 X ( 默认:自动居中 )
progressBarTop: 进度条显示位置 Y ( 默认:自动居中 )
progressBarWidth: 进度条宽度 ( 默认:窗口宽度的 1/3 )
progressBarHeight: 进度条高度 ( 默认:窗口高度的 1/10 )
progressBarColor: 进度条颜色 0xRRGGBB ( 默认:默认色 )
progressBarBackColor: 进度条背景色 0xRRGGBB ( 默认:默认色 )

取消按钮初始化参数
cancelButtonEnable: 是否显示取消按钮 ( 默认:true )
cancelButtonCaption: 显示在取消按钮上的文本 ( 默认:Cancel )
cancelButtonLeft: 取消按钮显示位置 X ( 默认:自动居中 )
cancelButtonTop: 取消按钮显示位置 Y ( 默认:从下往上高度 3 倍的位置 )
cancelButtonWidth: 取消按钮宽度 ( 默认:文本字符数*12+8 )
cancelButtonHeight: 取消按钮高度 ( 默认:20 )

背景图像初始化参数 ( 未实现 )
backGround: 背景指定 图层：直接参照图层的图像 数值:用相应颜色填充 默认:无

消息初始化参数 ( 未实现 )
messages: 消息信息或其数组
left: 显示坐标 X
top: 显示坐标 Y
text: 初始显示文本
size: 显示大小
color: 显示颜色
shadowColor: 阴影色
shadowDistanceX: 阴影偏移指定
shadowDistanceY: 阴影偏移指定
font: 字体指定
fontStyle: 字体样式

---

### doProgress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `percent` | `&nbsp;` | 以百分比指定进度状态 |

**返回值**

有取消请求时为 true

**说明**

通知进度处理的进度状态。

---

### setProgressMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 文本 ID ( 注册顺序 ) |
| `text` | `&nbsp;` | 显示文本 |

**说明**

替换进度处理的文本

---

### endProgress

方法

**说明**

结束进度处理。

---

### PBS_SMOOTH

常量

值: `1`

**说明**

进度条样式指定 进度条平滑指定

---

### PBS_VERTICAL

常量

值: `4`

**说明**

进度条垂直配置指定

---
