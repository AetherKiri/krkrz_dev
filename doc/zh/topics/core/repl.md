# REPL (Read-Eval-Print Loop)

给以 `KRKRZ_REPL=ON` 构建的二进制文件附上命令行参数 `-repl`
( 或 `-repl=yes` ) 启动后，交互式 TJS shell 就会变为可用。
支持 Windows / macOS / Linux。行编辑
使用 [icline](https://github.com/deths74r/icline) ( isocline fork )。

详细规格 ( 命令列表、编辑功能、故障排查 ) 请参照
src/core 侧的指南:

- [doc/REPL.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)

---

## 启动

```bash
krkrz -repl data/      # SDL 版
krkrz64 -repl data/    # Win32 版 (親コンソールに AttachConsole)
```

没有 `-repl` 时 REPL 不会启动 ( 没有 TTY 自动判定 )。
也可以用 `-repl=no` / `-repl=off` / `-repl=false` / `-repl=0` 显式禁用。

以 `KRKRZ_REPL_LINE_EDIT=OFF` 构建即可得到无 icline 依赖的最小模式
( 方向键等行编辑功能无效 )。

### 选项列表

REPL 相关选项集中在此处 ( 详情见各节，格式见
[命令行选项](../../guide/CommandLine.md) )。各选项相互独立，
可以同时指定。

| 选项 | 默认 | 内容 |
|---|---|---|
| `-repl[=yes\|no\|new]` | 禁用 | 控制台 REPL。`new` 强制新建控制台 |
| `-replfile=<dir>` | 禁用 | 文件通道 ( **agent 驱动的主力** ) |
| `-replsocket=<name>` | 禁用 | abstract unix socket 通道 ( Linux 系 ) |
| `-replweb[=[host:]port]` | 禁用 | HTTP + SSE 服务器 + 浏览器 UI ( 默认 127.0.0.1:8899 ) |
| `-replwebopen=app\|tab\|no` | 条件性自动 | 浏览器的自动打开。**从终端启动时默认不打开** |
| `-replwebidle=<秒>\|no` | **5 秒** | 浏览器消失后到退出为止 |
| `-replwebpad=<dir>` | 禁止写入 | 允许 Pad 标签页 [保存] 的存储路径前缀 |
| `-replwatchfile=<path>\|no` | `.krkrz_watch` | 监视表达式列表的保存位置 |
| `-replmodaltimeout=<秒>` | 30 | 等待模态响应的超时 ( 0 = 无限 ) |

`-nostartup` ( 不执行 startup.tjs ) 与 `-loglevel=` 并非 REPL 专用，
但在 agent 驱动中经常并用。

---

## 主要的特殊命令

提示符是 `krkrz>`，继续行是 `...`。可以直接输入 TJS 的表达式和语句，
历史会保存到 `.krkrz_history`。

| 命令 | 说明 |
|---|---|
| `exit` / `quit` / `Ctrl+D` | 退出 REPL 并结束应用 |
| `.help` | 显示帮助 |
| `.clear` | 清除继续输入中的缓冲区 |
| `.depth [N]` | 显示 / 设置结果显示的展开深度 |
| `.compact [on\|off]` | 切换结果显示的精简模式 |
| `.mem` | 分配器 + 进程内存的一行摘要 |
| `.memdump` | 把详细内存统计转储到日志 |
| `.memsites [N] [函数名]` | 按调用方把存活分配的前 N 条转储到日志 ( 诊断构建 + 启动时 `-memstatsite`。传入函数名时仅限包含该函数的调用链 ) |
| `.memoverlay [on\|off]` | 切换画面覆盖层 ( SDL3 构建 ) |
| `.mempeakclear` | 把 peak 计测值重新对齐到 current_used |
| `.sysalloc` | 一行显示系统分配器信息 ( 空闲 / 可分配 / RSS ) |
| `.padoverlay [on\|off]` | 切换手柄覆盖层 ( SDL3 构建 ) |
| `.filecache` | 把 StorageCache ( file 层 ) 全部条目转储到日志 |
| `.imagecache` | 把 TVPGraphicCache ( decode 层 ) 全部条目转储到日志 |
| `.cap [path]` | 把下一帧的实际画面 ( 含 overlay ) 保存为 PNG |
| `.dlg` | 活动对话框列表 |
| `.dlgclose` | 关闭最前面的对话框 |
| `.click X Y` | 向 (X,Y) 注入鼠标点击 ( `Agent.click` ) |
| `.watch` | 以 `id: 表达式 = 值` 显示监视表达式列表 ( 显示前先对全部条目求值 ) |
| `.watch add EXPR` | 添加监视表达式并立即求值 |
| `.watch rm ID` / `.watch rm all` | 删除监视表达式 / 全部清除 |
| `.watch edit ID EXPR` | 替换监视表达式 |
| `.watch auto [ms\|on\|off]` | 显示 / 设置自动更新的间隔 ( `on` = 500ms，`0` = 每帧，下限 100ms ) |
| `.event [on\|off\|toggle]` | 显示 / 切换 `System.eventDisabled` |

内存系命令的详情请参照 [内存观测指南](memory_observation.md)，
手柄覆盖层的详情请参照 [PadOverlay](pad_overlay.md)。

`.watch` 相当于吉里吉里2 引擎本体内置的调试窗口“监视表达式”。
预先注册表达式后，每次执行 `.watch` ( 或按自动更新的间隔 ) 都会统一
求值并列出表达式与值。求值上下文固定为 global，即使表达式抛出异常，
也只是把 `(error) <消息>` **作为值**显示，因此即使有 1 条监视表达式
损坏，REPL 和应用都不会死。

表达式列表与自动更新间隔**保存到当前目录的 `.krkrz_watch`**，
下次启动时读回 ( 用 `-replwatchfile=<path>` 更改，用 `=no` 禁用 )。

---

## REPL 启动期间的错误处理器行为

通过 `-repl` 或 `-replfile` 启用 REPL 时，未捕获异常不会再让吉里吉里
立即退出。发生异常时不显示原生对话框，只输出带调用栈的日志，
因此可以修正后重新 eval。同样地，`System.inform` 和
`Application::MessageDlg` 的输出目标会被改接到 REPL 控制台
( 只返回默认响应，不弹出对话框 )，因此无头自动测试也不会中断。

并用 `-nostartup` 还可以抑制 startup.tjs 的自动执行，因此可以组织出
无窗口静止启动 → 从 REPL 显式启动处理的流程 ( 详情请参照
[命令行选项](../../guide/CommandLine.md) 的 `-nostartup` )。

---

## 文件通道 ( -replfile )

指定 `-replfile=<dir>` 后，会启动不经由控制台、基于文件的
REPL 通道。外部 agent 向指定目录内的命令文件写入
TJS 表达式，并从响应文件读取结果 JSON
( lockstep )。可以与 `-repl` 独立启用，
也可以同时使用。

```bash
krkrz -replfile=./replbus data/
```

面向无头自动测试，以及从其他进程的 agent 控制 krkrz
的用途。协议详情请参照 src/core 侧的文档。

行首为 `.` 的行会被视为**特殊命令**，与控制台 REPL 相同的输出会
进入响应 JSON 的 `result` ( 可以从 agent 直接调用
`.watch` / `.mem` / `.cap` 等 )。

---

## 浏览器 UI ( -replweb )

`GET /` 返回的内嵌页面是 **Console / Watch 的标签页结构**。

| 标签页 | 内容 |
|---|---|
| Console | 上=日志 / 下=输入 ( 以往的页面 ) |
| Watch | 监视表达式的表 ( 表达式 / 值 ) + 添加、删除、内联编辑 ( 双击 ) + 自动更新间隔 |
| Pad | 脚本编辑器。多行用 Ctrl+Enter 执行，向存储读取 / 保存 |

**可以把项目自有的面板作为标签页加进来** ( `WebServer.registerPanel` )。用自己的
页面通过 `serveStatic` 提供，并把其路径传过去，就会排列在内置标签页的右
侧。内容因为是 iframe，不依赖内置 UI 的内部结构，从面板侧可以在
同源下调用 `/cmd` `/watch` `/pad/exec` 以及自有端点。

```tjs
WebServer.serveStatic("/tool/", "web/");
WebServer.registerPanel("mytool", "案件ツール", "/tool/tool.html");
```

如果整个用自有页面顶替 ( 只用 `serveStatic` )，会失去 Console / Watch / Pad 和
控制器，因此**只是想添加观测面板的话，前面那种方式更合适**。

因为内置于引擎本体，只用 `-replweb` 就能完成 ( 不需要插件和脚本 )。
想替换为自有 UI 时，请使用 `WebServer.serveStatic`。

### 让浏览器 UI 与应用的生命周期保持一致

在以浏览器为 UI 的构成中，**只剩一方存活**是最麻烦的
( 关闭了窗口，引擎本体却还在 / 引擎本体已经结束，却留下 «disconnected» 的
页面 )。两个方向都要关闭。

**引擎本体侧** — 浏览器消失后退出 ( `-replwebidle` )

| 状态 | 行为 |
|---|---|
| 启动～**直到最初的连接到来** | 待机 ( 永不退出 ) |
| 有 1 条以上连接 | 持续运行 |
| 连接全部消失 | `<秒>` 后退出 |

**默认启用 ( 5 秒 )**。用 `-replwebidle=no` 禁用，用 `=<秒>` 指定秒数。
武装的只有 **通过 `-replweb` 启动时**，用 TJS 的 `WebServer.start()`
启动的服务器不会武装 ( 为了不擅自停掉应用自己管理的服务器 )。
由于**一旦有过连接就会武装**，不打开浏览器的 agent 驱动或
作为 API 面的利用不受影响。关闭页面时会发出信号 ( `POST /bye` )，
通常约 2 秒就会退出。

**浏览器侧** — 引擎本体消失后关闭

| 状态 | 行为 |
|---|---|
| 引擎本体通知结束 ( `/sub/state` 的 `exiting` ) | 立即关闭窗口 |
| SSE 断开后 5 秒内未恢复 ( 崩溃等 ) | 关闭窗口 |
| `window.close()` 无效 ( 普通标签页 ) | 全屏显示“吉里吉里Z が終了しました” |

### 显示语言

**默认遵循引擎本体的语言设置** ( `-language=` 和 OS 语言会原样反映，
与引擎的消息变成相同语言 )。也可以用上部的语言选择器当场
切换，选择会记忆在该浏览器中。

目前支持 **日语 / 英语**。引擎本体选择了其他语言 ( 中文等 ) 时，
会以与引擎相同的回退方式回退到英语。

### Pad ( 脚本编辑器 )

编写多行 TJS 后**用 Ctrl+Enter 整体执行** ( 与 `/cmd` 的 1 行执行
不同，可以直接执行函数定义和循环 )。正文会自动保存到浏览器的 `localStorage`，
因此重新加载也不会消失。

可以通过路径栏 + [读取] / [保存] 与存储交互，但**保存默认禁止**。
只有在指定了 `-replwebpad=<dir>` 时，才能写入其之下
( 这是为了“不因不小心按下 UI 的 [保存] 而覆盖素材”的栅栏。
打开 `-replweb` 的时刻就可以执行任意 TJS，因此这并不是安全边界 )。

### 浏览器的自动打开 ( -replwebopen )

默认仅在“回环绑定 且 无控制台 ( GUI 启动 )”时才会以应用
模式打开。**从终端启动时不会打开**。显式指定为
`-replwebopen=app` ( 应用模式 ) / `tab` ( 普通窗口 ) / `no` ( 不打开 )。
从终端启动同时想打开浏览器时，使用 `-replwebopen=app`。

---

## 监视表达式的 HTTP API ( -replweb )

并用 `-replweb` 后，监视表达式也可以从浏览器或 curl 操作。

| 路由 | 说明 |
|---|---|
| `GET /watch` | 列表 + 当前值 ( JSON )。因为**不进行求值**，轮询也安全。用 `?eval=1` 则先求值再返回 |
| `POST /watch` | 操作 ( form-urlencoded )。`op=add&expr=…` / `op=rm&id=…` / `op=edit&id=…&expr=…` / `op=clear` / `op=interval&ms=…` / `op=eval` |
| `GET /sub/watch` | 自动更新的 push ( SSE )。在值发生变化时，以及在不伴随求值的更改 ( 删除 / 全部清除 / 间隔更改 ) 时 |

!!! warning "内置路由先于 register 判定"
    `/` `/events` `/cmd` `/sub/<ch>` `/watch` `/state` `/pad/exec` `/pad/file`
    `/bye` 无法用 [WebServer.register](../../reference/WebServer.md#register) /
    [serveStatic](../../reference/WebServer.md#servestatic) **覆盖**。
    自有端点请使用其他前缀 ( `/api/` `/ui/` 等 )。

```bash
curl -s -X POST -d 'op=add&expr=System.getTickCount()' localhost:8899/watch
curl -s -X POST -d 'op=interval&ms=500'                localhost:8899/watch
curl -N localhost:8899/sub/watch
```

响应与 push 的形式相同。

```json
{"interval":500,"entries":[{"id":1,"expr":"System.getTickCount()","value":"32470","error":false}]}
```

---

## 套接字通道 ( -replsocket / Linux 系限定 )

指定 `-replsocket=<name>` ( 或环境变量 `KRKRZ_REPL_SOCKET` ) 后，
会启动监听 abstract namespace 的 Unix 域套接字的命令通道
( Linux 系构建限定。在其他 OS 上被忽略 )。这是文件通道
的套接字版，接收 1 行 = 1 条命令 ( TJS 表达式 )，在主线程
执行并以 1 行 JSON 响应。可以与 `-repl` / `-replfile` 独立启动，
也可以同时使用。

- 在行末放置 `\` 会被视为继续行，可以在保留换行的同时把多行
  作为 1 条命令执行 ( 这是从 `nc` 等也能使用的、协议层面的续行
  标记 )。
- 单行中行首为 `.` 的内容会被解释为通道侧的 dot 命令
  ( `.help` / `.depth` / `.compact` )。

---

## agent 驱动用的 Agent 类 ( SDL3 构建 )

`KRKRZ_REPL` 构建的 SDL3 版中内置了用于从外部 agent / 自动测试
驱动 krkrz 的 [Agent](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)
TJS 类。与 `System` 类一样以类方法
的形式调用 ( 无需实例化 )。

| 功能 | API ( 主要方法 ) |
|---|---|
| 输入注入 | `Agent.mouseMove / mouseDown / mouseUp / click / wheel`，`Agent.keyDown / keyUp / keyPress`，`Agent.text` |
| 对话框观测 / 控制 | `Agent.dialogs()` / `Agent.dialogTree(index)` / `Agent.dialogClick(index, id)` / `Agent.dialogFocus(index, id)` / `Agent.closeDialog()` / `Agent.closeAllDialogs()` |
| 画面捕获 | `Agent.captureScreen(path[, x, y, w, h])` / `Agent.lastCapture()` |

经由 `Agent` 的输入会通过与真实输入相同的 `TTVPWindowForm::Send*` 路径，
因此既能到达游戏，也能到达 [Dialog](../../reference/ElementsDialog.md)。
`captureScreen` 会在下一帧 present 直前把含 overlay 的实际画面
读回并保存为 PNG ( 即使请求时处于闲置状态，也会在 1 帧后
保存 )。

该类仅在 `KRKRZ_REPL=ON` 的 SDL3 构建中注册。规格的详细
内容 ( 按钮常量、shift 掩码、文件通道的协议等 ) 请
参照 [doc/REPL.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/REPL.md)。
