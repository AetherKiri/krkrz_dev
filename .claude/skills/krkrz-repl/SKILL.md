---
name: krkrz-repl
description: 吉里吉里Z (krkrz) の SDL3 / WINVER ビルドを REPL 経由でエージェントから駆動するためのリファレンス。krkrz を起動して TJS スクリプトを評価・検証・デバッグする、startup.tjs を介さず明示的に処理を開始する、入力イベント (キー/マウス) を注入する、画面をキャプチャして目視確認する、Elements ダイアログを観測・操作する、例外やダイアログ表示をコンソールで観測する、コアデモ全シーンを自動巡回してキャプチャで表示確認する (-demotest / -demotestcap)、といった場面で使う。**外部エージェントは console(CONIN$) に打てないので -replfile ファイルチャネルが本命**。起動フラグ (-repl / -replfile / -nostartup / -loglevel / -display / -ignoremouse)、ファイルチャネルのプロトコル、Agent API (入力注入 / captureScreen / dialogs / dialogClick)、ドットコマンド (.cap/.dlg/.click/.mem 等)、REPL 駆動時の挙動変更 (例外で即終了しない / inform と例外ダイアログがコンソールに出る) を網羅。TJS2 言語仕様そのものは skill `tjs2`、本体クラス API は skill `krkrz` を参照。中文说明：从外部 agent 通过 REPL（主要是 -replfile 文件通道）驱动 krkrz，进行 TJS 脚本求值、调试、输入注入、屏幕捕获与目视验证时使用。触发词：REPL 驱动、replfile、文件通道、输入注入、屏幕捕获、点命令、截屏验证、调试脚本、Agent API。
---

> **路径基准**：正文中的相对路径以 **engine 根**为基准（krkrz_dev 中需前置 `src/core/`，见下文）。工作目录不是 krkrz_dev（如 krkrz_android / krkrz_ios 等外围仓库或项目文件夹）时，请**前置 `${KRKRZ_BASE}/krkrz_dev/`** 再读取（用 `echo $KRKRZ_BASE` 确认实际路径。每台机器的值不同，因此不要写入绝对路径）。

# krkrz REPL 驱动参考

krkrz SDL3 构建内置了交互式 TJS shell（REPL）（位于 engine 的 `common/utils/REPL.cpp`）。
这是 agent 启动 krkrz 后对脚本进行求值、验证的机制。

## 按仓库构成进行路径替换（先确认）

本技能以 engine 仓库（krkrz.git / krkrz_develop.git）为对象，但检出形态有 2 种，
**只有 engine 源码的路径写法不同**。REPL / Agent 的协议和 TJS 侧用法完全相同。

| 形态 | engine 根 | 例：REPL 实现 | data 默认 | 构建 |
|---|---|---|---|---|
| engine 单仓库（`krkrz` 等） | 仓库根下 | `common/utils/REPL.cpp` | `data/` | `cmake --preset x64-windows` |
| umbrella（`krkrz_dev`） | `src/core/` | `src/core/common/utils/REPL.cpp` | `src/core/data/` | `make`（预设为 `src/core/CMakePresets.json`） |

下文均以 engine 根为基准相对书写（`common/...`、`sdl3/...`、`doc/...`）。
**在 umbrella 中工作的话，请前置 `src/core/` 再阅读**。

**REPL 引擎本体 + `-replfile` 通道在所有桌面变体中有效**（`KRKRZ_REPL`
默认跟随 `KRKRZ_DESKTOP`。WIN32 = ON，因此 **WINVER（`x64-windows-win`）也能用
`-replfile` 进行 TJS eval / 状态确认**）。REPL / 执行队列 / 文件通道都位于
`common/`，与 SDL 无关。**Agent API・captureScreen 也已支持 WINVER**
（2026-07-31）：
- **Agent API** 已统一到 `common/environ/AgentControlIntf.cpp`。输入注入通过
  `AgentInput` seam（`generic/environ/AgentInput.cpp` = SendMouseMessage/SendMessage、
  `win32/environ/AgentInput.cpp` = OnMouse*/OnKey*）做平台分离。SDL3 /
  WINVER 下 `Agent.click` / `keyPress` / `dialogs` / `dialogClick` / `text` 均可使用。
