# NullDrawDevice

NullDrawDevice 类是用于将该实例注册到 [Window.drawDevice](Window.md#drawdevice) 后使用的 DrawDevice，提供什么都不绘制的空实现。

在无头执行，或想在外部完全控制自行准备的绘制路径时使用。

## 成员列表

### 构造函数

- [NullDrawDevice](#nulldrawdevice)

### 属性

- [interface](#interface)

### 方法

- [recreate](#recreate)

---

### NullDrawDevice

构造函数

**说明**

NullDrawDevice 对象的构建

构建 NullDrawDevice 类的对象。

---

### interface

属性 \ 访问: `r`

**说明**

获取接口对象

用于插件等利用 DrawDevice 对象。

---

### recreate

方法

**说明**

内部设备重新生成

进行内部设备的重新生成。

通常不会使用。

---
