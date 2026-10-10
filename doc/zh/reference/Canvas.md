# Canvas

Canvas 是提供绘制功能的类。
生成 Window 后，属性 canvas 会被自动创建。
使用时，请使用该 Window 的 canvas 属性。

## 成员列表

### 属性

- [clearColor](#clearcolor)
- [renderTarget](#rendertarget)
- [blendMode](#blendmode)
- [matrix](#matrix)
- [defaultShader](#defaultshader)
- [defaultFillShader](#defaultfillshader)
- [width](#width)
- [height](#height)
- [clipRect](#cliprect)
- [enableClipRect](#enablecliprect)
- [enableCulling](#enableculling)

### 方法

- [clear](#clear)
- [capture](#capture)
- [save](#save)
- [restore](#restore)
- [fill](#fill)
- [drawMesh](#drawmesh)
- [drawMesh](#drawmesh)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTexture](#drawtexture)
- [drawTransition](#drawtransition)
- [drawTransition](#drawtransition)
- [drawTextureAtlas](#drawtextureatlas)
- [drawTextureAtlas](#drawtextureatlas)
- [draw9Patch](#draw9patch)
- [beginEffect](#begineffect)
- [endEffect](#endeffect)
- [beginMaskClip](#beginmaskclip)
- [endMaskClip](#endmaskclip)
- [beginStencilClip](#beginstencilclip)
- [endStencilClip](#endstencilclip)
- [flush](#flush)
- [drawText](#drawtext)

---

### clearColor

属性 \ 访问: `r/w`

**说明**

清除色指定、绘制处理前的画面清除色

---

### renderTarget

属性 \ 访问: `r/w`

**说明**

绘制目标指定

可以指定 Offscreen 类。
指定 null/void 时改为直接绘制。

---

### blendMode

属性 \ 访问: `r/w`

**说明**

绘制的合成模式指定

可以指定 bmDisable、bmOpaque、bmAlpha、bmAdd、bmAddWithAlpha。
如果需要这里没有的混合方法，请编写着色器。

---

### matrix

属性 \ 访问: `r/w`

**说明**

绘制矩阵指定

(Matrix32 类)

---

### defaultShader

属性 \ 访问: `r/w`

**说明**

用于纹理绘制的默认着色器 (只向 drawTexture 传入 1 张纹理时使用的着色器)

也可以设置，但基本上不需要更改。
放入 void 后会恢复为内置的初始默认着色器。

默认着色器的 a_opacity uniform 会在 Canvas 生成时被设置为 1.0。
只有希望以半透明方式绘制时，才更改 `canvas.defaultShader.a_opacity`。
在自定义着色器中声明了 a_opacity 时，需要由调用方设置
(请注意未设置的 uniform 为 GL 初始值 0 = 完全透明)。

---

### defaultFillShader

属性 \ 访问: `r/w`

**说明**

fill 时使用的默认着色器

也可以设置，但基本上不需要更改
放入 void 后会恢复为内置的初始默认着色器。

---

### width

属性 \ 访问: `r/w`

**说明**

绘制区域的宽度

基本上与客户端区域一致，从 Window 调整大小到重绘之间会有暂时不一致的期间 (1 帧)。

---

### height

属性 \ 访问: `r/w`

**说明**

绘制区域的高度

基本上与客户端区域一致，从 Window 调整大小到重绘之间会有暂时不一致的期间 (1 帧)。

---

### clipRect

属性 \ 访问: `r/w`

**说明**

用于裁剪的矩形 Rect 类

可以通过 canvas.clipRect.set( l, t, r, b ); 等调用。
可以通过 enableClipRect 设置启用/禁用

---

### enableClipRect

属性 \ 访问: `r/w`

**说明**

是否使用矩形进行裁剪的设置

为 true 时，会依据 clipRect 属性进行裁剪

---

### enableCulling

属性 \ 访问: `r/w`

**说明**

是否进行正面/背面剔除的设置

为 true 时进行，为 false 时不进行，默认为 false。

---

### clear

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `argb` | `int` | `&nbsp;` | 清除色 (未指定时使用 clearColor 属性清除) |

**说明**

清除整个绘制区域

---

### capture

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dest` | `&nbsp;` | `&nbsp;` | 捕获目标 Bitmap/Texture/Offscreen |
| `front` | `bool` | `true` | 指定是从 front buffer 捕获还是从 back buffer 捕获。true 为 front，false 为 back |

**说明**

将当前的绘制内容整体捕获到 Bitmap/Texture/Offscreen

位图的尺寸会被校正为屏幕尺寸
为 Texture/Offscreen 时不会被更改

---

### save

方法

**说明**

保存 matrix 与 clip 的状态 (栈)

---

### restore

方法

**说明**

恢复 matrix 与 clip 的状态 (栈)

---

### fill

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 填充范围宽度 |
| `height` | `int` | `&nbsp;` | 填充范围高度 |
| `colors` | `&nbsp;` | `0xffffffff` | 4 个顶点的顶点颜色 ARGB。单个数值时为单色，数组时为 4 个顶点分别指定 |
| `shader` | `&nbsp;` | `null` | 填充着色器。为 null 时使用 defaultFillShader 填充 |

**说明**

使用颜色填充

XY 坐标通过 matrix 指定。

---

### drawMesh

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `shader` | `ShaderProgram` | `&nbsp;` | 指定已关联纹理与顶点信息的着色器 |
| `count` | `int` | `&nbsp;` | 要绘制的顶点数 |
| `primitiveType` | `int` | `VertexBuffer.ptTriangles` | 指定三角形等图元 |
| `offset` | `int` | `0` | 顶点数组中开始绘制的偏移量 |

**说明**

网格绘制

网格 (VertexBinder：顶点信息) 必须在调用前关联到 shader (通过属性设置)。
纹理信息也同样需要事先关联。
调用后请解除 (=void) 关联到 shader 的信息。

---

### drawMesh

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `shader` | `ShaderProgram` | `&nbsp;` | 指定已关联纹理与顶点信息的着色器 |
| `index` | `VertexBinder` | `&nbsp;` | 指定索引缓冲区 |
| `count` | `int` | `&nbsp;` | 要绘制的索引数 |
| `primitiveType` | `int` | `VertexBuffer.ptTriangles` | 指定三角形等图元 |

**说明**

使用索引缓冲区的网格绘制版本

网格 (VertexBinder：顶点信息) 必须在调用前关联到 shader (通过属性设置)。
纹理信息也同样需要事先关联。
调用后请解除 (=void) 关联到 shader 的信息。

---

### drawTexture

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 指定绘制使用的纹理 |

**说明**

绘制 1 张纹理

使用 defaultShader 绘制。
位置、缩放、旋转通过 matrix 指定。
纹理不仅可以指定 Texture 类，指定 Offscreen 类也没有问题。
指定 Offscreen 类时，前提是该 Offscreen 类已从 renderTarget 中移除 (以免循环)。

---

### drawTexture

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 指定绘制使用的纹理 |
| `shader` | `ShaderProgram` | `&nbsp;` | 指定绘制使用的着色器 |

**说明**

指定着色器绘制 1 张纹理

位置、缩放、旋转通过 matrix 指定。
纹理不仅可以指定 Texture 类，指定 Offscreen 类也没有问题。
指定 Offscreen 类时，前提是该 Offscreen 类已从 renderTarget 中移除 (以免循环)。

---

### drawTexture

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 指定绘制使用的纹理 |
| `texture2` | `Texture` | `&nbsp;` | 指定绘制使用的第 2 张纹理 |
| `shader` | `ShaderProgram` | `&nbsp;` | 指定绘制使用的着色器 |

**说明**

指定着色器绘制 2 张纹理

位置、缩放、旋转通过 matrix 指定。
纹理不仅可以指定 Texture 类，指定 Offscreen 类也没有问题。
指定 Offscreen 类时，前提是该 Offscreen 类已从 renderTarget 中移除 (以免循环)。

---

### drawTexture

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `texture` | `Texture` | `&nbsp;` | 指定绘制使用的纹理 |
| `texture2` | `Texture` | `&nbsp;` | 指定绘制使用的第 2 张纹理 |
| `texture3` | `Texture` | `&nbsp;` | 指定绘制使用的第 3 张纹理 |
| `shader` | `ShaderProgram` | `&nbsp;` | 指定绘制使用的着色器 |

**说明**

指定着色器绘制 3 张纹理

位置、缩放、旋转通过 matrix 指定。
纹理不仅可以指定 Texture 类，指定 Offscreen 类也没有问题。
指定 Offscreen 类时，前提是该 Offscreen 类已从 renderTarget 中移除 (以免循环)。
OpenGL ES 2.0 的情况下纹理最多 8 张，3.0 时顶点侧最多 16 张、片元侧最多 16 张，所以还可以继续添加，但暂且只定义到 3 张。
将来会考虑制作以数组传递纹理的版本，4 张以上的情况由该版本支持。

---

### drawTransition

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `front` | `Texture` | `&nbsp;` | 正面 (phase=0.0 时显示) 纹理 |
| `back` | `Texture` | `&nbsp;` | 背面 (phase=1.0 时显示) 纹理 |
| `phase` | `real` | `&nbsp;` | 进度 0.0~1.0 (超出范围会被钳制) |

**说明**

交叉淡化绘制正面/背面 2 张纹理

将 front → back 按进度 phase 混色后绘制。
着色器已内置，因此不需要准备 ShaderProgram。
位置、缩放、旋转通过 matrix 指定 (与 drawTexture 相同规约，
也遵循 blendMode / 裁剪)。
纹理不仅可以指定 Texture 类，也可以指定 Offscreen 类。

---

### drawTransition

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `front` | `Texture` | `&nbsp;` | 正面纹理 |
| `back` | `Texture` | `&nbsp;` | 背面纹理 |
| `phase` | `real` | `&nbsp;` | 进度 0.0~1.0 |
| `rule` | `Texture` | `&nbsp;` | rule 图像纹理 (tcfAlpha)。为 null 时交叉淡化 |
| `vague` | `int` | `64` | 边界模糊宽度 (rule 值尺度 0~255) |

**说明**

通用转场绘制正面/背面 2 张纹理

rule 图像 (灰度) 的值越小的像素越早切换到 back 侧。
切换的阈值会扫描 phase * (1 + vague/255)，
因此在 phase=1.0 时所有像素必定为 back。边界会按 vague 的宽度进行模糊。

请以 tcfAlpha 格式创建 rule 纹理
(例：`new Texture("rule.png", tcfAlpha)`)。向 rule 传入 null 时
会作为交叉淡化运行。

与 Elements 对话框的流程画面切换特效 (JSON `transitions` 的
`effect` / `rule` / `vague`) 具有相同语义，可以使用相同的 rule 素材。

---

### drawTextureAtlas

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `rect` | `Rect` | `&nbsp;` | 纹理内要绘制的矩形区域 |
| `texture` | `Texture` | `&nbsp;` | 要绘制的纹理 |

**说明**

绘制纹理的一部分

使用 defaultShader 绘制。

---

### drawTextureAtlas

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `rect` | `Rect` | `&nbsp;` | 纹理内要绘制的矩形区域 |
| `texture` | `Texture` | `&nbsp;` | 要绘制的纹理 |
| `shader` | `ShaderProgram` | `&nbsp;` | 绘制使用的着色器 |

**说明**

绘制纹理的一部分 (指定着色器)

---

### draw9Patch

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `txture` | `Texture` | `&nbsp;` |  |
| `width` | `int` | `&nbsp;` | 要绘制的宽度 |
| `height` | `int` | `&nbsp;` | 要绘制的高度 |
| `shader` | `ShaderProgram` | `null` | 绘制使用的着色器。可省略。 |

**返回值**

返回边距信息。

**说明**

使用 9patch 绘制

用于绘制的 Texture 需要已读取 9patch 信息。
只能指定 Texture 类。

---

### beginEffect

方法

**说明**

开始捕获后处理效果

从这里到 [endEffect](#endeffect) 为止的绘制会被捕获到中间缓冲区
(已清除为透明)。可以嵌套。忘记关闭时会在帧终点被丢弃，
并输出警告日志。
命令规格与内部结构的详细信息请参阅
[3D 图形系统](../guide/Graphic3DSystem.md)。

**相关:** [Canvas.endEffect](Canvas.md#endeffect)

---

### endEffect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `commands` | `null` | 加工命令 (Dictionary) 的数组。省略时为直通合成。 |

**说明**

对捕获的绘制应用加工命令列并合成

对从 [beginEffect](#begineffect) 开始的绘制依次应用 commands，
并以当前的 blendMode 合成到之前的绘制目标上。加工无需
回读 CPU，在 GPU 内闭环完成。

命令通过 `%[ cmd:"名前", ... ]` 形式的 Dictionary 数组指定：
LUT 系 (gamma / adjustGamma / light / lut)、
混合系 (grayscale / colorize / modulate / noise / generateWhiteNoise /
overcolor)、邻域系 (boxBlur / gaussianBlur)。
各命令的参数与融合规则请参阅
[3D 图形系统](../guide/Graphic3DSystem.md)。

**相关:** [Canvas.beginEffect](Canvas.md#begineffect)

---

### beginMaskClip

方法

**说明**

开始捕获遮罩裁剪

从这里到 [endMaskClip](#endmaskclip) 为止的绘制会被捕获。
这是对任何绘制都能安全使用的图像裁剪方式。

**相关:** [Canvas.endMaskClip](Canvas.md#endmaskclip)

---

### endMaskClip

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `mask` | `&nbsp;` | `&nbsp;` | 用作遮罩的 Texture / Offscreen。为 void 时直通合成。 |
| `x` | `int` | `&nbsp;` | 放置遮罩的 X 位置 |
| `y` | `int` | `&nbsp;` | 放置遮罩的 Y 位置 |

**说明**

对捕获的绘制乘以遮罩的 α 并合成

乘以 mask 的 α 后合成到之前的绘制目标上。遮罩矩形的
外侧为 α=0 (完全裁剪)。相当于 CPU 版 Layer.clipAlphaRect。

**相关:** [Canvas.beginMaskClip](Canvas.md#beginmaskclip)

---

### beginStencilClip

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `mask` | `&nbsp;` | `&nbsp;` | 用作遮罩的 Texture / Offscreen |
| `x` | `int` | `&nbsp;` | 放置遮罩的 X 位置 |
| `y` | `int` | `&nbsp;` | 放置遮罩的 Y 位置 |
| `threshold` | `int` | `1` | α 阈值 (1~255) |

**说明**

开始模板裁剪

将遮罩的 α 写入模板缓冲，
对到 [endStencilClip](#endstencilclip) 为止的绘制进行裁剪。面向单纯纹理
绘制的轻量方式 (会与自行使用模板的绘制冲突，这种情况下
请使用遮罩裁剪)。

**相关:** [Canvas.endStencilClip](Canvas.md#endstencilclip)

---

### endStencilClip

方法

**说明**

结束模板裁剪

**相关:** [Canvas.beginStencilClip](Canvas.md#beginstencilclip)

---

### flush

方法

**说明**

刷新绘制

在需要切换 renderTarget 使绘制生效等情况下使用。
在 onDraw 中切换 renderTarget 时，内部会调用 flush，因此不需要显式调用。

---

### drawText

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `font` | `Font` | `&nbsp;` | 字体 |
| `x` | `int` | `&nbsp;` | X 位置 |
| `y` | `int` | `&nbsp;` | Y 位置 |
| `text` | `string` | `&nbsp;` | 文本 |
| `color` | `int` | `&nbsp;` | 颜色指定 |

**说明**

文本绘制 (未实现)

---
