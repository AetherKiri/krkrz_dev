# Threepp.Matrix3

3x3 矩阵类

## 成员列表

### 构造函数

- [Matrix3](#matrix3)

### 方法

- [set](#set)
- [identity](#identity)
- [copy](#copy)
- [setFromMatrix4](#setfrommatrix4)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyMatrices](#multiplymatrices)
- [multiplyScalar](#multiplyscalar)
- [determinant](#determinant)
- [invert](#invert)
- [transpose](#transpose)
- [getNormalMatrix](#getnormalmatrix)
- [scale](#scale)
- [rotate](#rotate)
- [translate](#translate)
- [equals](#equals)

---

### Matrix3

构造函数

**说明**

构造函数

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `n11` | `&nbsp;` |  |
| `n12` | `&nbsp;` |  |
| `n13` | `&nbsp;` |  |
| `n21` | `&nbsp;` |  |
| `n22` | `&nbsp;` |  |
| `n23` | `&nbsp;` |  |
| `n31` | `&nbsp;` |  |
| `n32` | `&nbsp;` |  |
| `n33` | `&nbsp;` |  |

**说明**

设置元素

---

### identity

方法

**说明**

设置为单位矩阵

---

### copy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

复制

---

### setFromMatrix4

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

从 Matrix4 设置

---

### multiply

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

相乘

---

### premultiply

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

左乘

---

### multiplyMatrices

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**说明**

两个矩阵的乘积

---

### multiplyScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

标量相乘

---

### determinant

方法

**说明**

行列式

---

### invert

方法

**说明**

逆矩阵

---

### transpose

方法

**说明**

转置

---

### getNormalMatrix

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

获取法线矩阵

---

### scale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |

**说明**

缩放

---

### rotate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**说明**

旋转

---

### translate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |

**说明**

平移

---

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

等价判定

---
