# TemporaryFiles

管理临时文件的类
预先将要临时化的文件登记为条目，
之后废弃该对象，
便会在文件关闭时自动删除

## 成员列表

### 构造函数

- [TemporaryFiles](#temporaryfiles)

### 方法

- [entry](#entry)
- [entryFolder](#entryfolder)

---

### TemporaryFiles

构造函数

**说明**

构造函数

---

### entry

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |

**返回值**

注册成功则为 true

**说明**

将文件登记为条目

---

### entryFolder

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `foldername` | `&nbsp;` | 文件夹名 |

**返回值**

注册成功则为 true

**说明**

将文件夹登记为条目

---