- **screencapture** 也已实现 `BasicDrawDevice::FulfillScreenCapture[FromBackBuffer]`，
  WINVER 下 `System.captureScreen` / `Agent.captureScreen` 可保存含 overlay 的 PNG。

因此 **WINVER 也能像 SDL3 一样进行 GUI 验证（输入注入 + captureScreen 目视确认）**。
仍为 SDL3 专用的只有启动时 UserConfig UI（`-userconf`，需要在游戏窗口生成前创建
独立 OS 窗口）。

## 重要：开工前须知

1. **外部 agent（Claude）驱动 GUI 版 krkrz 时，请使用 `-replfile=<dir>`
   文件通道**。`-repl` 的 console REPL 在 Windows 上读取 `CONIN$`
   （实际控制台），工具无法向其输入。文件通道只需 Write/Read `cmd`/`resp`
   文件即可逐步驱动，还能 Read `captureScreen` 生成的 PNG 做目视确认。
   → 见下文「文件通道驱动」。
2. REPL 驱动期间**出现异常不会立即退出 / inform・异常对话框不以原生
   message box 而是输出到控制台**。请以这一差异为前提阅读日志。
3. `-replfile` 与 `-repl` 可独立启动（也可同时启用）。主执行通过
   共享队列 `ReplMainQueue` 串行化。

## 启动参数

| 参数 | 含义 |
|---|---|
| `-repl` | 启动 console REPL（直接读取 CONIN$）。面向人类交互。可用 `-repl=no/off/false/0` 抑制。 |
| `-replfile=<dir>` | **启动文件通道（面向外部 agent，主力方式）**。通过 `<dir>` 下的 `cmd`/`resp` 文件驱动。与 `-repl` 相互独立。 |
| `-replweb[=port]` | HTTP+SSE 服务器（默认 127.0.0.1:8899）。`GET /`=浏览器 REPL 页面 / `GET /events`=日志 SSE / `POST /cmd`=TJS 求值 / `GET /sub/<ch>`=通用 SSE / `GET|POST /watch` + `GET /sub/watch`=监视表达式。`GET /` 为 Console / Watch / Pad 标签页 UI（顶栏有事件停止 / 退出）。`POST /pad/exec` 可整体执行多行脚本。**`-replwebidle` 默认 5 秒有效** = 关闭浏览器后应用也随之退出（`=no` 可禁用。不过它会**收到至少一次 SSE 订阅后才进入待命**，因此仅 curl / 未连接的驱动不会退出）。用 `-replwebopen=app|tab|no` 可在从终端启动时也打开浏览器。**也可用 curl 驱动**（`curl -X POST -d 'expr' http://127.0.0.1:8899/cmd`）。 |
| `-nostartup` | 抑制 startup.tjs 的自动执行。无 window 启动也不会立即退出。只有明确调用脚本后处理才开始。可用 `-nostartup=no/off/false/0` 禁用。 |
| `-loglevel=info` | 日志级别。控制输出到控制台的信息量。`MASTER` 构建默认 WARNING。 |
| `-display=<番号\|名前>` | 指定启动所用的显示器（监视器）。**多显示器环境下不想占用主显示器做验证时使用**。编号为 1 origin（Windows `\\.\DISPLAYn` 的 n）、名称取监视器名的部分匹配，也支持 `primary`。`-display=list` 可把列表输出到日志。WINVER / SDL3 均支持。 |

> ⚠ **`-replweb` 的默认端口 8899 在整台 PC 上只有 1 个**。如果其他会话
> （或 user 本人）的 krkrz 先占用了它，后启动的自己的应用抢不到端口，
> 可**自己的日志里却照样输出 `listening on http://127.0.0.1:8899/`**，
> 让人难以察觉，而 `curl` **驱动的是对方的应用**。验证启动时请**显式指定
> `-replweb=<固有ポート>`**（不想打开浏览器时再加上 `-replwebopen=no`）。
> `-replfile` 的通道是自己的目录，必然到达自己的应用 —— **HTTP 与文件通道
> 结果不一致时先怀疑这一点**。确认方法是用 `Get-CimInstance Win32_Process -Filter "Name='krkrz64.exe'"` 查看
> ExecutablePath / CommandLine。

