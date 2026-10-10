# Offscreen

离屏。
即所谓的渲染目标。也可以作为纹理使用。
内部会生成 FBO、Renderbuffer、Texture。
如果不把它设置为渲染目标，就没有必要特意使用这个类。
使用 Texture 类的内存效率更好。

## 成员列表

### 构造函数

- [Offscreen](#offscreen)

### 属性

- [width](#width)
- [height](#height)
- [nativeHandle](#nativehandle)

### 方法

- [copyRect](#copyrect)
- [copyRect](#copyrect)
- [copyTo](#copyto)
- [copyTo](#copyto)
- [copyTo](#copyto)
- [exchangeTexture](#exchangetexture)

---

### Offscreen

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 离屏宽度 |
| `height` | `int` | `&nbsp;` | 离屏高度 |

**说明**

生成离屏。

销毁会在 invalidate 时进行，因此不再需要时建议显式调用 invalidate。

---

### width

属性 \ 访问: `r/w`

**说明**

宽度，生成时指定的值[r]

---

### height

属性 \ 访问: `r/w`

**说明**

高度，生成时指定的值[r]

---

### nativeHandle

属性 \ 访问: `r/w`

**说明**

环境相关的句柄[r]

在 OpenGL ES 下为 texture id。

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

矩形复制

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

矩形复制

---

### copyTo

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | 保存目标位图 |
| `dleft` | `int` | `&nbsp;` | 复制目标左端 |
| `dtop` | `int` | `&nbsp;` | 复制目标上端 |
| `sleft` | `int` | `&nbsp;` | 复制源左端 |
| `stop` | `int` | `&nbsp;` | 复制源上端 |
| `width` | `int` | `&nbsp;` | 尺寸宽度 |
| `height` | `int` | `&nbsp;` | 尺寸高度 |

**说明**

复制到位图

---

### copyTo

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | 保存目标位图 |

**说明**

复制到位图

位图会按 Offscreen 的尺寸进行缩放。

---

### copyTo

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `destBitmap` | `Bitmap` | `&nbsp;` | 保存目标位图 |
| `dleft` | `int` | `&nbsp;` | 复制目标左端 |
| `dtop` | `int` | `&nbsp;` | 复制目标上端 |
| `srcRect` | `Rect` | `&nbsp;` | 复制源矩形 |

**说明**

复制到位图

---

### exchangeTexture

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 要交换的 Texture 类的实例。 |

**说明**

将设置到帧缓冲上的纹理与 Texture 类所指的纹理进行交换。

如果不事先使要交换的纹理尺寸保持一致，就会发生异常。
颜色格式也必须为 RGBA。
在渲染途中也不进行交换或许更好 (需确认)。
在交叉淡化等不需要向两者都绘制的情况下，可以将之前的图像作为 Texture 取出，替换为新的 Texture，从而减少开销。
由于会向渲染目标设置 Texture (以便复用)，实质上相当于从 Texture 到内存的复制，但在 OpenGL ES 2.0/3.0 中只能从帧缓冲进行复制。因此 copyTo 方法会执行这样的处理：先设置到帧缓冲再复制，之后返回原来的渲染目标。也就是说，该方法最好极力避免使用，或者说推荐不要使用更合适——它效率低下。如果当前已经设置到帧缓冲上，那还稍好一些。不过，实际是否效率低下，不测量速度就无法得知。原本 CPU <-> GPU 之间的传输就应尽量避免。

---
