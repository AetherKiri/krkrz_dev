# GdiPlus.Matrix

该类由多个插件扩展。

## 插件扩展: layerExDraw

处理矩阵信息的类

### 成员列表

#### 构造函数

- [Matrix](#matrix)
- [Matrix](#matrix)
- [Matrix](#matrix)

#### 方法

- [OffsetX](#offsetx)
- [OffsetY](#offsety)
- [Equals](#equals)
- [SetElemetns](#setelemetns)
- [GetLastStatus](#getlaststatus)
- [Invert](#invert)
- [IsIdentity](#isidentity)
- [IsInvertible](#isinvertible)
- [Multiply](#multiply)
- [Reset](#reset)
- [Rotate](#rotate)
- [RotateAt](#rotateat)
- [Scale](#scale)
- [Share](#share)
- [Translate](#translate)

---

### Matrix

构造函数

**说明**

构造函数

生成正规矩阵

---

### Matrix

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rectF` | `&nbsp;` | 矩形 (RectF 类) 矩阵的旋转部分 |
| `pointF` | `&nbsp;` | 点 (PointF 类) 矩阵的平移部分 |

**说明**

构造函数

---

### Matrix

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m11` | `&nbsp;` | 第 1 行第 1 列 |
| `m12` | `&nbsp;` | 第 1 行第 2 列 |
| `m21` | `&nbsp;` | 第 2 行第 1 列 |
| `m22` | `&nbsp;` | 第 2 行第 2 列 |
| `dx` | `&nbsp;` | 第 3 行第 1 列 |
| `dy` | `&nbsp;` | 第 3 行第 2 列 |

**说明**

构造函数

---

### OffsetX

方法

---

### OffsetY

方法

---

### Equals

方法

---

### SetElemetns

方法

---

### GetLastStatus

方法

---

### Invert

方法

---

### IsIdentity

方法

---

### IsInvertible

方法

---

### Multiply

方法

---

### Reset

方法

---

### Rotate

方法

---

### RotateAt

方法

---

### Scale

方法

---

### Share

方法

---

### Translate

方法

---

## 插件扩展: layerExVector

处理矩阵信息的类

### 成员列表

#### 构造函数

- [Matrix](#matrix)
- [Matrix](#matrix)

#### 方法

- [OffsetX](#offsetx)
- [OffsetY](#offsety)
- [Equals](#equals)
- [SetElements](#setelements)
- [Invert](#invert)
- [IsIdentity](#isidentity)
- [IsInvertible](#isinvertible)
- [Multiply](#multiply)
- [Reset](#reset)
- [Rotate](#rotate)
- [Scale](#scale)
- [Translate](#translate)

---

### Matrix

构造函数

**说明**

构造函数

生成正规矩阵

---

### Matrix

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m11` | `&nbsp;` | 第 1 行第 1 列 |
| `m12` | `&nbsp;` | 第 1 行第 2 列 |
| `m21` | `&nbsp;` | 第 2 行第 1 列 |
| `m22` | `&nbsp;` | 第 2 行第 2 列 |
| `dx` | `&nbsp;` | 第 3 行第 1 列 |
| `dy` | `&nbsp;` | 第 3 行第 2 列 |

**说明**

构造函数

---

### OffsetX

方法

---

### OffsetY

方法

---

### Equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |

---

### SetElements

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### Invert

方法

---

### IsIdentity

方法

---

### IsInvertible

方法

---

### Multiply

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Reset

方法

---

### Rotate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Scale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---

### Translate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |
| `order` | `MatrixOrderPrepend` |  |

---
