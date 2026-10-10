# GdiPlus.Path

该类由多个插件扩展。

## 插件扩展: layerExDraw

### 成员列表

#### 构造函数

- [Path](#path)

#### 方法

- [startFigure](#startfigure)
- [closeFigure](#closefigure)
- [drawArc](#drawarc)
- [drawPie](#drawpie)
- [drawBezier](#drawbezier)
- [drawBeziers](#drawbeziers)
- [drawClosedCurve](#drawclosedcurve)
- [drawClosedCurve2](#drawclosedcurve2)
- [drawCurve](#drawcurve)
- [drawCurve2](#drawcurve2)
- [drawCurve3](#drawcurve3)
- [drawEllipse](#drawellipse)
- [drawLine](#drawline)
- [drawLines](#drawlines)
- [drawPolygon](#drawpolygon)
- [drawRectangle](#drawrectangle)
- [drawRectangles](#drawrectangles)

---

### Path

构造函数

**说明**

路径信息类

---

### startFigure

方法

**说明**

不关闭当前图形，开始下一个图形

---

### closeFigure

方法

**说明**

关闭当前图形

---

### drawArc

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**说明**

圆弧的绘制

---

### drawPie

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**说明**

扇形的绘制

---

### drawBezier

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**说明**

贝塞尔曲线的绘制

---

### drawBeziers

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

连续贝塞尔曲线的绘制

---

### drawClosedCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

封闭基数样条的绘制

---

### drawClosedCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**说明**

封闭基数样条的绘制

---

### drawCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

基数样条的绘制

---

### drawCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**说明**

基数样条的绘制

---

### drawCurve3

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | 张力 |

**说明**

基数样条的绘制

---

### drawEllipse

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

椭圆的绘制

---

### drawLine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x1` | `&nbsp;` | 起点 X 坐标 |
| `y1` | `&nbsp;` | 起点 Y 坐标 |
| `x2` | `&nbsp;` | 终点 X 坐标 |
| `y2` | `&nbsp;` | 终点 Y 坐标 |

**说明**

线段的绘制

---

### drawLines

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

连续线段的绘制

---

### drawPolygon

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

多边形的绘制

---

### drawRectangle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

矩形的绘制

---

### drawRectangles

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rects` | `&nbsp;` | 矩形的数组 [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**说明**

多个矩形的绘制

---

## 插件扩展: layerExVector

### 成员列表

#### 构造函数

- [Path](#path)

#### 方法

- [startFigure](#startfigure)
- [closeFigure](#closefigure)
- [drawArc](#drawarc)
- [drawPie](#drawpie)
- [drawBezier](#drawbezier)
- [drawBeziers](#drawbeziers)
- [drawClosedCurve](#drawclosedcurve)
- [drawClosedCurve2](#drawclosedcurve2)
- [drawCurve](#drawcurve)
- [drawCurve2](#drawcurve2)
- [drawCurve3](#drawcurve3)
- [drawEllipse](#drawellipse)
- [drawLine](#drawline)
- [drawLines](#drawlines)
- [drawPolygon](#drawpolygon)
- [drawRectangle](#drawrectangle)
- [drawRectangles](#drawrectangles)

---

### Path

构造函数

**说明**

路径信息类

---

### startFigure

方法

**说明**

不关闭当前图形，开始下一个图形

---

### closeFigure

方法

**说明**

关闭当前图形

---

### drawArc

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**说明**

圆弧的绘制

---

### drawPie

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**说明**

扇形的绘制

---

### drawBezier

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**说明**

贝塞尔曲线的绘制

---

### drawBeziers

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

连续贝塞尔曲线的绘制

---

### drawClosedCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

封闭基数样条的绘制

---

### drawClosedCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**说明**

封闭基数样条的绘制

---

### drawCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

基数样条的绘制

---

### drawCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**说明**

基数样条的绘制

---

### drawCurve3

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | 张力 |

**说明**

基数样条的绘制

---

### drawEllipse

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

椭圆的绘制

---

### drawLine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x1` | `&nbsp;` | 起点 X 坐标 |
| `y1` | `&nbsp;` | 起点 Y 坐标 |
| `x2` | `&nbsp;` | 终点 X 坐标 |
| `y2` | `&nbsp;` | 终点 Y 坐标 |

**说明**

线段的绘制

---

### drawLines

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

连续线段的绘制

---

### drawPolygon

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**说明**

多边形的绘制

---

### drawRectangle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

矩形的绘制

---

### drawRectangles

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rects` | `&nbsp;` | 矩形的数组 [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**说明**

多个矩形的绘制

---
