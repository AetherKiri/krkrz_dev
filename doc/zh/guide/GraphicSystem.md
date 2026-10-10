# 图形系统

## 关于图形系统

吉里吉里拥有基于图层的图形显示机制。

各图层拥有通过 Alpha 混合进行透明叠加以及层级结构管理的功能。另外，为了让图层能够作为 GUI 部件 (widget) 运行，还拥有接收用户输入的机制 ( 焦点 )。



叠加后的图层由称为绘制设备的机制绘制到窗口上。绘制设备可以通过操作 [Window.drawDevice](../reference/Window.md#drawdevice) 属性自由替换，用户也可以自行 (以插件的形式) 定义符合用途的演出效果等。

引擎本体内置了以下绘制设备，启动时的默认值因构建而异 (可以通过启动选项 `-drawdevice` 选择。详情请参阅[命令行选项](CommandLine.md))。

| 类 | 内容 | 备注 |
|---|---|---|
| [BasicDrawDevice](../reference/Window.BasicDrawDevice.md) | 基于 Direct3D 11 的标准绘制 | Windows 原生 (WINVER) 构建的默认 |
| [SDLOGLDrawDevice](../reference/SDLOGLDrawDevice.md) | OpenGL ES 直接绘制 | SDL3 构建的默认 (启用 OpenGL 的构建时) |
| [SDLDrawDevice](../reference/SDLDrawDevice.md) | 基于 SDL_Renderer 的标准绘制 | SDL3 构建。禁用 OpenGL 的构建的默认 |
| [OGLDrawDevice](../reference/OGLDrawDevice.md) | 包含 OpenGL ES 与 [Canvas](../reference/Canvas.md) 等 GL 类群的全功能版 | 两种构建均可使用 |
| [NullDrawDevice](../reference/NullDrawDevice.md) | 不进行绘制 | 用于验证 |

使用 OpenGL 系列的设备需要可以利用 OpenGL ES 的环境。另外，以 `-drawdevice=sdl` 启动 SDL3 构建时，无法在运行中切换到 OpenGL 系列。

不用于显示的工作用图像由 [Bitmap](../reference/Bitmap.md) 类处理，其加工使用 [ImageFunction](../reference/ImageFunction.md) 类。三者的关系与用法区分请参阅 [Layer 与 Bitmap 与 ImageFunction](LayerAndBitmap.md)。

## 可读写的图像格式

标准状态下的吉里吉里中，可以用 [Layer.loadImages](../reference/Layer.md#loadimages) 加载到图层、以及可以写入图层的格式如下。

- **BMP**  
  Windows 标准的位图格式。32 bpp 的 BMP 被视为带 Alpha 通道的位图。
  
  无法读取经 RLE 压缩的位图。
- **PNG**  
  可以读取 Portable Network Graphic 格式。带 Alpha 通道的位图 PNG 也可以读取。
- **JPEG**  
  可以读取 JPEG 格式。算术压缩的和无损压缩的无法读取，不过本来就很少见，我想也没什么关系。
- **TLG5**  
  吉里吉里独有的无损压缩格式。扩展名为 .tlg。带 Alpha 通道的也可以读取。压缩率不算高，但特征是可以高速解压。**本格式不能用于遮罩图像(_m) 或区域图像 (_p)**。只能处理无 Alpha 通道的全彩色图像，或者带 Alpha 通道的全彩色图像。
- **TLG6**  
  吉里吉里独有的无损压缩格式。扩展名与 TLG5 相同，为 .tlg。TLG6 以高压缩率为特征。解压速度要花 TLG5 近两倍的时间，但即便如此也能以 PNG 两倍以上的速度解压，大小也比 PNG 小 2~4 成。
- **主图像/遮罩分离格式**  
  主图像/遮罩分离格式是将颜色信息的图像 (主图像) 与 Alpha 通道 (遮罩) 的图像分离的格式，遮罩图像是在主图像的文件名后附加 _m 得到的 ( 例如，abc.jpeg 对应 abc_m.jpeg )。
  
  主图像/遮罩图像的格式不同也没有关系。

此外，还可以使用 Susie Plug-in 增加可读取的图像格式。Susie plug-in 可以通过 [Plugins.link](../reference/Plugins.md#link) 方法加载。

从 Susie Plug-in 传递来 32bpp 的位图时，会被视为带 Alpha 通道的位图。

## 图层类型

吉里吉里的图层可以用各种合成模式 (图层类型) 显示。

有以下合成模式，可以将以 lt 开头的图层类型常量指定给 [Layer.type](../reference/Layer.md#type) 属性。

另外，式中的 *result* 是结果，*dest* 是叠加目标图像的亮度，*src* 是要叠加的图像的亮度，*α* 是要叠加的图像每像素的 Alpha 值，所有值的范围均为 0.0 ~ 1.0。

另外，这里为了说明，定义以下函数。

- abs(*a*) : *a* 的绝对值
- max(*a*, *b*) : *a* 与 *b* 中较大的一方
- min(*a*, *b*) : *a* 与 *b* 中较小的一方
- blend(*a*, *b*, *r*) = *a* × (1.0 - *r*) + *b* × *r*

- ****ltOpaque** (**ltCoverRect**)**  
  ltOpaque 是不带透明的显示。图层的整个矩形始终为完全不透明的显示 ( 虽然不仅限于这种图层类型，但用 [Layer.opacity](../reference/Layer.md#opacity) 降低不透明度时，会遵从该设置 )。
  
  
  
  公式：*result* = *src*
  
  > **Note:**
  > ltCoverRect 也表示相同的意思，但那是 2.23 beta 2 之前的旧名称。
- ****ltAlpha** (**ltTransparent**)**  
  ltAlpha 进行 Alpha 合成。是进行透明处理时最基本的类型。从 BMP 或 Susie plug-in 输入 Alpha 通道时也使用下面的公式。
  
  
  
  公式：*result* = blend(*dest*, *src*, *α*)
  
  > **Note:**
  > ltTransparent 也表示相同的意思，但那是 2.23 beta 2 之前的旧名称。
- ****ltAddAlpha****  
  ltAddAlpha 进行加法 Alpha 合成。
  
  使用 可以输出适合这种格式的图像。另外，还可以用 [Layer.convertType](../reference/Layer.md#converttype) 方法从 ltAlpha 转换为这种格式。
  
  ltAddAlpha 的图层如果成为 ltAlpha 图层的直接子级，将无法正常显示。
  
  
  
  公式：*result* = min(1.0, *dest* × ( 1.0 - *α* ) + *src*)
- ****ltAdditive****  
  ltAdditive 进行加法合成。适合表现光晕。在 Photoshop 中相当于“线性减淡(添加)”，但如果想获得与 Photoshop 相同的效果，请使用后述的 ltPsAdditive。与 ltPsAdditive 不同，ltAdditive 会忽略 *α*。
  
  中性色 (叠加后也不发生变化的颜色) 是黑色。
  
  
  
  公式：*result* = min(1.0, *dest* + *src*)
- ****ltSubtractive****  
  ltSubtractive 进行减法合成。*α* 会被忽略。
  
  中性色是白色。
  
  
  
  公式：*result* = max(0.0, *dest* + *src* - 1.0)
  
  > **Note:**
  > 与 *result* = *dest* - *src* 的差别，仅在于 src 是否反转这一点。
- ****ltMultiplicative****  
  ltMultiplicative 进行乘法合成。*α* 会被忽略。
  
  中性色是白色。
  
  
  
  公式：*result* = *dest* × *src*
- ****ltDodge****  
  ltDodge 进行“减淡”合成。适合表现被光照亮的效果。*α* 会被忽略。
  
  中性色是黑色。
  
  
  
  公式：*result* = min(1.0, *dest* ÷ ( 1.0 -  *src* ) )
- ****ltLighten****  
  ltLighten 进行“变亮”合成。*α* 会被忽略。
  
  中性色是黑色。
  
  
  
  公式：*result* = max(*dest*, *src*)
- ****ltDarken****  
  ltDarken 进行“变暗”合成。*α* 会被忽略。
  
  中性色是白色。
  
  
  
  公式：*result* = min(*dest*, *src*)
- ****ltScreen****  
  ltLighten 进行“滤色”合成。*α* 会被忽略。
  
  中性色是黑色。
  
  
  
  公式：*result* = 1.0 - ( 1.0 - *dest* ) × ( 1.0 - *src* )
- ****ltPsNormal****  
  ltPsNormal 拥有与 ltAlpha 相同的效果。出于历史原因，与 ltAlpha 是不同的例程和名称。
- ****ltPsAdditive****  
  ltPsAdditive 进行 Photoshop 兼容的“线性减淡(添加)”合成 (加法合成)。与 ltAdditive 不同，*α* 不会被忽略。
  
  中性色是黑色。
  
  
  
  公式：*result* = blend(*dest*, min(1.0, *dest* + *src*), *α*)
- ****ltPsSubtractive****  
  ltPsSubtractive 进行 Photoshop 兼容的“线性加深”合成 (减法合成)。与 ltSubtractive 不同，*α* 不会被忽略。
  
  中性色是白色。
  
  
  
  公式：*result* = blend(*dest*, max(0.0, *dest* + *src* - 1.0), *α*)
- ****ltPsMultiplicative****  
  ltPsMultiplicative 进行 Photoshop 兼容的“正片叠底”合成。与 ltMultiplicative 不同，*α* 不会被忽略。
  
  中性色是白色。
  
  
  
  公式：*result* = blend(*dest*, *dest* × *src*, *α*)
- ****ltPsScreen****  
  ltPsScreen 进行 Photoshop 兼容的“滤色”合成。与 ltScreen 不同，*α* 不会被忽略。
  
  中性色是黑色。
  
  
  
  公式：*result* = blend(*dest*, 1.0 - (1.0 - *dest*) × (1.0 - *src*), *α*)
- ****ltPsOverlay****  
  ltPsOverlay 进行 Photoshop 兼容的“叠加”合成。
  
  中性色是 50% 灰色。
  
  
  
  公式：*result* = blend(*dest*, overlay(*dest*, *src*), *α*)
  
  其中 overlay(*a*, *b*) =
  
  *a* × *b* × 2.0  ( *a* < 0.5 时)
  
  1.0 - (1.0 - *a*) × (1.0 - *b*) × 2.0 (其他情况)
- ****ltPsHardLight****  
  ltPsHardLight 进行 Photoshop 兼容的“强光”合成。
  
  中性色是 50% 灰色。
  
  
  
  公式：*result* = blend(*dest*, hardlight(*dest*, *src*), *α*)
  
  其中 hardlight(*a*, *b*) =
  
  *a* × *b* × 2.0  (*b* < 0.5 时)
  
  1.0 - (1.0 - *a*) × (1.0 - *b*) × 2.0 (其他情况)
- ****ltPsSoftLight****  
  ltPsSoftLight 进行 Photoshop 兼容的“柔光”合成。
  
  中性色是 50% 灰色。
  
  
  
  公式：*result* = blend(*dest*, softlight(*dest*, *src*), *α*)
  
  其中 softlight(*a*, *b*) =
  
  *a*(0.5 ÷ *b*)  (*b* > 0.5 时)
  
  *a*((1.0 - *b*) × 2)  (其他情况)
- ****ltPsColorDodge****  
  ltPsColorDodge 进行 Photoshop 兼容的“颜色减淡”合成。与 ltDodge 不同，*α* 不会被忽略。
  
  中性色是黑色。
  
  
  
  公式：*result* = blend(*dest*, min(1.0, *dest* ÷ ( 1.0 -  *src* ) ), *α*)
- ****ltPsColorDodge5****  
  ltPsColorDodge 进行与 Photoshop 5.x 及以下版本兼容的“颜色减淡”合成。公式与 ltPsColorDodge 略有不同。
  
  中性色是黑色。
  
  
  
  公式：*result* = min(1.0, *dest* ÷ ( 1.0 - *src* × *α*) )
- ****ltPsColorBurn****  
  ltPsColorBurn 进行 Photoshop 兼容的“颜色加深”合成。
  
  中性色是白色。
  
  
  
  公式：*result* = blend(*dest*, max(0.0, 1.0 - (1.0 - *dest*) ÷ *src*), *α*)
- ****ltPsLighten****  
  ltPsLighten 进行 Photoshop 兼容的“变亮”合成。与 ltLighten 不同，*α* 不会被忽略。
  
  中性色是黑色。
  
  
  
  公式：*result* = blend(*dest*, max(*dest*, *src*), *α*)
- ****ltPsDarken****  
  ltPsDarken 进行 Photoshop 兼容的“变暗”合成。与 ltDarken 不同，*α* 不会被忽略。
  
  中性色是白色。
  
  
  
  公式：*result* = blend(*dest*, min(*dest*, *src*), *α*)
- ****ltPsDifference****  
  ltPsDifference 进行 Photoshop 兼容的“差值”合成。
  
  中性色是黑色。
  
  
  
  公式：*result* = blend(*dest*, abs(*dest* - *src*), *α*)
- ****ltPsDifference5****  
  ltPsDifference5 进行与 Photoshop 5.x 及以下版本兼容的“差值”合成。公式与 ltPsDifference 略有不同。
  
  中性色是黑色。
  
  
  
  公式：*result* = abs(*dest* - *src* × *α*)
- ****ltPsExclusion****  
  ltPsExclusion 进行 Photoshop 兼容的“排除”合成。
  
  中性色是黑色。
  
  
  
  公式：*result* = blend(*dest*,  *dest* + *src* - 2.0 × *src* × *dest*, *α*)

## Alpha 合成与加法 Alpha 合成

吉里吉里拥有两种 Alpha 合成模式。

- **Alpha 合成**  
  在 [Layer.type](../reference/Layer.md#type) 属性中指定 **ltAlpha** 就会变成这种显示类型。
  
  ltAlpha 是许多绘图软件采用的 Alpha 合成模式。直接读取其他绘图软件输出的数据时，适合使用这种模式。
- **加法 Alpha 合成**  
  在 [Layer.type](../reference/Layer.md#type) 属性中指定 **ltAddAlpha** 就会变成这种显示类型。
  
  与 Alpha 合成相比，这种格式有以下优点与缺点。
  
  - 由于公式比 Alpha 合成更简单，能够高速显示，在许多绘制方法中也可以进行高速绘制
  - 可以同时表现 Alpha 合成和加法合成
  - 几乎没有支持这种格式的绘图软件
  
  支持与 ltAddAlpha 相同合成模式的绘图软件应该不多，因此要在吉里吉里中以这种格式处理其他软件的输出，
  
  需要使用 输出这种类型的图像，或者用 [Layer.convertType](../reference/Layer.md#converttype) 方法从 ltAlpha 转换为这种格式。
  
  图像格式转换器可以接受 Photoshop 格式下“正常”图层与“线性减淡(添加)”图层组合而成的输入，作为加法 Alpha 合成用图像的输入。

## 图层类型、绘制方式与运算模式

吉里吉里中有图层类型 (用以 lt 开头的常量指定)、绘制方式 (用以 df 开头的常量指定) 和运算模式 (用以 om 开头的常量指定)。

它们各自有着相似的名称，但用途如下所示。

- **图层类型**  
  图层类型是通过 [Layer.type](../reference/Layer.md#type) 属性指定的值，用于指定图层如何显示。
- **绘制方式**  
  绘制方式是通过 [Layer.face](../reference/Layer.md#face) 属性指定的值，用于指定如何向图层绘制。指定 dfAuto 时，会根据图层类型决定合适的绘制方式。也可以用与图层类型最适绘制方法不同的绘制方式来绘制。
  
  在 [Layer.copyRect](../reference/Layer.md#copyrect) 方法这样的图层间复制方法中，也用于选择复制哪些信息。dfBoth (或 dfAlpha、dfAddAlpha 时) 会同时复制主图像和遮罩。dfMain (或 dfOpaque) 时只复制主图像。dfMask 时只复制遮罩，dfProvince 时只复制区域图像。
  
  同样地，在 [Layer.fillRect](../reference/Layer.md#fillrect) 方法中，也用于选择填充哪些信息。dfBoth (或 dfAlpha、dfAddAlpha 时) 会同时填充主图像和遮罩。dfMain (或 dfOpaque) 时只填充主图像。dfMask 时只填充遮罩，dfProvince 时只填充区域图像。
- **运算模式**  
  运算模式是通过 [Layer.operateRect](../reference/Layer.md#operaterect) 方法的参数等指定的值，用于指定如何处理运算源 (被叠加的图层)。指定 omAuto 时，会根据运算源的图层类型决定合适的模式。

## Alpha 通道的保护

当 [Layer.face](../reference/Layer.md#face) 属性指定的绘制方式为 **dfOpaque** 时，可以通过 [Layer.holdAlpha](../reference/Layer.md#holdalpha) 属性指定是否保护绘制目标 ( 要执行方法的图层 ) 的 Alpha 通道。

保护 Alpha 通道时，Alpha 通道 (不透明度) 会受到保护，透明部分保持透明。

不保护 Alpha 通道时，Alpha 通道 (不透明度) 会被破坏。所谓被破坏，就是说会变成什么状态变得不可知。

但是，当 [Layer.type](../reference/Layer.md#type) 属性既不是 **ltAlpha** 也不是 **ltAddAlpha** 时，由于图层的 Alpha 通道不会被使用，所以即使把 Layer.holdAlpha 属性设为假，通常也没有问题。另外，设为假后，在许多方法中都能比设为真时绘制得更快。
