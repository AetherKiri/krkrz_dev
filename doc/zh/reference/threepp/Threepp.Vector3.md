# Threepp.Vector3

3D 向量类

表示三维向量。也可以从数组 [x, y, z] 或字典 %[x:, y:, z:] 转换。

## 成员列表

### 构造函数

- [Vector3](#vector3)

### 属性

- [x](#x)
- [y](#y)
- [z](#z)

### 方法

- [set](#set)
- [setScalar](#setscalar)
- [setX](#setx)
- [setY](#sety)
- [setZ](#setz)
- [copy](#copy)
- [add](#add)
- [addScalar](#addscalar)
- [addVectors](#addvectors)
- [addScaledVector](#addscaledvector)
- [sub](#sub)
- [subScalar](#subscalar)
- [subVectors](#subvectors)
- [multiply](#multiply)
- [multiplyScalar](#multiplyscalar)
- [multiplyVectors](#multiplyvectors)
- [applyAxisAngle](#applyaxisangle)
- [applyEuler](#applyeuler)
- [applyMatrix3](#applymatrix3)
- [applyMatrix4](#applymatrix4)
- [applyQuaternion](#applyquaternion)
- [project](#project)
- [unproject](#unproject)
- [transformDirection](#transformdirection)
- [divide](#divide)
- [divideScalar](#dividescalar)
- [min](#min)
- [max](#max)
- [clamp](#clamp)
- [clampScalar](#clampscalar)
- [clampLength](#clamplength)
- [floor](#floor)
- [ceil](#ceil)
- [round](#round)
- [negate](#negate)
- [dot](#dot)
- [lengthSq](#lengthsq)
- [length](#length)
- [manhattanLength](#manhattanlength)
- [normalize](#normalize)
- [setLength](#setlength)
- [lerp](#lerp)
- [lerpVectors](#lerpvectors)
- [cross](#cross)
- [crossVectors](#crossvectors)
- [reflect](#reflect)
- [angleTo](#angleto)
- [distanceTo](#distanceto)
- [distanceToSquared](#distancetosquared)
- [manhattanDistanceTo](#manhattandistanceto)
- [setFromMatrixPosition](#setfrommatrixposition)
- [setFromMatrixScale](#setfrommatrixscale)
- [equals](#equals)

---

### Vector3

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `0` | X 分量 |
| `y` | `0` | Y 分量 |
| `z` | `0` | Z 分量 |

**说明**

构造函数

---

### x

属性 \ 访问: `r/w`

**说明**

X 分量

---

### y

属性 \ 访问: `r/w`

**说明**

Y 分量

---

### z

属性 \ 访问: `r/w`

**说明**

Z 分量

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

设置值

---

### setScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**说明**

将所有分量设置为同一个值

---

### setX

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**说明**

设置 X 分量

---

### setY

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**说明**

设置 Y 分量

---

### setZ

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**说明**

设置 Z 分量

---

### copy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

从另一个向量复制

---

### add

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

加上向量

---

### addScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

加上标量

---

### addVectors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**说明**

设置两个向量之和

---

### addScaledVector

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |
| `s` | `&nbsp;` |  |

**说明**

缩放后加上

---

### sub

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

减去向量

---

### subScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

减去标量

---

### subVectors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**说明**

设置两个向量之差

---

### multiply

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

向量之间逐分量相乘

---

### multiplyScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

乘以标量

---

### multiplyVectors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**说明**

设置两个向量的逐分量乘积

---

### applyAxisAngle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**说明**

按轴和角度旋转

---

### applyEuler

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**说明**

按欧拉角旋转

---

### applyMatrix3

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

应用 3x3 矩阵

---

### applyMatrix4

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

应用 4x4 矩阵

---

### applyQuaternion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

用四元数旋转

---

### project

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `camera` | `&nbsp;` |  |

**说明**

投影到相机

---

### unproject

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `camera` | `&nbsp;` |  |

**说明**

取消投影

---

### transformDirection

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

变换方向向量

---

### divide

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

向量之间逐分量相除

---

### divideScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

除以标量

---

### min

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

各分量的最小值

---

### max

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

各分量的最大值

---

### clamp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**说明**

对每个分量进行钳制

---

### clampScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**说明**

按标量范围钳制

---

### clampLength

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

**说明**

钳制长度

---

### floor

方法

**说明**

对每个分量向下取整

---

### ceil

方法

**说明**

对每个分量向上取整

---

### round

方法

**说明**

对每个分量四舍五入

---

### negate

方法

**说明**

符号取反

---

### dot

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

内积

---

### lengthSq

方法

**说明**

长度的平方

---

### length

方法

**说明**

长度

---

### manhattanLength

方法

**说明**

曼哈顿距离

---

### normalize

方法

**说明**

归一化

---

### setLength

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `length` | `&nbsp;` |  |

**说明**

设置长度

---

### lerp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**说明**

线性插值

---

### lerpVectors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**说明**

两个向量之间的线性插值

---

### cross

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

外积

---

### crossVectors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**说明**

两个向量的外积

---

### reflect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |

**说明**

反射

---

### angleTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

与另一个向量的夹角

---

### distanceTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

与另一个向量的距离

---

### distanceToSquared

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

距离的平方

---

### manhattanDistanceTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

曼哈顿距离

---

### setFromMatrixPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

获取矩阵的位置分量

---

### setFromMatrixScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

获取矩阵的缩放分量

---

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

相等判定

---
