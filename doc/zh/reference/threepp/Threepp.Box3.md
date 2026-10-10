# Threepp.Box3

轴对齐包围盒 (AABB) 类

## 成员列表

### 构造函数

- [Box3](#box3)

### 属性

- [min](#min)
- [max](#max)

### 方法

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [makeEmpty](#makeempty)
- [isEmpty](#isempty)
- [getCenter](#getcenter)
- [getSize](#getsize)
- [expandByPoint](#expandbypoint)
- [expandByVector](#expandbyvector)
- [expandByScalar](#expandbyscalar)
- [containsPoint](#containspoint)
- [containsBox](#containsbox)
- [intersectsBox](#intersectsbox)
- [intersectsSphere](#intersectssphere)
- [intersectsPlane](#intersectsplane)
- [distanceToPoint](#distancetopoint)
- [intersect](#intersect)
- [union_](#union_)
- [applyMatrix4](#applymatrix4)
- [translate](#translate)
- [equals](#equals)

---

### Box3

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `min` | `&nbsp;` | 最小坐标 (Vector3) |
| `max` | `&nbsp;` | 最大坐标 (Vector3) |

**说明**

构造函数

---

### min

属性 \ 访问: `r/w`

**说明**

最小坐标（只读）

---

### max

属性 \ 访问: `r/w`

**说明**

最大坐标（只读）

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |

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
| `box` | `&nbsp;` |  |

**说明**

复制

---

### makeEmpty

方法

**说明**

置为空

---

### isEmpty

方法

**说明**

是否为空

---

### getCenter

方法

**说明**

获取中心

---

### getSize

方法

**说明**

获取尺寸

---

### expandByPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

用点扩展

---

### expandByVector

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vector` | `&nbsp;` |  |

**说明**

用向量扩展

---

### expandByScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `scalar` | `&nbsp;` |  |

**说明**

用标量扩展

---

### containsPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

是否包含点

---

### containsBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**说明**

是否包含盒

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

### intersectsSphere

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sphere` | `&nbsp;` |  |

**说明**

是否与球相交

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

### distanceToPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

到点的距离

---

### intersect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**说明**

获取相交部分

---

### union_

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `box` | `&nbsp;` |  |

**说明**

获取并集

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
| `box` | `&nbsp;` |  |

**说明**

相等判定

---
