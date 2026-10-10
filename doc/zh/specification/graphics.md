# 图像处理功能

记载吉里吉里Z 支持的图像处理功能。

## 概要

吉里吉里Z 的图像处理以 CPU 侧的 32bpp BGRA 位图 (`tTVPBaseBitmap`) 作为合成面进行。混合 (合成运算) 与重采样 (缩放、旋转) 等像素处理通过 SIMD 实现 (SSE2 / AVX2 / NEON) 加速，同时也为无法使用 SIMD 的环境准备了 C 参考实现 (`tvpgl.c`)。

此外，还有使用 OpenGL ES 的 Canvas / Texture 的 GPU 绘制路径，可在 GPU 上进行纹理合成与基于着色器的绘制。

### 目录

[规格参数](#spec)

[可读写的图像格式](#imageformat)

[合成运算](#blend_mode)

## 规格参数 { #spec }

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- | --- | --- |
| 合成<br>运算 | 不透明 | 乘法合成 | Photoshop 兼容<br>线性减淡 (添加) 合成 (加法合成) | Photoshop 兼容<br>强光合成 | Photoshop 兼容<br>变亮合成 |
| 合成<br>运算 | Alpha 合成 | 减淡合成 | Photoshop 兼容<br>线性加深合成 (减法合成) | Photoshop 兼容<br>柔光合成 | Photoshop 兼容<br>变暗合成 |
| 合成<br>运算 | 加法 Alpha 合成 | 变亮合成 | Photoshop 兼容<br>正片叠底合成 | Photoshop 兼容<br>颜色减淡合成 | Photoshop 兼容<br>差值合成 |
| 合成<br>运算 | 加法合成 | 变暗合成 | Photoshop 兼容<br>滤色合成 | Photoshop V.5.x 及以下兼容<br>颜色减淡合成 | Photoshop V.5.x 及以下兼容<br>差值合成 |
| 合成<br>运算 | 减法合成 | 滤色合成 | Photoshop 兼容<br>叠加合成 | Photoshop 兼容<br>颜色加深合成 | Photoshop 兼容<br>排除合成 |

## 可读写的图像格式 { #imageformat }

标准状态下同时支持读取与写入的图像格式如下。

| 格式 | 扩展名 | 备注 |
| --- | --- | --- |
| BMP | .bmp | Windows 标准的位图格式。32bpp 的 BMP 被视为带 Alpha 通道。 |
| JPEG | .jpg / .jpeg | 由 libjpeg-turbo 进行解码/编码。 |
| PNG | .png | 由 libpng 进行解码/编码。支持带 Alpha 通道。 |
| TLG5 / TLG6 | .tlg | 吉里吉里独有的无损压缩格式。TLG5 以高速解压、TLG6 以高压缩率为特征。 |

此外，还支持把颜色信息的图像 (主图像) 与 Alpha 通道 (遮罩) 分离的 **主图像/遮罩分离格式**。遮罩图像是在主图像的文件名后附加 `_m` (例如 `abc.jpg` 对应 `abc_m.jpg`)。主图像与遮罩的格式不同也没有关系。

支持的图像格式可以通过插件扩展。

## 合成运算 { #blend_mode }

下面列出图层的合成运算 (图层类型)。式中的 *result* 是结果，*dest* 是叠加目标的亮度，*src* 是要叠加的图像的亮度，*α* 是每个像素的 Alpha 值，取值范围均为 0.0 ~ 1.0。`blend(a, b, r)` 表示 `a × (1.0 - r) + b × r`。

| No. | 类型 | 式 | 说明 |
| --- | --- | --- | --- |
| 1 | 不透明 | result = src | 不参照 Alpha 通道进行合成 |
| 2 | Alpha 合成 | result = blend(dest, src, α) | 进行 Alpha 合成。<br>是进行透明处理时最基本的类型。 |
| 3 | 加法 Alpha 合成 | result = min(1.0, dest × ( 1.0 - α ) + src) | 进行加法 Alpha 合成。 |
| 4 | 加法合成 | result = min(1.0, dest × ( 1.0 - α ) + src) | 进行加法合成。适合表现光晕。<br>相当于 11.Photoshop 中的“线性减淡 (添加)”，但本合成会忽略 Alpha。<br>中性色 (叠加后也不发生变化的颜色) 是黑色。 |
| 5 | 减法合成 | result = max(0.0, dest + src - 1.0)<br>※ 与 result = dest - src 的不同仅在于 src 是否反转这一点。 | 进行减法合成。Alpha 会被忽略。<br>中性色是白色。 |
| 6 | 乘法合成 | result = dest × src | 进行乘法合成。<br>Alpha 会被忽略。<br>中性色是白色。 |
| 7 | 减淡合成 | result = min(1.0, dest ÷ ( 1.0 - src ) ) | 进行减淡合成。<br>适合表现被光照亮的效果。<br>Alpha 会被忽略。<br>中性色是黑色。 |
| 8 | 变亮合成 | result = max(dest, src) | 进行“变亮”合成。<br>Alpha 会被忽略。<br>中性色是黑色。 |
| 9 | 变暗合成 | result = min(dest, src) | 进行“变暗”合成。<br>Alpha 会被忽略。<br>中性色是白色。 |
| 10 | 滤色合成 | result = 1.0 - ( 1.0 - dest ) × ( 1.0 - src ) | 进行“滤色”合成。<br>Alpha 会被忽略。<br>中性色是黑色。 |
| 11 | Photoshop 兼容<br>线性减淡 (添加) 合成<br>(加法合成) | result = blend(dest, min(1.0, dest + src), α) | 进行 Photoshop 兼容的“线性减淡 (添加)”合成 (加法合成)。<br>与 4.加法合成不同，Alpha 不会被忽略。<br>中性色是黑色。 |
| 12 | Photoshop 兼容<br>线性加深合成<br>(减法合成) | result = blend(dest, max(0.0, dest + src - 1.0), α) | 进行 Photoshop 兼容的“线性加深”合成 (减法合成)。<br>与 5.减法合成不同，Alpha 不会被忽略。<br>中性色是白色。 |
| 13 | Photoshop 兼容<br>正片叠底合成 | result = blend(dest, dest × src, α) | 进行 Photoshop 兼容的“正片叠底”合成。<br>与 6.乘法合成不同，Alpha 不会被忽略。<br>中性色是白色。 |
| 14 | Photoshop 兼容<br>滤色合成 | result = blend(dest, 1.0 - (1.0 - dest) × (1.0 - src), α) | 进行 Photoshop 兼容的“滤色”合成。<br>与 10.滤色合成不同，Alpha 不会被忽略。<br>中性色是黑色。 |
| 15 | Photoshop 兼容<br>叠加合成 | result = blend(dest, overlay(dest, src), α)<br>这里 overlay(a, b) =<br>a × b × 2.0 ( a < 0.5 时)<br>1.0 - (1.0 - a) × (1.0 - b) × 2.0 (其他情况) | 进行 Photoshop 兼容的“叠加”合成。<br>中性色是 50% 灰色。 |
| 16 | Photoshop 兼容<br>强光合成 | result = blend(dest, hardlight(dest, src), α)<br>这里 hardlight(a, b) =<br>a × b × 2.0 (b < 0.5 时)<br>1.0 - (1.0 - a) × (1.0 - b) × 2.0 (其他情况) | 进行 Photoshop 兼容的“强光”合成。<br>中性色是 50% 灰色。 |
| 17 | Photoshop 兼容<br>柔光合成 | result = blend(dest, softlight(dest, src), α)<br>这里 softlight(a, b) =<br>之后再贴入用 Latex 写的公式 | 进行 Photoshop 兼容的“柔光”合成。<br>中性色是 50% 灰色。 |
| 18 | Photoshop 兼容<br>颜色减淡合成 | result = blend(dest, min(1.0, dest ÷ ( 1.0 - src ) ), α) | 进行 Photoshop 兼容的“颜色减淡”合成。<br>与 ltDodge 不同，Alpha 不会被忽略。<br>中性色是黑色。 |
| 19 | Photoshop Ver.5.x 以下兼容<br>颜色减淡合成 | result = min(1.0, dest ÷ ( 1.0 - src × α) ) | 进行与 Photoshop 版本 5.x 及以下兼容的“颜色减淡”合成。<br>与 18.Photoshop 兼容颜色减淡合成相比，公式略有不同。<br>中性色是黑色。 |
| 20 | Photoshop 兼容<br>颜色加深合成 | result = blend(dest, max(0.0, 1.0 - (1.0 - dest) ÷ src), α) | 进行 Photoshop 兼容的“颜色加深”合成。<br>中性色是白色。 |
| 21 | Photoshop 兼容<br>变亮合成 | result = blend(dest, max(dest, src), α) | 进行 Photoshop 兼容的“变亮”合成。<br>与 8.变亮合成不同，Alpha 不会被忽略。<br>中性色是黑色。 |
| 22 | Photoshop 兼容<br>变暗合成 | result = blend(dest, min(dest, src), α) | 进行 Photoshop 兼容的“变暗”合成。<br>与 9.变暗合成不同，Alpha 不会被忽略。<br>中性色是白色。 |
| 23 | Photoshop 兼容<br>差值合成 | result = blend(dest, abs(dest - src), α) | 进行 Photoshop 兼容的“差值”合成。<br>中性色是黑色。 |
| 24 | Photoshop Ver.5.x 以下兼容<br>差值合成 | result = abs(dest - src × α) | 进行与 Photoshop 版本 5.x 及以下兼容的“差值”合成。<br>与 23.Photoshop 兼容差值合成相比，公式略有不同。<br>中性色是黑色。 |
| 25 | Photoshop 兼容<br>排除合成 | result = blend(dest, dest + src - 2.0 × src × dest, α) | 进行 Photoshop 兼容的“排除”合成。<br>中性色是黑色。 |
