# Threepp.EllipseCurve

椭圆曲线

表示椭圆或圆弧的曲线。

## 成员列表

### 构造函数

- [EllipseCurve](#ellipsecurve)

### 属性

- [aX](#ax)
- [aY](#ay)
- [xRadius](#xradius)
- [yRadius](#yradius)
- [aStartAngle](#astartangle)
- [aEndAngle](#aendangle)
- [aClockwise](#aclockwise)
- [aRotation](#arotation)

### 方法

- [getLength](#getlength)
- [getPoint](#getpoint)

---

### EllipseCurve

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `aX` | `0` | 中心 X 坐标 |
| `aY` | `0` | 中心 Y 坐标 |
| `xRadius` | `1` | X 方向的半径 |
| `yRadius` | `1` | Y 方向的半径 |
| `aStartAngle` | `0` | 开始角度（弧度） |
| `aEndAngle` | `Math.PI*2` | 结束角度（弧度） |
| `aClockwise` | `false` | 是否顺时针 |
| `aRotation` | `0` | 椭圆的旋转角度（弧度） |

**说明**

构造函数

---

### aX

属性 \ 访问: `r/w`

**说明**

中心 X 坐标

---

### aY

属性 \ 访问: `r/w`

**说明**

中心 Y 坐标

---

### xRadius

属性 \ 访问: `r/w`

**说明**

X 方向的半径

---

### yRadius

属性 \ 访问: `r/w`

**说明**

Y 方向的半径

---

### aStartAngle

属性 \ 访问: `r/w`

**说明**

开始角度

---

### aEndAngle

属性 \ 访问: `r/w`

**说明**

结束角度

---

### aClockwise

属性 \ 访问: `r/w`

**说明**

顺时针标志

---

### aRotation

属性 \ 访问: `r/w`

**说明**

旋转角度

---

### getLength

方法

**说明**

获取曲线长度

---

### getPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

获取参数 t (0-1) 的点

---
