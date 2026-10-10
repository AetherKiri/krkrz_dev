# XMLParser

基于伪代码的手册

Copyright 2005-2009 GoWatanabe

由 expat 进行处理，并自动执行方法的回调处理
具体的 DOM 实现示例请参照 XML.tjs

## 成员列表

### 属性

- [errorCode](#errorcode)
- [errorString](#errorstring)
- [currentByteIndex](#currentbyteindex)
- [currentLineNumber](#currentlinenumber)
- [currentColumnNumber](#currentcolumnnumber)
- [currentButeCount](#currentbutecount)

### 方法

- [parse](#parse)
- [parseStorage](#parsestorage)

---

### errorCode

属性 \ 访问: `r/w`

**说明**

错误代码的数值

---

### errorString

属性 \ 访问: `r/w`

**说明**

错误代码的字符串

---

### currentByteIndex

属性 \ 访问: `r/w`

**说明**

当前的字节索引

---

### currentLineNumber

属性 \ 访问: `r/w`

**说明**

当前的行号

---

### currentColumnNumber

属性 \ 访问: `r/w`

**说明**

当前的行号

---

### currentButeCount

属性 \ 访问: `r/w`

**说明**

当前的字节计数

---

### parse

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文本。省略时对当前设置中的文本进行处理 |

**说明**

对文本执行解析处理。

---

### parseStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文本的文件名 |

**说明**

对文本执行解析处理。

---
