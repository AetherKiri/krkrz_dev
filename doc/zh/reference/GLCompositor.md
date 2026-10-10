# GLCompositor

这是即使在不使用 OGLDrawDevice 的状况下 ( 画面的绘制设备为 D3D11 或
SDL_Renderer 等 )，也能在背后进行基于 OpenGL ES 的离屏合成，并将其结果写回
Layer 的类。

它以引擎本体内置、并且共享 Canvas / Offscreen 既有 GL 绘制代码的形式，
提供相当于旧 krkrgles 插件 GLESAdaptor 的功能。不依赖绘制设备，
从窗口获取 GL 上下文并自行将其设为当前 ( 不进行向画面的 present，仅绘制到
离屏 FBO )。当 OGL 绘制设备正在运行时，共享其上下文。

capture() 的回调以“incontextof 该合成器”执行，
回调内的 this 会变为该 GLCompositor。因此可以直接利用 this.canvas
( 内部 Canvas ) 的完整 API (drawTexture / beginEffect / endEffect / 裁剪等) 以及
this.drawLayer / this.copyLayer (GLESAdaptor 兼容)。

## 成员列表

### 构造函数

- [GLCompositor](#glcompositor)

### 属性

- [canvas](#canvas)
- [blendMode](#blendmode)
- [unpremultiply](#unpremultiply)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [GLGetProcAddress](#glgetprocaddress)

### 方法

- [capture](#capture)
- [drawLayer](#drawlayer)
- [copyLayer](#copylayer)
- [setScreenSize](#setscreensize)
- [makeCurrent](#makecurrent)

---

### GLCompositor

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `window` | `Window` | `&nbsp;` | 目标 Window 对象 |

**说明**

生成 GLCompositor。

使用指定窗口的 GL 上下文进行初始化。

---

### canvas

属性 \ 访问: `r`

**说明**

内部 Canvas。

可以使用 drawTexture / beginEffect / endEffect / 裁剪等 Canvas 的
完整 API。

---

### blendMode

属性 \ 访问: `r/w`

**说明**

绘制的合成模式指定。

对应内部 Canvas 的 blendMode。

---

### unpremultiply

属性 \ 访问: `r/w`

**说明**

在 capture 读回时是否进行 un-premultiply ( 默认 false )。

设为 true 后，会在 capture() 读回时将 premultiplied-alpha 还原为
straight-alpha ( RGB = RGB×255÷A ) 并写入 Layer。对于启用了 MSAA 的
3D ( VRM 立绘等 )，其半透明边缘若以 premultiplied 原样被读回，通常 Alpha 合成
( ltAlpha ) 会在边缘产生白色镶边，此设置可以防止这一问题。相当于旧 GLESAdaptor.unpremultiply。

---

### screenWidth

属性 \ 访问: `r/w`

**说明**

离屏合成的默认宽度。

---

### screenHeight

属性 \ 访问: `r/w`

**说明**

离屏合成的默认高度。

---

### GLGetProcAddress

属性 \ 访问: `r`

**说明**

指向 GL 入口点解析函数的指针 (整数)。

用作 GLES 系插件 ( EffekseerDevice 等 ) 的 oglbase。
例: new EffekseerDevice(compositor)。

---

### capture

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | 绘制结果的写回目标 Layer |
| `callback` | `&nbsp;` | `&nbsp;` | 绘制回调 function(w:int, h:int, param) (this=GLCompositor) |
| `param` | `&nbsp;` | `&nbsp;` | 传给 callback 的任意值 |
| `color` | `int` | `&nbsp;` | 清除色 (ARGB) |

**说明**

执行离屏合成，并将结果写回 layer。

用 color 清除 layer 大小的离屏 FBO 后，
以“incontextof 该合成器”调用 callback(w, h, param) 让其绘制，
并将结果读回到 layer 的主图像。callback 内 this 会变为
该 GLCompositor，因此可以使用 this.canvas 进行 drawTexture / beginEffect /
裁剪等绘制，也可以直接利用 this.drawLayer / this.copyLayer
( GLESAdaptor 兼容。canvas 不是通过参数，而是通过 this.canvas 引用 )。

---

### drawLayer

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | 绘制源 Layer |
| `a` | `real` | `&nbsp;` | 变换矩阵 m11 |
| `b` | `real` | `&nbsp;` | 变换矩阵 m12 |
| `c` | `real` | `&nbsp;` | 变换矩阵 m21 |
| `d` | `real` | `&nbsp;` | 变换矩阵 m22 |
| `tx` | `real` | `&nbsp;` | 平移 x |
| `ty` | `real` | `&nbsp;` | 平移 y |
| `opacity` | `int` | `255` | = 255 不透明度 (0~255) |

**说明**

以仿射变换 + 不透明度将 layer 绘制到当前绘制目标。

从 capture() 的回调内调用。变换矩阵由
2x2 部分 (a,b,c,d) + 平移 (tx,ty) 指定。

---

### copyLayer

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `layer` | `Layer` | `&nbsp;` | 绘制源 Layer |
| `left` | `int` | `&nbsp;` | 放置 x |
| `top` | `int` | `&nbsp;` | 放置 y |

**说明**

将 layer 原样绘制到 (left, top)。

是 drawLayer 的单纯平移版。从 capture() 的回调内
调用。

---

### setScreenSize

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `width` | `int` | `&nbsp;` | 宽度 |
| `height` | `int` | `&nbsp;` | 高度 |

**说明**

设置离屏合成的默认大小。

---

### makeCurrent

方法

**说明**

将该 GLCompositor 的 GL 上下文设为当前。

---