### WebServer 类（`-replweb` 的扩展注册入口）

`KRKRZ_REPL_WEB` 构建中，脚本 / 插件可向 web 服务器追加公开功能
（可随时注册，仅服务器运行时提供）。**处理器始终在主线程执行**。

- `WebServer.register(prefix, handler)` — 动态处理器（最长匹配）。
  `handler(%[method,path,query,body,bytes])` → 字符串=200 JSON / octet /
  整数=status / void=204 / `%[status,mime,body]`
- `WebServer.serveStatic(prefix, storageDir)` — 经 Storages 的静态文件服务（拒绝 ".."）
- `WebServer.broadcast(channel, text)` — 向 `/sub/<channel>` 订阅者 SSE 分发
- `WebServer.active` / `WebServer.url`（= `System.replWebURL`）

详见 engine `doc/REPL.md` 的「浏览器 REPL / Web 服务器」一节。threepp 的
浏览器编辑 UI（threepp/docs/webui.md、`/ui/` + `/app/` + `/api/three/`）是实际用例。
验证用 curl 就够：处理器注册通过 `-replfile` 通道或 `/cmd` eval →
再用 `curl http://127.0.0.1:8899/<path>` 确认响应。

代表性的 agent 启动方式（文件通道 + 带游戏画面）：

```
krkrz64.exe <ABS_DATA_DIR> -replfile=<ABS_CHANNEL_DIR>
```

加上 `-nostartup` 后为不执行 startup.tjs 的静止启动（也没有 window）。
绘制和对话框验证需要 window，此时需从通道显式创建 Window，或执行 startup.tjs。

exe 使用 krkrz_dev 的构建产物（相对仓库根）：

- SDL3 版：   `build/x64-windows/core/Release/krkrz64.exe`
- WINVER 版： `build/x64-windows-win/core/Release/krkrz64.exe`

进程的启动 / 停止请遵循 skill `dev-toolkit:appctl` 的约定（记录 PID，停止时
只停该 PID・带 exe 路径核对。像 `taskkill /IM krkrz64.exe` 这样按镜像名
批量 kill 会连累并行会话，禁止使用）。`dev-toolkit:appctl` 收录在
插件 `dev-toolkit` 中，随附辅助 `scripts/appctl.sh` 的位置请看
其 SKILL.md（下文按已放入 `$APPCTL` 的前提书写）。

shell 操作本身遵循 skill `dev-toolkit:msys2` 的启动惯例
（`MSYSTEM=MSYS /c/msys64/usr/bin/bash.exe -lc '...'`）。直接调用 `bash`
会引到 Git Bash 上。

```bash
export APPCTL_DIR="$SCRATCHPAD/appctl"
S="$APPCTL"                    # dev-toolkit:appctl 的 scripts/appctl.sh
CH="$SCRATCHPAD/replchan"

bash "$S" start krkrz \
  "$REPO/build/x64-windows-win/core/Release/krkrz64.exe" \
  "$REPO/src/core/data" -readencoding=UTF-8 -replfile="$CH" -loglevel=info
# ... チャネル経由で評価・検証 ...
bash "$S" stop krkrz
```

### 路径陷阱

项目目录参数按**相对 exe 的路径**解析。使用仓库的
data 目录时请传入**绝对路径**。若传相对 `data/`，会去查找
`build/.../Release/data/`，从而变成 "startup.tjs が見つかりません"（找不到 startup.tjs）。

相对仓库根为 `src/core/data/`（umbrella 的情况）。engine 单仓库检出
则为 `data/`。无论哪种都请**展开为绝对路径**再传入。

## REPL 驱动时的行为变化（本构建已实现）

