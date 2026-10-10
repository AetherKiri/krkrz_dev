# Zip

基于伪代码的手册

ZIP 压缩类

## 成员列表

### 构造函数

- [Zip](#zip)

### 方法

- [open](#open)
- [add](#add)
- [close](#close)

---

### Zip

构造函数

**说明**

构造函数

进行 LZMA 压缩

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |
| `overwrite` | `0` | 0：通常创建 1：覆盖 2：追加写入 |

**说明**

为写入而打开 ZIP 归档

---

### add

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `srcfile` | `&nbsp;` | 要追加的文件（吉里吉里存储名） |
| `destfile` | `&nbsp;` | 归档中的名称（归档内路径名） |
| `commpressLevel` | `void` |  |
| `password` | `void` | 指定加密密码 |
| `compressionMethod` | `Zip.CompressionMethodDeflate` | 压缩方法 |
| `clearDate` | `false` | 将日期指定置空的指定。默认为存储文件的日期 |

**返回值**

追加成功时为 true

**说明**

向归档追加文件

---

### close

方法

**说明**

关闭 ZIP 归档

---
