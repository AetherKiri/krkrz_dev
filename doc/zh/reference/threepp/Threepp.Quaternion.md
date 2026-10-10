# Threepp.Quaternion

四元数（Quaternion）类

表示旋转的四元数。不会发生万向节锁。

## 成员列表

### 构造函数

- [Quaternion](#quaternion)

### 属性

- [x](#x)
- [y](#y)
- [z](#z)
- [w](#w)

### 方法

- [set](#set)
- [copy](#copy)
- [setFromEuler](#setfromeuler)
- [setFromAxisAngle](#setfromaxisangle)
- [setFromRotationMatrix](#setfromrotationmatrix)
- [setFromUnitVectors](#setfromunitvectors)
- [angleTo](#angleto)
- [rotateTowards](#rotatetowards)
- [identity](#identity)
- [invert](#invert)
- [conjugate](#conjugate)
- [dot](#dot)
- [lengthSq](#lengthsq)
- [length](#length)
- [normalize](#normalize)
- [multiply](#multiply)
- [premultiply](#premultiply)
- [multiplyQuaternions](#multiplyquaternions)
- [slerp](#slerp)
- [slerpQuaternions](#slerpquaternions)
- [equals](#equals)

---

### Quaternion

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `0` | X 分量 |
| `y` | `0` | Y 分量 |
| `z` | `0` | Z 分量 |
| `w` | `1` | W 分量 |

**说明**

构造函数

---

### x

属性 \ 访问: `r/w`

**说明**

X 分量（只读）

---

### y

属性 \ 访问: `r/w`

**说明**

Y 分量（只读）

---

### z

属性 \ 访问: `r/w`

**说明**

Z 分量（只读）

---

### w

属性 \ 访问: `r/w`

**说明**

W 分量（只读）

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |

**说明**

设置值

---

### copy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

复制

---

### setFromEuler

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**说明**

从欧拉角设置

---

### setFromAxisAngle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**说明**

从轴与角度设置

---

### setFromRotationMatrix

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

从旋转矩阵设置

---

### setFromUnitVectors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vFrom` | `&nbsp;` |  |
| `vTo` | `&nbsp;` |  |

**说明**

从两个单位向量设置

---

### angleTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

与另一个四元数的角度

---

### rotateTowards

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |
| `step` | `&nbsp;` |  |

**说明**

向另一个四元数旋转

---

### identity

方法

**说明**

设置为单位四元数

---

### invert

方法

**说明**

逆四元数

---

### conjugate

方法

**说明**

共轭

---

### dot

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

点积

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

### normalize

方法

**说明**

归一化

---

### multiply

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

相乘

---

### premultiply

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

左乘

---

### multiplyQuaternions

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**说明**

两个四元数的乘积

---

### slerp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |
| `t` | `&nbsp;` |  |

**说明**

球面线性插值

---

### slerpQuaternions

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `qa` | `&nbsp;` |  |
| `qb` | `&nbsp;` |  |
| `t` | `&nbsp;` |  |

**说明**

两个四元数之间的球面线性插值

---

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

相等判定

---
