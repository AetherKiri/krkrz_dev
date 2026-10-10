# WebServer

!!! warning "实验中 ( 不在稳定性保证范围内 )"
    这个 API 的形式尚未固定。**有可能在无预告的情况下被更改或删除**
    ( 即使是非兼容更改，主版本号也不会提升 )。
    关于版本提升方式，请参阅 [版本管理](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)。

    这是用于开发、验证的 API。会随着 REPL / 调试窗口的完善而变化。 内置路由有可能在无预告的情况下增加 ( 增加的路径无法用 register 覆盖 )。

WebServer 类是用于控制内置于吉里吉里Z 的 HTTP + SSE 服务器的类。不能从这个类创建对象。与 System 一样，用 `WebServer.start(...)` 这样的方式直接调用使用。

这个服务器是供命令行选项 `-replweb` 使用的，通过从 TJS 注册端点，可以构建浏览器 UI 或来自外部的控制。这个类仅在启用了 `KRKRZ_REPL_WEB` 的构建中可用。

注册的处理器为 `handler(req)` 形式，`req` 是持有以下键的字典。处理器必定在主线程中执行。

- `method` ... HTTP 方法 ( "GET" / "POST" 等 )
- `path`   ... 请求路径
- `query`  ... 查询字符串
- `body`   ... 请求体 ( 字符串 )
- `bytes`  ... 请求体 ( 字节序列。仅在 body 非空时存在 )

响应由处理器的返回值决定。

- 字符串     ... 作为 200 application/json 返回
- 字节序列   ... 作为 200 application/octet-stream 返回
- 整数       ... 以该状态码返回空正文
- void       ... 返回 204
- 字典 `%[status, mime, body]` ... 按指定的那样返回
- 发生 TJS 异常时返回 500

另外，以下路由已内置在服务器侧 ( 不是 TJS 的成员 )。

- `GET /`              ... 查看器本体 ( Console / Watch / Pad 的标签页 UI )
- `GET /events`        ... REPL 控制台用的 SSE 流
- `POST /cmd`          ... 向 REPL 发送命令
- `GET /sub/<channel>` ... 任意通道的 SSE 订阅
- `GET`/`POST /watch`  ... 监视表达式的获取 / 操作
- `GET`/`POST /state`  ... 控制器 ( `System.eventDisabled` / 退出请求 )
- `POST /pad/exec` , `GET`/`POST /pad/file` ... Pad ( 脚本编辑器 )
- `GET /panels`      ... 已注册面板的列表 ( 内置 UI 用于组建标签页 )
- `POST /bye`          ... 关闭页面的信号

