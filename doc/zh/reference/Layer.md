# Layer

Layer 类是用于管理**图层**的类。

除了图像缓冲区 (主图像与区域图像) 之外，还持有父子树、显示位置、不透明度、输入事件，是
“被显示的图像”。不伴随显示的工作用图像由 [Bitmap](Bitmap.md) 类处理，其加工则
使用 [ImageFunction](ImageFunction.md) 类。

三者的关系与用法区分请参阅 [Layer 与 Bitmap 与 ImageFunction](../guide/LayerAndBitmap.md)。

### 朗读 (屏幕阅读器) 用成员

把 [ElementsDialog.a11yLayers](ElementsDialog.md#a11ylayers) 设为真时，处于焦点链中的
Layer 会出现在屏幕阅读器的朗读树中 (名字是 [hint](#hint))。
在 Layer 上添加以下成员，可以改变朗读方式。它们都是可选的，只是引擎本体读取其值的
约定 (Layer 类本身并不持有这些成员)。

| 成员 | 内容 |
|---|---|
| `a11yName` / `a11yRole` | 名字 / 角色 (与 [ElementsDialog.setGameA11y](ElementsDialog.md#setgamea11y) 相同的名字)。只要有其中之一，无法获取焦点的 Layer (标题或说明文本) 也会被载入 |
| `a11yValue` / `a11yDescription` | 值 / 补充说明 |
| `a11yStates` | 数组或 `"checked,selected"` 形式。`disabled` 也会由 [enabled](#enabled) 附加 |
| `a11yHidden` | 为真时连同子级一起移除 (在 `setGameA11y` 中为自己载入的 Layer 设置) |
| `onA11yAction(action, arg)` | 接收来自屏幕阅读器的操作。返回 false 时也会执行默认处理 |

默认处理是：`"focus"` 对应 [focus](#focus)，`"click"` 则先设置焦点再发送
Enter 键。值的更改 (`"increment"` / `"set_value"` 等) 只能由 `onA11yAction`
接收。把这些做成 property 的 getter 时请保持轻量
(最多每 150ms 重新读取一次)。完整规格请参阅
[无障碍 (屏幕阅读器) 支持](../specification/accessibility.md)。

## 成员列表

### 构造函数

- [Layer](#layer)

### 属性

- [parent](#parent)
- [children](#children)
- [order](#order)
- [absolute](#absolute)
- [absoluteOrderMode](#absoluteordermode)
- [visible](#visible)
- [cached](#cached)
- [nodeVisible](#nodevisible)
- [neutralColor](#neutralcolor)
- [hasImage](#hasimage)
- [opacity](#opacity)
- [window](#window)
- [isPrimary](#isprimary)
- [left](#left)
- [top](#top)
- [width](#width)
- [height](#height)
- [imageLeft](#imageleft)
- [imageTop](#imagetop)
- [imageWidth](#imagewidth)
- [imageHeight](#imageheight)
- [clipLeft](#clipleft)
- [clipTop](#cliptop)
- [clipWidth](#clipwidth)
- [clipHeight](#clipheight)
- [type](#type)
- [face](#face)
- [holdAlpha](#holdalpha)
- [imageModified](#imagemodified)
- [hitType](#hittype)
- [hitThreshold](#hitthreshold)
- [cursor](#cursor)
- [cursorX](#cursorx)
- [cursorY](#cursory)
- [hint](#hint)
- [showParentHint](#showparenthint)
- [focusable](#focusable)
- [prevFocusable](#prevfocusable)
- [nextFocusable](#nextfocusable)
- [joinFocusChain](#joinfocuschain)
- [focused](#focused)
- [enabled](#enabled)
- [nodeEnabled](#nodeenabled)
- [attentionLeft](#attentionleft)
- [attentionTop](#attentiontop)
- [useAttention](#useattention)
- [imeMode](#imemode)
- [callOnPaint](#callonpaint)
- [font](#font)
- [name](#name)
- [mainImageBuffer](#mainimagebuffer)
- [mainImageBufferForWrite](#mainimagebufferforwrite)
- [mainImageBufferPitch](#mainimagebufferpitch)
- [provinceImageBuffer](#provinceimagebuffer)
- [provinceImageBufferForWrite](#provinceimagebufferforwrite)
- [provinceImageBufferPitch](#provinceimagebufferpitch)
- [ignoreHintSensing](#ignorehintsensing)
- [nodeFocusable](#nodefocusable)

### 方法

- [moveBefore](#movebefore)
- [moveBehind](#movebehind)
- [bringToBack](#bringtoback)
- [bringToFront](#bringtofront)
- [loadImages](#loadimages)
- [loadProvinceImage](#loadprovinceimage)
- [getMainPixel](#getmainpixel)
- [setMainPixel](#setmainpixel)
- [getMaskPixel](#getmaskpixel)
- [setMaskPixel](#setmaskpixel)
- [getProvincePixel](#getprovincepixel)
- [setProvincePixel](#setprovincepixel)
- [getLayerAt](#getlayerat)
- [releaseCapture](#releasecapture)
- [setPos](#setpos)
- [setClip](#setclip)
- [setSize](#setsize)
- [setSizeToImageSize](#setsizetoimagesize)
- [setImagePos](#setimagepos)
- [setImageSize](#setimagesize)
- [independMainImage](#independmainimage)
- [independProvinceImage](#independprovinceimage)
- [fillRect](#fillrect)
- [colorRect](#colorrect)
- [drawText](#drawtext)
- [drawGlyph](#drawglyph)
- [drawShapedText](#drawshapedtext)
- [drawShapedTextArea](#drawshapedtextarea)
- [measureShapedText](#measureshapedtext)
- [shapedTextCount](#shapedtextcount)
- [drawVerticalTextArea](#drawverticaltextarea)
- [measureVerticalTextArea](#measureverticaltextarea)
- [copyRect](#copyrect)
- [copy9Patch](#copy9patch)
- [piledCopy](#piledcopy)
- [operateRect](#operaterect)
- [stretchCopy](#stretchcopy)
- [operateStretch](#operatestretch)
- [affineCopy](#affinecopy)
- [operateAffine](#operateaffine)
- [doBoxBlur](#doboxblur)
- [adjustGamma](#adjustgamma)
- [doGrayScale](#dograyscale)
- [flipLR](#fliplr)
- [flipUD](#flipud)
- [convertType](#converttype)
- [update](#update)
- [setCursorPos](#setcursorpos)
- [focus](#focus)
- [focusPrev](#focusprev)
- [focusNext](#focusnext)
- [setMode](#setmode)
- [removeMode](#removemode)
- [setAttentionPos](#setattentionpos)
- [beginTransition](#begintransition)
- [stopTransition](#stoptransition)
- [assignImages](#assignimages)
- [saveLayerImage](#savelayerimage)
- [copyToBitmapFromMainImage](#copytobitmapfrommainimage)
- [copyFromBitmapToMainImage](#copyfrombitmaptomainimage)
- [dump](#dump)
- [releaseTouchCapture](#releasetouchcapture)

### 事件

- [onClick](#onclick)
- [onDoubleClick](#ondoubleclick)
- [onMouseDown](#onmousedown)
- [onMouseUp](#onmouseup)
- [onMouseMove](#onmousemove)
- [onMouseEnter](#onmouseenter)
- [onMouseLeave](#onmouseleave)
- [onMouseWheel](#onmousewheel)
- [onKeyDown](#onkeydown)
- [onKeyUp](#onkeyup)
- [onKeyPress](#onkeypress)
- [onHitTest](#onhittest)
- [onBlur](#onblur)
- [onFocus](#onfocus)
- [onNodeDisabled](#onnodedisabled)
- [onNodeEnabled](#onnodeenabled)
- [onSearchPrevFocusable](#onsearchprevfocusable)
- [onSearchNextFocusable](#onsearchnextfocusable)
- [onBeforeFocus](#onbeforefocus)
- [onPaint](#onpaint)
- [onTransitionCompleted](#ontransitioncompleted)
- [onTouchDown](#ontouchdown)
- [onTouchUp](#ontouchup)
- [onTouchMove](#ontouchmove)
- [onTouchScaling](#ontouchscaling)
- [onTouchRotate](#ontouchrotate)
- [onMultiTouch](#onmultitouch)

---

### Layer

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 指定将持有该图层的窗口 ( [Window](Window.md) 类的<br>对象 )。<br>窗口一经确定便无法更改。 |
| `parent` | `&nbsp;` | 指定作为该图层的父级的图层。<br>指定 null 时成为主图层。<br>主图层在窗口中只能存在一个，并且在使用图层时<br>必定存在一个，是所有图层的父图层。<br>不过，根据绘制设备 (可通过 [Window.drawDevice](Window.md#drawdevice) 设置) 的不同，有些窗口<br>可以拥有多个主图层。<br>图层的父级可以通过 [Layer.parent](Layer.md#parent) 属性更改。 |

**说明**

构建 Layer 对象

构建 Layer 类的对象。

Layer 类以非显示状态构建。

---

### parent

属性 \ 访问: `r/w`

**说明**

父图层

表示父图层对象。

也可以设置值。设置值后会成为该图层的子级。

不能成为属于不同窗口或不同主图层的图层的子级，也不能成为自己自身或自己后代的
子级。

用 invalidate 使图层失效时，子图层不会自动失效，
而是会作为与父级分离 (不持有父级) 的有效图层保留下来。分离后的
图层虽然不会显示到画面，但绘制方法等仍会不抛出异常地运行，
因此请注意：即使绘制到了旧的引用上也不容易察觉。要连同整个子树
一起废弃时，请 (递归地) 逐个 invalidate 子图层。

---

### children

属性 \ 访问: `r`

**说明**

子图层数组

表示存储了子图层的数组对象。

向这里得到的数组写入值、删除或添加项目等都不会反映到实际的图层状态中。请认为只能进行读取。

---

### order

属性 \ 访问: `r/w`

**说明**

相对位置

表示具有相同父级的兄弟图层之间的顺序。值越小越显示在后面。

设置值可以改变兄弟图层之间的顺序。设置值后，
父图层的 [Layer.absoluteOrderMode](Layer.md#absoluteordermode) 属性会被设为假。

**相关:** [Layer.absolute](Layer.md#absolute) / [Layer.absoluteOrderMode](Layer.md#absoluteordermode) / [Layer.bringToBack](Layer.md#bringtoback) / [Layer.bringToFront](Layer.md#bringtofront)

---

### absolute

属性 \ 访问: `r/w`

**说明**

绝对位置

表示具有相同父级的兄弟图层之间的叠加顺序。值越小越显示在后面。

与 [Layer.order](Layer.md#order) 属性不同，同一批兄弟之间的值不需要连续。

设置值可以改变兄弟图层之间的顺序。设置值后，
父图层的 [Layer.absoluteOrderMode](Layer.md#absoluteordermode) 属性会被设为真。

**相关:** [Layer.order](Layer.md#order) / [Layer.absoluteOrderMode](Layer.md#absoluteordermode) / [Layer.bringToBack](Layer.md#bringtoback) / [Layer.bringToFront](Layer.md#bringtofront)

---

### absoluteOrderMode

属性 \ 访问: `r/w`

**说明**

是否为绝对位置模式

表示直属子图层的叠加顺序模式。也可以设置值。

指定假时变为相对位置指定，由 [Layer.order](Layer.md#order) 属性
表示其顺序。

指定真时变为绝对位置指定，由 [Layer.absolute](Layer.md#absolute) 属性
表示其顺序。

**相关:** [Layer.order](Layer.md#order) / [Layer.absolute](Layer.md#absolute) / [Layer.bringToBack](Layer.md#bringtoback) / [Layer.bringToFront](Layer.md#bringtofront)

---

### visible

属性 \ 访问: `r/w`

**说明**

是否可见

表示是否可见。也可以设置值。

指定假时变为不可见。指定真时变为可见。

---

### cached

属性 \ 访问: `r/w`

**说明**

是否进行缓存

表示是否进行缓存。也可以设置值。

设置为进行缓存时，会预先持有将自身与子图层全部叠加后的状态图像，此后只要自身或子图层没有发生更改，就不会进行与自身及子图层叠加有关的图像运算(发生更改时会自动重新构建缓存)。

设置为不进行缓存时，每次画面更新时都会进行叠加运算。

默认不进行缓存，但在转场过程中会自动启用缓存 (不过该属性并不表示转场中等情况下自动启用的缓存的有无状态)。

对于某个图层，如果已知其图像和子图层的图像及状态不会变化，且画面会被频繁改写，那么在该图层进行缓存可以提高整体性能。

---

### nodeVisible

属性 \ 访问: `r`

**说明**

节点是否可见

表示节点是否可见。

父图层中只要有一个不可见的图层就为假。

父图层全部可见时为真。

---

### neutralColor

属性 \ 访问: `r/w`

**说明**

中性色

以 0xAARRGGBB 形式表示图层的中性色。也可以设置值。

图层的中性色会在更改 [Layer.type](Layer.md#type) 属性时，被设置为该类型的中性色。

中性色在图层图像的尺寸被扩展时，成为填充扩展部分的初始值。

通过设置值，可以指定图层图像尺寸扩展时的初始颜色。

---

### hasImage

属性 \ 访问: `r/w`

**说明**

图层是否持有图像

表示图层是否持有图像。也可以设置值。

指定真时图层持有图像。这是默认值。

指定假时图层的图像被释放，图层不再持有图像。

设置 [Layer.type](Layer.md#type) 属性时，hasImage 会被重置为真。

图层不持有图像时，如果 [Layer.type](Layer.md#type) 为 **ltOpaque**，则图层被视为整个面
被 [Layer.neutralColor](Layer.md#neutralcolor) 填充后显示。

其他类型的情况下被视为完全透明。

该属性为假的图层，当 [Layer.hitType](Layer.md#hittype) 为 htMask 时，整个面被视为不透明度 0 (完全透明)。另外，不能进行绘制或操作字体。

该属性为假的图层，通常用于汇总多个子图层，让自身只是作为透明的图层使用。

---

### opacity

属性 \ 访问: `r/w`

**说明**

不透明度

表示图层的不透明度。可以设置值。

值为 0 ~ 255 的整数，值越大显示越不透明。

---

### window

属性 \ 访问: `r`

**说明**

窗口对象

表示持有该图层的窗口对象。

---

### isPrimary

属性 \ 访问: `r`

**说明**

是否为主图层

表示是否为主图层。

主图层是不持有父级的图层，也是显示在最后面的图层。

---

### left

属性 \ 访问: `r/w`

**说明**

左端位置

以父图层的显示坐标中的像素为单位指定图层左端位置。

也可以设置值。

**相关:** [Layer.setPos](Layer.md#setpos)

---

### top

属性 \ 访问: `r/w`

**说明**

上端位置

以父图层的显示坐标中的像素为单位指定图层上端位置。

也可以设置值。

**相关:** [Layer.setPos](Layer.md#setpos)

---

### width

属性 \ 访问: `r/w`

**说明**

宽度

以像素为单位指定图层的显示宽度。

也可以设置值。

**相关:** [Layer.setSize](Layer.md#setsize)

---

### height

属性 \ 访问: `r/w`

**说明**

高度

以像素为单位指定图层的显示高度。

也可以设置值。

**相关:** [Layer.setSize](Layer.md#setsize)

---

### imageLeft

属性 \ 访问: `r/w`

**说明**

图层图像左端偏移

以像素为单位指定图层显示偏移的左端。

也可以设置值。

**相关:** [Layer.setImagePos](Layer.md#setimagepos)

---

### imageTop

属性 \ 访问: `r/w`

**说明**

图层图像上端偏移

以像素为单位指定图层显示偏移的上端。

也可以设置值。

**相关:** [Layer.setImagePos](Layer.md#setimagepos)

---

### imageWidth

属性 \ 访问: `r/w`

**说明**

图像宽度

以像素为单位指定图层的图像宽度。

也可以设置值。

**相关:** [Layer.setImageSize](Layer.md#setimagesize)

---

### imageHeight

属性 \ 访问: `r/w`

**说明**

图像高度

以像素为单位指定图层的图像高度。

也可以设置值。

**相关:** [Layer.setSize](Layer.md#setsize)

---

### clipLeft

属性 \ 访问: `r/w`

**说明**

绘制裁剪矩形左端位置

以像素为单位指定绘制裁剪矩形的左端。

也可以设置值。

**相关:** [Layer.setClip](Layer.md#setclip)

---

### clipTop

属性 \ 访问: `r/w`

**说明**

绘制裁剪矩形上端位置

以像素为单位指定绘制裁剪矩形的上端。

也可以设置值。

**相关:** [Layer.setClip](Layer.md#setclip)

---

### clipWidth

属性 \ 访问: `r/w`

**说明**

绘制裁剪矩形宽度

以像素为单位指定绘制裁剪矩形的宽度。

也可以设置值。

**相关:** [Layer.setClip](Layer.md#setclip)

---

### clipHeight

属性 \ 访问: `r/w`

**说明**

绘制裁剪矩形高度

以像素为单位指定绘制裁剪矩形的高度。

也可以设置值。

**相关:** [Layer.setClip](Layer.md#setclip)

---

### type

属性 \ 访问: `r/w`

**说明**

图层显示类型

表示图层的显示类型。也可以设置值。

- 指定 `**ltOpaque**` 或 `**ltCoverRect**` 时，逐像素的 Alpha 混合将无效。`ltCoverRect` 与 `ltOpaque` 含义相同。
[Layer.opacity](Layer.md#opacity) 属性为 255 时，将作为完全
不透明的矩形显示。遮罩图像被忽略。适合该类型的绘制方式 (由 [Layer.face](Layer.md#face) 指定) 是 `**dfOpaque**`。
- 指定 `**ltAlpha**` 或 `**ltTransparent**` 时，逐像素的 Alpha 混合将有效。`ltTransparent` 与 `ltAlpha` 含义相同。
遮罩图像用于透明度处理。适合该类型的绘制方式是 `**dfAlpha**`。
- 指定 `**ltAddAlpha**` 时，逐像素的加法 Alpha 混合将有效。适合该类型的绘制方式是 `**dfAddAlpha**`。
- 指定 `**ltAdditive**` 时，进行加法合成。遮罩图像被忽略。适合该类型的绘制方式是 `**dfOpaque**`。
- 指定 `**ltSubtractive**` 时，进行减法合成。遮罩图像被忽略。适合该类型的绘制方式是 `**dfOpaque**`。
- 指定 `**ltMultiplicative**` 时，进行乘法合成。遮罩图像被忽略。适合该类型的绘制方式是 `**dfOpaque**`。
- 指定 `**ltDodge**` 时，进行减淡合成。遮罩图像被忽略。适合该类型的绘制方式是 `**dfOpaque**`。
- 指定 `**ltDarken**` 时，进行变暗合成。遮罩图像被忽略。适合该类型的绘制方式是 `**dfOpaque**`。
- 指定 `**ltLighten**` 时，进行变亮合成。遮罩图像被忽略。适合该类型的绘制方式是 `**dfOpaque**`。
- 指定 `**ltScreen**` 时，进行滤色乘法合成。遮罩图像被忽略。适合该类型的绘制方式是 `**dfOpaque**`。

关于其他图层显示类型，请参阅 [图形系统](../guide/GraphicSystem.md)。

**相关:** [Layer.face](Layer.md#face)

---

### face

属性 \ 访问: `r/w`

**说明**

绘制方式

表示对图层的绘制方式。也可以设置值。

在吉里吉里 2.23 beta 1 以前称为“绘制面”。

- 指定 `**dfAlpha**` 或 `**dfBoth**` 时，图像被视为带 Alpha 通道的图像进行绘制。`dfBoth` 与 `dfAlpha` 相同。与该绘制方法对应的图层类型是 `ltTransparent` 或 `ltAlpha`。
- 指定 `**dfAddAlpha**` 时，图像被视为带加法 Alpha 通道的图像进行绘制。与该绘制方法对应的图层类型是 `ltAddAlpha`。
-  指定 `**dfOpaque**` 或 `**dfMain**` 时，图层的图像全部被视为完全不透明进行绘制。与该绘制方法对应的图层类型是 `ltOpaque` 或 `ltCoverRect`，或者是 `ltAdditive` 这类进行算术/逻辑运算的图层类型。
- 指定 `**dfMask**` 时，将遮罩图像 (Alpha 通道) 作为绘制的对象。
- 指定 `**dfProvince**` 时，将区域图像作为绘制的对象。
- 指定 `**dfAuto**` 时，按照当前的 [Layer.type](Layer.md#type) 属性自动决定绘制方式。刚创建的图层的绘制方式是 dfAuto。

根据该属性的值，有些方法无法操作。

**相关:** [Layer.type](Layer.md#type)

---

### holdAlpha

属性 \ 访问: `r/w`

**说明**

是否保护 Alpha 通道

指定在绘制时是否保护 Alpha 通道。也可以设置值。

默认为假。

在吉里吉里 2.23 beta 1 以前，各绘制方法有名为 hda 的参数，其运行与该属性相同，从 2.23 beta 2 起被分离为属性。

在一些绘制运算中，当 [Layer.face](Layer.md#face) 属性为 **dfOpaque** 时，可以用该属性指定是否保持图像的 Alpha 通道 (遮罩图像)。对许多方法而言，将该属性设为假可以实现更高速的绘制。当 [Layer.type](Layer.md#type) 既不是 **ltAlpha** 也不是 **ltAddAlpha** 时，不会使用图像的 Alpha 通道，因此将该属性设为假也没有问题。不过，该属性为假时 Alpha 通道会被破坏。

以下方法不受该属性影响。

[Layer.loadImages](Layer.md#loadimages)

[Layer.loadProvinceImage](Layer.md#loadprovinceimage)

[Layer.setMainPixel](Layer.md#setmainpixel)

[Layer.setMaskPixel](Layer.md#setmaskpixel)

[Layer.setProvincePixel](Layer.md#setprovincepixel)

[Layer.piledCopy](Layer.md#piledcopy)

[Layer.adjustGamma](Layer.md#adjustgamma)(始终保护 Alpha 通道)

[Layer.doGrayScale](Layer.md#dograyscale)(始终保护 Alpha 通道)

[Layer.flipLR](Layer.md#fliplr)

[Layer.flipUD](Layer.md#flipud)

[Layer.assignImages](Layer.md#assignimages)

以下方法受该属性影响。

[Layer.copyRect](Layer.md#copyrect)

[Layer.stretchCopy](Layer.md#stretchcopy)

[Layer.affineCopy](Layer.md#affinecopy)

[Layer.fillRect](Layer.md#fillrect)

[Layer.colorRect](Layer.md#colorrect)

[Layer.drawText](Layer.md#drawtext)

[Layer.operateRect](Layer.md#operaterect)

[Layer.operateStretch](Layer.md#operatestretch)

[Layer.operateAffine](Layer.md#operateaffine)

---

### imageModified

属性 \ 访问: `r/w`

**说明**

图像是否已更改

表示图层的图像是否已更改。也可以设置值。

对图层的图像进行绘制、或更改图层的图像尺寸时会自动设为真。

如果预先将该属性设为假，那么图层的图像被更改时它会变为真，因此
可以知道图层的图像是否已被更改。

该属性本身不影响图层的运行。

---

### hitType

属性 \ 访问: `r/w`

**说明**

命中判定类型

表示鼠标事件的命中判定类型。也可以设置值。

指定 `**htProvince**` 时，只有区域图像中非 0 的区域才会接收
鼠标事件。

指定 `**htMask**` 时，只有在遮罩(不透明度)图像的值为 [Layer.hitThreshold](Layer.md#hitthreshold) 属性指
定的值以上时才会接收鼠标事件。

未被接收的鼠标事件会由更后方的图层处理。

初始状态下为 `htMask`。

---

### hitThreshold

属性 \ 访问: `r/w`

**说明**

命中判定阈值

表示鼠标事件的命中判定的阈值位置。也可以设置值。

该属性仅在 [Layer.hitType](Layer.md#hittype) 属性为 htMask 时有效，
遮罩(不透明度)图像的值在该属性指定的值以上时会接收鼠标消息。

指定 0 时所有鼠标消息都会被接收。指定 256 时所有鼠标消息都
不会被接收。

初始状态下为 16。

---

### cursor

属性 \ 访问: `r/w`

**说明**

鼠标光标

表示图层的鼠标光标。也可以设置值。

作为鼠标光标，可以指定以 cr 开头的**鼠标光标常量**，
或扩展名为 .cur 的鼠标光标、扩展名为 .ani 的动画鼠标光标的
存储名。

---

### cursorX

属性 \ 访问: `r/w`

**说明**

鼠标光标 x 位置

以显示坐标中的像素为单位表示图层鼠标光标的 x 坐标值。也可以设置值。

设置值时，只设置 cursorX 属性并不会移动鼠标光标。
接着设置 cursorY 属性时鼠标光标才会移动。

**相关:** [Layer.setCursorPos](Layer.md#setcursorpos)

---

### cursorY

属性 \ 访问: `r/w`

**说明**

鼠标光标 y 位置

以显示坐标中的像素为单位表示图层鼠标光标的 y 坐标值。也可以设置值。

设置值时，只设置 cursorX 属性并不会移动鼠标光标。
接着设置 cursorY 属性时鼠标光标才会移动。

**相关:** [Layer.setCursorPos](Layer.md#setcursorpos)

---

### hint

属性 \ 访问: `r/w`

**说明**

提示

表示图层的提示字符串。也可以设置值。

提示字符串是在图层上让鼠标光标稍微静止时，显示在鼠标光标附近的
字符串。

不想显示提示时请指定空字符串。

**相关:** [Layer.showParentHint](Layer.md#showparenthint)

---

### showParentHint

属性 \ 访问: `r/w`

**说明**

是否继承父图层的提示

表示是否继承父图层的提示。也可以设置值。

为真时，如果 [Layer.hint](Layer.md#hint) 属性为空字符串，则向上
追溯父图层，直接继承并显示设置了提示的图层的
提示。Layer.hint 属性不为空字符串时则显示它。

为假时，Layer.hint 属性不为空字符串则显示它，为空字符串时
不显示提示。

---

### focusable

属性 \ 访问: `r/w`

**说明**

是否可以接收焦点

表示是否可以接收焦点。也可以设置值。

为真时图层可以接收焦点。

为假时图层不能接收焦点。

---

### prevFocusable

属性 \ 访问: `r`

**说明**

前方可接收焦点的图层

向前方搜索可接收焦点的图层。

如果没有相应的图层则为 null。

---

### nextFocusable

属性 \ 访问: `r`

**说明**

后方可接收焦点的图层

向后方搜索可接收焦点的图层。

如果没有相应的图层则为 null。

---

### joinFocusChain

属性 \ 访问: `r/w`

**说明**

是否加入焦点链

表示是否加入焦点链。

指定真时加入焦点链，会出现在 [Layer.prevFocusable](Layer.md#prevfocusable) 等中，
并可以通过 TAB 键等把焦点移动到该图层，这样
就可以做到了。

指定假时不加入焦点链，但可以通过 [Layer.focus](Layer.md#focus)
方法等接收焦点。

---

### focused

属性 \ 访问: `r`

**说明**

是否已获得焦点

表示是否已获得焦点。

为真时已获得焦点。为假时未获得焦点。

---

### enabled

属性 \ 访问: `r/w`

**说明**

是否可操作

表示图层是否可操作。也可以设置值。

为真时可操作，可以接收焦点等。

为假时不可操作，不能接收焦点等。

---

### nodeEnabled

属性 \ 访问: `r`

**说明**

图层节点是否可操作

表示图层节点是否可操作。

自身不可操作，或父图层中存在不可操作的图层时为假。

除此之外为真。

---

### attentionLeft

属性 \ 访问: `r/w`

**说明**

注视左端位置

以显示坐标中的像素为单位表示注视左端位置。也可以设置值。

**相关:** [Layer.setAttentionPos](Layer.md#setattentionpos) / [Layer.useAttention](Layer.md#useattention)

---

### attentionTop

属性 \ 访问: `r/w`

**说明**

注视上端位置

以显示坐标中的像素为单位表示注视上端位置。也可以设置值。

**相关:** [Layer.setAttentionPos](Layer.md#setattentionpos) / [Layer.useAttention](Layer.md#useattention)

---

### useAttention

属性 \ 访问: `r/w`

**说明**

是否使用注视信息

表示是否使用注视信息。也可以设置值。

指定真时，使用该图层的注视信息。

指定假时，使用该图层的父级的注视信息 (如果有的话)。

**相关:** [Layer.setAttentionPos](Layer.md#setattentionpos) / [Layer.attentionLeft](Layer.md#attentionleft) / [Layer.attentionTop](Layer.md#attentiontop)

---

### imeMode

属性 \ 访问: `r/w`

**说明**

IME 模式

表示 IME 的模式。也可以设置值。

图层被设置焦点时，IME 会切换到在这里指定的模式。

可设置的值如下。

- 指定 `**imDisable**` 时，IME 无效。无法使用 IME 输入，用户操作也无法启用 IME。

- 指定 `**imClose**` 时，IME 无效。与 imDisable 不同，可以通过用户操作启用 IME。

- 指定 `**imOpen**` 时，IME 有效。

- 指定 `**imDontCare**` 时，IME 的启用/禁用状态继承之前的状态。可以通过用户操作启用或禁用 IME。在日语输入中，这是让用户自由输入半角/全角字符时的常见模式。

- 指定 `**imSAlpha**` 时，IME 有效，并进入半角字母输入模式。

- 指定 `**imAlpha**` 时，IME 有效，并进入全角字母输入模式。

- 指定 `**imHira**` 时，IME 有效，并进入平假名输入模式。

- 指定 `**imSKata**` 时，IME 有效，并进入半角片假名输入模式。

- 指定 `**imKata**` 时，IME 有效，并进入全角片假名输入模式。

- 指定 `**imChinese**` 时，IME 有效，并进入接收 2 字节中文输入的模式。在日语环境中不可使用。

- 指定 `**imSHanguel**` 时，IME 有效，并进入接收 1 字节韩语输入的模式。在日语环境中不可使用。

- 指定 `**imHanguel**` 时，IME 有效，并进入接收 2 字节韩语输入的模式。在日语环境中不可使用。

未指定时为 imDisable。

在 Windows 上，`imDisable` 通过**输入上下文的分离**
( `ImmAssociateContext(hwnd, NULL)` ) 来实现。因此
当焦点位于 `imDisable` 的图层上时，即使按下半角/全角键，
IME 也不会打开。与 `imClose` 的区别就在这里。焦点
移动到 `imDisable` 以外的图层时会自动重新关联。

想要完全禁用 IME 控制时，使用启动参数 `-controlime=no`
(图层的 `imeMode` 将完全不生效)。

在 SDL 系的构建中，采用仅在焦点位于 `imDisable` 以外的图层上时
启用 OS 文本输入的方式实现相同含义。

**相关:** [Window.imeMode](Window.md#imemode)

---

### callOnPaint

属性 \ 访问: `r/w`

**说明**

是否调用 onPaint 事件

表示是否调用 [Layer.onPaint](Layer.md#onpaint) 事件。也可以设置值。

指定真时，会在下一次向画面绘制之前调用 onPaint 事件。onPaint 事件
处理完成后，该属性会自动恢复为假。

指定假的状态下不会发生 onPaint 事件。

[Layer.update](Layer.md#update) 方法会将该属性设为真。

---

### font

属性 \ 访问: `r`

**说明**

字体

[Layer.drawText](Layer.md#drawtext) 方法绘制时使用的字体所对应的 [Font](Font.md) 类的
对象。

---

### name

属性 \ 访问: `r/w`

**说明**

图层名

表示图层名。也可以设置值。

通过该属性设置的内容不会影响 Layer 类的运行。

---

### mainImageBuffer

属性 \ 访问: `r`

**说明**

主图像缓冲区指针

表示指向主图像 (包含颜色与遮罩(不透明度)信息的 32bpp 位图) 的图像缓冲区左上角的
指针。

该属性是为了给插件等提供直接访问图像缓冲区的手段
而准备的。

虽然以整数类型返回，但在插件等中请强制转换为适当的类型 (const unsigned long * 等) 后
使用。

请不要向通过该属性获得的指针写入值。
通过 [Layer.mainImageBufferForWrite](Layer.md#mainimagebufferforwrite) 获得的指针则可以写入。

图层未分配图像时返回 NULL (0)。

图像的大小由 [Layer.imageWidth](Layer.md#imagewidth) 与 [Layer.imageHeight](Layer.md#imageheight) 属性
表示。

指针的计算方法请参阅 [Layer.mainImageBufferPitch](Layer.md#mainimagebufferpitch)。

**相关:** [Layer.mainImageBufferForWrite](Layer.md#mainimagebufferforwrite) / [Layer.mainImageBufferPitch](Layer.md#mainimagebufferpitch)

---

### mainImageBufferForWrite

属性 \ 访问: `r`

**说明**

主图像缓冲区指针 (写入用)

表示指向主图像 (包含颜色与遮罩(不透明度)信息的 32bpp 位图) 的图像缓冲区左上角的
指针。

该属性是为了给插件等提供直接访问图像缓冲区的手段
而准备的。

虽然以整数类型返回，但在插件等中请强制转换为适当的类型 (unsigned long * 等) 后
使用。

与 [Layer.mainImageBuffer](Layer.md#mainimagebuffer) 不同，可以向通过该属性获得的指针
写入值。在吉里吉里内部，完全相同的图像会在多个图层之间等共享，但
引用该属性会解除该共享状态。

图层未分配图像时返回 NULL (0)。

图像的大小由 [Layer.imageWidth](Layer.md#imagewidth) 与 [Layer.imageHeight](Layer.md#imageheight) 属性
表示。

指针的计算方法请参阅 [Layer.mainImageBufferPitch](Layer.md#mainimagebufferpitch)。

**相关:** [Layer.mainImageBuffer](Layer.md#mainimagebuffer) / [Layer.mainImageBufferPitch](Layer.md#mainimagebufferpitch)

---

### mainImageBufferPitch

属性 \ 访问: `r`

**说明**

主图像缓冲区跨距

表示主图像 (包含颜色与遮罩(不透明度)信息的 32bpp 位图) 的图像缓冲区的跨距
(到下一条扫描线的字节数)。

该属性是为了给插件等提供直接访问图像缓冲区的手段
而准备的。

将 tjs_uint32 视为 32bit 的整数类型、tjs_uint8 视为 8bit (1byte) 的整数类型，指向图像位置 (x, y) 的
指针用 C 语言编写时可以如下计算。

`( (tjs_uint32*)( (tjs_uint8*)mainImageBuffer + y*mainImageBufferPitch )) + x`

请注意，该属性返回的不是到下一条扫描线的像素数，而是字节数。该数值有时会比图像宽度
刚好需要的字节数稍大一些。

请注意，该属性的值可能为负。

**相关:** [Layer.mainImageBuffer](Layer.md#mainimagebuffer) / [Layer.mainImageBufferForWrite](Layer.md#mainimagebufferforwrite)

---

### provinceImageBuffer

属性 \ 访问: `r`

**说明**

区域图像缓冲区指针

表示指向区域图像 (包含区域信息的 8bpp 位图) 的图像缓冲区左上角的
指针。

该属性是为了给插件等提供直接访问图像缓冲区的手段
而准备的。

虽然以整数类型返回，但在插件等中请强制转换为适当的类型 (const unsigned char * 等) 后
使用。

请不要向通过该属性获得的指针写入值。
通过 [Layer.provinceImageBufferForWrite](Layer.md#provinceimagebufferforwrite) 获得的指针则可以写入。

图像未分配时返回 NULL (0)。图像未分配时
必须将整个区域视为区域编号 0。

图像的大小由 [Layer.imageWidth](Layer.md#imagewidth) 与 [Layer.imageHeight](Layer.md#imageheight) 属性
表示。

指针的计算方法请参阅 [Layer.provinceImageBufferPitch](Layer.md#provinceimagebufferpitch)。

**相关:** [Layer.provinceImageBufferForWrite](Layer.md#provinceimagebufferforwrite) / [Layer.provinceImageBufferPitch](Layer.md#provinceimagebufferpitch)

---

### provinceImageBufferForWrite

属性 \ 访问: `r`

**说明**

区域图像缓冲区指针(写入用)

表示指向区域图像 (包含区域信息的 8bpp 位图) 的图像缓冲区左上角的
指针。

该属性是为了给插件等提供直接访问图像缓冲区的手段
而准备的。

虽然以整数类型返回，但在插件等中请强制转换为适当的类型 (unsigned char * 等) 后
使用。

与 [Layer.provinceImageBuffer](Layer.md#provinceimagebuffer) 不同，可以向通过该属性获得的指针
写入值。在吉里吉里内部，完全相同的图像会在多个图层之间等共享，但
引用该属性会解除该共享状态。

图层未分配图像时，会在引用该属性的时点自动
分配，并将整个区域初始化为区域编号 0。

图像的大小由 [Layer.imageWidth](Layer.md#imagewidth) 与 [Layer.imageHeight](Layer.md#imageheight) 属性
表示。

指针的计算方法请参阅 [Layer.provinceImageBufferPitch](Layer.md#provinceimagebufferpitch)。

**相关:** [Layer.provinceImageBuffer](Layer.md#provinceimagebuffer) / [Layer.provinceImageBufferPitch](Layer.md#provinceimagebufferpitch)

---

### provinceImageBufferPitch

属性 \ 访问: `r`

**说明**

区域图像缓冲区跨距

表示区域图像 (包含区域信息的 8bpp 位图) 的图像缓冲区的跨距
(到下一条扫描线的字节数)。

该属性是为了给插件等提供直接访问图像缓冲区的手段
而准备的。

将 tjs_uint8 视为 8bit (1byte) 的整数类型，指向图像位置 (x, y) 的
指针用 C 语言编写时可以如下计算。

`(tjs_uint8*)provinceImageBuffer + y*provinceImageBufferPitch + x`

该属性的数值有时会比图像宽度刚好需要的字节数稍大一些。

请注意，该属性的值可能为负。

**相关:** [Layer.provinceImageBuffer](Layer.md#provinceimagebuffer) / [Layer.provinceImageBufferForWrite](Layer.md#provinceimagebufferforwrite)

---

### ignoreHintSensing

属性 \ 访问: `r/w`

**说明**

提示显示判定的有无

表示提示显示判定的有无。

设置 true 时，该图层不进行提示判定。

设置 false 时进行判定。

**相关:** [Window.onHintChanged](Window.md#onhintchanged)

---

### nodeFocusable

属性 \ 访问: `r/w`

**说明**

节点单位的焦点可否

返回该图层节点是否可以持有焦点。
反映考虑了父层级所包含的 `focusable` 的结果。只读。

**相关:** [Layer.focusable](Layer.md#focusable)

---

### moveBefore

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 移动到在这里指定的图层的前面。<br>只能指定兄弟图层 (持有相同父级的图层)。 |

**说明**

移动到指定图层的前面

在重叠顺序中，移动到指定图层的前面。

该方法会把 [Layer.absoluteOrderMode](Layer.md#absoluteordermode) 属性设为 false。

---

### moveBehind

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 移动到在这里指定的图层的后面。<br>只能指定兄弟图层 (持有相同父级的图层)。 |

**说明**

移动到指定图层的后面

在重叠顺序中，移动到指定图层的后面。

该方法会把 [Layer.absoluteOrderMode](Layer.md#absoluteordermode) 属性设为 false。

---

### bringToBack

方法

**说明**

移到最后面

在重叠顺序中，移动到兄弟图层 (持有相同父级的图层) 中最靠后的位置。

执行该方法后，父图层的 [Layer.absoluteOrderMode](Layer.md#absoluteordermode) 属性会被设为假。

**相关:** [Layer.order](Layer.md#order) / [Layer.absolute](Layer.md#absolute) / [Layer.absoluteOrderMode](Layer.md#absoluteordermode) / [Layer.bringToFront](Layer.md#bringtofront)

---

### bringToFront

方法

**说明**

移到最前面

在重叠顺序中，移动到兄弟图层 (持有相同父级的图层) 中最靠前的位置。

执行该方法后，父图层的 [Layer.absoluteOrderMode](Layer.md#absoluteordermode) 属性会被设为假。

**相关:** [Layer.order](Layer.md#order) / [Layer.absolute](Layer.md#absolute) / [Layer.absoluteOrderMode](Layer.md#absoluteordermode) / [Layer.bringToBack](Layer.md#bringtoback)

---

### loadImages

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `image` | `&nbsp;` | 指定要加载的图像存储。<br>在这里指定的存储名(去除扩展名) 后加上 _m 的图像存储如果<br>存在，则作为遮罩(不透明度)图像加载。<br>在这里指定的存储名(去除扩展名) 后加上 _p 的图像存储如果<br>存在，则作为区域图像加载。 |
| `colorkey` | `clNone` | 指定要加载的图像的颜色键 (透明色)。<br>以 0xRRGGBB 形式指定颜色时，该颜色将作为颜色键。<br>指定 `**clPalIdx**` 加上任意调色板索引后的数值时，<br>该调色板索引将成为透明色 (256 色以下图像的情况)。<br>指定 `**clAdapt**` 时，图像最上面一行中<br>使用最多的颜色会自动成为透明色。<br>指定 `**clAlphaMat**` 加上 0xRRGGBB<br>形式的颜色数值后的值时，图像会在该颜色之上<br>用 α 混合(ltAlpha 的方式)进行叠加。<br>例如，指定 (clAlphaMat + 0xffffff) 时，<br>加载的图像会叠加到白色之上。<br>图像将全部变为不透明的图像<br>( 图像将全部变为不透明，但<br>在该模式下标签信息完全不会被更改，<br>请注意 )。 |

**返回值**

标签信息的字典数组

**说明**

图像的加载

向图层加载图像。

该方法会更改图层的图像尺寸，但除了图像尺寸比图层的显示尺寸小的情况
之外，不会更改图层的显示尺寸。

作为返回值，返回标签信息(该图像的图层类型和显示位置等、针对图像本身的信息)的字典数组。

图像不持有标签信息时返回 null。

在当前版本中，只有 PNG、TLG5/6 格式可以持有标签信息。关于可以获取的信息，请参阅 [图像格式转换器](../guide/TPC.md)。

---

### loadProvinceImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `image` | `&nbsp;` | 指定作为区域图像加载的图像存储。 |

**说明**

区域图像的加载

加载图层的区域图像。其他图像保持不变。

尝试加载的图像与图层的图像尺寸不同时会抛出异常。

---

### getMainPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定要获取颜色的 (图层图像坐标中的) x 坐标。 |
| `y` | `&nbsp;` | 指定要获取颜色的 (图层图像坐标中的) y 坐标。 |

**返回值**

0xRRGGBB 形式的颜色编号

**说明**

主图像的颜色的获取

获取图层主图像 (持有颜色的图像) 任意位置的颜色。

指定图像坐标中无效 (范围外) 的位置时会抛出异常。

---

### setMainPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定要设置颜色的 (图层图像坐标中的) x 坐标。 |
| `y` | `&nbsp;` | 指定要设置颜色的 (图层图像坐标中的) y 坐标。 |
| `color` | `&nbsp;` | 以 0xRRGGBB 形式指定要设置的颜色。 |

**说明**

主图像的颜色的设置

设置图层主图像 (持有颜色的图像) 任意位置的颜色。

指定图像坐标中无效 (范围外) 的位置时会抛出异常。

---

### getMaskPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定要获取值的 (图层图像坐标中的) x 坐标。 |
| `y` | `&nbsp;` | 指定要获取值的 (图层图像坐标中的) y 坐标。 |

**返回值**

遮罩图像的值 (0 ~ 255)

**说明**

遮罩图像的值的获取

获取图层遮罩图像 (持有不透明度的图像) 任意位置的值 (0 ~ 255)。

指定图像坐标中无效 (范围外) 的位置时会抛出异常。

---

### setMaskPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定要设置值的 (图层图像坐标中的) x 坐标。 |
| `y` | `&nbsp;` | 指定要设置值的 (图层图像坐标中的) y 坐标。 |
| `value` | `&nbsp;` | 指定要设置的值 (0 ~ 255)。 |

**说明**

遮罩图像的值的设置

设置图层遮罩图像 (持有不透明度的图像) 任意位置的值 (0 ~ 255)。

指定图像坐标中无效 (范围外) 的位置时会抛出异常。

---

### getProvincePixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定要获取值的 (图层图像坐标中的) x 坐标。 |
| `y` | `&nbsp;` | 指定要获取值的 (图层图像坐标中的) y 坐标。 |

**返回值**

区域图像的值 (0 ~ 255)

**说明**

区域图像的值的获取

获取图层区域图像任意位置的值 (0 ~ 255)。

指定图像坐标中无效 (范围外) 的位置时会抛出异常。

---

### setProvincePixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定要设置值的 (图层图像坐标中的) x 坐标。 |
| `y` | `&nbsp;` | 指定要设置值的 (图层图像坐标中的) y 坐标。 |
| `value` | `&nbsp;` | 指定要设置的值 (0 ~ 255)。 |

**说明**

区域图像的值的设置

设置图层区域图像任意位置的值 (0 ~ 255)。

指定图像坐标中无效 (范围外) 的位置时会抛出异常。

---

### getLayerAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以显示坐标上的像素为单位指定要获取的图层位置的 x 坐标。<br>使用执行该方法的图层的显示坐标 (不是主图层上的<br>显示坐标) |
| `y` | `&nbsp;` | 以显示坐标上的像素为单位指定要获取的图层位置的 y 坐标。<br>使用执行该方法的图层的显示坐标 (不是主图层上的<br>显示坐标) |
| `exclude_self` | `false` | 指定是否从图层搜索中排除自己自身。<br>指定假时，自己自身的图层也包含在搜索中。<br>指定真时，自己自身的图层会从搜索中排除，被当作仿佛不存在一样处理。<br>省略该参数时视为指定了假。 |
| `get_disabled` | `false` | 指定是否获取已禁用的图层的对象。<br>指定假时，如果指定位置存在已禁用 ([Layer.enabled](Layer.md#enabled) 属性为假等) 的图层，则返回 null。<br>指定真时，如果指定位置存在已禁用的图层，则返回该图层对象。<br>省略该参数时视为指定了假。 |

**返回值**

位于指定位置的图层对象。指定位置没有图层等情况时返回 null。

**说明**

获取指定位置的图层

返回位于 x,y 所示位置的图层对象。

命中判定使用与通常的鼠标事件命中判定相同的机制。也就是说，从图层重叠顺序中最靠前的位置开始查看指定位置，返回第一个符合命中判定的图层。

通过 exclude_self 参数指定真，可以将执行该方法的图层从搜索对象中排除。

**相关:** [Layer.hitType](Layer.md#hittype) / [Layer.hitThreshold](Layer.md#hitthreshold) / [Layer.onHitTest](Layer.md#onhittest)

---

### releaseCapture

方法

**说明**

鼠标事件捕获的解除

解除鼠标事件捕获。

鼠标事件捕获是指，只向最初按下鼠标按钮时所在的图层，在放开鼠标按钮之前一直独占性地发送鼠标事件的功能。

该方法解除该功能，恢复到通常的鼠标事件处理状态。

执行该方法后，属于同一窗口的图层的鼠标捕获会被解除，即使执行方法的图层与成为捕获对象的图层不同也是如此。

该方法在不是捕获状态时不做任何事。

---

### setPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 以像素为单位指定图层的 (父图层的显示坐标中的) 左端位置。<br>该值也可以通过 [Layer.left](Layer.md#left) 属性获取和设置。 |
| `top` | `&nbsp;` | 以像素为单位指定图层的 (父图层的显示坐标中的) 上端位置。<br>该值也可以通过 [Layer.top](Layer.md#top) 属性获取和设置。 |
| `width` | `void` | 以像素为单位指定图层的宽度。<br>该值也可以通过 [Layer.width](Layer.md#width) 属性获取和设置。<br>省略该参数与 height 参数时，只进行基于 left 参数与 top 参数的位置更改。 |
| `height` | `void` | 以像素为单位指定图层的高度。<br>该值也可以通过 [Layer.height](Layer.md#height) 属性获取和设置。<br>省略该参数与 width 参数时，只进行基于 left 参数与 top 参数的<br>位置更改。 |

**说明**

图层显示位置的设置

设置图层的显示位置。

---

### setClip

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 以像素为单位指定绘制裁剪矩形的 (图层图像坐标中的) 左端位置。<br>该值也可以通过 [Layer.clipLeft](Layer.md#clipleft) 属性获取和设置。 |
| `top` | `&nbsp;` | 以像素为单位指定绘制裁剪矩形的 (图层图像坐标中的) 上端位置。<br>该值也可以通过 [Layer.clipTop](Layer.md#cliptop) 属性获取和设置。 |
| `width` | `void` | 以像素为单位指定绘制裁剪矩形的宽度。<br>该值也可以通过 [Layer.clipWidth](Layer.md#clipwidth) 属性获取和设置。 |
| `height` | `void` | 以像素为单位指定绘制裁剪矩形的高度。<br>该值也可以通过 [Layer.clipHeight](Layer.md#clipheight) 属性获取和设置。 |

**说明**

绘制裁剪矩形的设置

设置图层的**绘制裁剪矩形**。

对图层的绘制会被限制在该绘制裁剪矩形内 (超出矩形的部分
不会被绘制)。不过，也有像 [Layer.flipLR](Layer.md#fliplr) 和 [Layer.flipUD](Layer.md#flipud) 这样
不受绘制裁剪矩形影响的方法。

初始值方面，裁剪矩形被设置为整个图层图像区域 (可以在图层整个面
上绘制)。

绘制裁剪矩形会在加载图像、图像尺寸被更改、或图层的显示类型
被更改时恢复到初始值。

另外，不带参数调用该方法可以将绘制裁剪矩形恢复为初始值。

---

### setSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 以像素为单位指定图层的显示宽度。<br>该值也可以通过 [Layer.width](Layer.md#width) 属性获取和设置。 |
| `height` | `&nbsp;` | 以像素为单位指定图层的显示高度。<br>该值也可以通过 [Layer.height](Layer.md#height) 属性获取和设置。 |

**说明**

图层显示尺寸的设置

设置图层的显示尺寸。

---

### setSizeToImageSize

方法

**说明**

让图层显示尺寸与图像尺寸一致

将图层的显示尺寸设置为与图像尺寸相同。

许多更改图像尺寸的操作不会更改显示尺寸，但
使用该方法可以让显示尺寸与图像尺寸相同。

---

### setImagePos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 以像素为单位指定图层上要显示的图像的左端位置 (x 偏移)。<br>该值也可以通过 [Layer.imageLeft](Layer.md#imageleft) 属性获取和设置。 |
| `top` | `&nbsp;` | 以像素为单位指定图层上要显示的图像的上端位置 (y 偏移)。<br>该值也可以通过 [Layer.imageTop](Layer.md#imagetop) 属性获取和设置。 |

**说明**

图层图像偏移的设置

指定图层图像偏移。

图层图像尺寸可以大于图层显示尺寸，但无法显示全部，
因此需要通过该方法、[Layer.imageLeft](Layer.md#imageleft) 或 [Layer.imageTop](Layer.md#imagetop)
属性来指定显示偏移。

偏移为 0 或负数值。

---

### setImageSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 以像素为单位指定图层图像的宽度。<br>该值也可以通过 [Layer.imageWidth](Layer.md#imagewidth) 属性获取和设置。 |
| `height` | `&nbsp;` | 以像素为单位指定图层图像的高度。<br>该值也可以通过 [Layer.imageHeight](Layer.md#imageheight) 属性获取和设置。 |

**说明**

图层图像尺寸的设置

指定图层图像尺寸。

尺寸被扩展时，图层的显示尺寸不会更改，但尺寸被
缩小时，图层的显示尺寸也会缩小。

---

### independMainImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `copy` | `true` | 指定解除共享状态时是否复制原来的图像。<br>指定真时复制原来的图像。指定假时不会复制原来的图像，图像的<br>内容将变为未定义。 |

**说明**

解除主图像的共享

强制解除图层图像的共享状态。

吉里吉里在用 assignImages 等把图像整个复制到其他图层时，实际上
不会进行图像缓冲区的复制，而是共享同一图像。

通常，在即将对图像进行更改之前，这个共享状态会被自动解除，
但用该方法可以强制解除。

给 copy 参数指定 false 时，图像的共享会被解除，但不保证
继承原来的图像 (图像内容将变为未定义)，不过可以
更高速地进行共享的解除。如果要改写图层的全部图像，
就不需要继承原来的图像，因此在绘制之前预先给该方法指定 false
调用，有时会提高效率。

该方法在图像未被共享时不做任何事。

---

### independProvinceImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `copy` | `true` | 指定解除共享状态时是否复制原来的图像。<br>指定真时复制原来的图像。指定假时不会复制原来的图像，图像的<br>内容将变为未定义。 |

**说明**

解除区域图像的共享

强制解除区域图像的共享状态。

吉里吉里在用 assignImages 等把图像整个复制到其他图层时，实际上
不会进行图像缓冲区的复制，而是共享同一图像。

通常，在即将对图像进行更改之前，这个共享状态会被自动解除，
但用该方法可以强制解除。

给 copy 参数指定 false 时，图像的共享会被解除，但不保证
继承原来的图像 (图像内容将变为未定义)，不过可以
更高速地进行共享的解除。如果要改写图层的全部图像，
就不需要继承原来的图像，因此在绘制之前预先给该方法指定 false
调用，有时会提高效率。

该方法在图像未被共享时不做任何事。

---

### fillRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的左端位置。 |
| `top` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的上端位置。 |
| `width` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的宽度。 |
| `height` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的高度。 |
| `value` | `&nbsp;` | 指定要填充的颜色或值。<br>该值根据 [Layer.face](Layer.md#face) 属性的值而含义不同。<br>`**dfAlpha** (或**dfBoth**)  ` : 请以 0xAARRGGBB 形式指定不透明度与颜色。主图像与遮罩双方都会被填充。<br>`**dfAddAlpha**              ` : 请以 0xAARRGGBB 形式指定不透明度与颜色。主图像与遮罩双方都会被填充。<br>`**dfOpaque** (或**dfMain**) ` : 请以 0xRRGGBB 形式指定颜色。[Layer.holdAlpha](Layer.md#holdalpha) 属性为真时，仅主图像被填充，遮罩保持不变。为假时与 dfAlpha 和 dfAddAlpha 时相同，接受 0xAARRGGBB 形式的不透明度与颜色指定，主图像与遮罩双方都会被填充。<br>`**dfMask**                  ` : 请指定遮罩(不透明度)的值 (0 ~ 255)。仅遮罩被填充，主图像保持不变。<br>`**dfProvince**              ` : 请指定区域的值 (0 ~ 255)。仅区域被填充。 |

**说明**

矩形填充

以指定的方法填充指定的图层图像的矩形。

---

### colorRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的左端位置。 |
| `top` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的上端位置。 |
| `width` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的宽度。 |
| `height` | `&nbsp;` | 以 (图像位置中的) 像素为单位指定要填充的矩形的高度。 |
| `value` | `&nbsp;` | 指定要填充的颜色或值。<br>该值根据 [Layer.face](Layer.md#face) 属性的值而含义不同。<br>`**dfAlpha** (或**dfBoth**)   ` : 请以 0xRRGGBB 形式指定颜色<br>`**dfAddAlpha**                   ` : 请以 0xRRGGBB 形式指定颜色<br>`**dfOpaque** (或**dfMain**)  ` : 请以 0xRRGGBB 形式指定颜色<br>`**dfMask**                       ` : 请指定遮罩(不透明度)的值 (0 ~ 255)<br>`**dfProvince**                   ` : 请指定区域的值 (0 ~ 255)<br>指定 dfOpaque 时，遮罩信息会被忽略(遮罩信息是被保持还是被破坏取决于 [Layer.holdAlpha](Layer.md#holdalpha) 属性)。另外，指定 dfMask 时，颜色信息保持不变。<br>在 dfAlpha 的情况下且 opa 为负时，该参数被忽略。 |
| `opa` | `255` | 指定要填充的不透明度 (-255 ~ 0 ~ 255)。<br>当 [Layer.face](Layer.md#face) 属性的值为 dfMask 或<br>dfProvince 时，该参数被忽略 (始终完全不透明)。<br>指定负数仅在 [Layer.face](Layer.md#face) 为 dfAlpha 时有效，<br>这种情况下 value 参数被忽略，图像的不透明度会被去除 (<br>指定 -255 时矩形变为完全透明)。 |

**说明**

矩形半透明填充

以指定的方法填充指定的图层图像的矩形。

与 [Layer.fillRect](Layer.md#fillrect) 不同，可以指定透明度进行半透明填充。

---

### drawText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定开始绘制文字的 (图像位置中的) 原点的 x 坐标。 |
| `y` | `&nbsp;` | 以像素为单位指定开始绘制文字的 (图像位置中的) 原点的 y 坐标。 |
| `text` | `&nbsp;` | 指定要绘制的文字。 |
| `color` | `&nbsp;` | 以 0xRRGGBB 形式 (24bit) 指定要绘制的文字颜色。<br>**注意:** 请将高位 8bit (Alpha) 设为 0。指定高位 8bit 不为 0 的<br>值 (例: 本意是白色而写 0xFFFFFFFF) 时，该值会被解释为“系统颜色<br>编号” (内部经由 `TVPToActualColor`)，变成并非本意的颜色<br>(多数情况下几乎为黑)。不透明度请勿通过 color 而通过 opa 参数<br>指定。<br>( [Layer.fillRect](Layer.md#fillrect) / [Layer.colorRect](Layer.md#colorrect) /<br>[Layer.operateRect](Layer.md#operaterect) 等方法的颜色为 0xAARRGGBB 形式、<br>包含 Alpha，而 drawText / drawGlyph 等字体绘制类的 color 为<br>24bit RGB，这一点不同。) |
| `opa` | `255` | 指定要绘制的文字的不透明度 (-255 ~ 0 ~ 255)。<br>指定负数仅在 [Layer.face](Layer.md#face) 为 dfAlpha 时有效，<br>这种情况下文字形状中的不透明度会被去除 (值越小<br>效果越大)。 |
| `aa` | `true` | 指定是否进行抗锯齿。<br>指定真时进行抗锯齿。指定假时不进行。 |
| `shadowlevel` | `0` | 指定阴影的不透明度。合适的值会根据 shadowwidth 参数的值变化。<br>指定 0 时不绘制阴影。 |
| `shadowcolor` | `0x000000` | 以 0xRRGGBB 形式指定阴影的颜色。 |
| `shadowwidth` | `0` | 指定阴影的宽度 (模糊)。 0 最锐利 (不模糊)，增大<br>值可以使阴影模糊。 |
| `shadowofsx` | `0` | 以像素为单位指定阴影位置的 x 坐标值。 指定 0 时阴影绘制在正下方。 |
| `shadowofsy` | `0` | 以像素为单位指定阴影位置的 y 坐标值。 指定 0 时阴影绘制在正下方。 |

**说明**

文字绘制

向图层绘制文字。仅在 [Layer.face](Layer.md#face) 为 dfAlpha (或 dfBoth)、dfAddAlpha、dfOpaque (或 dfMain)
的情况下可以绘制。

指定 dfOpaque (或 dfMain) 时，绘制目标的遮罩是被破坏还是被保护取决于 [Layer.holdAlpha](Layer.md#holdalpha) 属性。

字体使用由 [Layer.font](Layer.md#font) 指定的字体。

---

### drawGlyph

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定开始绘制文字的 (图像位置中的) 原点的 x 坐标。 |
| `y` | `&nbsp;` | 以像素为单位指定开始绘制文字的 (图像位置中的) 原点的 y 坐标。 |
| `glyph` | `&nbsp;` | 指定要绘制的字形。 |
| `color` | `&nbsp;` | 以 0xRRGGBB 形式 (24bit) 指定要绘制的文字颜色。<br>**注意:** 与 [Layer.drawText](Layer.md#drawtext) 的 color 相同，请将高位 8bit 设为<br>0 (传入 0xFFFFFFFF 等会被当作系统颜色，变成并非本意的<br>颜色)。不透明度通过 opa 参数指定。 |
| `opa` | `255` | 指定要绘制的文字的不透明度 (-255 ~ 0 ~ 255)。<br>指定负数仅在 face 为 dfAlpha 时有效，<br>这种情况下文字形状中的不透明度会被去除 (值越小<br>效果越大)。 |
| `aa` | `true` | 指定是否进行抗锯齿。<br>指定真时进行抗锯齿。指定假时不进行。 |
| `shadowlevel` | `0` | 指定阴影的不透明度。合适的值会根据 shadowwidth 参数的值变化。<br>指定 0 时不绘制阴影。 |
| `shadowcolor` | `0x000000` | 以 0xRRGGBB 形式指定阴影的颜色。 |
| `shadowwidth` | `0` | 指定阴影的宽度 (模糊)。 0 最锐利 (不模糊)，增大<br>值可以使阴影模糊。 |
| `shadowofsx` | `0` | 以像素为单位指定阴影位置的 x 坐标值。 指定 0 时阴影绘制在正下方。 |
| `shadowofsy` | `0` | 以像素为单位指定阴影位置的 y 坐标值。 指定 0 时阴影绘制在正下方。 |

**说明**

文字绘制

向图层绘制字形。

字形请指定 glyph : Array[9] = [ width, height, originx, originy, incx, incy, inc, bitmap(Octet), colors ] 这样的形式的数组。

省略字形的 colors 时，会被判断为 256 阶调。

---

### drawShapedText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定要绘制的基线原点的 x 坐标。 |
| `y` | `&nbsp;` | 以像素为单位指定要绘制的基线原点的 y 坐标。 |
| `text` | `&nbsp;` | 指定要绘制的字符串。 |
| `color` | `&nbsp;` | 以 0xAARRGGBB 形式指定要绘制的文字颜色 (省略高位 8bit 的 α = 不透明)。 |
| `font` | `void` | 汇总指定绘制属性。为以下之一。<br>+ [Font](Font.md) 对象 … 使用 face (字体指定)、height (大小 px)、<br>bold、italic、underline、strikeout、angle (1/10 度单位、逆时针。彩色 emoji<br>不支持转换，因此保持直立)<br>+ 字符串 … 仅替换自图层的 font 的 face 后使用<br>+ void (省略) … 直接使用自图层的 [Layer.font](Layer.md#font)<br>face (字体指定) 是 data/fonts.json 中声明的字体名、存储路径、<br>( WINVER 的 ) 已安装系统字体名中的任意一种，用逗号分隔指定多个时<br>会成为回退链 (每个码点使用最先收录的 face。例:<br>"メイリオ,Segoe UI Emoji" )。 |
| `base` | `0` | 指定基本方向。0 = 自动判定 / 1 = 左横排 (LTR) / 2 = 右横排 (RTL)。 |
| `count` | `-1` | 指定 0 以上时，按逻辑顺序 (读取顺序) 仅绘制开头 count 个“字符”<br>( 用于打字机显示 )。“字符”是绘制时作为一块处理的簇单位，<br>与 [Layer.shapedTextCount](Layer.md#shapedtextcount) 的计数方式相同 (连字、组合字符、<br>emoji ZWJ 序列算作 1)。因为先对全文进行整形，再只绘制开头部分，<br>所以显示过程中阿拉伯语的上下文字形等也不会变化。省略时 (-1) 绘制整体。 |

**返回值**

返回已绘制部分的前进宽度 (像素)。失败时返回 -1。

**说明**

文字绘制 (整形 / 统一字体引擎)

使用统一字体引擎 glyphware (FreeType + HarfBuzz)，在主图像的
基线原点 (x, y) 绘制文本。[Layer.drawText](Layer.md#drawtext)
是独立的绘制路径，支持 **BiDi (双向文本)、复杂脚本的整形、
字体回退** (阿拉伯语、希伯来语等)。返回值是
已绘制部分的前进宽度 (像素)。

**注意:** 这是用于阶段性迁移的、与现有 drawText 并存的新路径。想将现有 drawText 的
行为 (1 码点单位的 cell-stepping) 切换为 glyphware 时，
使用 [Font.rasterizer](Font.md#rasterizer) (它不进行整形)。

---

### drawShapedTextArea

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定矩形的左端。 |
| `y` | `&nbsp;` | 以像素为单位指定矩形的上端。 |
| `width` | `&nbsp;` | 以像素为单位指定矩形的宽度。 |
| `height` | `&nbsp;` | 以像素为单位指定矩形的高度。 |
| `text` | `&nbsp;` | 指定要绘制的字符串。 |
| `color` | `&nbsp;` | 以 0xAARRGGBB 形式指定要绘制的文字颜色 (省略高位 8bit 的 α = 不透明)。 |
| `font` | `void` | 汇总指定绘制属性 (与 [Layer.drawShapedText](Layer.md#drawshapedtext) 相同)。 |
| `base` | `0` | 指定基本方向 (0 = 自动 / 1 = LTR / 2 = RTL)。 |
| `count` | `-1` | 指定 0 以上时，在整体中仅绘制开头 count 个“字符”(簇)<br>( 用于打字机显示 )。因为折行位置先由全文确定再绘制，<br>所以显示过程中不会发生行的重组 (重排)。省略时 (-1) 绘制整体。 |
| `lineSpacing` | `0` | 指定行间追加的像素数 (可为负值)。 |
| `align` | `0` | 指定行对齐。0 = 左对齐 / 1 = 居中 / 2 = 右对齐。 |

**返回值**

返回绘制结果的 Dictionary (失败时为 void):
%[ "height" => 消耗的高度 (px), "lines" => 绘制的行数,
"count" => 实际绘制的簇数 ]

**说明**

矩形内文字绘制 (整形 / 简易折行)

使用统一字体引擎 glyphware，在矩形 (x, y, width, height) 的内侧
带简易折行地绘制文本。\n (\r\n / \r) 被作为显式换行处理，
以空白分隔的语言 (英语等) 按词单位、日语等 CJK 按字符单位
折行 (附带行首、行末的简易避头尾处理)。超过矩形下端的行不会被绘制，
绘制会被裁剪到矩形内。font 的 angle 被忽略。

---

### measureShapedText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要测量的字符串。 |
| `font` | `void` | 汇总指定绘制属性 (与 [Layer.drawShapedText](Layer.md#drawshapedtext) 相同)。 |
| `base` | `0` | 指定基本方向 (0 = 自动 / 1 = LTR / 2 = RTL)。 |

**返回值**

返回测量结果的 Dictionary (失败时为 void)。全部为以基线原点 (0,0)
为基准的像素值:
%[ "width" => 前进宽度, "left" => 墨水左, "top" => 墨水上 (负 = 基线之上),
"right" => 墨水右, "bottom" => 墨水 下, "ascent" => ascent, "descent" => descent,
"count" => 绘制簇数 (与 [Layer.shapedTextCount](Layer.md#shapedtextcount) 相同) ]

**说明**

字符串测量 (整形 / 统一字体引擎)

使用统一字体引擎 glyphware 测量文本，并以 Dictionary 返回结果。
不进行绘制。用与 [Layer.drawShapedText](Layer.md#drawshapedtext)
相同的字体指定、整形进行测量。

---

### shapedTextCount

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要计数的字符串。 |
| `font` | `void` | 汇总指定绘制属性 (与 [Layer.drawShapedText](Layer.md#drawshapedtext) 相同。<br>簇数有时会因字体是否有连字等而变化)。 |
| `base` | `0` | 指定基本方向 (0 = 自动 / 1 = LTR / 2 = RTL)。 |

**返回值**

返回簇数。失败时返回 -1。

**说明**

绘制字符数 (簇数) 的获取

返回文本的“绘制时作为一块处理的字符数 (簇数)”。
与 [Layer.drawShapedText](Layer.md#drawshapedtext) /
[Layer.drawShapedTextArea](Layer.md#drawshapedtextarea) 的 count 参数所限制的
单位相同。连字、基底字符 + 组合字符、emoji ZWJ 序列各自
被计数为 1，因此有时与码点数 (字符串的 length) 不一致。
换行字符会分割行，其自身不被计数。

---

### drawVerticalTextArea

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定矩形的左端。 |
| `y` | `&nbsp;` | 以像素为单位指定矩形的上端。 |
| `width` | `&nbsp;` | 以像素为单位指定矩形的宽度 (列排列方向的长度)。 |
| `height` | `&nbsp;` | 以像素为单位指定矩形的高度 (1 列的长度)。 |
| `text` | `&nbsp;` | 指定要绘制的字符串。 |
| `color` | `&nbsp;` | 以 0xAARRGGBB 形式指定要绘制的文字颜色 (省略高位 8bit 的 α = 不透明)。 |
| `font` | `void` | 汇总指定绘制属性 (与 [Layer.drawShapedText](Layer.md#drawshapedtext) 相同)。 |
| `count` | `-1` | 指定 0 以上时，在整体中仅绘制开头 count 个“字符”(簇)<br>( 用于打字机显示 )。因为行的分割先由全文确定再施加限制，<br>所以显示过程中不会发生列的重组 (重排)。西文的单词间空白在这里<br>不计入 (计数的单位是实际被绘制的字符本身)。省略时 (-1) 绘制整体。 |
| `lineSpacing` | `0` | 指定列间 (行间) 追加的像素数 (可为负值)。 |
| `options` | `void` | 用 Dictionary 指定排版选项 (可省略)。未指定的<br>键保持默认值:<br>+ "orientation" => 直立 / 横倒的指定。0 = 日文直立、西文横倒 (默认) /<br>1 = 全部直立 / 2 = 全部横倒<br>+ "verticalLr" => 为真时列从左向右推进 (默认为假 = 从右到左)<br>+ "punctuation" => 进行标点符号的收紧 (JLReq 间隙量表) (默认为真。为假则密排)<br>+ "latinGap" => 在日文与西文之间加入间隙 (默认为真)<br>+ "hanging" => 将行末的句读点排出版面之外 (悬挂排版。默认为假)<br>+ "justify" => 对齐行末 (默认为真)。即使为假也会进行溢出部分的收紧<br>+ "letterSpacing" => 以 em 为单位的实数指定字间 (默认为 0) |

**返回值**

返回绘制结果的 Dictionary (失败时为 void):
%[ "width" => 使用的宽度 (px。列排列方向的厚度), "lines" => 绘制的列数,
"count" => 实际绘制的簇数,
"totalCount" => 没有 count 限制时的簇总数 ]

**说明**

矩形内竖排绘制 (整形 / 日语竖写)

使用统一字体引擎 glyphware，在矩形 (x, y, width, height) 的内侧
以**竖排 (竖写)** 绘制文本。与横排的
[Layer.drawShapedTextArea](Layer.md#drawshapedtextarea) 是不同路径，
将日文按直立、西文按横倒分开排版，标点符号 (句读点、括号类) 的收紧、行首行末避头尾、
挤入 / 挤出按照日语排版规则 (JLReq) 的间隙量表处理。

列的长度为 height，列的步进 (行距) 为“字体大小 + lineSpacing”。
默认 (竖排从右到左) 下第 1 列位于矩形右端并向左推进。放不进矩形的
列不会被绘制，绘制会被裁剪到矩形内。\n (\r\n / \r) 被作为显式换行 (段落
分隔) 处理。

**支持范围仅限正文。** 不支持注音、纵中横、着重号、割注、字距分配、分栏。
font 的 angle、underline (下划线)、strikeout (删除线) 被忽略。

---

### measureVerticalTextArea

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 以像素为单位指定矩形的宽度。 |
| `height` | `&nbsp;` | 以像素为单位指定矩形的高度。 |
| `text` | `&nbsp;` | 指定要测量的字符串。 |
| `font` | `void` | 汇总指定绘制属性 (与 [Layer.drawShapedText](Layer.md#drawshapedtext) 相同)。 |
| `count` | `-1` | 指定 0 以上时仅将开头 count 个簇作为测量对象<br>( 省略时 (-1) 为整体 )。 |
| `lineSpacing` | `0` | 指定列间 (行间) 追加的像素数 (可为负值)。 |
| `options` | `void` | 用 Dictionary 指定排版选项<br>( 与 [Layer.drawVerticalTextArea](Layer.md#drawverticaltextarea) 相同 )。 |

**返回值**

返回测量结果的 Dictionary (失败时为 void)。内容与
[Layer.drawVerticalTextArea](Layer.md#drawverticaltextarea) 的返回值相同。

**说明**

矩形内竖排的测量

不进行绘制，仅按与 [Layer.drawVerticalTextArea](Layer.md#drawverticaltextarea) 相同的排版
进行处理，并以 Dictionary 返回结果。用于在绘制前
调查需要多少列 / 总共有多少字符。

---

### copyRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的左端位置。 |
| `dtop` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的上端位置。 |
| `src` | `&nbsp;` | 指定复制源的图层对象。<br>也可以指定 Bitmap 类的对象。(1.1.0 及以后) |
| `sleft` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的左端位置。 |
| `stop` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的上端位置。 |
| `swidth` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的宽度。 |
| `sheight` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的高度。 |

**说明**

矩形复制

将指定的复制源图层的矩形部分复制到自己的图层的指定位置。

被复制的图像会根据复制目标图层 (执行方法的图层) 的
[Layer.face](Layer.md#face) 属性的值而变化。

`**dfAlpha** (或 dfBoth)    ` : 主图像与遮罩图像都会被复制

`**dfAddAlpha**             ` : 主图像与遮罩图像都会被复制

`**dfOpaque** (或 dfMain)   ` : [Layer.holdAlpha](Layer.md#holdalpha) 属性为真时，仅主图像被复制 (遮罩图像不被复制)。为假时主图像与遮罩图像都会被复制

`**dfMask**                 ` : 仅遮罩图像被复制 (主图像不被复制)

`**dfProvince**             ` : 仅区域图像被复制 (遮罩图像与主图像不被复制)

复制源图层的 Layer.face 属性被忽略。

该方法不受 [Layer.holdAlpha](Layer.md#holdalpha) 影响 (dfAlpha 与 dfAddAlpha 的情况下，无论 holdAlpha 如何，遮罩图像也会被复制)

---

### copy9Patch

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 指定复制源的图层对象。<br>也可以指定 Bitmap 类的对象。 |

**返回值**

边距信息

**说明**

利用 9 path 的图像复制(1.3.0 及以后)

利用 9 path (slice) 进行图像复制。

返回的边距信息是 Rect 类的对象。

---

### piledCopy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的左端位置。 |
| `dtop` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的上端位置。 |
| `src` | `&nbsp;` | 指定复制源的图层对象。 |
| `sleft` | `&nbsp;` | 以 (复制源图层的显示位置中的) 像素为单位指定要复制的矩形的左端位置。 |
| `stop` | `&nbsp;` | 以 (复制源图层的显示位置中的) 像素为单位指定要复制的矩形的上端位置。 |
| `swidth` | `&nbsp;` | 以 (复制源图层的显示位置中的) 像素为单位指定要复制的矩形的宽度。 |
| `sheight` | `&nbsp;` | 以 (复制源图层的显示位置中的) 像素为单位指定要复制的矩形的高度。 |

**说明**

复制叠加图层后的图像

将指定的复制源图层的指定矩形部分连同子图层一起叠加，将
其结果图像复制到自己的图层的指定位置。

该方法不受复制源图层或复制目标图层的 [Layer.face](Layer.md#face) 属性
影响。

---

### operateRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 以 (运算目标图层的图像位置中的) 像素为单位指定运算目标的矩形的左端位置。 |
| `dtop` | `&nbsp;` | 以 (运算目标图层的图像位置中的) 像素为单位指定运算目标的矩形的上端位置。 |
| `src` | `&nbsp;` | 指定运算源的图层对象。<br>也可以指定 Bitmap 类的对象。(1.1.0 及以后) |
| `sleft` | `&nbsp;` | 以 (运算源图层的图像位置中的) 像素为单位指定要运算的矩形的左端位置。 |
| `stop` | `&nbsp;` | 以 (运算源图层的图像位置中的) 像素为单位指定要运算的矩形的上端位置。 |
| `swidth` | `&nbsp;` | 以 (运算源图层的图像位置中的) 像素为单位指定要运算的矩形的宽度。 |
| `sheight` | `&nbsp;` | 以 (运算源图层的图像位置中的) 像素为单位指定要运算的矩形的高度。 |
| `mode` | `omAuto` | 指定运算的模式。<br>指定 `**omAuto**` 时，根据运算源图层的 [Layer.type](Layer.md#type) 属性自动决定运算的种类。<br>指定 `**omPsNormal**` 时，进行 Photoshop 兼容的 Alpha 合成。<br>指定 `**omPsAdditive**` 时，进行 Photoshop 兼容的线性减淡 (添加) 合成。<br>指定 `**omPsSubtractive**` 时，进行 Photoshop 兼容的线性加深合成。<br>指定 `**omPsMultiplicative**` 时，进行 Photoshop 兼容的正片叠底合成。<br>指定 `**omPsScreen**` 时，进行 Photoshop 兼容的滤色合成。<br>指定 `**omPsOverlay**` 时，进行 Photoshop 兼容的叠加合成。<br>指定 `**omPsHardLight**` 时，进行 Photoshop 兼容的强光合成。<br>指定 `**omPsSoftLight**` 时，进行 Photoshop 兼容的柔光合成。<br>指定 `**omPsColorDodge**` 时，进行 Photoshop 兼容的颜色减淡合成。<br>指定 `**omPsColorDodge5**` 时，进行与 Photoshop 5.x 及以下版本兼容的颜色减淡合成。<br>指定 `**omPsColorBurn**` 时，进行 Photoshop 兼容的颜色加深合成。<br>指定 `**omPsLighten**` 时，进行 Photoshop 兼容的变亮合成。<br>指定 `**omPsDarken**` 时，进行 Photoshop 兼容的变暗合成。<br>指定 `**omPsDifference**` 时，进行 Photoshop 兼容的差值合成。<br>指定 `**omPsDifference5**` 时，进行与 Photoshop 5.x 及以下版本兼容的差值合成。<br>指定 `**omPsExclusion**` 时，进行 Photoshop 兼容的排除合成。<br>指定 `**omAdditive**` 时，进行加法合成。<br>指定 `**omSubtractive**` 时，进行减法合成。<br>指定 `**omMultiplicative**` 时，进行乘法合成。<br>指定 `**omDodge**` 时，进行减淡合成。<br>指定 `**omDarken**` 时，进行变暗合成。<br>指定 `**omLighten**` 时，进行变亮合成。<br>指定 `**omScreen**` 时，进行滤色合成。<br>指定 `**omAlpha**` 时，进行 Alpha 合成。<br>指定 `**omAddAlpha**` 时，进行加法 Alpha 合成。<br>指定 `**omOpaque**` 时，src 的 Alpha 信息会被忽略，src 始终被视为完全不透明。 |
| `opa` | `255` | 指定运算的强度 (0 ~ 255)。 |

**说明**

矩形运算合成

将指定的运算源图层的矩形部分以指定的模式运算合成到自己的图层的指定位置。

运算目标 (执行方法) 的图层以及运算源的图层的 [Layer.face](Layer.md#face) 属性的值
被忽略。

运算目标图层的 [Layer.holdAlpha](Layer.md#holdalpha) 属性为假时，
运算系的合成 (omAdditive / omSubtractive / omMultiplicative / omDodge /
omDarken / omLighten / omScreen 以及 omPs 系) 不会保护运算目标的遮罩 (Alpha)
信息，结果的遮罩会成为因模式而异的不定值
( 例: 乘法、减淡、比较系为 0，滤色为 255 )。向 ltAlpha 的
图层进行运算合成等、想要保持遮罩时，请将 holdAlpha 设为
真。

指定 mode 为 omAuto 时，会根据运算源图层的 [Layer.type](Layer.md#type) 属性自动决定运算的种类。

---

### stretchCopy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的左端位置。 |
| `dtop` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的上端位置。 |
| `dwidth` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的宽度。 |
| `dheight` | `&nbsp;` | 以 (复制目标图层的图像位置中的) 像素为单位指定复制目标的矩形的高度。 |
| `src` | `&nbsp;` | 指定复制源的图层对象。<br>也可以指定 Bitmap 类的对象。(1.1.0 及以后) |
| `sleft` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的左端位置。 |
| `stop` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的上端位置。 |
| `swidth` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的宽度。 |
| `sheight` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的高度。 |
| `type` | `stNearest` | 指定缩放的类型。<br>`**stNearest**          ` : 使用最近邻点法<br>`**stFastLinear**       ` : 使用低精度线性插值 (部分实现)<br>`**stSemiFastLinear**   ` : 使用定点线性插值 (1.3 及以后)<br>`**stLinear**           ` : 使用线性插值 (1.3 及以后实现变更)<br>`**stFastCubic**        ` : 使用定点三次插值 (1.3 及以后)<br>`**stCubic**            ` : 使用三次插值 (1.3 及以后实现变更)<br>`**stFastLanczos2**     ` : 使用范围为 4x4 的定点 Lanczos 插值 (1.3 及以后)<br>`**stLanczos2**         ` : 使用范围为 4x4 的 Lanczos 插值 (1.3 及以后)<br>`**stFastLanczos3**     ` : 使用范围为 6x6 的定点 Lanczos 插值 (1.3 及以后)<br>`**stLanczos3**         ` : 使用范围为 6x6 的 Lanczos 插值 (1.3 及以后)<br>`**stFastSpline16**     ` : 使用定点样条插值 4x4 (1.3 及以后)<br>`**stSpline16**         ` : 使用样条插值 4x4 (1.3 及以后)<br>`**stFastSpline36**     ` : 使用定点样条插值 6x6 (1.3 及以后)<br>`**stSpline36**         ` : 使用样条插值 6x6 (1.3 及以后)<br>`**stFastAreaAvg**      ` : 使用定点面积平均缩小。不能放大 (1.3 及以后)<br>`**stAreaAvg**          ` : 使用面积平均缩小。不能放大 (1.3 及以后)<br>`**stFastGaussian**     ` : 使用定点高斯插值 4x4 (1.3 及以后)<br>`**stGaussian**         ` : 使用高斯插值 4x4 (1.3 及以后)<br>`**stFastBlackmanSinc** ` : 使用定点 Blackman-Sinc 插值 8x8 (1.3 及以后)<br>`**stBlackmanSinc**     ` : 使用 Blackman-Sinc 插值 8x8 (1.3 及以后)<br>速度按 stNearest > stFastLinear > stLinear > stCubic 的顺序递减，画质则是速度<br>越快的类型越低。<br>stCubic 及以后的插值方法画质都足够高，可以说是个人喜好的差异。<br>不过，高斯插值会呈现有些模糊的画质。<br>stFastLinear 与其他线性插值 (stSemiFastLinear 与 stLinear) 的差异在缩小时会明显体现出来。<br>stFastLinear 总是参照周围 4 个像素，而 stSemiFastLinear、stLinear 在缩小时会<br>参照等倍时影响范围为 4 个像素那样的范围，即参照更大范围的像素进行插值，因此画质更高<br>(从算法上说才是原本的线性插值)。<br>对于 stFastLinear，可以用按位逻辑或追加指定 stRefNoClip；这种情况下，<br>允许参照要复制的位图的区域外来合成颜色。不指定它时，<br>即使转送源位图的周围有富余，也不会参照转送源位图的范围<br>之外 ( 范围外的颜色被视为最接近位置上的范围内的像素颜色 )。 |
| `option` | `-1.0` | 1.3 及以后添加。<br>三次插值时的锐度。在其他插值方法中目前没有意义。<br>将锐度的值向正方向调大会逐渐模糊，向负方向调大会逐渐锐利。 |

**说明**

缩放复制

将指定的复制源图层的矩形复制到复制目标 (执行方法的图层) 的
矩形。复制源矩形与复制目标矩形的尺寸不同时会进行放大或
缩小。

在当前版本中，通过指定 stFastLinear 使线性插值生效的，是叠加目标 (执行方法的) 图层的 [Layer.face](Layer.md#face) 属性为 dfAlpha (或 dfBoth) 或 dfAddAlpha 的情况。另外，Layer.face 属性为 dfOpaque、[Layer.holdAlpha](Layer.md#holdalpha) 属性为假时也可以线性插值。

另外，在当前版本中，指定 stLinear 或 stCubic 有效的，仅限不伴随
左右/上下翻转、且复制目标矩形不超出图层的情况。

叠加目标 (执行方法的) 图层的 [Layer.face](Layer.md#face) 属性为
dfAlpha (或 dfBoth) 或 dfAddAlpha 时，主图像与遮罩图像双方都会被复制。

dfOpaque (或 dfMain) 时，[Layer.holdAlpha](Layer.md#holdalpha) 属性为真时仅主图像被复制，为假时主图像与遮罩图像双方都会被复制。

---

### operateStretch

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 以 (叠加目标图层的图像位置中的) 像素为单位指定叠加目标的矩形的左端位置。 |
| `dtop` | `&nbsp;` | 以 (叠加目标图层的图像位置中的) 像素为单位指定叠加目标的矩形的上端位置。 |
| `dwidth` | `&nbsp;` | 以 (叠加目标图层的图像位置中的) 像素为单位指定叠加目标的矩形的宽度。 |
| `dheight` | `&nbsp;` | 以 (叠加目标图层的图像位置中的) 像素为单位指定叠加目标的矩形的高度。 |
| `src` | `&nbsp;` | 指定叠加源的图层对象。<br>也可以指定 Bitmap 类的对象。(1.1.0 及以后) |
| `sleft` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的左端位置。 |
| `stop` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的上端位置。 |
| `swidth` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的宽度。 |
| `sheight` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的高度。 |
| `mode` | `omAuto` | 指定运算的模式。<br>指定 `**omAuto**` 时，根据运算源图层的 [Layer.type](Layer.md#type) 属性自动决定运算的种类。<br>指定 `**omPsNormal**` 时，进行 Photoshop 兼容的 Alpha 合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsAdditive**` 时，进行 Photoshop 兼容的线性减淡 (添加) 合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsSubtractive**` 时，进行 Photoshop 兼容的线性加深合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsMultiplicative**` 时，进行 Photoshop 兼容的正片叠底合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsScreen**` 时，进行 Photoshop 兼容的滤色合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsOverlay**` 时，进行 Photoshop 兼容的叠加合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsHardLight**` 时，进行 Photoshop 兼容的强光合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsSoftLight**` 时，进行 Photoshop 兼容的柔光合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsColorDodge**` 时，进行 Photoshop 兼容的颜色减淡合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsColorDodge5**` 时，进行与 Photoshop 5.x 及以下版本兼容的颜色减淡合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsColorBurn**` 时，进行 Photoshop 兼容的颜色加深合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsLighten**` 时，进行 Photoshop 兼容的变亮合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsDarken**` 时，进行 Photoshop 兼容的变暗合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsDifference**` 时，进行 Photoshop 兼容的差值合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsDifference5**` 时，进行与 Photoshop 5.x 及以下版本兼容的差值合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsExclusion**` 时，进行 Photoshop 兼容的排除合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omAdditive**` 时，进行加法合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omSubtractive**` 时，进行减法合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omMultiplicative**` 时，进行乘法合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omDodge**` 时，进行减淡合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omDarken**` 时，进行变暗合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omLighten**` 时，进行变亮合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omScreen**` 时，进行滤色合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omAlpha**` 时，进行 Alpha 合成。<br>指定 `**omAddAlpha**` 时，进行加法 Alpha 合成。这种情况下，当转送目标的 [Layer.face](Layer.md#face) 属性为 dfOpaque 且 [Layer.holdAlpha](Layer.md#holdalpha) 属性为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。<br>指定 `**omOpaque**` 时，src 的 Alpha 信息会被忽略，src 始终被视为完全不透明。这种情况下，当转送目标的 [Layer.face](Layer.md#face) 属性为 dfOpaque 且 [Layer.holdAlpha](Layer.md#holdalpha) 属性为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。 |
| `opa` | `255` | 指定运算的强度 (0 ~ 255)。 |
| `type` | `stNearest` | 指定缩放的类型。<br>`**stNearest**          ` : 使用最近邻点法<br>`**stFastLinear**       ` : 使用低精度线性插值 (部分实现)<br>`**stSemiFastLinear**   ` : 使用定点线性插值 (1.3 及以后)<br>`**stLinear**           ` : 使用线性插值 (1.3 及以后实现变更)<br>`**stFastCubic**        ` : 使用定点三次插值 (1.3 及以后)<br>`**stCubic**            ` : 使用三次插值 (1.3 及以后实现变更)<br>`**stFastLanczos2**     ` : 使用范围为 4x4 的定点 Lanczos 插值 (1.3 及以后)<br>`**stLanczos2**         ` : 使用范围为 4x4 的 Lanczos 插值 (1.3 及以后)<br>`**stFastLanczos3**     ` : 使用范围为 6x6 的定点 Lanczos 插值 (1.3 及以后)<br>`**stLanczos3**         ` : 使用范围为 6x6 的 Lanczos 插值 (1.3 及以后)<br>`**stFastSpline16**     ` : 使用定点样条插值 4x4 (1.3 及以后)<br>`**stSpline16**         ` : 使用样条插值 4x4 (1.3 及以后)<br>`**stFastSpline36**     ` : 使用定点样条插值 6x6 (1.3 及以后)<br>`**stSpline36**         ` : 使用样条插值 6x6 (1.3 及以后)<br>`**stFastAreaAvg**      ` : 使用定点面积平均缩小。不能放大 (1.3 及以后)<br>`**stAreaAvg**          ` : 使用面积平均缩小。不能放大 (1.3 及以后)<br>`**stFastGaussian**     ` : 使用定点高斯插值 4x4 (1.3 及以后)<br>`**stGaussian**         ` : 使用高斯插值 4x4 (1.3 及以后)<br>`**stFastBlackmanSinc** ` : 使用定点 Blackman-Sinc 插值 8x8 (1.3 及以后)<br>`**stBlackmanSinc**     ` : 使用 Blackman-Sinc 插值 8x8 (1.3 及以后)<br>速度按 stNearest > stFastLinear > stLinear > stCubic 的顺序递减，画质则是速度<br>越快的类型越低。<br>stCubic 及以后的插值方法画质都足够高，可以说是个人喜好的差异。<br>不过，高斯插值会呈现有些模糊的画质。<br>stFastLinear 与其他线性插值 (stSemiFastLinear 与 stLinear) 的差异在缩小时会明显体现出来。<br>stFastLinear 总是参照周围 4 个像素，而 stSemiFastLinear、stLinear 在缩小时会<br>参照等倍时影响范围为 4 个像素那样的范围，即参照更大范围的像素进行插值，因此画质更高<br>(从算法上说才是原本的线性插值)。<br>对于 stFastLinear，可以用按位逻辑或追加指定 stRefNoClip；这种情况下，<br>允许参照要复制的位图的区域外来合成颜色。不指定它时，<br>即使转送源位图的周围有富余，也不会参照转送源位图的范围<br>之外 ( 范围外的颜色被视为最接近位置上的范围内的像素颜色 )。 |
| `option` | `-1.0` | 1.3 及以后添加。<br>三次插值时的锐度。在其他插值方法中目前没有意义。<br>将锐度的值向正方向调大会逐渐模糊，向负方向调大会逐渐锐利。 |

**说明**

缩放运算合成

将指定的叠加源图层的矩形，运算合成到叠加目标 (执行方法的图层) 的
矩形。叠加源矩形与叠加目标矩形的尺寸不同时会进行放大或缩小。

关于 [Layer.holdAlpha](Layer.md#holdalpha) 属性为假时运算系合成不保护叠加目标的遮罩 (Alpha) 信息的要点，请参阅 [Layer.operateRect](Layer.md#operaterect)。

指定 mode 为 omAuto 时，会根据运算源图层的 [Layer.type](Layer.md#type) 属性自动决定运算的种类。

---

### affineCopy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 指定复制源的图层对象。<br>也可以指定 Bitmap 类的对象。(1.1.0 及以后) |
| `sleft` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的左端位置。 |
| `stop` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的上端位置。 |
| `swidth` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的宽度。 |
| `sheight` | `&nbsp;` | 以 (复制源图层的图像位置中的) 像素为单位指定要复制的矩形的高度。 |
| `affine` | `&nbsp;` | 指定如何对待后续的 6 个参数 (A ~ F 参数)。<br>指定真时，6 个参数分别按以下方式解释。<br>`A   : 2D 仿射变换矩阵的 a`<br>`B   : 2D 仿射变换矩阵的 b`<br>`C   : 2D 仿射变换矩阵的 c`<br>`D   : 2D 仿射变换矩阵的 d`<br>`E   : 2D 仿射变换矩阵的 tx`<br>`F   : 2D 仿射变换矩阵的 ty`<br>通过仿射变换，复制源的图像位置 (x, y) (不过，以复制源矩形左上角为 (0, 0)) 会按以下公式变换为复制目标的图像位置 (x', y')。<br>x' =  a*x + c*y + tx<br>y' =  b*x + d*y + ty<br>指定假时，6 个参数分别按以下方式解释。这些参数也接受以实数指定。<br>`A   : 复制源矩形左上角点在复制目标图像位置中的 X 坐标位置(x0)`<br>`B   : 复制源矩形左上角点在复制目标图像位置中的 Y 坐标位置(y0)`<br>`C   : 复制源矩形右上角点在复制目标图像位置中的 X 坐标位置(x1)`<br>`D   : 复制源矩形右上角点在复制目标图像位置中的 Y 坐标位置(y1)`<br>`E   : 复制源矩形左下角点在复制目标图像位置中的 X 坐标位置(x2)`<br>`F   : 复制源矩形左下角点在复制目标图像位置中的 Y 坐标位置(y2)`<br>指定假时，与复制源右下角对应的复制目标位置 (x3, y3) 会自动按以下公式计算。<br>x3 = x1 - x0 + x2<br>y3 = y1 - y0 + y2 |
| `A` | `&nbsp;` | A 参数。含义根据 affine 参数变化。 |
| `B` | `&nbsp;` | B 参数。含义根据 affine 参数变化。 |
| `C` | `&nbsp;` | C 参数。含义根据 affine 参数变化。 |
| `D` | `&nbsp;` | D 参数。含义根据 affine 参数变化。 |
| `E` | `&nbsp;` | E 参数。含义根据 affine 参数变化。 |
| `F` | `&nbsp;` | F 参数。含义根据 affine 参数变化。 |
| `type` | `stNearest` | 指定仿射变换的类型。<br>`**stNearest**    ` : 使用最近邻点法<br>`**stFastLinear** ` : 使用低精度线性插值 ( 部分实现 )<br>`**stLinear**     ` : 使用线性插值 ( 未实现 )<br>`**stCubic**      ` : 使用三次插值 ( 未实现 )<br>对于 stFastLinear 以及 stLinear、stCubic，可以用按位逻辑或追加指定<br>stRefNoClip；这种情况下，允许参照要复制的位图的区域外来合成<br>颜色。不指定它时，即使转送源位图的周围有富余，<br>也不会参照转送源位图的范围之外 ( 范围外的颜色被视为最接近位置上的<br>范围内的像素颜色 )。 |
| `clear` | `false` | 指定是否用 [Layer.neutralColor](Layer.md#neutralcolor) 属性所示的颜色、透明度清除转送目标图层中仿射变换后图像的周围。指定真时清除，省略该参数或传入假时不清除。<br>清除的区域也可以用 [Layer.setClip](Layer.md#setclip) 方法限制。<br>使用该清除功能，可以省去先清除转送目标图层、再用仿射变换覆盖转送图像时，对被覆盖区域(被清除处将被仿射变换覆盖的部分)进行清除的浪费。 |

**说明**

仿射变换复制

将指定的复制源图层的矩形一边进行仿射变换，一边复制到复制目标
 (执行方法的图层)。

通过 affine 参数，可以选择将变形参数指定为二维仿射变换矩阵，
或者直接指定变换后的点。

在当前版本中，通过指定 stFastLinear 使线性插值生效的，是叠加目标 (执行方法的) 图层的 [Layer.face](Layer.md#face) 属性为 dfAlpha (或 dfBoth) 或 dfAddAlpha 的情况。另外，Layer.face 属性为 dfOpaque、[Layer.holdAlpha](Layer.md#holdalpha) 属性为假时也可以线性插值。

叠加目标 (执行方法的) 图层的 [Layer.face](Layer.md#face) 属性为
dfAlpha (或 dfBoth) 或 dfAddAlpha 时，主图像与遮罩图像双方都会被复制。

叠加目标 (执行方法的) 图层的 Layer.face 属性为
dfOpaque (或 dfMain) 时，[Layer.holdAlpha](Layer.md#holdalpha) 属性为真时仅主图像被复制，为假时主图像与遮罩图像双方都会被复制。

二维仿射变换矩阵进行的变换，以复制源矩形左上角为原点 (0, 0)，
定义如下。

![](../_assets/2DAffineMatrix.png)

通过进行二维仿射变换，可以进行放大缩小、旋转、切变(倾斜)、平移、翻转，或者这些的全部组合变形。

在进行二维仿射变换的方法中，也可以不指定二维仿射矩阵，而是直接指定变换后的各顶点来指定变形，但即使在这种情况下，也无法进行无法用二维仿射变换定义的变形。

在仿射变换中，像素被视为具有 1.0 × 1.0 的大小。也就是说，(0, 0) 位置的像素被视为位于 (-0.5, -0.5) - (0.5, 0.5) 的范围内。

---

### operateAffine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 指定叠加源的图层对象。<br>也可以指定 Bitmap 类的对象。(1.1.0 及以后) |
| `sleft` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的左端位置。 |
| `stop` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的上端位置。 |
| `swidth` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的宽度。 |
| `sheight` | `&nbsp;` | 以 (叠加源图层的图像位置中的) 像素为单位指定要叠加的矩形的高度。 |
| `affine` | `&nbsp;` | 指定如何对待后续的 6 个参数 (A ~ F 参数)。<br>指定为真时，6 个参数分别按以下方式解释。<br>`A   : 2D 仿射变换矩阵的 a`<br>`B   : 2D 仿射变换矩阵的 b`<br>`C   : 2D 仿射变换矩阵的 c`<br>`D   : 2D 仿射变换矩阵的 d`<br>`E   : 2D 仿射变换矩阵的 tx`<br>`F   : 2D 仿射变换矩阵的 ty`<br>通过仿射变换，叠加源的图像位置 (x, y) ( 不过，以叠加源矩形的左上角为 (0, 0) ) 会按以下式子被转换为叠加目标的图像位置 (x', y')。<br>x' =  a*x + c*y + tx<br>y' =  b*x + d*y + ty<br>指定为假时，6 个参数分别按以下方式解释。<br>`A   : 复制源矩形左上角点在复制目标图像位置中的 X 坐标位置(x0)`<br>`B   : 复制源矩形左上角点在复制目标图像位置中的 Y 坐标位置(y0)`<br>`C   : 复制源矩形右上角点在复制目标图像位置中的 X 坐标位置(x1)`<br>`D   : 复制源矩形右上角点在复制目标图像位置中的 Y 坐标位置(y1)`<br>`E   : 复制源矩形左下角点在复制目标图像位置中的 X 坐标位置(x2)`<br>`F   : 复制源矩形左下角点在复制目标图像位置中的 Y 坐标位置(y2)`<br>指定为假时，与叠加源右下角对应的叠加目标位置 (x3, y3) 会按以下式子自动计算。<br>x3 = x1 - x0 + x2<br>y3 = y1 - y0 + y2 |
| `A` | `&nbsp;` | A 参数。含义根据 affine 参数变化。 |
| `B` | `&nbsp;` | B 参数。含义根据 affine 参数变化。 |
| `C` | `&nbsp;` | C 参数。含义根据 affine 参数变化。 |
| `D` | `&nbsp;` | D 参数。含义根据 affine 参数变化。 |
| `E` | `&nbsp;` | E 参数。含义根据 affine 参数变化。 |
| `F` | `&nbsp;` | F 参数。含义根据 affine 参数变化。 |
| `mode` | `omAuto` | 指定运算的模式。<br>指定 `**omAuto**` 时，根据运算源图层的 [Layer.type](Layer.md#type) 属性自动决定运算的种类。<br>指定 `**omPsNormal**` 时，进行 Photoshop 兼容的 Alpha 合成 ( 现行版本中未实现 )。<br>指定 `**omPsAdditive**` 时，进行 Photoshop 兼容的线性减淡 (添加) 合成 ( 现行版本中未实现 )。<br>指定 `**omPsSubtractive**` 时，进行 Photoshop 兼容的线性加深合成 ( 现行版本中未实现 )。<br>指定 `**omPsMultiplicative**` 时，进行 Photoshop 兼容的正片叠底合成 ( 现行版本中未实现 )。<br>指定 `**omPsScreen**` 时，进行 Photoshop 兼容的滤色合成 ( 现行版本中未实现 )。<br>指定 `**omPsOverlay**` 时，进行 Photoshop 兼容的叠加合成 ( 现行版本中未实现 )。<br>指定 `**omPsHardLight**` 时，进行 Photoshop 兼容的强光合成 ( 现行版本中未实现 )。<br>指定 `**omPsSoftLight**` 时，进行 Photoshop 兼容的柔光合成 ( 现行版本中未实现 )。<br>指定 `**omPsColorDodge**` 时，进行 Photoshop 兼容的颜色减淡合成 ( 现行版本中未实现 )。<br>指定 `**omPsColorDodge5**` 时，进行与 Photoshop 5.x 及以下版本兼容的颜色减淡合成 ( 现行版本中未实现 )。<br>指定 `**omPsColorBurn**` 时，进行 Photoshop 兼容的颜色加深合成 ( 现行版本中未实现 )。<br>指定 `**omPsLighten**` 时，进行 Photoshop 兼容的变亮合成 ( 现行版本中未实现 )。<br>指定 `**omPsDarken**` 时，进行 Photoshop 兼容的变暗合成 ( 现行版本中未实现 )。<br>指定 `**omPsDifference**` 时，进行 Photoshop 兼容的差值合成 ( 现行版本中未实现 )。<br>指定 `**omPsDifference5**` 时，进行与 Photoshop 5.x 及以下版本兼容的差值合成 ( 现行版本中未实现 )。<br>指定 `**omPsExclusion**` 时，进行 Photoshop 兼容的排除合成 ( 现行版本中未实现 )。<br>指定 `**omAdditive**` 时，进行加法合成 ( 现行版本中未实现 )。<br>指定 `**omSubtractive**` 时，进行减法合成 ( 现行版本中未实现 )。<br>指定 `**omMultiplicative**` 时，进行乘法合成 ( 现行版本中未实现 )。<br>指定 `**omDodge**` 时，进行减淡合成 ( 现行版本中未实现 )。<br>指定 `**omDarken**` 时，进行变暗合成 ( 现行版本中未实现 )。<br>指定 `**omLighten**` 时，进行变亮合成 ( 现行版本中未实现 )。<br>指定 `**omScreen**` 时，进行滤色合成 ( 现行版本中未实现 )。<br>指定 `**omAlpha**` 时，进行 Alpha 合成。<br>指定 `**omAddAlpha**` 时，进行加法 Alpha 合成。这种情况下，当转送目标的 [Layer.face](Layer.md#face) 属性为 dfOpaque 且 [Layer.holdAlpha](Layer.md#holdalpha) 属性为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。<br>指定 `**omOpaque**` 时，src 的 Alpha 信息会被忽略，src 始终被视为完全不透明。这种情况下，当转送目标的 [Layer.face](Layer.md#face) 属性为 dfOpaque 且 [Layer.holdAlpha](Layer.md#holdalpha) 属性为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。 |
| `opa` | `255` | 指定叠加的不透明度 (0 ~ 255)。 |
| `type` | `stNearest` | 指定仿射变换的类型。<br>`**stNearest**    ` : 使用最近邻点法<br>`**stFastLinear** ` : 使用低精度线性插值 (部分实现)<br>`**stLinear**     ` : 使用线性插值 (未实现)<br>`**stCubic**      ` : 使用三次插值 (未实现)<br>速度按 stNearest > stFastLinear > stLinear > stCubic 的顺序递减，画质则是速度<br>越快的模式越低。<br>对于 stFastLinear 以及 stLinear、stCubic，可以用按位逻辑或追加指定<br>stRefNoClip；这种情况下，允许参照要复制的位图的区域外来合成<br>颜色。不指定它时，即使转送源位图的周围有富余，<br>也不会参照转送源位图的范围之外 ( 范围外的颜色被视为最接近位置上的<br>范围内的像素颜色 )。 |

**说明**

仿射变换运算合成

将指定的叠加源图层的矩形一边进行仿射变换，一边运算合成到
叠加目标 (执行方法的图层)。

关于仿射变换，也请参阅 [Layer.affineCopy](Layer.md#affinecopy)。

关于 [Layer.holdAlpha](Layer.md#holdalpha) 属性为假时运算系合成不保护叠加目标的遮罩 (Alpha) 信息的要点，请参阅 [Layer.operateRect](Layer.md#operaterect)。

指定 mode 为 omAuto 时，会根据运算源图层的 [Layer.type](Layer.md#type) 属性自动决定运算的种类。

---

### doBoxBlur

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `xblur` | `1` | 指定横向模糊的范围。 |
| `yblur` | `1` | 指定纵向模糊的范围。 |

**说明**

应用矩形模糊

进行模糊 (blur)。算法是“矩形模糊”(box blur)。

矩形模糊是取由 xblur 和 yblur 两个参数表现的“范围”中像素亮度的平均值。例如 xblur=10 yblur=2 时，以对象像素为中心，横向取 -10~10、纵向取 -2~2 的矩形范围内像素的亮度平均值，它就是该像素最终的亮度。

范围的面积可以用 (xblur×2+1) × (yblur×2+1) 计算。在当前版本中，该面积小于 256 时会采用比面积在 256 以上时更高速的算法。

[Layer.face](Layer.md#face) 属性为 dfAlpha 时会使用用于 Alpha 合成的特别算法，因此会稍慢一些。dfAddAlpha 及其他绘制方式时，算法会更高速。

---

### adjustGamma

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rgamma` | `1.0` | 指定红色分量的伽马值 (0.0 ~ 1.0 ~ 9.0)。 |
| `rfloor` | `0` | 指定红色分量的输出最低值 (0 ~ 255)。 |
| `rceil` | `255` | 指定红色分量的输出最大值 (0 ~ 255)。 |
| `ggamma` | `1.0` | 指定绿色分量的伽马值 (0.0 ~ 1.0 ~ 9.0)。 |
| `gfloor` | `0` | 指定绿色分量的输出最低值 (0 ~ 255)。 |
| `gceil` | `255` | 指定绿色分量的输出最大值 (0 ~ 255)。 |
| `bgamma` | `1.0` | 指定蓝色分量的伽马值 (0.0 ~ 1.0 ~ 9.0)。 |
| `bfloor` | `0` | 指定蓝色分量的输出最低值 (0 ~ 255)。 |
| `bceil` | `255` | 指定蓝色分量的输出最大值 (0 ~ 255)。 |

**说明**

伽马校正

对图像执行伽马校正。

伽马值指定为 1.0 时伽马曲线变为直线。

输出最低值与输出最大值是用于指定各分量亮度的最低值和最高值的。

将最高值设置为低于最低值的值可以使图像反转。

该方法会参照 [Layer.face](Layer.md#face) 属性。它为 dfAddAlpha 时，该方法
使用用于加法 Alpha 合成的特别伽马校正例程。该例程对加法 Alpha 合成中相当于 Alpha 合成的分量进行伽马校正，但对相当于加法合成的分量不进行伽马校正。

---

### doGrayScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rweight` | `&nbsp;` | 指定红色分量的权重。请 3 个全部省略或 3 个全部指定。 |
| `gweight` | `&nbsp;` | 绿色分量的权重。 |
| `bweight` | `&nbsp;` | 蓝色分量的权重。 |

**说明**

灰度转换

将图像转换为灰度。

省略参数时使用相当于 BT.709 的权重 (0.2126 / 0.7152 / 0.0722)
(以往的行为)。 传入 3 个权重时可以使用任意的加权。 例如
BT.601 的话为 `doGrayScale(0.299, 0.587, 0.114)`。

权重被作为相对值处理，内部会先归一化为合计 1，再量化为 8 位定点
(合计 256)。 因此 `0.299, 0.587, 0.114` 与
`76, 149, 29` 会得到相同的结果。 由于量化，转换结果与理论值
最多偏差 1 左右 (显式指定 BT.709 的权重时，会得到与省略参数时
完全相同的结果)。

权重为负、或合计为 0 时会抛出异常。

---

### flipLR

方法

**说明**

左右翻转

进行图像的左右翻转。

该方法不受 [Layer.setClip](Layer.md#setclip) 方法等带来的绘制裁剪矩形的影响 (始终翻转整个图层图像)。

也不受 [Layer.face](Layer.md#face) 属性和 [Layer.holdAlpha](Layer.md#holdalpha) 属性的影响。

---

### flipUD

方法

**说明**

上下翻转

进行图像的上下翻转。

该方法不受 [Layer.setClip](Layer.md#setclip) 方法等带来的绘制裁剪矩形的影响 (始终翻转整个图层图像)。

也不受 [Layer.face](Layer.md#face) 属性和 [Layer.holdAlpha](Layer.md#holdalpha) 属性的影响。

---

### convertType

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 指定作为转换源的绘制方式类型。 |

**说明**

图层图像表现形式转换

转换图层图像的格式。

该方法用于在 ltAlpha (dfAlpha) 与 ltAddAlpha (dfAddAlpha) 这样“图层图像表现形式不同但可以进行同样表现的类型”之间转换图像的表现形式。

例如，把以 ltAlpha 显示的图层类型直接改为 ltAddAlpha 时，由于 Alpha 通道与颜色信息的处理方式不同，不会正常显示。因此需要使用该方法，从 dfAlpha 转换为 dfAddAlpha。

在该方法中，转换目标的图像表现形式是 [Layer.face](Layer.md#face) 属性所指定的绘制方式对应的形式 (请注意不是由 [Layer.type](Layer.md#type) 指定的图层类型，而是绘制方式)。

from 参数请指定与转换源的图像表现形式对应的绘制方式(df 开头的常量; 参照 [Layer.face](Layer.md#face))。from 参数不能指定 `dfAuto`。

目前支持的转换是 dfAlpha→dfAddAlpha 与 dfAddAlpha→dfAlpha 的转换。dfAddAlpha→dfAlpha 时，转换可能会丢失颜色信息。

该方法不受绘制裁剪矩形的影响 (始终影响整个图层图像)。

---

### update

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 以显示坐标中的像素为单位指定要更新的矩形的左端位置。 |
| `top` | `&nbsp;` | 以显示坐标中的像素为单位指定要更新的矩形的上端位置。 |
| `width` | `&nbsp;` | 以显示坐标中的像素为单位指定要更新的矩形的宽度。 |
| `height` | `&nbsp;` | 以显示坐标中的像素为单位指定要更新的矩形的高度。 |

**说明**

图像的更新

该方法强制图层绘制到画面。

执行绘制系的方法等时会自动发生画面更新，但
用该方法可以强制引起向画面的绘制。

省略全部参数时会重新绘制整个图层。

该方法会把 [Layer.callOnPaint](Layer.md#callonpaint) 属性设为真。

在实际绘制到画面之前，无论执行该方法多少次，发生画面绘制的
都只有 1 次 (会被缓存)。

---

### setCursorPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 以像素为单位指定鼠标光标的 (该图层的显示坐标中的) x 坐标值。<br>该值也可以通过 [Layer.cursorX](Layer.md#cursorx) 属性设置/获取。 |
| `y` | `&nbsp;` | 以像素为单位指定鼠标光标的 (该图层的显示坐标中的) y 坐标值。<br>该值也可以通过 [Layer.cursorX](Layer.md#cursorx) 属性设置/获取。 |

**说明**

鼠标光标位置的指定 (图层坐标)

用**该图层的显示坐标**指定鼠标光标的位置。

⚠ [Window.setCursorPos](Window.md#setcursorpos) 与之同名，但那边是
**绘制区域坐标**，坐标系不同。

---

### focus

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `direction` | `true` | 传递给 [Layer.onBeforeFocus](Layer.md#onbeforefocus) 与 [Layer.onFocus](Layer.md#onfocus) 事件的<br>direction 参数的值。 |

**说明**

焦点的设置

为图层指定**焦点**。图层接收到焦点后，
就可以进行键盘输入。

---

### focusPrev

方法

**返回值**

新获得焦点的图层对象

**说明**

向靠前的图层设置焦点

向前方搜索可获得焦点的图层，找到图层后就向该图层设置焦点。

---

### focusNext

方法

**返回值**

新获得焦点的图层对象

**说明**

向靠后的图层设置焦点

向后方搜索可获得焦点的图层，找到图层后就向该图层设置焦点。

---

### setMode

方法

**说明**

进入模态状态

为图层设置**模式**。设置模式后 (成为**模态**后)，仅该图层的子图层
可以接收焦点和鼠标消息。

---

### removeMode

方法

**说明**

解除模态状态

解除由 [Layer.setMode](Layer.md#setmode) 设置的模态状态。

---

### setAttentionPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 以像素为单位指定要注视的 (该图层的显示坐标中的) x 坐标值。<br>该值也可以通过 [Layer.attentionLeft](Layer.md#attentionleft) 属性设置/获取。 |
| `top` | `&nbsp;` | 以像素为单位指定要注视的 (该图层的显示坐标中的) x 坐标值。<br>该值也可以通过 [Layer.attentionTop](Layer.md#attentiontop) 属性设置/获取。 |

**说明**

注视位置的指定

指定**注视位置**。注视位置通常设置为插入符 (在文本编辑器等中用于指示
键盘文字输入位置而闪烁的竖线) 的位置。IME 的未确定文字会显示在该注视
位置。

**相关:** [Layer.useAttention](Layer.md#useattention)

---

### beginTransition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定转场名。<br>默认定义了 'crossfade' (交叉淡化)、'universal' (通用转<br>场)、'scroll' (滚动转场)。 |
| `withchildren` | `true` | 是否让子图层也一起进行转场。指定真时<br>连子图层一起转场。指定假时仅执行方法的图层<br>进行转场。 |
| `transsrc` | `null` | 指定作为切换目标的图层。根据转场的不同，有的可能<br>不需要指定 (例如单独进行转场的)。 |
| `options` | `%[ ]` | 用字典数组指定转场的选项。<br>需要的选项因转场的种类而异。<br>与转场种类无关、可以通用指定的选项有 'selfupdate' 成员和 'callback' 成员。<br>'selfupdate' 成员为真时，吉里吉里将不进行自动的画面更新。<br>这种情况下，必须由程序侧适当地用 [Layer.update](Layer.md#update) 方法等更新画面。该功能在想要使转场引起的绘制与程序引起的绘制完全同步时很方便。<br>给 'callback' 成员指定 TJS2 的方法后，<br>每次实际进行绘制时都会调用该方法。<br>在该方法 (被回调的方法) 中，请返回 0 以上的 'tick' 值。<br>许多转场根据以毫秒为单位的实际时间 'tick'<br>值进行转场，<br>但通过在被回调的方法中实现为返回任意的 tick，<br>可以在任意时点回退转场的效果、或在途中快进，<br>从而可以不受实际时间影响地控制转场。<br>许多转场把用选项的 'time'<br>成员指定的值视为转场的终点。<br>因此，例如把选项的 'time' 指定为 1000 等适当的值，<br>并在该被回调的方法中返回小于 1000 的值，<br>就可以让转场在任意阶段进行显示。<br>另外，在许多转场中，当 'tick' 值达到选项的 'time'<br>指定的值时，转场会停止，<br>因此如果不想让转场停止，请总是指定小于 'time'<br>指定值的值。 |

**说明**

转场的开始

开始转场。

children=真 时的转场在结束时，会与 transsrc 指定的
转场源完全交换父子关系的树结构。

children=假 时，只有转场源的图层与执行了方法的图层 (
转场目标的图层) 会被交换。

无论哪种情况，都会在树结构上进行交换，请注意。

该方法只是开始转场，会立即返回。

---

### stopTransition

方法

**说明**

停止转场

停止正在进行的转场。

---

### assignImages

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 指定复制源的图层。 |

**说明**

图像的复制

复制 src 指定的图层的主图像、遮罩图像、区域图像的全部。

图像尺寸与复制源图层的图像尺寸相同。其他信息不会被复制。

虽说是复制，实际上只是变为“同一个图像被两个以上的图层共享”的状态，因此
该方法几乎不花费执行时间。

---

### saveLayerImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 指定要保存的存储名。 |
| `type` | `"bmp"` | 用字符串指定要保存的图像格式。在当前版本中可以指定以下格式。<br>"**bmp**" 或 "**bmp32**"<br>32bpp 的 BMP。也会保存 Alpha 通道(遮罩)。<br>"**bmp24**"<br>24bpp 的 BMP。不会保存 Alpha 通道(遮罩)。<br>"**bmp8**"<br>8bpp 的 BMP。不会保存 Alpha 通道(遮罩)。图像会<br>使用 252 色固定调色板的 4×4 有序抖动进行减色。<br>"**jpg**"<br>JPEG。不会保存 Alpha 通道(遮罩)。图像会<br>以质量 90% 保存。<br>"**jpg###**"<br>JPEG。不会保存 Alpha 通道(遮罩)。图像会<br>以由 ### 指定的质量保存。"jpg010" 为 10%、"jpg100" 为 100%、"jpg080" 为 80%。<br>"**png**"<br>32bpp 的 PNG。也会保存 Alpha 通道(遮罩)。<br>"**png24**"<br>24bpp 的 PNG。不会保存 Alpha 通道(遮罩)。<br>"**tlg5**"<br>32bpp 的 TLG5。也会保存 Alpha 通道(遮罩)。<br>"**tlg524**"<br>24bpp 的 TLG5。不会保存 Alpha 通道(遮罩)。<br>"**tlg6**"<br>32bpp 的 TLG6。也会保存 Alpha 通道(遮罩)。<br>"**tlg624**"<br>24bpp 的 TLG6。不会保存 Alpha 通道(遮罩)。 |

**说明**

图像的保存

将文件以 type 指定的图像格式保存到 name 指定的存储 (文件) 中。

保存的是图层的图像，区域图像无法保存。

---

### copyToBitmapFromMainImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dest` | `&nbsp;` | 指定复制目标的 [Bitmap](Bitmap.md) 对象。 |

**说明**

向 Bitmap 复制图像

将图层的主图像复制到 dest 指定的 Bitmap 对象。

图像尺寸与复制源图层的图像尺寸相同。

虽说是复制，实际上只是变为“同一个图像被两个以上的图层共享”的状态，因此
该方法几乎不花费执行时间。

**相关:** [Layer.copyFromBitmapToMainImage](Layer.md#copyfrombitmaptomainimage)

---

### copyFromBitmapToMainImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 指定复制源的 [Bitmap](Bitmap.md) 对象。 |

**说明**

从 Bitmap 复制图像

将图像从 src 指定的 Bitmap 对象复制到图层的主图像。

图像尺寸与复制源的 Bitmap 对象的图像尺寸相同。

虽说是复制，实际上只是变为“同一个图像被两个以上的图层共享”的状态，因此
该方法几乎不花费执行时间。

**相关:** [Layer.copyToBitmapFromMainImage](Layer.md#copytobitmapfrommainimage)

---

### dump

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `level` | `0` | 指定要输出的层级深度。指定 0 或省略时<br>输出属下的全部层级。 |

**说明**

图层结构的转储输出

将以该图层为起点的图层树结构输出到调试日志。

---

### releaseTouchCapture

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `void` | 指定要释放的个别触摸 ID。省略时释放该图层<br>已获得的全部触摸捕获。 |

**说明**

触摸捕获的释放

释放自身已获得的触摸捕获。

---

### onClick

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 图层被点击位置的 x 坐标 (图层显示坐标中的) 的值。 |
| `y` | `&nbsp;` | 图层被点击位置的 y 坐标 (图层显示坐标中的) 的值。 |

**说明**

图层被点击

图层被点击时发生。

**相关:** [Layer.onMouseDown](Layer.md#onmousedown) / [Layer.onDoubleClick](Layer.md#ondoubleclick)

---

### onDoubleClick

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 图层被双击位置的 x 坐标 (图层显示坐标中的) 的值。 |
| `y` | `&nbsp;` | 图层被双击位置的 y 坐标 (图层显示坐标中的) 的值。 |

**说明**

图层被双击

图层被双击时发生。

**相关:** [Layer.onClick](Layer.md#onclick)

---

### onMouseDown

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标按钮被按下位置的 x 坐标 (图层显示坐标中的) 的值。 |
| `y` | `&nbsp;` | 鼠标按钮被按下位置的 y 坐标 (图层显示坐标中的) 的值。 |
| `button` | `&nbsp;` | 被按下的鼠标按钮。为以下之一的值。<br>`**mbLeft**    : `按下了鼠标左键<br>`**mbMiddle**  : `按下了鼠标中键<br>`**mbRight**   : `按下了鼠标右键<br>`**mbX1**      : `按下了鼠标侧键第 1 键<br>`**mbX2**      : `按下了鼠标侧键第 2 键 |
| `shift` | `&nbsp;` | 鼠标按钮被按下时同时按着的 Shift 系按键的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键 |

**说明**

鼠标按钮被按下

鼠标按钮被按下时发生。

**相关:** [Layer.onClick](Layer.md#onclick)

---

### onMouseUp

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标按钮被放开位置的 x 坐标 (图层显示坐标中的) 的值。 |
| `y` | `&nbsp;` | 鼠标按钮被放开位置的 y 坐标 (图层显示坐标中的) 的值。 |
| `button` | `&nbsp;` | 被放开的鼠标按钮。为以下之一的值。<br>`**mbLeft**    : `放开了鼠标左键<br>`**mbMiddle**  : `放开了鼠标中键<br>`**mbRight**   : `放开了鼠标右键<br>`**mbX1**      : `放开了鼠标侧键第 1 键<br>`**mbX2**      : `放开了鼠标侧键第 2 键 |
| `shift` | `&nbsp;` | 鼠标按钮被放开时同时按着的 Shift 系按键的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键 |

**说明**

鼠标按钮被放开

鼠标按钮被放开时发生。

---

### onMouseMove

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 鼠标移动位置的 x 坐标 (图层显示坐标中的) 的值。 |
| `y` | `&nbsp;` | 鼠标移动位置的 y 坐标 (图层显示坐标中的) 的值。 |
| `shift` | `&nbsp;` | 鼠标移动时同时按着的 Shift 系按键和鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键 |

**说明**

鼠标移动了

鼠标移动时发生。

---

### onMouseEnter

事件

**说明**

鼠标进入

鼠标进入图层区域内时发生。

**相关:** [Layer.onMouseLeave](Layer.md#onmouseleave)

---

### onMouseLeave

事件

**说明**

鼠标离开

鼠标从图层区域内离开时发生。

**相关:** [Layer.onMouseEnter](Layer.md#onmouseenter)

---

### onMouseWheel

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `shift` | `&nbsp;` | 鼠标移动时同时按着的 Shift 系按键和鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键 |
| `delta` | `&nbsp;` | 滚轮的旋转角。向上 (与用户相反的方向) 旋转时为正，<br>向下 (用户一侧的方向) 旋转时为负值。通常，最小量为 120<br>。 |
| `x` | `&nbsp;` | 滚轮旋转位置的 x 坐标 (图层显示坐标中的) 的值。 |
| `y` | `&nbsp;` | 滚轮旋转位置的 y 坐标 (图层显示坐标中的) 的值。 |

**说明**

鼠标滚轮旋转了

鼠标滚轮旋转时发生。

该事件与键盘事件相同，只会在持有焦点的图层上发生。

---

### onKeyDown

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 被按下的键的**虚拟键码**值。 |
| `shift` | `&nbsp;` | 键被按下时同时按着的 Shift 系按键和鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键<br>另外，键盘被长时间按住、发生按键重复时，<br>还会组合以下值。<br>`**ssRepeat**  : `发生了按键重复 |
| `process` | `true` | 调用超类的 onKeyDown 时，向该参数传入假，超类将<br>不再对该键执行默认处理(焦点的移动等)。 |

**说明**

键被按下

键被按下时发生。

---

### onKeyUp

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 被放开的键的**虚拟键码**值。 |
| `shift` | `&nbsp;` | 键被放开时同时按着的 Shift 系按键和鼠标按钮的状态。<br>为以下值的按位 OR 组合。<br>`**ssAlt**     : `按着 ALT 键<br>`**ssShift**   : `按着 SHIFT 键<br>`**ssCtrl**    : `按着 CTRL 键<br>`**ssLeft**    : `按着鼠标左键<br>`**ssMiddle**  : `按着鼠标中键<br>`**ssRight**   : `按着鼠标右键 |
| `process` | `true` | 调用超类的 onKeyUp 时，向该参数传入假，超类将<br>不再对该键执行默认处理(焦点的移动等)。 |

**说明**

键被放开

键被放开时发生。

---

### onKeyPress

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 输入的字符。 |
| `process` | `true` | 调用超类的 onKeyPress 时，向该参数传入假，超类将<br>不再对该键执行默认处理(焦点的移动等)。 |

**说明**

字符被输入

字符被输入时发生。与 [Layer.onKeyDown](Layer.md#onkeydown) 不同的是，onKeyDown
处理虚拟键码，而该事件处理字符本身。被按下的键是
与字符无关的键 (功能键等) 时，该事件不会发生。

---

### onHitTest

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 进行命中判定的位置的 (图层显示坐标内的) x 坐标。 |
| `y` | `&nbsp;` | 进行命中判定的位置的 (图层显示坐标内的) y 坐标。 |
| `hit` | `&nbsp;` | 命中判定的结果，命中时为真，未命中时为假。<br>命中判定的结果请传递给同名超类事件的该参数。 |

**说明**

命中判定

在对图层内的某一点进行命中判定 (命中测试) 时被调用。

命中判定的结果请传递给超类的该事件第 3 个参数
 (第 1 个参数与
第 2 个参数请原样传递)。

命中判定的结果为命中时，鼠标消息变为不透过，由该图层处理。

未命中时变为透过，鼠标消息由位于更后方的图层处理。

该事件在 [Layer.hitThreshold](Layer.md#hitthreshold) 与 [Layer.hitType](Layer.md#hittype) 所进行的
命中判定中判断为“命中”之后被调用。因此
在 Layer.hitThreshold 与 Layer.hitType 中判断为“未命中”时
不会调用该事件。

---

### onBlur

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `focused` | `&nbsp;` | 新获得焦点的图层对象。 |

**说明**

失去了焦点

图层失去焦点时被调用。

---

### onFocus

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `focused` | `&nbsp;` | 失去焦点的图层对象。 |
| `direction` | `&nbsp;` | 通过焦点的向后搜索更改焦点时为真，<br>通过焦点的向前搜索进行时为假。 |

**说明**

获得了焦点

图层获得焦点时被调用。

---

### onNodeDisabled

事件

**说明**

节点变为不可操作

由于该图层或该图层 (父子关系上) 上级图层的 [Layer.enabled](Layer.md#enabled) 属性
被更改，导致该图层变为不可操作时被调用。

---

### onNodeEnabled

事件

**说明**

节点变为可操作

由于该图层或该图层 (父子关系上) 上级图层的 [Layer.enabled](Layer.md#enabled) 属性
被更改，导致该图层变为可操作时被调用。

---

### onSearchPrevFocusable

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 要接收焦点的图层对象。<br>调用父类的同名方法时作为参数指定。<br>传入 null 时，按不存在可获取焦点的图层处理。 |

**说明**

可获取焦点的图层的向前搜索

进行可获取焦点的图层的向前搜索时发生的事件。

指定要接收焦点的图层时，请在超类的同名事件
的参数中指定该图层。

---

### onSearchNextFocusable

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 要接收焦点的图层对象。<br>调用父类的同名方法时作为参数指定。<br>传入 null 时，按不存在可获取焦点的图层处理。 |

**说明**

可获取焦点的图层的向后搜索

进行可获取焦点的图层的向后搜索时发生的事件。

指定要接收焦点的图层时，请在超类的同名事件
的参数中指定该图层。

---

### onBeforeFocus

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 要接收焦点的图层对象。<br>通常传递 this，但调用超类的同名事件时<br>如果指定不同的图层对象，就可以向该图层<br>传递焦点。 |
| `blurred` | `&nbsp;` | 将失去焦点的图层对象。 |
| `direction` | `&nbsp;` | 通过焦点的向后搜索更改焦点时为真，<br>通过焦点的向前搜索进行时为假。 |

**说明**

将要接收焦点之前

将要接收焦点之前发生的事件。

指定要接收焦点的图层时，可以在超类的同名事件
的第 1 个参数中指定该图层。

---

### onPaint

事件

**说明**

被绘制时

图层实际被绘制到窗口之前被调用。

本事件仅在 [Layer.callOnPaint](Layer.md#callonpaint) 属性为真时被调用，
Layer.callOnPaint 在本事件执行结束后会自动被设为假。

**相关:** [Layer.update](Layer.md#update)

---

### onTransitionCompleted

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dest` | `&nbsp;` | 转场目标的图层对象 (通常为 this) 会被传递。 |
| `src` | `&nbsp;` | 转场来源的图层对象会被传递。<br>根据转场的种类，也可能为 null。 |

**说明**

转场结束了

转场结束时被调用。

---

### onTouchDown

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 被触摸位置的 x 坐标 (客户端坐标中的) 值。 |
| `y` | `&nbsp;` | 被触摸位置的 y 坐标 (客户端坐标中的) 值。 |
| `cx` | `&nbsp;` | 手指接触的横向像素数。<br>设备不支持时始终为 1。 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数。<br>设备不支持时始终为 1。 |
| `id` | `&nbsp;` | 触摸 ID。<br>多点触控时，会为每个位置设置固有值，通过该 ID 可以识别位置。 |

**说明**

屏幕被触摸

在触摸面板上触摸时发生。

本事件在 X, Y 坐标位于该图层内时发生。

---

### onTouchUp

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 离开位置的 x 坐标 (客户端坐标中的) 值。 |
| `y` | `&nbsp;` | 离开位置的 y 坐标 (客户端坐标中的) 值。 |
| `cx` | `&nbsp;` | 手指接触的横向像素数。<br>设备不支持时始终为 1。 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数。<br>设备不支持时始终为 1。 |
| `id` | `&nbsp;` | 触摸 ID。<br>多点触控时，会为每个位置设置固有值，通过该 ID 可以识别位置。 |

**说明**

手指从屏幕离开

手指从触摸面板离开时发生。

本事件在 X, Y 坐标位于该图层内时发生。

不过，与鼠标不同，由于按当前坐标判定，可能与 onTouchDown 发生的图层不是同一个。

---

### onTouchMove

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 触摸位置的 x 坐标 (客户端坐标中的) 值。 |
| `y` | `&nbsp;` | 触摸位置的 y 坐标 (客户端坐标中的) 值。 |
| `cx` | `&nbsp;` | 手指接触的横向像素数。<br>设备不支持时始终为 1。 |
| `cy` | `&nbsp;` | 手指接触的纵向像素数。<br>设备不支持时始终为 1。 |
| `id` | `&nbsp;` | 触摸 ID。<br>多点触控时，会为每个位置设置固有值，通过该 ID 可以识别位置。 |

**说明**

手指移动了

在触摸面板上接触的手指移动时发生。

本事件在 X, Y 坐标位于该图层内时发生。

不过，与鼠标不同，由于按当前坐标判定，可能与 onTouchDown 发生的图层不是同一个。

---

### onTouchScaling

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `startdistance` | `&nbsp;` | 多点触控开始时的像素距离。 |
| `currentdistance` | `&nbsp;` | 事件发生时触摸的像素距离。 |
| `cx` | `&nbsp;` | 中心位置的 x 坐标。以该图层的局部坐标 (与 [onTouchDown](#ontouchdown) 相同) 传递。 |
| `cy` | `&nbsp;` | 中心位置的 y 坐标。坐标系与 cx 相同。 |
| `flag` | `&nbsp;` | 多点触控状态标志。<br>`**0x01**     : ` 设置在多点触控开始的最初事件上。 |

**说明**

进行了放大操作

在触摸面板上通过多点触控进行放大操作时发生。

本事件在有焦点的图层上发生。

距离 (startdistance / currentdistance) 是绘制区域上的像素距离，不会换算为图层坐标
(放大率请用 `currentdistance / startdistance` 的比求出)。
中心 (cx / cy) 在 2026-09-29 以前是按绘制区域坐标原样传递的。

---

### onTouchRotate

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `startangle` | `&nbsp;` | 多点触控开始时的弧度角。 |
| `currentangle` | `&nbsp;` | 事件发生时触摸的弧度角。 |
| `distance` | `&nbsp;` | 事件发生时触摸的像素距离。 |
| `cx` | `&nbsp;` | 中心位置的 x 坐标。以该图层的局部坐标 (与 [onTouchDown](#ontouchdown) 相同) 传递。 |
| `cy` | `&nbsp;` | 中心位置的 y 坐标。坐标系与 cx 相同。 |
| `flag` | `&nbsp;` | 多点触控状态标志。<br>`**0x01**     : ` 设置在多点触控开始的最初事件上。 |

**说明**

进行了旋转操作

在触摸面板上通过多点触控进行旋转操作时发生。

本事件在有焦点的图层上发生。

---

### onMultiTouch

事件

**说明**

多点触控状态发生了变化

多点触控状态开始、移动、离开时发生。

坐标信息可以通过 [Window.touchPointCount](Window.md#touchpointcount) 属性和 [Window.getTouchPoint](Window.md#gettouchpoint) 方法获取。

本事件在有焦点的图层上发生。

**相关:** [Window.getTouchPoint](Window.md#gettouchpoint) / [Window.touchPointCount](Window.md#touchpointcount)

---

## 插件扩展: krkr_richtext

图层被扩展了富文本绘制方法

### 成员列表

#### 属性

- [useCache](#usecache)

#### 方法

- [drawTextEx](#drawtextex)
- [drawParagraph](#drawparagraph)
- [drawStyledText](#drawstyledtext)
- [drawTextLayout](#drawtextlayout)
- [drawParagraphLayout](#drawparagraphlayout)
- [drawStyledLayout](#drawstyledlayout)
- [drawRectEx](#drawrectex)
- [clearCache](#clearcache)
- [setCacheMaxSize](#setcachemaxsize)

---

### useCache

属性 \ 访问: `r/w`

**说明**

字形缓存的使用与否

true (默认): 缓存字形以提高速度
false: 每次渲染

---

### drawTextEx

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 要绘制的文本 |
| `x` | `&nbsp;` | 绘制开始 X 坐标 |
| `y` | `&nbsp;` | 绘制开始 Y 坐标（基线位置） |
| `style` | `&nbsp;` | RichText.Style 对象 |
| `appearance` | `&nbsp;` | RichText.Appearance 对象 |

**返回值**

绘制区域的数组 [x, y, width, height]

**说明**

绘制单行文本

基本的单行文本绘制。不会自动换行。

注意: 为避免与吉里吉里标准的 Layer.drawText() 名称冲突，
TJS 侧的名称是 drawTextEx。

使用示例:
var style = new RichText.Style();
style.setFonts(["MSゴシック"]);
style.fontSize = 24;

var app = new RichText.Appearance();
app.addFill(0xFFFFFFFF);

var rect = layer.drawTextEx("Hello World", 10, 50, style, app);

---

### drawParagraph

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 要绘制的文本 |
| `x` | `&nbsp;` | 绘制区域的左端 |
| `y` | `&nbsp;` | 绘制区域的上端 |
| `width` | `&nbsp;` | 绘制区域的宽度 |
| `height` | `&nbsp;` | 绘制区域的高度 |
| `hAlign` | `&nbsp;` | 水平对齐 (RichText.HALIGN_LEFT/CENTER/RIGHT) |
| `vAlign` | `&nbsp;` | 垂直对齐 (RichText.VALIGN_TOP/MIDDLE/BOTTOM) |
| `style` | `&nbsp;` | RichText.Style 对象 |
| `appearance` | `&nbsp;` | RichText.Appearance 对象 |

**返回值**

实际绘制区域的数组 [x, y, width, height]

**说明**

绘制段落（多行文本）

在指定的矩形区域内自动换行并绘制文本。

使用示例:
var rect = layer.drawParagraph(
"长文本会自动\n换行。",
10, 10, 300, 200,
RichText.HALIGN_LEFT,
RichText.VALIGN_TOP,
style, app
);

---

### drawStyledText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 带样式标签的文本 |
| `x` | `&nbsp;` | 绘制区域的左端 |
| `y` | `&nbsp;` | 绘制区域的上端 |
| `width` | `&nbsp;` | 绘制区域的宽度 |
| `height` | `&nbsp;` | 绘制区域的高度 |
| `hAlign` | `&nbsp;` | 水平对齐 (RichText.HALIGN_LEFT/CENTER/RIGHT) |
| `vAlign` | `&nbsp;` | 垂直对齐 (RichText.VALIGN_TOP/MIDDLE/BOTTOM) |
| `styles` | `&nbsp;` | 单个 Style，或样式名 → Style 的字典 |
| `appearances` | `&nbsp;` | 单个 Appearance，或样式名 → Appearance 的字典 |
| `lineSpacing` | `0` | 行距（省略时为 0） |

**返回值**

实际绘制区域的数组 [x, y, width, height]

**说明**

绘制带样式标签的文本

一边用 <style:名称> 标签切换样式一边绘制文本。
向 styles / appearances 传入单个对象时，会被当作 "default" 键处理。

使用示例:
// 用单个样式绘制
layer.drawStyledText(
"文本",
10, 10, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
style, app
);

// 用多个样式绘制
var styles = %[ "default": normalStyle, "bold": boldStyle ];
var apps = %[ "default": normalApp, "bold": boldApp ];
layer.drawStyledText(
"普通<style:bold>粗体</style>普通",
10, 10, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
styles, apps
);

---

### drawTextLayout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `textLayout` | `&nbsp;` | RichText.Layout 对象（已 layout()） |
| `x` | `&nbsp;` | 绘制开始 X 坐标 |
| `y` | `&nbsp;` | 绘制开始 Y 坐标（基线位置） |
| `appearance` | `&nbsp;` | RichText.Appearance 对象 |
| `maxChars` | `-1` | 绘制的字符数上限（-1 为全部，省略时: -1） |

**返回值**

绘制区域的数组 [x, y, width, height]

**说明**

绘制已完成布局的 TextLayout

绘制事先完成布局计算的 Layout。
可用于同一布局的重绘。

使用示例:
var tl = new RichText.Layout();
tl.layout("Hello World", style);
layer.drawTextLayout(tl, 10, 50, appearance);

---

### drawParagraphLayout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `paraLayout` | `&nbsp;` | RichText.ParagraphLayout 对象（已 layout()） |
| `x` | `&nbsp;` | 绘制区域的左端 |
| `y` | `&nbsp;` | 绘制区域的上端 |
| `width` | `&nbsp;` | 绘制区域的宽度 |
| `height` | `&nbsp;` | 绘制区域的高度 |
| `hAlign` | `&nbsp;` | 水平对齐 (RichText.HALIGN_LEFT/CENTER/RIGHT) |
| `vAlign` | `&nbsp;` | 垂直对齐 (RichText.VALIGN_TOP/MIDDLE/BOTTOM) |
| `style` | `&nbsp;` | RichText.Style 对象 |
| `appearance` | `&nbsp;` | RichText.Appearance 对象 |
| `maxChars` | `-1` | 绘制的字符数上限（-1 为全部，省略时: -1） |

**返回值**

实际绘制区域的数组 [x, y, width, height]

**说明**

绘制已完成布局的 ParagraphLayout

绘制事先完成布局计算的 ParagraphLayout。
通过指定 maxChars 可以实现逐次显示（字符送进）。

使用示例:
var pl = new RichText.ParagraphLayout();
pl.layout("长文本...", 300, style);

layer.drawParagraphLayout(pl, 10, 10, 300, 200,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
style, app);

// 字符送进（只绘制前 5 个字符）
layer.drawParagraphLayout(pl, 10, 10, 300, 200,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
style, app, 5);

---

### drawStyledLayout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `styledLayout` | `&nbsp;` | RichText.StyledLayout 对象 |
| `x` | `&nbsp;` | 绘制 X 坐标 |
| `y` | `&nbsp;` | 绘制 Y 坐标 |
| `maxChars` | `-1` | 绘制的字符数上限（-1 为全部，省略时: -1） |

**返回值**

实际绘制区域的数组 [x, y, width, height]

**说明**

绘制已完成布局的 StyledLayout

绘制事先完成布局计算的 StyledLayout。
通过指定 maxChars 可以实现字符送进动画。

使用示例:
var sl = new RichText.StyledLayout();
sl.layout(text, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
style, app);

// 全部绘制
layer.drawStyledLayout(sl, 10, 10);

// 字符送进（只绘制前 5 个字符）
layer.drawStyledLayout(sl, 10, 10, 5);

---

### drawRectEx

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X 坐标 |
| `y` | `&nbsp;` | Y 坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `fillColor` | `0` | 填充色（ARGB，省略时: 0） |
| `strokeColor` | `0` | 描边色（ARGB，0 为无效，省略时: 0） |
| `strokeWidth` | `0` | 描边宽度（省略时: 0） |

**说明**

绘制矩形

注意: 为避免与吉里吉里标准的 Layer.drawRect() 名称冲突，
TJS 侧的名称是 drawRectEx。

使用示例:
layer.drawRectEx(10, 10, 200, 100, 0x80FF0000);  // 半透明的红色矩形
layer.drawRectEx(10, 10, 200, 100, 0, 0xFF000000, 2);  // 仅黑色边框

---

### clearCache

方法

**说明**

缓存的清除

---

### setCacheMaxSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bytes` | `&nbsp;` | 最大字节数 |

**说明**

设置缓存的最大大小

---

## 插件扩展: layerExAreaAverage

基于伪代码的手册

图层被扩展了基于面积平均法的图像缩小绘制方法

### 成员列表

---

## 插件扩展: layerExBTOA

基于伪代码的手册

### 成员列表

#### 方法

- [copyRightBlueToLeftAlpha](#copyrightbluetoleftalpha)
- [copyBottomBlueToTopAlpha](#copybottombluetotopalpha)
- [fillAlpha](#fillalpha)
- [copyAlphaToProvince](#copyalphatoprovince)
- [clipAlphaRect](#clipalpharect)
- [overwrapRect](#overwraprect)
- [fillByProvince](#fillbyprovince)
- [fillToProvince](#filltoprovince)

---

### copyRightBlueToLeftAlpha

方法

**说明**

将图层右半部分的 Blue CHANNEL 复制到左半部分的 Alpha CHANNEL

※不支持裁剪

---

### copyBottomBlueToTopAlpha

方法

**说明**

将图层下半部分的 Blue CHANNEL 复制到上半部分的 Alpha CHANNEL

※不支持裁剪

---

### fillAlpha

方法

**说明**

将图层的 Alpha CHANNEL 填充为 0xff

---

### copyAlphaToProvince

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `threshold` | `&nbsp;` | 阈值。省略时为 void 则原样复制<br>指定数值时，Alpha 为阈值以上则填充为 matched，否则填充为 otherwise |
| `matched` | `1` | 指定 threshold 时，对阈值以上填充的值。设为 0-255 范围外则不填充 |
| `otherwise` | `0` | 指定 threshold 时，对低于阈值填充的值。设为 0-255 范围外则不填充 |

**说明**

将图层的 Alpha CHANNEL 复制到 Province Image（区域图像）

---

### clipAlphaRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 左端位置 |
| `dtop` | `&nbsp;` | 上端位置 |
| `src` | `&nbsp;` | 持有用于乘法的 α 的源图像 |
| `sleft` | `&nbsp;` | 源图像的左端位置 |
| `stop` | `&nbsp;` | 源图像的上端位置 |
| `swidth` | `&nbsp;` | 源图像的宽度 |
| `sheight` | `&nbsp;` | 源图像的高度 |
| `clear` | `&nbsp;` | 用该值（opacity）填充运算范围外的区域<br>省略时或不是 0-255 的值时不填充 |

**说明**

将图层的 Alpha CHANNEL 与 src 的 Alpha CHANNEL 相乘

---

### overwrapRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 左端位置 |
| `dtop` | `&nbsp;` | 上端位置 |
| `src` | `&nbsp;` | 持有用于乘法的 α 的源图像 |
| `sleft` | `&nbsp;` | 源图像的左端位置 |
| `stop` | `&nbsp;` | 源图像的上端位置 |
| `swidth` | `&nbsp;` | 源图像的宽度 |
| `sheight` | `&nbsp;` | 源图像的高度 |
| `threshold` | `1` | 阈值 |

**说明**

将 src 叠加到图层上（但 src 的 Alpha CHANNEL < 阈值的除外） / 由于在使用 SSE 时会出现 operateRect 的 omAlpha 不能变为正确值的情况

---

### fillByProvince

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 区域图像的索引值 (0~255) |
| `color` | `&nbsp;` | 要填充的颜色 (0xAARRGGBB) |

**说明**

将区域图像中为指定值的场所用指定的颜色填充

---

### fillToProvince

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 填充对象的颜色 (0xRRGGBB) |
| `index` | `&nbsp;` | 区域图像的索引值 (0~255) |
| `threshold` | `64` | Alpha 阈值 (0-255，指定值以上匹配) |

**说明**

将匹配特定颜色的像素用区域图像的指定索引填充

---

## 插件扩展: layerExDraw

图层被扩展了矢量绘制方法

・绘制处理会按图层上设置的裁剪区域进行裁剪。

### 成员列表

#### 属性

- [updateWhenDraw](#updatewhendraw)
- [smoothingMode](#smoothingmode)
- [textRenderingHint](#textrenderinghint)
- [record](#record)

#### 方法

- [setTransform](#settransform)
- [resetTransform](#resettransform)
- [rotateTransform](#rotatetransform)
- [scaleTransform](#scaletransform)
- [translateTransform](#translatetransform)
- [setResolution](#setresolution)
- [clear](#clear)
- [drawPath](#drawpath)
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
- [drawPathString](#drawpathstring)
- [drawString](#drawstring)
- [measureString](#measurestring)
- [measureStringInternal](#measurestringinternal)
- [drawImage](#drawimage)
- [drawImageRect](#drawimagerect)
- [drawImageStretch](#drawimagestretch)
- [drawImageAffine](#drawimageaffine)
- [setViewTransform](#setviewtransform)
- [resetViewTransform](#resetviewtransform)
- [rotateViewTransform](#rotateviewtransform)
- [scaleViewTransform](#scaleviewtransform)
- [translateViewTransform](#translateviewtransform)
- [saveRecord](#saverecord)
- [loadRecord](#loadrecord)
- [getRecordImage](#getrecordimage)
- [saveImage](#saveimage)
- [getColorRegionRects](#getcolorregionrects)

#### 常量

- [EncoderValueCompressionLZW](#encodervaluecompressionlzw)
- [EncoderValueCompressionCCITT3](#encodervaluecompressionccitt3)
- [EncoderValueCompressionCCITT4](#encodervaluecompressionccitt4)
- [EncoderValueCompressionRle](#encodervaluecompressionrle)
- [EncoderValueCompressionNone](#encodervaluecompressionnone)
- [EncoderValueScanMethodInterlaced](#encodervaluescanmethodinterlaced)
- [EncoderValueScanMethodNonInterlaced](#encodervaluescanmethodnoninterlaced)
- [EncoderValueVersionGif87](#encodervalueversiongif87)
- [EncoderValueVersionGif89](#encodervalueversiongif89)
- [EncoderValueRenderProgressive](#encodervaluerenderprogressive)
- [EncoderValueRenderNonProgressive](#encodervaluerendernonprogressive)
- [EncoderValueTransformRotate90](#encodervaluetransformrotate90)
- [EncoderValueTransformRotate180](#encodervaluetransformrotate180)
- [EncoderValueTransformRotate270](#encodervaluetransformrotate270)
- [EncoderValueTransformFlipHorizontal](#encodervaluetransformfliphorizontal)
- [EncoderValueTransformFlipVertical](#encodervaluetransformflipvertical)

---

### updateWhenDraw

属性 \ 访问: `r/w`

**说明**

绘制时是否对该区域调用 update()

---

### smoothingMode

属性 \ 访问: `r/w`

**说明**

绘制的抗锯齿指定 (SmoothingMode) @description 默认为 SmoothingModeAntiAlias

---

### textRenderingHint

属性 \ 访问: `r/w`

**说明**

文本绘制的渲染指定 (TextRenderingHint) @description 默认为 TextRenderingHintAntiAlias

---

### record

属性 \ 访问: `r/w`

**说明**

是否记录由该插件进行的绘制内容

当 record = true 的状态下，指定 viewTransform 时
会按绘制内容原样重绘。
------------------------------------------------ 图元文件操作 ------------------------------------------------

---

### setTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |

**说明**

指定绘制时的变换

---

### resetTransform

方法

---

### rotateTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

---

### scaleTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |

---

### translateTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### setResolution

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `resx` | `&nbsp;` | 横向分辨率 % 指定 |
| `resy` | `&nbsp;` | 纵向分辨率 % 指定 |

**说明**

分辨率指定

---

### clear

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `argb` | `&nbsp;` | 清除色 |

**说明**

画面的清除

---

### drawPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `path` | `&nbsp;` | 路径。指定 GdiPlus.Path |

**返回值**

更新区域信息的字典 left, top, width, height

**说明**

路径的绘制

---

### drawArc

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**返回值**

更新区域信息的字典 left, top, width, height

**说明**

圆弧的绘制

---

### drawPie

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**返回值**

更新区域信息 (RectF)

**说明**

扇形的绘制

---

### drawBezier

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

贝塞尔曲线的绘制

---

### drawBeziers

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

连续贝塞尔曲线的绘制

---

### drawClosedCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

封闭基数样条的绘制

---

### drawClosedCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**返回值**

更新区域信息 (RectF)

**说明**

封闭基数样条的绘制

---

### drawCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

基数样条的绘制

---

### drawCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**返回值**

更新区域信息 (RectF)

**说明**

基数样条的绘制

---

### drawCurve3

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | 张力 |

**返回值**

更新区域信息 (RectF)

**说明**

基数样条的绘制

---

### drawEllipse

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

椭圆的绘制

---

### drawLine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x1` | `&nbsp;` | 起点 X 坐标 |
| `y1` | `&nbsp;` | 起点 Y 坐标 |
| `x2` | `&nbsp;` | 终点 X 坐标 |
| `y2` | `&nbsp;` | 终点 Y 坐标 |

**返回值**

更新区域信息 (RectF)

**说明**

线段的绘制

---

### drawLines

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

连续线段的绘制

---

### drawPolygon

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

多边形的绘制

---

### drawRectangle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

矩形的绘制

---

### drawRectangles

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `rects` | `&nbsp;` | 矩形的数组 [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

多个矩形的绘制

---

### drawPathString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `font` | `&nbsp;` | 字体。用 GdiPlus.Font 指定字体 |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` | 绘制位置 X |
| `y` | `&nbsp;` | 绘制位置 Y |
| `text` | `&nbsp;` | 要绘制的文本 |

**返回值**

更新区域信息 (RectF)

**说明**

基于路径的字符串绘制

---

### drawString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `font` | `&nbsp;` | 字体。用 GdiPlus.Font 指定字体 |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式。※只参照画笔 |
| `x` | `&nbsp;` | 绘制位置 X |
| `y` | `&nbsp;` | 绘制位置 Y |
| `text` | `&nbsp;` | 要绘制的文本 |

**返回值**

更新区域信息 (RectF)

**说明**

字符串的绘制。绘制质量遵循 textRenderingHint。

-------------------------------------------------------------

---

### measureString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `font` | `&nbsp;` | 字体 |
| `text` | `&nbsp;` | 要绘制的文本 |

**返回值**

绘制区域信息 (RectF)

**说明**

获取字符串的绘制区域信息。绘制质量遵循 textRenderingHint

---

### measureStringInternal

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `font` | `&nbsp;` | 字体 |
| `text` | `&nbsp;` | 要绘制的文本 |

**返回值**

绘制区域信息 (RectF)

**说明**

获取字符串的绘制区域信息。对于 measureString() 获取的区域，返回去除边距后字符串实际存在区域的矩形。

---

### drawImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` |  |
| `dtop` | `&nbsp;` |  |
| `src` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

图像的绘制。复制目标为考虑了原图像 Bounds 的位置，大小按 Pixel 指定。

-------------------------------------------------------------

---

### drawImageRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 复制目标左端 |
| `dtop` | `&nbsp;` | 复制目标上端 |
| `src` | `&nbsp;` | 复制源图像(Image/Layer/文件名) |
| `sleft` | `&nbsp;` | 原矩形的左端 |
| `stop` | `&nbsp;` | 原矩形的上端 |
| `swidth` | `&nbsp;` | 原矩形的宽度 |
| `sheight` | `&nbsp;` | 原矩形的高度 |

**返回值**

更新区域信息 (RectF)

**说明**

图像的矩形复制

---

### drawImageStretch

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 复制目标左端 |
| `dtop` | `&nbsp;` | 复制目标上端 |
| `dwidth` | `&nbsp;` | 复制目标的宽度 |
| `dheight` | `&nbsp;` | 复制目标的高度 |
| `src` | `&nbsp;` | 复制源图像(Image/Layer/文件名) |
| `sleft` | `&nbsp;` | 原矩形的左端 |
| `stop` | `&nbsp;` | 原矩形的上端 |
| `swidth` | `&nbsp;` | 原矩形的宽度 |
| `sheight` | `&nbsp;` | 原矩形的高度 |

**返回值**

更新区域信息 (RectF)

**说明**

图像的缩放复制

---

### drawImageAffine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 复制源图像(Image/Layer/文件名) |
| `sleft` | `&nbsp;` | 原矩形的左端 |
| `stop` | `&nbsp;` | 原矩形的上端 |
| `swidth` | `&nbsp;` | 原矩形的宽度 |
| `sheight` | `&nbsp;` | 原矩形的高度 |
| `affine` | `&nbsp;` | 仿射参数的种类 (true:变换矩阵, false:坐标指定), |
| `A` | `&nbsp;` |  |
| `B` | `&nbsp;` |  |
| `C` | `&nbsp;` |  |
| `D` | `&nbsp;` |  |
| `E` | `&nbsp;` |  |
| `F` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

图像的仿射变换复制

---

### setViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |

**说明**

指定记录内容显示时的变换

---

### resetViewTransform

方法

---

### rotateViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

---

### scaleViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |

---

### translateViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### saveRecord

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 保存文件名 |

**返回值**

成功时返回 true

**说明**

记录内容的保存

---

### loadRecord

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 读取文件名 |

**返回值**

成功时返回 true

**说明**

记录内容的读取

---

### getRecordImage

方法

**说明**

以 Image 形式返回记录内容

返回 Image 对象

---

### saveImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |
| `mime` | `&nbsp;` | 要保存的图像格式 image/jpeg, image/png, image/gif 等 |
| `param` | `void` | 编码参数(字典)<br>compression, scanmethod, version, render, transform, quality(0~100), depth(1,4,8,24,32) |

**说明**

图像的保存

---

### getColorRegionRects

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 颜色指定 |

**返回值**

矩形的数组

**说明**

返回包含指定颜色区域的 region

-------------------------------------------------------------

---

### EncoderValueCompressionLZW

常量

**说明**

用于 compression

---

### EncoderValueCompressionCCITT3

常量

---

### EncoderValueCompressionCCITT4

常量

---

### EncoderValueCompressionRle

常量

---

### EncoderValueCompressionNone

常量

---

### EncoderValueScanMethodInterlaced

常量

**说明**

用于 scanmethod

---

### EncoderValueScanMethodNonInterlaced

常量

---

### EncoderValueVersionGif87

常量

**说明**

用于 version

---

### EncoderValueVersionGif89

常量

---

### EncoderValueRenderProgressive

常量

**说明**

用于 render

---

### EncoderValueRenderNonProgressive

常量

---

### EncoderValueTransformRotate90

常量

**说明**

用于 transform

---

### EncoderValueTransformRotate180

常量

---

### EncoderValueTransformRotate270

常量

---

### EncoderValueTransformFlipHorizontal

常量

---

### EncoderValueTransformFlipVertical

常量

---

## 插件扩展: layerExImage

基于伪代码的手册

### 成员列表

#### 方法

- [light](#light)
- [colorize](#colorize)
- [modulate](#modulate)
- [noise](#noise)
- [generateWhiteNoise](#generatewhitenoise)

---

### light

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `brightness` | `&nbsp;` | 亮度 -255 ~ 255，为负数时变暗 |
| `contrast` | `&nbsp;` | 对比度 -100 ~ 100，为 0 时不变 |

**说明**

亮度与对比度

---

### colorize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hue` | `&nbsp;` | 色相 |
| `sat` | `&nbsp;` | 彩度 |
| `blend` | `&nbsp;` | 混合 0 (无效果) ~ 1 (full effect) |

**说明**

色相与彩度

---

### modulate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hue` | `&nbsp;` | 色相 -180~180 (度) |
| `saturation` | `&nbsp;` | 彩度 -100~100 (%) |
| `luminance` | `&nbsp;` | 亮度 -100~100 (%) |

**说明**

色相、彩度与亮度的更改

---

### noise

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `level` | `&nbsp;` | 噪点级别 0 (no noise) ~ 255 (lot of noise)。 |

**说明**

噪点添加

---

### generateWhiteNoise

方法

**说明**

噪点生成（忽略原图像，绘制灰度的白噪声／维护 α 信息）

---

## 插件扩展: layerExLongExposure

基于伪代码的手册

Layer 扩展

### 成员列表

#### 方法

- [initExposure](#initexposure)
- [snapExposure](#snapexposure)
- [statExposure](#statexposure)
- [copyExposure](#copyexposure)
- [termExposure](#termexposure)

---

### initExposure

方法

**说明**

初始化

以当前图层大小初始化总和缓冲区

---

### snapExposure

方法

**说明**

将当前图像加到总和缓冲区

必须与 init 时图像大小相同（不同则为异常）

---

### statExposure

方法

**返回值**

%[ min_r, max_r,
min_g, max_g,
min_b, max_b,
min_a, max_a ];

**说明**

获取总和缓冲区的最大值／最小值

---

### copyExposure

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `stat` | `&nbsp;` | : 用于截断的信息字典／为 void 时隐式执行 statExposure 并使用其值<br>自身会作为各元素的 min~max 为 0~255 的图像被改写<br>各元素中 min >= max 时始终返回 0xFF |

**说明**

从总和缓冲区创建图像

---

### termExposure

方法

**说明**

总和缓冲区销毁

销毁已分配的缓冲区
invalidate 时也会自动销毁

---

## 插件扩展: layerExRaster

基于伪代码的手册

图层被扩展了类似光栅处理风格的复制绘制方法

### 成员列表

#### 方法

- [copyRaster](#copyraster)

---

### copyRaster

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 绘制源图层。如果不是与自己相同的大小，则不进行处理。 |
| `maxh` | `&nbsp;` | 最大振幅(pixel) |
| `lines` | `&nbsp;` |  |
| `cycle` | `&nbsp;` | 周期指定(msec) |
| `time` | `&nbsp;` | 当前时刻 |

**说明**

光栅复制处理

---

## 插件扩展: layerExSave

图层扩展

### 成员列表

#### 方法

- [saveLayerImageTlg5](#savelayerimagetlg5)
- [saveLayerImagePng](#savelayerimagepng)
- [saveLayerImagePngOctet](#savelayerimagepngoctet)
- [saveProvinceImage](#saveprovinceimage)
- [getCropRect](#getcroprect)
- [getCropRectZero](#getcroprectzero)
- [getDiffRect](#getdiffrect)
- [getDiffPixel](#getdiffpixel)
- [oozeColor](#oozecolor)
- [copyBlueToAlpha](#copybluetoalpha)
- [isBlank](#isblank)
- [clearAlpha](#clearalpha)
- [getAverageColor](#getaveragecolor)
- [getFingerPrintValue](#getfingerprintvalue)
- [getShrinkVectorOctet](#getshrinkvectoroctet)

---

### saveLayerImageTlg5

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |
| `tags` | `void` | 标签信息 |

**说明**

以 TLG5 形式保存图像。注意点:数据保存完成之前处理不会返回。

---

### saveLayerImagePng

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |
| `tags` | `void` | 记述标签信息与压缩级别(comp_lv)的字典 |

**说明**

以 PNG 形式保存图像。注意点:数据保存完成之前处理不会返回。

---

### saveLayerImagePngOctet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `compression_level_or_tags` | `1` | 压缩率或标签信息字典(省略时为 1) |

**说明**

以 octet 返回 PNG 形式图像。注意点:数据保存完成之前处理不会返回。

标签信息字典与 saveLayerImagePng 相同形式（可用 comp_lv 指定压缩率）

---

### saveProvinceImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |
| `palette` | `void` | 调色板信息（※将来预留／当前未实现） |

**说明**

保存 Province 图像(格式：固定为 256 调色板式 PNG)　※仅在 LodePNG 实现模式下有效

没有 Province 图像时为异常（在从未用 dfProvince 绘制过的图层等中发生）

---

### getCropRect

方法

**返回值**

%[ x, y, w, h] 形式的字典，或 void（全部透明时）

**说明**

获取裁剪图层图像（切去上下左右的空白透明部分）后的

尺寸。

---

### getCropRectZero

方法

**返回值**

%[ x, y, w, h] 形式的字典，或 void（全部透明时）

**说明**

获取裁剪图层图像（切去上下左右的完全透明部分(0x00000000)）后的

尺寸。

---

### getDiffRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `base` | `&nbsp;` | 作为差分来源的基准图像 |

**返回值**

%[ x, y, w, h ] 形式的字典，或 void（完全相同的图像时）
（base 不与实例自身大小相同则抛出异常）

**说明**

获取图层的差分区域。

---

### getDiffPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `base` | `&nbsp;` | 作为差分来源的基准图像 |
| `samecol` | `&nbsp;` | 相同时填充的颜色(0xAARRGGBB)（为 void 或省略则不填充） |
| `diffcol` | `&nbsp;` | 不同时填充的颜色(0xAARRGGBB)（为 void 或省略则不填充）<br>@description（base 不与实例自身大小相同则抛出异常） |

**说明**

进行图层的像素比较。

---

### oozeColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `level` | `&nbsp;` | 进行处理的次数。越大拉伸区域越多 |
| `threshold` | `1` | Alpha 阈值(1~255)。向低于此值的像素拉伸 |
| `fillColor` | `0` | 处理区域以外的填充色(0xRRGGBB) |

**说明**

将图层边缘的颜色拉伸到透明部分（防止缩小时出现伪色）

---

### copyBlueToAlpha

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 复制源图层 |

**说明**

将图层的 Blue CHANNEL 复制到 Alpha 区域

---

### isBlank

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**返回值**

是空白数据则返回 true

**说明**

确认图层的指定区域是否为空白数据

---

### clearAlpha

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `threthold` | `0` | α 的下限 |
| `fillColor` | `0` | 填充色(0x00RRGGBB) |

**说明**

将 α 为指定值以下的部分用指定颜色填充

---

### getAverageColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

返回图层指定区域的平均颜色

---

### getFingerPrintValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ignore_transparent` | `true` | : 忽略完全透明的 RGB 值 |

**返回值**

64bit 哈希值

**说明**

返回图层 dfMain 图像的哈希值

哈希也会考虑 imageWidth/Height／即使值相同，也请使用 getDiffPixel 等进行严格比较

---

### getShrinkVectorOctet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `w` | `16` |  |
| `h` | `16` |  |

**返回值**

矢量 octet

**说明**

返回图层图像的缩小矢量 octet

---

## 插件扩展: layerExVector

图层被扩展了矢量绘制方法

・绘制处理会按图层上设置的裁剪区域进行裁剪。

### 成员列表

#### 属性

- [updateWhenDraw](#updatewhendraw)
- [smoothingMode](#smoothingmode)

#### 方法

- [setViewTransform](#setviewtransform)
- [resetViewTransform](#resetviewtransform)
- [rotateViewTransform](#rotateviewtransform)
- [scaleViewTransform](#scaleviewtransform)
- [translateViewTransform](#translateviewtransform)
- [setTransform](#settransform)
- [resetTransform](#resettransform)
- [rotateTransform](#rotatetransform)
- [scaleTransform](#scaletransform)
- [translateTransform](#translatetransform)
- [clear](#clear)
- [drawPath](#drawpath)
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
- [drawString](#drawstring)
- [drawStringArea](#drawstringarea)
- [drawImage](#drawimage)
- [drawImageRect](#drawimagerect)
- [drawImageStretch](#drawimagestretch)
- [drawImageAffine](#drawimageaffine)

---

### updateWhenDraw

属性 \ 访问: `r/w`

**说明**

绘制时是否对该区域调用 update()

---

### smoothingMode

属性 \ 访问: `r/w`

**说明**

绘制的抗锯齿指定(为兼容性而保留)

---

### setViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |

**说明**

指定显示变换

---

### resetViewTransform

方法

---

### rotateViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

---

### scaleViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |

---

### translateViewTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### setTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `matrix` | `&nbsp;` |  |

**说明**

指定绘制时的变换

---

### resetTransform

方法

---

### rotateTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

---

### scaleTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sx` | `&nbsp;` |  |
| `sy` | `&nbsp;` |  |

---

### translateTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |

---

### clear

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `argb` | `&nbsp;` | 清除色 |

**说明**

画面的清除

---

### drawPath

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `path` | `&nbsp;` | 路径。指定 GdiPlus.Path |

**返回值**

更新区域信息 (RectF)

**说明**

路径的绘制

---

### drawArc

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**返回值**

更新区域信息 (RectF)

**说明**

圆弧的绘制

---

### drawPie

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` | 左上角坐标 |
| `y` | `&nbsp;` | 左上角坐标 |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `startAngle` | `&nbsp;` | 顺时针方向的圆弧起始位置 |
| `sweepAngle` | `&nbsp;` | 绘制角度 |

**返回值**

更新区域信息 (RectF)

**说明**

扇形的绘制

---

### drawBezier

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x1` | `&nbsp;` |  |
| `y1` | `&nbsp;` |  |
| `x2` | `&nbsp;` |  |
| `y2` | `&nbsp;` |  |
| `x3` | `&nbsp;` |  |
| `y3` | `&nbsp;` |  |
| `x4` | `&nbsp;` |  |
| `y4` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

贝塞尔曲线的绘制

---

### drawBeziers

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

连续贝塞尔曲线的绘制

---

### drawClosedCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

封闭基数样条的绘制

---

### drawClosedCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**返回值**

更新区域信息 (RectF)

**说明**

封闭基数样条的绘制

---

### drawCurve

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

基数样条的绘制

---

### drawCurve2

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `tension` | `&nbsp;` | 张力 |

**返回值**

更新区域信息 (RectF)

**说明**

基数样条的绘制

---

### drawCurve3

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |
| `offset` | `&nbsp;` |  |
| `numberOfSegments` | `&nbsp;` |  |
| `tension` | `&nbsp;` | 张力 |

**返回值**

更新区域信息 (RectF)

**说明**

基数样条的绘制

---

### drawEllipse

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

椭圆的绘制

---

### drawLine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x1` | `&nbsp;` | 起点 X 坐标 |
| `y1` | `&nbsp;` | 起点 Y 坐标 |
| `x2` | `&nbsp;` | 终点 X 坐标 |
| `y2` | `&nbsp;` | 终点 Y 坐标 |

**返回值**

更新区域信息 (RectF)

**说明**

线段的绘制

---

### drawLines

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

连续线段的绘制

---

### drawPolygon

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `points` | `&nbsp;` | 点的数组 [ [x1, y1], [x2, y2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

多边形的绘制

---

### drawRectangle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

矩形的绘制

---

### drawRectangles

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `app` | `&nbsp;` | 外观 |
| `rects` | `&nbsp;` | 矩形的数组 [ [x1, y1, width1, height1], [x2, y2, width2, height2] .... ] |

**返回值**

更新区域信息 (RectF)

**说明**

多个矩形的绘制

---

### drawString

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `font` | `&nbsp;` | 字体。用 GdiPlus.Font 指定字体 |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` | 绘制位置 X |
| `y` | `&nbsp;` | 绘制位置 Y |
| `text` | `&nbsp;` | 要绘制的文本 |

**返回值**

更新区域信息 (RectF)

**说明**

字符串的绘制

---

### drawStringArea

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `font` | `&nbsp;` | 字体。用 GdiPlus.Font 指定字体 |
| `app` | `&nbsp;` | 外观。用 GdiPlus.Appearance 指定绘制样式 |
| `x` | `&nbsp;` | 矩形左端 |
| `y` | `&nbsp;` | 矩形上端 |
| `w` | `&nbsp;` | 矩形宽度 |
| `h` | `&nbsp;` | 矩形高度 |
| `alignX` | `&nbsp;` | 水平对齐 (0=左, 0.5=中央, 1=右) |
| `alignY` | `&nbsp;` | 垂直对齐 (0=上, 0.5=中央, 1=下) |
| `wrap` | `&nbsp;` | 单词换行模式 (0=None, 1=Char, 2=Word, 3=MixedWrap, 4=Ellipsis) |
| `text` | `&nbsp;` | 要绘制的文本 |

**返回值**

更新区域信息 (RectF)

**说明**

向矩形区域内绘制字符串

---

### drawImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 复制目标原点 X |
| `y` | `&nbsp;` | 复制目标原点 Y |
| `image` | `&nbsp;` | 复制源图像(Image/文件名) |

**返回值**

更新区域信息 (RectF)

**说明**

图像的绘制。复制目标为考虑了原图像 Bounds 的位置，大小按 Pixel 指定。

-------------------------------------------------------------

---

### drawImageRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 复制目标左端 |
| `dtop` | `&nbsp;` | 复制目标上端 |
| `src` | `&nbsp;` | 复制源图像(Image/文件名) |
| `sleft` | `&nbsp;` | 原矩形的左端 |
| `stop` | `&nbsp;` | 原矩形的上端 |
| `swidth` | `&nbsp;` | 原矩形的宽度 |
| `sheight` | `&nbsp;` | 原矩形的高度 |

**返回值**

更新区域信息 (RectF)

**说明**

图像的矩形复制

---

### drawImageStretch

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 复制目标左端 |
| `dtop` | `&nbsp;` | 复制目标上端 |
| `dwidth` | `&nbsp;` | 复制目标的宽度 |
| `dheight` | `&nbsp;` | 复制目标的高度 |
| `src` | `&nbsp;` | 复制源图像(Image/文件名) |
| `sleft` | `&nbsp;` | 原矩形的左端 |
| `stop` | `&nbsp;` | 原矩形的上端 |
| `swidth` | `&nbsp;` | 原矩形的宽度 |
| `sheight` | `&nbsp;` | 原矩形的高度 |

**返回值**

更新区域信息 (RectF)

**说明**

图像的缩放复制

---

### drawImageAffine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 复制源图像(Image/文件名) |
| `sleft` | `&nbsp;` | 原矩形的左端 |
| `stop` | `&nbsp;` | 原矩形的上端 |
| `swidth` | `&nbsp;` | 原矩形的宽度 |
| `sheight` | `&nbsp;` | 原矩形的高度 |
| `affine` | `&nbsp;` | 仿射参数的种类(true:变换矩阵, false:坐标指定) |
| `A` | `&nbsp;` |  |
| `B` | `&nbsp;` |  |
| `C` | `&nbsp;` |  |
| `D` | `&nbsp;` |  |
| `E` | `&nbsp;` |  |
| `F` | `&nbsp;` |  |

**返回值**

更新区域信息 (RectF)

**说明**

图像的仿射变换复制

---

## 插件扩展: shrinkCopy

基于伪代码的手册

Layer 扩展

### 成员列表

#### 方法

- [shrinkCopy](#shrinkcopy)
- [shrinkCopyFast](#shrinkcopyfast)

---

### shrinkCopy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dleft` | `&nbsp;` | 复制目标矩形的左端。可指定小数点。 |
| `dtop` | `&nbsp;` | 复制目标矩形的上端。可指定小数点。 |
| `dwidth` | `&nbsp;` | 复制目标矩形的宽度。可指定小数点。 |
| `dheight` | `&nbsp;` | 复制目标矩形的高度。可指定小数点。 |
| `src` | `&nbsp;` | 复制源图层 |
| `sleft` | `&nbsp;` | 复制源矩形的左端。单位为像素。不可指定小数点。 |
| `stop` | `&nbsp;` | 复制源矩形的上端。单位为像素。不可指定小数点。 |
| `swidth` | `&nbsp;` | 复制源矩形的宽度。单位为像素。不可指定小数点。 |
| `sheight` | `&nbsp;` | 复制源矩形的高度。单位为像素。不可指定小数点。 |

**说明**

缩小复制

被放大（dwidth > swidth || dheight > sheight）时为错误。
缩小算法为面积平均法。缩小到 1/2 以下时比 affineCopy 质量更高。
与 stretchCopy 不同，忽略 Layer.face, holdAlpha。

※在透明与不透明的交界部分可能出现伪色（完全透明部分背后的颜色），因此
建议预先使用 layerExSave.dll 的 Layer.oozeColor() 等

---

### shrinkCopyFast

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` |  |
| `shrink_x` | `&nbsp;` | 横向缩小系数(1 以上) |
| `shrink_y` | `&nbsp;` | 纵向缩小系数(1 以上)。省略时或为 0 时使用 shrink_x 的值 |

**说明**

限定缩小复制（按整数分之一缩小＆忽略 α 成分处理）

透明部分被忽略，始终变为不透明
右端、下端的 1dot 部分不能整除时的余数部分可能看起来被拉伸

※自身的尺寸会被强制更改，请注意
⇒ 相当于 setImageSize(Math.ceil(src.imageWidth / shrink_x), Math.ceil(src.imageHeight / shrink_y))

---

## 插件扩展: tftSave

图层扩展

### 成员列表

#### 方法

- [drawGlyph](#drawglyph)
- [renderGlyph](#renderglyph)
- [setGlyphInfo](#setglyphinfo)

---

### drawGlyph

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ch` | `&nbsp;` | 字符代码 |

**说明**

绘制用于 System.savePreRenderedFont 的文字

更新自身对象的 PreRenderedFontImage 属性
※吉里吉里Z 中存在同名函数，请注意

---

### renderGlyph

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ch` | `&nbsp;` | 字符代码 |

**返回值**

成功时返回 true

**说明**

DirectWrite 版 drawGlyph (experimental)

通过 DirectWrite 的字形绘制（有可能失败）

---

### setGlyphInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ch` | `&nbsp;` | 字符代码 |

**说明**

设置字形信息

仅更新自身对象的 PreRenderedFontImage 属性
（是不绘制 drawGlyph 字形图像的函数）

---