通过检查 `TVPReplActive`（REPL 运行中为 true、`SysInitIntf.h`），在调用
`Application->MessageDlg` 的各包装器侧进行分支（override 实现
`SDL3Application::MessageDlg` 的主体未改动）。

- **出现异常不会立即退出**：REPL 期间 `TVPShowScriptException` 既不显示原生
  对话框也不调用 `TVPTerminateSync`，只把异常消息 + trace 通过
  `TVPAddImportantLog` 输出到控制台。修正后可重新 eval。
- **System.inform → 控制台**：REPL 期间 `TVPShowSimpleMessageBox`
  只把 `[dialog] caption: text` 写入日志，不弹出阻塞的 message box
  （按默认响应继续。获取响应为将来扩展）。
- **致命错误（ShowException）**：已通过 `TVPLOG_CRITICAL` 输出，REPL 期间
  抑制 message box。
- **System.confirm / Storages.selectFile / Storages.selectDirectory → agent 响应**：
  REPL 期间不弹出原生模式对话框，agent 可通过下文「模式响应通道」实际
  返回响应（没有响应口时，confirm 默认 Yes、选择走原生）。
  `System.inputString` 也已由引擎本体实现，走同一通道（2026-09-25 实测）。

## 模式响应通道（confirm / 字符串输入 / 候选值 / 文件选择）

在 `-replfile=<dir>` 驱动期间，当引擎本体执行 `System.confirm` / `System.inputString` / `System.choice` /
`Storages.selectFile` / `Storages.selectDirectory` 时，会通过**与 cmd/resp 不同的专用文件对**来
索取响应。主执行会被阻塞，但响应由另一进程（agent）直接写入，因此不会死锁。

协议（在 `<dir>` 下、投出 cmd 之后）：
1. 引擎本体把请求 JSON 写入 `<dir>/modal`。例：
   - `{"type":"confirm","caption":"確認","text":"続行?"}`
   - `{"type":"inputString","caption":"題名","prompt":"入力してください","default":"きてい"}`
   - `{"type":"choice","caption":"確認","text":"保存しますか?","choices":["yes","no","cancel"],"default":2}`
   - `{"type":"selectFile","name":"","title":"開く","save":false}`
   - `{"type":"selectDirectory","name":"","title":"フォルダ","save":false}`
2. agent 检测到 `modal` 出现后，把响应写入 **`<dir>/modalresp`**
   （纯字符串）：
   - confirm         : `yes` `y` `1` `true` `ok` 为真，**其余均为假**
   - inputString     : `ok<改行><入力値>` / 单独 `cancel` 表示取消（返回 void）
   - choice          : 所选元素的字符串（不区分大小写）或 index。空 / 不匹配的值 = `default`
   - selectFile/Dir  : 要返回的路径（可直接输入）/ 空字符串 = 取消

   ⚠ **每种类型的取消写法都不同**。不能用通用的 1 个字符串应付，
   需查看 `modal` 的 `"type"` 来区分（把 `cancel` 返回给 selectFile
   会被当成「选择了名为 cancel 的路径」）。
3. 引擎本体读取 `modalresp`，删除 `modal`/`modalresp` 后继续处理 → 照常
   把最终结果写入 `resp`。

也就是说 **selectFile/selectDirectory 不弹出对话框，agent 把想返回的
路径直接写入 `modalresp`，那就是选择结果**（会按 `name` 规范化写回）。

