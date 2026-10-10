# Dictionary

## 成员列表

### 方法

- [saveStruct2](#savestruct2)
- [toStructString](#tostructstring)

---

### saveStruct2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 存放目标文件 |
| `utf8` | `false` | 输出编码指定。true 则为 UTF-8，false 则为当前代码页 |
| `newline` | `0` | 换行符 0:CRLF 1:LF |
| `option` | `0` | 格式化选项 sso* 的组合（后述）或直接指定数值 |

**说明**

以遵循 saveStruct 的形式保存数据

---

### toStructString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `newline` | `1` | 换行符 0:CRLF 1:LF |
| `option` | `0` | 格式化选项 sso* 的组合（后述）或直接指定数值 |

**返回值**

返回遵循 saveStruct 形式的字符串

---
