# System

System 类是用于获取和设置吉里吉里本体以及吉里吉里运行环境相关信息的类。不能从该类创建对象。

## 成员列表

### 属性

- [versionString](#versionstring)
- [versionInformation](#versioninformation)
- [eventDisabled](#eventdisabled)
- [graphicCacheLimit](#graphiccachelimit)
- [platformName](#platformname)
- [osName](#osname)
- [exePath](#exepath)
- [resourcePath](#resourcepath)
- [replWebURL](#replweburl)
- [personalPath](#personalpath)
- [appDataPath](#appdatapath)
- [dataPath](#datapath)
- [exeName](#exename)
- [title](#title)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [desktopLeft](#desktopleft)
- [desktopTop](#desktoptop)
- [desktopWidth](#desktopwidth)
- [desktopHeight](#desktopheight)
- [exitOnWindowClose](#exitonwindowclose)
- [exceptionHandler](#exceptionhandler)
- [onActivate](#onactivate)
- [onDeactivate](#ondeactivate)
- [onJoypadChange](#onjoypadchange)
- [drawThreadNum](#drawthreadnum)
- [savedGamesPath](#savedgamespath)
- [exeBits](#exebits)
- [osBits](#osbits)
- [exitOnNoWindowStartup](#exitonnowindowstartup)
- [isGeneric](#isgeneric)
- [isWindows](#iswindows)
- [licenseText](#licensetext)
- [openGLESVersion](#openglesversion)
- [processorNum](#processornum)
- [renderStats](#renderstats)
- [texUploadUsePBO](#texuploadusepbo)
- [touchDevice](#touchdevice)
- [platformTag](#platformtag)
- [systemLanguage](#systemlanguage)
- [padButtonMapping](#padbuttonmapping)
- [padStyle](#padstyle)
- [buildVariantName](#buildvariantname)
- [padAxisLeftX](#padaxisleftx)
- [padAxisLeftY](#padaxislefty)
- [padAxisRightX](#padaxisrightx)
- [padAxisRightY](#padaxisrighty)
- [padAxisLeftTrigger](#padaxislefttrigger)
- [padAxisRightTrigger](#padaxisrighttrigger)
- [padEnabled](#padenabled)
- [replActive](#replactive)

### 方法

- [terminate](#terminate)
- [exit](#exit)
- [addContinuousHandler](#addcontinuoushandler)
- [removeContinuousHandler](#removecontinuoushandler)
- [inform](#inform)
- [confirm](#confirm)
- [inputString](#inputstring)
- [choice](#choice)
- [getTickCount](#gettickcount)
- [getKeyState](#getkeystate)
- [registerHotKey](#registerhotkey)
- [unregisterHotKey](#unregisterhotkey)
- [shellExecute](#shellexecute)
- [readRegValue](#readregvalue)
- [getArgument](#getargument)
- [setArgument](#setargument)
- [toActualColor](#toactualcolor)
- [createAppLock](#createapplock)
- [createUUID](#createuuid)
- [assignMessage](#assignmessage)
- [doCompact](#docompact)
- [touchImages](#touchimages)
- [showVersion](#showversion)
- [dumpHeap](#dumpheap)
- [captureScreen](#capturescreen)
- [renderStatsReset](#renderstatsreset)
- [addFont](#addfont)
- [clearGraphicCache](#cleargraphiccache)
- [getJoypadType](#getjoypadtype)
- [nullpo](#nullpo)
- [system](#system)
- [getSystemAllocatorInfo](#getsystemallocatorinfo)
- [resetMemoryPeak](#resetmemorypeak)
- [beginAllocTag](#beginalloctag)
- [endAllocTag](#endalloctag)
- [setMemoryOverlay](#setmemoryoverlay)
- [setPadOverlay](#setpadoverlay)
- [setDrawStatsLog](#setdrawstatslog)
- [getTextureMemory](#gettexturememory)
- [setTextureMemoryLog](#settexturememorylog)
- [resetTextureMemoryPeak](#resettexturememorypeak)
- [getJoypadCount](#getjoypadcount)
- [hasJoypad](#hasjoypad)
- [getPadAxis](#getpadaxis)
- [rumblePad](#rumblepad)
- [stopRumblePad](#stoprumblepad)
- [getLicenseList](#getlicenselist)
- [getLicenseText](#getlicensetext)
- [readEnvValue](#readenvvalue)
- [writeEnvValue](#writeenvvalue)
- [expandEnvString](#expandenvstring)
- [urlencode](#urlencode)
- [urldecode](#urldecode)
- [getAboutString](#getaboutstring)
- [breathe](#breathe)
- [getMonitorInfo](#getmonitorinfo)
- [getDisplayMonitors](#getdisplaymonitors)
- [getSystemMetrics](#getsystemmetrics)

---

### versionString

属性 \ 访问: `r`

**说明**

版本字符串

可以获取吉里吉里本体的版本字符串。

版本字符串采用如下形式。

`1.0.0.1`

---

### versionInformation

属性 \ 访问: `r`

**说明**

版本信息字符串

可以获取吉里吉里本体的版本信息字符串。

版本信息字符串比 [System.versionString](System.md#versionstring) 更长，

如下所示。

`吉里吉里[きりきり] Z 実行コア/1.0.0.0 (Compiled on Dec 16 2013 23:15:27) TJS2/2.4.28 Copyright (C) 1997-2013 W.Dee and contributors All rights reserved.`

---

### eventDisabled

属性 \ 访问: `r/w`

**说明**

事件分发是否已停止

吉里吉里的**事件分发**停止时为 true。也可以设置值。

一旦事件分发停止，吉里吉里上的事件将不再发生，或者发生被推迟（根据事件类型行为有所不同）。

---

### graphicCacheLimit

属性 \ 访问: `r/w`

**说明**

图像缓存限制

以字节为单位表示吉里吉里的**图像缓存限制**。也可以设置值。

指定 `**gcsAuto**` 时，会根据机器搭载的内存容量自动设置值。

rule 图像与区域图像会消耗以 宽度×高度 表示的字节数。其他图像则消耗以 宽度×高度×4 表示的字节数。

---

### platformName

属性 \ 访问: `r`

**说明**

平台名

表示吉里吉里运行所在的平台名。在 Windows 下，OS 为 32bit 版时为 'Win32'，为 64bit 版时为 'Win64'。

在 1.3.0 及以前，始终为 'Win32'。

---

### osName

属性 \ 访问: `r`

**说明**

OS 名称

表示吉里吉里运行所在的 OS 的名称。

---

### exePath

属性 \ 访问: `r`

**说明**

吉里吉里本体所在文件夹的路径

表示吉里吉里本体所在的路径。路径名以统一存储名表示。

**相关:** [System.appDataPath](System.md#appdatapath) / [System.personalPath](System.md#personalpath)

---

### resourcePath

属性 \ 访问: `r`

**说明**

引擎内置资源所在的路径

以末尾带 `/` 的统一存储名返回 `config.cf` / `messages.json` / 随附字体（`roboto-regular.ttf` 等）这样
的引擎内置资源的存放位置。

实体因平台而异。

| 平台 | 值 | 实体 |
|---|---|---|
| WINVER / 桌面 SDL3 | `resource://./` | exe 嵌入 / OS 资源 |
| 浏览器 (wasm) | `file://./resource/` | 启动时预加载到 MEMFS |

浏览器构建中不存在 `resource://` 媒体本身，因此直接写入 `resource://...` 的
脚本会在 [Storages.isExistentStorage](Storages.md#isexistentstorage) 时点抛出“対応していないメディアタイプです”异常。参照随附字体等时
请务必前置该属性。

```tjs
// 同梱の英字フォントを参照する
var path = System.resourcePath + "roboto-regular.ttf";
```

**相关:** [System.exePath](System.md#exepath)

---

### replWebURL

属性 \ 访问: `r`

**说明**

浏览器 REPL 查看器的 URL

表示用 `-replweb` 打开的浏览器 REPL 查看器的 URL。未启动时为空字符串。

---

### personalPath

属性 \ 访问: `r`

**说明**

我的文档的路径

以统一存储名（末尾带 `/`）表示用户的文档文件夹（OS 标准的“文档”文件夹本身）的路径。
它不是应用固有的子文件夹，因此写入时请在脚本侧创建子文件夹。

| OS | 返回的文件夹 |
|---|---|
| Windows | “文档”（也会解析到 OneDrive 等的重定向目标。没有则为 RoamingAppData） |
| macOS | `~/Documents/` |
| iOS / iPadOS | 应用沙盒内的 `Documents/` |
| Linux | XDG 的文档文件夹（未设置则为 `$HOME`） |
| Android | 应用专用的外部存储（没有则为内部存储） |
| Web ( wasm ) | 无专用文件夹 → [System.exePath](System.md#exepath) |

无法确定文件夹时，返回与 [System.exePath](System.md#exepath) 相同的文件夹
（脚本侧只要与 exePath 相等，就可以视为“没有别处的存放位置”）。

!!! note "2026-10 以前的 SDL3 / 通用构建"
    在 Windows 以外始终返回 exePath。

**相关:** [System.appDataPath](System.md#appdatapath) / [System.dataPath](System.md#datapath) / [System.exePath](System.md#exepath)

---

### appDataPath

属性 \ 访问: `r`

**说明**

用户应用程序数据文件夹的路径

以统一存储名（末尾带 `/`）表示放置应用程序数据的 OS 标准文件夹（不是应用固有的子文件夹，
而是其基点）的路径。该文件夹通常是隐藏文件夹。写入时请在脚本侧创建组织名、应用名等
子文件夹。

| OS | 返回的文件夹 |
|---|---|
| Windows | RoamingAppData（通常为 `C:\Users\<ユーザ名>\AppData\Roaming`） |
| macOS | `~/Library/Application Support/` |
| iOS / iPadOS | 应用沙盒内的 `Library/Application Support/`（没有则创建） |
| Linux | `$XDG_DATA_HOME`（未设置则为 `~/.local/share/`） |
| Android | 应用的内部存储 |
| Web ( wasm ) | 无专用文件夹 → [System.exePath](System.md#exepath) |

无法确定文件夹时，返回与 [System.exePath](System.md#exepath) 相同的文件夹。

!!! note "2026-10 以前的 SDL3 / 通用构建"
    在 Windows 以外始终返回 exePath。另外，2026-08-25 之前的
    SDL3 / 通用构建连这个属性本身都没有，因此要兼容旧引擎的
    脚本请用 `typeof System.appDataPath` 确认其存在。
    存档数据等的保存位置使用 [System.dataPath](System.md#datapath) 才是安全的。

**相关:** [System.dataPath](System.md#datapath) / [System.exePath](System.md#exepath) / [System.personalPath](System.md#personalpath)

---

### dataPath

属性 \ 访问: `r`

**说明**

数据保存位置的路径

表示通过命令行选项的 -datapath 指定的目录。

默认情况下，日志等全部输出到这里。

用户脚本保存数据时，推荐保存到这里。

未指定 -datapath 时的默认值，在 Windows 下是可执行文件旁边的
`savedata`，**Linux 版则是 `~/.local/share/<orgname>/<appname>/`**（从 2026-10 起。
以前 Linux 也是可执行文件旁边）。组织名、应用程序名由
-orgname / -appname（在发布物中写在 `<exe名>.cf` 中）决定。
Linux 版的值也是本地路径，因此可以使用 `Storages.getLocalName()`。

**存在于所有构建中，并指向应用固有的保存位置**，因此获取保存位置使用
该属性才是安全的（[System.appDataPath](System.md#appdatapath) /
[System.personalPath](System.md#personalpath) 是 OS 标准文件夹本身，
在旧的 SDL3 / 通用构建中会返回 exePath，或者连属性本身都没有）。

**相关:** [System.appDataPath](System.md#appdatapath)

---

### exeName

属性 \ 访问: `r`

**说明**

吉里吉里本体的路径

表示指向吉里吉里本体的路径名。路径名以统一存储名表示。

---

### title

属性 \ 访问: `r/w`

**说明**

标题

以字符串表示主窗口的标题。也可以设置值。

**相关:** [Window.caption](Window.md#caption)

---

### screenWidth

属性 \ 访问: `r`

**说明**

屏幕宽度

以像素为单位表示屏幕尺寸（屏幕分辨率）的横向大小。

值以主窗口所在的显示器为对象。

没有主窗口时以主显示器为对象
（用 [-display](../guide/CommandLine.md) 指定了启动显示器时，
在创建主窗口之前以该显示器为对象）。

**相关:** [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### screenHeight

属性 \ 访问: `r`

**说明**

屏幕高度

以像素为单位表示屏幕尺寸（屏幕分辨率）的纵向大小。

值以主窗口所在的显示器为对象。

没有主窗口时以主显示器为对象
（用 [-display](../guide/CommandLine.md) 指定了启动显示器时，
在创建主窗口之前以该显示器为对象）。

**相关:** [System.screenWidth](System.md#screenwidth) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopLeft

属性 \ 访问: `r`

**说明**

桌面左端位置

以像素为单位表示桌面（可显示窗口的区域）的左端位置。

!!! warning "仅限 Windows 原生 ( WINVER ) 构建"
    `desktopLeft` / `desktopTop` / `desktopWidth` / `desktopHeight` 在
    SDL3 / 通用构建中不存在。如果只需要屏幕分辨率，请使用所有构建都
    具备的 [System.screenWidth](System.md#screenwidth) /
    [System.screenHeight](System.md#screenheight)。

值以主窗口所在的显示器为对象。

没有主窗口时以主显示器为对象
（用 [-display](../guide/CommandLine.md) 指定了启动显示器时，
在创建主窗口之前以该显示器为对象）。

**相关:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopTop

属性 \ 访问: `r`

**说明**

桌面上端位置

以像素为单位表示桌面（可显示窗口的区域）的上端位置。

值以主窗口所在的显示器为对象。

没有主窗口时以主显示器为对象
（用 [-display](../guide/CommandLine.md) 指定了启动显示器时，
在创建主窗口之前以该显示器为对象）。

**相关:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopWidth](System.md#desktopwidth) / [System.desktopHeight](System.md#desktopheight)

---

### desktopWidth

属性 \ 访问: `r`

**说明**

桌面宽度

以像素为单位表示桌面（可显示窗口的区域）的宽度。

值以主窗口所在的显示器为对象。

没有主窗口时以主显示器为对象
（用 [-display](../guide/CommandLine.md) 指定了启动显示器时，
在创建主窗口之前以该显示器为对象）。

**相关:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopHeight](System.md#desktopheight)

---

### desktopHeight

属性 \ 访问: `r`

**说明**

桌面高度

以像素为单位表示桌面（可显示窗口的区域）的高度。

值以主窗口所在的显示器为对象。

没有主窗口时以主显示器为对象
（用 [-display](../guide/CommandLine.md) 指定了启动显示器时，
在创建主窗口之前以该显示器为对象）。

**相关:** [System.screenWidth](System.md#screenwidth) / [System.screenHeight](System.md#screenheight) / [System.desktopLeft](System.md#desktopleft) / [System.desktopTop](System.md#desktoptop) / [System.desktopWidth](System.md#desktopwidth)

---

### exitOnWindowClose

属性 \ 访问: `r/w`

**说明**

主窗口关闭时是否退出

表示主窗口（最先创建的 Window 类实例）关闭时是否退出。也可以设置值。默认为真。

请注意：主窗口关闭，且没有显示其他调试相关窗口时，吉里吉里不会退出而是残留在系统中，
可能陷入无法控制的状态（有可能只能从任务管理器结束进程）。

---

### exceptionHandler

属性 \ 访问: `r/w`

**说明**

用于未被捕获的异常的处理器函数

表示处理未被捕获的异常（未被任何地方捕获而传递给吉里吉里本体的异常）的函数。

指定 null 时，采用默认行为。

默认行为是指：

- 停止异步事件的分发（把 [System.eventDisabled](System.md#eventdisabled) 设为 真）
- 开始把日志输出到文件（调用 [Debug.logAsError](Debug.md#logaserror)）
- 显示通知错误的对话框，并在脚本编辑器中指示该位置

处理器函数接受一个参数，它就是异常对象。

未指定处理器函数、处理器函数为 null、或处理器函数返回假时，执行默认行为。

处理器函数返回真时，不执行上述默认行为。

请考虑执行处理器函数期间可能发生异步事件。如果吉里吉里本体能够处理异步事件，就有可能
在执行异常处理器期间再次发生意外的异常。为避免这种情况，通常在执行处理器函数中做某种
等待处理时（吉里吉里有处理异步事件的机会时），停止异步事件的发生。

System.exceptionHandler = function (e)

{

// 当任何地方都未捕获的异常被系统侧捕获时，会调用

// 这个函数。e 是异常对象。

if(e instanceof "ConductorException")

{

// 当是 Conductor 抛出的异常时

Debug.logAsError(); // 开始把日志写入文件等操作

var event_disabled = System.eventDisabled;

System.eventDisabled = true;

// 如果在显示错误原因期间发生事件会很麻烦，

// 所以暂时停止事件的发生

System.inform(e.message);

System.eventDisabled = event_disabled;

// 把是否发生事件恢复到原来的状态

return true; // 返回 true 时本体侧不再进行异常处理

}

else

{

return false; // 返回 false 时执行通常的异常处理

}

};

**相关:** [System.eventDisabled](System.md#eventdisabled) / [Debug.logAsError](Debug.md#logaserror)

---

### onActivate

属性 \ 访问: `r/w`

**说明**

应用程序变为活动状态时

表示应用程序变为活动状态时被调用的事件函数。

指定 null 时不会调用函数。

与通常的事件处理器不同，想接收该事件时，请把要调用的函数设置到该属性。

[Window.onActivate](Window.md#onactivate) 在同一个应用程序内的各窗口变为活动状态时发生，
而该事件在主窗口变为活动状态时发生。

请注意，该事件在主窗口已经处于活动状态时也可能发生
（不能保证完全按 onActivate → onDeactivate → onActivate → …… 的顺序发生）。

**相关:** [System.onDeactivate](System.md#ondeactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### onDeactivate

属性 \ 访问: `r/w`

**说明**

应用程序变为非活动状态时

表示应用程序变为非活动状态时被调用的事件函数。

指定 null 时不会调用函数。

与通常的事件处理器不同，想接收该事件时，请把要调用的函数设置到该属性。

[Window.onDeactivate](Window.md#ondeactivate) 在同一个应用程序内的各窗口变为非活动状态时发生，
而该事件在主窗口变为非活动状态时发生。

请注意，该事件在主窗口已经处于非活动状态时也可能发生
（不能保证完全按 onActivate → onDeactivate → onActivate → …… 的顺序发生）。

**相关:** [System.onActivate](System.md#onactivate) / [Window.onActivate](Window.md#onactivate) / [Window.onDeactivate](Window.md#ondeactivate)

---

### onJoypadChange

属性 \ 访问: `r/w`

**说明**

手柄构成变更时被调用的事件

表示在手柄连接、断开等导致构成变化时被调用的事件函数。

指定 null 时不会调用函数。

与通常的事件处理器不同，想接收该事件时，请把要调用的函数设置到该属性。

---

### drawThreadNum

属性 \ 访问: `r/w`

**说明**

绘制所使用的线程数

表示吉里吉里的图层系统在绘制时使用的**线程数**。也可以设置值。

指定 `**dtnAuto**` 时，会自动分配与 OS 识别的处理器数量相同数量的线程。

通过设置多个绘制线程，有可能提升多核环境下的绘制性能，但反之也可能导致性能下降。

应用于绘制面积大的处理、Affine 系的高负载处理、运算繁重的图层合成处理等，
有可能获得良好结果。

即使设置为使用多线程，若系统判断绘制处理负载较轻、无法获得多线程化效果，
也可能不会以多线程执行。

---

### savedGamesPath

属性 \ 访问: `r`

**说明**

已保存游戏的路径 (1.1.0 及以后)

表示已保存游戏的路径。

通常如下。

C:\Users\<用户名>\Saved Games

---

### exeBits

属性 \ 访问: `r`

**说明**

吉里吉里本体是 32bit 版还是 64bit 版 (1.3.0 及以后)

以整数 32 或 64 表示可执行二进制是 32bit 版还是 64bit 版。

**相关:** [System.osBits](System.md#osbits) / [System.platformName](System.md#platformname)

---

### osBits

属性 \ 访问: `r`

**说明**

OS 是 32bit 版还是 64bit 版 (1.3.0 及以后)

以整数 32 或 64 表示 OS 是 32bit 版还是 64bit 版。

**相关:** [System.exeBits](System.md#exebits) / [System.platformName](System.md#platformname)

---

### exitOnNoWindowStartup

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

无窗口启动时的自动退出

为真时，在未创建任何窗口的情况下完成启动时自动结束引擎。
用于调试用途或批处理时的控制。

---

### isGeneric

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

是否为通用构建的判定

基于 SDL3 的跨平台构建 ( generic / SDL ) 中返回真，
Win32 原生构建 ( WINVER ) 中返回假。
只读。

**相关:** [System.isWindows](System.md#iswindows)

---

### isWindows

属性 \ 访问: `r/w`

**说明**

判定系统是否为 Windows [r]

---

### licenseText

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

许可证字符串

返回吉里吉里Z 本体内置的用于显示许可证的字符串。
用于在“吉里吉里设置”对话框等中显示。
在引擎本体条款之后，会附上随附组件的许可证列表
（与 getLicenseList 相同的内容）。需要各自的全文时请使用
getLicenseText。
只读。

---

### openGLESVersion

属性 \ 访问: `r/w`

**说明**

OpenGL ES 的版本

返回实际值乘以 100 的数，即 2.0 为 200、3.0 为 300。

---

### processorNum

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

逻辑处理器数量

返回 OS 识别到的逻辑处理器数量。
用于绘制线程数的自动决定等。只读。

---

### renderStats

属性 \ 访问: `r/w`

**类型**: `Dictionary`

**说明**

屏幕上传开销的测量值

返回把合成完毕的画面缓冲区上传到 GPU 纹理所花费的时间。
只读。返回的字典的键如下。

| 键 | 含义 |
|---|---|
| `texUploadUs` | 上传调用的累计时间 (微秒) |
| `texUploads` | 上传次数 (以脏矩形为单位) |
| `texUploadBytes` | 上传的累计字节数 |
| `frames` | 绘制合成帧的次数 (与有无上传无关) |

全部是累计值，因此**读取两次并取差值，与实际经过时间的比值**用于
查看“每秒上传花费了多少毫秒”。
可以用 `System.renderStatsReset()` 重置为 0。

在没有画面变化的帧中不会进行上传本身，因此静止期间
`texUploads` 不会增加（`frames` 会增加）。反之，明明静止但
`texUploadBytes` 每帧增加一个画面大小的情况下，说明某处发出了
全面更新。

上传有时会因驱动的缘故而阻塞 (例如 GPU 仍在引用目标纹理时等)，
该等待也包含在这个时间里。
不同绘制设备的上传方法不同 (OpenGL = glTexSubImage2D /
SDLDrawDevice = SDL_UpdateTexture / Windows 原生 =
UpdateSubresource)，因此用作实机上是否出现瓶颈的初步指标。

无需构建选项，始终会被测量 (每帧仅数次
计数器累加)。覆盖层对话框一侧的明细请参照
`ElementsDialog.renderStats`。

!!! tip "数值的解读方法"
    即使上传率 ( 上传时间 / 实际经过时间 ) 很高，**只要 fps 还在，
    等待的大部分就是 vsync 同步的部分** ( 驱动在上传调用中
    等待下一帧 )。如果上传真的拖了后腿，fps 会
    下降。这个判定基准、各路径的差异、测量的推进方法都
    汇总在核心演示 `perf_stats` 和引擎附带文档
    `src/core/doc/ScreenTransfer.md` 中。

**相关:** [System.renderStatsReset](System.md#renderstatsreset)

---

### texUploadUsePBO

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

强制指定纹理上传是否使用 PBO

为了测量、比较，强制指定把画面缓冲区上传到 GPU 纹理的路径。
可设置的值如下。

| 值 | 含义 |
|---|---|
| `void` (默认) | 按各用途的默认 (主画面 = 根据上传大小自动判定 / 覆盖层 = 直接上传) |
| `true` | 始终经由 PBO 上传 |
| `false` | 始终用 `glTexSubImage2D` 直接上传 |

默认情况下，上传字节数为 256KB 及以上时选择 PBO，低于此值时选择直接上传。
这是因为在大量更新小矩形的画面中，PBO 的固定成本会起作用而变得
不利。另外，在 ANGLE 实现 (Windows 的 GLES → D3D11
模拟) 中，无论大小始终为直接上传。

A/B 比较请并用 `System.renderStatsReset()` 和 `System.renderStats`。
用环境变量 `KRKRZ_GLTEXUP=pbo|direct` 也可以进行相同的指定，
但在无法传递环境变量的环境中使用这里的方法。

仅在启用了 OpenGL 绘制的构建中存在 (默认启用)。

**相关:** [System.renderStats](System.md#renderstats)

---

### touchDevice

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

触摸设备的可用性

运行环境中存在触摸输入设备时返回真。
只读。

---

### platformTag

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

平台标签

表示正在运行的平台的短标识符 ( `"windows"` / `"android"` /
`"macos"` / `"linux"` / `"web"` 等 )。只读。

[System.platformName](System.md#platformname) 是从 OS 获得的原始字符串，
包含空白和表记差异，因此难以用于文件名或条件分支；相比之下，
这个是**被规范化为小写、无空格**的，可以直接用于机型分支。

在有多个标签适用的环境 ( 不同世代的游戏机等 ) 中，会返回**最具体的那个**。

!!! info "按机型的引擎设置 `config_<tag>.cf`"
    资源内的设置文件除了共通的 `config.cf` 之外，
    放置 `config_<タグ>.cf` 即可按机型覆盖。
    读取按“具体的标签 → 一般的标签 → 共通 `config.cf`”的顺序进行，
    先读取的优先。不存在的文件会被直接跳过。

**相关:** [System.platformName](System.md#platformname) / [System.osName](System.md#osname)

---

### systemLanguage

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

本体的显示语言

以 [BCP-47](https://www.rfc-editor.org/info/bcp47) 的语言标签返回在
OS ( 家用游戏机则为硬件 ) 中设置的显示语言。
只读。值为 `"ja-JP"` / `"en-US"` / `"zh-Hant"` / `"zh-Hans"` 之类。

这是让游戏的**默认**语言跟随硬件设置的入口。语言的选择与
保存是游戏侧的职责，该属性只返回“本体设定为何种语言”。
不需要地区时请查看 `-` 之前的部分。

```tjs
var lang = System.systemLanguage;
var code = lang.indexOf("-") >= 0 ? lang.substring(0, lang.indexOf("-")) : lang;
if(code == "") code = "ja";   // 取得できない環境はゲーム既定へ
```

!!! warning "无法获取的环境返回空字符串"
    在没有获取语言手段的环境中返回空字符串。
    请由调用方回退到游戏的默认语言。

获取来源因环境而异 ( Windows 原生版 =
`GetUserDefaultLocaleName` / SDL3 版 = `SDL_GetPreferredLocales` 的开头。
家用游戏机为各硬件的 API )。在 SDL3 版中无法获取地区时，
只返回语言，如 `"ja"`。

引擎自身的消息 ( 错误文案等 ) 和选项说明的语言选择
( ja / en / chs / cht ) 也跟随该值。可以用启动选项 `-language`
显式指定来覆盖 ( [命令行选项](../guide/CommandLine.md) )。

**相关:** [System.platformTag](System.md#platformtag)

---

### padButtonMapping

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

手柄的按钮分配方式

表示手柄的物理按键如何分配到 `VK_PAD1`~`VK_PAD4` 的
字符串。也可以设置值。

- `"label"` ( 默认 ) … 按**按钮的标识**分配。`VK_PAD1` = 标识 A
  ( PlayStation 上为 ✕ )、`VK_PAD2` = B ( ○ )、`VK_PAD3` = X ( □ )、
  `VK_PAD4` = Y ( △ )。即使像任天堂系那样 A/B、X/Y 的**位置互换了**
  的手柄，画面显示与实际按下的按钮也能一致。
- `"position"` … 照旧按**位置**分配 ( 下 = `VK_PAD1`、
  右 = `VK_PAD2`、左 = `VK_PAD3`、上 = `VK_PAD4` )。

无法判定标识的手柄会自动回退到以位置为基准。
PlayStation / Xbox 系无论哪种方式结果都相同。

也可以用启动选项 `-padbuttons=label|position` ( `config.cf` 中亦可 ) 指定。
代入 `"label"` / `"position"` 以外的值会抛出异常。

!!! warning "仅限 SDL3 / 通用构建"
    该属性仅存在于 SDL3 / 通用构建。Windows 原生
    ( WINVER ) 构建的手柄输入基于 XInput，按钮的标识
    固定为 Xbox 系，因此位置与标识不会出现不一致。

**相关:** [System.getJoypadType](System.md#getjoypadtype)

---

### padStyle

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

所连接手柄的按钮标注系列 ( 只读 )

表示“最后操作的手柄”的按钮标注系列的字符串。
为 `"xbox"` / `"ps"` / `"switch"` 之一，无法判定时
为空字符串。

可用于判断画面上显示的按钮图 ( 操作提示等 ) 采用哪个系列。
对 [ElementsDialog.setPadTheme](ElementsDialog.md#setpadtheme) 指定 `"auto"` 时的
自动选择也参照与该属性相同的判定。

**相关:** [System.padButtonMapping](System.md#padbuttonmapping) / [System.getJoypadType](System.md#getjoypadtype)

---

### buildVariantName

属性 \ 访问: `r`

**类型**: `String`

**说明**

构建变体名

返回正在运行的引擎构建的**变体名**。

- `WIN` ... Win32 原生构建 ( WINVER )
- `SDL` ... 基于 SDL3 的通用构建 ( generic / SDL )
- `LIB` ... 静态库形式 ( libkrkrz )

只读。在需要比 `System.isGeneric` 更具体的变体识别
时使用。

**相关:** [System.isGeneric](System.md#isgeneric) / [System.platformName](System.md#platformname)

---

### padAxisLeftX

属性 \ 访问: `r`

**类型**: `Integer`

**说明**

手柄轴 ID: 左摇杆 X 轴

指定给 [System.getPadAxis](System.md#getpadaxis) 的 axisId 参数的常量。
只读。

---

### padAxisLeftY

属性 \ 访问: `r`

**类型**: `Integer`

**说明**

手柄轴 ID: 左摇杆 Y 轴

---

### padAxisRightX

属性 \ 访问: `r`

**类型**: `Integer`

**说明**

手柄轴 ID: 右摇杆 X 轴

---

### padAxisRightY

属性 \ 访问: `r`

**类型**: `Integer`

**说明**

手柄轴 ID: 右摇杆 Y 轴

---

### padAxisLeftTrigger

属性 \ 访问: `r`

**类型**: `Integer`

**说明**

手柄轴 ID: L 扳机

---

### padAxisRightTrigger

属性 \ 访问: `r`

**类型**: `Integer`

**说明**

手柄轴 ID: R 扳机

---

### padEnabled

属性 \ 访问: `r/w`

**类型**: `Boolean ( 真 = 启用 / 假 = 禁用。默认为启用 )`

**说明**

手柄功能的启用/禁用

代入假会完全禁用游戏手柄功能 ( 状态获取、按键事件
生成都不再进行 )。代入真可重新启用。运行时随时
可以切换。

可用于应对其他设备被误识别为手柄而误动作之类的
情况 ( 设置画面中的禁用选项等 )。用命令行
选项 `-joypad=no` 也可以从启动时起禁用，但用该属性
显式设置时以属性为准。

---

### replActive

属性 \ 访问: `r`

**类型**: `Boolean`

**说明**

是否由 REPL 驱动

REPL ( `-repl` / `-replfile` / `-replweb` ) 有效时为真。只读。
用于判定是否只在被 agent 驱动期间改变处理 ( 例如用
[System.choice](System.md#choice) 的模态响应通道代替确认对话框等 )。
不包含 REPL 的构建 ( MASTER 等 ) 中始终为假。

在 WINVER 构建中，REPL 在启动脚本之后才有效，因此在 `startup.tjs` 执行期间
仍为假。想在启动后立即判定时，请并用 `System.getArgument("-replfile")` 等。

---

### terminate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `code` | `0` | 指定进程的退出代码 |

**说明**

吉里吉里的异步退出

使吉里吉里**退出**。

即使调用该方法，吉里吉里也不会立即退出。

会在所有事件处理器把控制权交还给吉里吉里时退出。

---

### exit

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `code` | `0` | 指定进程的退出代码 |

**说明**

吉里吉里的同步退出

使吉里吉里**退出**。

该方法与 [System.terminate](System.md#terminate) 不同，在调用的时点就退出。因此，
该方法不会返回。

---

### addContinuousHandler

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | 指定作为处理器的函数。 |

**说明**

添加 Continuous 处理器

注册 **Continuous 处理器**。

Continuous 处理器是“尽可能频繁地”被调用的事件处理器。

没有其他要处理的处理时，吉里吉里会持续调用 Continuous 处理器。
发生其他事件等时，优先处理那些。

不过，用命令行选项的 -contfreq 指定了调用频率时则遵循它。

---

### removeContinuousHandler

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | 指定处理函数。 |

**说明**

删除 Continuous 处理器

删除 **Continuous 处理器**。

---

### inform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要显示的消息。 |
| `caption` | `""` | 指定作为窗口标题的字符串。 |

**说明**

消息的显示

显示用于向用户提示消息的窗口。

窗口以模态方式显示 ( 也就是说，显示期间无法操作其他窗口 )。

---

### confirm

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要显示的消息。 |
| `caption` | `""` | 指定作为窗口标题的字符串。 |
| `window` | `void` | 指定作为父窗口的窗口 ( 可省略 )。仅在 WINVER 构建中<br>父窗口指定会生效。 |

**返回值**

用户选择“是”时返回真，选择“否”或关闭对话框时
返回假。

**说明**

确认消息的显示 ( Yes / No )

显示用于询问用户“是 / 否”的模态窗口
( [System.inform](System.md#inform) 的 Yes/No 版 )。显示期间无法
操作其他窗口。
在由 REPL 的文件通道 ( `-replfile` ) 驱动期间不显示阻塞式对话框，
而是通过模态响应通道接收 agent 的回答
( `yes` / `y` / `1` / `true` / `ok` 为真 )。

**相关:** [System.choice](System.md#choice)

---

### inputString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `caption` | `&nbsp;` | 指定对话框的标题。 |
| `prompt` | `""` | 指定提示输入的说明文字 ( 省略时使用 caption )。 |
| `default` | `""` | 指定输入框的初始值 ( 可省略 )。 |

**返回值**

返回用户输入的字符串。**取消时返回 void**。

**说明**

字符串的输入

显示让用户输入 1 行文本的模态对话框
( 吉里吉里2 兼容 )。
WINVER 构建显示原生的输入对话框，SDL 构建显示
基于 Elements 的输入对话框。根据平台不同，有时会替换为 OS 的
软键盘等 ( 不支持的环境中返回 void )。
REPL 驱动期间不弹出阻塞式对话框，而是经由 REPL 的响应通道
接收输入 ( 没有响应口时返回 default )。

---

### choice

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `caption` | `&nbsp;` | 指定对话框的标题。 |
| `text` | `&nbsp;` | 指定正文。 |
| `choices` | `&nbsp;` | 指定按钮文本的数组 ( 1 个以上。空数组会抛出异常 )。 |
| `default` | `0` | 指定默认按钮的编号 ( 超出范围时为 0 )。 |

**返回值**

返回所选按钮的编号 ( choices 的下标 )。

**说明**

从选项中选择 1 个

显示排列着选项按钮的模态对话框，返回所选按钮的编号
( 用于“保存 / 不保存 / 取消”这样的 3 选等、
[System.confirm](System.md#confirm) 的 2 选无法表达的问询 )。
```tjs
var r = System.choice("確認", "変更を保存しますか?", ["保存", "保存しない", "キャンセル"], 2);
if(r == 0) save(); else if(r == 2) return;
```
WINVER 构建用 TaskDialog、SDL3 系构建用 Elements 的对话框 ( 无法使用时用 OS 的
消息框 ) 显示。焦点会放在默认按钮上，用 Esc 或关闭按钮
关闭时也返回默认编号。

在由 REPL 的文件通道 ( `-replfile` ) 驱动期间不弹出对话框，而是向模态响应通道输出
`{"type":"choice","caption":…,"text":…,"choices":[…],"default":n}` 并
等待 agent 的回答。回答为所选元素的字符串 ( 不区分大小写 ) 或编号，
为空或不符的值时采用默认编号。

**相关:** [System.confirm](System.md#confirm) / [System.replActive](System.md#replactive)

---

### getTickCount

方法

**返回值**

返回滴答计数 (64bit 的整数)。

**说明**

滴答计数的获取

**滴答计数**是每 1/1000 秒递增计数的数值。在两个时点用该方法
获取滴答计数并取其差值，就可以知道两个时点的时间差。

---

### getKeyState

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `code` | `&nbsp;` | 指定要获取状态的**虚拟键码**。 |

**返回值**

按键被按下时为真，未被按下时为假。

**说明**

按键状态的获取

获取与 code 指定的键码对应的按键在调用该方法的时点是否被按下。

---

### registerHotKey

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 虚拟键码 ( `VK_RETURN` / `VK_ESCAPE` / `VK_F1` 等 )。 |
| `mods` | `&nbsp;` | `ssShift` / `ssAlt` / `ssCtrl` 的组合。仅按这 3 位进行匹配，<br>忽略 NumLock / CapsLock 等状态。 |
| `callback` | `&nbsp;` | 按下时调用的函数。以 `callback(key, shift)` 的形式调用，<br>**返回 false ( 或 0 ) 时不消费**，流向通常的 dispatch<br>( 包含 void 在内的其他返回值则消费 )。 |

**说明**

最上位热键的注册

在事件泵入口处匹配按键，**先于获得焦点的图层 / 文本输入 /
[ElementsDialog](ElementsDialog.md) ( 含模态 )** 同步调用 callback。

这是为了在一处处理像 Alt+Enter 的全屏切换、Esc 的退出确认这类
“无论画面是什么都希望生效”的按键的机制。

对相同 key + mods 的重新注册会替换原有注册。注册表为进程共享
( 并非以 Window 为单位 )，在引擎退出时释放。

```tjs
// Esc は終了確認。ただしモーダルダイアログ表示中は素通しする
System.registerHotKey(VK_ESCAPE, 0, function(key, shift) {
if(ElementsDialog.modalActive) return false;   // 消費せず通常の dispatch へ
askQuit();
return true;
});
```

按住不放的重复不会让回调再次触发 ( 只会被消费 )，
up 仅按 key 匹配，消费了对应 down 的按键必定消费
( 即使先松开修饰键，另一半也不会漏到输入图层 )。即使回调
抛出异常，事件泵也不会损坏，会记录到日志并继续。

在 WINVER ( Windows 原生 ) 构建与 SDL3 系构建双方均可工作。

想在把焦点交给对话框的同时只让特定按键由宿主侧接收时，请使用
用途不同的 [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey) ( 不交给对话框
而是直接放行到通常的游戏输入路径。模态期间无效 )。

**相关:** [System.unregisterHotKey](System.md#unregisterhotkey) / [ElementsDialog.modalActive](ElementsDialog.md#modalactive)

---

### unregisterHotKey

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 注册时指定的虚拟键码。 |
| `mods` | `&nbsp;` | 注册时指定的修饰键的组合。 |

**返回值**

是否成功解除 ( 没有注册时为假 )。

**说明**

解除最上位热键

解除通过 [registerHotKey](#registerhotkey) 注册的热键。

**相关:** [System.registerHotKey](System.md#registerhotkey)

---

### shellExecute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 指定要执行的文件或软件。<br>指定文件时，会启动与其相关联的程序。 |
| `param` | `""` | 指定传给要执行的软件的参数。<br>target 参数指定为文件时请省略该参数，或者指定空字符串。<br>**平台差异**<br>Windows 原生版使用 ShellExecute，SDL 版使用 SDL_OpenURL，<br>以 OS 的默认处理器打开 target ( 支持 URL 和文件的打开 )。<br>SDL 版中 param ( 参数 ) 会被忽略 ( 不支持带参数的程序执行 )。 |

**返回值**

执行成功时返回真，失败时返回假。

**说明**

文件/程序的执行

**执行** target 指定的文件或软件。

---

### readRegValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 指定要读取的注册表项。 |

**返回值**

执行成功时返回注册表的值，失败时返回 void。

**说明**

注册表的读取

读取 key 指定的 Windows 注册表。

注册表项可以以下列根键名开头。

`HKEY_CLASSES_ROOT
HKEY_CURRENT_CONFIG
HKEY_CURRENT_USER

HKEY_LOCAL_MACHINE
HKEY_USERS
HKEY_PERFORMANCE_DATA

HKEY_DYN_DATA
`
例如，可以像下面这样的字符串指定给 key。

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\hoeg\installdir`

只能读取数值和单一字符串。数值时返回整数类型、字符串时返回字符串类型
的结果。

---

### getArgument

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定要获取的命令行选项名。请在最前面加上 '-'<br>( 连字符 ) ( 例 : `'-nosplash'` )。 |

**返回值**

指定了该命令行选项时返回其值，未指定时
返回 void。

**说明**

命令行选项的获取

**命令行选项**必须以下列形式

`-name=value`

或者

`-name`

的形式传递给吉里吉里。前者时作为值返回 `value`，前者时作为值
返回 `'yes'`。

**相关:** [System.setArgument](System.md#setargument)

---

### setArgument

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定要设置的命令行选项名。请在最前面加上 '-'<br>( 连字符 ) ( 例 : `'-contfreq'` )。 |
| `value` | `&nbsp;` | 指定要设置的值。 ( 例 : `'60'` )。 |

**说明**

命令行选项的设置

动态设置**命令行选项**。并非所有命令行选项都可以设置。

关于可设置的命令行选项，请参照[命令行选项](../guide/CommandLine.md)。对于这里没有标注为可动态更改的选项，请不要进行更改。

该方法不检查该选项是否可动态更改、选项是否存在、值的有效性等。设置值时请十分小心。

**相关:** [System.getArgument](System.md#getargument)

---

### toActualColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 指定颜色常量 ( 参照[颜色常量](../guide/ColorCodes.md) )。<br>指定通常的 0xRRGGBB 形式的颜色时，原样返回该值。 |

**返回值**

以 0xRRGGBB 形式返回指定颜色常量所表示的实际颜色。

**说明**

颜色常量的实际颜色的获取

把颜色常量转换为实际颜色，以 0xRRGGBB 形式返回。

---

### createAppLock

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 指定用于检查的键字符串。如果其他正在<br>运行的吉里吉里把相同的键字符串指定给了该方法，则返回 false。<br>键字符串基本上请认为只能使用与 TJS 变量的命名规则相同的字符。<br>键字符串必须足够唯一。<br>WINVER 构建通过命名 Mutex、SDL3 系构建通过以 OS 的互斥锁抓住<br>临时区域的锁文件的形式实现。两者在进程退出时<br>( 即使是异常退出 ) 都会被释放。 |

**返回值**

已经存在指定了相同键字符串的吉里吉里正在运行时为 false，否则返回 true。

**说明**

重复启动的检查

如果有其他指定了相同键字符串的吉里吉里正在运行则为 false，否则返回 true。

用于防止重复启动。

---

### createUUID

方法

**返回值**

以 "e8b2a2b5-5ceb-4f75-a08b-1f1bdfdca4f1" 的形式返回生成的 UUID 字符串
(除连字符外的各英数字为 16 进制数字)。

**说明**

UUID 字符串的生成

生成并返回 UUID 字符串。该方法基于随机位串生成
128bit 的 UUID (universal unique identifier)。

吉里吉里中实现的 UUID 生成算法会在一定程度上拾取
环境噪声来生成随机位串，但不建议用于要求
高安全性的用途。不过，
可以认为与其他 UUID“以非常非常高的概率不重复”。

---

### assignMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 指定要分配的消息 ID。 |
| `msg` | `&nbsp;` | 指定分配给 id 所指定 ID 的消息。 |

**返回值**

ID 存在且消息分配成功时为真，否则返回假。

**说明**

消息分配的更改

更改消息分配。

可以用该方法把吉里吉里内置的消息更改为其他消息。

通常记述在消息映射文件内 ( 参照[启动](../guide/Startup.md) )。

要获取可设置的 ID 及当前分配给它们的消息列表，请从 [Controller](Controller.md)
执行“消息映射文件的创建”。

---

### doCompact

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `level` | `clAll` | 指定级别。<br>指定 **clIdle** 时，执行在系统空闲状态 (系统比较不工作的状态) 下进行的压缩整理相同的处理。当前版本中执行 TJS2 的垃圾回收。<br>指定 **clDeactivate** 时，执行吉里吉里变为非活动 (其他应用程序变为活动) 时进行的压缩整理相同的处理。当前版本中会清除图层运算用的临时图像缓冲区、图层缓存、XP3 归档的分段(存储片段) 缓存、自动搜索路径的缓存。<br>指定 **clMinimize** 时，执行吉里吉里被最小化时进行的压缩整理相同的处理。当前版本中会清除绘制文字的缓存、图像缓存。<br>指定 **clAll** 时，执行上述所有压缩整理。<br>压缩整理的级别按 clIdle < clDeactivate < clMinimize < clAll 的顺序变强。指定更上级的级别时，下位级别进行的压缩整理也会执行。例如，执行 clDeactivate 时，clIdle 的处理也会执行。<br>省略参数时，视为指定了 clAll。 |

**说明**

内存的压缩整理

进行内存的压缩整理。压缩整理是指释放未使用的内存和各种缓存用内存，减少内存使用量的处理。

吉里吉里会自动进行该处理，因此通常不必太在意，但想在程序侧的处理中强制进行时可以使用该方法。

---

### touchImages

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storages` | `&nbsp;` | 以数组(Array 类的对象)传递想要放入缓存的图像存储名。<br>写在越前面的越优先。<br>吉里吉里把指定给 [Layer.loadImages](Layer.md#loadimages) 第 1 个参数的<br>字符串直接作为键来管理缓存，<br>因此要使缓存有意义，<br>这里指定的图像存储名必须与指定给 Layer.loadImages 第 1 个参数的<br>名称相同。 |
| `limitbytes` | `0` | 以字节为单位指定本次方法调用所使用的缓存容量限制值。<br>指定 0 时，使用全部缓存。<br>指定正数时，会尝试将缓存使用到该字节数。<br>指定负数时，把当前缓存的<br>限制值 ( [System.graphicCacheLimit](System.md#graphiccachelimit) ) 加上该数值所得的数 ( 不过<br>由于加的是“负数”，实际是减去 ) 作为限制值使用。如果结果限制值<br>变为 0 或负数，则该方法什么都不做就结束。例如，<br>指定 -2*1024*1024 时，被视为从当前缓存限制值中减去 2MB 所得数值<br>作为指定值。这在想给缓存剩余容量留出富余时很方便。 |
| `timeout` | `0` | 以 ms 为单位指定超时 ( 时间限制 )。指定 0 时<br>为无限制。<br>该方法在经过该参数指定的时间后，中止此后的图像读取并<br>返回。不过，即使在某张图像的读取中发生超时，在该图像的读<br>取结束之前也不会返回。 |

**说明**

图像读入缓存

该方法尝试把指定的图像放入缓存。不过，该方法虽然会努力把图像放入缓存，
但并不保证图像实际会进入缓存。超出图像缓存的限制值或超时时，会中止图像读取。
在 storages 参数指定的图像中，写在越前面的越有可能进入缓存
( 越优先 )。如果指定的图像已经进入缓存，则只执行把它在缓存中的
生存顺位提高的动作。

该方法忽略图像读取中的所有错误。

在当前版本中，能用该方法放入缓存的图像，通常是可以
由 [Layer.loadImages](Layer.md#loadimages) 读取、且未指定颜色键的图像
( 带 Alpha 通道的图像没有问题 )。通用转场的 rule 图像和
区域图像虽然也会执行读取动作，但不会成为作为缓存有效的数据 ( 读取的
数据会被浪费 )，因此请不要指定。

关于图像在缓存中使用的字节数，请参照 [System.graphicCacheLimit](System.md#graphiccachelimit)。

---

### showVersion

方法

**说明**

about 对话框的显示 (1.1.0 及以后)

显示 about 对话框。

---

### dumpHeap

方法

**说明**

堆信息转储 (1.1.0 及以后)

把堆的信息输出到控制台。

---

### captureScreen

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 保存目标的统一存储路径 (.png) |
| `x` | `0` | = 0 保存范围的左端 |
| `y` | `0` | = 0 保存范围的上端 |
| `w` | `0` | = 0 保存范围的宽度 (0 为整个画面) |
| `h` | `0` | = 0 保存范围的高度 (0 为整个画面) |

**说明**

把实际画面保存为 PNG

在下一帧 present 之前，发出把包含覆盖层的实际画面读回并 PNG 保存到 path 的
请求 (实际保存是在 DrawDevice 绘制时)。可以用 x,y,w,h 指定保存范围，
w/h 为 0 时表示整个画面。这与 SDL 的 `Agent.captureScreen` 等效，是为了在
不支持 Agent 的 WINVER 上也能使用而在 REPL 有效时准备的测试/验证用功能。
返回值是保存目标路径。

---

### renderStatsReset

方法

**说明**

重置屏幕上传开销的测量值

把 `System.renderStats` 的累计计数器重置为 0。
作为测量区间的起点调用。

**相关:** [System.renderStats](System.md#renderstats)

---

### addFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要添加的字体文件的存储名。 |

**返回值**

返回所添加字体提供的 face 名的数组。

**说明**

字体的添加

把存储内的字体文件添加到引擎。
添加的字体可以从图层或字体绘制 API 通过 face 名引用。

**相关:** [Font](Font.md)

---

### clearGraphicCache

方法

**说明**

图形缓存的销毁

销毁 `Layer.loadImages` 等使用的内部图形缓存。
在想要急剧减少内存使用量，或强制进行图像替换后的重新读取时调用。

---

### getJoypadType

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `0` | 指定手柄编号 ( 默认值 0 )。**0 是指向“最后操作的<br>手柄”的特别编号**，1 以上指向按连接顺序的实际手柄 ( 第 1 个, 第 2 个, … )。<br>手柄相关 API 和按键事件 ( VK_PAD* ) 都遵循该<br>编号体系，按键事件始终以 0 号 ( = 最后操作的手柄 ) 为<br>发生源。连接台数可以用 `System.getJoypadCount()` 获取。 |

**返回值**

返回表示手柄机型名的字符串。指定编号的手柄
不存在时返回空字符串。

**说明**

获取所连接手柄的种类 ( 机型名 )

以机型名的“字符串”返回指定编号的手柄的种类
( 不是数值的种类 ID )。字符串依赖环境，SDL 构建中为
SDL 识别的机型名 ( 例: "Xbox Series X Controller" )、WINVER 构建中为
源自 XInput 的通用名 ( "XInput Controller" )。

---

### nullpo

方法

**说明**

引发空指针访问

请不要调用。

---

### system

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `command` | `&nbsp;` | 指定要执行的命令字符串。 |

**返回值**

原样返回 `_wsystem()` 的返回值。

**说明**

shell 命令的执行

以相当于 OS 的 `system(3)` 的方式同步执行 shell 命令。仅限 Win32 构建。
执行后立即发出 `TVP_COMPACT_LEVEL_MAX` 级别的压缩整理事件，
所有缓存都会被销毁。

---

### getSystemAllocatorInfo

方法

**返回值**

返回包含上述键的字典。

**说明**

平台分配器信息的获取

一次性获取进程和系统的内存状态。未能获取值的项目，
键本身不存在于字典中，因此可以用 `"xxx" in dict` 判定。

返回的字典的键 (根据环境可能缺少一部分):

- `totalFreeSize`        : 堆整体的空闲容量 ( 字节 )
- `allocatableSize`      : 可确保的最大连续区域 ( 字节 )
- `usedSize`             : 当前的使用量 ( 字节 )
- `peakUsedSize`         : 启动以来的使用量峰值 ( 字节 )
- `totalSize`            : 堆的总容量 ( 字节 )
- `processRss`           : 进程 RSS ( 字节 )
- `processPeakRss`       : 进程 peak RSS ( 字节 )
- `processVsize`         : 进程虚拟大小 ( 字节 )
- `systemTotalPhysical`  : 系统物理内存总量 ( 字节 )
- `systemAvailPhysical`  : 系统可用物理内存 ( 字节 )

**相关:** [System.resetMemoryPeak](System.md#resetmemorypeak)

---

### resetMemoryPeak

方法

**说明**

内存峰值测量的重置

把 File / Bitmap / Sound 分配器的 **peak_used** 重新对齐到 current_used，
并重置 Krkrz 全局分配器的峰值。
用于想把 `MemoryOverlay` 的 `(peak X.XX)` 显示变为“从这之后的最大值”
时。等同于 REPL 的 `.mempeakclear`。

---

### beginAllocTag

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定标签名。 |

**说明**

内存分配器标签作用域的开始

把 `name` push 到 thread-local 的标签栈。此后从该
线程运行的引擎侧 ( Krkrz ) 的内存分配都会按该标签
归类计量。必须用 `System.endAllocTag()` 进行对应的 pop
操作。

使用示例:

```
System.beginAllocTag("User");
loadChapter(3);
System.endAllocTag();
```

与已知的标签名 ( `TVPAllocTag` 枚举名: `TJS2` / `User` / `GraphicsLoader`
等 ) 不一致的名称会被视为 **User**。

**相关:** [System.endAllocTag](System.md#endalloctag)

---

### endAllocTag

方法

**说明**

内存分配器标签作用域的结束

取出用 [System.beginAllocTag](System.md#beginalloctag) push 的标签。

**相关:** [System.beginAllocTag](System.md#beginalloctag)

---

### setMemoryOverlay

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enable` | `&nbsp;` | 真为显示，假为隐藏。省略参数 ( 或传 void ) 时<br>切换当前状态。 |

**返回值**

设置后的状态以真 ( 1 ) 或假 ( 0 ) 返回。

**说明**

内存状态覆盖层的设置

切换是否在画面右上角实时显示引擎内存状态的覆盖层。
标志本身在所有构建中都可以切换，但
**实际绘制的是 OGL 系 DrawDevice ( `OGLDrawDevice` / `SDLOGLDrawDevice` )
和 SDL 的 `SDLDrawDevice`**。Windows 原生 ( WINVER ) 构建的
默认 `BasicDrawDevice` (D3D11) 没有绘制挂钩，因此不会显示，
不过在 WINVER 中把 `Window.drawDevice` 切换到 OGL 系也会显示。

---

### setPadOverlay

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enable` | `&nbsp;` | 真为显示，假为隐藏。省略参数 ( 或传 void ) 时<br>切换当前状态。 |

**返回值**

设置后的状态以真 ( 1 ) 或假 ( 0 ) 返回。

**说明**

手柄状态覆盖层的设置

切换是否在画面左上角显示手柄 16 个按键和 6 个轴的模拟值的覆盖层。
标志本身在所有构建中都可以切换，但
**实际绘制的是 OGL 系 DrawDevice ( `OGLDrawDevice` / `SDLOGLDrawDevice` )
和 SDL 的 `SDLDrawDevice`**。Windows 原生 ( WINVER ) 构建的
默认 `BasicDrawDevice` (D3D11) 没有绘制挂钩，因此不会显示，
不过在 WINVER 中把 `Window.drawDevice` 切换到 OGL 系也会显示
( 手柄的状态获取使用所有构建共通的逻辑层，因此在 WINVER 上也会
显示 XInput 的手柄名、按钮、轴 )。

---

### setDrawStatsLog

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enable` | `&nbsp;` | 真为输出日志，假为停止。省略参数 ( 或传 void ) 时<br>切换当前状态。 |

**返回值**

设置后的状态以真 ( 1 ) 或假 ( 0 ) 返回。

**说明**

绘制统计日志输出的设置

切换在 `KRKRZ_DRAW_STATS=ON` 构建且 MemoryOverlay 显示期间，每 500ms 把
`DrawThreadPool` 利用统计写入日志的模式。
在实机 ( Switch 等 ) 上实时显示流动太快看不清时
使用。在 OFF 构建或 MemoryOverlay 非显示时调用也没有实际
危害，但不会输出日志。

---

### getTextureMemory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tag` | `&nbsp;` | 传入字符串时，也会以该名称把使用量作为 1 行日志输出。<br>用于想在场景边界等处打标记时。省略时不输出日志。 |

**返回值**

使用量的字典

**说明**

GL 纹理内存使用量的获取

以字典返回 GL 系 DrawDevice 确保的纹理类的内存使用量。
分配器或进程使用量 ( REPL 的 `.mem` 等 ) 处理的 CPU 侧内存
不包含 GL 驱动确保的纹理，因此在这里另行测量。

返回的字典的成员如下 ( 单位为字节 )。

| 成员 | 内容 |
|---|---|
| `texture` | [Texture](Texture.md) ( GL 纹理 ) 实体的合计 |
| `pbo` | 上传用 PBO 的合计。**只有会被更新的纹理才拥有** ( 延迟分配 ) |
| `total` | `texture` + `pbo` |
| `peak` | 合计的最大值 |
| `textureCount` | 存活的纹理数量 |
| `pboCount` | 存活的 PBO 数量 |

`peak` 是包含 [Offscreen](Offscreen.md) 使用的 FBO 部分在内的合计最大值，因此
使用 FBO 时会成为比 `total` 更大的值 ( `total` 不包含 FBO )。

**仅存在于 SDL3 / LIB 构建且启用了 OpenGL 绘制的构建中**。
WINVER 构建中目前没有。

**相关:** [System.setTextureMemoryLog](System.md#settexturememorylog) / [System.resetTextureMemoryPeak](System.md#resettexturememorypeak)

---

### setTextureMemoryLog

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enable` | `&nbsp;` | 真为输出日志，假为停止。省略参数 ( 或传 void ) 时<br>切换当前状态。 |

**返回值**

设置后的状态以真 ( 1 ) 或假 ( 0 ) 返回。

**说明**

GL 纹理内存日志输出的设置

切换每当 GL 纹理内存的合计增减 8MiB 就把使用量写入日志的
模式。默认无效。

**仅存在于 SDL3 / LIB 构建且启用了 OpenGL 绘制的构建中**。

**相关:** [System.getTextureMemory](System.md#gettexturememory)

---

### resetTextureMemoryPeak

方法

**说明**

GL 纹理内存峰值值的重置

把 [System.getTextureMemory](System.md#gettexturememory) 返回的 `peak` 重置为当前值。
用于想测量“从这之后的最大值”时。

**仅存在于 SDL3 / LIB 构建且启用了 OpenGL 绘制的构建中**。

**相关:** [System.getTextureMemory](System.md#gettexturememory)

---

### getJoypadCount

方法

**返回值**

手柄数量 ( 整数 )。

**说明**

获取正在连接的手柄数量

返回当前识别到连接的游戏手柄的数量。

**相关:** [System.hasJoypad](System.md#hasjoypad)

---

### hasJoypad

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `0` | 指定手柄编号 ( 默认值 0 )。 |

**返回值**

已连接时为真，否则为假。

**说明**

手柄的连接确认

返回指定编号的手柄是否已连接。

**相关:** [System.getJoypadCount](System.md#getjoypadcount)

---

### getPadAxis

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 指定手柄编号 ( 0 = 最后操作的手柄、1 以上 = 按连接顺序的实际手柄 )。 |
| `axisId` | `&nbsp;` | 指定轴 ID。 |

**返回值**

以实数返回轴的模拟值。

**说明**

手柄轴模拟值的获取

返回指定手柄的指定轴的模拟值。轴 ID 请使用
`System.padAxisLeftX` 等常量。

返回值的范围:

- 摇杆轴 ( LeftX / LeftY / RightX / RightY ) ... -1.0 ~ +1.0
- 扳机轴 ( LeftTrigger / RightTrigger ) ... 0.0 ~ +1.0

未连接、无效的轴 ID 等情况下返回 0.0。

**相关:** [System.padAxisLeftX](System.md#padaxisleftx) / [System.padAxisLeftY](System.md#padaxislefty) / [System.padAxisRightX](System.md#padaxisrightx) / [System.padAxisRightY](System.md#padaxisrighty) / [System.padAxisLeftTrigger](System.md#padaxislefttrigger) / [System.padAxisRightTrigger](System.md#padaxisrighttrigger)

---

### rumblePad

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 指定手柄编号 ( 0 = 最后操作的手柄 )。 |
| `low` | `&nbsp;` | 低频马达的强度 ( 0~255 )。 |
| `high` | `&nbsp;` | 高频马达的强度 ( 0~255 )。 |
| `duration` | `&nbsp;` | 以毫秒指定驱动时间。 |

**返回值**

开始成功时为真，失败时为假。

**说明**

手柄振动的开始

驱动指定手柄的振动马达。

**相关:** [System.stopRumblePad](System.md#stoprumblepad)

---

### stopRumblePad

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `0` | 指定手柄编号 ( 默认值 0 )。 |

**返回值**

停止成功时为真，失败时为假。

**说明**

手柄振动的停止

停止用 [System.rumblePad](System.md#rumblepad) 开始的振动。

**相关:** [System.rumblePad](System.md#rumblepad)

---

### getLicenseList

方法

**返回值**

许可证信息 ( 字典 ) 的数组

**说明**

许可证列表的获取

返回把引擎与插件内置的第三方组件的许可证信息，以及
放置在项目的 `licenses/` 文件夹中的许可证文件
( `licenses/*.txt` 或 `.md` ) 汇总起来的列表。
这是为了在脚本侧自由构建游戏内的许可证显示画面
( 字体选择画面等 ) 的信息源。

各元素是字典，包含以下成员:
+ `name` : 显示名 ( 传给 `getLicenseText` )
+ `group` : 分类 ( "engine" / "font" / "font-engine" / "audio" / "video" /
"ui" / "platform" / "plugin:~" / "data" 等 )
+ `source` : 出处 ( "builtin" = 引擎本体内置 / "plugin" = 插件注册 /
"storage" = 项目的 licenses/ 文件夹 )

同名许可证存在于多个出处时会被合并为 1 条
( 插件注册 > 引擎本体内置 > storage 的优先级 )。

**相关:** [System.getLicenseText](System.md#getlicensetext)

---

### getLicenseText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 许可证名 |

**返回值**

许可证文本 ( 找不到则为 void )

**说明**

许可证文本的获取

指定 [System.getLicenseList](System.md#getlicenselist) 的 `name`，
以字符串获取许可证文本全文。找不到时返回 void。

放置在项目的 `licenses/` 文件夹中的文件 ( 追加字体的
许可证文本等 ) 也可以用相同的名称解析获取
( `licenses/<name>.txt` → 没有则为 `.md` )。

**相关:** [System.getLicenseList](System.md#getlicenselist)

---

### readEnvValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定环境变量名。 |

**返回值**

返回环境变量的值。未设置时返回 void。

**说明**

环境变量的获取

在 WINVER / SDL3 系构建双方均可使用。

**相关:** [System.writeEnvValue](System.md#writeenvvalue) / [System.expandEnvString](System.md#expandenvstring)

---

### writeEnvValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定环境变量名。 |
| `value` | `&nbsp;` | 指定要设置的值。指定空字符串会删除该环境变量。 |

**返回值**

返回设置前的值。未设置时返回 void。

**说明**

环境变量的设置

设置只对这个进程 ( 以及从此处启动的子进程 ) 有效。

**相关:** [System.readEnvValue](System.md#readenvvalue)

---

### expandEnvString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要展开的字符串。 |

**返回值**

返回展开后的字符串。

**说明**

环境变量的展开

把字符串中的 `%NAME%` 替换为环境变量的值。
没有对应环境变量的 `%NAME%` 原样保留，`%%` 变为 `%` 1 个
( 与 Win32 的 ExpandEnvironmentStrings 相同的规则 )。

**相关:** [System.readEnvValue](System.md#readenvvalue)

---

### urlencode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 指定要转换的字符串。 |
| `utf8` | `true` | 为真 ( 默认 ) 时作为 UTF-8 的字节序列、为假时作为系统的<br>多字节字符串进行转换。 |

**返回值**

返回转换后的字符串。

**说明**

URL 编码

把 RFC 3986 的非保留字符 ( 英数字与 `-` `_` `.` `~` ) 以外的字符转换为 `%XX`。
空格也会变为 `%20` ( 不会变为 `+` )。
```tjs
System.urlencode("a b&c=d");   // "a%20b%26c%3Dd"
System.urlencode("あ");         // "%E3%81%82"
```

**相关:** [System.urldecode](System.md#urldecode)

---

### urldecode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 指定要转换的字符串。包含非法 `%XX` 时会抛出异常。 |
| `utf8` | `true` | 为真 ( 默认 ) 时按 UTF-8、为假时按系统的多字节字符串<br>解释。 |

**返回值**

返回转换后的字符串。

**说明**

URL 解码

把 `%XX` 还原为原来的字节并变为字符串。`+` 不会还原为空格。

**相关:** [System.urlencode](System.md#urlencode)

---

### getAboutString

方法

**返回值**

返回版本信息的字符串。

**说明**

版本信息字符串的获取

返回与用启动选项 `-about` 显示的内容相同的、引擎与随附库的
版本信息文本。

---

### breathe

方法

**说明**

消息的处理

在长时间处理的中途调用时，只处理 OS 的消息，避免窗口看起来
无响应。处理期间不会派发 TJS 的事件。

---

### getMonitorInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nearest` | `&nbsp;` | 对象没有重叠的显示器时，若想返回最近的显示器则指定真。 |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**返回值**

返回显示器信息的字典。

**说明**

显示器信息的获取

以如下形式的字典返回显示器的信息。矩形为屏幕坐标。
```tjs
%[ name:"\\.\DISPLAY1", primary:1,
monitor:%[ x:0, y:0, w:3840, h:2160 ],   // モニタ全体
work:   %[ x:0, y:0, w:3840, h:2064 ] ]  // タスクバー等を除いた作業領域
```
对象根据参数的数量而变化。

| 参数 | 对象 |
|---|---|
| 无 | 主显示器 |
| `(nearest, window)` | 该窗口所在的显示器 |
| `(nearest, x, y)` | 该点所在的显示器 |
| `(nearest, x, y, w, h)` | 与该矩形重叠的显示器 |

`nearest` 为真时返回最近的显示器，为假时在没有重叠的显示器时
返回 void。

在 WINVER / SDL3 系构建双方均可使用。没有显示器概念的环境
( 始终全屏的机型等 ) 中返回 void。

**相关:** [System.getDisplayMonitors](System.md#getdisplaymonitors)

---

### getDisplayMonitors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定矩形的左端 ( 可省略 )。 |
| `y` | `&nbsp;` | 指定矩形的上端 ( 可省略 )。 |
| `w` | `&nbsp;` | 指定矩形的宽度 ( 可省略 )。 |
| `h` | `&nbsp;` | 指定矩形的高度 ( 可省略 )。 |

**返回值**

返回显示器信息的数组。没有显示器概念的环境中为空数组。

**说明**

显示器列表的获取

以数组返回所有显示器的信息 ( 形式与 [System.getMonitorInfo](System.md#getmonitorinfo) 相同 )。
指定矩形时，只返回与该矩形重叠的显示器，并把
重叠部分放入各元素的 `intersect` ( `%[ x, y, w, h ]` )。

SDL3 系构建中显示器的排列是当时的排列。由于插拔会变化，
请不要保存下标使用。

**相关:** [System.getMonitorInfo](System.md#getmonitorinfo)

---

### getSystemMetrics

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定度量的名称。 |

**返回值**

返回值。未知名称时返回 void。

**说明**

系统度量的获取

按名称获取 Win32 的 GetSystemMetrics 的值。名称为去掉 `SM_` 的部分
( `"CXSIZEFRAME"` / `"CYCAPTION"` / `"CMONITORS"` 等。不区分大小写 )。

仅限 WINVER 构建。SDL3 系构建没有该方法。

---

## 插件扩展: process

### 成员列表

#### 方法

- [commandExecute](#commandexecute)

---

### commandExecute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 程序 |
| `param` | `&nbsp;` | 参数 |
| `timeout` | `0` | 超时时间(ms) |

**返回值**

%[
status:   ok/error/timeout 中的任一字符串,
stdout:   控制台输出字符串数组(按换行分离)
exitcode: 退出代码(仅当 status=="ok" 时),
message:  错误消息(仅当 status!="ok" 时)
];

**说明**

带控制台输出获取的命令行程序执行

没有后台处理。在作为执行目标的程序结束之前，吉里吉里会停止。

---

## 插件扩展: shellExecute

### 成员列表

#### 方法

- [commandExecute](#commandexecute)

---

### commandExecute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 程序 |
| `param` | `&nbsp;` | 参数 |
| `timeout` | `0` | 超时时间(ms) |

**返回值**

%[
status:   ok/error/timeout 中的任一字符串,
stdout:   控制台输出字符串数组(按换行分离)
exitcode: 退出代码(仅当 status=="ok" 时),
message:  错误消息(仅当 status!="ok" 时)
];

**说明**

带控制台输出获取的命令行程序执行

没有后台处理。在作为执行目标的程序结束之前，吉里吉里会停止。

---

## 插件扩展: stdio

System 类的标准输入输出扩展

### 成员列表

#### 属性

- [stdioState](#stdiostate)

#### 方法

- [attachConsole](#attachconsole)
- [allocConsole](#allocconsole)
- [freeConsole](#freeconsole)
- [stdin](#stdin)
- [stdout](#stdout)
- [stderr](#stderr)
- [flush](#flush)

---

### stdioState

属性 \ 访问: `r/w`

**说明**

返回与标准输入输出的连接状态

---

### attachConsole

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bind` | `0` | 0:仅连接未连接的部分 其他:强制连接指定的部分<br>标准输入:0x01 标准输出:0x02 标准错误输出:0x04 的按位或 |

**返回值**

是否成功

**说明**

把标准输入输出连接到既有控制台

---

### allocConsole

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bind` | `0` | 0:仅连接未连接的部分 其他:强制连接指定的部分<br>标准输入:0x01 标准输出:0x02 标准错误输出:0x04 的按位或 |

**返回值**

是否成功

**说明**

创建控制台并连接标准输入输出

---

### freeConsole

方法

**返回值**

是否成功

**说明**

从控制台分离

---

### stdin

方法

**返回值**

输入的文本

**说明**

从标准输入输入文本。输入会阻塞。

---

### stdout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `string` | `&nbsp;` | 要输出的消息 |

**说明**

向标准输出输出字符串

---

### stderr

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `string` | `&nbsp;` | 要输出的消息 |

**说明**

向标准错误输出输出字符串

---

### flush

方法

**说明**

刷新标准输出

---

## 插件扩展: systemEx

基于伪代码的手册

### 成员列表

#### 方法

- [writeRegValue](#writeregvalue)
- [readEnvValue](#readenvvalue)
- [writeEnvValue](#writeenvvalue)
- [expandEnvString](#expandenvstring)
- [urlencode](#urlencode)
- [urldecode](#urldecode)
- [getAboutString](#getaboutstring)
- [confirm](#confirm)
- [waitForAppLock](#waitforapplock)
- [setDpiAwareness](#setdpiawareness)
- [getOSVersion](#getosversion)
- [getKnownFolderPath](#getknownfolderpath)
- [processApplicationMessages](#processapplicationmessages)
- [handleApplicationMessage](#handleapplicationmessage)
- [setDefaultDllDirectories](#setdefaultdlldirectories)
- [addDllDirectory](#adddlldirectory)
- [removeDllDirectory](#removedlldirectory)

---

### writeRegValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 写入目标的键(readRegValue 同样指定 HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\hoeg\\installdir) |
| `value` | `&nbsp;` | 要写入的值(字符串或整数值) |

**说明**

向注册表写入数据

---

### readEnvValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 环境变量名 |

**返回值**

环境变量值（未定义时为 void）

**说明**

获取环境变量

※在引擎本体存在同名方法的环境中会使用本体版本
(本插件仅在引擎本体没有该方法的旧环境中进行补充注册)。
规格请参照本体的 [System.readEnvValue](System.md#readenvvalue)。
注册表的读取请使用内置的 System.readRegValue

---

### writeEnvValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 环境变量名 |
| `value` | `&nbsp;` | 要设置的值 |

**返回值**

原来的环境变量值（未定义时为 void）

**说明**

设置环境变量

※在引擎本体存在同名方法的环境中会使用本体版本
(本插件仅在引擎本体没有该方法的旧环境中进行补充注册)。
规格请参照本体的 [System.writeEnvValue](System.md#writeenvvalue)。

---

### expandEnvString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 要展开的字符串 |

**返回值**

展开后的字符串

**说明**

将字符串内的“%~%”用环境变量展开

※在引擎本体存在同名方法的环境中会使用本体版本
(本插件仅在引擎本体没有该方法的旧环境中进行补充注册)。
规格请参照本体的 [System.expandEnvString](System.md#expandenvstring)。

---

### urlencode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 原字符串 |
| `utf8` | `true` | 以 UTF8 输出时为 true |

**返回值**

URLEncode 后的字符串

**说明**

进行 URLEncode 处理

※在引擎本体存在同名方法的环境中会使用本体版本
(本插件仅在引擎本体没有该方法的旧环境中进行补充注册)。
规格请参照本体的 [System.urlencode](System.md#urlencode)。

---

### urldecode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 原字符串 |
| `utf8` | `true` | 作为 UTF8 处理时为 true |

**返回值**

URLDecode 后的字符串

**说明**

进行 URLDecode 处理

※在引擎本体存在同名方法的环境中会使用本体版本
(本插件仅在引擎本体没有该方法的旧环境中进行补充注册)。
规格请参照本体的 [System.urldecode](System.md#urldecode)。

---

### getAboutString

方法

**返回值**

文本(TVPGetAboutString)

**说明**

获取用 Ctrl+F12 显示的环境信息文本

※在引擎本体存在同名方法的环境中会使用本体版本
(本插件仅在引擎本体没有该方法的旧环境中进行补充注册)。
规格请参照本体的 [System.getAboutString](System.md#getaboutstring)。

---

### confirm

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 要显示的消息 |
| `caption` | `""` | 窗口的标题字符串 |
| `window` | `void` | 有指定时把该窗口作为父窗口显示 |

**返回值**

按下 YES 时为 true

**说明**

显示确认用消息窗口。窗口以模态方式显示。

※在引擎本体实现了 System.confirm 的环境中会使用本体版本
(本插件仅在引擎本体没有该方法的旧环境中进行补充注册)。

---

### waitForAppLock

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | AppLock 的键字符串 |
| `timeout` | `0` | 超时等待时间(ms) |

**返回值**

true:正常结束(AppLock 不存在，或在超时时间内消失),  false:超时, (void:错误)

※在该函数之后无需再用相同的键调用 createAppLock（因为已经拥有所有权，会失败）

**说明**

等待被其他进程的 System.createAppLock 创建的 Mutex 释放，并获取所有权

---

### setDpiAwareness

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `context` | `&nbsp;` | : 上下文值（-1~-5）<br>DPI_AWARENESS_CONTEXT_UNAWARE              : -1<br>DPI_AWARENESS_CONTEXT_SYSTEM_AWARE         : -2<br>DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE    : -3<br>DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 : -4 (Creators Update or later)<br>DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED    : -5 (October 2018 update or later) |

**返回值**

之前的值(※无法设置时为 0)

**说明**

设置 DPI Awareness

在 Windows10 Redstone1 (ver 1607) 及以后有效

---

### getOSVersion

方法

**返回值**

void or %[ major, minor, build, platform, spmajor, spminor, servevicepack, suite, type ];

**说明**

获取 OS 版本信息的详情

请参照 RtlGetVersion API 以及 RTL_OSVERSIONINFOW 结构体
(October 2018 update or later)

---

### getKnownFolderPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `folderid` | `&nbsp;` | 想要获取的 FOLDERID (String or GUID-octet) |
| `flags` | `0` | KF_FLAG_* 值（KF_FLAG_CREATE = 0x00008000 等） |

**返回值**

结果的本地路径字符串 or ""(不明) or void(失败)

**说明**

SHGetKnownFolderPath 的包装

FOLDERID 为字符串时，指定 FOLDERID_{} 的 {} 部分的字符串。GUID 时指定 <% 00000000 0000 0000 0000 0000000000000 %> 的 16byte octet
作为该函数独有的特殊指定，folderid 可以指定 "Captures"（与指定 GameBar 的捕获文件夹[Video\Captures] : GUID {EDC0FE71-98D8-4F4A-B920-C8DC133CB165} 等效的动作）

---

### processApplicationMessages

方法

**说明**

消息的处理 ( 调用本体的 TVPProcessApplicationMessages() )

与 System.breathe() 不同，吉里吉里的事件也会被处理。
注意：基本上 processApplicationMessages 在应用结束之前不会返回。

在事件处理器内发生异常时，不会从该方法传播。
插件侧只是原样传递对本体的调用，异常由本体的事件分发侧
捕获，并作为通常的未处理脚本异常处理 ( 异常对话框 / 日志
输出，如果设置了 System.exceptionHandler 则通知给它 )。

---

### handleApplicationMessage

方法

**说明**

处理 1 条消息 ( 调用本体的 TVPHandleApplicationMessage() )

异常的处理与 processApplicationMessages 相同。

---

### setDefaultDllDirectories

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `flags` | `&nbsp;` | lls* 标志的组合 |

**返回值**

成功则返回 true

**说明**

::SetDefaultDllDirectories 的包装

---

### addDllDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 要添加的本地路径（※需事先调用 Storages.getLocalName） |

**返回值**

用于传给 removeDllDirectory 的固有值（为 0 时失败）
需事先在 setDefaultDllDirectories 中设置 llsUserDirs 标志

**说明**

::AddDllDirectory 的包装

0x00000400

---

### removeDllDirectory

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `cookie` | `&nbsp;` | 要删除的 addDllPath 固有值 |

**返回值**

成功则返回 true

**说明**

::RemoveDllDirectory 的包装

---

## 插件扩展: tftSave

系统扩展

### 成员列表

#### 方法

- [savePreRenderedFont](#saveprerenderedfont)
- [loadPreRenderedFont](#loadprerenderedfont)
- [modifyPreRenderedFont](#modifyprerenderedfont)

---

### savePreRenderedFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 要保存的文件名 |
| `characters` | `&nbsp;` | 包含要保存的字符（字符代码）的数组 |
| `callback` | `&nbsp;` | 获取信息与图像的回调<br>必须以字符代码为参数，返回图层(PreRenderedFontImage)的函数<br>function(ch) { return layer; } |

**说明**

把预渲染字体数据保存到文件

---

### loadPreRenderedFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 要读取的文件名 |
| `characters` | `&nbsp;` | 用于接收列表字符的数组 |
| `callback` | `&nbsp;` | 将来计划实现接收图像的回调(目前必须传入 void） |

**说明**

从文件读取预渲染字体数据

---

### modifyPreRenderedFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 要读取的文件名 |
| `callback` | `&nbsp;` | 用于获取和更新信息的回调<br>function(ch, info = %[ blackbox_x\|y, origin_x\|y, inc_x\|y, inc ]) { return true_if_modofied; } |

**说明**

更新预渲染字体数据的字形信息(可更改的只有origin_x|y, inc_x|y, inc / blackbox 固定)

---

## 插件扩展: windowEx

System 扩展

※引擎本体的 System 中也包含 getMonitorInfo / getDisplayMonitors / breathe /
readEnvValue / expandEnvString (WINVER / SDL3 系) 与 getSystemMetrics (WINVER)。
读取本插件后，这些会被插件版覆盖。

### 成员列表

#### 方法

- [getDisplayMonitors](#getdisplaymonitors)
- [getDisplayMonitors](#getdisplaymonitors)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [getMonitorInfo](#getmonitorinfo)
- [setDpiAwareness](#setdpiawareness)
- [setCursorPos](#setcursorpos)
- [getCursorPos](#getcursorpos)
- [setClipCursor](#setclipcursor)
- [getSystemMetrics](#getsystemmetrics)
- [getDoubleClickTime](#getdoubleclicktime)
- [readEnvValue](#readenvvalue)
- [expandEnvString](#expandenvstring)
- [setApplicationIcon](#setapplicationicon)
- [setIconicPreview](#seticonicpreview)
- [breathe](#breathe)
- [isBreathing](#isbreathing)
- [findWindowEx](#findwindowex)
- [classLongPtr](#classlongptr)
- [loadCursor](#loadcursor)
- [mapVirtualKey](#mapvirtualkey)

---

### getDisplayMonitors

方法

**返回值**

[ %[ name, primary, monitor:%[ x, y, w, h ], work:%[ x,y,w,h ], intersect:%[ x,y,w,h ] ], ... ];
name:      显示器的名称('\\.\DISPLAY?' 等)
primary:   是否为主显示器
monitor:   显示器的范围字典
work:      显示器的工作区域范围(最大化窗口时的显示范围等)
intersect: 与指定范围相交的区域(未指定时与 monitor 相同)

**说明**

获取显示器的信息列表

枚举所有显示器

---

### getDisplayMonitors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**说明**

只枚举与指定范围相交的显示器

---

### getMonitorInfo

方法

**返回值**

%[ name, primary, monitor:%[ x, y, w, h ], work:%[ x, y, w, h ] ];
显示器的信息。字典内容与 getDisplayMonitors 相同 (但没有 intersect 信息)。
near=false 时且没有显示器时返回 void。

**说明**

获取显示器信息

返回主显示器

---

### getMonitorInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

返回指定坐标位置所在的显示器

---

### getMonitorInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**说明**

返回与指定坐标范围相交最多的显示器

---

### getMonitorInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `window` | `&nbsp;` |  |

**说明**

返回与指定窗口的范围相交最多的显示器

---

### setDpiAwareness

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `context` | `&nbsp;` |  |

**说明**

调用 SetThreadDpiAwarenessContext

---

### setCursorPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**返回值**

get 时：%[ x, y ] 或 void(获取失败时)

**说明**

设置、获取鼠标光标的屏幕坐标

---

### getCursorPos

方法

---

### setClipCursor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `win_or_rect` | `&nbsp;` |  |

**说明**

光标位置裁剪处理

---

### getSystemMetrics

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | SM_* 的“*”部分的字符串（不过与大小写无关） |

**返回值**

度量值（内容因 index 而异）

**说明**

获取系统度量信息

详情请参照 GetSystemMetrics() API 的手册
SW_ARRANGE 没有 ARW_* 的定义，因此要用直接数值指定来比较

---

### getDoubleClickTime

方法

**返回值**

时间(ms) 默认值为 500ms

**说明**

获取系统的双击允许时间

详情请参照 GetDoubleClickTime() API 的手册
双击的允许移动范围可以用 getSystemMetrics 的 CXDOUBLECLK/CYDOUBLECLK 获取
在不用 Layer.onDoubleClick 而由软件模拟进行双击判定时使用（虽然写死时间也没问题，不过姑且……）

---

### readEnvValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 环境变量名 |

**返回值**

环境变量值（未定义时为 void）

**说明**

获取环境变量

---

### expandEnvString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 要展开的字符串 |

**返回值**

展开后的字符串

**说明**

将字符串内的“%~%”用环境变量展开

---

### setApplicationIcon

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` | 图标文件或 void（void 或 "" 时重置为初始状态） |

**说明**

更改在任务栏或 ALT+TAB 等中显示的应用程序图标

※ 不能指定归档内的文件，指定 exe 或 DLL 时会设置最开头的图标

---

### setIconicPreview

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `iconic` | `&nbsp;` | true 则显示图标代替缩略图／false 则解除设置 |

**返回值**

是否成功（XP 及以前总是失败）

**说明**

将 Vista 及以后的任务栏或 Alt+TAB 中的缩略图显示强制改为应用程序图标显示

※ 会在应用程序窗口上设置 DWMWA_FORCE_ICONIC_REPRESENTATION

---

### breathe

方法

**说明**

TVPBreathe, TVPGetBreathing 的包装

---

### isBreathing

方法

---

### findWindowEx

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `winname` | `void` | 窗口名 |
| `clsname` | `void` | 类名 |
| `parwin` | `void` | 父窗口（指定 Window 类或 HWND 数值） |
| `childafter` | `void` | 搜索起始位置的窗口（同上） |

**返回值**

成功时为 HWND 数值

**说明**

findWindoeEx 的包装

---

### classLongPtr

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `win` | `&nbsp;` | 对象窗口（指定 Window 类或 HWND 数值） |
| `key` | `&nbsp;` | 对象索引 在当前实现中为 {cursor,icon,iconsm,brbackground} 的任一字符串 |
| `setvalue_or_getasvoid` | `void` | 获取时传 void，指定数值时为 set （不过 key=brbackground 时可以指定 {black,white,gray,ltgray,dkgray} 的 Stock 画刷） |

**返回值**

成功时为当前（或紧邻前一次）的 LONG_PTR 数值／失败时为 void

**说明**

{Get,Set}ClassLongPtr 的包装

---

### loadCursor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `idc_or_res` | `&nbsp;` | 数值>=0 时为 MAKEINTRESOURCE，数值<0 时为 crXXXX，字符串时为资源名 |
| `hmodule` | `void` | 资源对象的 HMODULE 值 |

**返回值**

HCURSOR 数值

**说明**

LoadCursor 的包装

---

### mapVirtualKey

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `code` | `&nbsp;` | 虚拟键码或扫描码 |
| `maptype` | `&nbsp;` | MAPVK_* 值 |

**返回值**

keycode

**说明**

MapVirtualKey 的包装

---
