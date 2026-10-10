---
name: krkrz
description: 吉里吉里Z (kirikiri Z) 本体クラス API のリファレンス。TJS2 で吉里吉里Z 上のスクリプトを書く、レビューする、デバッグするときに使う。Layer / Window / Bitmap / System / Storages / Font / Plugins / Timer / Debug / AsyncTrigger / Scripts / BinaryStream / Matrix32 / Matrix44 / Rect / ImageFunction のコア API、サウンド系 (WaveSoundBuffer / SoundBuffer / VideoOverlay)、DrawDevice (BasicDrawDevice / SDLDrawDevice / OGLDrawDevice / NullDrawDevice)、OpenGL 描画系 (Canvas / Texture / ShaderProgram / Offscreen / VertexBinder / VertexBuffer)、および主要プラグイン提供クラス (HttpRequest / GdiPlus.* / WIN32Dialog / CSVParser / LineParser / Process / Pad / MenuItem / Unzip / Zip / PSD / SimpleHTTPServer) を網羅。**呼び出されたら必ず「共通パターン」と「クロスカッティング概念」を確認し、必要な詳細クラスは doc/reference/*.md を Read しに行くこと。** TJS2 言語そのものや組み込みクラス (Array / Dictionary / Math 等) は別 skill (`tjs2`) を参照。エンジン内部構造 (C++ 実装、レンダリングパイプライン詳細) は対象外。中文说明：吉里吉里Z（kirikiri Z）引擎本体类 API（Window / Layer / Bitmap / Storages / DrawDevice 等）的参考文档，在 TJS2 中编写、审查、调试吉里吉里Z 脚本时使用。触发词：吉里吉里Z、krkrz、TJS2、引擎本体API、图层、绘制、存储、DrawDevice、事件、插件。
---

> **路径基点**：本文的相对路径以 **krkrz_dev 仓库根目录为基准**。当工作目录不是 krkrz_dev（如 krkrz_android / krkrz_ios 等外围仓库或项目文件夹）时，请**在前面加上 `${KRKRZ_BASE}/krkrz_dev/`** 再读取（用 `echo $KRKRZ_BASE` 确认实际路径。每台机器的值不同，不要写入绝对路径）。

# 吉里吉里Z 引擎本体类 API 参考文档

这是吉里吉里Z（kirikiri Z）从 TJS2 可见的类 API 技能。从脚本作者的角度，快速定位
"用哪个类""调用哪个方法"。更深入的说明请用 Read 读取 reference/*.md。

## 重要：开始工作之前

1. **务必先确认下面的「横切概念」**。如果把 Layer 树 / 事件 /
   存储 / DrawDevice 的思维模型搞错，就会用错 API 组合（例：Layer 既是 GUI
   部件也是绘制面，Bitmap 是与 Layer 相互独立的 bits 区域）。
2. **关于 TJS2 语言本身的问题请参照另一 skill（`tjs2`）**。`var` / 字典
   字面量 `%[ ... ]` / `new Foo()` 必须带括号 等与 JS 不同的语法都集中在那里。
3. **类的具体细节请 Read `doc/reference/<Class>.md`**。本文件只是
   入口，深入内容在 reference 中。

## 横切概念（搞错这些就会卡死）

### Layer 树

- 1 个窗口拥有 1 个**主图层**（[Window.primaryLayer](doc/reference/Window.md#primarylayer)）
- [Layer](doc/reference/Layer.md) 是父子树结构。通过 `parent`/`children`/`order` 定位
- 图层**同时兼有**「绘制面（持有图像的 Bitmap）」+「GUI 部件（焦点・光标・hint・hitTest）」
- 绘制相关属性：`width`/`height`（绘制区域）、`imageWidth`/`imageHeight`（Bitmap 部分）、`clip*`（裁剪矩形）、`face`（绘制面的种类）、`type`（合成方式）
- 用 [Layer.face](doc/reference/Layer.md#face) 的值切换 `dfBoth`/`dfMain`/`dfProvince`/`dfAlpha` 等
- 输入：`cursor`/`hint`/`hitType`/`focusable`/`enabled` 以图层为单位，用 `focused` 控制焦点
- 绘制：`loadImages`/`drawText`/`fillRect`/`copyRect`/`affineCopy` 等。用 `update()` 设置重绘标志
- 动态生成基本固定为 `new Layer(window, parent)` + `setImageSize(w, h)` + `setSize(w, h)`

### 事件

- **同步事件**：在方法调用过程中发生（例：`play` 中触发 SoundBuffer 的 `onStatusChanged`）
- **异步事件**：经由事件队列，在其他处理器完成后分发（例：`onTimer`、用户输入）
- **画面反映也是异步的**：即使在同一个处理器内多次调用 `update`，在退出该处理器之前画面也不会更新
- 从脚本侧产生异步事件使用 [AsyncTrigger](doc/reference/AsyncTrigger.md)
- 事件处理器的注册方法是**把函数赋值给属性**（`layer.onMouseDown = function(x, y, ...) { ... }`）
- 在子类中重写 super 的处理器时，写法如 `function onTimer() { super.onTimer(...);  ... }`
- 详情：`doc/guide/EventSystem.md`

### 统一存储名（`file://./...`）

- 记法：`媒体://域/路径`（分隔符为 `/`）
- 本地文件：`file://./c/program files/...`（包含 Windows 驱动器号）
- 归档内：`archive.xp3>file.png`（分隔符 `>`，2.19 beta 14 起。旧的 `#` 可用 `-arcdelim=#` 兼容）
- 自动搜索路径：用 [Storages.addAutoPath](doc/reference/Storages.md#addautopath) 注册，以相对名变为可查找
- 所有路径都会经 `Storages.getFullPath` 规范化。在未定义 `TVP_NO_NORMALIZE_PATH` 的构建中，目录枚举结果也会转为小写
- 详情：`doc/guide/StorageSystem.md`

### 文件 / 图像缓存（2 层结构）

- **file 层**：把从存储读出的二进制数据保持在内存中（StorageCache）。用 `addCacheTargetExtension(ext, minSize)` 注册目标
- **decode 层**：保存图像解码结果的 Bitmap（ImageCache）。用 `addDecodeTargetExtension(ext, minSize)` 注册目标
- 后台 prefetch：[Storages.requestCache](doc/reference/Storages.md#requestcache)（对两层都触发）、[Storages.requestFastCache](doc/reference/Storages.md#requestfastcache)
- 进度确认：[Storages.isCacheLoading](doc/reference/Storages.md#iscacheloading)（file 层）、[Storages.isImagePrefetchLoading](doc/reference/Storages.md#isimageprefetchloading)（decode 层）
- pin 管理：[Storages.pinCache](doc/reference/Storages.md#pincache) / [Storages.unpinCache](doc/reference/Storages.md#unpincache)（被 pin 的内容不会因 transient clear 而消失）
- 全部删除 / 部分删除：[Storages.clearAllCaches](doc/reference/Storages.md#clearallcaches) / [Storages.clearTransientCaches](doc/reference/Storages.md#cleartransientcaches) / [Storages.clearCache](doc/reference/Storages.md#clearcache)
- 条目枚举：[Storages.getFileCacheList](doc/reference/Storages.md#getfilecachelist) / [Storages.getImageCacheList](doc/reference/Storages.md#getimagecachelist)
- 详情：`doc/topics/core/memory_observation.md`

### DrawDevice（窗口 → 画面的绘制器）

- 可通过 [Window.drawDevice](doc/reference/Window.md#drawdevice) 属性切换
- 4 种：[BasicDrawDevice](doc/reference/Window.BasicDrawDevice.md)（WINVER 默认、Direct3D）、[SDLDrawDevice](doc/reference/SDLDrawDevice.md)（SDL3 默认、SDL_Renderer）、[OGLDrawDevice](doc/reference/OGLDrawDevice.md)（OpenGL ES、Canvas/Shader/Texture/Offscreen 有效）、[NullDrawDevice](doc/reference/NullDrawDevice.md)（不绘制）
- **OGLDrawDevice 是 lazy 初始化**：从 TJS 替换的瞬间才生成 GL 上下文，在此之前无法使用 Canvas/Texture/Shader 等
- 启动时的默认值可用 `-drawdevice` 选项覆盖（`sdl` / `sdlogl` / `ogl`）

### OpenGL 系（仅在 OGLDrawDevice 之下有效）

- [Canvas](doc/reference/Canvas.md) — OGL 绘制上下文，`drawTexture`/`fillRect`/`drawTransition`（内建双纹理交叉淡化 / rule 图像通用转场，phase 0-1・rule 为 tcfAlpha・vague 0-255）等
- [Texture](doc/reference/Texture.md) — GL 纹理。从 Bitmap 或 Storage 生成
- [Offscreen](doc/reference/Offscreen.md) — 离屏渲染目标
- [ShaderProgram](doc/reference/ShaderProgram.md) — GLSL 着色器
- [VertexBuffer](doc/reference/VertexBuffer.md) / [VertexBinder](doc/reference/VertexBinder.md) — 顶点缓冲区
- 在未激活 OGLDrawDevice 的状态下 new 这些对象也无效

### Bitmap 与 Layer 的关系

- [Bitmap](doc/reference/Bitmap.md) 是**独立的 bits 区域**。也可以通过 Layer.mainImageBuffer 访问，但可以作为独立对象 new
- [BitmapLayerTreeOwner](doc/reference/BitmapLayerTreeOwner.md) 是把「Layer 树写入 Bitmap」的容器。用于截图和动态图层渲染
- Layer 是绘制面 + GUI，Bitmap 是纯粹的像素序列。不要混淆

### finalize 与 invalidate

- 所有类都通过 GC 或显式 `invalidate` 销毁对象。若定义了 `finalize()` 方法则会被调用
- 推荐对 Window / Layer / Bitmap 等重量级对象显式调用 `invalidate`
- 注意：在 finalize 内抛出异常会让处理系统陷入困境

## 类索引（Read doc/reference/<Name>.md）

文件相对于 krkrz_dev 仓库根目录为 `doc/reference/<Name>.md`。
在线版见 <https://wamsoft.github.io/krkrz_dev/reference/<name>/> 。

### 窗口 / 图层 / 绘制

| 类 | 主要作用 |
|---|---|
| [Window](doc/reference/Window.md) | 主窗口、大小、`drawDevice`、输入事件 `onKeyDown`/`onMouseDown` 等、`primaryLayer` |
| [Layer](doc/reference/Layer.md) | 图层树、Bitmap 绘制（`loadImages` / `drawText` / `fillRect` / `copyRect` / `affineCopy`）、GUI 功能 |
| [Bitmap](doc/reference/Bitmap.md) | 独立的 bits 区域、`load`/`save`/`loadAsync` |
| [BitmapLayerTreeOwner](doc/reference/BitmapLayerTreeOwner.md) | 把 Layer 树写入 Bitmap |
| [Font](doc/reference/Font.md) | 字体设置（face / height / italic / bold / strikeout） |
| [Rect](doc/reference/Rect.md) | 矩形 |
| [Matrix32](doc/reference/Matrix32.md) / [Matrix44](doc/reference/Matrix44.md) | 2D / 3D 变换矩阵 |
| [ImageFunction](doc/reference/ImageFunction.md) | 图像变换工具 |
| [PreRenderedFontImage](doc/reference/PreRenderedFontImage.md) | 预渲染字体（tftSave 插件提供） |

### DrawDevice

| 类 | 平台 |
|---|---|
| [BasicDrawDevice](doc/reference/Window.BasicDrawDevice.md) | WINVER 默认（Direct3D） |
| [SDLDrawDevice](doc/reference/SDLDrawDevice.md) | SDL3 默认（SDL_Renderer） |
| [OGLDrawDevice](doc/reference/OGLDrawDevice.md) | OpenGL ES、启用 Canvas/Shader |
| [NullDrawDevice](doc/reference/NullDrawDevice.md) | 不绘制（无头 / 验证用） |

### OpenGL（仅 OGLDrawDevice 之下）

| 类 | 作用 |
|---|---|
| [Canvas](doc/reference/Canvas.md) | OGL 绘制上下文 |
| [Texture](doc/reference/Texture.md) | GL 纹理 |
| [Offscreen](doc/reference/Offscreen.md) | 离屏渲染目标 |
| [ShaderProgram](doc/reference/ShaderProgram.md) | GLSL 着色器 |
| [VertexBuffer](doc/reference/VertexBuffer.md) | 顶点缓冲区 |
| [VertexBinder](doc/reference/VertexBinder.md) | 顶点属性绑定器 |

### 声音 / 视频

| 类 | 作用 |
|---|---|
| [WaveSoundBuffer](doc/reference/WaveSoundBuffer.md) | 波形音频（BGM/SE） |
| [WaveSoundBuffer.PhaseVocoder](doc/reference/WaveSoundBuffer.PhaseVocoder.md) | 音高 / 速度独立变更 |
| [SoundBuffer](doc/reference/SoundBuffer.md) | 声音缓冲区（PCM 生成等底层） |
| [VideoOverlay](doc/reference/VideoOverlay.md) | 视频播放 |

### 存储 / I/O

| 类 | 作用 |
|---|---|
| [Storages](doc/reference/Storages.md) | 文件 / 归档操作、auto path、cache 管理 |
| [BinaryStream](doc/reference/BinaryStream.md) | 二进制流 |

### 系统 / 事件 / 插件

| 类 | 作用 |
|---|---|
| [System](doc/reference/System.md) | OS 信息、命令行、内存统计、手柄、`addContinuousHandler` |
| [Plugins](doc/reference/Plugins.md) | 插件的 link/unlink，用 `canLink` 预判 |
| [Scripts](doc/reference/Scripts.md) | 脚本的编译 / 执行 |
| [Timer](doc/reference/Timer.md) | 周期 / 单发定时器 |
| [AsyncTrigger](doc/reference/AsyncTrigger.md) | 自行触发异步事件 |
| [Debug](doc/reference/Debug.md) | 日志输出 / 控制台输出 |
| [Console](doc/reference/Console.md) | 控制台窗口 |
| [Clipboard](doc/reference/Clipboard.md) | 剪贴板 I/O |
| [Controller](doc/reference/Controller.md) | 控制器（调试操作 UI） |

### 插件提供的类（主要）

| 类 | 提供插件 | 用途 |
|---|---|---|
| [HttpRequest](doc/reference/HttpRequest.md) | httprequest | HTTP 客户端 |
| [GdiPlus.Image](doc/reference/GdiPlus.Image.md) / [.Path](doc/reference/GdiPlus.Path.md) / [.Matrix](doc/reference/GdiPlus.Matrix.md) / [.Font](doc/reference/GdiPlus.Font.md) / [.Appearance](doc/reference/GdiPlus.Appearance.md) / [.PointF](doc/reference/GdiPlus.PointF.md) / [.RectF](doc/reference/GdiPlus.RectF.md) | layerExDraw | GDI+ 矢量绘制 |
| [WIN32Dialog](doc/reference/WIN32Dialog.md) / [WIN32DialogEX](doc/reference/WIN32DialogEX.md) / [.Header](doc/reference/WIN32Dialog.Header.md) / [.Items](doc/reference/WIN32Dialog.Items.md) | win32dialog | Win32 对话框 |
| [CSVParser](doc/reference/CSVParser.md) | csvParser | CSV 解析器 |
| [LineParser](doc/reference/LineParser.md) | lineParser | 行解析器 |
| [Process](doc/reference/Process.md) | process | 进程启动 |
| [Pad](doc/reference/Pad.md) | windowEx | 手柄（高功能版） |
| [MenuItem](doc/reference/MenuItem.md) | menu | 菜单项 |
| [Unzip](doc/reference/Unzip.md) / [Zip](doc/reference/Zip.md) | minizip | ZIP I/O |
| [PSD](doc/reference/PSD.md) | psdfile | PSD 文件读取 |
| [SimpleHTTPServer](doc/reference/SimpleHTTPServer.md) | httpserv | 简易 HTTP 服务器 |

### 主要工具插件（Scripts / Array / Dictionary 扩展）

这些不是吉里吉里引擎本体而是插件，但实际运营中的脚本经常默认它们存在。写 standalone
tool 时需要自己链接：

| 插件 | 提供功能 | 备注 |
|---|---|---|
| `scriptsEx.dll` | `Scripts.foreach(obj, func, args*)` / `Scripts.getObjectKeys(obj)` / `Scripts.getObjectCount(obj)` / `Scripts.getObjectContext(obj)` / `Scripts.equalStruct(a, b)` / `Scripts.clone(obj)` / `Scripts.propSet` / `Scripts.propGet` | 引擎本体没有 Dictionary 的枚举 API，因此事实上必需 |
| `saveStruct.dll` | `Array.save2(file, utf8=false, newline=0)` / `Array.saveStruct2(file, utf8, newline, opt)` / `Dictionary.saveStruct2(file, utf8, newline, opt)` / `.toStructString(newline, opt)` | 内置 `Array.save` 固定为 UTF-16 LE + BOM，需要保存 UTF-8 文本时用这个 |
| `fstat.dll` | `Storages.dirlistEx(dir)`（带 size / attrib / 时间的枚举） / 文件属性的获取・设置 / 写入时间 / `fstat`・`getTime` 的 `atime`・`ctime` | **`dirlist` / `dirtree` / `createDirectory` / `isExistentDirectory` / `fstat`（size + mtime） / `getTime`（mtime） / `currentPath`（读取）引擎本体也有**（无需链接，所有构建可用）。读取插件后，`fstat` / `getTime` / `currentPath` / `dirlistEx` 会替换为插件版（信息更多的版本）。目录参数末尾必须带 `/`。SSOT = src/core/doc/LocalFileOps.md |
| `PackinOne.dll` | 整合提供上述 fstat / saveStruct / scriptsEx 的部分功能 | wamsoft 独有的整合版。但 link 时会经 fstat 执行路径验证，在 standalone 环境中有时会 init throw。只需要单项功能时，分开用各插件更安全 |

**Scripts.foreach 的陷阱**（scriptsEx.dll）：
回调函数的执行上下文在调用方插件侧，因此**引用外层函数的 local 变量会引发运行时异常**。对策：
- 使用追加参数机制：`Scripts.foreach(obj, function(k, v, arg) { ... }, arg)`
- 用 `Scripts.getObjectKeys(obj)` 取出 keys 数组，用原生 `for` 循环迭代（最可靠）

更详细的内容也请参照 tjs2 skill 的「闭包的陷阱」。

## 通用模式

### 事件处理器注册

```tjs
// プロパティに関数を代入
layer.onMouseDown = function(x, y, button, shift) { ... };

// または class サブクラスで override
class MyLayer extends Layer {
    function MyLayer(win, parent) { super.Layer(win, parent); }
    function onMouseDown(x, y, button, shift) {
        super.onMouseDown(x, y, button, shift);
        // 追加処理
    }
}
```

### Layer 的典型初始化

```tjs
var lay = new Layer(window, parent);
lay.setImageSize(640, 480);   // Bitmap 部分のサイズ
lay.setSize(640, 480);         // 表示サイズ
lay.setPos(0, 0);              // 位置
lay.loadImages("bg/title");    // 自動検索パスから
lay.visible = true;
```

### 异步图像读取 + cache

```tjs
Storages.addCacheTargetExtension(".png");
Storages.addDecodeTargetExtension(".png");
Storages.requestCache("bg/title.png");  // 非同期 prefetch
// ... 後で loadImages したときに cache hit
```

### Timer 周期处理

```tjs
class MyTimer extends Timer {
    function MyTimer() { super.Timer(); interval = 1000; enabled = true; }
    function onTimer() { /* 1秒毎 */ }
}
```

### 切换 DrawDevice 启用 OGL

```tjs
// OGLDrawDevice に切替えてから Canvas/Shader 系を new する
window.drawDevice = new OGLDrawDevice();
var canvas = new Canvas(window);
var tex = new Texture(window, "image.png");
```

## 相关文档

- 指南（概念解说）：`doc/guide/EventSystem.md`, `doc/guide/StorageSystem.md`, `doc/guide/GraphicSystem.md`, `doc/guide/SoundSystem.md`, `doc/guide/CommandLine.md`
- 朗读（屏幕阅读器）：`doc/guide/Accessibility.md`。画在 Layer 上的 UI 用 `ElementsDialog.setGameA11y`（传入节点表）或 `ElementsDialog.a11yLayers = true`（自动装载焦点链上的 Layer。可在 Layer 上添加 `a11yName` / `a11yRole` / `a11yHidden` / `onA11yAction` 等来补充 — 列表见 `doc/reference/Layer.md` 的类说明）。任意语句用 `ElementsDialog.announce`
- 周边信息：`doc/topics/core/*.md`（gamepad〔标识 / 位置 2 套系统・padStyle〕、viewport、engine_setting、memory_observation、low_memory、draw_stats、pad_overlay、repl、logging、anti_cracking）
- TJS2 语言本体见另一 skill（`tjs2`）

## 相关技能

- skill `tjs2` — TJS2 语言规格与内置类（Array / Dictionary / Math / Date / RegExp / Exception 等）
- （未创建）吉里吉里Z 内部结构 / engine internals — C++ 实现、渲染管线、SIMD、插件加载器等

引擎内部计划另建 skill。本技能只覆盖从 TJS 可见的表层 API。