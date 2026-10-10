# Texture

纹理类。
与硬件上的纹理基本对应。

通过 invalidate 会使纹理失效，因此不再需要时建议显式调用 invalidate。

## 成员列表

### 构造函数

- [Texture](#texture)
- [Texture](#texture)
- [Texture](#texture)
- [Texture](#texture)

### 属性

- [width](#width)
- [height](#height)
- [memoryWidth](#memorywidth)
- [memoryHeight](#memoryheight)
- [isGray](#isgray)
- [isPowerOfTwo](#ispoweroftwo)
- [nativeHandle](#nativehandle)
- [stretchType](#stretchtype)
- [wrapModeHorizontal](#wrapmodehorizontal)
- [wrapModeVertical](#wrapmodevertical)
- [margin9Patch](#margin9patch)

### 方法

- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [setDrawSize](#setdrawsize)

### 常量

- [stNearest](#stnearest)
- [stLinear](#stlinear)
- [wmRepeat](#wmrepeat)
- [wmClampToEdge](#wmclamptoedge)
- [wmMirror](#wmmirror)

---

### Texture

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `filename` | `string` | `&nbsp;` | 图像文件名 |
| `format` | `int` | `tcfRGBA` | 颜色格式 (tcfRGBA / tcfAlpha / tcfAlphaChannel)<br>选择 `**tcfAlpha**` 时颜色信息会被灰度化 (将**亮度**做成 8bit 纹理)。<br>选择 `**tcfAlphaChannel**` 时，将 α 通道原样做成 8bit 纹理。<br>适合用于仅参照 α 的裁剪遮罩图像，内存只需 RGBA 的 1/4，<br>也不会分配上传用 PBO。“亮度为纯白色、数据在 α”这类常见的遮罩素材<br>在 tcfAlpha 下无法处理，因此使用该指定。传入非 32bpp 的图像时<br>会回退到以往的灰度处理。 |
| `is9patch` | `bool` | `false` | 是否读取 9patch 信息并将其用于 9patch 绘制 |

**说明**

文件读取版构造函数

---

### Texture

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `bitmap` | `Bitmap` | `&nbsp;` | 作为纹理来源的 Bitmap 类的实例 |
| `format` | `int` | `tcfRGBA` | 颜色格式 (tcfRGBA / tcfAlpha / tcfAlphaChannel)<br>值的含义与文件读取版构造函数相同。<br>`**tcfAlpha**` 将亮度灰度化，`**tcfAlphaChannel**` 将 α 通道<br>原样做成 8bit 纹理。 |
| `is9patch` | `bool` | `false` | 是否读取 9patch 信息并将其用于 9patch 绘制 |

**说明**

Bitmap 复制版构造函数

---

### Texture

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 纹理宽度 |
| `height` | `int` | `&nbsp;` | 纹理高度 |
| `format` | `int` | `tcfRGBA` | 颜色格式 (tcfRGBA / tcfAlpha / tcfAlphaChannel)<br>由于内容是未初始化的空纹理，`**tcfAlphaChannel**` 会被视为与 `**tcfAlpha**` 相同。 |

**说明**

尺寸指定版构造函数

纹理的内容未初始化，因此含有垃圾数据。

---

### Texture

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `sizelist` | `Array` | `&nbsp;` | 通过数组以宽度、高度的组合指定要生成 mipmap 的尺寸。 |
| `filename` | `string` | `&nbsp;` | 图像文件名 |
| `type` | `&nbsp;` | `stFastAreaAvg` | 指定缩小算法。与 ImageFunction.operateStretch 的 type 或 Layer.operateStretch 的 type 参数相同。 |
| `typeopt` | `real` | `-1.0` | 3 维插值时的锐度。在其他插值方法下目前没有意义。 |

**说明**

mipmap 生成版构造函数

---

### width

属性 \ 访问: `r/w`

**说明**

宽度 (有效范围)

如果未指定 pot，则与 memoryWidth 相同。

---

### height

属性 \ 访问: `r/w`

**说明**

高度 (有效范围)

如果未指定 pot，则与 memoryHeight 相同。

---

### memoryWidth

属性 \ 访问: `r/w`

**说明**

实际 (硬件上的) 宽度

---

### memoryHeight

属性 \ 访问: `r/w`

**说明**

实际 (硬件上的) 高度

---

### isGray

属性 \ 访问: `r/w`

**说明**

是否为 8bit 颜色 (内部为 Alpha 纹理)

---

### isPowerOfTwo

属性 \ 访问: `r/w`

**说明**

纹理尺寸是否为 2 的幂值

---

### nativeHandle

属性 \ 访问: `r/w`

**说明**

原生句柄 (取决于环境)

在 OpenGL ES2/3 环境下为纹理 ID

---

### stretchType

属性 \ 访问: `r/w`

**说明**

缩放时的插值方法

---

### wrapModeHorizontal

属性 \ 访问: `r/w`

**说明**

水平方向环绕模式

---

### wrapModeVertical

属性 \ 访问: `r/w`

**说明**

垂直方向环绕模式

---

### margin9Patch

属性 \ 访问: `r/w`

**说明**

9patch 边距

指定 is9patch 读取时，可以通过只读方式访问 Rect 类的对象。
未指定或无法读取时为 void。

---

### copyRect

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dleft` | `int` | `&nbsp;` | 复制目标左端 |
| `dtop` | `int` | `&nbsp;` | 复制目标上端 |
| `src` | `Bitmap` | `&nbsp;` | Bitmap 类的对象 |
| `srcRect` | `Rect` | `&nbsp;` | src 的复制源矩形 |

**说明**

矩形复制 (位置指定 Rect 版)

---

### copyRect

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dleft` | `int` | `&nbsp;` | 复制目标左端 |
| `dtop` | `int` | `&nbsp;` | 复制目标上端 |
| `src` | `Bitmap` | `&nbsp;` | Bitmap 类的对象 |
| `sleft` | `int` | `&nbsp;` | 复制源左端位置 |
| `stop` | `int` | `&nbsp;` | 复制源上端位置 |
| `swidth` | `int` | `&nbsp;` | 复制源宽度 |
| `sheight` | `int` | `&nbsp;` | 复制源高度 |

**说明**

矩形复制 (位置指定)

---

### copyRect

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `src` | `Bitmap` | `&nbsp;` | Bitmap 类的对象 |

**说明**

矩形复制 (全量复制)

复制整个 bitmap。超出范围时会被裁剪。

---

### setDrawSize

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 显示基准宽度 |
| `height` | `int` | `&nbsp;` | 显示基准高度 |

**说明**

绘制基准尺寸的设置

用 Canvas.drawTexture 进行等倍绘制时，如果不做任何指定，会按纹理的尺寸绘制，但用该方法设置宽度和高度后，使用该纹理实例绘制时，就会按设置的尺寸绘制。
缩放等也以该尺寸为基准进行绘制。
在内部图像数据的尺寸与平时绘制的尺寸不同的情况下预先设置好，就能以想要显示的尺寸为基准来指定缩放率。

---

### stNearest

常量

**说明**

最近邻点法。设置到 stretchType 属性中。

---

### stLinear

常量

**说明**

线性插值。设置到 stretchType 属性中。

---

### wmRepeat

常量

**说明**

重复。设置到 wrapModeHorizontal/wrapModeVertical 属性中。

---

### wmClampToEdge

常量

**说明**

边缘颜色拉伸。设置到 wrapModeHorizontal/wrapModeVertical 属性中。不是 2 的幂尺寸时必须为该常量 (default)。

---

### wmMirror

常量

**说明**

镜像重复。设置到 wrapModeHorizontal/wrapModeVertical 属性中。

---
