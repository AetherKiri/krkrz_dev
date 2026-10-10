---
name: krkrz-webui
description: 吉里吉里Z (krkrz) の -replweb HTTP+SSE サーバ (WebServer クラス) にブラウザ UI を載せて、本体アプリの操作/編集/観測パネルをブラウザ側に組み込む方法論。ゲーム本体は 3D 表示やゲーム内 UI に専念させ、編集ツール・インスペクター・ダッシュボード・REPL コンソールをブラウザ (別ウィンドウ/別PC) から使う構成を作るときに読む。プラグインや TJS がサーバへエンドポイントを追加公開する手順 (WebServer.register / serveStatic / broadcast)、ハンドラ呼び出し規約 (req %[method,path,query,body,bytes] → 文字列/octet/整数/辞書)、状態同期パターン (fetch POST + SSE /sub push + throttle + 差分/tick 配信)、既存 REPL コンソール (/events + /cmd) の UI 埋め込み、ブラウザのアプリモード起動 (Chromium --app / -webui)、json.dll 連携、TJS2 由来のハマりどころ (ローカル関数クロージャ不在→クラス化 / ブロックコメントのネスト誤爆 / startup 例外の致命性 / ハンドラは必ずメインスレッド実行) を網羅。エンジン側 WebServer クラスそのものの仕様は krkrz core doc/REPL.md、REPL/Agent 駆動は skill krkrz-repl、Elements ネイティブ UI は skill elements、TJS2 言語は skill tjs2、本体 API は skill krkrz を参照。中文说明：在吉里吉里Z 的 -replweb HTTP+SSE 服务器上集成浏览器 UI，制作编辑工具・检查器・仪表盘・REPL 控制台等浏览器侧操作/编辑/观测面板时使用。触发词：浏览器 UI、replweb、WebServer、SSE、端点注册、状态同步、浏览器面板、webui、REPL 控制台。
---

> **路径基准**：正文的相对路径以 **engine 根目录为基准**（在 krkrz_dev 中前置 `src/core/`，见下文）。工作目录不是 krkrz_dev（krkrz_android / krkrz_ios 等外围仓库或项目文件夹）时，请**前置 `${KRKRZ_BASE}/krkrz_dev/`** 再阅读（用 `echo $KRKRZ_BASE` 确认实际路径；每台机器的值不同，请勿写入绝对路径）。

# 基于 krkrz replweb 的浏览器 UI 集成方法论

在 krkrz 引擎的 `-replweb` HTTP+SSE 服务器（`KRKRZ_REPL_WEB` 构建）之上，
把引擎本体应用的**操作・编辑・观测 UI 集成到浏览器侧**的方法论。
可以构建「游戏本体 = 显示 + 游戏内 UI、浏览器 = 编辑工具 + 检查器 + REPL」
这样的分离架构。好处是摆脱 Elements 原生 UI（skill `elements`）的约束（布局/
输入/复制粘贴/字体），UI 迭代无需重新构建引擎。

引擎侧 `WebServer` 类本身的规格以 krkrz core `doc/REPL.md` 的
「浏览器 REPL / Web 服务器」一节为 SSOT。本 skill 汇总的是**在其之上构建 UI 那一侧**的
设计模式。

正文中的引擎路径以 engine 根目录为相对基准（`doc/...`、`common/...`、`data/...`）。
本 skill 所在的 umbrella 仓库（`krkrz_dev`）中请**前置 `src/core/`** 阅读
（例：`src/core/doc/REPL.md`）。单独检出 engine 时则直接使用。

## 何时使用 / 何时不用

- **使用**：VRM/3D 编辑器、舞台/场景编辑、参数调整面板、实时检查器/仪表盘、
  远程（另一台 PC）编辑、希望 REPL 与 UI 共存。
- **不使用**：游戏内自成一体的常驻 UI・模态对话框（→ skill `elements`）。
  大致的标准是：作为游戏一部分分发的对话 UI 用 Elements，开发/编辑工具用浏览器。

## 前提条件

- engine 为 `KRKRZ_REPL_WEB` 构建（`WebServer` 类已注册）。
- **服务器启动的基本方式是从脚本调用 `WebServer.start([port])`**（默认 8899）。
  这样就不需要 `-replweb` 选项 = 不必让使用者每次都加上（在应用的 startup 中写
  `if (!WebServer.active) WebServer.start(8899);`）。若显式指定 `-replweb[=port]`，
  引擎本体会先启动，因此 `WebServer.start` 为避免重复启动而变为 no-op。
  可用 `0.0.0.0:<port>` 跨 LAN 访问（`WebServer.startAt("0.0.0.0", port)`。仅限可信
  网络・启动日志中有警告）。监听 URL 为 `WebServer.url` / `System.replWebURL`。
