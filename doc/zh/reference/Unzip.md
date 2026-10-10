# Unzip

ZIP 解压类

## 成员列表

### 构造函数

- [Unzip](#unzip)

### 方法

- [open](#open)
- [list](#list)
- [extract](#extract)
- [close](#close)

---

### Unzip

构造函数

**说明**

构造函数

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |
| `force_utf8` | `0` | 0：文件名的字符编码根据第一个文件自动判别 1：强制 UTF8 |

**说明**

为解压而打开 ZIP 归档

---

### list

方法

**返回值**

文件列表（文件信息的数组）
文件信息以字典的形式提供，包含以下信息
<dl>
<dt>filename <dd>归档内路径名
<dt>uncompressed_size <dd>解压后大小
<dt>compressed_size <dd>压缩后大小
<dt>crypted <dd>是否已加密
<dt>deflated <dd>是否已压缩
<dt>deflateLevel <dd>压缩级别
<dt>crc <dd>文件的 CRD
</dl>

**说明**

获取 ZIP 归档中包含的文件的信息

---

### extract

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `srcname` | `&nbsp;` | 解压源文件（归档内路径名） |
| `destfile` | `&nbsp;` | 解压目标文件（吉里吉里存储名） |
| `password` | `void` | 指定密码 |

**返回值**

解压成功时为 true

**说明**

文件的解压

---

### close

方法

**说明**

关闭 ZIP 归档

---