步骤的关键：投出 `cmd` 后、在等待 `resp` 之前**轮询 `modal` 是否出现**，
出现就写 `modalresp`。之后 `resp` 才会出现。PowerShell 示例：
```powershell
# cmd 送信後
while (-not (Test-Path "$chan/modal")) { Start-Sleep -Milliseconds 30 }
[IO.File]::WriteAllText("$chan/modalresp", "yes")   # or "ok`n<値>" / "cancel" / パス / "no" / ""
# この後 $chan/resp が出るので通常どおり読む
```

⚠ **不回答就不会返回 `resp`**。引擎本体默认等待 30 秒（`-replmodaltimeout=<秒>`，0 为无限）
后抛出 TJS 异常。投出可能弹出模式对话框的表达式的测试框架，要在 `resp` 等待循环中
同时盯住 `modal`，出现时按类型回答。

脚本侧可通过 `System.replActive`（只读）判断「当前是否正被 REPL 驱动」。
⚠ WINVER 下 REPL 在启动脚本之后才生效，因此 `startup.tjs` 执行期间仍为假
（SDL3 从启动时即为真）。启动瞬间的判断可并用 `System.getArgument("-replfile")`。

## 文件通道驱动（agent 推荐）

用 `-replfile=<dir>` 启动后，可通过 `<dir>` 下的文件驱动 REPL。
不经由 console，因此可直接用 Claude 的工具（Write/Read）操作。

协议（lockstep）：

1. 把命令（UTF-8 TJS）写入 `<dir>/cmd.tmp`，再 rename 为 `<dir>/cmd`。
2. 通道执行后，把结果 JSON 写入 `<dir>/resp`
   （`{"ok":bool,"result":"<pretty>","error":"<msg>"}`）。
3. 等待 `resp` 出现并读取，**删除之后**再发出下一条 `cmd`。
   （存在未读 `resp` 期间不处理下一条命令）

PowerShell 辅助示例（用 Move-Item 做 atomic rename → 等待 resp）：

```powershell
function Send-Cmd($script, $timeoutMs = 5000) {
    $cmdTmp = "$chan/cmd.tmp"; $cmd = "$chan/cmd"; $resp = "$chan/resp"
    [IO.File]::WriteAllText($cmdTmp, $script, [Text.UTF8Encoding]::new($false))
    Move-Item -Force $cmdTmp $cmd
    $sw = [Diagnostics.Stopwatch]::StartNew()
    while ($sw.ElapsedMilliseconds -lt $timeoutMs) {
        if (Test-Path $resp) { Start-Sleep -Milliseconds 30
            $c = [IO.File]::ReadAllText($resp); Remove-Item -Force $resp; return $c }
        Start-Sleep -Milliseconds 30
    }
    "<TIMEOUT>"
}
```

启动 → 等待数秒完成 window/DrawDevice 初始化 → 用 `Send-Cmd` 发送命令。
`win` 等 startup.tjs 的全局变量也可直接引用。

- 1 条命令 = 1 个表达式 / 1 条语句。**用 `;` 连接多条语句有时会成为
  syntax error**，因此请分开发送，或用 `(function(){ ...; return x; })()` 包裹。

## Agent API（输入注入 / 捕获 / 对话框控制）

`Agent` 与 `System` 一样无需实例即可调用类方法（SDL3 / WINVER +
`KRKRZ_USE_ELEMENTS` + `KRKRZ_USE_REPL` 时注册。`KRKRZ_REPL=OFF` 时消失）。输入
走与真实输入相同的路径，因此能到达游戏和 Elements 对话框。

| 方法 | 用途 |
|---|---|
| `Agent.mouseMove/mouseDown/mouseUp(x,y[,btn[,shift]])` | 鼠标（逻辑坐标，btn：0=左 1=右 2=中） |
| `Agent.click(x,y[,btn[,shift]])` / `Agent.wheel(delta,x,y)` | 点击（move+down+up）/ 滚轮（120 单位） |
| `Agent.keyDown/keyUp/keyPress(vk[,shift])` | 键（vk 为 `VK_*` 数值，例 `VK_RETURN`） |
| `Agent.text(str)` | 向活动对话框输入文本（input_box 等） |
| `Agent.ignoreRealMouse` | 设为真时**丢弃真实鼠标输入**（只放行 Agent 注入）。也可用启动选项 `-ignoremouse=yes` 设置。人移动指针也不会弄脏测量。⚠启用期间人无法手动操作鼠标 |
| `Agent.dialogs()` | 活动对话框数组 `%[index,modal,active,screen,focused,x,y,w,h]` |
| `Agent.closeDialog()` / `Agent.closeAllDialogs()` | 关闭最前 / 全部对话框 |
| `Agent.dialogClick(i,id)` / `Agent.dialogFocus(i,id)` | 按 id 指定启动 / 聚焦（无需坐标） |
| `Agent.captureScreen(path[,x,y,w,h])` | 在**下一帧**保存含 overlay 的实际画面为 PNG（返回值=path） |
| `Agent.lastCapture()` | 最近一次捕获结果 `%[path,width,height,ok]` |
| `Agent.a11yTree()` | 以 JSON 字符串返回朗读树（屏幕阅读器所看到的内容）。`{"dialogs":[…],"game":…}`。没有屏幕阅读器也能获取 |
| `Agent.a11yLog([since])` | 朗读日志 `%[lines, next]`（「大致会读成什么」的行：`[focus]` / `[value]` / `[state]` / `[caret]` / `[polite]` …）。仅在 REPL 运行期间积累 |
| `Agent.a11yAction(node, action[, arg])` | 沿屏幕阅读器相同的路径操作（不是键合成）。action = click / focus / increment / decrement / set_value |

验证流程示例（文件通道）。`$CAP_DIR` 是会话 scratchpad 等
可写工作目录的绝对路径：

```
Send-Cmd "win.openMenu()"
Send-Cmd "Agent.dialogs()"                       # 状态確認 (screen/rect)
Send-Cmd "Agent.click(255,80)"                   # 座標クリックで遷移
Send-Cmd "Agent.dialogClick(0,'sound')"          # or id 指定で操作
Send-Cmd "Agent.captureScreen('$CAP_DIR/cap.png')" # 即 return、~1 フレーム後に保存
# (少し待って) Read tool で cap.png を開いて目視確認
```

`captureScreen` 内部会调用 `RequestUpdate`，因此即使空闲也会保存。
默认 DrawDevice 为 `SDLOGLDrawDevice`（GL），经 `glReadPixels` 读回。
优点是**可规避 PrintWindow/BitBlt 下 GL 客户区变黑的问题**
（跑起来等几百 ms 后 captureScreen→Read 目视确认，是常规做法）。

## 向 stdin 送入 TJS（console REPL / 面向人类）

REPL 工作线程通过 `ic_readline`（icline）或 fgets shim 逐行读取。
来自工作线程的请求由主线程的 `TVPDrainREPL()` 每帧取出 1 条，
用 `TVPExecuteExpression` 执行。

### 批量执行（推荐：用于验证 / 冒烟测试）

送入多行并拾取结果（data 路径用绝对路径，请按自己的构成替换）：

```bash
printf '%s\n' \
  'var w = new Window(); w.setSize(320,240); w.visible = true;' \
  'Debug.message("hello from repl");' \
  '1 + 2 * 3' \
  'exit' \
  | krkrz64.exe <ABS_DATA_DIR> -repl -nostartup -loglevel=info
