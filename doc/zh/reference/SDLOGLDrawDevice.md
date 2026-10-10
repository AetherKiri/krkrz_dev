# SDLOGLDrawDevice

SDLOGLDrawDevice 类是用于将该实例注册到 [Window.drawDevice](Window.md#drawdevice) 中使用的 DrawDevice，在 SDL3 构建中直接使用 OpenGL ES 将图层合成结果绘制到画面。它专用于 SDL3 构建 (KRKRZ_VARIANT=SDL)，不包含在 WINVER 构建中。

在启用 OpenGL 的构建 ( 默认配置 ) 的 SDL3 中，它作为**启动时的默认 DrawDevice** 从一开始就被注册，因此通常无需特意关注。也可以通过启动选项 `-drawdevice=sdlogl` 显式指定 ( [命令行选项](../guide/CommandLine.md) )。

与 [SDLDrawDevice](SDLDrawDevice.md) ( 经由 `SDL_Renderer` ) 的区别在于，它不经过 SDL 的渲染器抽象，而是直接向 OpenGL ES 进行纹理更新、绘制。它相当于从 [OGLDrawDevice](OGLDrawDevice.md) ( 拥有 [Canvas](Canvas.md) / [Texture](Texture.md) / [ShaderProgram](ShaderProgram.md) 等 TJS 公开 GL 类群的全功能版 ) 中去掉这些 TJS 公开逻辑后的“图层绘制 + 视频播放”简化版。GL 上下文可以与 OGLDrawDevice 共享，想使用 Canvas 等时，可以在 Window.drawDevice 中设置 [OGLDrawDevice](OGLDrawDevice.md) 进行切换。

使用它需要能够使用 OpenGL ES 的环境 ( OS 的 OpenGL 驱动的 ES profile，或 ANGLE 的 `libEGL.dll` / `libGLESv2.dll`。也可以用 `-forceegl` 强制使用 EGL )。

## 成员列表

### 构造函数

- [SDLOGLDrawDevice](#sdlogldrawdevice)

### 属性

- [interface](#interface)
- [window](#window)
- [glVideoPresenterHost](#glvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

---

### SDLOGLDrawDevice

构造函数

**说明**

构建 SDLOGLDrawDevice 对象

构建 SDLOGLDrawDevice 类的对象。

在启用 OpenGL 的构建的 SDL3 中，它从一开始就作为启动时的默认 DrawDevice 注册在 Window.drawDevice 中，因此无需重新注册。

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

获取相关联的 Window 对象

返回设置了该 DrawDevice 的 Window 对象。

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
