# Threepp.Path

2D 路径

创建由多条曲线组合而成的 2D 路径。
可以使用与 Canvas API 相同的方法进行绘制。

## 成员列表

### 构造函数

- [Path](#path)

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

---

### Path

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 初始点的数组（可省略） |

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

当前的笔位置（只读）

---

### getLength

方法

**说明**

获取路径的总长度

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

移动笔

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

从绝对位置绘制圆弧

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

通过点数组的样条曲线

---

### closePath

方法

**说明**

闭合路径

---