```

`=>` 行是求值结果。用 `exit` / `quit` 关闭 REPL 并结束进程。

### icline 与 TTY 的注意事项

默认构建使用 icline（行编辑・历史・颜色），期待 raw TTY。
管道 stdin 时行为可能紊乱，因此**agent / 无头（headless）通过管道驱动的话，
用 `KRKRZ_REPL_LINE_EDIT=OFF` 构建**会变成基于 fgets 的垫片
（`KRKRZ_REPL_NO_ICLINE`），可原样顺畅处理管道 stdin。

- engine 单仓库：`cmake --preset x64-windows -DKRKRZ_REPL_LINE_EDIT=OFF`
- umbrella：`PRESET=x64-windows CMAKEOPT='-DKRKRZ_REPL_LINE_EDIT=OFF' make prebuild build`

### 长脚本经 Storages 执行

多行脚本与其经 stdin 发送，不如放在文件里、从 REPL 调用更可靠：

```tjs
Scripts.execStorage("mytest.tjs");      // data/ 配下 (autopath)
```

用 `-nostartup` 启动后再以上述方式开始测试，是基本流程。

## 点命令

用 `.help` 查看列表。**console / `-replfile` / `-replweb` 3 个前端全部可用**
（文件通道中，以 `.` 开头的行按点命令处理，输出行以换行分隔
放入响应 JSON 的 `result`）。主要命令：

| 命令 | 用途 |
|---|---|
| `.help` | 命令列表 |
| `.clear` | 丢弃 multiline 输入 |
| `.depth [N]` / `.compact [on/off]` | 结果的 pretty-print 设置 |
| `.mem` | 内存摘要 1 行（File/Bitmap/Sound/Global/Process/SysAlloc） |
| `.memdump` | 把全部内存统计写入日志（`TVPHeapDump`） |
| `.memsites [N] [関数名の一部]` | 存活分配按调用方统计的前 N 条（仅诊断构建 + `-memstatsite` 启动时） |
| `.sysalloc` | 系统分配器信息 |
| `.filecache` / `.imagecache` | 把文件 / 图像缓存列表写入日志 |
| `.memoverlay [on/off]` / `.padoverlay [on/off]` | 画面覆盖层显示开关 |
| `.mempeakclear` | 重置 peak_used |
| `.cap [path]` | 画面捕获（`Agent.captureScreen`，省略时 agent_cap.png） |
| `.dlg` / `.dlgclose` | 对话框列表 / 全部关闭（`Agent.dialogs`/`closeAllDialogs`） |
| `.click X Y` | 向 (X,Y) 注入点击（`Agent.click`） |
| `.a11y` | 显示朗读树（`Agent.a11yTree`） |
| `.a11ylog [N]` | 朗读日志第 N 行起（`Agent.a11yLog`） |
| `.a11ydo <node> <action> [arg]` | 沿 AT 路径操作朗读树的节点（`Agent.a11yAction`）。node 是 `.a11y` 的 id（画面 JSON 的 `"id"` / setGameA11y 的 id / `layer:<Layer.name>` / `#<hex>`） |
| `.say <text>` | `ElementsDialog.announce` |
| `.watch` | 以 `id: 式 = 値` 显示监视表达式列表（显示前先全部求值） |
| `.watch add EXPR` | 添加监视表达式并立即求值（表达式可含空格） |
| `.watch rm ID` / `.watch rm all` | 删除监视表达式 / 全部清除 |
| `.watch edit ID EXPR` | 替换监视表达式 |
| `.watch auto [ms/on/off]` | 自动更新的间隔（`on`=500ms / `0`=每帧 / 下限 100ms） |
| `.event [on/off/toggle]` | `System.eventDisabled` 的显示 / 切换 |