- 使用 JSON I/O 时需要 `json.dll`（`Scripts.toJSONString` / `evalJSON`）。见下文。
- 验证时用 `krkrz-repl`（`-replfile` 通道 / `/cmd`）和 curl 很方便。

## 4 层架构

| 层 | 实体 | 职责 |
|---|---|---|
| ① 服务器 | engine `common/utils/ReplWebServer.cpp` + TJS 类 `WebServer`（`ReplWebIntf.cpp`） | HTTP+SSE。路由・静态文件服务・SSE 通道。**处理器始终在主线程执行** |
| ② 处理器 | 原生（插件）或 TJS | 处理 `/api/…` 和 `/app/…`。繁重/需要类型转换的处理用原生，细致的操作用 TJS |
| ③ 应用桥接 | TJS（应用侧脚本） | 把应用的模型层（状态获取/操作函数）桥接到 HTTP 路由 + 注册静态文件服务 + SSE 推送 |
| ④ 浏览器 UI | `data/ui/**` 的静态 HTML/JS | 单页面（免构建的 vanilla JS 就足够）。fetch POST + SSE 订阅 |

## 最小步骤

### 1. 提供静态 UI
```tjs
// アプリ起動後 (startup.tjs 等) に一度
if (typeof global.WebServer != "undefined") {
    WebServer.serveStatic("/ui/", "ui/");   // data/ui/** を /ui/** で配信 (json.dll 不要)
}
```
放好 `data/ui/index.html` 后即可用 `http://127.0.0.1:8899/ui/` 打开。
静态文件服务经 Storages 进行（xp3 内也可以）。`..` 会因目录穿越而被拒绝（403）。

### 2. 注册操作端点
```tjs
// TJS2 はローカル関数のレキシカルクロージャを持たない (下記ハマりどころ)。
// ハンドラはクラスのメンバにして objthis 経由で相互参照させる。
class AppBridge {
    function AppBridge() {}
    function handler(req) {
        // req = %[ method, path, query, body(文字列), bytes(octet: body 非空時) ]
        if (req.path == "/app/state") return Scripts.toJSONString(buildState());
        var arg = (req.body != "") ? Scripts.evalJSON(req.body) : %[];
        if (req.path == "/app/do") { app.doSomething(arg.x); push(); return "{\"ok\":true}"; }
        return %[ "status" => 404, "body" => "{}" ];
    }
    function buildState() { return %[ /* アプリ状態 */ ]; }
    function push() { WebServer.broadcast("state", Scripts.toJSONString(buildState())); }
}
global.bridge = new AppBridge();
WebServer.register("/app/", bridge.handler);   // プレフィックス最長一致
```

### 3. 从浏览器调用（在 index.html 内）
```js
// 取得
const st = await (await fetch('/app/state')).json();
// 操作
await fetch('/app/do', {method:'POST', body: JSON.stringify({x:1})});
// 変更購読 (サーバ push)
const es = new EventSource('/sub/state');
es.onmessage = e => render(JSON.parse(e.data));
```

## WebServer API 速查表

| 成员 | 用途 |
|---|---|
| `WebServer.register(prefix, handler)` | 动态处理器注册（最长匹配・覆盖）。服务器未启动时也会保留，启动时即生效 |
| `WebServer.unregister(prefix)` | 注销 |
| `WebServer.serveStatic(prefix, storageDir)` | 经 Storages 的静态文件服务。例 `("/ui/","ui/")` |
| `WebServer.unserveStatic(prefix)` | 解除静态挂载 |
| `WebServer.broadcast(channel, text)` | 向 `/sub/<channel>` 订阅者推送 SSE（可含换行） |
| `WebServer.registerPanel(id, label, path)` | **在内置 UI 中追加一个标签页**（见下文） |
| `WebServer.unregisterPanel(id)` | 移除面板 |
| `WebServer.start([port])` / `startAt(host, port)` | 从脚本启动服务器（无需 `-replweb`）。已在运行时为 no-op。返回值 = 是否在运行 |
| `WebServer.stop()` | 停止服务器 |
| `WebServer.openBrowser([url [, appMode=true]])` | 在浏览器中打开 url。appMode 时先用 `--app` 尝试 Edge/Chrome，不行则回退到默认浏览器。省略 url 时使用运行中的 URL。**SDL 版也可用应用模式** |
| `WebServer.active` / `WebServer.url` | 是否在运行 / 监听 URL |

