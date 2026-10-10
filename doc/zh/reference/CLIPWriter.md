# CLIPWriter

CLIP 文件的编辑 / 写出类。

与读取侧 (CLIP) 是不同的类。由于会把编辑源全部读入内存 (不使用 mmap)，
因此可以写回同一路径。

**写出的文件请先通过 validate() 再在 CSP 中打开。**
“这边的读取器能读，但 CSP 不接受”这类错误 (存储类型、
mipmap 级数、校验和、缩略图的世代编号、CanvasPreview) 由
clipparse 侧负责处理，但引用完整性的破坏只能通过 validate()
检测到。处于这种状态的文件在 CSP 中会崩溃或整体变为透明。

使用示例:
var w = new CLIPWriter();
w.load("in.clip");
w.setLayerAttr(5, %[ opacity: 128, composite: CLIPWriter.composite_multiply ]);
w.save("out.clip");
var problems = CLIPWriter.validate("out.clip");
if (problems.count) Debug.message(problems.join("\n"));

## 成员列表

### 属性

- [error](#error)
- [external_count](#external_count)

### 方法

- [load](#load)
- [save](#save)
- [clearData](#cleardata)
- [setLayerAttr](#setlayerattr)
- [setPixels](#setpixels)
- [addLayer](#addlayer)
- [deleteLayer](#deletelayer)
- [dropThumbnail](#dropthumbnail)
- [setCanvasPreview](#setcanvaspreview)
- [resizeCanvas](#resizecanvas)
- [setSeed](#setseed)
- [validate](#validate)

---

### error

属性 \ 访问: `r`

**说明**

最近一次失败的原因。没有则为空字符串。

**成功时不会被清除，因此只应在返回值为 false 时读取。**

---

### external_count

属性 \ 访问: `r`

**说明**

外部块 (CHNKExta) 的数量

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 文件名 (必须能落到本地路径。<br>归档内的文件不能作为编辑源，会抛出异常) |

**返回值**

成功时为 true (失败原因见 error 属性)

**说明**

读取编辑源的 CLIP 文件

---

### save

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 保存目标的文件名 (本地路径) |

**返回值**

写出的字节数。失败时为 0

**说明**

以当前状态组装文件并写出。

未更改地写回时，与原始文件的 sha256 一致。

---

### clearData

方法

**说明**

显式丢弃所持有的数据

---

### setLayerAttr

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId (CLIP.getLayerInfo().layer_id 的值) |
| `attr` | `&nbsp;` | 属性字典 |

**返回值**

成功时为 true

**说明**

编辑图层属性。只更改 attr 字典中被指定的键

%[ name:       // 图层名
opacity:    // 不透明度 0..**256** (CLIP 为 256 级。不是 0..255)
visibility: // 显示状态 0/1
composite:  // 合成模式 (composite_* 常量)
clipping:   // 是否由下层图层裁剪
folder:     // 文件夹属性 (bit0=文件夹 / bit4=折叠)
]

---

### setPixels

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId |
| `layer` | `&nbsp;` | 像素提供源的 Layer |

**返回值**

成功时为 true

**说明**

用 Layer 对象的内容替换图层的像素。

**Layer 的大小必须与该图层 100% mipmap 的尺寸一致。
这并不一定是画布大小** — CSP 会根据图层，
以向上取整到 256x256 块边界的大小 (300x400 的画布也可能是 512x512 等)
持有像素。所需尺寸可以通过读取侧的
`CLIP.getLayerAttribute(图层编号)` 的 width / height 查询:

var a = clip.getLayerAttribute(3);
lay.setImageSize(a.width, a.height);
lay.setSizeToImageSize();
// ... 在 lay 上绘制 ...
w.setPixels(clip.getLayerInfo(3).layer_id, lay);

尺寸不匹配时返回 false，error 中会填入
"pixel size does not match the 100% mipmap"。
仅支持 RGBA 平面的图层 (getLayerAttribute().num_channels == 4)。

---

### addLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 新的图层名 |
| `copyFrom` | `&nbsp;` | 作为模板的既有图层的 LayerId |
| `layer` | `void` | 像素提供源的 Layer (省略/void 则整体透明) |
| `after` | `-1` | 插入到该 LayerId 的正上方。负值为最上层。默认 -1 |
| `parent` | `0` | 父文件夹的 LayerId。0 表示根直下。默认 0 |

**返回值**

新图层的 LayerId。失败时为 0

**说明**

以既有图层为模板添加图层。

因为会从模板继承表现色等属性，所以必须选择添加来源的图层。

---

### deleteLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId |

**返回值**

成功时为 true

**说明**

删除图层

---

### dropThumbnail

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layerId` | `&nbsp;` | LayerId |

**返回值**

成功时为 true

**说明**

只丢弃缩略图的实体并更新世代编号 (CSP 打开时会重新生成)。

用于想要避免替换了像素却残留旧缩略图的情况，但
setPixels / addLayer 会在内部处理，因此通常不需要调用。

---

### setCanvasPreview

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 像素提供源的 Layer |

**返回值**

成功时为 true

**说明**

替换打开后立即显示的图像 (CanvasPreview)

---

### resizeCanvas

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 新的宽度 |
| `height` | `&nbsp;` | 新的高度 |
| `dpi` | `0` | 分辨率 (0 则保持不变)。默认 0 |

**返回值**

成功时为 true

**说明**

连同画布尺寸一起重建 (伸缩 mipmap 链)。

**像素的实体会全部丢失，因此调用后请用 setPixels 重新写入。**

---

### setSeed

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `seed` | `&nbsp;` | 随机数种子 |

**说明**

固定外部 ID 的随机数种子 (测试需要输出可复现性时)

---

### validate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 要检查的文件 (本地路径) |

**返回值**

问题的字符串数组。空数组则没有问题

**说明**

静态方法

检查引用完整性。**在 CSP 中打开之前务必先通过此检查。**
检查 mipmap 级数 / 环路 / 孤立行 / 存储类型 / 对已消失图层的引用。

---
