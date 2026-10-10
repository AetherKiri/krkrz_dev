# KAGParser

基于伪代码的手册

吉里吉里Z KAGParserEx 插件。

提供解析 KAG 剧本文件的 KAGParser 类。
用 Plugins.link("KAGParserEx.dll") 链接后，KAGParser 类会被替换为本插
件的扩展版 ( 断开链接后恢复原状 )。

KAGParser 从 KAG 剧本的开头 ( 或指定的标签 ) 开始解释，
每次调用 getNextTag() 都会将“下一个标签”作为字典返回，是一个词法解析器。
它本身不进行文字的显示和标签的执行 ( 由 KAG3 的 MainWindow 等
使用方解释并执行 getNextTag() 返回的标签 )。

使用示例:
var parser = new KAGParser();
parser.loadScenario("first.ks");
parser.goToLabel("*start");
var tag;
while((tag = parser.getNextTag()) !== void) {
// tag.tagname 中为标签名，其他成员中为属性
}

getNextTag() 返回的字典中，标签名作为 tagname 成员，标签的属性
以“属性名 => 值 ( 字符串 )”的形式存放。正文会逐个字符作为
tagname 为 "ch" 的伪标签 ( text 成员中为文字 ) 返回，换行会作为
tagname 为 "r" 的伪标签 ( 行尾带 eol=true ) 返回。

当 processSpecialTags 为真 ( 默认 ) 时，以下系统标签会在解析器内部
处理，不会出现在 getNextTag() 的返回值中:
if / ignore / elsif / else / endif / endignore ( 条件分支 )、
macro / endmacro / erasemacro ( 宏的记录、删除 )、
pmacro / erasepmacro ( 参数宏的注册、删除 )、
jump / call / return ( 剧本内跳转、调用 )、
emb ( 嵌入表达式的求值结果 )。

