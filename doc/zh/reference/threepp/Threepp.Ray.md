# Threepp.Ray

射线类

## 成员列表

### 构造函数

- [Ray](#ray)

### 方法

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [at](#at)
- [lookAt](#lookat)
- [recast](#recast)
- [closestPointToPoint](#closestpointtopoint)
- [distanceToPoint](#distancetopoint)
- [distanceSqToPoint](#distancesqtopoint)
- [distanceSqToSegment](#distancesqtosegment)
- [intersectSphere](#intersectsphere)
- [intersectsSphere](#intersectssphere)
- [intersectBox](#intersectbox)
- [intersectsBox](#intersectsbox)
- [intersectPlane](#intersectplane)
- [intersectsPlane](#intersectsplane)
- [applyMatrix4](#applymatrix4)
- [equals](#equals)

---

### Ray

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `origin` | `&nbsp;` | 原点 (Vector3) |
| `direction` | `&nbsp;` | 方向 (Vector3) |

**说明**

构造函数

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `origin` | `&nbsp;` |  |
| `direction` | `&nbsp;` |  |

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
| `ray` | `&nbsp;` |  |

**说明**

复制

---

### at

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

获取射线上的点

---

### lookAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

设置方向

---

### recast

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

移动原点

---

### closestPointToPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

获取最近点

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

### distanceSqToPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

距离的平方

---

### distanceSqToSegment

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v0` | `&nbsp;` |  |
| `v1` | `&nbsp;` |  |

**说明**

与线段的距离的平方

---

### intersectSphere

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**说明**

与球的交点

---

### intersectsSphere

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**说明**

是否与球相交

---

### intersectBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**说明**

与盒的交点

---

### intersectsBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**说明**

是否与盒相交

---

### intersectPlane

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**说明**

与平面的交点

---

### intersectsPlane

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `plane` | `&nbsp;` |  |

**说明**

是否与平面相交

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

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ray` | `&nbsp;` |  |

**说明**

相等判定

---
