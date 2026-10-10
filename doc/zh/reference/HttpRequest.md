# HttpRequest

HttpRequest 类

提供基于 HTTP/HTTPS 的异步通信功能。
文件的收发处理在后台执行。
基于伪代码的手册

## 成员列表

### 构造函数

- [HttpRequest](#httprequest)

### 属性

- [readyState](#readystate)
- [response](#response)
- [responseData](#responsedata)
- [status](#status)
- [statusText](#statustext)
- [contentType](#contenttype)
- [contentTypeEncoding](#contenttypeencoding)
- [contentLength](#contentlength)

### 方法

- [open](#open)
- [setRequestHeader](#setrequestheader)
- [send](#send)
- [sendStorage](#sendstorage)
- [abort](#abort)
- [getAllResponseHeaders](#getallresponseheaders)
- [getResponseHeader](#getresponseheader)
- [getResponseText](#getresponsetext)
- [onReadyStateChange](#onreadystatechange)
- [onProgress](#onprogress)

### 常量

- [UNINITIALIZED](#uninitialized)
- [OPEN](#open)
- [SENT](#sent)
- [RECEIVING](#receiving)
- [LOADED](#loaded)

---

### HttpRequest

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 用于线程同步处理的父窗口 |
| `cert` | `true` | HTTP 通信时是否进行证书检查。设为 false 时强制允许。 |
| `agentName` | `"KIRIKIRI"` | HTTP 通信时的 agent 名 |

**说明**

构造函数

---

### readyState

属性 \ 访问: `r`

**说明**

通信状态。只读

---

### response

属性 \ 访问: `r`

**说明**

响应。只读。

---

### responseData

属性 \ 访问: `r`

**说明**

响应。只读

---

### status

属性 \ 访问: `r`

**说明**

响应的 HTTP 状态码。只读

---

### statusText

属性 \ 访问: `r`

**说明**

响应的 HTTP 状态字符串

---

### contentType

属性 \ 访问: `r`

**说明**

响应的 Content-Type (不包含编码指定)

---

### contentTypeEncoding

属性 \ 访问: `r`

**说明**

响应的 Content-Type 的编码指定

优先采用 HTTP 头的指定，但在未指定且接收数据为 text/html 的情况下，
也会参照文件开头的 META 指定。

---

### contentLength

属性 \ 访问: `r`

**说明**

响应的 Content-Length

HTTP 头中不存在时，在文件下载完成后确定大小。

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `method` | `&nbsp;` | 访问方法 |
| `url` | `&nbsp;` | 请求目标的 URL |
| `userName` | `void` | 用户名。指定后会附加认证头 |
| `password` | `void` | 密码 |

**说明**

用指定的方法向指定的 URL 发起请求

※始终以异步方式调用

---

### setRequestHeader

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | HTTP 头名称 |
| `value` | `&nbsp;` | 值 |

**说明**

添加发送时附带的 HTTP 头

---

### send

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `data` | `void` | 要发送的数据<br>octet 时  : 直接发送<br>字符串时 : 按规定的编码处理后发送<br>其他     : 不发送数据 |
| `storeStorage` | `void` |  |

**说明**

发送请求。发送处理以异步方式执行。

出错时也不会发生异常，请根据 readyState 和 status 判断。

---

### sendStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 要发送的文件数据 |
| `storeStorage` | `void` |  |

**说明**

发送请求。收发以异步方式执行。

出错时也不会发生异常，请根据 readyState 和 status 判断。

---

### abort

方法

**说明**

取消当前正在执行的收发

---

### getAllResponseHeaders

方法

**返回值**

存储了 HTTP 头的字典

**说明**

获取所有 HTTP 头

---

### getResponseHeader

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | HTTP 头标签名 |

**返回值**

HTTP 头的值

**说明**

获取指定的 HTTP 头

---

### getResponseText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `encoding` | `void` | 编码指定。省略时遵循 Content-type 的指定。 |

**说明**

以文本形式获取响应

---

### onReadyStateChange

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `readyState` | `&nbsp;` | 新的状态 |

**说明**

readyState 变化时的事件

------------------------------------ ------------------------------------

---

### onProgress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `upload` | `&nbsp;` | 发送中为 true |
| `percent` | `&nbsp;` | 进度状态 (0~100%) |

**说明**

数据收发事件

---

### UNINITIALIZED

常量

值: `0`

**说明**

readyState 初始状态

---

### OPEN

常量

值: `1`

**说明**

readyState 处理开始

---

### SENT

常量

值: `2`

**说明**

readyState 请求发送

---

### RECEIVING

常量

值: `3`

**说明**

readyState 接收中

---

### LOADED

常量

值: `4`

**说明**

readyState 读取完成

---