TJS 求值直接把不以 dot 开头的行原样输入（表达式・语句均可，
直到括号 / 引号闭合前可跨多行）。

### 监视表达式（`.watch`）——挂载状态进行观测

相当于吉里吉里2 调试窗口的「监视表达式」。是**不必每次重打相同表达式
就能盯住状态**的工具，适合追踪值变化的验证。

```
.watch add win.layer.left
.watch add ElementsDialog.modalActive
.watch auto 500      # 自動更新 (0 = 毎フレーム / off で停止)
.watch               # 一覧 (表示前に全件評価する)
```

- 求值上下文**固定为 global**。即使表达式抛出异常，也只是把
  `(error) <メッセージ>` **当作值**摆出来，REPL 和应用都不会死。
- **列表显示会伴随求值**，因此想确认「是否仅靠自动更新就求值了」时，
  可埋入带副作用的表达式（如计数器自增）再用别的命令读取。
- 表达式列表与间隔**保存在当前目录的 `.krkrz_watch`**，下次启动时
  读回（用 `-replwatchfile=<path>` 更改、`=no` 禁用）。**验证时想清除，
  就删除该文件或加 `=no`**。
- **从 HTTP 也能触达同一核心**（并用 `-replweb` 时）：
  `curl -s -X POST -d 'op=add&expr=…' localhost:8899/watch` /
  `curl -s localhost:8899/watch`（不求值。用 `?eval=1` 求值）/
  `curl -N localhost:8899/sub/watch`（自动更新的 push）。
  看到的是与点命令相同的列表，因此**一边添加、另一边观测**即可。

