# Threepp.Spherical

球面坐标类

## 成员列表

### 构造函数

- [Spherical](#spherical)

### 属性

- [radius](#radius)
- [phi](#phi)
- [theta](#theta)

### 方法

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeSafe](#makesafe)
- [setFromVector3](#setfromvector3)
- [setFromCartesianCoords](#setfromcartesiancoords)

---

### Spherical

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `radius` | `1` | 半径 |
| `phi` | `0` | 极角 (弧度) |
| `theta` | `0` | 方位角 (弧度) |

**说明**

构造函数

---

### radius

属性 \ 访问: `r/w`

**说明**

半径

---

### phi

属性 \ 访问: `r/w`

**说明**

极角

---

### theta

属性 \ 访问: `r/w`

**说明**

方位角

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |
| `phi` | `&nbsp;` |  |
| `theta` | `&nbsp;` |  |

**说明**

设置值

---

### clone

方法

**说明**

克隆

---

### copy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

复制

---

### makeSafe

方法

**说明**

校正为安全值

---

### setFromVector3

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

从 Vector3 设置

---

### setFromCartesianCoords

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

从笛卡尔坐标设置

---
