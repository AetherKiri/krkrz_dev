# OGLDrawDevice

OGLDrawDevice 类是用于将该实例注册到 [Window.drawDevice](Window.md#drawdevice) 后使用的 DrawDevice，提供使用 OpenGL ES (glad / ANGLE / EGL) 的绘制功能。

它不是启动时的默认 DrawDevice，而是在 TJS 脚本中显式设置到 Window.drawDevice 的时机，内部的 OpenGL 上下文会被生成，之后的所有绘制都会经过 GL 路径。也可以通过启动选项 `-drawdevice=ogl` 从启动时就选择该设备 ( [命令行选项](../guide/CommandLine.md) )。

使用它需要能够使用 OpenGL ES 的环境。WINVER 构建始终经由 EGL ( ANGLE 的 `libEGL.dll` / `libGLESv2.dll` )，因此必须随附 DLL。SDL3 构建优先使用 OS 的 OpenGL 驱动的 ES profile，无法使用时回退到相同的 ANGLE DLL ( 也可以用 `-forceegl` 强制使用 EGL )。另外，以 `-drawdevice=sdl` 启动 SDL3 构建时，无法在运行中切换到该设备。

仅在该设备处于活动状态期间，TJS 公开类 [Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md) / [Offscreen](Offscreen.md) / [Matrix32](Matrix32.md) / [VertexBuffer](VertexBuffer.md) / [VertexBinder](VertexBinder.md) 才会工作。

## 成员列表

### 构造函数

- [OGLDrawDevice](#ogldrawdevice)

### 属性

- [interface](#interface)
- [window](#window)
- [canvas](#canvas)
- [texture](#texture)
- [matrix](#matrix)
- [glVideoPresenterHost](#glvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

### 方法

- [recreate](#recreate)
- [createCanvas](#createcanvas)
- [resumeOnDraw](#resumeondraw)

### 事件

- [onInit](#oninit)
- [onDone](#ondone)
- [onDraw](#ondraw)

---

### OGLDrawDevice

构造函数

**说明**

构建 OGLDrawDevice 对象

构建 OGLDrawDevice 类的对象。

刚构建后还不会生成 OpenGL 上下文。设置到 Window.drawDevice 时会被初始化。

---

### interface

属性 \ 访问: `r`

**说明**

获取接口对象

用于让插件等使用 DrawDevice 对象。

---

### window

属性 \ 访问: `r`

**说明**

获取关联的 Window 对象

返回设置了该 DrawDevice 的 Window 对象。

---

### canvas

属性 \ 访问: `r`

**说明**

获取用于绘制的 Canvas 对象

返回该设备管理的 [Canvas](Canvas.md) 对象。
可以从 onDraw 等之中访问并发出绘制命令。

---

### texture

属性 \ 访问: `r`

**说明**

获取纹理管理对象

返回该设备管理的 [Texture](Texture.md) 对象。

---

### matrix

属性 \ 访问: `r`

**说明**

获取矩阵对象

返回该设备管理的 [Matrix32](Matrix32.md) 对象。
用于绘制时的坐标变换。

---

### glVideoPresenterHost

属性 \ 访问: `r`

**说明**

叠加视频 presenter 注册入口 (指针值)

这是叠加视频侧为了以 pull 型合成到该 GL 设备而读取的、指向 presenter host
的指针值 ( 与 WINVER 的 [videoPresenterHost](Window.BasicDrawDevice.md#videopresenterhost) /
SDL 的 [sdlVideoPresenterHost](SDLDrawDevice.md#sdlvideopresenterhost) 相同规约 )。
通常由引擎内部/插件使用。

---

### dialogRendererHost

属性 \ 访问: `r`

**说明**

Elements 对话框 renderer host (指针值)

这是用于获取 Elements 覆盖层绘制适配器的、指向 host 的指针值。
通常由引擎内部/插件使用。

---

### viewportBackgroundHost

属性 \ 访问: `r`

**说明**

视口余白涂色填充注册入口 (指针值)

这是用于接收游戏画面未覆盖整个绘制区域时的余白 ( [Window.viewportBgColor](Window.md#viewportbgcolor) /
[Window.setViewportWallpaper](Window.md#setviewportwallpaper) ) 的、指向
`iTVPViewportBackgroundHost` 的指针值。Window 仅在该属性为非 0
时才反映余白设置 ( 在不具有该属性的绘制设备上，余白的涂色填充不会
生效，仍保持该设备默认的填充 )。通常由引擎内部/插件
使用。

---

### recreate

方法

**说明**

内部设备重新生成

重新生成内部设备。

通常不会用到。

---

### createCanvas

方法

**说明**

生成 Canvas 对象

请求生成与该设备关联的 [Canvas](Canvas.md) 对象。
生成的 Canvas 可以通过 [canvas](#canvas) 属性获取。

---

### resumeOnDraw

方法

**说明**

重新开始已自动停止的 onDraw 触发

当 onDraw 处理器每帧持续抛出异常，达到连续异常上限
( 命令行选项 `-eventexceptionlimit`，默认 10 ) 时，
onDraw 的触发会自动停止 ( 画面清除等绘制周期本身仍会继续 )。
调用本方法即可重新开始触发。

---

### onInit

事件

**说明**

GL 上下文初始化时被调用的事件

在该设备被设置到 Window.drawDevice、内部 OpenGL ES 上下文的生成与初始化完成后立即触发。

着色器、纹理等初始资源的分配在这里进行。

**相关:** [OGLDrawDevice.onDone](OGLDrawDevice.md#ondone)

---

### onDone

事件

**说明**

GL 上下文销毁前被调用的事件

在该设备被分离、或上下文被销毁之前立即触发。

onInit 中分配的资源释放在这里进行。

**相关:** [OGLDrawDevice.onInit](OGLDrawDevice.md#oninit)

---

### onDraw

事件

**说明**

画面绘制时被调用的事件

每个绘制周期触发。分配了 Canvas 时，由于会在内部被 BeginDrawing ~ EndDrawing 夹着的状态下调用，因此可以在处理器内经由 [canvas](#canvas) 属性发出绘制命令。

---
