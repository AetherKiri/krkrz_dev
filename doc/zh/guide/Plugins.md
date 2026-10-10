# 关于插件

## 什么是插件

用于连接到吉里吉里，扩展吉里吉里的功能。

现阶段，吉里吉里可用的插件种类有 3 种，具体如下。

- Susie Plug-in (图像读取与归档访问)
- 用于扩展 WaveSoundBuffer 可播放格式的插件
- 其他吉里吉里专用插件



使用插件时，需要使用 [Plugins.link](../reference/Plugins.md#link) 方法连接到吉里吉里引擎本体。

## 插件的搜索

[Plugins.link](../reference/Plugins.md#link) 方法按以下顺序搜索指定的插件。

1. 与吉里吉里引擎本体相同的文件夹
2. 与吉里吉里引擎本体相同的文件夹下的 plugin (Windows 的 64bit 版为 plugin64) 文件夹内
3. 自动搜索路径

### 插件文件夹的名称 (按平台区分) {#plugin-folder}

| 运行环境 | 插件文件夹 |
|---|---|
| Windows 64bit 版 (WINVER / SDL) | `plugin64/` |
| Windows 32bit 版 | `plugin/` |
| Linux / 其他桌面 (含 64bit) | `plugin/` |
| macOS | 与可执行文件相同的文件夹 (应用包的 `Contents/MacOS`) |
| Android | 无 (插件为静态链接) |

!!! warning "重要 (2026-10 的更改)"
    使用 `plugin64/` 的**只有 Windows 的 64bit 版**。在 Linux 等平台上，即使是 64bit 版也会查找 `plugin/`。这与 CMake 的安装目标 (`plugin/`) 是同一规则，Linux 的行为从以前起就没有改变。

    - 在 Linux 等平台上，如果可执行文件旁边存在 `plugin64/`，启动时会在日志中输出“不会搜索”之意的警告。请将其内容移动到 `plugin/`。
    - 实际搜索的文件夹可以通过启动日志中的 `pluginPath:` 行确认 (SDL 版)。
    - 只有用 gcc / clang (MinGW 等) 构建的 **Windows 64bit 的 SDL 版**，搜索目标从 `plugin/` 变成了 `plugin64/` (MSVC 版原本就是 `plugin64/`)。

当自动搜索路径位于归档内等无法作为本地文件访问的位置时，吉里吉里会尝试把插件解压到**与吉里吉里引擎本体相同的文件夹**。由于这可能引发问题，**强烈建议**将插件放在“与吉里吉里引擎本体相同的文件夹”或“与吉里吉里引擎本体相同的文件夹下的 plugin 文件夹内”。


为了在 Windows 上区分读取 32bit 版 / 64bit 版插件，将其放在 plugin/plugin64 文件夹内也很重要。

另外，吉里吉里的设置工具 ( Releaser 或 -userconf 选项 ) 为了收集各插件的内嵌选项信息而搜索插件，搜索顺序如下。

1. 与吉里吉里引擎本体相同的文件夹
2. 与吉里吉里引擎本体相同的文件夹下的 plugin 文件夹内

吉里吉里的设置工具不会搜索到自动搜索路径，因此包含设置项的插件必须放在“与吉里吉里引擎本体相同的文件夹”或“与吉里吉里引擎本体相同的文件夹下的 plugin 文件夹内”。

## 插件的自动加载

吉里吉里具备自动搜索插件并在启动时加载的功能。要让插件被自动加载，需要把插件的扩展名从 dll 改为 tpm。

吉里吉里在启动时 (执行 startup.tjs 之前) 会从以下文件夹中查找扩展名为 tpm 的文件，并作为插件自动加载。

- 与吉里吉里引擎本体相同的文件夹
- 与吉里吉里引擎本体相同的文件夹下的 plugin (Windows 的 64bit 版为 plugin64) 文件夹内

吉里吉里会把找到的插件按名称升序排列，并按该顺序加载插件。例如，aaa.tpm 会比 aab.tpm 先被加载。这与插件所在的文件夹无关，只受插件名称影响 (即使与吉里吉里引擎本体相同的文件夹中有 z.tpm，只要 plugin 文件夹内有 a.tpm，a.tpm 也会先被加载)。如果想规定插件的加载顺序，需要更改插件的文件名。

## 关于插件的创建

吉里吉里的源码中有吉里吉里附带的插件源码，请作为参考。

现阶段，“其他吉里吉里专用插件”的规格**尚未固定**。即使将来规格发生更改，我认为源码级别的兼容性也会保持，因此即使在二进制级别的兼容性丢失的情况下，只要配合吉里吉里引擎本体重新构建，应该就能继续使用。

## 关于 Susie Plug-in

可以利用 Takechin 制作的图像查看器 “Susie32” 用的插件。

可以使用 00IN 格式 (图像用插件) 与 00AM 格式 (归档用插件)，但存在以下限制或吉里吉里特有的规格。

- 吉里吉里通过扩展名判断图像格式，因此无法支持被赋予了与原本扩展名 ( GetPluginInfo 函数返回的扩展名 ) 不同的扩展名的图像 ( 归档会检查所有支持的格式，所以即使扩展名不同也 OK )
- 32bpp 的位图会被视为带 Alpha 通道的位图
- 有一部分不接受的位图格式 (RLE 压缩的、指定了 BITFIELDS 的等 )
- 经由 Susie 插件的图像读取与归档访问，与吉里吉里原生处理的图像格式或 xp3 归档相比，性能会低相当多
- 归档中的文件会被解压到内存上，因此不适合处理大文件
- 不支持归档内嵌套归档
- 不支持 Mac binary

此外，在未完全符合 Susie plug-in 规格的插件中，也存在与吉里吉里兼容性不佳的插件。

## 关于吉里吉里附带的插件

这是吉里吉里Z 标准随附的插件一览。各插件的源代码在 [wamsoft](https://github.com/wamsoft) 下的各仓库中管理。

添加类的插件请参阅参考文档中各类的页面，扩展既有类的插件请参阅扩展目标类的页面中的“插件扩展”一节。

### 所有平台通用

| 插件 | 说明 |
|---|---|
| **AlphaMovie** | 添加播放带 Alpha 通道的视频 ( .amv ) 的 [AlphaMovie](../reference/AlphaMovie.md) 类。 |
| **clipfile** | 添加进行 CLIP STUDIO PAINT 文件 ( .clip ) 读取、编辑、保存的 [CLIP](../reference/CLIP.md) / [CLIPWriter](../reference/CLIPWriter.md) 类。也可以用 `clip://` 直接加载图层图像。 |
| **csvParser** | 添加解析 CSV 文件的 [CSVParser](../reference/CSVParser.md) 类。 |
| **expat** | 添加解析 XML 的 [XMLParser](../reference/XMLParser.md) 类。 |
| **extrans** | 注册 wave / mosaic / turn / rotatezoom / rotatevanish / rotateswap / ripple 7 种追加转场。详情请参阅[转场](Transition.md)。 |
| **extNagano** | 注册 3duniversal / blurfade / scanline / zoomfade / rgbfade / spin / flutter / book / imagewipe / honeyturn / morphing / multiripple 12 种追加转场。详情请参阅[转场](Transition.md)。 |
| **getSample** | 向 [WaveSoundBuffer](../reference/WaveSoundBuffer.md) 添加获取播放中声音采样值的方法。 |
| **json** | 向 [Scripts](../reference/Scripts.md) 添加 JSON 的读写 ( evalJSON / saveJSON 等 )。 |
| **KAGParserEx** | 添加解析 KAG 剧本的 [KAGParser](../reference/KAGParser.md) 类 ( 用扩展版替换引擎本体内置版 )。 |
| **krkr_richtext** | 添加进行支持多语言与装饰的富文本绘制的 [RichText](../reference/RichText.md) 类群与 [Layer](../reference/Layer.md) 扩展。 |
| **layerExAreaAverage** | 向 [Layer](../reference/Layer.md) 添加基于面积平均法的高品质缩小拷贝。 |
| **layerExBTOA** | 向 [Layer](../reference/Layer.md) 添加把蓝色分量转换为 Alpha 值的方法。 |
| **layerExImage** | 向 [Layer](../reference/Layer.md) 添加明度 / 对比度 / 色相 / 饱和度调整及添加噪声等图像处理。 |
| **layerExLongExposure** | 向 [Layer](../reference/Layer.md) 添加长时间曝光 ( 帧累积合成 ) 风格的效果。 |
| **layerExRaster** | 向 [Layer](../reference/Layer.md) 添加光栅滚动效果。 |
| **layerExSave** | 向 [Layer](../reference/Layer.md) / [Window](../reference/Window.md) 添加图层图像的异步保存 ( PNG / TLG5 )。 |
| **layerExVector** | 向 [Layer](../reference/Layer.md) 添加基于 thorvg 的 SVG 等矢量绘制 ( [GdiPlus](../reference/GdiPlus.md) 兼容 API )。 |
| **lineParser** | 添加进行按行文本解析的 [LineParser](../reference/LineParser.md) 类。 |
| **minizip** | 添加进行 ZIP 归档读取 ( zip:// 自动搜索路径 ) 与创建的 [Zip](../reference/Zip.md) / [Unzip](../reference/Unzip.md) 类。 |
| **psdfile** | 添加进行 Photoshop PSD 文件读取、编辑、保存的 [PSD](../reference/PSD.md) 类。也可以用 `psd://` 直接加载图层图像。 |
| **saveStruct** | 扩展 Array / Dictionary 的 saveStruct，使 UTF-8 等输出编码可以指定 ( 请参阅 [Scripts](../reference/Scripts.md) )。 |
| **scriptsEx** | 向 [Scripts](../reference/Scripts.md) 添加脚本执行相关的实用工具。 |
| **shrinkCopy** | 向 [Layer](../reference/Layer.md) 添加高速缩小拷贝。 |
| **sigcheck** | 向 [Window](../reference/Window.md) 添加文件签名的后台验证。 |

#### OpenGL ES 绘制类

这是使用 GLES ( ANGLE/glad ) 进行绘制的插件群。绘制目标的 GL 上下文由吉里吉里引擎本体的 `OGLDrawDevice`，或者在 Windows 上由 `krkrgles` 的 `GLESAdaptor` 提供。

| 插件 | 说明 |
|---|---|
| **krkreffekseer** | 添加将 [Effekseer](https://effekseer.github.io/) 的效果 ( .efk / .efkefc / .efkzip ) 绘制到宿主提供的 GL 上下文的 `EffekseerDevice` / `EffekseerEffect` / `EffekseerPlayer` 类。 |
| **krkrlive2d** | 添加播放、绘制 Live2D Cubism 模型的 `Live2DDevice` / `Live2DModel` / `Live2DPlayer` / `Live2DMatrix` 类。**由于需要 Live2D Cubism Core，仅在设置了环境变量 `CUBISM_SDK` 时才会构建** ( 驱动侧 CMake 会引用 `$CUBISM_SDK/Core` )。 |
| **krkrgles** | 添加将经由 OpenGL ES ( ANGLE/EGL ) 绘制的结果回收到 [Layer](../reference/Layer.md) 的 `GLESAdaptor` / `GLESTexture` 类。具备在 GPU 上闭环完成的后处理效果机制。**由于要从 `Window.HWND` 生成 EGL/ANGLE 上下文，因此为 Windows 专用** ( 在 macOS / Linux 上，GL 上下文请利用引擎本体的 `OGLDrawDevice` )。 |

### Windows ( WINVER 构建 ) 专用

由于依赖 Win32 API，目前仅在 WINVER 构建中可以使用。

| 插件 | 说明 |
|---|---|
| **addFont** | 进行私有字体 ( .ttf / .otf ) 的动态添加 ( 引擎本体的 [System.addFont](../reference/System.md#addfont) 也能做同样的事 )。 |
| **binaryStream** | 添加以二进制级别读写文件的 [BinaryStream](../reference/BinaryStream.md) 类。 |
| **fpslimit** | 对主循环的执行频率施加限制 ( 现在可以用引擎本体的 -contfreq 选项替代 )。 |
| **fstat** | 向 [Storages](../reference/Storages.md) 添加文件大小与更新时间的获取等。基本的文件操作 ( `fstat` / `getTime` / `copyFile` / `dirlist` 等 ) 在引擎本体中也有，任何构建都能使用。加载本插件后，`fstat` / `getTime` / `currentPath` / `dirlistEx` 会被替换为返回创建、访问时间与属性的版本，并增加属性设置等 Win32 固有操作。 |
| **gamepad** | 添加直接操作手柄的 [Pad](../reference/Pad.md) 类。 |
| **httprequest** | 添加进行 HTTP 通信的 [HttpRequest](../reference/HttpRequest.md) 类。 |
| **layerExDraw** | 添加进行基于 GDI+ 的图形 / 文本绘制的 [GdiPlus](../reference/GdiPlus.md) 类群。 |
| **memfile** | 向 [Storages](../reference/Storages.md) 添加内存上的虚拟文件 ( mem:// )。 |
| **menu** | 添加构建窗口菜单的 [MenuItem](../reference/MenuItem.md) 类。 |
| **messenger** | 向 [Window](../reference/Window.md) 添加与外部进程之间基于 WM_COPYDATA 的消息交换。 |
| **msgreceiver** | 添加外部控制的入口 ( WM_COPYDATA 接收 ) ( 已不推荐。请使用 messenger )。 |
| **process** | 添加进行外部进程启动与监视的 [Process](../reference/Process.md) 类。 |
| **shellExecute** | 向 [System](../reference/System.md) 添加通过关联应用程序打开文件 / URL。 |
| **stdio** | 向 [System](../reference/System.md) 添加对标准输入输出的访问。 |
| **systemEx** | 向 [System](../reference/System.md) 添加 OS 信息获取等实用工具。环境变量与 URL 编码 ( `readEnvValue` / `urlencode` 等 ) 在引擎本体中也有，会使用引擎本体版。本插件中保留的是注册表 / OS 版本 / 已知文件夹 / DLL 搜索路径等 Win32 固有功能。 |
| **tftSave** | 向 [System](../reference/System.md) / [Layer](../reference/Layer.md) 添加已渲染字体数据的保存功能。 |
| **varfile** | 添加把 TJS 的变量空间 ( 字典中的 octet ) 作为文件引用的 var:// 访问。 |
| **win32dialog** | 添加构建 Win32 原生对话框的 [WIN32Dialog](../reference/WIN32Dialog.md) 类。 |
| **win32ole** | 添加处理 OLE 自动化 / ActiveX 的 [WIN32OLE](../reference/WIN32OLE.md) / [ActiveX](../reference/ActiveX.md) / [JScriptHost](../reference/JScriptHost.md) 类。 |
| **windowEx** | 向 [Window](../reference/Window.md) / [System](../reference/System.md) / [Console](../reference/Console.md) 等添加窗口操作的各种扩展。最大化 / 矩形 / 扩展事件 / 监视器信息在引擎本体中也有，任何构建都能使用 ( 加载本插件后会被插件版覆盖 )。已预定废止。 |
| **windowExProgress** | 向 [Window](../reference/Window.md) 添加即使处于执行阻塞中也持续显示的带进度条窗口显示。 |
