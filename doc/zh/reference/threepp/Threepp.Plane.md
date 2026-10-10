# Threepp.Plane

平面类

## 成员列表

### 构造函数

- [Plane](#plane)

### 方法

- [set](#set)
- [setComponents](#setcomponents)
- [setFromNormalAndCoplanarPoint](#setfromnormalandcoplanarpoint)
- [clone](#clone)
- [copy](#copy)
- [normalize](#normalize)
- [negate](#negate)
- [distanceToPoint](#distancetopoint)
- [distanceToSphere](#distancetosphere)
- [coplanarPoint](#coplanarpoint)
- [applyMatrix4](#applymatrix4)
- [translate](#translate)
- [equals](#equals)

---

### Plane

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `normal` | `&nbsp;` | 法线 (Vector3) |
| `constant` | `&nbsp;` | 常量 |

**说明**

构造函数

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |
| `constant` | `&nbsp;` |  |

**说明**

设置值

---

### setComponents

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |

**说明**

通过分量设置

---

### setFromNormalAndCoplanarPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `normal` | `&nbsp;` |  |
| `point` | `&nbsp;` |  |

**说明**

根据法线和点设置

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
| `plane` | `&nbsp;` |  |

**说明**

复制

---

### normalize

方法

**说明**

归一化

---

### negate

方法

**说明**

取反

---

### distanceToPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

到点的距离

---

### distanceToSphere

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**说明**

到球体的距离

---

### coplanarPoint

方法

**说明**

获取平面上的点

---

### applyMatrix4

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

应用矩阵

---

### translate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `offset` | `&nbsp;` |  |

**说明**

平移

---

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**说明**

等价判定

---
