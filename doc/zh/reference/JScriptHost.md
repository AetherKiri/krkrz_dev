# JScriptHost

JScript 执行用宿主。利用 IActiveScript 可以进行 JScript 的表达式求值与结果获取。
示例:
var js = new JScriptHost();
var r = js.eval("1+2"); // -> 3
js.addGlobal("tvp", global); // 将 TJS 的 global 对象添加到 JScript 侧
var v = js.eval("tvp.version");

## 成员列表

### 构造函数

- [JScriptHost](#jscripthost)

### 方法

- [eval](#eval)
- [addGlobal](#addglobal)
- [reset](#reset)
- [invoke](#invoke)
- [set](#set)
- [get](#get)
- [missing](#missing)

---

### JScriptHost

构造函数

**说明**

构造函数

生成并连接 JScript 引擎。

---

### eval

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `code` | `&nbsp;` | 要求值的 JScript 表达式字符串 |

**返回值**

求值结果 (数值/字符串/bool/IDispatch 包装 等)

**说明**

表达式求值

---

### addGlobal

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 在 JScript 侧引用的名称 |
| `obj` | `&nbsp;` | 要添加的对象 (TJS 对象；作为 IDispatch 公开) |

**说明**

全局对象的添加（注册到 JScript 内部的 namedObject 列表）

---

### reset

方法

**说明**

引擎的重新初始化

重新初始化脚本状态。

---

### invoke

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 方法名 |
| `...` | `&nbsp;` | 后续参数 |

**说明**

方法的执行

------------------------------------------------------------------------------- 针对 JScript 的 global 的直接操作方法 对通过 GetScriptDispatch() 获取的 IDispatch 进行与 WIN32OLE 相同的操作。 -------------------------------------------------------------------------------

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 属性名 |
| `value` | `&nbsp;` |  |

**说明**

属性的设置

---

### get

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 属性名 |

**返回值**

设定值

**说明**

属性的获取

---

### missing

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `...` | `&nbsp;` |  |

**说明**

TJS missing 处理。未注册的名称会按原样尝试 set/get/invoke 处理

---
