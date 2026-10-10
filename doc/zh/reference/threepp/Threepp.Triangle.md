# Threepp.Triangle

三角形类

## 成员列表

### 构造函数

- [Triangle](#triangle)

### 属性

- [a](#a)
- [b](#b)
- [c](#c)

### 方法

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [getArea](#getarea)
- [getMidpoint](#getmidpoint)
- [getNormal](#getnormal)
- [getPlane](#getplane)
- [getBarycoord](#getbarycoord)
- [containsPoint](#containspoint)
- [isFrontFacing](#isfrontfacing)
- [closestPointToPoint](#closestpointtopoint)
- [equals](#equals)

---

### Triangle

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` | 顶点 A (Vector3) |
| `b` | `&nbsp;` | 顶点 B (Vector3) |
| `c` | `&nbsp;` | 顶点 C (Vector3) |

**说明**

构造函数

---

### a

属性 \ 访问: `r/w`

**说明**

顶点 A（只读）

---

### b

属性 \ 访问: `r/w`

**说明**

顶点 B（只读）

---

### c

属性 \ 访问: `r/w`

**说明**

顶点 C（只读）

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `c` | `&nbsp;` |  |

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
| `triangle` | `&nbsp;` |  |

**说明**

复制

---

### getArea

方法

**说明**

面积

---

### getMidpoint

方法

**说明**

重心

---

### getNormal

方法

**说明**

法线

---

### getPlane

方法

**说明**

包含三角形的平面

---

### getBarycoord

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

获取重心坐标

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

### isFrontFacing

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `direction` | `&nbsp;` |  |

**说明**

是否朝向正面

---

### closestPointToPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |

**说明**

最近点

---

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `triangle` | `&nbsp;` |  |

**说明**

相等判定

---
