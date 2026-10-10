# Scripts

Scripts 类是管理 TJS2 相关方法和属性的类。无法从该类创建对象。

## 成员列表

### 属性

- [textEncoding](#textencoding)

### 方法

- [execStorage](#execstorage)
- [evalStorage](#evalstorage)
- [compileStorage](#compilestorage)
- [exec](#exec)
- [eval](#eval)
- [dump](#dump)
- [getTraceString](#gettracestring)
- [setCallMissing](#setcallmissing)
- [getClassNames](#getclassnames)
- [dumpStringHeap](#dumpstringheap)

---

### textEncoding

属性 \ 访问: `r/w`

**说明**

指定读取脚本时使用的文本编码

指定读取脚本时使用的文本编码。

当前可以指定的只有 "UTF-8" 或 "Shift_JIS" 之一。

---

### execStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要执行的存储。 |
| `mode` | `''` | 指定读取文件时的模式字符串。在 "o" 之后以十进制指定偏移量，则从文件的该字节位置开始读取。 |
| `context` | `global` | 指定执行上下文。 |

**返回值**

返回执行脚本的结果。

**说明**

执行存储上的脚本

读取指定的存储，并将其内容作为 TJS2 脚本执行。

脚本执行过程中发生的异常不会在该方法内捕获，因此可以在该方法的调用方捕获。

**相关:** [Scripts.evalStorage](Scripts.md#evalstorage)

---

### evalStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定要评估的存储。 |
| `mode` | `''` | 指定读取文件时的模式字符串。在 "o" 之后以十进制指定偏移量，则从文件的该字节位置开始读取。 |
| `context` | `global` | 指定执行上下文。 |

**返回值**

返回对表达式求值的结果。

**说明**

对存储上的表达式求值

读取指定的存储，并将其内容作为 TJS2 表达式求值。

脚本执行过程中发生的异常不会在该方法内捕获，因此可以在该方法的调用方捕获。

**相关:** [Scripts.execStorage](Scripts.md#execstorage)

---

### compileStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `inputfile` | `&nbsp;` | 指定要编译的存储。 |
| `outputfile` | `&nbsp;` | 指定输出的字节码存储。 |
| `isresult` | `false` | 指定是否需要返回值。 |
| `outputdebug` | `false` | 指定是否包含调试信息。 |
| `isexpression` | `false` | 指定是否为表达式。 |

**说明**

编译存储上的脚本

读取指定的存储，将其内容编译后作为字节码文件输出。

编译后的字节码文件可以用 execStorage 或 evalStorage 像普通脚本一样执行。

**相关:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.evalStorage](Scripts.md#evalstorage)

---

### exec

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `script` | `&nbsp;` | 以字符串指定要执行的脚本。 |
| `name` | `''` | 指定用于错误消息的文件名 |
| `linesof` | `0` | 指定用于错误消息的行号 |
| `context` | `global` | 指定执行上下文。 |

**返回值**

返回执行脚本的结果。

**说明**

执行脚本

将 script 指定的字符串作为 TJS2 脚本执行。

脚本执行过程中发生的异常不会在该方法内捕获，因此可以在该方法的调用方捕获。

**相关:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.eval](Scripts.md#eval)

---

### eval

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `expression` | `&nbsp;` | 以字符串指定要执行的表达式。 |
| `name` | `''` | 指定用于错误消息的文件名 |
| `linesof` | `0` | 指定用于错误消息的行号 |
| `context` | `global` | 指定执行上下文。 |

**返回值**

返回对表达式求值的结果。

**说明**

表达式求值

将 expression 指定的字符串作为 TJS2 表达式执行。

脚本执行过程中发生的异常不会在该方法内捕获，因此可以在该方法的调用方捕获。

**相关:** [Scripts.execStorage](Scripts.md#execstorage) / [Scripts.exec](Scripts.md#exec)

---

### dump

方法

**说明**

上下文的转储

将当前已由 TJS2 读取的脚本块中各上下文内容的详细信息输出到本地文件。主要会输出 VM 代码的反汇编结果。

输出文件会输出到与吉里吉里的可执行文件相同的文件夹中，其文件名是在吉里吉里的可执行文件上附加 .dump.txt 后得到的。

---

### getTraceString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `limit` | `0` | 指定获取历史记录的最大调用深度。省略该参数或指定 0 时，将获取能够获取的全部历史记录。 |

**返回值**

将调用历史记录字符串化后的内容

**说明**

获取调用历史记录

以字符串形式获取方法的调用历史记录。可以获取调用该方法这一时刻的历史记录。

要使用该方法，必须已通过命令行选项使 -debug (调试模式) 处于启用状态。调试模式无效时，该方法返回空字符串。

返回的字符串例如 'messagelayer.tjs(1561)[(function) addButton] <-- mainwindow.tjs(4463)[(function expression) (anonymous)] <-- conductor.tjs(427)[(function) onTag] <-- conductor.tjs(95)[(function) timerCallback]' 这样的内容。

---

### setCallMissing

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `missing` | `&nbsp;` | 找不到成员时被调用的处理器。 |

**说明**

注册找不到成员时被调用的处理器

注册找不到成员时被调用的处理器。

---

### getClassNames

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obect` | `&nbsp;` | 要获取类名的对象。 |

**返回值**

类名的数组

**说明**

获取类名

从对象获取类名。

---

### dumpStringHeap

方法

**说明**

字符串堆的转储

将 TJS2 运行时管理的字符串堆内容进行调试输出。
只能在以启用 `TJS_DEBUG_DUMP_STRING` 的方式构建的引擎中调用。
专用于内存泄漏排查等调试用途。

---

## 插件扩展: json

伪代码形式的手册

### 成员列表

#### 方法

- [evalJSON](#evaljson)
- [evalJSONStorage](#evaljsonstorage)
- [saveJSON](#savejson)
- [toJSONString](#tojsonstring)

---

### evalJSON

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `jsonText` | `&nbsp;` | 存放 JSON 的文本 |

**返回值**

Array 或 Dictionary

**说明**

解析 JSON 字符串并返回 Array 或 Dictionary

---

### evalJSONStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `jsonFile` | `&nbsp;` | 存放 JSON 的文本文件的文件名 |
| `utf8` | `false` | 输入编码指定。true 则为 UTF-8，false 则为当前代码页 |

**返回值**

Array 或 Dictionary

**说明**

解析 JSON 文件并返回 Array 或 Dictionary

---

### saveJSON

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `jsonFile` | `&nbsp;` | 存放目标文件 |
| `obj` | `&nbsp;` | 保存目标对象 |
| `utf8` | `false` | 输出编码指定。true 则为 UTF-8，false 则为当前代码页 |
| `newline` | `0` | 换行符 0:CRLF 1:LF |

**说明**

以 JSON 格式保存数据

---

### toJSONString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` |  |
| `newline` | `0` | 换行符 0:CRLF 1:LF |

**返回值**

JSON 格式的文本

**说明**

将数据转换为 JSON 格式的字符串

---

## 插件扩展: saveStruct

### 成员列表

#### 方法

- [toStructString](#tostructstring)

---

### toStructString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `target` | `&nbsp;` | 要字符串化的对象（字典、数组以外的 int/real/string/octet/null/void 也可以） |
| `newline` | `1` | 换行符 0:CRLF 1:LF |
| `option` | `ssoIndent\|ssoSort` | 格式化选项 sso* 的组合（后述）或直接指定数值 |

**返回值**

返回遵循 saveStruct 形式的字符串

**说明**

注意 option 的默认值与 Array/Dictionary 不同（设想用于调试用途）

---

## 插件扩展: scriptsEx

### 成员列表

#### 方法

- [getObjectKeys](#getobjectkeys)
- [getObjectCount](#getobjectcount)
- [getObjectContext](#getobjectcontext)
- [isNullContext](#isnullcontext)
- [equalStruct](#equalstruct)
- [equalStructNumericLoose](#equalstructnumericloose)
- [foreach](#foreach)
- [getMD5HashString](#getmd5hashstring)
- [clone](#clone)
- [rehash](#rehash)
- [propSet](#propset)
- [propGet](#propget)
- [safeEvalStorage](#safeevalstorage)

---

### getObjectKeys

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 目标对象 |

**返回值**

存放键的数组

**说明**

返回对象的成员名列表

---

### getObjectCount

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 目标对象 |

**返回值**

返回个数

**说明**

返回对象的成员个数

---

### getObjectContext

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 目标对象 |

**返回值**

上下文对象

**说明**

返回对象的上下文

---

### isNullContext

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 目标对象 |

**返回值**

上下文为 null

**说明**

判定对象的上下文

---

### equalStruct

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj1` | `&nbsp;` | 对象 1 |
| `obj2` | `&nbsp;` | 对象 2 |

**返回值**

相等则为 true

**说明**

比较对象之间是否相等。字典/数组的情况下会递归比较其中的元素

---

### equalStructNumericLoose

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj1` | `&nbsp;` | 对象 1 |
| `obj2` | `&nbsp;` | 对象 2 |

**返回值**

相等则为 true

**说明**

比较对象之间是否相等。字典/数组的情况下会递归比较其中的元素

数值会进行宽松比较（将 0.0 和 0 视为相等）

---

### foreach

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 处理目标对象(字典或数组) |
| `func` | `&nbsp;` | 调用函数。以 func(key, value, args*) 的形式调用。<br>匿名函数等上下文为 null 时，会自动在 this 上下文中运行<br>函数返回某种值时，处理会被中断 |
| `args*` | `&nbsp;` |  |

**返回值**

中断时返回的值

**说明**

遍历对象的全部成员

---

### getMD5HashString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `octet` | `&nbsp;` | 目标 octet |

**返回值**

哈希值（32 个字符的十六进制哈希字符串（小写））

**说明**

获取 octet 的 MD5 哈希值

---

### clone

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 克隆来源<br>void/数值/字符串/octet 会原样返回原值。<br>字典、数组对象会返回 deep copy 处理后的结果。嵌套会递归处理。<br>一般对象如果存在 "clone" 方法，则返回其返回值，否则原样返回原值 |

**说明**

返回值的克隆。

---

### rehash

方法

**说明**

调用 TJSDoRehash()

为基于 TJSCustomObject 的对象的哈希表大小设置重建标志。
（字典以及大部分类和实例的对象都属于处理对象）

说明：
哈希表大小由该对象持有的元素个数决定。
设置标志后，会在向对象写入某些内容的时机进行重新计算，
仅在表大小发生变化时才会进行重建。（大小 = 2^(元素个数的位数+2) 左右？）
平时，吉里吉里会定期（空闲时且距上次已过 1.5 秒以上时）
调用 TJSDoRehash()，所以并不需要特别在意，
但在不经过空闲状态而大量添加元素的情况下，
用计数器以每数千~数万次一次之类的间隔来调用，应该会比较有效。

---

### propSet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` | 目标对象 |
| `member` | `&nbsp;` | 成员名(typeof member == "Integer" 时调用 Prop{Set,Get}ByNum) |
| `value` | `&nbsp;` | 要设置的值(仅 propSet) |
| `flag` | `Scripts.pfMemberEnsure` | 标志(Scripts.pf* 的"\|"(or)组合指定，或 0)<br>Scripts.pfMemberEnsure    : (set 时)指定新增成员时使用（没有指定时只能改写既有成员）<br>Scripts.pfMemberMustExist : (get 时)成员不存在时出错（字典的 undefined 也不会返回 void，而是出错）<br>Scripts.pfIgnoreProp      : (get/set 时)忽略属性行为（与 TJS 的 & 指定行为相同）<br>Scripts.pfHiddenMember    : (set 时)指定隐藏成员（在 assignStruct/saveStruct 等 EnumMembers 系列处理中会被忽略）<br>Scripts.pfStaticMember    : (set 时)指定 Static 成员（用于类对象等） |

**返回值**

获取到的值(仅 propGet，set 时为 void)

**说明**

调用指定对象的 PropSet/Get

---

### propGet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `obj` | `&nbsp;` |  |
| `member` | `&nbsp;` |  |
| `flag` | `Scripts.pfMemberMustExist` |  |

---

### safeEvalStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 要评估的存储（字节码二进制不可／以 saveStruct 带 (const) 保存的字典／数组为对象） |
| `mode` | `&nbsp;` | 模式字符串 |
| `context` | `&nbsp;` | 执行上下文 |

**返回值**

评估后的数据

**说明**

安全地评估带 (const) 的字典／数组

TJS_STATICMEMBER

---

## 插件扩展: windowEx

Scripts 扩展

### 成员列表

#### 方法

- [setEvalErrorLog](#setevalerrorlog)

---

### setEvalErrorLog

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` | 输出许可 |

**返回值**

原值

**说明**

抑制 Scripts.eval 的错误日志输出

将 enabled 设置为 false 后，Scripts.eval 的评估处理
会改为经由 TVPExecuteExpression 进行，发生异常时不会输出日志
请注意，随着吉里吉里版本升级，规格可能会发生变化

---
