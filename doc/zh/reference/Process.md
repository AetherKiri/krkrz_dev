# Process

基于伪代码的手册

提供启动外部应用并等待其结束的机制。

## 成员列表

### 属性

- [status](#status)

### 方法

- [execute](#execute)
- [commandExecute](#commandexecute)
- [terminate](#terminate)
- [sendSignal](#sendsignal)
- [onExecuted](#onexecuted)
- [onOutput](#onoutput)

---

### status

属性 \ 访问: `r`

**说明**

当前状态

0:未执行
1:执行中

---

### execute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 程序 |
| `param` | `void` | 参数 |
| `folder` | `void` | 执行时文件夹 (未指定时为当前文件夹) |

**返回值**

启动成功时为 true

**说明**

在后台执行外部程序

处理结束后会发生 onExecuted 事件。

---

### commandExecute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 程序 |
| `param` | `void` | 参数 |
| `folder` | `void` | 执行时文件夹 (未指定时为当前文件夹) |

**返回值**

启动成功时为 true

**说明**

带控制台输出获取的命令行程序的执行

每当控制台按行输出时，就会发生 onOutput 事件。
处理结束后会发生 onExecuted 事件。

---

### terminate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `endCode` | `&nbsp;` | 退出代码 |

**说明**

强制结束正在执行的外部程序

---

### sendSignal

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `isBreak` | `&nbsp;` | 发送 Ctrl+Break 而不是 Ctrl+C |

**返回值**

成功时为 true

**说明**

发送 Ctrl+C 事件 (experimental:并非在所有环境中都能运行)

---

### onExecuted

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `endCode` | `&nbsp;` | 退出代码 |

**说明**

事件:shell 执行结束

--------------------------------------------------------------------------

---

### onOutput

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `line` | `&nbsp;` | 行号 |
| `text` | `&nbsp;` | 输出文本（以 1 行为单位） |

**说明**

事件:控制台输出

---
