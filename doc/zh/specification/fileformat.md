# 文件格式

记载吉里吉里Z 支持的文件格式。

### 目录

[文件格式](#fileformat)

## 文件格式 { #fileformat }

| 种类 | 格式 | 扩展名 | 说明 |
| --- | --- | --- | --- |
| 静态图像 | Windows 位图 (Bitmap) | .bmp | 仅支持无压缩格式。 |
| 静态图像 | JPEG | .jpg | 可在读取时指定精度。<br>可设置的值是 'high' (高)、'normal' (标准)、'low' (低) 之一。<br>默认是 'normal'。<br>low 的 IDCT 使用定点 (整数) ANN，无色差放大插值。<br>normal 的 IDCT 使用定点 (整数) ANN，有色差放大插值。<br>high 的 IDCT 使用浮点 AAN，有色差放大插值。<br>指定方法请参照[启动选项 -jpegdec (JPEG 图像解码精度)](../guide/CommandLine.md)。<br>※ 把 IDCT 使用定点 (整数) LLM、带色差放大插值作为默认会更好。 |
| 静态图像 | Portable Network Graphic (PNG) | .png | 支持 Alpha 通道与透明色指定。 |
| 静态图像 | Entis Rasterized Image format (ERI) | .eri | L.Entis 提出的无损压缩格式<br>带 Alpha 通道的也可以读取。<br>详情请参照 [ERI Developer's site](http://www.entis.jp/eridev/frame.html)。 |
| 静态图像 | TLG5 | .tlg | 吉里吉里独有格式。<br>特点是解压速度快 (约为 PNG 的 4 倍速)。<br>可用[图像格式转换器](../guide/TPC.md)转换。 |
| 静态图像 | TLG6 | .tlg | 吉里吉里独有格式。<br>压缩率比 PNG 与 TLG5 高，但解压耗时约为 TLG5 的两倍。<br>不过即便如此也约为 PNG 的 2 倍速，因此仍算高速。<br>可用[图像格式转换器](../guide/TPC.md)转换。 |
| 静态图像 | 其他 | .* | 可通过 Susie-plugin 扩展。 |
| 音频 | WAVE | .wav | 支持无压缩 WAVE 格式。 |
| 音频 | Ogg Vorbis | .ogg | 已整合到本体 (无需追加 DLL)。 |
| 音频 | Opus | .opus | 已整合到本体 (无需追加 DLL)。 |
| 音频 | 其他 | .* | 可通过插件扩展。 |
| 视频 | WebM | .webm | VP8 / VP9。支持带 Alpha (透明) 的视频。视频播放机制已整合到本体 (无需追加 DLL)。 |
| 视频 | MPEG-1 | .mpg<br>.mpeg<br>.mpv<br>.m1v<br>.dat | 仅支持 MPEG-1 (不支持 MPEG-2 及以后)。用本体整合的 pl_mpeg 解码。 |
| 视频 | MP4 | .mp4<br>.m4v<br>.mov | H.264 / HEVC。用 Media Foundation 解码 (默认硬件解码)。 |
| 视频 | Windows Media Video (WMV) | .wmv<br>.asf | 用 Media Foundation 解码。播放端需要 Windows Media 组件。 |
| 视频 | AVI | .avi | 非官方支持。仅当内部编解码器能被 Media Foundation 处理时才可播放 (不提供官方支持)。 |
| 动画 | ASD 文件 | .asd | 吉里吉里独有的动画定义格式。<br>请参照 AnimationLayer.tjs 的注释。 |
| 归档 | XP3 | .xp3 | 吉里吉里独有格式。<br>用 [Releaser](../guide/Releaser.md) 创建。 |
| 归档 | PEXP3 | .exe | 吉里吉里独有格式。<br>吉里吉里可执行文件 (krkr.eXe) 与 XP3 格式的组合形式。<br>已不推荐的形式。<br>用 [Releaser](../guide/Releaser.md) 创建。 |
| 归档 | 其他 | .* | 可通过插件扩展。 |
| 字体 | 预渲染字体 | .tft | 吉里吉里独有格式。<br>用[预渲染字体数据创建工具](../guide/FontMaker.md)生成 |
| 字体 | TrueType/OpenType 字体 | .ttf<br>.otf | 非官方支持。<br>无需把字体安装到系统即可使用。<br>需要 [addFont.dll](https://github.com/wamsoft/addFont)。仅支持 Windows。 |