内置路由：`GET /` = 内置 UI（**Console / Watch 标签页**）/ `GET /events` = 日志 SSE /
`POST /cmd` = TJS 求值 / `GET /sub/<ch>` = 通用 SSE /
**`GET|POST /watch` + `/sub/watch` = 监视表达式** / **`POST /pad/exec` + `GET|POST /pad/file` = Pad** / **`GET|POST /state` + `/sub/state` = 控制器** / **`POST /bye`**（见下文）。
**内置路由会比 `WebServer.register` 先被判定**，因此这些路径无法被自己的处理器
覆盖（请使用其他名称）。

### 项目面板（`registerPanel`）— 在内置 UI 中添加标签页

**在立起整套自建 UI 之前先考虑这个。** 只用 `serveStatic` 做独立页面的话，
会失去 Console / Watch / Pad 和控制器。作为面板添加即可共存。

```tjs
WebServer.serveStatic("/tool/", "web/");
WebServer.registerPanel("mytool", "案件ツール", "/tool/tool.html");
```

- 内容是 **iframe**。不是向内置页面注入脚本的方式，因此**不依赖内置 UI 的内部 DOM**
  （那边怎么变都不会坏）
- 因为同源，面板可以正常调用 `/cmd` `/watch` `/pad/exec` 以及自己
  `register` 的端点
- 用相同 id 覆盖。注册/注销会通过 `/sub/panels` **立即反映到已打开的页面**
- 内容在**首次打开标签页时**才读取（即使是很重的工具，启动也不会变慢）
- `path` 是**以 `/` 开头的服务器路径**。非法时不会注册，且日志会给出原因
  （⚠ 从 msys2 的 bash 用 curl 调用时，`/tool/...` 会被自动转换成 Windows 路径
  而被拒绝。请使用文件 body 或 PowerShell）

### 对齐浏览器 UI 与应用的生命周期（双向）

在以浏览器为 UI 的构成中，**只剩一边残留**是最麻烦的。engine 侧
已把双向都关掉了。

**引擎本体 → 浏览器消失则退出**（`-replwebidle`）

- **默认 5 秒生效**。`-replwebidle=no` 禁用，`=<秒数>` 修改
- **至少收到过一次 SSE 订阅后才开始生效（武装）**。因此不挂订阅的
  agent 驱动 / API 面使用不会掉线。**自己的 UI 只要挂 1 条 `EventSource`，
  它就是 «浏览器在线» 的标志**
- 多标签页按订阅数处理，所以直到最后 1 个标签页关闭前都不会退出
- 页面在 `pagehide`/`beforeunload` 时发送 `navigator.sendBeacon('/bye')`，
  宽限时间会提前到约 2 秒（**自己的 UI 做同样的事也能加快关闭**）。
  即使不发送，也会在 `<秒数>` 后折叠

**浏览器 → 引擎本体消失则关闭**

- `/sub/state` 收到 `{"exiting":true}` 时立即 `window.close()`
  （engine 通过 `Stop()` 发送）
- SSE 断开后 5 秒未恢复则 close（崩溃 / 强制退出）
- close 无效的普通标签页回退到全屏覆盖层
- **自己的 UI 也实现这 2 条，就能防止 «只有引擎本体退出而页面残留»**

### 浏览器自动打开（`-replwebopen`）

默认仅在「回环绑定 且 无控制台（GUI 启动）」时才使用 app 模式。
**从终端启动不会打开**，想打开时用 `-replwebopen=app`
（`tab` = 普通窗口 / `no` = 禁止）。从 TJS 用 `WebServer.openBrowser`。

⚠ engine 的 app 模式会用 **用户的常规配置文件**启动 `msedge.exe --app=<url>`
（不指定配置文件）。验证时若自己传 `--user-data-dir=<一次性>`，
**Edge 的首次引导（催促同步的对话框）会出现在用户画面上**，因此使用一次性
配置文件时请附上 `--disable-sync --no-first-run
--no-default-browser-check`，**用完务必连窗口一起清理干净**。

### 监视表达式 API（`/watch`）### Pad API（`/pad/*`）— 多行脚本的执行与保存

- `POST /pad/exec` — 把 body **整体执行 1 次**（与 `/cmd` 的单行执行不同，
  函数定义和循环可以直接跑）。返回 `{"ok","result","error"}`
