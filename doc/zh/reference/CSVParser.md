# CSVParser

基于伪代码的手册

Copyright 2005-2009 GoWatanabe

## 成员列表

### 构造函数

- [CSVParser](#csvparser)

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

### CSVParser

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 转发事件的目标。未指定时发送给自己 |
| `separator` | `&nbsp;` | 分隔符。默认为 "," |
| `newline` | `&nbsp;` | 中途被分隔时的数据中的换行符。默认为 "\\r\\n" |

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
| `readmode` | `false` | 读取模式<br>typeof readmode == "String"  : 作为相当于 Array.load 的文本读取处理运行<br>typeof readmode == "Integer" : 为 true 时作为 UTF-8 读取模式运行，否则为 CP_ACP 文本读取<br>※在插件编译时加上 /D:CSVPARSER_DEFAULT_TEXTSTREAM=1，省略时的默认值就会变成 readmode='' |

**说明**

初始化处理目标文本

---

### getNextLine

方法

**返回值**

列数据 (Array)

**说明**

以数组形式获取下一行的信息

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
| `readmode` | `&nbsp;` | 读取模式（详细说明请参照 initStorage 项） |

**说明**

对文本执行解析处理。

---

### doLine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `columns` | `&nbsp;` | 列数据 (Array) |
| `lineNo` | `&nbsp;` | 逻辑行号 (1~) |

**说明**

由 parse/parseStorage 调用的事件

----------------------------------

---
