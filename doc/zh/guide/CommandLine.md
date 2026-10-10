# 命令行选项

## 命令行选项

吉里吉里的命令行选项除了可以通过常规命令行指定之外，

还可以通过 ( krkrrel.exe ) 或

( -userconf ) 保存到配置文件中。

选项的读取顺序为

1. 嵌入吉里吉里引擎本体的选项
2. 与吉里吉里核心位于同一目录的 .cf 文件
3. “引擎设置”(-userconf) 输出的、位于数据保存位置的 .cfu 文件
4. 在命令行中指定的选项

如此。对于 .cf 文件和 .cfu 文件，不存在时会被直接忽略。越靠后读取的指定越优先。

### 配置文件的名称与位置

| | Windows 原生版 | SDL3 版 (桌面) | SDL3 版 (其他) |
|---|---|---|---|
| 与 exe 相同位置 | `<exe名>.cf` | `<exe名>.cf` → `config.cf` | `config.cf` |
| 数据保存位置 | `<exe名>.cfu` | `<exe名>.cfu` | ( 不读取 ) |

`<exe名>.cf` 是把可执行文件的扩展名改为 `.cf` 后的文件 ( `krkrz64.exe` 的话就是
`krkrz64.cf` )。SDL3 版的桌面 ( Windows / macOS / Linux ) 按与 Windows
原生版相同的规则读取。以往就有的固定名称 `config.cf` 也会继续被
读取，但**两者都存在时 `<exe名>.cf` 优先**。

Android / iOS / 浏览器 ( wasm ) / 嵌入式设备中，“可执行文件旁边”和数据
保存位置未必是本地路径，因此按照以往方式仅读取 `config.cf`。

### 嵌入可执行文件的配置文件

除此之外，还有嵌入可执行文件内资源中的配置文件
( SDL3 系构建。Windows 原生版的嵌入选项作为可执行文件的
资源持有 )。