相对原始 KAGParser ( 吉里吉里Z 引擎本体内置版 ) 的扩展点:
- 通过 multiLineTagEnabled 属性进行标签的多行记述
( 在行尾放置 " \"，并将下一行的开头以 ";" 开始 )
- 在 getNextTag() 的返回值中新增 taglist 成员 ( 按记载顺序存放
标签名的数组 )
- 参数宏展开功能 ( paramMacros 属性 / pmacro、
erasepmacro 系统标签 )。已注册的参数名出现在标签中时，
会按在该处插入了已注册参数列来处理
- 为 emb 标签新增 escape 参数。指定 escape=false 时，
会不转义 "[~]" 形式的求值结果，而将其作为普通标签求值
- 写在宏展开的“*”( 剩余的全体参数 ) 之前的参数也会
有效 ( 在原始版中会被覆盖而消失 )

## 成员列表

### 构造函数

- [KAGParser](#kagparser)

### 属性

- [curStorage](#curstorage)
- [curLabel](#curlabel)
- [curLine](#curline)
- [curPos](#curpos)
- [curLineStr](#curlinestr)
- [processSpecialTags](#processspecialtags)
- [ignoreCR](#ignorecr)
- [debugLevel](#debuglevel)
- [macros](#macros)
- [paramMacros](#parammacros)
- [macroParams](#macroparams)
- [mp](#mp)
- [callStackDepth](#callstackdepth)
- [multiLineTagEnabled](#multilinetagenabled)

### 方法

- [loadScenario](#loadscenario)
- [goToLabel](#gotolabel)
- [callLabel](#calllabel)
- [getNextTag](#getnexttag)
- [assign](#assign)
- [clear](#clear)
- [store](#store)
- [restore](#restore)
- [clearCallStack](#clearcallstack)
- [interrupt](#interrupt)
- [resetInterrupt](#resetinterrupt)

---

### KAGParser

构造函数

**说明**

构造函数 ( 无参数 )

---

### curStorage

属性 \ 访问: `r/w`

**说明**

当前正在解析的剧本的存储名。设置值后会进行与 loadScenario() 相同的操作

---

### curLabel

属性 \ 访问: `r`

**说明**

最后经过的标签名（只读）

---

### curLine

属性 \ 访问: `r`

**说明**

当前正在解析的行号 ( 0 起点 )（只读）

---

### curPos

属性 \ 访问: `r`

**说明**

当前正在解析的行内的字符位置 ( 0 起点 )（只读）

---

### curLineStr

属性 \ 访问: `r`

**说明**

当前正在解析的行内容（只读）

---

### processSpecialTags

属性 \ 访问: `r/w`

**说明**

系统标签 ( if / macro / jump / emb 等 ) 是否在解析器内部处理。

设为假时，这些也会作为普通标签从 getNextTag() 返回。默认为真

---

### ignoreCR

属性 \ 访问: `r/w`

**说明**

设为真时会忽略剧本中的换行 ( 不返回 "r" 伪标签 )。默认为假

---

### debugLevel

属性 \ 访问: `r/w`

**说明**

调试输出的级别。0 ( 不输出 )、1 ( 简易 )、2 ( 详细 ) 之一

---

### macros

属性 \ 访问: `r`

**说明**

已记录的宏的字典 ( 宏名 => 宏内容的字符串 )（只读）

---

### paramMacros

属性 \ 访问: `r`

**说明**

参数宏的字典（只读、KAGParserEx 扩展）。

按“参数名 => [ 参数名, 值, 参数名, 值, ... ]”的形式
注册后，已注册的参数名出现在标签中时，会按在该处插入了
注册内容来处理。值开头的 % 和 & 会在运行时展开。
也可以用 pmacro / erasepmacro 系统标签注册、删除

---

### macroParams

属性 \ 访问: `r`

**说明**

当前正在执行的宏所接收的参数的字典（只读）

---

### mp

属性 \ 访问: `r`

**说明**

macroParams 的别名（只读）

---

### callStackDepth

属性 \ 访问: `r`

**说明**

由 callLabel() 形成的调用栈深度（只读）

---

### multiLineTagEnabled

属性 \ 访问: `r/w`

**说明**

是否启用标签的多行记述 ( KAGParserEx 扩展 )。默认为假。

设为真后，在行尾放置 " \" ( 其前面需要 1 个以上的空白 )，
并将下一行的开头以 ";" 开始，即可将标签分成多行记述。
标签名必须记述在第 1 行

---

### loadScenario

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 要读取的剧本文件 ( .ks ) 的存储名 |

**说明**

读取剧本文件

解析位置会变为文件的开头。若已读取了相同的存储，
则不会进行重新读取。

---

### goToLabel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `label` | `&nbsp;` | 目标标签名。像 "*标签名" 这样在开头附加 * 来指定 |

**说明**

移动到指定标签

将解析位置移动到当前剧本文件内的指定标签位置。

---

### callLabel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `label` | `&nbsp;` | 目标标签名。像 "*标签名" 这样在开头附加 * 来指定 |

**说明**

将当前位置压入调用栈后移动到指定标签

可以用 return 系统标签返回到调用方位置。
当前的调用深度可以通过 callStackDepth 属性获取。

---

### getNextTag

方法

**返回值**

保存了标签信息的字典对象。到达剧本末尾时
为 void

**说明**

获取下一个标签

标签名存放在 tagname 成员，标签的属性以“属性名 => 值”的
形式存放。正文会作为 tagname="ch" ( text 成员中为 1 个字符 )、
换行会作为 tagname="r" ( 行尾带 eol=true ) 的伪标签返回。
存在由 interrupt() 发出的中断请求时，会返回 tagname="interrupt" 的
伪标签。

作为 KAGParserEx 扩展，新增了 taglist 成员 ( 按记载顺序排列
该字典中存放的标签名的数组 )。

返回的字典对象会被 KAGParser 在内部重复使用，因此若想
保留内容，请进行复制。

---

### assign

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 复制来源的 KAGParser 对象 |

**说明**

复制其他 KAGParser 对象的状态

---

### clear

方法

**说明**

清除状态

将已读取的剧本、调用栈、宏等状态
恢复为初始状态。

---

### store

方法

**返回值**

表示当前状态 ( 解析位置、调用栈、宏等 ) 的
字典对象

**说明**

将状态作为字典取出

将返回的字典保存起来并传给 restore()，即可恢复
状态。可用于保存到书签 ( 存档数据 )。

---

### restore

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dic` | `&nbsp;` | store() 返回的字典对象 |

**说明**

恢复用 store() 取出的状态

---

### clearCallStack

方法

**说明**

清除调用栈

丢弃所有由 callLabel() 压入的调用栈。

---

### interrupt

方法

**说明**

请求中断解析

在下一次 getNextTag() 返回标签的时机，会代替普通标签
返回 tagname="interrupt" 的伪标签。用于想从异步事件处理
等中断解析循环的场景。

---

### resetInterrupt

方法

**说明**

取消由 interrupt() 发出的中断请求

---
