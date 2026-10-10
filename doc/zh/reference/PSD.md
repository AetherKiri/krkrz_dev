# PSD

基于伪代码的手册

PSD 文件存储功能
可以用以下的路径名把 PSD 文件的图层图像直接作为文件加载

psd://PSD文件名/root/文件夹名/.../图层名.bmp
psd://PSD文件名/id/图层ID.bmp

- PSD 文件名只取基本名，并以小写规范化
- 文件夹名、图层名全部以小写规范化，其中包含的 “/” 会被替换为 “_”
- 名称重复时，后面的优先

## 成员列表

### 属性

- [width](#width)
- [height](#height)
- [channels](#channels)
- [depth](#depth)
- [color_mode](#color_mode)
- [layer_count](#layer_count)
- [hresolution](#hresolution)
- [vresolution](#vresolution)
- [merged_alpha](#merged_alpha)

### 方法

- [load](#load)
- [loadOctet](#loadoctet)
- [clear](#clear)
- [assignAutoIds](#assignautoids)
- [getLayerType](#getlayertype)
- [getLayerName](#getlayername)
- [getLayerInfo](#getlayerinfo)
- [getLayerData](#getlayerdata)
- [getLayerDataRaw](#getlayerdataraw)
- [getLayerDataMask](#getlayerdatamask)
- [getSlices](#getslices)
- [getGuides](#getguides)
- [getBlend](#getblend)
- [getLayerComp](#getlayercomp)
- [getLayerMask](#getlayermask)
- [getLayerBlendingRanges](#getlayerblendingranges)
- [getLayerSheetColor](#getlayersheetcolor)
- [getLayerInfoKeys](#getlayerinfokeys)
- [getLayerDescriptor](#getlayerdescriptor)
- [getLayerDescriptorBytes](#getlayerdescriptorbytes)
- [getLayerEffects](#getlayereffects)
- [getLayerFill](#getlayerfill)
- [getColorTable](#getcolortable)
- [getGlobalLayerMask](#getgloballayermask)
- [getImageResourceIds](#getimageresourceids)
- [getImageResource](#getimageresource)
- [getICCProfile](#geticcprofile)
- [getEXIF](#getexif)
- [getXMP](#getxmp)
- [getThumbnail](#getthumbnail)
- [save](#save)
- [createBlank](#createblank)
- [deleteLayer](#deletelayer)
- [moveLayer](#movelayer)
- [groupSpan](#groupspan)
- [moveLayerSibling](#movelayersibling)
- [moveLayerRange](#movelayerrange)
- [duplicateLayer](#duplicatelayer)
- [copyLayerFrom](#copylayerfrom)
- [setLayerName](#setlayername)
- [setFillOpacity](#setfillopacity)
- [setLayerOpacity](#setlayeropacity)
- [setLayerClipping](#setlayerclipping)
- [setLayerVisible](#setlayervisible)
- [setLayerBlendMode](#setlayerblendmode)
- [setLayerEffects](#setlayereffects)
- [setLayerDescriptor](#setlayerdescriptor)
- [setMaskDisabled](#setmaskdisabled)
- [setMaskDensity](#setmaskdensity)
- [setMaskFeather](#setmaskfeather)
- [setMaskDefaultColor](#setmaskdefaultcolor)
- [setLayerPixels](#setlayerpixels)
- [setLayerMaskPixels](#setlayermaskpixels)
- [addLayer](#addlayer)
- [setMergedImage](#setmergedimage)
- [setLayerText](#setlayertext)
- [setLayerRunStyle](#setlayerrunstyle)
- [setLayerRichText](#setlayerrichtext)
- [setLayerJustification](#setlayerjustification)
- [getLayerFonts](#getlayerfonts)
- [getLayerTextTransform](#getlayertexttransform)
- [setLayerTextTransform](#setlayertexttransform)
- [moveTextLayer](#movetextlayer)
- [getLayerTextBounds](#getlayertextbounds)
- [setLayerTextBounds](#setlayertextbounds)
- [clearStorageCache](#clearstoragecache)

---

### width

属性 \ 访问: `r`

**说明**

图像的基本属性

---

### height

属性 \ 访问: `r`

**说明**

图像高度

---

### channels

属性 \ 访问: `r`

**说明**

通道数

---

### depth

属性 \ 访问: `r`

**说明**

每通道的位数 (1/8/16/32)

---

### color_mode

属性 \ 访问: `r`

**说明**

颜色模式

---

### layer_count

属性 \ 访问: `r`

**说明**

图层数

---

### hresolution

属性 \ 访问: `r`

**说明**

水平分辨率 (dpi，默认 72，image resource 1005)

---

### vresolution

属性 \ 访问: `r`

**说明**

垂直分辨率 (dpi，默认 72)

---

### merged_alpha

属性 \ 访问: `r`

**说明**

合成图像是否包含 Alpha 通道

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 |

**返回值**

加载成功时返回 true

**说明**

PSD 图像的加载

---

### loadOctet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `data` | `&nbsp;` | 存放整个 PSD 文件的 octet |

**返回值**

加载成功时返回 true

**说明**

加载放入 octet 的 PSD 数据。

字节序列会被复制到内部缓冲区，因此调用后丢弃 octet 也没有问题。
由于不带文件名，不会被注册到 psd:// 存储中。

---

### clear

方法

**说明**

显式丢弃持有的数据。

吉里吉里的对象寿命依赖 GC，因此在不想一直持有大 PSD 的时候调用。
之后的读取类操作会变成 "no data" 异常。

---

### assignAutoIds

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `base_id` | `0` | 分配的 ID 最小编号 -1 (※如果已有的任一图层 ID 比它大，则使用那个值) |

**返回值**

设置了 ID 的图层数量

**说明**

对未设置 LayerID 的图层自动分配 ID 编号 (从 base_id+1 起按 layer_no 顺序)

由于 Photoshop 兼容系的 psd 保存工具存在不分配图层 ID 的情况，会有 psd://~/id/ 无法正确加载的问题
基本上推荐在 load 之后立即调用

---

### getLayerType

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

图层种类

**说明**

获取图层种类

---

### getLayerName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

图层名称

**说明**

获取图层的名称

---

### getLayerInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

存放图层信息的字典
字典的内容
layer_type   图层种类
top          上坐标
left         左坐标
bottom       底坐标
right        右坐标
width        宽度
height       高度
blend_mode   合成模式 (blend_mode_*。未知模式为 blend_mode_invalid)
blend_mode_key PSD 上的原始合成模式键 (4 个字符。注意 3 字符的键末尾会带上空白
"mul " 等)。未知模式也能原样得到，因此
若要把读到的值原样写回，请把它传给 setLayerBlendMode
opacity      不透明度
fill_opacity 填充的不透明度
visible      显示状态
name         图层名
layer_id     图层ID
group_layer_id 父图层ID
parent_index 父文件夹的图层编号 (顶层为 -1)。layer_id 在部分 PSD 中
可能未设置 (-1)，因此要构建层级时用这个更可靠。
结构性编辑 (deleteLayer/moveLayer/duplicateLayer/addLayer 等) 之后
也会重新计算
type         合成模式（吉里吉里支持的模式)
clipping	是否为裁剪遮罩的对象？
mask		是否持有图层遮罩？
mask_params  遮罩参数 (density/feather)。仅存在于持有遮罩且参数
块实际存在的图层。只持有被指定的项目
%[ user_density:   // 用户遮罩浓度 0..255
user_feather:   // 用户遮罩模糊 (px)
vector_density: // 矢量遮罩浓度 0..255
vector_feather: // 矢量遮罩模糊 (px)
]
layer_comp    图层复合信息 (以复合 ID 为键的字典)
%[ <id>: [ id,       // 复合 ID (请参阅 getLayerComp())
offset_x, // 图层的 X 偏移
offset_y, // 图层的 Y 偏移
enable,   // 显示状态标志
],... ]
text         文本图层信息 (仅在文本图层 layer_type==layer_type_text 时存在。
其他图层中该键本身不存在)
%[ text:          // 正文整体 (换行为回车字符 CR)
orientation:   // "horizontal" 或 "vertical"(竖排)
justification: // 首个段落的对齐 0=左 1=右 2=居中
transform:     // 仿射变换 `[ xx, xy, yx, yy, tx, ty ]` (tx,ty=平移)
runs: [        // 文字样式的 run 数组 (正文的排列顺序)
%[ length:       // 适用字符数 (UTF-16 代码单元。emoji 等代理为 2)
font:         // 解析完成的字体名
size_px:      // 字体大小 (pt)
color:        // RGBA 各 0..1 的数组 `[ r, g, b, a ]` (未指定则不存在)
tracking:     // 字距调整 (字送进，1/1000 em)
kerning:      // 手动字距调整
auto_kerning: // 自动字距调整 (度量/视觉) 是否启用
bold:         // 仿粗体 (FauxBold)
italic:       // 仿斜体 (FauxItalic)
underline:    // 下划线 (Underline)
],... ]
paragraphs: [   // 各段落的对齐 (用于 box text 中按段落改变对齐)
%[ length:        // 段落的字符数 (UTF-16 代码单元)
justification: // 对齐 0=左 1=右 2=居中
],... ]
]
以下 additional information （※详情请参阅 PSD 规格文档）
obsolete
transparency_protected
pixel_data_irrelevant

**说明**

获取图层的信息

---

### getLayerData

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 读取目标图层 |
| `no` | `&nbsp;` | 图层编号<br>仅在 layer_type 为 layer_type_normal 时可以读取<br>以图像与遮罩合成后的状态读取。<br>除数据内容外，以下属性会被自动设置到图层上<br>left          左坐标<br>top           上坐标<br>width         宽度<br>height        高度<br>type          合成模式<br>opacity       不透明度<br>fill_opacity	 填充的不透明度<br>visible       显示状态<br>imageLeft     变为 0<br>imageTop      变为 0<br>imageWidth    变为 width<br>imageHeight   变为 height<br>name          被设置 name |

**说明**

图层数据的读取

---

### getLayerDataRaw

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 读取目标图层 |
| `no` | `&nbsp;` | 图层编号<br>仅在 layer_type 为 layer_type_normal 时可以读取<br>仅读取图像。<br>除数据内容外，以下属性会被自动设置到图层上<br>left          左坐标<br>top           上坐标<br>width         宽度<br>height        高度<br>type          合成模式<br>opacity       不透明度<br>fill_opacity	 填充的不透明度<br>visible       显示状态<br>imageLeft     变为 0<br>imageTop      变为 0<br>imageWidth    变为 width<br>imageHeight   变为 height<br>name          被设置 name |

**说明**

图层数据的读取

---

### getLayerDataMask

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 读取目标图层 |
| `no` | `&nbsp;` | 图层编号<br>仅在 layer_type 为 layer_type_normal 时可以读取<br>仅读取遮罩。<br>在遮罩的图像尺寸为 0 且只设置了 defualtMaskColor 的情况下，<br>为了回避“无法把图层尺寸设置为 0”这一吉里吉里的限制，<br>会创建 (0,0)-(1,1) 最小尺寸的图层作为替代，并用 defaultMaskColor 填充后返回。<br>除数据内容外，以下属性会被自动设置到图层上<br>left          左坐标<br>top           上坐标<br>width         宽度<br>height        高度<br>type          合成模式<br>opacity       不透明度<br>fill_opacity	 填充的不透明度<br>visible       显示状态<br>imageLeft     变为 0<br>imageTop      变为 0<br>imageWidth    变为 width<br>imageHeight   变为 height<br>name          被设置 name<br>defaultMaskColor  获取区域外的遮罩颜色 (始终为 0 或 255 之一) |

**说明**

图层数据的读取

---

### getSlices

方法

**返回值**

切片信息字典 %[ top, left, bottom, right, slices:[ %[ id, group_id, left, top, bottom, right ], ... ] ]
没有切片信息时返回 void
最后一个切片似乎是包含全部切片尺寸的切片

**说明**

切片数据的读取

---

### getGuides

方法

**返回值**

参考线信息字典 %[ vertical:[ x1, x2, ... ], horizontal:[ y1, y2, ... ] ]
没有参考线信息时返回 void

**说明**

参考线数据的读取

---

### getBlend

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 存放目标图层 |

**返回值**

获取成功时返回 true

**说明**

获取合成结果。

并不是在库中进行合成，而是读取 PSD 中保存的合成结果。
根据保存方式的不同，该图像可能不存在。
另外，在不含图层的颜色模式 (二值、索引颜色) 下，
必须用该方法获取图像数据。

---

### getLayerComp

方法

**返回值**

参考线信息字典 %[ last_applied_id,  // Photoshp 上最后处于应用状态的 id
comps:[id,                // 复合 ID
record_visibility, // 是否记录显示/隐藏
record_position,   // 是否记录位置
record_appearance, // 是否记录外观 (图层效果)
name,              // 复合名称
comment,           // 注释
],... ]
没有复合信息时返回 void

- record_xxx 标志未立起时，会继承最后应用的复合 (不是 last_applied_id，
而是在程序中最后应用的复合) 的状态
- 与复合 ID 对应的各图层显示状态信息，存放在图层信息的 layer_comp
属性中以复合 ID 为键的字典里。

**说明**

图层复合数据的读取

---

### getLayerMask

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

%[ top:, left:, bottom:, right:, // 遮罩矩形
width:, height:,
default_color:  // 遮罩区域外的值 0..255
flags:          // 原始标志字节
relative:       // 位置是否相对于图层 (bit0)
disabled:       // 遮罩是否禁用 (bit1)
inverted:       // 反转 (bit2、已废弃规格)
from_render:    // 是否来自其他数据的渲染 (bit3)
has_parameters: // 是否持有 density/feather 块 (bit4)
user_density:   // 用户遮罩浓度 0..255 (没有时键本身不存在)
user_feather:   // 用户遮罩模糊 (px，同上)
vector_density: // 矢量遮罩浓度 (同上)
vector_feather: // 矢量遮罩模糊 (同上)
real: %[        // real/user mask (没有时键本身不存在)
flags:, background:,
top:, left:, bottom:, right:, // 外接 (enclosing) 矩形
]
]  不持有遮罩时返回 void

**说明**

获取图层遮罩的详细信息

======================================================================== 读取类元数据 把 getLayerInfo() 中没有列入的详细信息单独取出的入口。 没有相应数据时一律返回 void (不作为异常)。 ========================================================================

---

### getLayerBlendingRanges

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

%[ gray:     %[ source:, dest: ],
channels: [ %[ source:, dest: ],... ]
]  没有混合范围块时返回 void

**说明**

获取图层的混合范围。source/dest 是 32bit 的原始值，

上下 16bit 中填入黑侧/白侧的范围 (详情请参阅 PSD 规格文档)。

---

### getLayerSheetColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

%[ index: // 0..11
name:  // "none" "red" "orange" "yellow" "green" "blue"
// "violet" "gray" "seafoam" "indigo" "magenta" "fuschia"
]  没有 lclr 块时返回 void
(index 0/"none" 是“显式地无标签”，因此与 void 相区分)

**说明**

获取图层面板的颜色标签 ('lclr')

---

### getLayerInfoKeys

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

键字符串 (4 个字符) 的数组

**说明**

获取图层持有的附加图层信息块的 4CC 键列表。

用于调查可以传给 getLayerDescriptor / getLayerDescriptorBytes 的键。

---

### getLayerDescriptor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |
| `key` | `&nbsp;` | 4 个字符的键 ("lfx2" 等) |
| `skip` | `-1` | 描述符本体之前的版本前缀字节数。<br>-1 时对已知键 (lfx2/SoCo/GdFl/PtFl/SoLd/SoLE/vstk/CgEd/vscg/vogk)<br>自动判定，其他情况为 0。默认 -1 |

**返回值**

字典。没有键或无法解析时返回 void

**说明**

把附加图层信息块作为 Photoshop 描述符字典化。

根据类型转换如下:
整数/实数     → 数值
布尔值        → 1/0
字符串        → 字符串
UnitFloat    → %[ value:, unit: ]  unit 为 "points" "millimeters" "angle"
"density" "distance" "none" "percent"
"pixels" 之一
Enumerated   → %[ type:, value: ]
List         → 数组
Descriptor   → 字典 (嵌套)
RawData      → octet
Class/Alias  → 字符串
Reference    → void

---

### getLayerDescriptorBytes

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |
| `key` | `&nbsp;` | 4 个字符的键 |

**返回值**

octet。没有键时返回 void

**说明**

获取附加图层信息块的原始字节

---

### getLayerEffects

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

字典。没有效果时返回 void

**说明**

获取图层效果 ('lfx2') 的描述符字典。

投影/发光/叠加/描边/斜面等以嵌套字典的形式存入。
与 getLayerDescriptor(no, "lfx2") 相同。

---

### getLayerFill

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | 图层编号 |

**返回值**

%[ type: // "solid" / "gradient" / "pattern"
data: // 描述符字典
]  不是填充图层时返回 void

**说明**

获取填充图层的内容 ('SoCo' 纯色/'GdFl' 渐变/'PtFl' 图案)

---

### getColorTable

方法

**返回值**

%[ valid_count:        // 有效条目数
transparency_index: // 透明色索引 (-1 表示没有)
colors: [ 0xAARRGGBB, ... ] // 始终为 256 条目
]  没有颜色表时返回 void

**说明**

获取颜色表 (索引颜色文档的调色板)

---

### getGlobalLayerMask

方法

**返回值**

%[ overlay_color_space:,
color: [ c1, c2, c3, c4 ],
opacity: // 0..100
kind:    // 0=反转 / 1=全遮罩 / 128=每个图层
]  块为空/不存在时返回 void

**说明**

获取 global layer mask info (用于显示遮罩的叠加颜色)

---

### getImageResourceIds

方法

**返回值**

ID (整数) 的数组

**说明**

获取文档持有的图像资源 ID 列表

---

### getImageResource

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 资源 ID (1039=ICC 配置文件，1058=EXIF，1060=XMP，<br>1036/1033=缩略图，1005=分辨率，1032=网格/参考线 等) |

**返回值**

octet。没有相应资源时返回 void

**说明**

获取图像资源的原始字节。解码由调用方负责。

---

### getICCProfile

方法

**说明**

ICC 配置文件 (资源 1039) 的原始字节。没有时返回 void

---

### getEXIF

方法

**说明**

EXIF (资源 1058) 的原始字节。没有时返回 void

---

### getXMP

方法

**返回值**

字符串。没有时返回 void

**说明**

以字符串形式获取 XMP 包 (资源 1060)。内容是 UTF-8 的 XML。

如果考虑到可能包含非法的 UTF-8，请用 getImageResource(1060)
获取原始字节。

---

### getThumbnail

方法

**返回值**

%[ format:      // "jpeg"(JFIF JPEG) 或 "raw"
width:, height:,
bits:        // 每像素的位数
resource_id: // 1036 或 1033
data:        // 载荷的 octet (除去 28 字节的头之后的部分)
]  没有缩略图时返回 void

**说明**

获取嵌入的缩略图 (资源 1036=RGB 顺序 / 旧 1033=BGR 顺序)

---

### save

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 保存目标文件名 (本地路径) |

**返回值**

成功时返回 true

**说明**

将当前内容作为 PSD 文件写出

======================================================================== 编辑类 API (psdparse v0.7+ 的编辑功能。可从 psdfile.dll 使用) 都只是操作 in-memory 的内容，实际的字节序列会在 save() 时 重新构建。像素/图层添加类仅支持 8bit RGB 文档。编辑后 psd:// 存储的图层检索缓存会被丢弃。 注意: 合成图像 (getBlend 的来源) 即使编辑也仍然保持旧内容 (直到在 Photoshop 中打开并重新合成才会反映)。文本的字形也不会 被重绘，因此正文/格式/布局的更改要体现在画面上， 只有在 Photoshop 中重新打开时。 ========================================================================

---

### createBlank

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |
| `mode` | `color_mode_rgb` | 颜色模式 (color_mode_*，默认 color_mode_rgb)。<br>**目前 color_mode_rgb 以外会返回 false**<br>(支持新建的只有 8bit RGB)。<br>像素编辑类 (addLayer/setLayerPixels/setMergedImage) 同样<br>仅支持 8bit RGB 文档 |

**返回值**

成功时返回 true

**说明**

把该 PSD 初始化为空的 8bit 文档 (白色的合成图像)。

之后可以用 addLayer(...) 添加图层并 save()。

---

### deleteLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |

**返回值**

成功时返回 true (超出范围时返回 false)

**说明**

删除 1 个图层

---

### moveLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 移动源图层编号 |
| `to` | `&nbsp;` | 移动目标 (删除后列表中的插入位置) |

**返回值**

成功时返回 true

**说明**

把图层从 from 移动到 to

---

### groupSpan

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |

**返回值**

%[ start: // 块的首个图层编号
count: // 块的数量
]  超出范围时返回 void

**说明**

返回图层在图层列表上占据的“块”。

对于文件夹 (layer_type_folder)，范围从对应的分隔图层 (layer_type_hidden) 到
自身 (嵌套的也包含在内)，除此之外只有自身 1 个。
与 moveLayerRange 组合使用可以整体移动文件夹。

---

### moveLayerSibling

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `up` | `true` | 为 true 时在图层面板显示上向上一个 (在图层列表中靠后)。<br>默认 true |

**返回值**

移动后的图层编号。已到边缘无法移动时或超出范围时返回 -1

**说明**

把图层与同一层级的相邻兄弟交换。

文件夹以分隔图层+内容汇总后的块移动，相邻项是文件夹时则整个块越过。
不进行跨层级的移动。

---

### moveLayerRange

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `from` | `&nbsp;` | 移动源起始图层编号 |
| `count` | `&nbsp;` | 移动的数量 |
| `to` | `&nbsp;` | 移动目标 (“取出之前”的图层列表中的索引) |

**返回值**

成功时返回 true (参数非法时返回 false)

**说明**

把图层列表上的 [from, from+count) 范围整体移动到 to 的位置

(低层 API。要整体移动文件夹时传入 groupSpan 的返回值)。

---

### duplicateLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |

**返回值**

复制出的新图层编号 (失败时返回 -1)

**说明**

复制图层 (插入到原图层之后)

---

### copyLayerFrom

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` | 复制源 PSD 实例 |
| `srcIndex` | `&nbsp;` | 复制源图层编号 |
| `destIndex` | `&nbsp;` | 插入位置 (负值表示末尾) |

**返回值**

新图层编号 (失败时返回 -1)

**说明**

从另一个 PSD 实例复制并插入图层。

颜色模式/位深度必须一致。复制源 PSD 需要
生存到该 PSD 的 save() 结束为止。

---

### setLayerName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `name` | `&nbsp;` | 新的名称 |

**返回值**

成功时返回 true

**说明**

重命名图层 (同时更新 pascal 名 + luni 名)

---

### setFillOpacity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `opacity` | `&nbsp;` | 0..255 |

**返回值**

成功时返回 true

**说明**

编辑填充不透明度 (fill opacity)

---

### setLayerOpacity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `opacity` | `&nbsp;` | 0..255 (超出范围会被钳制) |

**返回值**

成功时返回 true (图层编号超出范围时返回 false)

**说明**

编辑不透明度

---

### setLayerClipping

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `clipping` | `&nbsp;` | 0=base / 1=non-base (裁剪对象) |

**返回值**

成功时返回 true

**说明**

编辑是否为裁剪遮罩的对象

---

### setLayerVisible

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `visible` | `&nbsp;` | 是否显示 |

**返回值**

成功时返回 true

**说明**

编辑显示状态

---

### setLayerBlendMode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `mode` | `&nbsp;` | blend_mode_* 常量，或 PSD 上的原始键字符串 (4 个字符。<br>"norm" "mul " "scrn" 等。3 字符的键必须带末尾空白)。<br>可以直接传入 getLayerInfo().blend_mode_key 的值 |

**返回值**

成功时返回 true

**说明**

编辑合成模式

---

### setLayerEffects

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `changes` | `&nbsp;` | 部分字典 |

**说明**

编辑图层效果 ('lfx2') 的值。

changes 是与 getLayerEffects() 相同形式的“部分字典”，只有指定的叶节点的值会被
覆盖。结构/类 ID/类型/键顺序保持不变，未指定的项目以及
描述符侧不存在的键会被忽略 (因此能保持字节一致)。
值的给出方式:
数值/字符串/布尔值 → 原样
UnitFloat        → %[ value: ] 或原始数值 (不更改单位)
Enumerated       → %[ type:, value: ] 或只有值的字符串
List             → 数组 (从开头起按顺序覆盖到已有元素数为止)
Descriptor       → 字典 (以嵌套方式合并)
不持有 lfx2 块的图层会抛出异常。

---

### setLayerDescriptor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `key` | `&nbsp;` | 4 个字符的键 |
| `changes` | `&nbsp;` | 部分字典 |
| `skip` | `-1` | 描述符本体之前的版本前缀字节数<br>(-1 时对已知键自动判定。默认 -1) |

**说明**

针对任意附加图层信息键的 setLayerEffects 通用版

(填充图层的 'SoCo'/'GdFl'/'PtFl' 等)。
不持有相应键的图层会抛出异常。

---

### setMaskDisabled

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `disabled` | `&nbsp;` | 是否禁用遮罩 |

**返回值**

成功时返回 true

**说明**

编辑遮罩禁用标志 (仅限持有遮罩的图层)

---

### setMaskDensity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `density` | `&nbsp;` | 0..255 |

**返回值**

成功时返回 true

**说明**

编辑用户遮罩浓度 (仅限持有遮罩的图层)

---

### setMaskFeather

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `feather` | `&nbsp;` | 模糊半径 (px) |

**返回值**

成功时返回 true

**说明**

编辑用户遮罩模糊 (仅限持有遮罩的图层)

---

### setMaskDefaultColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `color` | `&nbsp;` | 0..255 |

**返回值**

成功时返回 true

**说明**

编辑遮罩默认色 (仅限持有遮罩的图层)

---

### setLayerPixels

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `layer` | `&nbsp;` | 像素提供来源 Layer |

**返回值**

成功时返回 true

**说明**

用 Layer 对象的内容替换已有图层的像素。

会取入 Layer 的 imageWidth×imageHeight、BGRA。left/top 保持不变，
width/height 会被更新。仅限 8bit RGB 文档。

---

### setLayerMaskPixels

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `layer` | `&nbsp;` | 遮罩提供来源 Layer |
| `top` | `&nbsp;` | 遮罩上端 |
| `left` | `&nbsp;` | 遮罩左端 |

**返回值**

成功时返回 true

**说明**

用 Layer 对象的内容 (把 B 分量作为灰度使用) 替换

图层的遮罩像素。遮罩矩形也会设置为 (top,left,imageWidth,imageHeight)。
没有遮罩时新建。仅限 8bit 文档。

---

### addLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 图层名 |
| `left` | `&nbsp;` | 左坐标 |
| `top` | `&nbsp;` | 上坐标 |
| `layer` | `&nbsp;` | 像素提供来源 Layer |
| `blendMode` | `blend_mode_normal` | 合成模式 (blend_mode_*，默认 blend_mode_normal) |
| `opacity` | `255` | 不透明度 0..255 (默认 255) |
| `destIndex` | `-1` | 插入位置 (负值表示末尾) |

**返回值**

新图层编号 (失败时返回 -1)

**说明**

添加新的图像图层。会取入 Layer 的 imageWidth×imageHeight、BGRA。

仅限 8bit RGB 文档。

---

### setMergedImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 像素提供来源 Layer |

**返回值**

成功时返回 true

**说明**

用 Layer 的内容替换合成图像 (预览/getBlend 的来源)。

Layer 的尺寸必须与 canvas 尺寸 (width×height) 一致。
仅限 8bit RGB 文档。

---

### setLayerText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `text` | `&nbsp;` | 新的正文 (换行是 \\r) |

**说明**

替换文本图层的正文 (样式会折叠到首个 run)。

不是文本图层或没有 TySh 块时会抛出异常。

---

### setLayerRunStyle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `runIndex` | `&nbsp;` | run 编号 |
| `style` | `&nbsp;` | 样式字典 |

**说明**

编辑文本图层的第 runIndex 个 run (对应 getLayerInfo().text.runs) 的

样式。只覆盖 style 字典中指定的键。
%[ font:      // 字体名。如果文档的字体集中没有则会被添加
// (getLayerFonts() 返回的 PostScript 风格的名字。请注意
//  不是显示名称。本地没有的名字会由 Photoshop 侧替代)
size_px:   // 字体大小 (px)
color:     // RGBA 各 0..1 的数组 `[ r, g, b, a ]` (省略 a 写成 `[ r, g, b ]` 也可)
tracking:  // 字距调整 (1/1000 em)
kerning:   // 手动字距调整
bold:      // 仿粗体 (FauxBold) true/false
italic:    // 仿斜体 (FauxItalic) true/false
underline: // 下划线 (Underline) true/false
]
正文与 run 的长度不变。对于通过继承没有该键的 run 会被添加。
不是文本图层或 runIndex 超出范围时会抛出异常。

---

### setLayerRichText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `text` | `&nbsp;` | 新的正文 (换行是 \\r) |
| `runs` | `void` | [ %[ length: // 适用字符数<br>…与 setLayerRunStyle 的 style 相同的键<br>],... ]   可省略 |
| `paragraphs` | `void` | [ %[ length:        // 段落的字符数<br>justification: // 对齐 0=左 1=右 2=居中<br>],... ]   可省略 |

**说明**

替换文本图层的正文与 run 构成/段落构成。

setLayerText 会把样式折叠到首个 run，因此想要在更改正文的同时
按部分更改格式时请使用这个。

runs / paragraphs 的 length 是 UTF-16 代码单元数 (emoji 等代理
对为 2)。length 的合计与正文长度不一致时，末尾元素会吸收多余/不足
(拉伸/截断)。长度为 0 的元素会被丢弃。传入 void 或空数组时
会折叠为单个 run/单个段落。末尾没有换行 (\r) 时会补上。
各 run 的样式是“以原来的首个 run 为模板，只覆盖指定的键”，因此
未指定的格式保持原来的外观。

不是文本图层时会抛出异常。

---

### setLayerJustification

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `justification` | `&nbsp;` | 对齐 0=左 1=右 2=居中 |
| `paraIndex` | `-1` | 目标段落编号 (对应 getLayerInfo().text.paragraphs)。<br>负值表示所有段落。默认 -1 |

**说明**

只更改文本图层段落的对齐 (正文与 run 构成都不变)。

不是文本图层或 paraIndex 超出范围时会抛出异常。

---

### getLayerFonts

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |

**返回值**

字体名的数组

**说明**

返回文本图层持有的字体名列表 (供字体选择 UI 的候选使用)。

可以传给 setLayerRunStyle / setLayerRichText 的 font 的名字。
不是文本图层时会抛出异常。

---

### getLayerTextTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |

**返回值**

`[ xx, xy, yx, yy, tx, ty ]` (tx,ty=平移)

**说明**

获取文本图层的配置 (仿射变换)。

与 getLayerInfo().text.transform 的值相同。不是文本图层时会抛出异常。

---

### setLayerTextTransform

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `matrix` | `&nbsp;` | [ xx, xy, yx, yy, tx, ty ] 的 6 个元素的数组 |

**说明**

替换文本图层的配置 (仿射变换)。

被改写的只有文本信息，图层矩形 (已栅格化的位图)
不会移动。单纯的平移请使用 moveTextLayer。
不是文本图层或元素数量不足时会抛出异常。

---

### moveTextLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `dx` | `&nbsp;` | X 平移量 (px) |
| `dy` | `&nbsp;` | Y 平移量 (px) |

**说明**

平移文本图层。仿射变换的 tx/ty 与图层矩形

(如果有遮罩矩形则也包括它) 会平移相同的量，因此 PSD 内置的位图也
一起移动。不是文本图层时会抛出异常。

---

### getLayerTextBounds

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |

**返回值**

%[ left:, top:, right:, bottom: ]

**说明**

获取文本图层的文本框 (仿射变换的局部坐标。

文档上的位置为加上 transform 的 tx/ty 后的值)。
不是文本图层时会抛出异常。

---

### setLayerTextBounds

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 图层编号 |
| `left` | `&nbsp;` | 左 |
| `top` | `&nbsp;` | 上 |
| `right` | `&nbsp;` | 右 |
| `bottom` | `&nbsp;` | 下 |

**说明**

替换文本图层的文本框 (仿射变换的局部坐标)。

实际文本框内排版会发生变化的只有段落文本 (box text)，
对于点文本，Photoshop 侧会根据字形重新生成文本框。
不是文本图层时会抛出异常。

---

### clearStorageCache

方法

**说明**

static method

清除作为存储保持的缓存

---
