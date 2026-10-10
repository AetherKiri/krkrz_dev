# LineParser

基于伪代码的手册

Copyright 2005-2009 GoWatanabe

## 成员列表

### 构造函数

- [LineParser](#lineparser)

### 属性

- [currentLineNumber](#currentlinenumber)

### 方法

- [init](#init)
- [initStorage](#initstorage)
- [getNextLine](#getnextline)
- [parse](#parse)
- [parseStorage](#parsestorage)
- [doLine](#doline)

---

### LineParser

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 转发事件的目标。未指定时发送给自己 |

**说明**

构造函数

---

### currentLineNumber

属性 \ 访问: `r/w`

**说明**

获取当前已处理的行号

---

### init

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文本 |

**说明**

初始化处理目标文本

---

### initStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文本的文件名 |
| `utf8` | `false` | 使用 UTF-8 文件时为 true |

**说明**

初始化处理目标文本

---

### getNextLine

方法

**返回值**

行

**说明**

以字符串形式获取下一行的信息

---

### parse

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文本。省略时对当前设置中的文本进行处理 |

**说明**

对文本执行解析处理。

每行调用 doLine() 事件。

---

### parseStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文本的文件名 |
| `utf8` | `false` | 使用 UTF-8 文件时为 true |

**说明**

对文本执行解析处理。

---

### doLine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 行的文本信息 |
| `lineNo` | `&nbsp;` | 行号 (从 1 开始) |

**说明**

由 parse/parseStorage 调用的事件

----------------------------------

---
