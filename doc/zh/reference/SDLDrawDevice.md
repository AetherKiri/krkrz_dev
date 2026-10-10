# SDLDrawDevice

SDLDrawDevice 类是用于将该实例注册到 [Window.drawDevice](Window.md#drawdevice) 后使用的 DrawDevice，提供使用 SDL3 (`SDL_Renderer` + `SDL_Texture`) 的标准绘制功能。专用于 SDL3 构建 (KRKRZ_VARIANT=SDL)，不包含在 WINVER 构建中。

SDL3 构建启动时的默认 DrawDevice，在 OpenGL 启用构建中是基于 OpenGL ES 的 [SDLOGLDrawDevice](SDLOGLDrawDevice.md)，在 OpenGL 禁用构建中是本类。指定启动选项 `-drawdevice=sdl` 后，OpenGL 启用构建也可以用本类启动 ( [命令行选项](../guide/CommandLine.md) )。`SDL_Renderer` 的后端为自动选择，可以通过 `-renderer` 选项显式指定。

另外，使用本类启动时，无法在运行中切换到 OpenGL 系 ( [SDLOGLDrawDevice](SDLOGLDrawDevice.md) / [OGLDrawDevice](OGLDrawDevice.md) ) ( OpenGL 的初始化无法通过 )。使用 OpenGL 功能 ( [Canvas](Canvas.md) 等 ) 时，请从一开始就用 OpenGL 系的 DrawDevice 启动。

## 成员列表

### 构造函数

- [SDLDrawDevice](#sdldrawdevice)

### 属性

- [interface](#interface)
- [window](#window)
- [sdlVideoPresenterHost](#sdlvideopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)

---

### SDLDrawDevice

构造函数

**说明**

构建 SDLDrawDevice 对象

构建 SDLDrawDevice 类的对象。

在本类为启动时默认 ( OpenGL 禁用构建，或指定 `-drawdevice=sdl` 时 ) 的情况下，Window.drawDevice 中从一开始就注册着本类的实例，因此无需重新注册。

---

### interface

属性 \ 访问: `r`

**说明**

获取接口对象

用于插件等利用 DrawDevice 对象。

---

### window

属性 \ 访问: `r`

**说明**

获取关联的 Window 对象

返回设置了该 DrawDevice 的 Window 对象。

---

### sdlVideoPresenterHost

属性 \ 访问: `r`

**说明**

叠加视频 presenter 注册入口 (指针值)

叠加视频侧为了以 pull 型合成到该 DrawDevice 而读取的 presenter host
的指针值 (与 WINVER 的 [videoPresenterHost](Window.BasicDrawDevice.md#videopresenterhost) 相同规约)。
通常由引擎内部/插件使用。

---

### dialogRendererHost

属性 \ 访问: `r`

**说明**

Elements 对话框 renderer host (指针值)

用于获取 Elements 的覆盖层绘制适配器的 host 指针值。
通常由引擎内部/插件使用。

---

### viewportBackgroundHost

属性 \ 访问: `r`

**说明**

视口余白涂色填充注册入口 (指针值)

接收游戏画面未覆盖整个绘制区域时的余白 ( [Window.viewportBgColor](Window.md#viewportbgcolor) /
[Window.setViewportWallpaper](Window.md#setviewportwallpaper) ) 的
`iTVPViewportBackgroundHost` 指针值。 Window 仅在该属性非 0
时才反映余白设置 ( 在不持有该属性的绘制设备中，余白的涂色填充
不生效，保持该设备默认的填充 )。 通常由引擎内部/插件
使用。

---