## 典型工作流程（agent）

1. 用 `-repl -nostartup` 启动（既无 window 也无 startup 的静止状态）。
2. 从 REPL 创建最小 Window 并把 `visible=true` → 进入 SDL 事件循环
   （没有 window 就不进入绘制循环的那类验证需要这一步）。
3. 用 `Scripts.execStorage` 或 stdin 求值验证脚本。
4. 即使出现异常进程也还活着，因此读取控制台的异常/trace、
   修改脚本后再次求值。
5. 用 `.mem` 等观察状态。用 `exit` 退出。

## 核心演示全场景显示确认（`-demotest` / `-demotestcap`）

引擎变更后「是否全都正常显示」的回归确认，比起在 REPL 里逐个发送场景，
**画廊自动巡回 + 自动捕获**更快（demolib 功能。
SSOT 是 `data/demolib/readme.txt` 的「ヘッドレス自動テスト」（无头自动测试）一节）。

```bash
krkrz <ABS>/src/core/data -demotest -demotestcap=<ABS_CAP_DIR>
# 例 (Linux、エージェントのシェルから): WAYLAND_DISPLAY=wayland-0 を前置
```

- 每场景巡回 40 帧，把各场景保存为 `<dir>/sceneNN.png`，
  以 `@demotest:ok` 自动结束（01 = 菜单）。日志中
  `@demotest:cap <path> <シーン名>` 是编号 → 场景名对应关系、
  `@demotest:<シーン名> ...` 是各场景的自验证结果
- `<dir>` 为绝对路径，不存在时会被创建。单独 `-demotestcap` 也会巡回
- 保存使用 `System.captureScreen`，因此仅限 REPL 有效的构建（MASTER 会
  输出 `@demotest:cap unavailable` 而不拍摄）。需要真实窗口
- 跑不完全程（挂起 / abort）本身就是故障信号。怀疑最后一条
  `@demotest:scene N/M` 的下一个场景（或其退出处理）
- 目视确认时，与其逐张 Read PNG，不如用 PIL 等缩小后拼成
  数张并排的列表图再 Read，速度更快
- 含随机数・动画的场景（图像处理 / 粒子 / FPS 显示等）每次
  像素都会变化，与上次捕获做差异比较时应作为噪声处理

**能拍到的只有各场景的第一页**。多页场景（GL Canvas 等）
的剩余部分用 `-replfile` 启动来发送：

```
demoShell.switchTo(13)              # シーン番号 (0 = メニュー、sceneNN の NN-1)
Agent.keyPress(VK_RIGHT)            # シーン内のページ送り
System.captureScreen("<ABS>/p2.png")  # 次フレームで保存されるので少し待つ
```

`demoShell` 是 `runDemoHub` 放在 global 中的 DemoShell 实例。

## 相关（路径以 engine 根为基准 / umbrella 下前置 `src/core/`）

- 语言规格：skill `tjs2` / 引擎本体 API：skill `krkrz`
- 构建：engine 单仓库用 `cmake --preset x64-windows`，umbrella 用 `make`
  （预设 `src/core/CMakePresets.json`）。详见各 `CLAUDE.md`
- REPL 实现：`common/utils/REPL.cpp` / 共享执行队列：
  `common/utils/ReplMainQueue.cpp` / 文件通道：
  `common/utils/ReplFileChannel.cpp` / 启用：CMake `KRKRZ_REPL`
  （= `KRKRZ_USE_REPL`）
- Agent API：`common/environ/AgentControlIntf.cpp`（通用部分）+ 输入 seam
  `generic/environ/AgentInput.cpp`（SDL3/LIB）/ `win32/environ/AgentInput.cpp`（WINVER）/
  捕获：`common/visual/ScreenCapture.cpp`
- 详细文档：`doc/REPL.md` 的「エージェント駆動」（agent 驱动）一节
- 多对话框同时显示的规格：`doc/ElementsDialog.md`