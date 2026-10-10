# GdiPlus.Image

该类由多个插件扩展。

## 插件扩展: layerExDraw

处理图像信息的类
※矢量图像数据的区域有时也可能位于坐标为负的区域

### 成员列表

#### 构造函数

- [Image](#image)

#### 方法

- [load](#load)
- [Clone](#clone)
- [GetBounds](#getbounds)
- [GetHorizontalResolution](#gethorizontalresolution)
- [GetVerticalResolution](#getverticalresolution)
- [GetWidth](#getwidth)
- [GetHeight](#getheight)
- [GetFlags](#getflags)
- [GetLastStatus](#getlaststatus)
- [GetPixelFormat](#getpixelformat)
- [GetType](#gettype)
- [RotateFlip](#rotateflip)

---

### Image

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `void` | 文件名。指定时会自动加载 |

**说明**

构造函数

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 图像文件名 |

**说明**

加载图像

---

### Clone

方法

**返回值**

此对象的副本 (Image)

---

### GetBounds

方法

**返回值**

Bounds 信息 (RectF)，单位为 pixel

**说明**

Bounds 信息的获取

---

### GetHorizontalResolution

方法

**返回值**

水平方向分辨率 (dpi)

---

### GetVerticalResolution

方法

**返回值**

垂直方向分辨率 (dpi)

---

### GetWidth

方法

**返回值**

宽度 (pixel 值：整数)

---

### GetHeight

方法

**返回值**

高度 (pixel 值:整数)

---

### GetFlags

方法

---

### GetLastStatus

方法

---

### GetPixelFormat

方法

---

### GetType

方法

---

### RotateFlip

方法

---

## 插件扩展: layerExVector

处理图像信息的类
※矢量图像数据的区域有时也可能位于坐标为负的区域

### 成员列表

#### 构造函数

- [Image](#image)

#### 属性

- [width](#width)
- [height](#height)
- [isLoaded](#isloaded)

#### 方法

- [load](#load)
- [Clone](#clone)
- [GetBounds](#getbounds)

---

### Image

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `void` | 文件名。指定时会自动加载 |

**说明**

构造函数

---

### width

属性 \ 访问: `r`

**说明**

宽度 (只读)

---

### height

属性 \ 访问: `r`

**说明**

高度 (只读)

---

### isLoaded

属性 \ 访问: `r`

**说明**

是否已加载 (只读)

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 图像文件名 |

**说明**

加载图像

---

### Clone

方法

**返回值**

此对象的副本 (Image)

---

### GetBounds

方法

**返回值**

Bounds 信息 (RectF)，单位为 pixel

**说明**

Bounds 信息的获取

---