- `resource/config.cf` … 全平台共通
- `resource/config_<标签>.cf` … 按平台区分 ( 标签 = [System.platformTag](../reference/System.md#platformtag) )

用于在多个平台共用同一份资源素材，同时只想分开各机型设置的
情况。读取顺序为“具体的标签 → 一般的标签 → 共通 `config.cf`”，
**先读取的优先** ( 不存在的文件会被直接跳过读取 )。

### 配置文件的格式

1 行写 1 个选项，以**去掉开头的 `-` 的形式**书写。

```
; 行頭が ';' の行はコメント
datapath="$(exepath)\savedata"
readencoding=UTF-8
lowpri
```

- 格式为 `名称=值`。省略 `=` 以后的部分时，值会变为 `yes` ( 上面的 `lowpri` )。
- 用 `"` 或 `'` 包围值时，会作为 TJS 的字符串字面量来解释
  ( 可以使用转义 )。`-userconf` 输出的 `.cfu` 就是这种格式。
- 行末的换行、前后的空白、开头的 BOM 会被自动去除。换行代码
  CRLF / LF 均可。

> **Note:**
> 行末的去除是 2026-08 以后构建的行为。在此之前，行末的换行会包含在
> 值中，未用引号包围的值以及省略了值的行无法正确生效。



命令行选项基本上是在 '-' (连字符) 之后紧跟选项的名称。然后再接着写 '='，书写选项的值。

例如，若 -cdvol 这个选项的值为 direct，则指定为 -cdvol=direct。



除“启动选项”、“调试相关选项”和“系统兼容性相关选项”之外，大部分都是用于解决环境相关问题而进行微调的选项。

关于环境相关问题的解决，

也请参照。

> **Note:**
> 通过 Releaser 或 -userconf，可以改写吉里吉里的可执行文件或外部配置文件来更改这些选项，但通常保持默认即可，没有问题。**由于是在制作作品一方固有的环境中出现了问题，因此不建议把将这些选项改为非默认值后的可执行文件或配置文件向一般用户分发** ( 当然，也有像 -datapath 这样应根据发布形态或使用形态来设置的选项 )。

在下面的列表中，标有“可动态更改”的项是可以用 [System.setArgument](../reference/System.md#setargument) 方法更改的项。除此之外的选项无法动态更改。

### 参数的分隔 ( `--` ) 与文件参数

命令行参数按如下方式处理。

- `-名称[=值]` 是选项 ( 省略值时视为 `yes` )。
- 开头没有连字符的参数，是项目文件夹 ( 或归档 ) 的指定。
- 单独的 `--` 之后的内容不会作为选项读取，而会成为传递给脚本的参数。
  可以按顺序以 `-arg0` / `-arg1` / … 这样的名称从 [System.getArgument](../reference/System.md#getargument) 取出。

```text
krkrz64.exe D:/game/ -loglevel=info -- -mode a.txt
→ プロジェクト: D:/game/、オプション: -loglevel=info、-arg0=-mode、-arg1=a.txt
```

像把文件关联起来打开的工具等，希望把“参数全部作为脚本接收的文件名”来
处理时，请使用引擎本体内置的安全选项 `acceptfilenameargument`
( `TVPSystemSecurityOptions` 的一个项目。由构建时的值，或对可执行文件进行相同长度的改写来决定 )。

| `acceptfilenameargument` | 行为 |
|---|---|
| 0 ( 默认 ) | 如上所述 |
| 1 | 把所有参数都变为 `-argN`。不读取选项，也不读取项目指定 |
| 2 | 若有单独的 `--`，则把它之前的 `-名称[=值]` 作为选项读取，把它之前的无连字符参数与 `--` 之后的内容按此顺序变为 `-argN`。没有 `--` 时与 1 相同 |

在 1 和 2 中，无连字符的参数不会用于项目指定 ( 项目会从可执行文件旁边的
`data.xp3` / `data` 文件夹等自动查找 )。使用 2 的话，即使是接收文件参数的工具，
也能在命令行传递 `-datapath` / `-loglevel` / `-replfile` 等选项。

```text
( acceptfilenameargument=2 )
tool.exe -replfile=D:/ch -datapath=D:/ch/sd -- -batch a.mmo
→ オプション: -replfile / -datapath、-arg0=-batch、-arg1=a.mmo
```

## 启动选项

为了仅调用并使用吉里吉里的特定功能，有以下选项。

- **-**userconf** (面向最终用户的设置工具的启动)**  
  启动引擎本体内置的面向最终用户的设置工具。
- **-**about** (版权信息对话框的显示)**  
  显示“版本、版权、环境信息”对话框。附带组件的许可证列表也会一并显示 ( 全文可以用 -license=<名称> 取出 )。
- **-**sel** (“文件夹/归档选择”对话框的显示)**  
  显示“文件夹/归档选择”对话框。data.xp3 等数据不会被自动检测。
  
  作为命令行参数 (不在开头加连字符) 指定文件夹时，可以在该文件夹处于初始选中状态下打开“文件夹/归档选择”对话框。
- **-**nosel** (“文件夹/归档选择”对话框的抑制 / Windows 原生 (WINVER) 构建限定)**  
  不显示无法确定数据文件夹时出现的“文件夹/归档选择”对话框，直接继续启动处理。不需要值。
  
  在像 -about / -license 那样输出信息后结束，或者不提供数据直接启动并从 REPL 侧开始处理等、对话框出现后停止会造成困扰的用途中指定。
- **-**printdatapath** (数据保存位置的输出)**  
  把数据保存位置 (-datapath 选项) 的设置内容与换行输出到标准输出，然后结束。这个选项是为了供与吉里吉里引擎本体协作进行存档数据管理的外部应用程序等使用。
  
  数据保存位置中，$(exepath) 等特殊字符串会以替换后的状态输出。
  
  吉里吉里引擎本体是 GUI 应用程序，因此即使从命令提示符直接启动吉里吉里可执行文件并指定 -printdatapath 选项，也不会显示任何内容。要获取输出内容，请使用管道或重定向。
- **-**license** (附带许可证的输出)**  
  把引擎本体、插件、项目数据持有的许可证信息输出到标准输出，然后结束。

  | 指定 | 输出 |
  |---|---|
  | `-license` | 列表 ( 名称 / 分类 / 提供者 ) |
  | `-license=<名称>` | 该 1 件的许可证全文 |
  | `-license=all` | 全部件的许可证全文 |

  列表中，除了引擎本体内置的部分之外，已加载插件注册的部分以及放在项目 `licenses` 文件夹中的文本 ( `licenses/*.txt` ) 也会汇入。要在运行时从 TJS 获取，请使用 [System.getLicenseList](../reference/System.md#getlicenselist) / [System.getLicenseText](../reference/System.md#getlicensetext)。

  即使不指定项目启动，也不会显示文件夹选择对话框 ( 输出许可证信息后结束 )。指定项目启动时，该项目的 `licenses` 文件夹的部分也会列入列表。

  与 -printdatapath 相同，吉里吉里引擎本体是 GUI 应用程序，因此从命令提示符直接启动也不会显示任何内容。要获取输出内容，请使用管道或重定向。另外，启动时的信息日志也会输出到同一标准输出，因此进行机械处理时请切出许可证信息部分。
- **-**startup** (启动脚本的指定)**  
  指定最初执行的脚本文件名。
  
  未指定时，会执行 startup.tjs。
- **-**nostartup** (启动脚本自动执行的抑制 / 面向 `KRKRZ_REPL` 构建)**  
  指定后，会抑制 startup.tjs ( 以及由 `-startup` 指定的启动脚本 ) 的自动执行。用于 `-repl` / `-replfile` 系 agent 驱动中，不打开窗口、以静止状态启动，想从 REPL 显式调用脚本来开始处理的场合。
  
  可设置的值是 **'1'**、**'yes'**、**'true'**、**'on'** ( 启用 ) 或省略值 ( 启用 )，以及 **'0'**、**'no'**、**'false'**、**'off'** ( 禁用 )。不指定则禁用。
  
  即使启动脚本无效，指定了 `-nostartup` 时也不会在没有创建窗口的情况下立即结束。

## 系统整体选项

- **-**datapath** (数据保存位置)**  
  设置吉里吉里保存各种数据的位置(文件夹)。
  
  可设置的值以字符串指定。
  
  也可以直接用完整路径指定文件夹名，但通常嵌入以下特殊字符串来使用。
  
  - **$(exepath)**  
    会被替换为 System.exePath (吉里吉里核心所在的文件夹名)。
  - **$(appdatapath)**  
    会被替换为 System.appDataPath (用户的主文件夹)。这个文件夹通常是隐藏文件夹。
  - **$(personalpath)**  
    会被替换为 System.personalPath (我的文档文件夹)。
  - **$(vistapath)**  
    OS 为 Vista 以后时替换为 $(appdatapath)，低于 Vista 时替换为 $(exepath)。
  - **$(savedgamespath)**  
    会被替换为 System.savedGamesPath (游戏存档数据用文件夹)。(1.1.0 以后)
  
  上面的说明是 Windows 版的内容。在 **Windows 以外的 SDL3 版**中，`$(appdatapath)` / `$(personalpath)` / `$(vistapath)` / `$(savedgamespath)` 都会替换为**每个应用的用户区域** ( `user://`。Linux 版为下述本地路径 )，与 [System.appDataPath](../reference/System.md#appdatapath) / [System.personalPath](../reference/System.md#personalpath) 返回的 OS 标准文件夹 ( macOS 的 `~/Library/Application Support/` 等 ) 不一致。
  
  默认情况下是“$(exepath)\savedata” (**Linux 版除外**。见下文)。这个设置适合不特别使用安装程序、把程序以 zip 等压缩打包后分发，用户展开后立即运行程序这样的分发形态。
  
  然而，在这个默认设置下，把程序放置在 Program Files 以下时，或者在 Windows XP 等“受限用户”等情况下启动程序时，可能因没有写入 Program Files 以下的权限而无法写入文件并出错。
  
  改为“$(appdatapath)\应用程序名”或“$(personalpath)\应用程序名”这样的名称后，会写入每个用户的文件夹，因此这类问题不易发生，但存档数据保存位置会变得不直观，用户可能会感到困惑。
  
  
  
  !!! warning "重要 (2026-10 的更改)：Linux 版的默认保存位置"
      Linux 版 (SDL3) 的默认值变为 **每个用户的文件夹 `~/.local/share/<组织名>/<应用程序名>/`** ( 如果有 `$XDG_DATA_HOME` 则在其下。组织名、应用程序名由 -orgname / -appname 指定，未指定则为 `wamsoft` / `krkrz` )。以前是可执行文件旁边的 `savedata`，但因为在 AppImage / Flatpak / `/opt` 等位置的部署中无法写入。

      - 在发布物中请在 `<exe名>.cf` 中写入 `orgname` 和 `appname`，为每个作品确定文件夹。Steam Cloud 的同步路径也要与这个文件夹一致。
      - 想按以往方式放在可执行文件旁边时，指定 `datapath="$(exepath)/savedata"`。
      - 在 Linux 版中，`$(appdatapath)` / `$(personalpath)` / `$(vistapath)` / `$(savedgamespath)` 也会替换为这个每个用户的文件夹 (本地路径)。用 `\` 分隔书写的值会被改为 `/`，末尾的分隔符也会被补上。
      - 实际的保存位置可以通过启动日志中的 `datapath (Linux default, ...)` / 数据保存位置行确认。如果可执行文件旁边残留着旧默认的存档 (`savedata*`)，会输出提示迁移的警告。
      - 以前的 Linux 版默认保存位置末尾没有 `/`，`System.dataPath + "文件名"` 会被写为可执行文件旁边的 `savedata文件名`。如果还残留着，请移动到新位置。

  由这个选项指定的数据保存位置，在吉里吉里启动时，如果不存在则会尝试创建。即使创建失败也不会就此结束，而是继续处理，因此请在用户脚本内 (通过捕获无法保存数据等异常的方式) 进行错误处理。
  
  
  
  用“引擎设置”进行的设置会创建在这个数据保存位置所指定的文件夹中。除此之外，各种日志默认也会创建在这个文件夹中。
- **-**contfreq** (处理等待)**  
  设置是否通过在转场等处理中边加等待边以指定的周期调用处理，来降低 CPU 使用率。
  
  可设置的值是 **'0' (不加等待)** 或正整数，不指定这个选项时视为指定了 '0'。指定正整数时，可以以 Hz 为单位指定周期。
  
  受这个选项影响的是转场以及用 System.addContinuousHandler 注册的 Continuous 处理器。
  
  设为 '0' 时，在执行转场等期间会用尽 CPU 进行处理。
  
  指定数值后，会以该周期进行处理，多余的时间会让 CPU 休息。由此可以降低对其他应用程序的影响、CPU 温度的上升以及计算机的耗电量。指定的数值越低，这个效果越强。不过，指定较低的数值可能会使转场等变得不流畅。
  
  用 waitvsync 选项进行垂直同步等待时，Continuous 处理器会配合垂直同步的时机被驱动，contfreq 选项的设置内容会被忽略。
  
  这个选项可以动态更改，但更改会在下次转场或 Continuous 处理器的运行中断时生效。
- **-**eventexceptionlimit** (每帧系事件的连续异常上限)**  
  这是当 onDraw 或 Timer 的处理器等每帧反复触发的事件持续抛出异常时的保护机制。按触发源统计连续异常次数，达到上限后会自动停止该触发源并输出 WARNING 日志。
  
  可设置的值是正整数，不指定这个选项时视为指定了 **'10'**。指定 **'0'** 则保护机制无效。
  
  主要用于 REPL 驱动等“不因异常而结束”的构成中，防止同样的异常每帧不断发生下去。
- **-**memusage** (内存使用量)**  
  内存使用量的设置。
  
  可设置的值是 **'normal' (通常)** 或 **'low' (低)**，不指定这个选项时视为指定了 'normal'。
  
  选择“低”会比选择“通常”更节省内存地使用。但是选择“低”时，吉里吉里内部的各种缓存机制会受到限制，TJS2 的哈希表大小也会受到限制，因此性能会下降。另外，选择“低”时，“图形-图像缓存限制”会被强制视为“不进行缓存”的设置。
- **-**laxtimer** (计时器事件容许量限制)**  
  设置是否限制一次蓄积到系统中的计时器事件数量 ( 最大发生容许量 )，以避免计时器事件积压过多而无法处理的情况。
  
  可设置的值是 **'no' (不限制)** 或 **'yes' (限制)**，不指定这个选项时视为指定了 'no'。
  
  在处理非常慢的计算机上，或者用计时器驱动非常繁重处理的场合等，可能无法跟上计时器发生的事件，导致吉里吉里难以响应操作。用这个选项指定 'yes' 后，会把系统中蓄积的计时器事件最大发生容许量固定为 1 ( Timer 类的 capacity 属性为 1 的状态 )。由此可以抑制系统无法处理完的计时器事件发生，但通常计时器的精度和准确性会降低。
- **-**lowpri** (低优先级)**  
  设置是否在转场等期间降低优先级。
  
  可设置的值是 **'no' (不降低)** 或 **'yes' (降低)**，不指定这个选项时视为指定了 'no'。
  
  设为 'yes' 后，在执行转场等、吉里吉里的主线程连续使用 CPU 的场合，会降低主线程的执行优先级。由此，转场中的声音中断、转场中其他应用程序难以操作等症状可能会得到改善。
- **-**language** (消息语言 / 显示语言的显式指定)**  
  显式指定引擎消息 ( 错误文本等 ) 与选项解说 ( `-userconf` 的设置 UI ) 的语言。
  
  可设置的值是 BCP-47 形式 ( **'ja-JP'**、**'en-US'**、**'zh-Hans'** 等 ) 或缩写形式 ( **'ja'**、**'en'**、**'chs'**、**'cht'** )。不指定时跟随 OS 的语言设置 ( [System.systemLanguage](../reference/System.md#systemlanguage) )。支持的语言是 ja / en / chs / cht，没有对应素材的语言会回退到英语 ( 若英语也没有则回退到日语 )。
  
  在 Windows 原生 ( WINVER ) 构建中会反映到 PE 资源的语言解析 ( 消息字符串、设置对话框 )，在 SDL3 构建中会反映到 `messages*.json` / `optiondesc*.json` 的选择。**反映到消息字符串仅在命令行中直接指定时** ( 在配置文件内指定时只反映到选项解说的语言 )。
- **-**exceptionexe** (异常时启动编辑器)**  
  指定发生异常时启动的编辑器。
- **-**exceptionarg** (异常时启动编辑器选项)**  
  指定发生异常时启动编辑器时所指定的选项。
  
  也可以单纯指定参数，但通常会嵌入以下特殊字符串来使用。
  
  - **%filepath%**  
    会被替换为发生异常的脚本的文件路径。
  - **%line%**  
    会被替换为发生异常的行号。
- **-**appname** (应用程序名 / SDL3 构建限定)**  
  指定用于决定用户数据保存位置 ( `user://` ) 的应用程序名。不指定则使用 'krkrz'。
  
  保存位置按照各 OS 的规范决定 ( Windows 下为 `%APPDATA%` 下的 组织名/应用程序名 )。想用同一引擎分开多个应用程序的数据时，与 -orgname 一起指定。
- **-**orgname** (组织名 / SDL3 构建限定)**  
  指定用于决定用户数据保存位置 ( `user://` ) 的组织名。不指定则使用 'wamsoft'。
- **-**uselfh** (使用 LFH / Windows 原生 (WINVER) 构建限定)**  
  可设置的值是 **'yes'**、**'true'** ( 使用 )，指定其他值以及不指定时不使用。
  
  启用抑制内存碎片化的 LFH ( Low Fragmentation Heap )。Windows Vista 以后由 OS 侧默认启用，通常无需指定。

### 内存池的大小

引擎会在启动时按用途各异的分配器统一确保 TLSF 池 ( 明细的查看方法请参照 [内存使用量的观测](../topics/core/memory_observation.md) )。

以下选项都取 **以 MB 为单位的整数**。指定 **'none'** / **'off'** / **'0'** 则不创建该池，按以往方式使用 malloc。

| 选项 | 对象 | 默认 |
|---|---|---|
| `-bitmappoolsize` | BitmapAllocator ( [Bitmap](../reference/Bitmap.md) 的图像区域。图像缓存的上限也跟随它 ) | 512MB ( 32bit 进程为 128MB ) |
| `-filepoolsize` | FileAllocator ( 文件层的缓存。缓存预算也跟随它 ) | 256MB ( 32bit 进程为 64MB ) |
| `-krkrzpoolsize` | GlobalAlloc[Krkrz] ( 经 `operator new` / `TJS_malloc` 的分配 ) | 256MB ( 32bit 进程为 64MB ) |
| `-soundpoolsize` | SoundAllocator ( PCM / 环形缓冲区 / DSP 的工作区 ) | 16MB |
| `-sdlpoolsize` | GlobalAlloc[SDL] ( 仅用 `KRKRZ_SDLMEMORY_STAT=ON` 构建的 SDL3 系构建 ) | 64MB |

池会在启动时整体确保，因此设大会相应减少可用于通用堆 ( GL / TJS / 图像解码等 ) 的内存。在可分配给应用程序的内存固定的环境中尤其如此，请按只增加默认不足的池的方向调整。池不足时只会回退到 malloc，并不会导致无法运行。

### 通过 web:// 的按需分发 ( 浏览器 (wasm) 构建限定 )

这是不把数据打包成 xp3，而是作为零散文件放在服务器上，用 `web://./<路径>` 逐次获取的设置。

- **-**webbase** (web:// 的基点 URL)**  
  指定解析 `web://` 路径时的基点 URL。
- **-**webmanifest** (文件列表清单的名称)**  
  指定放在基点 URL 正下方的文件列表清单 ( JSON ) 的名称。不指定则使用 'krkrz_files.json'。
  
  服务器上的零散文件无法列举文件夹内容，因此 [Storages.addAutoPath](../reference/Storages.md#addautopath) 的搜索表会根据这个清单构建。

## 输入相关选项

- **-**wheel** (鼠标滚轮旋转检测方法)**  
  设置如何检测鼠标滚轮的旋转。
  
  可设置的值是 **'no' (不使用)** 或 **'message' (窗口消息)**，不指定这个选项时视为指定了 'message'。选择“不使用”后鼠标滚轮将无法使用。
  
  ※ 以前存在的 'dinput' (DirectInput) 已被废除。DirectInput 是
  面向独占全屏时 `WM_MOUSEWHEEL` 无法送达的旧环境的规避手段，但
  现在由于是 D3D11 (无边框窗口)，始终可以通过窗口消息检测，
  因此已移除对 DirectInput 的依赖。为兼容起见，指定 'dinput' 会作为
  'message' 处理。
- **-**joypad** (手柄使用可否)**  
  设置是否使用游戏手柄 (摇杆)。
  
  可设置的值是 **'no' (不使用)**，指定后游戏手柄功能会完全
  失效 (状态获取、按键事件生成均不进行)。不指定
  时手柄有效，没有连接时会自动变为无效。
  
  ※ 游戏手柄的实现已重新设计为基于 XInput (WINVER) / SDL_Gamepad (其他)
  (旧 'dinput' 值已废除)。在其他设备被错误地
  识别为手柄而误动作的罕见情况下，请为支持用途使用 'no'
  ( 手柄规格请参照 Gamepad 一节 )。
- **-**paddelay** (手柄按键重复延迟)**  
  以毫秒为单位指定游戏手柄 (摇杆) 到按键重复为止的时间。
  
  可设置的值是正数或 -1，指定 -1 后将不再进行按键重复。不指定这个选项时视为指定了 500。
  
  这个选项可以动态更改。  
  
  **对 Elements 画面导航的影响**: 仅在这个选项被**显式指定时**，Elements 对话框的焦点移动 ( 手柄十字键 / 摇杆长按 ) 的默认值也会使用相同的值。不指定时仍按以往方式保持 Elements 侧的默认值 ( 400ms / 与按入量联动 )。如果画面 JSON 中写有 `"input": { "repeat_delay_ms", "repeat_rate_ms" }`，则优先使用它 ( 优先顺序 = 画面 JSON > 这个选项 > `input_defaults.jsonc` > 内置默认 )。
- **-**padinterval** (手柄按键重复间隔)**  
  以毫秒为单位指定手柄 (摇杆) 的按键重复间隔。值越小重复越快。
  
  可设置的值是正数，不指定这个选项时视为指定了 30
  
  这个选项可以动态更改。  
  
  **对 Elements 画面导航的影响**: 仅在这个选项被**显式指定时**，Elements 对话框的焦点移动 ( 手柄十字键 / 摇杆长按 ) 的默认值也会使用相同的值。不指定时仍按以往方式保持 Elements 侧的默认值 ( 400ms / 与按入量联动 )。如果画面 JSON 中写有 `"input": { "repeat_delay_ms", "repeat_rate_ms" }`，则优先使用它 ( 优先顺序 = 画面 JSON > 这个选项 > `input_defaults.jsonc` > 内置默认 )。
- **-**padbuttons** (手柄的按钮分配方式 / SDL3、通用构建限定)**  
  设置把游戏手柄的物理按钮如何分配到 `VK_PAD1`~`VK_PAD4`。
  
  可设置的值是 **'label' (按按钮的标识分配)** 或 **'position' (按按钮的位置分配)** 之一，不指定这个选项时视为指定了 'label'。
  
  在 'label' 下，`VK_PAD1` 分配到标识 A ( PlayStation 上为 ✕ ) 的按钮，`VK_PAD2` 为 B ( ○ )、`VK_PAD3` 为 X ( □ )、`VK_PAD4` 为 Y ( △ )。即使是像任天堂系那样 A/B、X/Y 位置互换的手柄，画面显示与实际按下的按钮也能一致。
  
  'position' 是以往的分配方式，下 = `VK_PAD1`、右 = `VK_PAD2`、左 = `VK_PAD3`、上 = `VK_PAD4`。无法判定标识的手柄即使在指定 'label' 时也会自动回退到这种方式。PlayStation / Xbox 系无论哪种方式结果都相同。
  
  运行中的更改可以通过 [System.padButtonMapping](../reference/System.md#padbuttonmapping) 进行。
  
  这个选项仅在 SDL3 / 通用构建中有效。Windows 原生 ( WINVER ) 构建的手柄输入基于 XInput，按钮的标识固定为 Xbox 系，因此位置与标识不会不一致。
- **-**controlime** (IME 状态控制)**  
  设置是否进行 IME (日语等转换输入软件) 的状态控制 (启用或禁用等控制)。
  
  可设置的值是 **'yes' (进行)** 或 **'no' (不进行)**，不指定这个选项时视为指定了 'yes'。
  
  选择“不进行”时，可能可以规避“无法通过 IME 进行日语等语言的输入”这类故障。

## 声音相关选项

- **-**wsfreq** (声音输出频率)**  
  声音输出 (混音器) 的采样频率的设置。
  
  可设置的值是表示频率的正整数，以 Hz 为单位，不指定这个选项时视为指定了 '44100'。
  
  特别是在使用 WDM 系声音驱动的环境 (Windows2000、XP 以后等) 中，有时即使更改设置，播放状态也没有变化。
- **-**wspreinit** (音频设备先行初始化)**  
  可设置的值是 **'yes' (进行)** 或 **'no' (不进行)**，不指定这个选项时视为指定了 'yes'。
  
  为 'yes' 时，启动时会先行初始化音频设备 (miniaudio 引擎)。为 'no' 时按照以往方式，在首次播放声音时才进行初始化。
  
  按照以往方式在首次播放声音时才打开设备时，播放开始会延迟设备打开所需的时间，声音的开头可能会缺失。设为 'yes' (默认) 时可以提前在启动时完成初始化，因此能防止这种开头缺失。
  
  出于某种原因希望避免在启动时打开设备时 (声音驱动不稳定等)，请指定 'no'。
- **-**opus_pcm_format** / **-**ogg_pcm_format** (解码输出格式)**  
  指定 **'f32'** 时，会将该编解码器的解码输出变为 IEEE 32bit float。不指定则以 16bit 整数输出 ( `-opus_pcm_format` 对应 opus，`-ogg_pcm_format` 对应 ogg ( Vorbis ) )。
  
  在需要大幅加算增益 ( 下述 -opus_gain / -ogg_gain / ReplayGain ) 等、希望避免在 16bit 下削波时使用。1 个采样会从 2 字节变为 4 字节，因此会相应增加内存和带宽的使用。

### 声音的增益

这是在解码压缩音频时**以 dB 为单位加算增益 (音量)** 的机制。它把旧 wuvorbis / wuopus 插件的增益扩展整合到了引擎本体内置解码器中。会应用整体增益 ( 下述选项 )、ReplayGain 标签、按曲目回调 ( [WaveSoundBuffer.setGainQueryCallback](../reference/WaveSoundBuffer.md) ) 的合计值。

- **-**opus_gain** (opus 整体增益)**  
  以 dB 指定适用于 opus 整个播放的增益。opus 会在解码器内部应用头部的输出增益 (R128)，因此这个值会加到它之上。
- **-**ogg_gain** / **-**vorbis_gain** (ogg/Vorbis 整体增益)**  
  以 dB 指定适用于 ogg ( Vorbis ) 整个播放的增益 ( 两者同义。`-vorbis_gain` 为旧插件兼容 )。Vorbis 的格式中没有增益概念，因此会在 float 域中缩放输出的 PCM 来应用。
- **-**ogg_rg** / **-**vorbis_rg** (ogg/Vorbis ReplayGain)**  
  可设置的值是 **'none' (不使用)**、**'track' (曲目增益)**、**'album' (专辑增益)**，默认为 'none'。会读取文件的 `replaygain_track_gain` / `replaygain_album_gain` 标签，并加算其 dB ( 为了不改变既有播放，默认无效 )。

> **推荐**: opus 按规格在头部持有输出增益 (R128)，可以在解码器内部准确、低成本地应用增益。积极处理增益或响度时，**推荐使用 opus**。

### 已废弃的声音选项

- **-**wsdecpri** (PCM 解码线程优先级)**  
  在声音底层迁移到 miniaudio 时被移除。指定也只会被忽略。

## 图形相关选项

- **-**display** (指定启动的显示器)**  
  在多显示器环境中，指定窗口最初显示的显示器 (监视器)。WINVER 构建 / SDL3 构建均可使用。

  可设置的值是以下之一。

  - **编号**  
    从 1 开始的显示器编号。在 Windows 中对应 `\\.\DISPLAY1` … 的编号 (与“设置”→“系统”→“显示”中显示的编号对应)。例: `-display=2`
  - **名称**  
    监视器名的一部分 (不区分大小写)。例: `-display=DELL`  
    与多个显示器匹配时，选择编号较小的一个。
  - **primary**  
    指定主显示器。
  - **list**  
    仅把显示器列表输出到日志，不进行显示器指定 (`?` / `help` 相同)。用于调查编号或名称。

  没有与指定匹配的显示器时，会在日志中输出警告和列表，然后按与未指定时相同的方式运行。

  窗口在生成时和首次显示之前，会被移动到指定显示器的工作区 ( 除去任务栏等的范围 ) 内。脚本指定了窗口位置时，会保持相对于该显示器工作区原点的位置。移动仅在启动时进行一次，因此不会妨碍之后用户把窗口移到其他显示器。

  全屏是针对窗口所在的显示器进行的，因此在全屏时会使用这个选项指定的显示器。

  这个选项主要假定用于测试用途 (在不打扰主显示器工作的情况下确认运行)。
- **-**maximizebox** (窗口最大化按钮的启用/禁用 / SDL3 构建的 Windows 限定)**  
  设置是否显示标题栏的最大化按钮。

  可设置的值是 **'yes' (启用)** 或 **'no' (禁用)**。不指定这个选项时视为指定了 'yes'。

  指定 'no' 后最大化按钮会消失，通过双击标题栏或 Win+↑ 进行的最大化也会变得不可用。**通过拖动窗口边框调整大小和用 Alt+Enter 切换全屏仍可照常使用**。在固定画面比例的构成 ( [Window.aspectLock](../reference/Window.md#aspectlock) ) 中，只希望禁止向整个工作区扩展的最大化时使用。

  仅在 SDL3 构建的 Windows 中有效 ( 在其他平台和 WINVER 构建中不执行任何操作 )。
- **-**gclim** (图像缓存限制)**  
  设置用于图像缓存的内存最大值。
  
  可设置的值是 **'auto' (自动)** 或整数值，指定整数值时以 MB 为单位指定用于图像缓存的内存。不指定这个选项时视为指定了 'auto'。
  
  吉里吉里具有缓存一旦读取过的图像以便快速访问的机制。这里指定该机制所用内存的限制值。
  
  指定 'auto' 时，会根据计算机上配备的物理内存量自动决定值。
  
  指定 '0' 时不进行缓存。
  
  如果吉里吉里运行中频繁发生交换，把这个值指定得较小或指定 '0' 可能会有所改善。
- **-**fsres** (全屏时的屏幕分辨率)**  
  全屏时的屏幕分辨率的设置。
  
  可设置的值是 **'auto' (自动)**、**'proportional' (纵横比相同的分辨率)**、**'nearest' (最近的分辨率)**、**'nochange' (不更改分辨率)** 之一，不指定这个选项时视为指定了 'nochange'。
  
  ※ 仅在 Windows 原生 ( WINVER ) 构建中有效 ( -fszoom 同样 )。SDL3 构建的全屏是不更改分辨率的无边框方式，显示倍率遵循 Window 的几何设置。
  
  选择 'auto' 时，会自动选择并使用最合适的分辨率。这种情况下，会从纵横比相同的分辨率中，选择与程序内指定的分辨率吻合的分辨率，如果没有这样的分辨率，则在不更改分辨率的情况下由引擎侧放大显示。这种设置下，即使 -fszoom (全屏时由引擎放大显示) 选项指定了 'no' (不进行)，也始终视为 'outer' (使其适合监视器内)。
  
  选择 'proportional' 时，会从屏幕纵横比与非全屏时相同的分辨率中，选择与程序内指定的分辨率相同或更大、且最接近的分辨率。
  
  选择 'nearest' 时，会选择与程序内指定的分辨率相同或更大、最接近的分辨率，但不保证选择到与非全屏时纵横比相同的分辨率。在显像管显示器或支持保持画面宽高比进行放大显示的液晶显示器等设备上，这种设置可能更合适。
  
  选择 'nochange' 时，将保持非全屏时的分辨率，不再更改分辨率。
  
  这个选项可以动态更改，但值会在下次尝试进入全屏时生效。
- **-**fszoom** (全屏时由引擎放大显示)**  
  指定全屏时如何由引擎进行画面放大。
  
  可设置的值是 **'inner' (使其适合监视器内)**、**'outer' (放大到充满监视器)**、**'no' (不进行)** 之一，不指定这个选项时视为指定了 'inner'。
  
  选择 'inner' 时，如有必要，会由引擎进行放大。必要的情况是指画面分辨率与程序内指定的分辨率不同的情况 ( 如果画面分辨率低于程序内指定的分辨率，则进行缩小处理 )。此时会在保持程序内指定的分辨率纵横比的状态下进行放大，但当监视器的纵横比与该纵横比不同时，上下或左右可能会出现空隙。这个空隙始终以全黑状态显示。
  
  指定 'outer' 时，与指定 'inner' 相同，如有必要会由引擎进行放大。但是与 'inner' 不同，当监视器的纵横比与程序内指定的纵横比不同时，会放大到极限以避免上下或左右出现空隙。因此不会出现空隙，但画面可能会溢出到监视器之外。这种设置下，例如在 16:10 的监视器上显示 16:9 的内容时，可以在不产生空隙的情况下放大到极限进行显示。当然，这会产生向左右溢出的区域，因此如果要制作设想这种显示的内容，就需要采取不把重要的 UI 或文字显示在溢出部分等对策。
  
  选择 'no' 时，即使有必要，引擎也不会进行放大。这种情况下，即使画面分辨率与程序内指定的分辨率不同，引擎侧也不会放大 ( 其结果，图像可能会较小地显示在画面中央 )。
  
  当监视器本来的分辨率与显卡输出的信号分辨率不同时，液晶显示器等可能会由监视器侧进行放大显示，但如果在监视器侧进行放大处理后引擎侧也进行放大显示，就会发生双重放大，图像可能会变差，请注意 ( -fsres 的“自动”选项会自动选择能防止这种双重放大显示的组合 )。
  
  这个选项可以动态更改，但值会在下次尝试进入全屏时生效。
- **-**fsmethod** (全屏的切换方式)**  
  过去是用于在 Direct3D 9 的全屏模式与通过 `ChangeDisplaySettings` 更改分辨率之间切换的选项，但随着 Direct3D 9 路径的撤除，**指定会被忽略** ( 始终为 `ChangeDisplaySettings` 路径 )。
- **-**gsplit** (图像运算的分割处理)**  
  设置是否把图像运算细分后进行。
  
  可设置的值是 **'yes' (进行)**、**'int' (隔行分割)**、**'bidi' (双向分割)**、**'no' (不进行)** 之一。WINVER 构建中不指定时视为指定了 'yes'，但 SDL3 构建中不指定时视为指定了 'no' ( 因为 GDI 单线程时代的 CPU 缓存局部性优化在 SDL3 / OpenGL 环境中，驱动同步 / dispatch 开销反而占主导，尤其是在全画面视频播放时会大幅变慢 )。
  
  吉里吉里为了有效利用 CPU 的内存缓存，在绘制图像时会分割成细小区域进行运算。在某些环境中这似乎会导致画面闪烁。在这样的环境中，指定 'no' 可能可以抑制闪烁，但绘制的性能也可能下降。启用双缓冲时，不进行分割处理的意义不大，因此建议设为进行分割处理。
  
  'int' 会每隔一个单位处理图像运算，但画面更新时可能会看到条纹。选择 'bidi' 时，图像运算的顺序会按 上→下、下→上 交替重复 ( 'yes' 时始终为 上→下 )。
- **-**smoothzoom** (放大显示时的平滑处理)**  
  设置在使用 Window.setZoom 等进行显示内容的放大显示时，或吉里吉里通过 -fsres 选项进行画面的放大 (缩小) 显示时，是否进行平滑处理 (放大时的插值) ( 与 Layer.affineCopy 等中的放大缩小无关 )。
  
  可设置的值是 **'no' (不进行)**、**'yes' (进行)** 之一，不指定这个选项时视为指定了 'yes'。
  
  进行平滑处理后，图像会变得平滑，但会有少许模糊感。不进行平滑处理时，图像会变得锐利，但锯齿会变得显眼。
  
  根据环境不同，不进行平滑处理可能反而会降低性能。另外，可能也存在平滑处理不起作用的环境。
  
  根据第三方绘制设备 ( 用 Window.drawDevice 属性设置的设备 ) 的不同，有些可能不受这个选项影响。
  
  这个选项可以动态更改，但不保证值会立即生效。
- **-**deffont** (默认字体)**  
  指定未指定字体名时使用的默认字体的字体名。
  
  不指定时，会根据运行环境的语言设置，从 `fonts.json` 中声明的字体、附带字体、OS 字体中选择。在 Windows 原生 (WINVER) 构建中，也可以指定 `DEFAULT_GUI_FONT` 等预置字体名。
- **-**systemfont** (使用 OS 字体)**  
  指定 **'yes' (使用)** (默认) 或 **'no' (不使用)**。这是设置 SDL 版等其他 (WINVER 以外) 构建中，是否可以通过名称使用 OS 中安装的字体的选项。
  
  为 'yes' 时，启动时会从 OS 的字体列表 (Windows 为 DirectWrite，Linux 为 fontconfig) 中只注册名称与文件的对应关系，实际文件会在首次使用该字体时读取。这样就能在 `Font.face` 中写 "Meiryo" 或 "Noto Sans CJK JP" 等 OS 字体名，默认字体的候选中也会包含 OS 的日语字体。macOS / Android 不支持 ( 不会注册 )。
  
  不希望发布物的外观受运行环境字体影响时，请指定 'no'。WINVER 构建由 GDI 直接处理 OS 字体，因此不受这个选项影响。
- **-**aamethod** (抗锯齿文字绘制方式)**  
  抗锯齿文字绘制方法的设置。
  
  可设置的值是 **'auto' (自动)**、**'res4' (重采样 4×4)**、**'res8' (重采样 8×8)**、**'api' (Windows API)** 之一，不指定这个选项时视为指定了 'auto'。
  
  'auto' 在当前版本中会自动选择 'api'。
  
  'res4' 或 'res8' 会以数倍大小 (4×4 或 8×8) 绘制文字，再对其进行缩小来实现抗锯齿。res4 比 res8 更快，但精度较低。
  
  'api' 使用 GetGlyphOutline API 绘制抗锯齿文字，但这个 API 似乎有很多不方便之处，根据环境不同可能无法正常绘制。
- **-**jpegdec** (JPEG 图像解码精度)**  
  JPEG 图像解码 (解压) 精度的设置。
  
  可设置的值是 **'high' (高)**、**'normal' (标准)**、**'low' (低)** 之一，不指定这个选项时视为指定了 'normal'。
  
  指定 'high' 会使解码变慢，但画质变高。指定 'low' 会使解码变快，但画质变低。不过在观感上几乎没有区别。
- **-**drawthread** (绘制线程数)**  
  绘制处理时使用的线程数量的设置。
  
  可设置的值是**任意数值**或 **'auto' (自动)** 之一，不指定这个选项时视为指定了 '1'。
  
  指定 'auto' 时，会自动分配与 OS 识别到的处理器数量相同数量的线程。
  
  设置多个绘制线程可能可以提升多核环境下的绘制性能，但反之也可能导致性能下降。
  
  应用于绘制面积较大的处理、Affine 系的高负载处理、运算较重的图层合成处理等时，可能可以获得良好的结果。
  
  即使设置为使用多线程，如果系统判断绘制处理的负载较轻、无法获得多线程化的效果，也可能不会以多线程执行。
- **-**bitmapallocator** (位图内存分配方式 Ver 1.1 以后)**  
  指定如何分配位图用的内存。
  
  可设置的值是 **'globalalloc' (用 GlobalAlloc 分配)**、**'separateheap' (使用分离堆)**、**'malloc' (使用 malloc)** 之一，不指定这个选项时视为指定了 'globalalloc'。
  
  使用 separateheap 可以减轻内存碎片化，可能可以规避内存不足错误的问题。
- **-**bitmapheapsize** (初始分离堆大小 Ver 1.1 以后)**  
  指定在位图内存分配方式中选择使用分离堆时的初始大小。
  
  可设置的值是 **'auto' (自动 (推荐))**、**'0' (自动扩展)**、**'64' (64MB)**、**'128' (128MB)**、**'256' (256MB)**、**'512' (512MB)**、**'1024' (1024MB)**、**'2048' (2048MB)** 之一，不指定这个选项时视为指定了 'auto'。
  
  通常用 auto 即可，但调整初始值可以减轻内存碎片化，可能可以规避内存不足错误的问题。
- **-**drawdevice** (启动时的 DrawDevice 选择)**  
  选择启动时使用的默认 DrawDevice。可选的值因构建而异。
  
  SDL3 构建:
  
    - **'sdl'**: 经 SDL_Renderer 的 [SDLDrawDevice](../reference/SDLDrawDevice.md) ( backend 自动选择 )
    - **'sdlogl'**: OpenGL ES 直接版 ( 经 PBO、不支持 Canvas 的纯粹版 ) ( 仅 `TVP_USE_OPENGL=ON` 时 )
    - **'ogl'**: 包含 OpenGL ES + Canvas / Texture / Shader / Offscreen 的全功能版 [OGLDrawDevice](../reference/OGLDrawDevice.md) ( 仅 `TVP_USE_OPENGL=ON` 时 )
  
  未指定时，`TVP_USE_OPENGL=ON` 构建选择 `sdlogl`，其他情况选择 `sdl`。
  
  Windows 原生 ( WINVER ) 构建:
  
    - **'basic'**: Direct3D 11 的 [BasicDrawDevice](../reference/Window.BasicDrawDevice.md) ( 默认 )
    - **'ogl'**: [OGLDrawDevice](../reference/OGLDrawDevice.md) ( 仅 `TVP_USE_OPENGL=ON` 时 )
    - **'null'**: 不进行绘制的 NullDrawDevice ( 验证用 )
  
  未指定时为 `basic`。无论哪种构建，指定未知的值都会输出警告并回退到默认值。
  
  这是**启动时的默认值**指定，运行中向 [Window.drawDevice](../reference/Window.md#drawdevice) 赋值来切换仍可照常进行。不过 **以 'sdl' 启动 SDL3 构建时，无法在运行中切换到 OpenGL 系 ( sdlogl / ogl )** ( OpenGL 初始化无法通过 )。想使用 OpenGL 功能 ( Canvas 等 ) 时，请从一开始就以 'sdlogl' / 'ogl' 启动。
  
  使用 OpenGL 系的 DrawDevice 需要可以利用 OpenGL ES 的环境。WINVER 始终经 EGL ( ANGLE 的 libEGL.dll / libGLESv2.dll )，因此必须附带 DLL；在 SDL3 的 Windows 中，会优先使用 OS 的 OpenGL 驱动的 ES profile，无法使用时回退到同样的 ANGLE DLL ( 参见下述 -forceegl )。
- **-**renderer** (SDL3 backend 的显式指定 / SDL3 构建限定)**  
  显式指定 SDLDrawDevice 所使用的 SDL_Renderer 的 backend 名。
  ( 例: `direct3d11`、`vulkan`、`opengl`、`software` 等 )。
  
  未指定时会交给 SDL3 自动选择。
  
  仅在 SDL3 构建 + 使用 SDLDrawDevice ( = 指定 `-drawdevice=sdl` 时 ) 时有意义。
- **-**forceegl** (OpenGL ES 上下文的 EGL 强制 / SDL3 构建限定)**  
  让 OpenGL ES 上下文从一开始就用 EGL ( Windows 下为 ANGLE 的 libEGL.dll / libGLESv2.dll ) 创建。
  
  可设置的值是 **'no' (默认，不强制)** 或 **'yes' (强制 EGL)**。
  
  SDL3 构建默认在图形驱动的 OpenGL 实现支持 ES profile ( `WGL_EXT_create_context_es2_profile` ) 时优先使用它，不支持时才回退到 EGL。在驱动的 ES profile 实现有问题、绘制混乱或初始化失败的环境中，指定 'yes' 可以固定为经 EGL ( ANGLE )，从而进行排查与规避 ( 内部会设置 SDL 的提示 `SDL_OPENGL_ES_DRIVER=1`。同名的环境变量也可以获得相同的效果 )。
  
  上下文的请求版本为 ES 3.2，无法创建时会自动降到 3.1 → 3.0 → 2.0 重试 ( ANGLE 的 D3D11 后端只到 ES 3.0/3.1，因此经 EGL 时会通过这个重试成立 )。实际获得的版本可以通过启动日志中的 `Loaded GLES x.y` 确认。
  
  WINVER 构建的 OpenGL 始终经 EGL ( ANGLE )，因此这个选项仅在 SDL3 构建中有意义。
- **-**mediaengine** (视频的硬件解码 / Windows 限定)**  
  指定在 [VideoOverlay](../reference/VideoOverlay.md) 的叠加播放 ( `vomOverlay` ) 中，
  是否用 Media Foundation ( IMFMediaEngine ) 对 mp4/H.264/HEVC/wmv/asf 等 MF-native 格式
  进行硬件解码。
  
  可设置的值是 **'yes' (默认，使用硬件解码)** 或
  **'no' / 'off' / 'false' / '0' (不使用)**。指定 'no' 后所有格式都会
  变为软件解码 ( MF SourceReader / pl_mpeg / movie-player )。
  
  webm ( VP8/VP9 ) 和 mpeg ( MPEG-1 ) 在 Media Foundation 中没有解码器，因此无论这个
  设置如何都始终为软件解码。另外 `vomMixer` 模式 ( 追加图像合成 ) 始终
  为软件合成路径 ( 参见 [VideoOverlay](../reference/VideoOverlay.md) 的
  `mode` 属性 )。

## CPU 功能相关选项

以下选项的可设置值全部是 **'yes' (可以使用时使用)**、**'no' (即使可以使用也不使用)**、**'force' (强制使用)** 之一，不指定选项时视为指定了 'yes'。

发生 CPU 识别问题时，设为 'no' 就不会使用该功能。

'force' 即使检测不到该 CPU 功能也会强制使用，但 CPU 没有该功能时当然无法正常运行。

除此之外，对 -**cpusimd** 指定 **'no'** 会禁用所有已检测到的 SIMD 功能，仅以 C 实现运行 ( 这个选项只能指定 'no' )。用于定位 SIMD 实现与 C 实现的差异。

吉里吉里引擎本体在图像运算等中会在运行时判定并分别使用 MMX / SSE ~ SSE4.2 / AVX / AVX2 / FMA3 ( x86 系 ) 与 NEON / ASIMD ( ARM 系 )，因此相应的选项分别会起作用。OggVorbis / opus 的解码器已成为引擎本体内置，因此不需要像旧 wuvorbis.dll 那样针对外部解码器的指定。其他 (第三方) 插件中也可能有受 CPU 功能设置影响的。

- -**cpummx** (MMX)
- -**cpu3dn** (3DNow!)
- -**cpusse** (SSE)
- -**cpucmov** (CMOVcc)
- -**cpue3dn** (Enhanced 3DNow!)
- -**cpuemmx** (EMMX (MMX2))
- -**cpusse2** (SSE2)
- -**cpusse3** (SSE3)
- -**cpussse3** (SSSE3)
- -**cpusse41** (SSE4.1)
- -**cpusse42** (SSE4.2)
- -**cpusse4a** (SSE4a)
- -**cpuavx** (AVX)
- -**cpuavx2** (AVX2)
- -**cpufma3** (FMA3)
- -**cpuaes** (AES)
- -**cpuneon** (NEON / ARM 构建限定)
- -**cpuasimd** (ASIMD / ARM64 构建限定)

## 调试相关选项

- **-**debug** (调试模式)**  
  设置是否让吉里吉里以调试模式 ( → [Debug](Debug.md) ) 运行。
  
  可设置的值是 **'no' (禁用)**、**'yes' (启用)** 之一，不指定这个选项时视为指定了 'no'。
  
  启用后，吉里吉里会以调试模式运行，一些调试支持功能会被启用，但执行速度会比普通模式慢。
- **-**forcelog** (向文件输出日志)**  
  设置是否把控制台的日志输出到文件。
  
  可设置的值是 **'no' (不输出)**、**'yes' (追加输出到既有文件)**、**'clear' (清除既有文件后再输出)** 之一，不指定这个选项时视为指定了 'no'。
- **-**logerror** (出错时向文件输出日志)**  
  设置出错时是否把控制台的日志输出到文件。
  
  可设置的值是 **'no' (不输出)**、**'yes' (追加输出到既有文件)**、**'clear' (清除既有文件后再输出)** 之一，不指定这个选项时视为指定了 'yes'。
- **-**loglevel** (日志输出级别)**  
  覆盖启动时的日志输出级别。
  
  可设置的值是 **'debug'**、**'info'**、**'warning'**、**'error'**、**'off'** 之一 ( 不区分大小写 )。仅输出指定级别以上的日志。
  
  不指定时的默认值：`MASTER` 构建为 `warning`，其他 Release 构建为 `info`，Debug 构建为 `debug`。用于在发布二进制中临时采集详细日志。
- **-**repl** (启用交互式 TJS shell / 面向 `KRKRZ_REPL` 构建)**  
  在启动时启用交互式 TJS REPL ( Read-Eval-Print Loop )。
  
  可设置的值是 **'yes'**、**'1'**、**'on'**、**'true'** ( 启用 ) 或省略值 ( 启用 )、**'no'**、**'0'**、**'off'**、**'false'** ( 禁用 )。不指定则禁用。
  
  进一步指定以下值时，会切换控制台的打开方式或显示形态 ( 均同时启用 )。
  
  - **'new'** ( 别名 **'window'** / **'separate'** ) : 不附加到父控制台或继承来的控制台，必定在新的控制台窗口中打开。从终端或其他应用启动时也不会混进启动来源的控制台。
  
  另外，本 exe 是 GUI ( windowed ) subsystem，因此运行中确保的控制台不管“默认终端应用”设置如何都会是 conhost ( 无法搭载到 Windows Terminal 上 )。希望不受终端限制进行操作时，下述 `-replweb` (浏览器查看器) 很方便。
  
  关于 REPL 的操作方法以及 `.help` 等特殊命令的详细内容，请参照 [REPL 指南](../topics/core/repl.md)。用 `KRKRZ_REPL=OFF` 构建的 exe 中会被忽略。
- **-**replfile** (启用 REPL 文件通道 / 面向 `KRKRZ_REPL` 构建)**  
  为外部 agent / 自动测试启用不经由控制台、而是经由文件接收 REPL 命令的通道。可以经由指定目录内的输入输出文件执行 TJS 表达式。
  
  可设置的值以字符串指定通信用的目录路径。指定 **'no'**、**'0'**、**'off'**、**'false'**、空字符串 则禁用 ( 默认 )。
  
  可以与 `-repl` ( 控制台版 ) 独立启动，也可以两者同时使用。详细内容请参照 [REPL 指南](../topics/core/repl.md)。
- **-**replsocket** (启用 REPL socket 通道 / `KRKRZ_REPL` 构建 + Linux 系限定)**  
  启用经 abstract namespace 的 Unix 域套接字接收 REPL 命令的通道。接收 1 行 = 1 条命令 ( TJS 表达式 )，并以 1 行 JSON 响应。
  
  可设置的值以字符串指定套接字名。也可以用环境变量 `KRKRZ_REPL_SOCKET` 指定。
  
  可以与 `-repl` / `-replfile` 独立启动，也可以同时使用。Linux 系以外的构建中会被忽略。详细内容请参照 [REPL 指南](../topics/core/repl.md)。
- **-**replweb** (启用浏览器 REPL 查看器 / 面向 `KRKRZ_REPL_WEB` 构建)**  
  搭建轻量的 HTTP + SSE 服务器，可以从浏览器以 上=日志 / 下=输入 的方式操作 REPL。不受终端 ( conhost ) 限制，文本选择、复制、粘贴、滚动、搜索都由浏览器原生支持。
  
  可设置的值是 `[主机:]端口`。例: `-replweb=8899` ( `http://127.0.0.1:8899/` )。默认绑定为 **127.0.0.1 ( 仅本地 )**。像 `-replweb=0.0.0.0:8899` 这样指定会绑定到所有网络接口，可以**从其他机器的浏览器连接** ( devkit / LAN 用途。会暴露到网络上，因此仅在可信环境中使用 )。在 macOS / iOS / Linux 中，指定所有接口 ( `0.0.0.0` / `*` / `::` ) 时会同时在 IPv6 和 IPv4 上监听 ( 为了从只能通过 IPv6 的 iOS 实机 USB 连接 ( `<设备名>.coredevice.local` ) 用开发 Mac 打开。IPv6 不可用时仅 IPv4 )。用 `no` / `0` / `off` / `false` 禁用。
  
  实现同时支持 WIN32 ( Winsock ) / POSIX 套接字，可以与 `-repl` / `-replfile` / `-replsocket` 独立、同时启动。详细内容请参照 [控制台](Console.md#replweb)。
- **-**replwebidle** (浏览器关闭后应用也结束前的秒数)**  
  在 `-replweb` 的 SSE 订阅**一条都没有的状态持续指定秒数后结束应用**。在把浏览器作为 UI 的构成中，防止窗口关闭了却只剩本体继续残留。
  
  **默认启用 ( 5 秒 )**。用 `-replwebidle=no` / `off` / `0` 禁用，用 `-replwebidle=<秒>` 更改秒数。
  
  **一旦有过订阅才会武装**，因此不打开浏览器的 agent 驱动，或把 `-replweb` 仅作为 API 使用而不打开浏览器时，会保持订阅为零，即使默认启用也不会结束。打开多个标签页时，在关闭最后一张之前不会结束。
  
  关闭页面时浏览器会发来关闭信号 ( `POST /bye` )，因此通常 2 秒左右就会结束。信号未能送达时 ( 崩溃等 ) 检测断开需要 SSE 心跳的时间，最多会比指定秒数晚大约 2 倍。
- **-**replwatchfile** (监视表达式的保存位置)**  
  REPL 的监视表达式 ( `.watch` / 浏览器 UI 的 Watch 标签页 ) 会把**表达式列表与自动更新间隔保存到当前目录的 `.krkrz_watch`**，并在下次启动时读回 ( 与 REPL 历史 `.krkrz_history` 同一风格 )。只有添加 / 删除 / 编辑表达式或更改间隔时才会写回。
  
  可以用 `-replwatchfile=<path>` 更改保存位置，用 `-replwatchfile=no` / `off` / `0` 禁用持久化。在无法写入的位置会默默放弃 ( 不会因无法保存而让应用停止 )。
- **-**replwebpad** (允许从浏览器 Pad 保存的目录)**  
  这是 `-replweb` 的浏览器 UI“Pad”标签页 ( 脚本编辑器 ) 中**允许 [保存] 的存储路径前缀**。例: `-replwebpad=work` 时只能写入 `work/` 之下。
  
  **默认禁止写入** ( 保存会返回 403 )。读取随时都可以。前缀比较时会在内部补上末尾的 `/`，因此 `-replwebpad=work` 不会命中 `work_other/...`。
  
  ⚠ **这不是安全边界**。打开 `-replweb` 时点起就可以从浏览器执行任意 TJS，进程的全部权限都是敞开的。请把它视为防止“不小心按下 UI 的 [保存] 而覆盖素材”的栅栏。向网络开放 ( `-replweb=0.0.0.0:...` ) 时，请仅在可信环境中使用。
- **-**replwebopen** (与 `-replweb` 一起打开浏览器)**  
  默认仅在“回环绑定 且 无控制台 ( GUI 启动 )”时才会以应用模式自动打开浏览器。**从终端启动时不会打开** ( 因为如果有终端可以自己打开，而且不打扰 CI / agent 驱动 )。这个选项显式覆盖该默认行为。
  
  | 值 | 行为 |
  |---|---|
  | `app` ( 省略值也相同 ) | 应用模式 ( Edge / Chrome 的 `--app`。无边框窗口 ) |
  | `tab` / `yes` | 默认浏览器的普通窗口 |
  | `no` / `off` | 不打开 ( 自动打开也抑制 ) |
  
  想**从终端启动的同时也打开浏览器**时，使用 `-replwebopen=app`。从 TJS 也可以用 `WebServer.openBrowser(url, appMode)` 打开。
- **-**replmodaltimeout** (REPL 模态响应等待的超时秒数)**  
  REPL 运行中时，`System.inputString` / `System.confirm` / 文件选择等模态会变为等待 modal 响应通道 ( agent 响应 ) 而不是原生对话框。在响应没有到来而超过指定秒数时，会抛出可 catch 的异常并传播给调用方，防止无限等待。
  
  默认为 **30** ( 秒 )。指定 **0** 则无限等待 ( 以往行为 )。
- **-**memoverlay** (内存状态叠加显示)**  
  启用从启动时起在画面右上角实时显示引擎内存状态 ( File / Bitmap / Sound / Krkrz / SDL 各分配器的使用量与进程 RSS / VSize 等 ) 的覆盖层。
  
  可设置的值是 **'1' (启用)**、**'0' (禁用)** 之一，不指定这个选项时视为指定了 '0'。
  
  运行中的动态切换可以通过 [System.setMemoryOverlay](../reference/System.md#setmemoryoverlay) 或 REPL 的 `.memoverlay` 进行。选项本身在所有构建中有效，但进行绘制的是 OGL 系 DrawDevice ( `OGLDrawDevice` / `SDLOGLDrawDevice` ) 和 SDL 的 `SDLDrawDevice`。WINVER 默认的 `BasicDrawDevice` (D3D11) 没有绘制钩子因此不会显示，但**在 WINVER 中只要把 drawDevice 切换到 OGL 系也会显示**。
- **-**padoverlay** (手柄状态叠加显示)**  
  启用从启动时起在画面左上角实时显示游戏手柄的 16 按钮矩阵与 6 轴模拟值的覆盖层。
  
  可设置的值是 **'1' (启用)**、**'0' (禁用)** 之一，不指定这个选项时视为指定了 '0'。
  
  运行中的动态切换可以通过 [System.setPadOverlay](../reference/System.md#setpadoverlay) 或 REPL 的 `.padoverlay` 进行。选项本身在所有构建中有效，但进行绘制的是 OGL 系 DrawDevice ( `OGLDrawDevice` / `SDLOGLDrawDevice` ) 和 SDL 的 `SDLDrawDevice`。WINVER 默认的 `BasicDrawDevice` (D3D11) 没有绘制钩子因此不会显示，但**在 WINVER 中只要把 drawDevice 切换到 OGL 系也会显示**。
- **-**drawstatslog** (DrawStats 的周期日志输出 / SDL3、LIB 构建限定)**  
  在 `KRKRZ_DRAW_STATS=ON` 构建且 MemoryOverlay 显示中时，每 500ms 把 DrawThreadPool 利用统计输出到日志 ( 用于实机等画面显示流动太快无法阅读的场合 )。
  
  可设置的值是 **'1' (启用)**、**'0' (禁用)** 之一，不指定这个选项时视为指定了 '0'。运行中的动态切换也可以通过 [System.setDrawStatsLog](../reference/System.md#setdrawstatslog) 进行。
  
  在 `KRKRZ_DRAW_STATS=OFF` 构建中只会置起标志，不会有任何反应。
- **-**memstatinterval** (内存统计的周期转储)**  
  指定正整数后，每经过该秒数就会把相当于 `System.dumpHeap` 的内存统计输出到日志。
  
  默认值为 0 ( 禁用 )。指定较短的周期 ( 1 ~ 数秒 ) 对日志量和性能影响很大，因此仅在调查时使用。用 `KRKRZ_ENABLE_PERIODIC_DUMP=OFF` 构建时会被忽略。
- **-**memstatonexit** (结束时的内存统计转储)**  
  可设置的值是 **'1' (启用)**、**'0' (禁用)** 之一，指定启用时会在引擎结束时转储一次内存统计。默认值为 '0'。
  
  用 `KRKRZ_ENABLE_PERIODIC_DUMP=OFF` 构建时会被忽略。
- **-**memstatsite** (按分配调用方汇总)**  
  指定 **'yes'** 或栈深度 (1~32) 后，会为每次分配获取栈，按调用方统计存活的分配。'yes' 为 16 层。结果会输出到 `.memdump` 的末尾和 REPL 的 `.memsites` 日志中。
  
  仅在 `KRKRZ_ENABLE_MEMSTAT_DETAIL=ON` 的 Windows 构建中有效，其他情况会被忽略。因为处理会相当慢，所以仅在调查时使用。详细内容请参照 [内存观测、泄漏调查](../topics/core/memory_observation.md)。
- **-**cachelistonexit** (结束时的缓存列表转储)**  
  在引擎结束时把 Storages 的 file 层 / decode 层缓存条目列表转储到日志。用于调查结束前缓存中残留了什么。
  
  可设置的值是以下之一:
  
    - **'1' / 'all'**: file 层 + decode 层两者
    - **'file'**: 仅 file 层
    - **'image'**: 仅 decode 层
    - **'0' / 'none'**: 禁用 ( 默认 )
  
  想在运行中查看列表时，请利用 [Storages.dumpFileCacheList](../reference/Storages.md#dumpfilecachelist) / [Storages.dumpImageCacheList](../reference/Storages.md#dumpimagecachelist)。
- **-**textencodingwarn** (文本编码自动回退的警告显示)**  
  当无法把没有 BOM 的文本文件按默认编码 ( 通常为 UTF-8，`KRKRZ_USE_SJIS` 构建中为 Shift_JIS ) 解释时，引擎会尝试用另一种编码重新解释 ( 自动回退 )。这个选项设置发生该回退时是否把对象文件名输出到 warning 日志。
  
  可设置的值是 **'1' (输出)**、**'0' (不输出)** 之一，不指定这个选项时视为指定了 '0'。
  
  编码混杂的项目中日志会被填满，因此默认不输出。调查乱码原因时请启用。
- **-**navlog** (Elements 对话框的导航诊断日志)**  
  把 Elements 对话框 ( → [ElementsDialog](../reference/ElementsDialog.md) ) 的焦点移动、cursor-warp ( 把光标飞到焦点目标的处理 )、手柄方向键的到达，带启动以来的经过毫秒数输出到日志。用于定位方向键长按期间说明文字与高亮错位这类输入与导航的时机偏差。
  
  这个选项**只要指定就有效**，不看值 ( 不指定则禁用 )。引擎侧与 elements_modal 侧的日志会同时启用。
  
  启用时，对于呈现花了 100ms 以上的帧还会输出 `slow frame` 行。明细的阶段与 [ElementsDialog.renderStats](../reference/ElementsDialog.md#renderstats) 相同，为 update / raster / acquire / upload / present，可用于定位卡在哪个阶段。
  
  日志量很大，输出本身会影响处理时间，因此请仅在调查时使用。

- **-**ignoremouse** (丢弃真实鼠标输入 / 用于运行测试)**  
  设为真后会**丢弃所有真实鼠标输入**，只放行从 [Agent](../reference/Agent.md) 注入的输入。这是为了在自动测试中建立“输入全部由 Agent 发出”的前提。即使人不小心动了指针，也不会污染测定。
  
  可设置的值是 **'yes' (启用)**、**'no' (禁用)** 之一，不指定这个选项则禁用。运行中的切换可以通过 [Agent.ignoreRealMouse](../reference/Agent.md#ignorerealmouse) 进行。
  
  hover 判定和光标参照会查看**虚拟光标位置**，该位置会因 Agent 的注入而更新，因此启用后悬停和焦点仍能照常工作 ( 设计见 `src/core/doc/VirtualCursor.md` )。
  
  ⚠ 启用后**将无法用人手进行鼠标操作**。在不持有 `Agent` 的构建 ( `MASTER` 等 ) 中会被忽略。

## 系统兼容性相关选项

- **-**arcdelim** (归档分隔符)**  
  指定归档分隔符 ( 分隔归档存储名与归档内存储名的字符 )。
  
  可设置的值是 **'>' (使用 '>')**、**'#' (使用 '#')** 之一，不指定这个选项时视为指定了 '>'。
  
  归档分隔符在吉里吉里 2 2.19 beta 14 中，从以往的 '#' 变更为 '>'。
  
  在低于 2.19 beta 14 的版本上运行的应用程序可能会因这个变更而无法运行，但通过这个选项把分隔符改为 '#' 就可以使其运行。
- **-**evalcontext** (后置'!'运算符的行为)**  
  指定 TJS2 的后置'!'运算符的行为。
  
  可设置的值是 **'this' (在 this 上求值表达式)**、**'global' (在 global 上求值表达式)** 之一，不指定这个选项时视为指定了 'this'。
  
  TJS2 的后置'!'运算符原本在 global 上下文上执行表达式，从 2.21 beta 9 起改为在 this 上下文上执行。
  
  以低于 2.21 beta 9 的版本为前提的应用程序，如果不把这个设置改为“在 global 上求值表达式”，可能无法运行。
- **-**holdalpha** (Layer.holdAlpha 属性的默认值)**  
  指定 [Layer.holdAlpha](../reference/Layer.md#holdalpha) 属性的默认值。
  
  可设置的值是 **'false' (假)**、**'true' (真)** 之一，不指定这个选项时视为指定了 'false'。
  
  在吉里吉里 2 2.23 beta 4 中，原本在各种运算函数中指定的 hda (是否保护 alpha 通道) 选项被取消，取而代之创建了 Layer.holdAlpha 属性。此时 Layer.holdAlpha 的默认值为真。Layer.holdAlpha 为真时不会影响过去应用程序的行为。
  
  在吉里吉里 2 2.23 beta 5 中，这个默认值变为假。想让以低于吉里吉里 2 2.23 beta 5 的版本为前提的应用程序运行时，如果不把这个选项指定为“真”，可能无法正常运行。
- **-**unaryaster** (前置'*'运算符的行为)**  
  指定 TJS2 的前置'*'运算符的行为。
  
  可设置的值是 **'default' (2.25 以后的行为)**、**'compat' (低于 2.25 的行为)** 之一，不指定这个选项时视为指定了 'default'。
  
  TJS2 的前置'*'运算符原本是不经由属性处理器直接取出属性对象本身的运算符，但从 2.25 beta 1 起，具有该功能的运算符变为前置'&'，前置'*'运算符则变成了用于让属性对象的属性处理器工作的运算符。以低于 2.25 beta 1 的版本为前提的应用程序，如果不把这个设置改为“与低于 2.25 的版本兼容”，可能无法正常运行。
- **-**lazyarraymember** (Array 方法的持有方式)**  
  可设置的值是 **'no' (以往的行为)**、**'yes' (从类中获取)** 之一，不指定这个选项时视为指定了 'no'。
  
  以往每创建一个 Array 对象都会把 Array 类的方法和属性 (add、count 等) 复制为各实例的成员，因此即使是空数组每个也要使用数 KB。改为 'yes' 后，不再向实例复制，而是对实例自身成员中不存在的名称从类中获取，并绑定到该实例使用。在大量创建数组的脚本中，内存使用量和生成时间会大幅减少。
  
  在实例上设置了同名成员时，仍然优先使用它。区别在于，删除设置在实例上的方法后，以往该方法就消失了，而 'yes' 时则会调用类的方法。继承 Array 的脚本类的实例仍然照常复制。
- **-**wsvolfactor** (音量曲线)**  
  可设置的值是 **'3322' (2.31 2011/6/14 以后的行为)**、**'5000' (2.31 2011/6/14 之前的行为)** 之一，不指定这个选项时视为指定了 '3322'。
  
  音量曲线从 2.31 2011/6/14 起变为更直观的曲线。
- **-**readencoding** (脚本读取字符编码)**  
  可设置的值是 **'Shift_JIS' (吉里吉里 2 兼容的行为)**、**'UTF-8' (吉里吉里Z 的行为)** 之一，不指定这个选项时视为指定了 'UTF-8'。
  
  这是读取脚本时使用的字符编码。
- **-**ignoretouch** (触摸事件的禁用 1.3.0 以后)**  
  可设置的值是 **'false' (假)**、**'true' (真)** 之一，不指定这个选项时视为指定了 'false'。
  
  指定 'true' 会禁用触摸事件，改为发生鼠标事件。