- `GET /pad/file?path=` — 从存储读取（text/plain）
- `POST /pad/file?path=` — 写入存储。**默认 403**。
  只有在用 `-replwebpad=<dir>` 启动引擎本体时，才能写入该前缀之下
  （⚠ 这不是安全边界，而是防止 «[保存] 手滑» 的栅栏。既然 `/cmd` 可以执行任意
  TJS，全权限本来就是敞开的）

### 监视表达式 API（`/watch`）— 挂接状态进行观测

引擎内置。维护表达式列表，统一求值后返回。在写自己的
检查器之前，先看看这个够不够用更快。

| 路由 | 说明 |
|---|---|
| `GET /watch` | 列表 + 当前值（JSON）。**不求值**，因此轮询安全。`?eval=1` 先求值再返回 |
| `POST /watch` | form-urlencoded。`op=add&expr=…` / `op=rm&id=…` / `op=edit&id=…&expr=…` / `op=clear` / `op=interval&ms=…` / `op=eval`。成功时返回与 GET 相同的 JSON |
| `GET /sub/watch` | 自动更新的推送。**只在值变化时**推送（即使挂了常量表达式也不会产生无用的推送） |

```js
await fetch('/watch', {method:'POST', body:new URLSearchParams({op:'add', expr:'System.getTickCount()'})});
await fetch('/watch', {method:'POST', body:new URLSearchParams({op:'interval', ms:'500'})});
new EventSource('/sub/watch').onmessage = e => render(JSON.parse(e.data));
```

payload = `{"interval":500,"entries":[{"id":1,"expr":"…","value":"…","error":false}]}`。
`interval` 为 `-1`=off / `0`=每帧 / 正数=ms（下限 100ms）。即使表达式抛出异常，
也只是 `value` 变成 `"(error) …"`，列表照常返回。

## 处理器调用约定

- 参数 `req` = `%[ method, path, query, body, bytes ]`（bytes 仅在 body 非空时为 octet）。
- 返回值的解释：
  - 字符串 → 200 `application/json`
  - octet → 200 `application/octet-stream`
  - 整数 → 以该状态码返回空响应体
  - void → 204
  - 字典 `%[status, mime, body(字符串 or octet)]` → 显式指定
- 处理器内的 TJS 异常 → 500（正文 = 消息）+ `WebServer: handler error:` 日志。
- **处理器必定在主线程被调用**（`ReplMainQueue` 任务）。可以自由调用 GL/TJS/引擎
  API。注意长时间的处理会阻塞帧（与 Elements 版相同的约束）。

## 状态同步模式（实践）

- **client → server**：`fetch POST`（body=JSON）。滑块等连续输入要做
  **throttle（节流）**（例 50ms，按键粒度只发送最新值）。连续反映类操作不调用 `push()`
  （操作源头才是事实，防止 SSE 回流把输入覆盖掉）。
- **server → client**：SSE `/sub/state`。
  - 每个操作路由之后立即 `push()`（一次性发整个字典）。
  - 从帧循环以约 4Hz 做**增量检测推送**（与上次 JSON 一致就不发送）。
    这样 REPL 等 UI 之外的更改也会自动反映到浏览器。
- **不要破坏编辑器 DOM 的重建**：把高频变化的观测数据（fps/日志等）与
  编辑状态分开，只在编辑状态变化时重建 DOM（观测数据用另一个 DOM 做增量更新）。
  持有滑块操作中的标志，操作期间抑制来自 SSE 的重绘。

## 让 REPL 控制台与 UI 共存

只需在浏览器 UI 侧**原样**订阅・POST 引擎内置的 `/events`（日志 SSE，
backlog 2000 行・附带按级别划分的 cls）和
`/cmd`（POST body = 将 1 行交给 TJS 求值，响应 body 在继续输入中为 "1"）。
不改引擎就能把 REPL 集成进编辑 UI。历史（↑↓）和继续输入提示的切换在浏览器侧实现。

## 以应用模式打开浏览器