!!! warning "内置路由先于 register 判定"
    上述路径无法用 [WebServer.register](WebServer.md#register) 或
    [serveStatic](WebServer.md#servestatic) **覆盖**。
    自有端点请使用其他前缀
    ( 例: `/api/` `/ui/` )。

!!! warning "日语等多字节的值请用 body 接收"
    `query` 是保持 percent-encoding 状态的字符串。将其还原的
    `System.urldecode` 仅限 Windows 原生构建，因此
    **在 SDL3 构建中无法通过查询接收非 ASCII**。
    字符串的传递请使用 `body` ( UTF-8 )，`query` 留给数值或标识符等
    ASCII 指定较为安全。

最小构成的实现示例在核心演示 `webui` 中 ( 把静态文件服务 + 动态端点
+ 来自游戏的 push 汇总到 1 个画面中的演示 )。

## 成员列表

### 属性

- [active](#active)
- [url](#url)

### 方法

- [register](#register)
- [registerPanel](#registerpanel)
- [unregisterPanel](#unregisterpanel)
- [unregister](#unregister)
- [serveStatic](#servestatic)
- [unserveStatic](#unservestatic)
- [broadcast](#broadcast)
- [start](#start)
- [startAt](#startat)
- [stop](#stop)
- [openBrowser](#openbrowser)

---

### active

属性 \ 访问: `r`

**说明**

服务器是否运行中

服务器运行中时返回真。只读。

**相关:** [WebServer.url](WebServer.md#url)

---

### url

属性 \ 访问: `r`

**说明**

监听 URL

表示服务器的监听 URL ( `http://host:port/` 形式 )。未运行时
为空字符串。只读。

**相关:** [WebServer.active](WebServer.md#active)

---

### register

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | 指定分配处理器的路径前缀。 |
| `handler` | `&nbsp;` | 指定 `handler(req)` 形式的处理器函数。 |

**说明**

注册动态处理器

对指定的 prefix 注册动态处理器。匹配按最长匹配
进行。注册到相同 prefix 时会被覆盖。

**相关:** [WebServer.unregister](WebServer.md#unregister)

---

### registerPanel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 面板的标识符。是覆盖、解除的键。 |
| `label` | `&nbsp;` | 显示在标签页上的名称。 |
| `path` | `&nbsp;` | 面板内容的 URL 路径。指定**以 `/` 开头的服务器上的路径**<br>( 不是本地文件路径 )。非法时不会<br>注册，理由会输出到日志。 |

**说明**

向内置 UI 添加面板 ( 标签页 )

在 `-replweb` 的内置浏览器 UI ( Console / Watch / Pad ) 的右侧，
**把项目自有的面板作为 1 个标签页添加进来**。事先用自己的页面
通过 [serveStatic](WebServer.md#servestatic) 提供，并把其路径传给
`path`。

内容会**以 iframe 加载**。之所以不采用向内置页面注入脚本的
方式，是为了不让项目依赖内置 UI 的内部 DOM
( 避免每次这边更改 UI 时项目就坏掉 )。面板是同源的，
因此可以用 `fetch` 或 `EventSource` 自由访问服务器
( 内置的 `/cmd` `/watch` `/pad/exec`，以及自己用
[register](WebServer.md#register) 注册的端点 )。

用相同的 `id` 重新调用会覆盖。注册、解除会**立即反映到
已打开的页面** ( 标签页增减 )。面板的内容**会在第一次打开
该标签页时加载**，因此即使注册很重的工具，启动也不会变慢。

```tjs
WebServer.serveStatic("/tool/", "web/");
WebServer.registerPanel("mytool", "案件ツール", "/tool/tool.html");
```

**相关:** [WebServer.unregisterPanel](WebServer.md#unregisterpanel)

---

### unregisterPanel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 要删除的面板的标识符。 |

**返回值**

找到并删除面板时返回 1，未找到时返回 0。

**说明**

从内置 UI 移除面板

删除用 [registerPanel](WebServer.md#registerpanel) 添加的标签页。
从已打开的页面中也会立即消失。

**相关:** [WebServer.registerPanel](WebServer.md#registerpanel)

---

### unregister

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | 指定要删除的处理器的前缀。 |

**返回值**

找到并删除处理器时返回 1，未找到时返回 0。

**说明**

删除动态处理器

删除用 [WebServer.register](WebServer.md#register) 注册的处理器。

**相关:** [WebServer.register](WebServer.md#register)

---

### serveStatic

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | 指定作为静态文件服务对象的路径前缀。 |
| `storageDir` | `&nbsp;` | 指定作为提供来源的存储目录。 |

**说明**

挂载静态文件服务

把对 prefix 以下的 GET 请求，从将相对路径拼接到 storageDir 后的存储中提供。
相对路径中包含 `..` 时返回 403。

**相关:** [WebServer.unserveStatic](WebServer.md#unservestatic)

---

### unserveStatic

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `prefix` | `&nbsp;` | 指定要删除的静态文件服务的前缀。 |

**返回值**

找到并删除挂载时返回 1，未找到时返回 0。

**说明**

卸载静态文件服务

删除用 [WebServer.serveStatic](WebServer.md#servestatic) 注册的
静态文件服务挂载。

**相关:** [WebServer.serveStatic](WebServer.md#servestatic)

---

### broadcast

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `channel` | `&nbsp;` | 指定推送目标的通道名。 |
| `text` | `&nbsp;` | 指定要推送的文本。 |

**说明**

向 SSE 订阅者推送

向订阅着 `/sub/<channel>` 的所有 SSE 客户端 push text。
text 可以包含多行。

---

### start

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `port` | `8899` | 指定监听端口号。 |

**返回值**

返回启动后的运行状态。

**说明**

启动服务器

在 127.0.0.1 上启动服务器。

**相关:** [WebServer.startAt](WebServer.md#startat) / [WebServer.stop](WebServer.md#stop)

---

### startAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `host` | `&nbsp;` | 指定监听主机。 |
| `port` | `&nbsp;` | 指定监听端口号。 |

**返回值**

返回启动后的运行状态。

**说明**

启动指定了主机的服务器

在显式指定的主机上启动服务器。指定 "0.0.0.0" 时会监听所有
网络接口。

**相关:** [WebServer.start](WebServer.md#start) / [WebServer.stop](WebServer.md#stop)

---

### stop

方法

**说明**

停止服务器

停止服务器。关闭连接中的客户端，结束 accept 线程。

**相关:** [WebServer.start](WebServer.md#start)

---

### openBrowser

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `url` | `""` | 指定要打开的 URL。<br>省略时使用运行中的服务器的 URL。 |
| `appMode` | `true` | 指定为真时，首先按 Edge → Chrome 的顺序尝试用 `--app=` 以<br>应用模式启动，都不存在时则用 OS 的默认浏览器打开。 |

**返回值**

返回成功与否。

**说明**

用浏览器打开

用浏览器打开指定的 url。

**相关:** [WebServer.url](WebServer.md#url)

---
