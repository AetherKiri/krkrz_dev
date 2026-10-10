# Wamsoft 派生版中删除/添加的功能

本页汇总了 Wamsoft Ltd. Partnership 维护的派生版 ( [wamsoft/krkrz_dev](https://github.com/wamsoft/krkrz_dev) ) 中，从上流吉里吉里Z / 吉里吉里2 **删除的遗留功能**和**新添加的功能**的概要。

关于个别 TJS API 的删除，也请参照 [吉里吉里Z 中删除的功能](deleted.md)。

## 删除的遗留功能

主要是对 Windows 遗留 API 的依赖以及会成为跨平台化障碍的实现，已被替换、移除。

| 删除的内容 | 替换 / 现状 |
| --- | --- |
| DirectSound ( 音频输出 ) | **miniaudio** ( 所有构建通用的音频引擎。WASAPI 共享模式、支持多声道 ) |
| 基于 DirectShow / EVR 的视频播放 ( `dsmovie` / `dslayerd` 等 ) | 统一为 CPU 解码 ( webm=movie-player / MPEG-1=pl_mpeg / 其他=Media Foundation SourceReader ) + **Direct3D 11 合成** |
| krmovie 的插件边界 ( tp_stub / V2Link DLL 边界 ) | 将 krmovie **直接内置到 exe** ( 直接调用引擎符号 ) |
| krflash / `.swf` ( Flash 视频 ) | 移除 |
| 基于 Direct3D 9 / DirectDraw 的显示 ( 独占全屏等 ) | **Direct3D 11 / DXGI** ( flip-model 交换链、无边框全屏 ) |
| DirectInput ( 手柄 / 鼠标 ) | 手柄为 **XInput**，鼠标滚轮为 `WM_MOUSEWHEEL` ( 通过共享 `tTVPPadManager` 支持多个手柄 ) |
| TLG6 的 NASM 汇编器优化 | C 参考实现 ( `tvpgl.c` )。SSE2/AVX2/NEON 的 SIMD 实现另行提供 |
| JPEG XR ( `.jxr` ) 加载器 | 移除 ( 无替代 ) |
| `timeBeginPeriod` / `timeGetTime` 计时器 | **QueryPerformanceCounter** + 高分辨率等待计时器 |
| 各种遗留 Win32 兼容垫片 ( XP/Vista/7/8 回退 ) | 以 Windows 10 以后为最低目标直接链接 |
| 各种 Perl 编写的生成器 ( `makestub.pl` / `gentext*.pl` 等 ) | **Python** 编写的生成器 ( 输出字节一致 ) |

### 从核心删除的主要 TJS 类 / API

以下是从引擎本体核心删除、由随附的 **Krkr2Compat** 或个别插件补全的要素 ( 详细请参照 [删除的功能](deleted.md) )。

- `KAGParser` 类 → 链接 `KAGParser.dll` 插件来使用
- `Menu` 类 → `menu.dll`
- `Console` 类 / 调试控制台窗口 ( `Debug.console` ) → Krkr2Compat
- `Font.doUserSelect` ( 字体选择对话框 ) / `System.inputString` ( 单行输入 ) → Krkr2Compat
- `Layer.hint`，以及 `affineBlend` / `affinePile` / `blendRect` / `pileRect` / `stretchBlend` / `stretchPile` 等 obsolete 方法 → 可以用 `operateAffine` / `operateRect` / `operateStretch` 以 TJS 重新实现

## 新添加的功能

以跨平台化 ( SDL3 ) 以及 GPU 绘制、开发支持、音频功能的扩展为中心。

| 添加的功能 | 概要 |
| --- | --- |
| SDL3 跨平台构建 | 支持 Windows / Linux / macOS / Android / Emscripten(web) 的 generic 构建，以及静态库形态的 LIB 构建 |
| OpenGL ES 绘制路径 | 延迟初始化的 GPU 绘制设备 [OGLDrawDevice](../../reference/OGLDrawDevice.md)，以及 [Canvas](../../reference/Canvas.md) / [Texture](../../reference/Texture.md) / [ShaderProgram](../../reference/ShaderProgram.md) / [Offscreen](../../reference/Offscreen.md) / VertexBuffer / Matrix32 / Matrix44 等 GL 类群 |
| GLCompositor | 即使在非 GL 绘制设备下，也在背后进行 OpenGL ES 离屏合成并写回 Layer 的类 ( [GLCompositor](../../reference/GLCompositor.md) ) |
| Canvas 转场绘制 | 通过 `Canvas.drawTransition` 进行的基于 GPU 的画面转场绘制 |
| 基于 Elements 的通用对话框 | 由 JSON / Dictionary 定义的跨平台 UI ( [ElementsDialog](../../reference/ElementsDialog.md) 类。详细请参照 [对话框](../../guide/ElementsDialog.md) ) |
| REPL ( 交互式 TJS shell ) | 通过 `-repl` / `-replfile` 进行脚本求值、验证 ( [REPL](../core/repl.md) ) |
| WebServer | 内置 HTTP + SSE 服务器 ( `-replweb` )。可以从 TJS 注册端点 ( [WebServer](../../reference/WebServer.md) ) |
| Agent | 输入注入、画面捕获、对话框操作的自动化驱动 API ( [Agent](../../reference/Agent.md) ) |
| FreeType 彩色 emoji 字体 | CBDT/COLR 彩色 emoji 的光栅化 ( `Font.emojiMode` ) |
| 字体元数据与延迟加载 | 在 `fonts.json` 中声明，首次使用时加载实际文件 ( 削减可执行文件大小 ) |
| 手柄多手柄支持的重新设计 | 支持多个手柄 ( 逻辑手柄 0 = 最后操作的手柄 )、共享 `tTVPPadManager` |
| 音频 3D 定位 ( spatializer ) | 基于 miniaudio 的位置 / 距离 / 多普勒 / 指向性 ( [WaveSoundBuffer](../../reference/WaveSoundBuffer.md) 的 `use3D` 系、[SoundListener](../../reference/SoundListener.md) ) |
| 唇形同步 / 音频解析 API | `getSoundLevel` / `getSoundSpectrum` / `getVowel` / `getVisBuffer` |
| 3D / 特效插件 | threepp ( three.js 移植 ) / Effekseer / Live2D / GLES 辅助 |
| Media Foundation 硬件视频 | 通过 `IMFMediaEngine` 的硬件解码 ( mp4/wmv 为默认，`-mediaengine=no` 时禁用 ) |
| 屏幕内调试显示 | 手柄状态 ( PadOverlay )、内存观测、绘制线程利用率 ( DrawStats ) |
| DPI 支持 / 无边框全屏 / 长路径 | PerMonitorV2 DPI 感知 ( 即使移动到放大率不同的显示器也维持绘制区域的像素尺寸，仅重绘边框 )、`\\?\` 扩展路径支持 |
| 游戏画面的显示画角控制 ( 视口 ) | 在外侧窗口中配置内侧游戏画面，以 fit / zoom / align / offset 指定，留白用背景色或壁纸填充 ( [视口](../core/viewport.md) ) |
| 启动显示器的指定 | 在多显示器环境中，通过编号 / 名称选择最初显示的显示器 `-display` ( [命令行选项](../../guide/CommandLine.md) ) |
| 启动时 DrawDevice 的选择 | 通过 `-drawdevice` 选择启动时的绘制设备 ( SDL3 的默认是基于 OpenGL ES 的 [SDLOGLDrawDevice](../../reference/SDLOGLDrawDevice.md) )。也可以指定强制 GLES 上下文使用 EGL 的 `-forceegl` |
| 消息 / 设置 UI 的多语言化 | 引擎消息与选项说明 ( `-userconf` ) 跟随 OS 语言 ( ja / en / chs / cht )。可通过 `-language` 显式指定 ( [命令行选项](../../guide/CommandLine.md) ) |
