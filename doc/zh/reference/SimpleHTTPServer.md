# SimpleHTTPServer

基于伪代码的手册

## 成员列表

### 构造函数

- [SimpleHTTPServer](#simplehttpserver)

### 属性

- [port](#port)
- [timeout](#timeout)
- [codepage](#codepage)

### 方法

- [start](#start)
- [start](#start)
- [onRequest](#onrequest)

### 常量

- [cpACP](#cpacp)
- [cpOEM](#cpoem)
- [cpUTF8](#cputf8)
- [cpSJIS](#cpsjis)
- [cpEUC](#cpeuc)
- [cpJIS](#cpjis)

---

### SimpleHTTPServer

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `port` | `0` | 使用的端口号（为 0 时自动分配） |
| `timeout` | `10` | onRequest 回调的超时时间 (sec) |
| `codepage` | `&nbsp;` |  |

**说明**

构造函数

---

### port

属性 \ 访问: `r`

---

### timeout

属性 \ 访问: `r`

---

### codepage

属性 \ 访问: `r/w`

**说明**

无法按会话更改代码页，因此不建议中途更改

---

### start

方法

**返回值**

端口号

**说明**

启动服务

---

### start

方法

**说明**

停止服务

---

### onRequest

方法

**返回值**

response = %[
status:状态码（可省略，没有错误时自动为 200）
content_type: Content-Type 名
error_type:错误的种类（在没有 text/file/binary 时有效）
error_desc:错误的说明（在没有 text/file/binary 时有效）
redirect: 重定向时的 URI（可省略）

以下为互斥（任选其一，从上到下优先）
text:返回的文本（由 codepage 自动编码）
file:返回的文件
binary:返回的二进制（Array 或 Octet）
];

**说明**

请求处理（事件）

---

### cpACP

常量

值: `CP_ACP`

**说明**

代码页（静态值）

---

### cpOEM

常量

值: `CP_OEMCP`

---

### cpUTF8

常量

值: `CP_UTF8`

---

### cpSJIS

常量

值: `CP_932`

---

### cpEUC

常量

值: `CP_20932`

---

### cpJIS

常量

值: `CP_50220`

**说明**

51932

---
