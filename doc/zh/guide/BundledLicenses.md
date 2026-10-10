# 随附许可证列表

<!-- 由 src/core/licenses/gen_licenses_c.py --mode table 生成 —— 禁止手动编辑。
     请编辑各 licenses/manifest.json 后重新生成。 -->

这是发布物中包含的第三方组件对照表。引擎本体 34 项 / 插件 19 项 / 字体 3 项 (其中依赖构建配置的 6 项)。

以各 `licenses/manifest.json` 为准，机制说明见 `src/core/doc/LicenseSystem.md`。许可证原文的全文位于发布物的 `licenses/` 文件夹中。

## 引擎本体

内置于引擎本体 (exe)、由 `make install` 导出到 `licenses/` 的部分。

### 引擎基础

| 组件 | 许可证 | 备注 |
|---|---|---|
| Kirikiri Z | 相当于 BSD-3-Clause | 日文原文。包含禁止将名称用于宣传的条款 |
| zlib | Zlib |  |
| libpng | libpng (PNG Ref Lib v2) |  |
| libjpeg-turbo | IJG + BSD-3-Clause | 多个许可证的复合 |
| Oniguruma | BSD-2-Clause |  |
| GLM | MIT |  |
| plog | MIT |  |
| icline | MIT |  |
| Brotli | MIT |  |
| bzip2 | bzip2 (BSD 系) |  |
| liblzma (XZ Utils) | 0BSD | 实际使用的只是 liblzma 部分 (CLI 工具类的 GPL 与之无关) |

### 文字排版 (glyphware)

| 组件 | 许可证 | 备注 |
|---|---|---|
| glyphware | MIT |  |
| FreeType | FTL / GPLv2 (双许可) | 选择 FTL 侧时，条件是在交付物中明确标注使用情况 |
| HarfBuzz | MIT (Old MIT) |  |
| SheenBidi | Apache-2.0 |  |
| picojson | BSD-2-Clause |  |

### 音频

| 组件 | 许可证 | 备注 |
|---|---|---|
| libogg | BSD-3-Clause |  |
| libvorbis | BSD-3-Clause |  |
| Opus | BSD-3-Clause |  |
| miniaudio | MIT-0 / Unlicense | 二选一 (实质上是公有领域) |

### 视频

| 组件 | 许可证 | 备注 |
|---|---|---|
| movie-player | MIT |  |
| libvpx | BSD-3-Clause |  |
| libyuv | BSD-3-Clause |  |
| nestegg | ISC |  |
| PL_MPEG | MIT |  |

### UI (Elements)

| 组件 | 许可证 | 备注 |
|---|---|---|
| Elements (cycfi) | MIT |  |
| ThorVG | MIT |  |
| JerryScript | Apache-2.0 | **仅当启用 `TVP_LICENSE_WITH_LOTTIE` 时** / 用于 Lottie Expressions 的表达式求值 |
| RapidJSON | MIT | **仅当启用 `TVP_LICENSE_WITH_LOTTIE` 时** / 用于 Lottie 解析器 |

### 平台

| 组件 | 许可证 | 备注 |
|---|---|---|
| SDL3 | Zlib | 仅 SDL 变体 |
| glad | WTFPL / CC0-1.0 + Apache-2.0 | 生成代码与 Khronos 规格的适用条件不同 |
| ANGLE | BSD-3-Clause | **仅当启用 `TVP_LICENSE_WITH_ANGLE` 时** / 在随附 libEGL / libGLESv2 的构建配置中需要。目前没有任何构建会随附它们，因此没有需要定义该宏的地方 |
| D3DCompiler | Microsoft 可再发行 | **仅当启用 `TVP_LICENSE_WITH_D3DCOMPILER` 时** / 非 OSS。Windows SDK 的可再发行组件。仅限直接链接 d3dcompiler 的 WIN 变体 |
| SDL_GameControllerDB | Zlib |  |

## 插件

各插件的 DLL 侧会在运行时注册 (汇入 `System.getLicenseList()` / `-license`)。原文在 install 时也会导出到发布物的 `licenses/plugins/` (仅限实际构建的插件的部分)。

| 插件 | 组件 | 许可证 | 备注 |
|---|---|---|---|
| clipfile | clipparse | MIT | 用于解析/写出 .clip 的不依赖吉里吉里的库 |
| clipfile | SQLite | 公有领域 | clipparse 为读取 .clip 内的元信息 DB 而随附构建 (amalgamation) |
| expat | expat | MIT |  |
| krkr_richtext | richtext | MIT |  |
| krkr_richtext | minikin | Apache-2.0 | 源自 Android 的断行 |
| krkreffekseer | Effekseer | MIT |  |
| krkreffekseer | minizip-ng | Zlib |  |
| krkrlive2d | Live2D Cubism Core | Live2D Proprietary Software License | 非 OSS。需要签订个别合同，并进行规定的版权标注 |
| krkrthreepp | threepp | MIT | three.js 的 C++ 移植 |
| krkrthreepp | VRM (Kota Iguchi) | MIT |  |
| layerExImage | CxImage | Zlib 系 (CxImage 自有条款) | 复用了部分图像处理代码 (xImaDsp) |
| layerExSave | LodePNG | Zlib | 用于 Layer.saveLayerImagePng 系列的 PNG 保存 (version 20161127) |
| layerExVector | ThorVG | MIT |  |
| layerExVector | JerryScript | Apache-2.0 | **仅当启用 `TVP_LICENSE_WITH_LOTTIE` 时** / 用于 Lottie Expressions 的表达式求值 |
| layerExVector | RapidJSON | MIT | **仅当启用 `TVP_LICENSE_WITH_LOTTIE` 时** / 用于 Lottie 解析器 |
| minizip | minizip-ng | Zlib |  |
| psdfile | psdparse | MIT |  |
| sigcheck | LibTomCrypt | 公有领域 / WTFPL (双许可) | 用于签名验证 (RSA/哈希) |
| sigcheck | LibTomMath | Unlicense (公有领域) | LibTomCrypt 的大数运算后端 |

## 其他 (字体、数据)

虽然不是代码而是数据，但只要包含在发布物中，就一律按同一列表处理。项目若要添加自有字体，不要放在 manifest 中，而应放在**游戏数据侧的 `licenses/*.txt`**，这样运行时即会汇入。

| 组件 | 许可证 | 备注 |
|---|---|---|
| Noto Fonts | OFL-1.1 |  |
| Roboto | Apache-2.0 |  |
| elements_basic (fontello icons) | OFL-1.1 | Font Awesome / Entypo / Elusive / Iconic 4 套 |
| 项目自行放置的部分 | 因项目而异 | 运行时枚举 `<データ>/licenses/*.txt` |

## 依赖构建配置的条目

有些组件在部分构建配置下连一行都不会被编译。在未定义宏的构建配置中，它们既不会出现在内置表里，也不会出现在发布物中。

| 宏 | 对象 |
|---|---|
| `TVP_LICENSE_WITH_ANGLE` | ANGLE |
| `TVP_LICENSE_WITH_D3DCOMPILER` | D3DCompiler |
| `TVP_LICENSE_WITH_LOTTIE` | JerryScript / RapidJSON |
