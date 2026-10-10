# Bitmap

Bitmap 类是保存图像信息的类。

与 [Layer](Layer.md) 不同，它不是显示要素，因此可以与窗口和图层树无关地单独创建，
即使进行绘制也不会产生重绘通知。用于保存不显示到画面的工作用图像和素材。

Bitmap 自身没有绘制方法。要进行合成、填充、文字绘制、滤镜等处理，
需要把 Bitmap 对象传递给 [ImageFunction](ImageFunction.md) 类的方法。

与 Layer 之间的传递除了通过 [Layer.copyToBitmapFromMainImage](Layer.md#copytobitmapfrommainimage) /
[Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage) 进行之外，
在 Layer 的 `copyRect` / `operateRect` / `stretchCopy` / `operateStretch` / `affineCopy` / `operateAffine` /
`copy9Patch` 中，还可以直接把 Bitmap 指定为复制源 (运算源)。

三者的关系与用法区分请参阅 [Layer 与 Bitmap 与 ImageFunction](../guide/LayerAndBitmap.md)。

## 成员列表

### 构造函数

- [Bitmap](#bitmap)
- [Bitmap](#bitmap)
- [Bitmap](#bitmap)

### 属性

- [width](#width)
- [height](#height)
- [buffer](#buffer)
- [bufferForWrite](#bufferforwrite)
- [bufferPitch](#bufferpitch)
- [loading](#loading)
- [imageWidth](#imagewidth)
- [imageHeight](#imageheight)
- [mainImageBuffer](#mainimagebuffer)
- [mainImageBufferForWrite](#mainimagebufferforwrite)
- [mainImageBufferPitch](#mainimagebufferpitch)

### 方法

- [getPixel](#getpixel)
- [setPixel](#setpixel)
- [getMaskPixel](#getmaskpixel)
- [setMaskPixel](#setmaskpixel)
- [independ](#independ)
- [setSize](#setsize)
- [copyFrom](#copyfrom)
- [save](#save)
- [load](#load)
- [loadAsync](#loadasync)
- [loadHeader](#loadheader)
- [getSaveOption](#getsaveoption)

### 事件

- [onLoaded](#onloaded)

---

### Bitmap

构造函数

**说明**

构建 Bitmap 对象

构建 Bitmap 类的对象。

初始状态下，宽度和高度为 32 像素。

---

### Bitmap

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 以像素为单位指定图像的宽度。 |
| `height` | `&nbsp;` | 以像素为单位指定图像的高度。 |
| `bpp` | `32` | 指定图像各像素的位数。<br>请指定 32 或 8 之一。 |

**说明**

构建 Bitmap 对象

构建指定大小的 Bitmap 类的对象。

---

### Bitmap

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 指定图像的文件名。 |
| `colorkey` | `clNone` | 指定颜色键。<br>值与 [Layer.loadImages](Layer.md#loadimages) 相同。 |

**说明**

构建 Bitmap 对象

从文件构建 Bitmap 类的对象。

---

### width

属性 \ 访问: `r/w`

**说明**

图像宽度

以像素为单位指定图像的宽度。

也可以设置值。

**相关:** [Bitmap.setSize](Bitmap.md#setsize)

---

### height

属性 \ 访问: `r/w`

**说明**

图像高度

以像素为单位指定图像的高度。

也可以设置值。

**相关:** [Bitmap.setSize](Bitmap.md#setsize)

---

### buffer

属性 \ 访问: `r`

**说明**

图像缓冲区指针

表示指向图像 (包含颜色与遮罩(不透明度)信息的 32bpp 位图) 的图像缓冲区左上角的指针。

这个属性是为了给插件等提供直接访问图像缓冲区的手段而准备的。

虽然以整数类型返回，但在插件等中请强制转换为适当的类型 (const unsigned long * 等) 后使用。

请不要向通过这个属性获得的指针写入值。
通过 [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) 获得的指针则可以写入。

图像的大小由 [Bitmap.width](Bitmap.md#width) 和 [Bitmap.height](Bitmap.md#height) 属性表示。

指针的计算方法请参阅 [Bitmap.bufferPitch](Bitmap.md#bufferpitch)。

**相关:** [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) / [Bitmap.bufferPitch](Bitmap.md#bufferpitch)

---

### bufferForWrite

属性 \ 访问: `r`

**说明**

图像缓冲区指针(写入用)

表示指向图像 (包含颜色与遮罩(不透明度)信息的 32bpp 位图) 的图像缓冲区左上角的指针。

这个属性是为了给插件等提供直接访问图像缓冲区的手段而准备的。

虽然以整数类型返回，但在插件等中请强制转换为适当的类型 (unsigned long * 等) 后使用。

与 [Bitmap.buffer](Bitmap.md#buffer) 不同，可以向通过这个属性获得的指针写入值。在吉里吉里内部，完全相同的图像会在多个对象之间共享，但引用这个属性会解除该共享状态。

图像的大小由 [Bitmap.width](Bitmap.md#width) 和 [Bitmap.height](Bitmap.md#height) 属性表示。

指针的计算方法请参阅 [Bitmap.bufferPitch](Bitmap.md#bufferpitch)。

**相关:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.bufferPitch](Bitmap.md#bufferpitch)

---

### bufferPitch

属性 \ 访问: `r`

**说明**

图像缓冲区跨距

表示图像 (包含颜色与遮罩(不透明度)信息的 32bpp 位图) 的图像缓冲区跨距 (到下一条扫描线的字节数)。

这个属性是为了给插件等提供直接访问图像缓冲区的手段而准备的。

将 tjs_uint32 视为 32bit 的整数类型、tjs_uint8 视为 8bit (1byte) 的整数类型，指向图像位置 (x, y) 的
指针用 C 语言编写时可以如下计算。

`( (tjs_uint32*)( (tjs_uint8*)buffer + y*bufferPitch )) + x`

请注意，这个属性返回的不是到下一条扫描线的像素数，而是字节数。这个数值有时会比图像宽度
刚好需要的字节数稍大一些。

请注意，这个属性的值可能为负。

**相关:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite)

---

### loading

属性 \ 访问: `r`

**说明**

确认是否正在异步读取

表示是否正在异步读取。

这个值为真时表示正在异步读取。

请注意，在异步读取过程中访问其他成员会发生异常。

**相关:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.bufferPitch](Bitmap.md#bufferpitch)

---

### imageWidth

属性 \ 访问: `r`

**说明**

图像宽度 ([Bitmap.width](Bitmap.md#width) 的别名)

以像素为单位表示图像的宽度。是返回与 [Bitmap.width](Bitmap.md#width) 相同值的只读别名。

这是为了让 DrawDevice 和插件无需区分 [Layer](Layer.md) 与 Bitmap、能够经由同名属性获取图像
而准备的 (与 [Layer.imageWidth](Layer.md#imagewidth) 同名)。

**相关:** [Bitmap.width](Bitmap.md#width) / [Bitmap.imageHeight](Bitmap.md#imageheight)

---

### imageHeight

属性 \ 访问: `r`

**说明**

图像高度 ([Bitmap.height](Bitmap.md#height) 的别名)

以像素为单位表示图像的高度。是返回与 [Bitmap.height](Bitmap.md#height) 相同值的只读别名。

这是为了让 DrawDevice 和插件无需区分 [Layer](Layer.md) 与 Bitmap、能够经由同名属性获取图像
而准备的 (与 [Layer.imageHeight](Layer.md#imageheight) 同名)。

**相关:** [Bitmap.height](Bitmap.md#height) / [Bitmap.imageWidth](Bitmap.md#imagewidth)

---

### mainImageBuffer

属性 \ 访问: `r`

**说明**

图像缓冲区指针 ([Bitmap.buffer](Bitmap.md#buffer) 的别名)

表示指向图像缓冲区左上角的指针。是返回与 [Bitmap.buffer](Bitmap.md#buffer) 相同值的只读别名。

这是为了让 DrawDevice 和插件无需区分 [Layer](Layer.md) 与 Bitmap、能够经由同名属性获取图像
而准备的 (与 [Layer.mainImageBuffer](Layer.md#mainimagebuffer) 同名)。请不要向这个指针写入值。需要写入时请使用 [Bitmap.mainImageBufferForWrite](Bitmap.md#mainimagebufferforwrite)。

**相关:** [Bitmap.buffer](Bitmap.md#buffer) / [Bitmap.mainImageBufferForWrite](Bitmap.md#mainimagebufferforwrite) / [Bitmap.mainImageBufferPitch](Bitmap.md#mainimagebufferpitch)

---

### mainImageBufferForWrite

属性 \ 访问: `r`

**说明**

图像缓冲区指针(写入用) ([Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) 的别名)

表示指向可写入的图像缓冲区左上角的指针。是返回与 [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) 相同值的只读别名 (引用时会解除图像的共享状态)。

这是为了让 DrawDevice 和插件无需区分 [Layer](Layer.md) 与 Bitmap、能够经由同名属性获取图像
而准备的 (与 [Layer.mainImageBufferForWrite](Layer.md#mainimagebufferforwrite) 同名)。

**相关:** [Bitmap.bufferForWrite](Bitmap.md#bufferforwrite) / [Bitmap.mainImageBuffer](Bitmap.md#mainimagebuffer) / [Bitmap.mainImageBufferPitch](Bitmap.md#mainimagebufferpitch)

---

### mainImageBufferPitch

属性 \ 访问: `r`

**说明**

图像缓冲区跨距 ([Bitmap.bufferPitch](Bitmap.md#bufferpitch) 的别名)

表示图像缓冲区的跨距 (到下一条扫描线的字节数)。是返回与 [Bitmap.bufferPitch](Bitmap.md#bufferpitch) 相同值的只读别名 (值可能为负)。

这是为了让 DrawDevice 和插件无需区分 [Layer](Layer.md) 与 Bitmap、能够经由同名属性获取图像
而准备的 (与 [Layer.mainImageBufferPitch](Layer.md#mainimagebufferpitch) 同名)。

**相关:** [Bitmap.bufferPitch](Bitmap.md#bufferpitch) / [Bitmap.mainImageBuffer](Bitmap.md#mainimagebuffer) / [Bitmap.mainImageBufferForWrite](Bitmap.md#mainimagebufferforwrite)

---

### getPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定要获取的 x 坐标值。 |
| `y` | `&nbsp;` | 以像素为单位指定要获取的 y 坐标值。 |

**返回值**

像素值

**说明**

像素值的获取

获取图像的像素值。

**相关:** [Bitmap.setPixel](Bitmap.md#setpixel)

---

### setPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定要设置的 x 坐标值。 |
| `y` | `&nbsp;` | 以像素为单位指定要设置的 y 坐标值。 |
| `value` | `&nbsp;` | 指定要设置的像素值。 |

**说明**

像素值的设置

设置图像的像素值。

**相关:** [Bitmap.getPixel](Bitmap.md#getpixel)

---

### getMaskPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定要获取的 x 坐标值。 |
| `y` | `&nbsp;` | 以像素为单位指定要获取的 y 坐标值。 |

**返回值**

像素的 Alpha 值

**说明**

像素的 Alpha 值的获取

获取图像像素的 Alpha 值。

**相关:** [Bitmap.setMaskPixel](Bitmap.md#setmaskpixel)

---

### setMaskPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定要设置的 x 坐标值。 |
| `y` | `&nbsp;` | 以像素为单位指定要设置的 y 坐标值。 |
| `value` | `&nbsp;` | 指定要设置的像素的 Alpha 值。 |

**说明**

像素的 Alpha 值的获取

设置图像像素的 Alpha 值。

**相关:** [Bitmap.getMaskPixel](Bitmap.md#getmaskpixel)

---

### independ

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `copy` | `true` | 指定在解除共享状态时，是否复制原来的图像。<br>指定为真时会复制原来的图像。指定为假时不会复制原来的图像，图像的<br>内容将变为未定义。 |

**说明**

解除图像的共享

强制解除图像的共享状态。

吉里吉里在用 assignImages 等整体复制图像时，实际上不会复制
图像缓冲区，而是共享同一图像。

通常，在即将对图像进行更改之前，这个共享状态会被自动解除，
但用这个方法可以强制解除。

给 copy 参数指定 false 时，图像的共享会被解除，但不保证
继承原来的图像 (图像内容将变为未定义)，不过可以更高速地进行共享的解除。如果要改写全部
图像，就不需要继承原来的图像，因此在绘制之前预先给这个方法指定 false 调用，
有时会提高效率。

这个方法在图像未被共享时不做任何事。

---

### setSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 以像素为单位指定图像的宽度。<br>这个值也可以通过 [Bitmap.width](Bitmap.md#width) 属性获取和设置。 |
| `height` | `&nbsp;` | 以像素为单位指定图像的高度。<br>这个值也可以通过 [Bitmap.height](Bitmap.md#height) 属性获取和设置。 |

**说明**

图像大小的设置

指定图像大小。

---

### copyFrom

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 指定作为复制源的 Bitmap 对象。 |

**说明**

图像的复制

进行图像的复制。

虽说是复制，但实际上只是变为“同一个图像被两个以上的对象共享”的状态，因此
这个方法几乎不花费执行时间。

---

### save

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定要保存的存储名。 |
| `type` | `"bmp"` | 用字符串指定要保存的图像格式。在当前版本中可以指定以下格式。<br>"**bmp**" 或 "**bmp32**"<br>32bpp 的 BMP。也会保存 Alpha 通道(遮罩)。<br>"**bmp24**"<br>24bpp 的 BMP。不会保存 Alpha 通道(遮罩)。<br>"**bmp8**"<br>8bpp 的 BMP。不会保存 Alpha 通道(遮罩)。图像会<br>使用 252 色固定调色板的 4×4 有序抖动进行减色。<br>"**jpg**"<br>JPEG。不会保存 Alpha 通道(遮罩)。图像会<br>以质量 90% 保存。<br>"**jpg###**"<br>JPEG。不会保存 Alpha 通道(遮罩)。图像会<br>以由 ### 指定的质量保存。"jpg010" 为 10%、"jpg100" 为 100%、"jpg080" 为 80%。<br>"**png**"<br>32bpp 的 PNG。也会保存 Alpha 通道(遮罩)。<br>"**png24**"<br>24bpp 的 PNG。不会保存 Alpha 通道(遮罩)。<br>"**tlg5**"<br>32bpp 的 TLG5。也会保存 Alpha 通道(遮罩)。<br>"**tlg524**"<br>24bpp 的 TLG5。不会保存 Alpha 通道(遮罩)。<br>"**tlg6**"<br>32bpp 的 TLG6。也会保存 Alpha 通道(遮罩)。<br>"**tlg624**"<br>24bpp 的 TLG6。不会保存 Alpha 通道(遮罩)。 |
| `meta` | `null` | TLG 格式时，以字典形式指定要保存的标签信息。<br>其他格式时指定附加选项(1.3.0 及以后)。<br>可指定的选项可以通过 getSaveOption 获取。 |

**说明**

图像的保存

以 type 指定的图像格式，将文件保存到 name 指定的存储 (文件) 中。

**相关:** [Bitmap.getSaveOption](Bitmap.md#getsaveoption)

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `image` | `&nbsp;` | 指定要读取的图像存储。 |
| `colorkey` | `clNone` | 指定要读取图像的颜色键 (透明色)。<br>以 0xRRGGBB 格式指定颜色时，该颜色将成为颜色键。<br>指定 `**clPalIdx**` 加上任意调色板索引后的数值时，<br>该调色板索引将成为透明色 (仅限 256 色以下的图像)。<br>指定 `**clAdapt**` 时，图像最上面一行中<br>使用最多的颜色会自动成为透明色。<br>指定 `**clAlphaMat**` 加上表示 0xRRGGBB<br>格式颜色的数值后的值时，图像会使用<br>Alpha 混合(ltAlpha 的方式)被叠加到该颜色之上。<br>例如，指定 (clAlphaMat + 0xffffff) 时，<br>读取到的图像会被叠加到白色之上。<br>图像将全部成为不透明图像<br>( 图像将全部成为不透明，但<br>这个模式下标签信息完全不会被更改，<br>请注意 )。 |

**返回值**

标签信息的字典数组

**说明**

图像的读取

读取图像。

作为返回值，会返回标签信息 (该图像的图层类型、显示位置等关于图像本身的信息) 的字典数组。

图像没有标签信息时返回 null。

在当前版本中，只有 PNG、TLG5/6 格式可以拥有标签信息。关于可获取的信息，请参阅[图像格式转换器](../guide/TPC.md)。

---

### loadAsync

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `image` | `&nbsp;` | 指定要读取的图像存储。<br>请注意，这里指定的文件名需要包含扩展名。<br>没有扩展名时会找不到文件并导致错误。 |

**说明**

图像的异步读取

异步读取图像。

读取的完成可以通过 [Bitmap.onLoaded](Bitmap.md#onloaded) 接收。

是否正在异步读取可以通过 [Bitmap.loading](Bitmap.md#loading) 确认。

异步读取过程中，访问 [Bitmap.loading](Bitmap.md#loading) 以外的成员会发生异常。

也请确认 [Bitmap.onLoaded](Bitmap.md#onloaded) 的说明。

**相关:** [Bitmap.onLoaded](Bitmap.md#onloaded) / [Bitmap.loading](Bitmap.md#loading) / [Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage)

---

### loadHeader

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `image` | `&nbsp;` | 指定要读取的图像存储。<br>请注意，这里指定的文件名需要包含扩展名。<br>没有扩展名时会找不到文件并导致错误。 |

**返回值**

信息的字典数组

**说明**

图像信息的读取(1.3.0 及以后)

只读取图像信息。

由于不进行图像的读取，只想获取信息时可以高速读取。

返回的字典中 width、height 是必需的，其他信息取决于图像格式。

---

### getSaveOption

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 指定图像格式。<br>指定方法与 save 方法相同。 |

**返回值**

附加信息的字典数组

**说明**

图像保存附加信息获取(1.3.0 及以后)

获取保存图像时可以指定的附加信息。

**相关:** [Bitmap.save](Bitmap.md#save)

---

### onLoaded

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `meta` | `&nbsp;` | 读取到的图像的标签信息。 |
| `async` | `&nbsp;` | 是否是通过异步方式读取的。<br>图像数据在缓存内时，会在 [Bitmap.loadAsync](Bitmap.md#loadasync) 执行过程中发生本事件。 |
| `error` | `&nbsp;` | 图像读取时是否发生了错误。 |
| `message` | `&nbsp;` | 错误消息。<br>发生错误时，会传递错误消息。 |

**说明**

异步读取已完成

在异步读取完成时发生。

读取到的图像可以通过 [Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage) 复制到 Layer。

读取处理是异步的，因此在读取完成时，用于接收该图像的 Layer 可能已经被无效化。

在本事件中访问其他对象时，请确认其没有被无效化。

或者，请确保在完成本事件之前，目标对象不会被无效化。

**相关:** [Bitmap.loadAsync](Bitmap.md#loadasync) / [Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage)

---
