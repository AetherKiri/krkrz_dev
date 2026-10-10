# ResourceReader

基于伪代码的手册

## 成员列表

### 构造函数

- [ResourceReader](#resourcereader)

### 方法

- [open](#open)
- [close](#close)
- [setLang](#setlang)
- [isExistentResource](#isexistentresource)
- [readToText](#readtotext)
- [readToFile](#readtofile)
- [readToOctet](#readtooctet)
- [enumTypes](#enumtypes)
- [enumNames](#enumnames)
- [enumLangs](#enumlangs)

---

### ResourceReader

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` |  |

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `file` | `&nbsp;` | 文件名（exe 或 dll） |

**说明**

打开要操作的文件

---

### close

方法

**说明**

关闭要操作的文件

---

### setLang

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `primaryLang` | `&nbsp;` | 主语言 |
| `subLang` | `&nbsp;` | 副语言 |

**返回值**

设置的 WORD 值
两者均可指定 LANG_* 或 SUBLANG_* 的字符串或数值。
详情请搜索 MAKELANGID 等。

**说明**

指定读取的语言

---

### isExistentResource

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 资源类型（字符串或数值，或指定 rt* 常量） |
| `name` | `&nbsp;` | 资源名（字符串或数值） |

**返回值**

存在时返回 true

**说明**

资源是否存在

---

### readToText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 资源类型（字符串或数值，或指定 rt* 常量） |
| `name` | `&nbsp;` | 资源名（字符串或数值） |
| `utf8` | `false` | （仅 readToText）对象为 UTF-8 编码时为 true（为 false 时是 Unicode） |

**返回值**

为 void 时表示资源不存在，存在时每个函数返回的值不同

**说明**

读取资源

---

### readToFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `file` | `&nbsp;` |  |

**说明**

-> 写出的文件大小

---

### readToOctet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |

**说明**

-> 资源的 octet

---

### enumTypes

方法

**返回值**

[ type1, type2, ... ]

**说明**

获取资源类型列表

---

### enumNames

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 资源类型（字符串或数值，或指定 rt* 常量） |

**返回值**

[ name1, name2, ... ]

**说明**

获取资源名列表

---

### enumLangs

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 资源类型（字符串或数值，或指定 rt* 常量） |
| `name` | `&nbsp;` | 资源名（字符串或数值） |

**返回值**

[ lang1, lang2, ... ]
返回的语言是整合了 primaryLang、subLang 的数值，请注意。
如果想把这个值传给 setLang，请使用 setLang(lang&0x3FF, lang>>10)。

**说明**

获取资源语言列表

---
