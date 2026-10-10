# GLESAdaptor

可以保持 OpenGL ES 绘制上下文的适配器 (基于 EGL)

用于绘制的对象以使用 egl 进行上下文处理为前提

## 成员列表

### 构造函数

- [GLESAdaptor](#glesadaptor)

### 属性

- [screenWidth](#screenwidth)
- [screenHeihgt](#screenheihgt)
- [blendMode](#blendmode)

### 方法

- [setScreenSize](#setscreensize)
- [makeCurrent](#makecurrent)
- [capture](#capture)
- [copyLayer](#copylayer)
- [drawLayer](#drawlayer)
- [beginEffect](#begineffect)
- [endEffect](#endeffect)
- [setClipRect](#setcliprect)
- [clearClipRect](#clearcliprect)
- [beginMaskClip](#beginmaskclip)
- [endMaskClip](#endmaskclip)
- [beginStencilClip](#beginstencilclip)
- [endStencilClip](#endstencilclip)

---

### GLESAdaptor

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 目标窗口 |

**说明**

构造函数

---

### screenWidth

属性 \ 访问: `r/w`

**说明**

屏幕宽度

---

### screenHeihgt

属性 \ 访问: `r/w`

**说明**

屏幕高度

---

### blendMode

属性 \ 访问: `r/w`

**说明**

混合模式 (相当于 tTVPBlendMode: 0=Disable,1=Opaque,2=Alpha,3=Add,...)

---

### setScreenSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

设置屏幕大小

---

### makeCurrent

方法

**说明**

设置 OpenGL 上下文

---

### capture

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 结果存放目标图层 |
| `callback` | `&nbsp;` | 处理函数  function(width, height, param)  在该对象的上下文中执行 |
| `param` | `&nbsp;` | 附加参数 |
| `color` | `&nbsp;` | 填充色 |

**说明**

执行 OpenGL 绘制处理

---

### copyLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 图层 或 GLESTexture |
| `left` | `&nbsp;` | 左侧位置 |
| `top` | `&nbsp;` | 顶部位置 |

**说明**

图层的复制

---

### drawLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 图层 或 GLESTexture |
| `a` | `&nbsp;` |  |
| `b` | `&nbsp;` |  |
| `c` | `&nbsp;` |  |
| `d` | `&nbsp;` |  |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |
| `opacity` | `&nbsp;` | 不透明度 0~255 (省略时 255) |

**说明**

图层的绘制

---

### beginEffect

方法

**说明**

开始捕获效果

之后的绘制会在中间帧缓冲 (已清除为透明) 中进行。
必须调用对应的 endEffect()。

===================================================================== 后处理效果 (绘制后处理) 用 beginEffect() ~ endEffect() 包围的绘制会被捕获到中间缓冲区， 在 GPU 上应用图像加工命令列后，合成到之前的绘制目标。 可在 capture() 的回调内，针对每个模块 (Live2D / drawLayer 等) 的绘制单独施加效果。可嵌套。 =====================================================================

---

### endEffect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `commands` | `&nbsp;` | 加工命令的数组。各元素为字典，cmd 成员表示种类，<br>其余成员为参数。请参照下面的“命令一览”。 |
| `opacity` | `255` | 合成时的不透明度 (0~255，省略时 255)。会乘到 α 上。<br>用于反映像 Live2D 那样在自身绘制中不解释 opacity 的<br>模块的图层不透明度。<br>如果不需要加工，向 commands 传入空数组，<br>就会变为“仅捕获并以 opacity 合成”。<br>例) [ %[ cmd:"grayscale" ], %[ cmd:"gamma", value:1.2 ] ] |

**说明**

效果应用与合成

对之前的 beginEffect() 之后绘制的内容依次应用 commands，
并以当前的 blendMode 合成到之前的绘制目标。

---

### setClipRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

设置矩形裁剪

之后的 drawLayer / endEffect / endMaskClip 的合成会被限制在矩形内。
如果绘制模块尊重 scissor 状态，对直接绘制也有效，
但若想可靠地裁剪，请用 beginMaskClip/endMaskClip 包围。
--------------------------------------------------------------------- 命令一览 (排列在 endEffect 的 commands 数组中) ● 点处理 (连续时会融合为 1 个 pass) %[ cmd:"grayscale" ] 灰度化  Y=(19*B+183*G+54*R)>>8 %[ cmd:"gamma", value:r ]                     // 全通道统一 %[ cmd:"gamma", rgamma:.., rfloor:.., rceil:.., ggamma:.., gfloor:.., gceil:.., bgamma:.., bfloor:.., bceil:.. ] // 按通道 伽马校正  out = pow(in/255, 1/gamma)*(ceil-floor)+floor (与本体 Layer.adjustGamma 相同。floor 默认 0 / ceil 默认 255) %[ cmd:"light", brightness:b, contrast:c ] 明度 b(-255~255) / 对比度 c(-100~100) %[ cmd:"lut", table:[ ...256个元素... ] ] 全通道共用的 256 级查找表 %[ cmd:"colorize", hue:h, sat:s, blend:b ] 色相 h(0~255) / 饱和度 s(0~255) / 合成率 b(0~1) %[ cmd:"modulate", hue:h, saturation:s, luminance:l ] 色相 h(-180~180) / 饱和度 s(-100~100) / 亮度 l(-100~100) %[ cmd:"noise", level:n ] 添加噪声 n(0~255) %[ cmd:"generateWhiteNoise" ] 生成灰度的白噪声 (α 保持) %[ cmd:"overcolor", color:0xAARRGGBB, type:mode, opacity:o ] 以指定色进行整体填充合成 (遵循吉里吉里 fillOperateRect)。 合成 α 由 color 的高 8bit(AA) 与 opacity(0~255,默认 255) 得到。 type 为吉里吉里的合成模式值 (tTVPBlendOperationMode): 1=Opaque 2=Alpha(默认) 3=Additive 4=Subtractive 5=Multiplicative 8=Dodge 9=Darken 10=Lighten 11=Screen 12=AddAlpha 13=PsNormal 14=PsAdditive 15=PsSubtractive 16=PsMultiplicative 17=PsScreen 18=PsOverlay 19=PsHardLight 20=PsSoftLight 21=PsColorDodge 22=PsColorDodge5 23=PsColorBurn 24=PsLighten 25=PsDarken 26=PsDifference 27=PsDifference5 28=PsExclusion ● 邻域处理 (经由中间缓冲区进行 H/V 2 pass) %[ cmd:"boxBlur", area:r, iter:n ] 半径 r 的均匀模糊 n 次 (iter 默认 1) %[ cmd:"gaussianBlur", radius:r ] 半径 r 的高斯模糊 ※ noise / blur 的最外周 / colorize 并非与 CPU 版完全一致，而是视觉上等效。 --------------------------------------------------------------------- ===================================================================== 裁剪 (相当于 AffineLayer 的 clip / clipImage) 矩形裁剪   : setClipRect / clearClipRect。用 scissor 实现。 图像裁剪   : 两种方式 mask 方式    : 用 beginMaskClip() ~ endMaskClip() 包围的绘制 会被捕获到中间缓冲区，一边乘算遮罩图像的 α 一边 合成到之前的绘制目标。遮罩矩形外侧为 α=0。 (相当于 CPU 版 Layer.clipAlphaRect 的第 8 个参数 0) 对绘制模块 (Live2D 等) 也可安全使用。 stencil 方式 : beginStencilClip() ~ endStencilClip()。 将遮罩 α 写入模板并裁剪绘制。 α 会按阈值二值化。绘制模块自行 使用模板时会冲突，因此专用于基于 drawLayer 的单纯纹理绘制。 =====================================================================

---

### clearClipRect

方法

**说明**

解除矩形裁剪

---

### beginMaskClip

方法

**说明**

开始遮罩裁剪捕获

之后的绘制会在中间帧缓冲 (已清除为透明) 中进行。
必须调用对应的 endMaskClip()。可与 beginEffect() 嵌套。

---

### endMaskClip

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mask` | `&nbsp;` | 遮罩图像 (GLESTexture 或 Layer)。为 void 时则直通合成<br>(在只想在合成时可靠应用矩形裁剪的情况下使用) |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

应用遮罩合成

对之前的 beginMaskClip() 之后绘制的内容乘上遮罩图像的 α，
并以当前的 blendMode 合成到之前的绘制目标。
遮罩矩形外侧为 α=0 (完全裁剪)。

---

### beginStencilClip

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mask` | `&nbsp;` | 遮罩图像 (GLESTexture 或 Layer) |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `threshold` | `&nbsp;` | 使裁剪有效的 α 阈值 (1~255，不可省略) |

**说明**

开始模板裁剪

将遮罩图像的 α 大于等于阈值的区域写入模板，
把之后的 drawLayer 裁剪到该区域内。

---

### endStencilClip

方法

**说明**

结束模板裁剪

---
