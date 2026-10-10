# Debug

Debug 类是提供吉里吉里调试相关功能的类。无法从该类创建对象。

吉里吉里的控制台日志的名称为 krkr.console.log。另外，发生硬件异常时创建的文件为 hwexcept.log。

这些日志文件默认位于项目目录。不过，如果项目目录是归档等无法写入的目录，则不会输出。

日志文件的输出目标可以通过 logLocation 属性更改。

## 成员列表

### 属性

- [logLocation](#loglocation)
- [logToFileOnError](#logtofileonerror)
- [clearLogFileOnError](#clearlogfileonerror)

### 方法

- [message](#message)
- [notice](#notice)
- [startLogToFile](#startlogtofile)
- [logAsError](#logaserror)
- [addLoggingHandler](#addlogginghandler)
- [removeLoggingHandler](#removelogginghandler)
- [getLastLog](#getlastlog)
- [prettyPrint](#prettyprint)

---

### logLocation

属性 \ 访问: `r/w`

**说明**

日志文件的输出目标

表示日志文件的输出目标目录。也可以写入值。

默认设置为数据保存位置 ( 命令行选项的 -datapath )。

更改该值后，之后的日志将作为该目录下的 *.console.log 被输出。

---

### logToFileOnError

属性 \ 访问: `r/w`

**说明**

发生错误时是否把控制台日志输出到文件

为真时，发生错误时将开始把控制台日志输出到文件。

为假时，即使发生错误也不会开始把日志输出到文件。

**相关:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### clearLogFileOnError

属性 \ 访问: `r/w`

**说明**

发生错误时是否清除控制台的日志文件

为真时，发生错误时将自动清除控制台的日志。

为假时不会清除，而是追加到既有的日志文件。

**相关:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.logToFileOnError](Debug.md#logtofileonerror)

---

### message

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `message` | `&nbsp;` | 指定要输出的消息。 |

**说明**

向控制台输出消息

向**控制台**输出消息。

---

### notice

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `message` | `&nbsp;` | 指定要输出的消息。 |

**说明**

向控制台输出重要消息

向**控制台**输出消息。

与 [Debug.message](Debug.md#message) 不同，在这里输出的消息，即使日志文件写入是从中途开始的，
也必定会被写入日志文件 ( 通过 Debug.message 输出的消息，只有回溯到一定程度为止的部分
会被写入 )。用于输出在回收日志文件时会有用的重要信息。

---

### startLogToFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `clear` | `false` | 指定真时会清除日志文件。<br>指定假时会追加到既有文件。 |

**说明**

开始输出控制台的日志

开始把控制台的日志输出到文件。

**相关:** [Debug.logToFileOnError](Debug.md#logtofileonerror) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### logAsError

方法

**说明**

像发生错误时一样开始把日志输出到文件

对于错误日志文件，让吉里吉里执行与发生错误时相同的动作。
也就是说，如果 [Debug.logToFileOnError](Debug.md#logtofileonerror) 为真，
就开始把控制台日志输出到文件。此时，如果
[Debug.clearLogFileOnError](Debug.md#clearlogfileonerror) 为真，
则清除文件。

与此相对，[Debug.startLogToFile](Debug.md#startlogtofile) 则无条件
开始把控制台日志输出到文件。

**相关:** [Debug.startLogToFile](Debug.md#startlogtofile) / [Debug.logToFileOnError](Debug.md#logtofileonerror) / [Debug.clearLogFileOnError](Debug.md#clearlogfileonerror)

---

### addLoggingHandler

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 指定日志处理器。 |

**说明**

添加日志处理器

注册每当错误日志被输出时调用的处理器。

处理器会以日志消息作为参数被调用。

即使在注册的方法内输出日志，也不会进行递归调用，而是被忽略。

---

### removeLoggingHandler

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `handler` | `&nbsp;` | 指定日志处理器。 |

**说明**

删除日志处理器

删除已注册的日志处理器。

---

### getLastLog

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `lines` | `void` | 指定要获取的行数。省略时会获取所保持日志的<br>最大行数部分。 |

**说明**

获取未输出的日志

获取尚未输出的日志。

---

### prettyPrint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `value` | `&nbsp;` | 指定要格式化的值。 |
| `depth` | `2` | 指定递归展开的深度。默认值为 2。 |
| `compact` | `false` | 指定真时变为紧凑的单行表记。默认值为假。 |

**返回值**

返回格式化结果的字符串。

**说明**

值的格式化显示

将任意 TJS 值 ( 包括字典数组或对象的内容 ) 格式化为易于阅读的字符串并返回。
用于 REPL 或日志输出中的调试用途。

---
