# ImageFunction

ImageFunction 类是操作图像的类。

不能从该类创建对象。所有方法都是类方法 ( static )，像
`ImageFunction.operateRect(...)` 这样直接调用。

操作对象仅为 [Bitmap](Bitmap.md) 对象，不能指定 [Layer](Layer.md) 对象。
请将它理解为从 Layer 所拥有的同名绘制方法中去掉 Layer 固有因素 ( face / holdAlpha / 裁剪矩形等
属性，以及绘制后的重绘通知 )，并把一切改为显式参数的版本。
在运算模式中指定 `omAuto` 时，由于 Bitmap 没有相当于 [Layer.type](Layer.md#type) 的信息，
因此总是被当作 `omAlpha` 处理。

Layer / Bitmap 与它的关系和用法区分请参阅 [Layer、Bitmap 与 ImageFunction](../guide/LayerAndBitmap.md)。

## 成员列表

### 方法

- [operateAffine](#operateaffine)
- [operateRect](#operaterect)
- [operateStretch](#operatestretch)
- [flipLR](#fliplr)
- [flipUD](#flipud)
- [adjustGamma](#adjustgamma)
- [doBoxBlur](#doboxblur)
- [doGrayScale](#dograyscale)
- [colorRect](#colorrect)
- [drawText](#drawtext)
- [drawGlyph](#drawglyph)
- [fillRect](#fillrect)
- [copy9Patch](#copy9patch)

---

### operateAffine

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dst` | `&nbsp;` | 指定叠加目标的 Bitmap 对象。 |
| `src` | `&nbsp;` | 指定叠加源的 Bitmap 对象。 |
| `A` | `&nbsp;` | A 参数。解释随 affine 参数而变。 |
| `B` | `&nbsp;` | B 参数。解释随 affine 参数而变。 |
| `C` | `&nbsp;` | C 参数。解释随 affine 参数而变。 |
| `D` | `&nbsp;` | D 参数。解释随 affine 参数而变。 |
| `E` | `&nbsp;` | E 参数。解释随 affine 参数而变。 |
| `F` | `&nbsp;` | F 参数。解释随 affine 参数而变。 |
| `srcrect` | `null` | 用 Rect 对象以像素为单位指定要叠加的矩形 ( 以叠加源 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪矩形 ( 以叠加目标 Bitmap 的图像位置为基准 )。<br>未指定时不进行裁剪。 |
| `affine` | `&nbsp;` | 指定如何对待后续的 6 个参数 (A ~ F 参数)。<br>指定为真时，6 个参数分别按以下方式解释。<br>`A   : 2D 仿射变换矩阵的 a`<br>`B   : 2D 仿射变换矩阵的 b`<br>`C   : 2D 仿射变换矩阵的 c`<br>`D   : 2D 仿射变换矩阵的 d`<br>`E   : 2D 仿射变换矩阵的 tx`<br>`F   : 2D 仿射变换矩阵的 ty`<br>通过仿射变换，叠加源的图像位置 (x, y) ( 不过，以叠加源矩形的左上角为 (0, 0) ) 会按以下式子被转换为叠加目标的图像位置 (x', y')。<br>x' =  a*x + c*y + tx<br>y' =  b*x + d*y + ty<br>指定为假时，6 个参数分别按以下方式解释。<br>`A   : 复制源矩形左上角点在复制目标图像位置中的 X 坐标位置(x0)`<br>`B   : 复制源矩形左上角点在复制目标图像位置中的 Y 坐标位置(y0)`<br>`C   : 复制源矩形右上角点在复制目标图像位置中的 X 坐标位置(x1)`<br>`D   : 复制源矩形右上角点在复制目标图像位置中的 Y 坐标位置(y1)`<br>`E   : 复制源矩形左下角点在复制目标图像位置中的 X 坐标位置(x2)`<br>`F   : 复制源矩形左下角点在复制目标图像位置中的 Y 坐标位置(y2)`<br>指定为假时，与叠加源右下角对应的叠加目标位置 (x3, y3) 会按以下式子自动计算。<br>x3 = x1 - x0 + x2<br>y3 = y1 - y0 + y2 |
| `mode` | `omAlpha` | 指定运算的模式。<br>指定 `**omPsNormal**` 时，进行 Photoshop 兼容的 Alpha 合成 ( 现行版本中未实现 )。<br>指定 `**omPsAdditive**` 时，进行 Photoshop 兼容的线性减淡 (添加) 合成 ( 现行版本中未实现 )。<br>指定 `**omPsSubtractive**` 时，进行 Photoshop 兼容的线性加深合成 ( 现行版本中未实现 )。<br>指定 `**omPsMultiplicative**` 时，进行 Photoshop 兼容的正片叠底合成 ( 现行版本中未实现 )。<br>指定 `**omPsScreen**` 时，进行 Photoshop 兼容的滤色合成 ( 现行版本中未实现 )。<br>指定 `**omPsOverlay**` 时，进行 Photoshop 兼容的叠加合成 ( 现行版本中未实现 )。<br>指定 `**omPsHardLight**` 时，进行 Photoshop 兼容的强光合成 ( 现行版本中未实现 )。<br>指定 `**omPsSoftLight**` 时，进行 Photoshop 兼容的柔光合成 ( 现行版本中未实现 )。<br>指定 `**omPsColorDodge**` 时，进行 Photoshop 兼容的颜色减淡合成 ( 现行版本中未实现 )。<br>指定 `**omPsColorDodge5**` 时，进行与 Photoshop 5.x 及以下版本兼容的颜色减淡合成 ( 现行版本中未实现 )。<br>指定 `**omPsColorBurn**` 时，进行 Photoshop 兼容的颜色加深合成 ( 现行版本中未实现 )。<br>指定 `**omPsLighten**` 时，进行 Photoshop 兼容的变亮合成 ( 现行版本中未实现 )。<br>指定 `**omPsDarken**` 时，进行 Photoshop 兼容的变暗合成 ( 现行版本中未实现 )。<br>指定 `**omPsDifference**` 时，进行 Photoshop 兼容的差值合成 ( 现行版本中未实现 )。<br>指定 `**omPsDifference5**` 时，进行与 Photoshop 5.x 及以下版本兼容的差值合成 ( 现行版本中未实现 )。<br>指定 `**omPsExclusion**` 时，进行 Photoshop 兼容的排除合成 ( 现行版本中未实现 )。<br>指定 `**omAdditive**` 时，进行加法合成 ( 现行版本中未实现 )。<br>指定 `**omSubtractive**` 时，进行减法合成 ( 现行版本中未实现 )。<br>指定 `**omMultiplicative**` 时，进行乘法合成 ( 现行版本中未实现 )。<br>指定 `**omDodge**` 时，进行减淡合成 ( 现行版本中未实现 )。<br>指定 `**omDarken**` 时，进行变暗合成 ( 现行版本中未实现 )。<br>指定 `**omLighten**` 时，进行变亮合成 ( 现行版本中未实现 )。<br>指定 `**omScreen**` 时，进行滤色合成 ( 现行版本中未实现 )。<br>指定 `**omAlpha**` 时，进行 Alpha 合成。<br>指定 `**omAddAlpha**` 时，进行加法 Alpha 合成。这种情况下，当 face 为 dfOpaque 且 hda 为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。<br>指定 `**omOpaque**` 时，src 的 Alpha 信息会被忽略，src 始终被视为完全不透明。这种情况下，当 face 为 dfOpaque 且 hda 为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。 |
| `face` | `dfAlpha` | 指定绘制方式。<br>指定 `**dfAlpha**` 时，图像会被视为带 Alpha 通道的图像进行绘制。<br>指定 `**dfAddAlpha**` 时，图像会被视为带加法 Alpha 通道的图像进行绘制。<br>指定 `**dfOpaque**` 时，图像会被视为全部完全不透明进行绘制。 |
| `opa` | `255` | 指定叠加的不透明度 ( 0 ~ 255 )。 |
| `type` | `stNearest` | 指定仿射变换的类型。<br>`**stNearest**    ` : 使用最近邻点法<br>`**stFastLinear** ` : 使用低精度线性插值 (部分实现)<br>`**stLinear**     ` : 使用线性插值 (未实现)<br>`**stCubic**      ` : 使用三次插值 (未实现)<br>速度按 stNearest > stFastLinear > stLinear > stCubic 的顺序递减，画质则是速度<br>越快的模式越低。<br>对于 stFastLinear 以及 stLinear、stCubic，可以用按位逻辑或追加指定<br>stRefNoClip；这种情况下，允许参照要复制的位图的区域外来合成<br>颜色。不指定它时，即使转送源位图的周围有富余，<br>也不会参照转送源位图的范围之外 ( 范围外的颜色被视为最接近位置上的<br>范围内的像素颜色 )。 |
| `hda` | `false` | 指定是否保护 Alpha 通道。 |

**说明**

仿射变换运算合成

对指定的叠加源 Bitmap 的矩形，一边进行仿射变换一边运算合成到叠加目标。

---

### operateRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dst` | `&nbsp;` | 指定叠加目标的 Bitmap 对象。 |
| `dleft` | `&nbsp;` | 以像素为单位指定运算目标的矩形左端位置 ( 以运算目标 Bitmap 的图像位置为基准 )。 |
| `dtop` | `&nbsp;` | 以像素为单位指定运算目标的矩形上端位置 ( 以运算目标 Bitmap 的图像位置为基准 )。 |
| `src` | `&nbsp;` | 指定运算源的 Bitmap 对象。<br>未指定时以整体为对象。 |
| `srcrect` | `null` | 用 Rect 对象以像素为单位指定要运算的矩形 ( 以运算源 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪矩形 ( 以叠加目标 Bitmap 的图像位置为基准 )。<br>未指定时不进行裁剪。 |
| `mode` | `omAuto` | 指定运算的模式。<br>指定 `**omPsNormal**` 时，进行 Photoshop 兼容的 Alpha 合成。<br>指定 `**omPsAdditive**` 时，进行 Photoshop 兼容的线性减淡 (添加) 合成。<br>指定 `**omPsSubtractive**` 时，进行 Photoshop 兼容的线性加深合成。<br>指定 `**omPsMultiplicative**` 时，进行 Photoshop 兼容的正片叠底合成。<br>指定 `**omPsScreen**` 时，进行 Photoshop 兼容的滤色合成。<br>指定 `**omPsOverlay**` 时，进行 Photoshop 兼容的叠加合成。<br>指定 `**omPsHardLight**` 时，进行 Photoshop 兼容的强光合成。<br>指定 `**omPsSoftLight**` 时，进行 Photoshop 兼容的柔光合成。<br>指定 `**omPsColorDodge**` 时，进行 Photoshop 兼容的颜色减淡合成。<br>指定 `**omPsColorDodge5**` 时，进行与 Photoshop 5.x 及以下版本兼容的颜色减淡合成。<br>指定 `**omPsColorBurn**` 时，进行 Photoshop 兼容的颜色加深合成。<br>指定 `**omPsLighten**` 时，进行 Photoshop 兼容的变亮合成。<br>指定 `**omPsDarken**` 时，进行 Photoshop 兼容的变暗合成。<br>指定 `**omPsDifference**` 时，进行 Photoshop 兼容的差值合成。<br>指定 `**omPsDifference5**` 时，进行与 Photoshop 5.x 及以下版本兼容的差值合成。<br>指定 `**omPsExclusion**` 时，进行 Photoshop 兼容的排除合成。<br>指定 `**omAdditive**` 时，进行加法合成。<br>指定 `**omSubtractive**` 时，进行减法合成。<br>指定 `**omMultiplicative**` 时，进行乘法合成。<br>指定 `**omDodge**` 时，进行减淡合成。<br>指定 `**omDarken**` 时，进行变暗合成。<br>指定 `**omLighten**` 时，进行变亮合成。<br>指定 `**omScreen**` 时，进行滤色合成。<br>指定 `**omAlpha**` 时，进行 Alpha 合成。<br>指定 `**omAddAlpha**` 时，进行加法 Alpha 合成。<br>指定 `**omOpaque**` 时，src 的 Alpha 信息会被忽略，src 始终被视为完全不透明。 |
| `face` | `dfAlpha` | 指定绘制方式。<br>指定 `**dfAlpha**` 时，图像会被视为带 Alpha 通道的图像进行绘制。<br>指定 `**dfAddAlpha**` 时，图像会被视为带加法 Alpha 通道的图像进行绘制。<br>指定 `**dfOpaque**` 时，图像会被视为全部完全不透明进行绘制。 |
| `opa` | `255` | 指定运算的强度 ( 0 ~ 255 )。 |
| `hda` | `false` | 指定是否保护 Alpha 通道。 |

**说明**

矩形运算合成

将指定的运算源 Bitmap 的矩形部分，以指定的模式运算合成到运算目标 Bitmap 的指定位置。

---

### operateStretch

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dst` | `&nbsp;` | 指定叠加目标的 Bitmap 对象。 |
| `src` | `&nbsp;` | 指定叠加源的 Bitmap 对象。 |
| `dstrect` | `null` | 用 Rect 对象以像素为单位指定叠加目标的矩形 ( 以叠加目标 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |
| `srcrect` | `null` | 用 Rect 对象以像素为单位指定要叠加的矩形 ( 以叠加源 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪矩形 ( 以叠加目标 Bitmap 的图像位置为基准 )。<br>未指定时不进行裁剪。 |
| `mode` | `omAuto` | 指定运算的模式。<br>指定 `**omPsNormal**` 时，进行 Photoshop 兼容的 Alpha 合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsAdditive**` 时，进行 Photoshop 兼容的线性减淡 (添加) 合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsSubtractive**` 时，进行 Photoshop 兼容的线性加深合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsMultiplicative**` 时，进行 Photoshop 兼容的正片叠底合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsScreen**` 时，进行 Photoshop 兼容的滤色合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsOverlay**` 时，进行 Photoshop 兼容的叠加合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsHardLight**` 时，进行 Photoshop 兼容的强光合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsSoftLight**` 时，进行 Photoshop 兼容的柔光合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsColorDodge**` 时，进行 Photoshop 兼容的颜色减淡合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsColorDodge5**` 时，进行与 Photoshop 5.x 及以下版本兼容的颜色减淡合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsColorBurn**` 时，进行 Photoshop 兼容的颜色加深合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsLighten**` 时，进行 Photoshop 兼容的变亮合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsDarken**` 时，进行 Photoshop 兼容的变暗合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsDifference**` 时，进行 Photoshop 兼容的差值合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsDifference5**` 时，进行与 Photoshop 5.x 及以下版本兼容的差值合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omPsExclusion**` 时，进行 Photoshop 兼容的排除合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omAdditive**` 时，进行加法合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omSubtractive**` 时，进行减法合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omMultiplicative**` 时，进行乘法合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omDodge**` 时，进行减淡合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omDarken**` 时，进行变暗合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omLighten**` 时，进行变亮合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omScreen**` 时，进行滤色合成 ( 1.3 及以后除 stNearest 与 stFastLinear 以外实现 )。<br>指定 `**omAlpha**` 时，进行 Alpha 合成。<br>指定 `**omAddAlpha**` 时，进行加法 Alpha 合成。这种情况下，当 face 为 dfOpaque 且 hda 为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。<br>指定 `**omOpaque**` 时，src 的 Alpha 信息会被忽略，src 始终被视为完全不透明。这种情况下，当 face 为 dfOpaque 且 hda 为假时，通过在 type 参数中指定 stFastLinear 即可进行线性插值。 |
| `face` | `dfAlpha` | 指定绘制方式。<br>指定 `**dfAlpha**` 时，图像会被视为带 Alpha 通道的图像进行绘制。<br>指定 `**dfAddAlpha**` 时，图像会被视为带加法 Alpha 通道的图像进行绘制。<br>指定 `**dfOpaque**` 时，图像会被视为全部完全不透明进行绘制。 |
| `opa` | `255` | 指定运算的强度 ( 0 ~ 255 )。 |
| `type` | `stNearest` | 指定缩放的类型。<br>`**stNearest**          ` : 使用最近邻点法<br>`**stFastLinear**       ` : 使用低精度线性插值 (部分实现)<br>`**stSemiFastLinear**   ` : 使用定点线性插值 (1.3 及以后)<br>`**stLinear**           ` : 使用线性插值 (1.3 及以后实现变更)<br>`**stFastCubic**        ` : 使用定点三次插值 (1.3 及以后)<br>`**stCubic**            ` : 使用三次插值 (1.3 及以后实现变更)<br>`**stFastLanczos2**     ` : 使用范围为 4x4 的定点 Lanczos 插值 (1.3 及以后)<br>`**stLanczos2**         ` : 使用范围为 4x4 的 Lanczos 插值 (1.3 及以后)<br>`**stFastLanczos3**     ` : 使用范围为 6x6 的定点 Lanczos 插值 (1.3 及以后)<br>`**stLanczos3**         ` : 使用范围为 6x6 的 Lanczos 插值 (1.3 及以后)<br>`**stFastSpline16**     ` : 使用定点样条插值 4x4 (1.3 及以后)<br>`**stSpline16**         ` : 使用样条插值 4x4 (1.3 及以后)<br>`**stFastSpline36**     ` : 使用定点样条插值 6x6 (1.3 及以后)<br>`**stSpline36**         ` : 使用样条插值 6x6 (1.3 及以后)<br>`**stFastAreaAvg**      ` : 使用定点面积平均缩小。不能放大 (1.3 及以后)<br>`**stAreaAvg**          ` : 使用面积平均缩小。不能放大 (1.3 及以后)<br>`**stFastGaussian**     ` : 使用定点高斯插值 4x4 (1.3 及以后)<br>`**stGaussian**         ` : 使用高斯插值 4x4 (1.3 及以后)<br>`**stFastBlackmanSinc** ` : 使用定点 Blackman-Sinc 插值 8x8 (1.3 及以后)<br>`**stBlackmanSinc**     ` : 使用 Blackman-Sinc 插值 8x8 (1.3 及以后)<br>速度按 stNearest > stFastLinear > stLinear > stCubic 的顺序递减，画质则是速度<br>越快的类型越低。<br>stCubic 及以后的插值方法画质都足够高，可以说是个人喜好的差异。<br>不过，高斯插值会呈现有些模糊的画质。<br>stFastLinear 与其他线性插值 (stSemiFastLinear 与 stLinear) 的差异在缩小时会明显体现出来。<br>stFastLinear 总是参照周围 4 个像素，而 stSemiFastLinear、stLinear 在缩小时会<br>参照等倍时影响范围为 4 个像素那样的范围，即参照更大范围的像素进行插值，因此画质更高<br>(从算法上说才是原本的线性插值)。<br>对于 stFastLinear，可以用按位逻辑或追加指定 stRefNoClip；这种情况下，<br>允许参照要复制的位图的区域外来合成颜色。不指定它时，<br>即使转送源位图的周围有富余，也不会参照转送源位图的范围<br>之外 ( 范围外的颜色被视为最接近位置上的范围内的像素颜色 )。 |
| `hda` | `false` | 指定是否保护 Alpha 通道。 |
| `option` | `-1.0` | 1.3 及以后追加。<br>是三次插值时的锐度。在其他插值方法中目前没有意义。<br>将锐度的值向正方向增大就会逐渐变模糊，向负方向增大就会逐渐变锐利。 |

**说明**

缩放运算合成

将指定的叠加源 Bitmap 的矩形，运算合成到叠加目标 Bitmap 的矩形。

当叠加源矩形与叠加目标矩形的大小不同时，会进行放大或缩小。

---

### flipLR

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要翻转的 Bitmap 对象。 |
| `rect` | `null` | 用 Rect 对象指定要翻转的区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |

**说明**

左右翻转

对图像进行左右翻转。

---

### flipUD

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要翻转的 Bitmap 对象。 |
| `rect` | `null` | 用 Rect 对象指定要翻转的区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |

**说明**

上下翻转

对图像进行上下翻转。

---

### adjustGamma

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要伽马校正的 Bitmap 对象。 |
| `rgamma` | `1.0` | 指定红色分量的伽马值 ( 0.0 ~ 1.0 ~ 9.0 )。 |
| `rfloor` | `0` | 指定红色分量的输出最小值 ( 0 ~ 255 )。 |
| `rceil` | `255` | 指定红色分量的输出最大值 ( 0 ~ 255 )。 |
| `ggamma` | `1.0` | 指定绿色分量的伽马值 ( 0.0 ~ 1.0 ~ 9.0 )。 |
| `gfloor` | `0` | 指定绿色分量的输出最小值 ( 0 ~ 255 )。 |
| `gceil` | `255` | 指定绿色分量的输出最大值 ( 0 ~ 255 )。 |
| `bgamma` | `1.0` | 指定蓝色分量的伽马值 ( 0.0 ~ 1.0 ~ 9.0 )。 |
| `bfloor` | `0` | 指定蓝色分量的输出最小值 ( 0 ~ 255 )。 |
| `bceil` | `255` | 指定蓝色分量的输出最大值 ( 0 ~ 255 )。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |
| `isaddalpha` | `false` | 指定是否为加法合成 Alpha 格式。 |

**说明**

伽马校正

对图像执行伽马校正。

伽马值指定为 1.0 时，伽马曲线会变成直线。

输出最小值与输出最大值用于指定各分量亮度的最小值与最大值。

将最大值设为低于最小值的值时，可以反转图像。

isaddalpha 为 true 时，此方法使用面向加法 Alpha 合成的特殊伽马校正例程。

该例程对加法 Alpha 合成中相当于 Alpha 合成的分量进行伽马校正，但对相当于加法合成的分量不进行伽马校正。

---

### doBoxBlur

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要施加矩形模糊的 Bitmap 对象。 |
| `xblur` | `1` | 指定横向模糊的范围。 |
| `yblur` | `1` | 指定纵向模糊的范围。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |
| `isalpha` | `true` | 指定是否具有 Alpha 通道。 |

**说明**

施加矩形模糊

施加模糊。算法为“矩形模糊”(box blur)。

矩形模糊是取由 xblur 与 yblur 两个参数所表示的“范围”中像素亮度的平均值。例如 xblur=10、yblur=2 时，以对象像素为中心，取横向 -10~10、纵向 -2~2 的矩形范围内像素亮度的平均值，该值就成为该像素最终的亮度。

范围的面积可以用 (xblur×2+1) × (yblur×2+1) 计算。在现行版本中，当该面积小于 256 时，会采用比面积不小于 256 的情况更高速的算法。

isalpha 为 true 时，由于使用面向 Alpha 合成的特殊算法，速度会稍慢。

为 false 时，则会使用更高速的算法。

---

### doGrayScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要转换为灰度的 Bitmap 对象。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |
| `rweight` | `&nbsp;` | 指定红色分量的权重。3 个参数要么全部省略，要么全部指定。 |
| `gweight` | `&nbsp;` | 指定绿色分量的权重。 |
| `bweight` | `&nbsp;` | 指定蓝色分量的权重。 |

**说明**

灰度转换

将图像转换为灰度。

省略 rweight / gweight / bweight 时，使用相当于 BT.709 的权重
(0.2126 / 0.7152 / 0.0722) (以往的行为)。 权重的处理方式与
[Layer.doGrayScale](Layer.md#dograyscale) 相同。

---

### colorRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要填充的 Bitmap 对象。 |
| `value` | `&nbsp;` | 指定要填充的颜色或值。<br>该值的含义随 face 参数的值而变化。<br>`**dfAlpha**    ` : 请用 0xRRGGBB 格式指定颜色<br>`**dfAddAlpha** ` : 请用 0xRRGGBB 格式指定颜色<br>`**dfOpaque**   ` : 请用 0xRRGGBB 格式指定颜色<br>`**dfMask**     ` : 请指定遮罩 (不透明度) 的值 ( 0 ~ 255 )<br>指定 dfOpaque 时，遮罩信息会被忽略。另外，指定 dfMask 时，颜色信息会保持原样。<br>当为 dfAlpha 且 opa 为负时，此参数会被忽略。 |
| `opa` | `255` | 指定填充的不透明度 ( -255 ~ 0 ~ 255 )。<br>当 face 的值为 dfMask 或 dfProvince 时，此参数会被忽略 ( 始终完全不透明 )。<br>指定负数仅在 face 为 dfAlpha 时有效，<br>这种情况下 value 参数会被忽略，图像的不透明度会被去除 (<br>指定 -255 时矩形会变成完全透明 )。 |
| `rect` | `null` | 用 Rect 对象以像素为单位指定要填充的矩形 ( 以图像位置为基准 )。<br>未指定时以整体为对象。 |
| `face` | `dfAlpha` | 指定绘制方式。<br>指定 `**dfAlpha**` 时，图像会被视为带 Alpha 通道的图像进行绘制。<br>指定 `**dfAddAlpha**` 时，图像会被视为带加法 Alpha 通道的图像进行绘制。<br>指定 `**dfOpaque**` 时，图像会被视为全部完全不透明进行绘制。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |

**说明**

矩形半透明填充

以指定的方法填充指定的 Bitmap 图像的矩形。

与 [ImageFunction.fillRect](ImageFunction.md#fillrect) 不同，可以指定透明度进行半透明填充。

---

### drawText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要绘制文字的 Bitmap 对象。 |
| `font` | `&nbsp;` | 用 Font 对象指定要绘制的字体。 |
| `x` | `&nbsp;` | 以像素为单位指定开始绘制文字的原点 ( 以图像位置为基准 ) 的 x 坐标。 |
| `y` | `&nbsp;` | 以像素为单位指定开始绘制文字的原点 ( 以图像位置为基准 ) 的 y 坐标。 |
| `text` | `&nbsp;` | 指定要绘制的文字。 |
| `color` | `&nbsp;` | 用 0xRRGGBB 格式指定要绘制的文字颜色。 |
| `opa` | `255` | 指定要绘制文字的不透明度 ( -255 ~ 0 ~ 255 )。<br>指定负数仅在 face 为 dfAlpha 时有效，<br>这种情况下会按文字的形状去除不透明度 ( 值越小<br>效果越大 )。 |
| `aa` | `true` | 指定是否进行抗锯齿。<br>指定为真时进行抗锯齿。指定为假时不进行。 |
| `face` | `dfAlpha` | 指定绘制方式。<br>指定 `**dfAlpha**` 时，图像会被视为带 Alpha 通道的图像进行绘制。<br>指定 `**dfAddAlpha**` 时，图像会被视为带加法 Alpha 通道的图像进行绘制。<br>指定 `**dfOpaque**` 时，图像会被视为全部完全不透明进行绘制。 |
| `shadowlevel` | `0` | 指定阴影的不透明度。合适的值会随 shadowwidth 参数的值而变化。<br>指定 0 时不绘制阴影。 |
| `shadowcolor` | `0x000000` | 用 0xRRGGBB 格式指定阴影的颜色。 |
| `shadowwidth` | `0` | 指定阴影的宽度 ( 模糊量 )。 0 最锐利 ( 不模糊 )，增大值<br>可以使阴影变模糊。 |
| `shadowofsx` | `0` | 以像素为单位指定阴影位置的 x 坐标值。 指定 0 时，阴影绘制在正下方。 |
| `shadowofsy` | `0` | 以像素为单位指定阴影位置的 y 坐标值。 指定 0 时，阴影绘制在正下方。 |
| `hda` | `false` | 指定是否保护 Alpha 通道。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |

**返回值**

绘制区域 ( Rect 对象 )

**说明**

文字绘制

在 Bitmap 上绘制文字。

当 face 指定为 dfOpaque 时，绘制目标的遮罩是被破坏还是被保护取决于 hda。

---

### drawGlyph

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要绘制文字的 Bitmap 对象。 |
| `x` | `&nbsp;` | 以像素为单位指定开始绘制文字的原点 ( 以图像位置为基准 ) 的 x 坐标。 |
| `y` | `&nbsp;` | 以像素为单位指定开始绘制文字的原点 ( 以图像位置为基准 ) 的 y 坐标。 |
| `glyph` | `&nbsp;` | 指定要绘制的字形。 |
| `color` | `&nbsp;` | 用 0xRRGGBB 格式指定要绘制的文字颜色。 |
| `opa` | `255` | 指定要绘制文字的不透明度 ( -255 ~ 0 ~ 255 )。<br>指定负数仅在 face 为 dfAlpha 时有效，<br>这种情况下会按文字的形状去除不透明度 ( 值越小<br>效果越大 )。 |
| `aa` | `true` | 指定是否进行抗锯齿。<br>指定为真时进行抗锯齿。指定为假时不进行。 |
| `face` | `dfAlpha` | 指定绘制方式。<br>指定 `**dfAlpha**` 时，图像会被视为带 Alpha 通道的图像进行绘制。<br>指定 `**dfAddAlpha**` 时，图像会被视为带加法 Alpha 通道的图像进行绘制。<br>指定 `**dfOpaque**` 时，图像会被视为全部完全不透明进行绘制。 |
| `shadowlevel` | `0` | 指定阴影的不透明度。合适的值会随 shadowwidth 参数的值而变化。<br>指定 0 时不绘制阴影。 |
| `shadowcolor` | `0x000000` | 用 0xRRGGBB 格式指定阴影的颜色。 |
| `shadowwidth` | `0` | 指定阴影的宽度 ( 模糊量 )。 0 最锐利 ( 不模糊 )，增大值<br>可以使阴影变模糊。 |
| `shadowofsx` | `0` | 以像素为单位指定阴影位置的 x 坐标值。 指定 0 时，阴影绘制在正下方。 |
| `shadowofsy` | `0` | 以像素为单位指定阴影位置的 y 坐标值。 指定 0 时，阴影绘制在正下方。 |
| `hda` | `false` | 指定是否保护 Alpha 通道。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |

**返回值**

绘制区域 ( Rect 对象 )

**说明**

文字绘制

在 Bitmap 上绘制字形。

当 face 指定为 dfOpaque 时，绘制目标的遮罩是被破坏还是被保护取决于 hda。

字形请指定为形如 glyph : Array[9] = [ width, height, originx, originy, incx, incy, inc, bitmap(Octet), colors ] 的数组。

省略字形的 colors 时，会被判断为 256 级灰度。

---

### fillRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bmp` | `&nbsp;` | 指定要填充的 Bitmap 对象。 |
| `value` | `&nbsp;` | 指定要填充的颜色或值。<br>该值的含义随 isalpha 的值而变化。<br>`**true**  ` : 请用 0xAARRGGBB 格式指定不透明度和颜色。主图像与遮罩都会被填充。<br>`**false** ` : 请用 0xRRGGBB 格式指定颜色。 |
| `rect` | `null` | 用 Rect 对象以像素为单位指定要填充的矩形 ( 以图像位置为基准 )。<br>未指定时以整体为对象。 |
| `isalpha` | `true` | 指定是否具有 Alpha 通道。 |
| `cliprect` | `null` | 用 Rect 对象指定裁剪区域 ( 以 Bitmap 的图像位置为基准 )。<br>未指定时以整体为对象。 |

**说明**

矩形填充

以指定的方法填充指定的 Bitmap 图像的矩形。

---

### copy9Patch

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dst` | `Bitmap` | `&nbsp;` | 复制目标的 Bitmap |
| `src` | `Bitmap` | `&nbsp;` | 复制源的 Bitmap |

**返回值**

边距信息

**说明**

利用 9 path 的图像复制 (多平台版及以后)

利用 9 path ( slice ) 进行图像复制。
返回的边距信息是 Rect 类的对象。
在该边距内绘制文本等。

---
