# Threepp.Line3

3D 线段类

## 成员列表

### 构造函数

- [Line3](#line3)

### 属性

- [start](#start)
- [end](#end)

### 方法

- [set](#set)
- [clone](#clone)
- [copy](#copy)
- [getCenter](#getcenter)
- [delta](#delta)
- [distanceSq](#distancesq)
- [distance](#distance)
- [at](#at)
- [closestPointToPoint](#closestpointtopoint)
- [closestPointToPointParameter](#closestpointtopointparameter)
- [applyMatrix4](#applymatrix4)
- [equals](#equals)

---

### Line3

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `start` | `&nbsp;` | 起点 (Vector3) |
| `end` | `&nbsp;` | 终点 (Vector3) |

**说明**

构造函数

---

### start

属性 \ 访问: `r/w`

**说明**

起点（只读）

---

### end

属性 \ 访问: `r/w`

**说明**

终点（只读）

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `start` | `&nbsp;` |  |
| `end` | `&nbsp;` |  |

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
| `line` | `&nbsp;` |  |

**说明**

复制

---

### getCenter

方法

**说明**

获取中心

---

### delta

方法

**说明**

获取方向向量

---

### distanceSq

方法

**说明**

长度的平方

---

### distance

方法

**说明**

长度

---

### at

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

获取参数位置处的点

---

### closestPointToPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |
| `clamp` | `&nbsp;` |  |

**说明**

获取最近点

---

### closestPointToPointParameter

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `point` | `&nbsp;` |  |
| `clamp` | `&nbsp;` |  |

**说明**

最近点的参数

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
| `line` | `&nbsp;` |  |

**说明**

等价判定

---
