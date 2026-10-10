# AsyncTrigger

AsyncTrigger 类是用于在控制权一旦返回吉里吉里引擎本体之后、紧接着的事件分发时机引发事件的类。此功能称为**异步触发器** ( asynchronous trigger )。

在像吉里吉里这样采用事件驱动型编程模型的脚本中，当希望在事件处理器之外执行在事件处理器内无法执行的处理 (例如试图在事件处理器内使事件的产生源对象失效等) 时，这个类会很有用。

## 成员列表

### 构造函数

- [AsyncTrigger](#asynctrigger)

### 属性

- [cached](#cached)
- [mode](#mode)

### 方法

- [trigger](#trigger)
- [cancel](#cancel)

### 事件

- [onFire](#onfire)

---

### AsyncTrigger

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `owner` | `&nbsp;` | 指定事件的产生目标。 |
| `actionname` | `"action"` | 在由 owner 指定的事件产生目标对象中，指定接收事件的<br>方法名。指定空字符串时，owner 会被视为方法，每次引发事件<br>都会直接调用 owner。 |

**说明**

构建 AsyncTriger 对象

构建 AsyncTrigger 类的对象。

---

### cached

属性 \ 访问: `r/w`

**说明**

是否缓存事件

表示是否缓存事件。也可以设置值。

指定为真时，在触发之前无论调用多少次 [AsyncTrigger.trigger](AsyncTrigger.md#trigger) 方法，
也都只会触发一次。

指定为假时，在触发之前调用了几次就会触发几次。

---

### mode

属性 \ 访问: `r/w`

**说明**

模式

表示运行的模式。也可以设置值。

请指定以下值之一。

`**atmNormal**    : ` 在通常的事件分发阶段触发。

`**atmExclusive** : ` 优先于其他异步事件触发

`**atmAtIdle**    : ` 在空闲状态 (没有其他要分发的事件时) 触发。

同时扣动触发器时，触发的顺序为 atmExclusive、atmNormal、atmIdle。

同一模式的触发器被扣动了多个时，按扣动触发器的顺序触发。

**相关:** [Timer.mode](Timer.md#mode)

---

### trigger

方法

**说明**

扣动触发器

引发事件。

调用此方法后，控制权返回吉里吉里引擎本体，当吉里吉里引擎本体进入分发积压的
异步事件的阶段时，会引发 [AsyncTrigger.onFire](AsyncTrigger.md#onfire) 事件。

---

### cancel

方法

**说明**

取消触发器

取消用 [AsyncTrigger.trigger](AsyncTrigger.md#trigger) 方法扣动的触发器。

只要尚未触发，随时都可以取消。

---

### onFire

事件

**说明**

触发时

在用 [AsyncTrigger.trigger](AsyncTrigger.md#trigger) 方法扣动触发器之后发生。

---
