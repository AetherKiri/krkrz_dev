# GdiPlus.Appearance

该类由多个插件扩展。

## 插件扩展: layerExDraw

绘制外观信息

请想象 Illustrator 的外观。
针对绘制，可以指定多个画笔（填充）和钢笔（线条）。
先添加的会位于下层

### 成员列表

#### 构造函数

- [Appearance](#appearance)

#### 方法

- [clear](#clear)
- [addBrush](#addbrush)
- [addPen](#addpen)

---

### Appearance

构造函数

**说明**

构造函数

---

### clear

方法

**说明**

信息的清除

---

### addBrush

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB 颜色指定或画笔信息（字典） |
| `ox` | `&nbsp;` | 显示偏移 X |
| `oy` | `&nbsp;` | 显示偏移 Y |

**说明**

画笔的添加

画笔信息定义
基本  点指定为 [x,y] 数组或 %[x:x, y:y] 字典
矩形指定为 [x,y,width,height] 数组或 %[x:x, y:y, width:w, height:h] 字典
颜色指定为 ARGB 32bit 整数值
关于参数，请参阅 GDI+ 的文档并进行研究

type: 用画笔种类 BrushType 指定

BrushTypeSolidColor 时 ※与直接指定 ARGB 颜色时相同
color: 颜色指定 (未指定时为白)

BrushTypeHatchFill 时
hatchStyle: 阴影样式的种类 (未指定时为 HatchStyleHorizontal)
foreColor: 前景色 (未指定时为白)
backColor: 背景色 (未指定时为黑)

BrushTypeTextureFill 时
image: 图像指定
wrapMode: 重复图案指定 (未指定时为 WrapModeTile)
dstRect: 纹理区域矩形指定 (未指定时为整幅图像)

BrushTypePathGradient 时
points: 点指定的数组
centerColor: 中心色
centerPoint: 中心点
focusScale: focus scales 指定 [xScale,yScale] 或 %[xScale:, yScale:]
surroundColors: 周围色指定。颜色的数组
---- 以下与 BrushTypeLinearGradient 也共通
blend: 混合因子指定。用数值数组 [blendFactors, blendPositions] 或字典
blendBellShape: 混合形状指定 (bell 形状) [focus, scale]
blendTriangularShape: 混合形状指定 (三角形状) [focus, scale]
gammaCorrection: 是否启用伽马校正 true/false
interpolationColors: [presetColors(颜色数组), blendPositions(数值数组)]

BrushTypeLinearGradient 时
共通
color1: 开始色指定
color2: 结束色指定
wrapMode: 重复图案指定 (未指定时为 WrapModeTile)
点指定
point1: 开始点
point2: 结束点
※角度似乎会自动决定
矩形指定
rect: 点指定。左上为开始，右下为结束
angle: 角度指定 (仅在 rect 指定时有效)
isAngleScalable (角度指定是否可缩放)
mode: 模式指定 (省略时为 LinearGradientModeHorizontal) 在没有 angle 指定时有效

---

### addPen

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB 颜色指定或画笔信息（字典） |
| `widthOrOption` | `&nbsp;` | 钢笔宽度或钢笔信息（字典） |
| `ox` | `&nbsp;` | 显示偏移 X |
| `oy` | `&nbsp;` | 显示偏移 Y |

**说明**

钢笔的添加

钢笔信息定义: widthOrOption 为字典时为详细信息定义
关于参数，请参阅 GDI+ 的文档并进行研究

width: 钢笔宽度指定
alignment: 对齐方式：省略时为 PenAlignmentCenter
compoundArray: compound array 指定。数值数组
dashCap: 虚线的 cap style 指定。省略时为 DashCapFlat
dashOffset: 虚线的偏移指定。省略时为 0
dashStyle: 虚线样式。设为数组时为用户定义（数值数组）。默认为 DasyStyleSolid
startCap: 起始位置的 cap style 指定。省略时为 LineCapFlat，字典时为 AdjustableArrowCap
endCap: 结束位置的 cap style 指定。省略时为 LineCapFlat，字典时为 AdjustableArrowCap
lineJoin: 连接形状指定。 省略时为 LineJoinMiter
miterLimit: miter limit 指定（数值）

AdjustableArrowCap：献给不满足于 LineCapArrowAnchor 的你
可以指定 width(箭头宽度), height(箭头高度), filled(true 则为三角形，false 则为三叉形)

---

## 插件扩展: layerExVector

绘制外观信息

请想象 Illustrator 的外观。
针对绘制，可以指定多个画笔（填充）和钢笔（线条）。
先添加的会位于下层

### 成员列表

#### 构造函数

- [Appearance](#appearance)

#### 方法

- [clear](#clear)
- [addBrush](#addbrush)
- [addPen](#addpen)

---

### Appearance

构造函数

**说明**

构造函数

---

### clear

方法

**说明**

信息的清除

---

### addBrush

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB 颜色指定或画笔信息（字典） |
| `ox` | `0` | 显示偏移 X |
| `oy` | `0` | 显示偏移 Y |

**说明**

画笔的添加

画笔信息定义
基本  点指定为 [x,y] 数组或 %[x:x, y:y] 字典
颜色指定为 ARGB 32bit 整数值

type: 用画笔种类 BrushType 指定

BrushTypeSolidColor 时 ※与直接指定 ARGB 颜色时相同
color: 颜色指定 (未指定时为白)

BrushTypePathGradient 时 (作为 RadialGradient 近似实现)
centerPoint: 中心点
centerColor: 中心色
radius: 半径 (未指定时为 100)

BrushTypeLinearGradient 时
point1: 开始点
point2: 结束点
color1: 开始色指定
color2: 结束色指定

---

### addPen

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `colorOrBrush` | `&nbsp;` | ARGB 颜色指定或画笔信息（字典） |
| `widthOrOption` | `1.0` | 钢笔宽度或钢笔信息（字典） |
| `ox` | `0` | 显示偏移 X |
| `oy` | `0` | 显示偏移 Y |

**说明**

钢笔的添加

钢笔信息定义: widthOrOption 为字典时为详细信息定义

width: 钢笔宽度指定
startCap / endCap: cap style 指定。用 LineCap 常量指定。省略时为 LineCapFlat
lineJoin: 连接形状指定。用 LineJoin 常量指定。省略时为 LineJoinBevel
miterLimit: miter limit 指定（数值）
dashStyle: 虚线图案。以数值数组指定
dashOffset: 虚线的偏移指定。省略时为 0

---
