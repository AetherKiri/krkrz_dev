# Threepp.Color

颜色类

表示 RGB 颜色。也可以从数组 [r, g, b]、字典 %[r:, g:, b:]、整数 (0xRRGGBB) 转换。

## 成员列表

### 构造函数

- [Color](#color)

### 属性

- [r](#r)
- [g](#g)
- [b](#b)

### 方法

- [setScalar](#setscalar)
- [setRGB](#setrgb)
- [setHSL](#sethsl)
- [setHex](#sethex)
- [copy](#copy)
- [add](#add)
- [addColors](#addcolors)
- [addScalar](#addscalar)
- [sub](#sub)
- [multiply](#multiply)
- [multiplyScalar](#multiplyscalar)
- [lerp](#lerp)
- [lerpColors](#lerpcolors)
- [lerpHSL](#lerphsl)
- [randomize](#randomize)
- [getHex](#gethex)
- [getHexString](#gethexstring)
- [getStyle](#getstyle)
- [equals](#equals)

---

### Color

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `r` | `1` | 红色分量 (0.0-1.0) 或 hex 值 (0xRRGGBB) |
| `g` | `1` | 绿色分量 (0.0-1.0) |
| `b` | `1` | 蓝色分量 (0.0-1.0) |

**说明**

构造函数

---

### r

属性 \ 访问: `r/w`

**说明**

红色分量 (0.0-1.0)

---

### g

属性 \ 访问: `r/w`

**说明**

绿色分量 (0.0-1.0)

---

### b

属性 \ 访问: `r/w`

**说明**

蓝色分量 (0.0-1.0)

---

### setScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

将所有分量设置为同一个值

---

### setRGB

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `r` | `&nbsp;` |  |
| `g` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |

**说明**

设置 RGB 值

---

### setHSL

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `h` | `&nbsp;` |  |
| `s` | `&nbsp;` |  |
| `l` | `&nbsp;` |  |

**说明**

从 HSL 值设置

---

### setHex

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hex` | `&nbsp;` |  |

**说明**

从十六进制数设置

---

### copy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**说明**

从另一个颜色复制

---

### add

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**说明**

加上颜色

---

### addColors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `c1` | `&nbsp;` |  |
| `c2` | `&nbsp;` |  |

**说明**

设置两个颜色之和

---

### addScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

加上标量

---

### sub

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**说明**

减去颜色

---

### multiply

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**说明**

乘以颜色

---

### multiplyScalar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

乘以标量

---

### lerp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**说明**

线性插值

---

### lerpColors

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `c1` | `&nbsp;` |  |
| `c2` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**说明**

两个颜色之间的线性插值

---

### lerpHSL

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` |  |
| `alpha` | `&nbsp;` |  |

**说明**

在 HSL 空间中进行线性插值

---

### randomize

方法

**说明**

生成随机颜色

---

### getHex

方法

**说明**

获取十六进制值

---

### getHexString

方法

**说明**

获取十六进制字符串

---

### getStyle

方法

**说明**

获取 CSS 格式的字符串

---

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` |  |

**说明**

等价判定

---
