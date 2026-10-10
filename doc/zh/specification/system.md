# 系统构成

记载吉里吉里Z (Wamsoft 派生实现) 的系统构成。

## 概要

现行的吉里吉里Z 大致分为 2 个构建系列。

- **WINVER** — Windows 原生实现。绘制使用 Direct3D 11，窗口/输入使用 Win32 API。是专用于在 Windows 上运行的系列。
- **SDL(GENERIC)** — 以 SDL3 为基础的跨平台实现，是默认系列。窗口/输入/显示交给 SDL3，绘制以 OpenGL ES 为基础。以 Windows / Linux / macOS / Android / Emscripten(web) 为对象。

此外，还有把 GENERIC 系列汇总为静态库的 **LIB** 形态。它不是可执行文件，而是作为库嵌入其他应用程序的构成，内部组件与 SDL(GENERIC) 共通。

无论哪个系列，都共享 TJS2 语言运行时、图层/Bitmap 的图像处理、OpenGL 绘制类群、miniaudio 音频、插件 ABI 等核心部分，系列的差异主要体现在窗口/绘制/输入/视频/音频的各平台结合部分。

## WINVER 的主要组件

| 功能 | 实现 | 备注 |
| --- | --- | --- |
| 绘制/显示 | Direct3D 11 / DXGI (BasicDrawDevice) | 默认的绘制设备。使用 flip-model 交换链 (`d3d11` / `dxgi` / `d3dcompiler`)。 |
| 窗口/输入 | Win32 API | 窗口创建、消息处理、键盘/鼠标输入。 |
| 手柄 | XInput | 旧的 DirectInput 实现已废除。 |
| 视频 | Media Foundation 等 | 由 Media Foundation SourceReader + IMFMediaEngine 进行 HW 解码，webm 用 movie-player，MPEG-1 用 pl_mpeg。krmovie 直接链接到 exe，旧的 DirectShow/EVR/插件边界已被移除。 |
| 音频 | miniaudio (WASAPI) | miniaudio 持有输出设备。旧的 DirectSound 实现已被移除。 |
| OpenGL ES 路径 (可选) | ANGLE / EGL | `libEGL.dll` / `libGLESv2.dll`。在把 drawDevice 切换到 OpenGL 系时使用。 |

## SDL(GENERIC) 的主要组件

| 功能 | 实现 | 备注 |
| --- | --- | --- |
| 窗口/输入/显示 | SDL3 | 负责窗口创建、输入、计时等。 |
| 绘制设备 | 基于 OpenGL ES (SDLOGLDrawDevice) / 基于 SDL_Renderer (SDLDrawDevice) | 默认是基于 OpenGL ES 的 SDLOGLDrawDevice。也可以选择基于 SDL_Renderer 的 SDLDrawDevice。 |
| OpenGL ES | glad + 平台的 GLES/EGL | 在 Windows 上会透明地回退到 ANGLE。 |
| 视频 | movie-player(webm) + pl_mpeg(MPEG-1) | 在 Emscripten(web) 中会变成使用浏览器 `<video>` 的 WebMoviePlayer。 |
| 音频 | miniaudio (no-device 模式) | miniaudio 以设备 I/O 禁用模式生成 PCM，输出设备由 SDL3 持有。 |

支持的平台是 Windows / Linux / macOS / Android / Emscripten(web)。

## 共享组件

两个系列共享以下组件。

- **TJS2 语言运行时** (`common/tjs2`) — 脚本语言 TJS2 的编译器/执行系统。
- **图层/Bitmap 图像处理** — 针对 CPU 侧 32bpp BGRA 合成面的混合/重采样等。拥有 SIMD 实现 (SSE2 / AVX2 / NEON) 与 C 参考实现 (`tvpgl.c`)。
- **OGLDrawDevice 与 GL 类群** — Canvas / Texture / ShaderProgram / Offscreen 等 OpenGL ES 绘制类群。两个系列共享相同的 GL 代码。
- **miniaudio 音频** — 在所有构建中作为单一音频引擎使用。
- **插件 ABI** — 经由 `tp_stub` 与插件之间的二进制接口。

## 启动时的默认绘制设备

| 系列 | 启动时的默认绘制设备 |
| --- | --- |
| WINVER | BasicDrawDevice (Direct3D 11) |
| SDL(GENERIC) | 基于 OpenGL ES (SDLOGLDrawDevice) |

OGLDrawDevice 在从 TJS 脚本切换 `drawDevice` 的时点被延迟初始化。两个系列都共享相同的 GL 绘制代码，因此切换后的行为是共通的。
