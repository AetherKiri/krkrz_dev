# CLIP

基于伪代码的手册

CLIP STUDIO PAINT (.clip) 读取 / 编辑插件 clipfile.dll

CLIP 文件存储功能
可以通过以下路径名将 CLIP 文件的图层图像直接作为文件加载

clip://CLIP文件名/root/文件夹名/.../图层名.bmp
clip://CLIP文件名/id/LayerId.bmp

・CLIP 文件名仅使用基本名，并以小写规范化
・文件夹名、图层名全部以小写规范化，其中包含的 "/" 会被替换为 "_"
・名称重复时，后面的优先
・不持有图像的图层 (文件夹、调整图层、空图层) 不会被列出

与 psdfile 插件的 psd:// 规则相同。

## 成员列表

### 属性

- [width](#width)
- [height](#height)
- [resolution](#resolution)
- [layer_count](#layer_count)
- [root_layer](#root_layer)
- [is_loaded](#is_loaded)
- [error](#error)

### 方法

- [load](#load)
- [loadOctet](#loadoctet)
- [clearData](#cleardata)
- [getLayerName](#getlayername)
- [getLayerInfo](#getlayerinfo)
- [getRoots](#getroots)
- [getChildren](#getchildren)
- [getLayerIndexById](#getlayerindexbyid)
- [getLayerAttribute](#getlayerattribute)
- [getLayerData](#getlayerdata)
- [getLayerDataRaw](#getlayerdataraw)
- [getLayerDataMask](#getlayerdatamask)
- [getLayerRegion](#getlayerregion)
- [getBlend](#getblend)
- [getPreviewPNG](#getpreviewpng)
- [check](#check)
- [clearStorageCache](#clearstoragecache)

---

### width

属性 \ 访问: `r`

**说明**

画布的宽度 (实际像素)。

CLIP 的 Canvas.CanvasWidth 依赖 CanvasUnit，存在以 mm 为单位的文件，
因此返回从 100% mipmap 的属性求得的实际像素值。未加载时为 -1

---

### height

属性 \ 访问: `r`

**说明**

画布的高度 (实际像素)。未加载时为 -1

---

### resolution

属性 \ 访问: `r`

**说明**

分辨率 (dpi)。未加载时为 0

---

### layer_count

属性 \ 访问: `r`

**说明**

图层数。未加载时为 -1

---

### root_layer

属性 \ 访问: `r`

**说明**

根文件夹的 LayerId。未加载时为 -1

---

### is_loaded

属性 \ 访问: `r`

**说明**

是否已加载

---

### error

属性 \ 访问: `r`

**说明**

最近一次失败的原因。没有则为空字符串

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |

**返回值**

加载成功时为 true (失败原因见 error 属性)

**说明**

加载 CLIP 文件。

本地有实体的文件以 mmap 打开，像素只在需要时按 256x256 块为单位
读取 (即使文件很大，load 本身也很轻)。
在归档内等无法落到本地路径的情况下，会先将整体从流读入内存
再解析。

---

### loadOctet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `data` | `&nbsp;` | 存放了整个文件的 octet |

**返回值**

加载成功时为 true

**说明**

加载放入 octet 的 CLIP 数据。

字节序列由本对象持有。由于没有文件名，
不会注册到 clip:// 存储中。

---

### clearData

方法

**说明**

显式丢弃所持有的数据。

吉里吉里的对象寿命依赖 GC，因此在不想一直持有大文件时调用。

---

### getLayerName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

图层名

**说明**

获取图层名

---

### getLayerInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

内含图层信息的字典
字典的内容
left         左坐标 (画布坐标)
top          上坐标
right        右坐标
bottom       下坐标
width        宽度
height       高度
name         图层名
layer_id     LayerId (CLIP 的 Layer.MainId)。CLIPWriter 的各方法以及
clip://~/id/ 使用的就是这个值
visible      显示状态
opacity      不透明度 0..255 (与 PSD / 吉里吉里 对齐的值)
opacity_raw  不透明度的原始值 0..**256** (CLIP 为 256 级)
clipping     是否由下层图层裁剪 (0/1)
composite    合成模式的原始值 (CLIP 的 LayerComposite。与 CLIPWriter 的
composite_* 常量相同的值)
type         合成模式 (吉里吉里的对应模式)。没有对应模式时会
落到 ltPsNormal，因此想准确查看时请使用 composite
blend_mode_key 以 PSD 的 4 个字符编码表示合成模式。用于与 psdfile 的
getLayerInfo().blend_mode_key 对照
is_group     是否为文件夹图层
is_filter    是否为调整图层 (自身不持有像素)
is_text      是否为文本图层
has_mask     是否持有图层遮罩
folder       文件夹属性的原始值 (bit0=文件夹 / bit4=折叠)
collapsed    文件夹是否已折叠
layer_type_raw LayerType 的原始值 (bit12(4096)=调整图层 / bit1(2)=有遮罩)
parent_index 父文件夹的图层编号 (最顶层为 -1)
children     直接子项的图层编号数组 (从下到上)。文件夹以外为空数组

**说明**

获取图层信息

图层编号 no 为 0 到 layer_count-1，排列顺序与 psdfile 相同的
“内容在前、文件夹在后、从下到上”的平坦顺序。

---

### getRoots

方法

**返回值**

图层编号的数组

**说明**

获取最顶层 (根直下) 的图层编号数组。从下到上的顺序

---

### getChildren

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

图层编号的数组 (文件夹以外为空数组)

**说明**

获取文件夹的直接子项的图层编号数组。从下到上的顺序

---

### getLayerIndexById

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | getLayerInfo().layer_id 的值 |

**返回值**

图层编号。找不到时为 -1

**说明**

由 LayerId 反查图层编号

---

### getLayerAttribute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |
| `mask` | `false` | 为 true 时查看遮罩一侧的 mipmap 链。默认为 false |

**返回值**

%[ width:, height:,        // 逻辑大小
cols:, rows:,           // 块网格
color_mode:             // 33=RGBA / 17=灰度、单色 / 1=遮罩
num_channels:           // 4 / 1 / 0
bit_depth:              // 5=8bpp RGBA / 2=8bpp / 1=1bpp
plane_bytes:,
block_width:, block_height:,
has_init_color:,
init_color:             // 将 RGBA 打包后的值
block_count:            // 块数
]  没有实体时为 void

**这里返回的 width / height 并不一定是画布大小** — CSP 会
根据图层，以向上取整到 256x256 块边界的大小 (300x400 的画布也可能是
512x512 等) 持有像素。传给 `CLIPWriter.setPixels` 的 Layer 的大小需要
与此值一致，因此在改写时请在这里查询。

**说明**

获取 100% mipmap 的 Offscreen 属性 (用于确认块网格或表现色)

---

### getLayerData

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 读取目标的图层 |
| `no` | `&nbsp;` | 图层编号<br>文件夹、调整图层、空图层不持有图像，因此什么都不做<br>(因为吉里吉里的 Layer 不能为 0 大小)。<br>除数据内容外，以下属性会被自动设置到图层<br>left          左坐标<br>top           上坐标<br>width         宽度<br>height        高度<br>type          合成模式<br>opacity       不透明度 (归一化为 0..255 的值)<br>visible       显示状态<br>imageLeft     会变为 0<br>imageTop      会变为 0<br>imageWidth    会变为 width<br>imageHeight   会变为 height<br>name          会被设置 name |

**说明**

读取图层图像 (已将遮罩融入 Alpha 的版本)

---

### getLayerDataRaw

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 读取目标的图层 |
| `no` | `&nbsp;` | 图层编号 |

**说明**

读取图层图像 (不融入遮罩的原始图像)。

设置的属性与 getLayerData 相同

---

### getLayerDataMask

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 读取目标的图层 |
| `no` | `&nbsp;` | 图层编号 |

**说明**

只读取图层的遮罩 (灰度)。

不持有遮罩的图层什么都不做。
opacity 会变为 255，type 会变为 ltPsNormal

---

### getLayerRegion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 读取目标的图层 |
| `no` | `&nbsp;` | 图层编号 |
| `x` | `&nbsp;` | 矩形的左 (画布坐标) |
| `y` | `&nbsp;` | 矩形的上 |
| `w` | `&nbsp;` | 矩形的宽度 |
| `h` | `&nbsp;` | 矩形的高度 |
| `mode` | `image_mode_masked` | image_mode_* (默认为 image_mode_masked) |

**说明**

只读取图层图像中指定矩形 (画布坐标) 的部分。

CLIP 以 256x256 瓦片持有像素，因此**只有重叠的瓦片会被
展开**。只想获取大图层的一部分时，用这个开销更低
(PSD 是行 RLE，因此做不到同样的事 = clipparse 特有的入口)。
读取目标的 Layer 的 left/top 会被设置为 x/y。

---

### getBlend

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 存放目标的图层 (会被调整为画布大小) |

**返回值**

获取成功时为 true

**说明**

获取将所有图层从下到上合成的图像。

与 psdfile 的 getBlend “只读取已保存到 PSD 的合成结果”不同，
这边由 clipparse 侧实际进行合成 (与 CSP 的 CanvasPreview 一致才是
正确状态)。支持 27 种合成模式、4 种表现色、遮罩、裁剪、
穿透文件夹、5 种调整图层。
如果只是想直接使用已保存的成品图，用 getPreviewPNG() 开销更低。

---

### getPreviewPNG

方法

**返回值**

PNG 数据的 octet。没有则为 void

**说明**

以 PNG 的 octet 返回嵌入文件中的成品图 (CanvasPreview)。

它本身是 CSP 保存的图像，因此无需合成计算，但**不一定是等倍**。

---

### check

方法

**返回值**

有问题时返回报告字符串，没有问题时为 void

**说明**

对全部块运行结构断言 (诊断用)

---

### clearStorageCache

方法

**说明**

静态方法

清除作为存储持有的缓存

---
