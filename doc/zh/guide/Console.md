# 控制台

吉里吉里Z (现行版) 中不存在独立的控制台窗口。
从命令行启动时，日志消息会输出到**该终端 (命令行) 上**，
必要时可以启动 REPL 来交互式地求值 TJS 表达式。

## 消息显示

从命令行启动后，吉里吉里系统或用户脚本通过
[Debug.message](../reference/Debug.md#message) 等输出的调试消息会流到
启动它的终端上。显示级别可以通过
[命令行选项](CommandLine.md)的 `-loglevel=` 调整。

Win32 构建是作为 windowed subsystem 制作的，因此从
`cmd.exe` / PowerShell 等启动时，会直接使用父进程的控制台。
SDL 构建是 console subsystem，因此在终端上始终能看到消息。

![](../_assets/Console.png)

## 交互式 shell ( REPL ) { #repl }

对以 `KRKRZ_REPL=ON` 构建的二进制文件附上命令行参数 `-repl`
( 或 `-repl=yes` ) 启动后，即可使用交互式 TJS shell ( REPL )。
支持 Windows / macOS / Linux。

```
krkrz -repl data/        # SDL 版
krkrz64 -repl data/      # Win32 版
```

不附上 `-repl` 时 REPL 不会启动 ( 没有 TTY 自动判定 )。
想显式禁用时，指定 `-repl=no` / `-repl=off` / `-repl=false` /
`-repl=0`。

Win32 ( windowed subsystem ) 版在 REPL 启动时会用 `AttachConsole` 获取父进程
的控制台，如果没有则用 `AllocConsole` 新分配。

#### 强制使用新控制台 ( `-repl=new` )

指定 `-repl=new` ( 别名 `-repl=window` / `-repl=separate` ) 后，不会 attach 到
父级或继承的控制台，而是必定打开**新的控制台窗口**。
适用于想从终端或其他应用启动 GUI，又不希望 REPL 挤入启动来源
控制台的场合。

!!! note "不会显示在 Windows Terminal 中"
    本 exe 是 GUI ( windowed ) subsystem，因此运行中分配的控制台无论
    “默认终端应用”设置如何，也不管是否经由 `wt.exe`，都会是传统的 conhost
    ( 因为 GUI 应用无法加入终端的伪控制台 )。

## 浏览器 REPL 查看器 ( `-replweb` ) { #replweb }

指定 `-replweb=<port>` ( 例 `-replweb=8899` ) 后，会在 `127.0.0.1:<port>` 上
启动轻量的 HTTP + SSE 服务器，**可以从浏览器操作 REPL 与调试窗口**
( 在以 `KRKRZ_REPL_WEB=ON` 构建的情况下默认 ON )。

```
krkrz64 data/ -replweb=8899      # → http://127.0.0.1:8899/ を開く
```

优点是不受控制台 ( conhost ) 的制约，**文本选择、复制、粘贴、
滚动、搜索全部以浏览器原生方式**生效。可以从多个浏览器
( 标签页 ) 同时连接，相同的日志会一起流动。

### 画面构成

上部排列着标签页与控制器。

| 标签页 | 内容 |
|---|---|
| **Console** | 上=日志 / 下=输入。日志按级别着色，可以用过滤器筛选、Clear。输入框可对表达式、语句求值，用 `↑↓` 浏览历史，可使用 `.help` 等特殊命令 |
| **Watch** | **监视表达式**。登录表达式后会并排显示其值，并按指定间隔自动更新。可以添加、删除、双击进行内联编辑 |
| **Pad** | **脚本编辑器**。编写多行 TJS，用 `Ctrl+Enter` 整体执行。也可以向存储读取 / 保存 ( 保存需要下述 `-replwebpad` ) |

右上方的**控制器**相当于吉里吉里2 的控制器窗口。

- **事件** … [System.eventDisabled](../reference/System.md) 的显示与切换。
  即使游戏侧更改，显示也会跟随更新
- **退出** … 结束应用程序

这些是把吉里吉里2 引擎本体内置的调试窗口 ( 控制台 / 控制器 /
监视表达式 / 脚本编辑器 ) 以不依赖平台的形式复活的功能。

### 显示语言

**默认遵循引擎本体的语言设置** ( 会反映 `-language=` 或 OS 语言，与引擎的
消息使用相同语言 )。可以通过上部的语言选择器当场切换，
选择会记忆在该浏览器中。支持日语 / 英语，其他语言设置的
情况下会以与引擎相同的回退方式变为英语。

### 浏览器与应用程序的生命周期

**关闭浏览器后应用也会退出** ( 默认 5 秒。用 `-replwebidle=no` 禁用 )。
这是为了防止把浏览器作为 UI 的构成中只剩下引擎本体一直存活。
**在最初的连接到来之前不会退出**，因此不打开浏览器的 Agent 驱动，或
把 `-replweb` 仅作为 API 面使用的构成不受影响。

反过来，**应用退出时浏览器的页面也会自动关闭**
( 在无法关闭的普通标签页中，会切换为“終了しました”( 已退出 ) 的显示 )。

### 选项

| 选项 | 内容 |
|---|---|
| `-replweb=[主机:]端口` | 监听。默认绑定为 **127.0.0.1** ( 仅本地 )。用 `0.0.0.0:8899` 绑定所有接口 ( 可从另一台机器的浏览器连接。由于会暴露到网络，仅限可信环境 )。用 `no` / `0` / `off` / `false` 禁用 |
| `-replwebopen=app\|tab\|no` | 浏览器的自动打开。默认仅在“回环 且 无控制台 ( GUI 启动 )”时以应用模式打开。**从终端启动时不会打开**，想让它打开时请用 `-replwebopen=app` |
| `-replwebidle=<秒>` | 浏览器消失后到退出为止的秒数 ( 默认 5，用 `no` 禁用 ) |
| `-replwebpad=<dir>` | **允许** Pad 标签页 **[保存]** 的存储路径前缀。默认为禁止写入 |
| `-replwatchfile=<path>` | 监视表达式列表的保存位置 ( 默认是当前的 `.krkrz_watch`，用 `no` 禁用 ) |

详情请参阅[命令行选项](CommandLine.md)。

- 实现同时支持 WIN32 ( Winsock ) / POSIX socket ( 服务器机制不依赖平台。
  在需要初始化各 OS socket 库的环境中，要先进行该初始化 )。
- 与 `-repl` ( 控制台 ) / `-replfile` / `-replsocket` 相互独立，也可以同时启动。
- 当前的 URL 可以从 TJS 通过 [`System.replWebURL`](../reference/System.md) 获取
  ( 未启动时为空字符串 )。
- 也可以从脚本或插件添加自有的端点
  ( [WebServer](../reference/WebServer.md) 类 )。HTTP API 的列表以及
  从浏览器以外 ( curl ) 的调用方法，请参阅
  [REPL ( 交互式 TJS shell )](../topics/core/repl.md)。

## 操作与结果显示 ( 通用 )

以下内容在控制台 / 浏览器 / `-replfile` 的任何前端中都相同。

### 输入

提示符是 `krkrz>`。继续输入中会变为 `...`。
输入 TJS 的表达式或语句并换行后会被求值，显示结果
( 省略 `;` 的表达式也会被求值 )。括号或引号未闭合时
会进入继续输入模式，可以输入多行。
输入历史在控制台 REPL 中会保存到当前目录的 `.krkrz_history`
( 浏览器侧的历史仅存在于页面内，可以用 `↑↓` 追溯 )。

以 `.` 开头的行是**特殊命令** ( 用 `exit` / `quit` / `Ctrl+D` 退出 REPL 并
同时结束应用程序，用 `.help` 查看列表 )。内存观测、画面捕获、监视表达式等
一应俱全，**控制台 / `-replfile` / `-replweb` 三者都可以使用相同的内容**。
列表汇总在 [REPL ( 交互式 TJS shell )](../topics/core/repl.md) 中
( 因为在这里重新刊载的话会只有一方变旧 )。

### 结果显示

求值结果会以与 [Debug.prettyPrint](../reference/Debug.md#prettyprint) 相同的排版
显示。

- `void` → `(void)`、null 对象 → `(null)`
- 数值 / 字符串 / 字节序列 → 以表达式表记原样显示
- 数组 → `[ e1, e2, ... ]` ( compact 时为 `[e1, e2, ...]` )
- 字典 → `%[ "key" => value, ... ]`
- 函数 / 类 / 属性 → `(function)` / `(class)` / `(property)`
- 其他对象 → `(object: 0x...)`
- 达到展开深度时 → `[...]` / `%[...]`
- 循环引用 → `(recursion)`

REPL 运行中，引擎输出的日志会按级别着色
( `VERBOSE`=灰、`DEBUG`=青色、`INFO`=默认、`WARNING`=黄、
`ERROR`=红、`CRITICAL`=粗体红 )，并插在提示符行上方显示。
