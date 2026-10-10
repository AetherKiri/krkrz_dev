# ResourceWriter

## 成员列表

### 构造函数

- [ResourceWriter](#resourcewriter)

### 方法

- [open](#open)
- [close](#close)
- [setLang](#setlang)
- [clear](#clear)
- [writeFromText](#writefromtext)
- [writeFromFile](#writefromfile)
- [writeFromOctet](#writefromoctet)

---

### ResourceWriter

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` |  |
| `clean` | `&nbsp;` |  |

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` | 文件名（exe 或 dll） |
| `clean` | `false` | 是否清除全部现有资源<br>基本上只能操作未被打开的文件<br>＞无法操作自己的 krkr.exe 以及通过 Plugins.link 链接的插件 |

**说明**

打开要操作的文件

---

### close

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `write` | `true` | 需要写出时为 true<br>当 write=false 时，writeFrom~ 及 clear 的处理会被全部取消，不会进行写出<br>即使 write=true，如果一次也没有调用 writeFrom~/clear，也不会进行写出 |

**说明**

关闭要操作的文件并实际写出

---

### setLang

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `primaryLang` | `&nbsp;` |  |
| `subLang` | `&nbsp;` |  |

**说明**

指定写出的语言

参数内容与 ResourceReader.setLang 相同

---

### clear

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 资源类型（字符串或数值，或指定 rt* 常量） |
| `name` | `&nbsp;` | 资源名（字符串或数值）<br>※即使调用此函数，在 close(true) 之前写出都会被保留 |

**说明**

删除目标资源

---

### writeFromText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 资源类型（字符串或数值，或指定 rt* 常量） |
| `name` | `&nbsp;` | 资源名（字符串或数值） |
| `text` | `&nbsp;` | （仅 writeFromText）对象的文本 |
| `utf8` | `false` | （仅 writeFromText）以 UTF-8 编码写出时为 true（为 false 时是 Unicode） |

**说明**

资源的写出

---

### writeFromFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `file` | `&nbsp;` |  |

---

### writeFromOctet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `oct` | `&nbsp;` |  |

---
