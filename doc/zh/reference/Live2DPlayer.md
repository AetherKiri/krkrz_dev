# Live2DPlayer

绘制用播放器

除与 Live2DModel 相同的接口外，还拥有绘制用的方法
生成需要 Live2DDevice

## 成员列表

### 构造函数

- [Live2DPlayer](#live2dplayer)

### 方法

- [clear](#clear)
- [load](#load)
- [loadModel](#loadmodel)
- [clone](#clone)
- [setScale](#setscale)
- [getScale](#getscale)
- [setMatrix](#setmatrix)
- [render](#render)
- [setVoiceValue](#setvoicevalue)
- [setVoiceWeight](#setvoiceweight)
- [setVoiceMode](#setvoicemode)
- [setBlinkingInterval](#setblinkinginterval)
- [setBlinkingSettings](#setblinkingsettings)
- [setBlinkingMode](#setblinkingmode)
- [setMosaicParam](#setmosaicparam)

---

### Live2DPlayer

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `device` | `&nbsp;` | Live2DDevice 实例 |

**说明**

构造函数

---

### clear

方法

**说明**

清空内容

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

---

### loadModel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `model` | `&nbsp;` | Live2DModel 实例 |

**说明**

从 Live2DModel 实例生成播放器

继承已加载模型的状态

---

### clone

方法

**说明**

复制

---

### setScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**说明**

设置显示缩放

---

### getScale

方法

---

### setMatrix

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m13` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `m23` | `&nbsp;` |  |

**说明**

指定显示矩阵

---

### render

方法

**说明**

显示处理。在 OpenGL 上下文中执行时会进行绘制

---

### setVoiceValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `voice` | `&nbsp;` |  |

---

### setVoiceWeight

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `weight` | `&nbsp;` |  |

---

### setVoiceMode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### setBlinkingInterval

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `interal` | `&nbsp;` |  |

---

### setBlinkingSettings

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `closing` | `&nbsp;` |  |
| `closed` | `&nbsp;` |  |
| `opening` | `&nbsp;` |  |

---

### setBlinkingMode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |

---

### setMosaicParam

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

---