用 Chromium 系的 `--app=<URL>` 会变成没有标签页/地址栏的窗口。
**基本是使用引擎本体的 `WebServer.openBrowser(url)`**（先用 `--app` 尝试 Edge → Chrome，
不行则回退到默认浏览器）。引擎把「打开 URL」（`TVPShellExecute` =
SDL 为 `SDL_OpenURL`）和「带参数执行程序」（`TVPExecuteProgram` = 桌面
Windows 用 Win32 `ShellExecute`）分开实现，因此**SDL 版也能用应用模式
打开**（直接调用 `System.shellExecute` 在 SDL 下 `--app` 参数会被丢弃，所以做不到）。
```tjs
WebServer.openBrowser(("" + WebServer.url) + "ui/");   // url 省略で稼働中サーバ URL
```
只要先调用过 `WebServer.start()`，服务器就是同步运行（`WebServer.active`=true），因此
**无需用 Timer 等待打开**（启动后直接 `openBrowser` 即可）。
如果要为旧引擎（未实现 `openBrowser`）写回退，
用 `typeof WebServer.openBrowser != "undefined"` 分支判断，仅在没有时才使用传统的
`System.shellExecute("msedge.exe", "--app=" + url)` 系列。

## json.dll

`/app/` 的 JSON I/O 需要 `json.dll`（`Scripts.toJSONString(v,indent)` /
`evalJSON(str)` / `evalJSONStorage(path,utf8)` / `saveJSON(path,v,utf8,indent)`）。
把与 exe 同世代的版本放进 plugin 文件夹。查看器/最小启动时可能未链接，因此
在桥接侧自行尝试 `try { Plugins.link("json.dll"); } catch(e){}`，不行的话
只注册静态文件服务（`/ui/`）并禁用操作类功能，回退会更干净。

## ★坑点（源自 TJS2/krkrz）

1. **TJS2 没有局部函数的词法闭包**：IIFE 内函数之间的相互引用会在
   运行时报「找不到成员」。→ 把处理器/辅助函数做成**类的成员**，
   经 `objthis`（实例）解析。用 `WebServer.register("/x/", obj.method)`
   传递时，调用时 objthis 就是该实例。
2. **TJS2 的块注释可以嵌套**：注释文中 `/ui/` + `*` 之类的排列会被
   误认为 `/*`，导致「注释永不结束直达文件末尾」。→ 编写桥接/处理器的
   .tjs **只使用行注释（`//`）** 最安全。
3. **startup 脚本中的异常是致命的**：REPL 保护（`TVPReplActive`）在
   `TVPCreateREPL()` 之后才建立，因此从 startup 调用的注册脚本若加载失败，
   整个进程都会崩溃。注册处理要写得防御性，尽量不抛异常/做好排查分离。
4. **处理器在主线程执行**，但 HTTP 线程要处理多个连接。设计前提是共享状态只在
   处理器内（主线程）访问（engine 会用 SubmitTask 串行化）。
5. **静态文件服务不依赖 json.dll**。想先只出 UI 页面时，可以在
   register 之前无条件调用 serveStatic。

## 验证

- 处理器注册用 `-replfile` 通道（skill `krkrz-repl`）或 `/cmd` eval，
  再用 `curl http://127.0.0.1:<port>/<path>` 确认响应（不需要浏览器即可做往返测试）。
- SSE 用 `curl -N http://127.0.0.1:<port>/sub/<ch>` 订阅，同时另发操作。
- 画面反映用 `Agent.captureScreen(path)` → 目视检查图像（skill `krkrz-repl`）。
- UI 的 JS 语法检查：抽出 `<script>` 部分后 `node --check`。

## 参考实现（krkr_threepp）

VRM 立绘/箱庭编辑器的完整实例：
- engine：`common/utils/ReplWebServer.cpp`（服务器）/ `ReplWebIntf.cpp`（TJS 类）/
  `doc/REPL.md`（规格 SSOT）
- 插件：`main.cpp` 的 `ThreeWebApi`（原生公开 `/api/three/`。
  链接时从 POST_REGIST 调用 `WebServer.register`，unlink 时注销）。面向 UI 的批量
  JSON 转储 `Object3D.treeJson` / `VRM.expressionListJson` / `morphListJson`
  （用 UTF-8→ttstr 转换辅助函数支持日语。默认 std::string 转换器仅限 ASCII）
- 应用+UI：`data/webui.tjs`（`WebUIBridge`，`/app/…` 桥接）+ `data/ui/index.html`
  （5 模式编辑 + 侧边栏 + REPL 控制台）。设计细节见 `threepp/docs/webui.md`

相关 skill：`krkrz-repl`（REPL/Agent 驱动・-replweb 启动）/ `elements`（原生 UI）/
`krkrz`（本体 API：Storages/System/Plugins）/ `tjs2`（语言规格）/ `dev-toolkit:msys2`（shell）。