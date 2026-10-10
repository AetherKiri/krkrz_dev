# Threepp.Shape

Shape（带孔 2D 形状）

继承 Path，可以添加孔的 2D 形状类
供 ExtrudeGeometry 和 ShapeGeometry 使用

## 成员列表

### 构造函数

- [Shape](#shape)

### 属性

- [autoClose](#autoclose)
- [currentPoint](#currentpoint)

### 方法

- [getLength](#getlength)
- [getPoint](#getpoint)
- [getPointAt](#getpointat)
- [moveTo](#moveto)
- [lineTo](#lineto)
- [quadraticCurveTo](#quadraticcurveto)
- [bezierCurveTo](#beziercurveto)
- [arc](#arc)
- [absarc](#absarc)
- [absellipse](#absellipse)
- [splineThru](#splinethru)
- [closePath](#closepath)
- [addHole](#addhole)
- [getHole](#gethole)
- [getHoleCount](#getholecount)
- [uuid](#uuid)

---

### Shape

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 初始点数组（可省略） |

**说明**

构造函数

---

### autoClose

属性 \ 访问: `r/w`

**说明**

是否自动闭合路径

---

### currentPoint

属性 \ 访问: `r/w`

**说明**

当前笔位置（只读）

---

### getLength

方法

**说明**

获取路径的全长

---

### getPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

获取参数 t (0-1) 处的点

---

### getPointAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `u` | `&nbsp;` |  |

**说明**

获取等间距参数 u 处的点

---

### moveTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

与 Path 相同的绘制方法

---

### lineTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

绘制直线

---

### quadraticCurveTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `cpX` | `&nbsp;` |  |
| `cpY` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

绘制二次贝塞尔曲线

---

### bezierCurveTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `cp1x` | `&nbsp;` |  |
| `cp1y` | `&nbsp;` |  |
| `cp2x` | `&nbsp;` |  |
| `cp2y` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

绘制三次贝塞尔曲线

---

### arc

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `radius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |

**说明**

从相对位置绘制圆弧

---

### absarc

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `radius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |

**说明**

按绝对位置绘制圆弧

---

### absellipse

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `xRadius` | `&nbsp;` |  |
| `yRadius` | `&nbsp;` |  |
| `startAngle` | `&nbsp;` |  |
| `endAngle` | `&nbsp;` |  |
| `clockwise` | `&nbsp;` |  |
| `rotation` | `&nbsp;` |  |

**说明**

绘制椭圆

---

### splineThru

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` |  |

**说明**

通过点数组的样条

---

### closePath

方法

**说明**

闭合路径

---

### addHole

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hole` | `&nbsp;` |  |

**说明**

孔的管理

---

### getHole

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**说明**

获取孔

---

### getHoleCount

方法

**说明**

获取孔的数量

---

### uuid

方法

**说明**

获取形状的 UUID

---
