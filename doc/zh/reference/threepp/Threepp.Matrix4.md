# Threepp.Matrix4

4x4 矩阵类

表示变换矩阵。

## 成员列表

### 构造函数

- [Matrix4](#matrix4)

### 方法

- [set](#set)
- [identity](#identity)
- [copy](#copy)
- [copyPosition](#copyposition)
- [extractBasis](#extractbasis)
- [makeBasis](#makebasis)
- [extractRotation](#extractrotation)
- [makeRotationFromEuler](#makerotationfromeuler)
- [makeRotationFromQuaternion](#makerotationfromquaternion)
- [lookAt](#lookat)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyMatrices](#multiplymatrices)
- [multiplyScalar](#multiplyscalar)
- [determinant](#determinant)
- [transpose](#transpose)
- [setPosition](#setposition)
- [invert](#invert)
- [scale](#scale)
- [getMaxScaleOnAxis](#getmaxscaleonaxis)
- [makeTranslation](#maketranslation)
- [makeRotationX](#makerotationx)
- [makeRotationY](#makerotationy)
- [makeRotationZ](#makerotationz)
- [makeRotationAxis](#makerotationaxis)
- [makeScale](#makescale)
- [makeShear](#makeshear)
- [compose](#compose)
- [decompose](#decompose)
- [makePerspective](#makeperspective)
- [makeOrthographic](#makeorthographic)
- [equals](#equals)

---

### Matrix4

构造函数

**说明**

构造函数

生成单位矩阵

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `n11` | `&nbsp;` |  |
| `n12` | `&nbsp;` |  |
| `n13` | `&nbsp;` |  |
| `n14` | `&nbsp;` |  |
| `n21` | `&nbsp;` |  |
| `n22` | `&nbsp;` |  |
| `n23` | `&nbsp;` |  |
| `n24` | `&nbsp;` |  |
| `n31` | `&nbsp;` |  |
| `n32` | `&nbsp;` |  |
| `n33` | `&nbsp;` |  |
| `n34` | `&nbsp;` |  |
| `n41` | `&nbsp;` |  |
| `n42` | `&nbsp;` |  |
| `n43` | `&nbsp;` |  |
| `n44` | `&nbsp;` |  |

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

### copyPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

仅复制位置分量

---

### extractBasis

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `xAxis` | `&nbsp;` |  |
| `yAxis` | `&nbsp;` |  |
| `zAxis` | `&nbsp;` |  |

**说明**

提取基向量

---

### makeBasis

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `xAxis` | `&nbsp;` |  |
| `yAxis` | `&nbsp;` |  |
| `zAxis` | `&nbsp;` |  |

**说明**

从基向量生成矩阵

---

### extractRotation

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

提取旋转分量

---

### makeRotationFromEuler

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**说明**

从欧拉角生成旋转矩阵

---

### makeRotationFromQuaternion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

从四元数生成旋转矩阵

---

### lookAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `eye` | `&nbsp;` |  |
| `target` | `&nbsp;` |  |
| `up` | `&nbsp;` |  |

**说明**

生成视线矩阵

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

### transpose

方法

**说明**

转置

---

### setPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

设置位置

---

### invert

方法

**说明**

逆矩阵

---

### scale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

缩放

---

### getMaxScaleOnAxis

方法

**说明**

各轴的最大缩放值

---

### makeTranslation

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

生成平移矩阵

---

### makeRotationX

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**说明**

生成 X 轴旋转矩阵

---

### makeRotationY

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**说明**

生成 Y 轴旋转矩阵

---

### makeRotationZ

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `theta` | `&nbsp;` |  |

**说明**

生成 Z 轴旋转矩阵

---

### makeRotationAxis

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**说明**

生成任意轴旋转矩阵

---

### makeScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

生成缩放矩阵

---

### makeShear

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `xy` | `&nbsp;` |  |
| `xz` | `&nbsp;` |  |
| `yx` | `&nbsp;` |  |
| `yz` | `&nbsp;` |  |
| `zx` | `&nbsp;` |  |
| `zy` | `&nbsp;` |  |

**说明**

生成剪切矩阵

---

### compose

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `position` | `&nbsp;` |  |
| `quaternion` | `&nbsp;` |  |
| `scale` | `&nbsp;` |  |

**说明**

由位置、旋转、缩放合成

---

### decompose

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `position` | `&nbsp;` |  |
| `quaternion` | `&nbsp;` |  |
| `scale` | `&nbsp;` |  |

**说明**

分解为位置、旋转、缩放

---

### makePerspective

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**说明**

生成透视投影矩阵

---

### makeOrthographic

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**说明**

生成正交投影矩阵

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
