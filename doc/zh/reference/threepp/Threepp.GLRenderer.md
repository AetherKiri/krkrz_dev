# Threepp.GLRenderer

OpenGL 渲染器

用于渲染场景的渲染器。
============================================================ Renderer 类 ============================================================

## 成员列表

### 构造函数

- [GLRenderer](#glrenderer)
- [GLRenderer](#glrenderer)

### 属性

- [autoClear](#autoclear)
- [autoClearColor](#autoclearcolor)
- [autoClearDepth](#autocleardepth)
- [autoClearStencil](#autoclearstencil)
- [sortObjects](#sortobjects)
- [useLegacyLights](#uselegacylights)
- [toneMappingExposure](#tonemappingexposure)

### 方法

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [render](#render)
- [setClearColor](#setclearcolor)
- [setPixelRatio](#setpixelratio)
- [setSize](#setsize)
- [setSampleCount](#setsamplecount)
- [setScissorTest](#setscissortest)
- [setShadowMapEnabled](#setshadowmapenabled)
- [setShadowMapType](#setshadowmaptype)
- [setShadowMapAutoUpdate](#setshadowmapautoupdate)
- [setShadowMapNeedsUpdate](#setshadowmapneedsupdate)
- [clear](#clear)
- [clearColor](#clearcolor)
- [clearDepth](#cleardepth)
- [clearStencil](#clearstencil)
- [dispose](#dispose)
- [resetState](#resetstate)

---

### GLRenderer

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `adaptor` | `&nbsp;` | GL 上下文提供对象 (持有 GLGetProcAddress) |
| `width` | `800` | 渲染宽度 |
| `height` | `600` | 渲染高度 |

**说明**

构造函数

在宿主准备的 GL 上下文上进行绘制的渲染器 (设备)。
将宿主的 GL 上下文提供对象 (gles 插件的
GLESAdaptor 等持有 GLGetProcAddress 属性的对象) 传给第 1 个参数后，
会从中获取函数指针 (getProcAddress) 并初始化 glad。
这与 effekseer / motion 插件的 Device 是相同的接线方式。

---

### GLRenderer

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `800` |  |
| `height` | `600` |  |

**说明**

构造函数 (传统形式)

如果调用方已经完成 GL 上下文的 current 化与 glad 的初始化，
则使用这个。无头 (headless) 生成。

---

### autoClear

属性 \ 访问: `r/w`

**说明**

是否自动清除

---

### autoClearColor

属性 \ 访问: `r/w`

**说明**

是否自动清除颜色缓冲区

---

### autoClearDepth

属性 \ 访问: `r/w`

**说明**

是否自动清除深度缓冲区

---

### autoClearStencil

属性 \ 访问: `r/w`

**说明**

是否自动清除模板缓冲区

---

### sortObjects

属性 \ 访问: `r/w`

**说明**

是否对对象排序

---

### useLegacyLights

属性 \ 访问: `r/w`

**说明**

是传统光照 (true) 还是物理精确 (false，默认)

---

### toneMappingExposure

属性 \ 访问: `r/w`

**说明**

色调映射的曝光

---

### onBeginScene

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 表面宽度 |
| `height` | `&nbsp;` | 表面高度 |

**说明**

帧绘制开始 (在宿主 GL 上下文为 current 的状态下调用)

使内部状态缓存失效，并设置绘制大小。
在 adaptor.capture() 的回调内、render() 之前调用。

---

### onEndScene

方法

**说明**

帧绘制结束

在 render() 之后调用。目前不进行特殊处理，但为了与宿主之间的
GL 状态保持一致，而预先确保调用位置。

---

### render

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `scene` | `&nbsp;` | 场景 |
| `camera` | `&nbsp;` | 相机 |

**说明**

渲染场景

---

### setClearColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 颜色 (0xRRGGBB) |
| `alpha` | `1` | Alpha 值 |

**说明**

设置清除色

---

### setPixelRatio

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ratio` | `&nbsp;` |  |

**说明**

设置像素比

---

### setSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

设置大小

---

### setSampleCount

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `count` | `&nbsp;` | 0/1=无效，2/4/8 等。默认 4。onBeginScene 绘制到内部多重采样 FBO，<br>onEndScene 解析 (resolve) 并转送到宿主 FBO。可减轻轮廓的锯齿。<br>若在意边缘的 premultiplied alpha，可在宿主侧 (GLESAdaptor.unpremultiply) 进行校正。 |

**说明**

设置 MSAA (多重采样抗锯齿) 的采样数

---

### setScissorTest

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**说明**

剪裁测试的启用/禁用

---

### setShadowMapEnabled

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**说明**

阴影 (ShadowMap) 的启用/禁用

为 true 时启用阴影贴图绘制。另外还需要：投射阴影的光源的
castShadow=true、接收阴影的网格的 receiveShadow=true、投射阴影的网格的
castShadow=true。在 GLES/捕获 FBO 路径下也能运行 (将深度烘焙到阴影用 FBO，
在主绘制时恢复到原来的绘制目标)。
使用示例:
renderer.setShadowMapEnabled(true);
var dir = new Threepp.DirectionalLight(0xffffff, 2.0);
dir.setPosition(3, 5, 2); dir.castShadow = true;
dir.setShadowOrthoBounds(-6, 6, 6, -6); dir.setShadowNearFar(0.5, 30);
scene.add(dir);
floor.receiveShadow = true; box.castShadow = true;

---

### setShadowMapType

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` |  |

**说明**

0=Basic，1=PCF (默认)，2=PCFSoft，3=相当于 VSM

---

### setShadowMapAutoUpdate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**说明**

每帧更新阴影 (默认 true)

---

### setShadowMapNeedsUpdate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `enabled` | `&nbsp;` |  |

**说明**

在 autoUpdate=false 时只更新 1 次

---

### clear

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `true` |  |
| `depth` | `true` |  |
| `stencil` | `true` |  |

**说明**

清除缓冲区

---

### clearColor

方法

**说明**

清除颜色缓冲区

---

### clearDepth

方法

**说明**

清除深度缓冲区

---

### clearStencil

方法

**说明**

清除模板缓冲区

---

### dispose

方法

**说明**

释放资源

---

### resetState

方法

**说明**

重置状态

---
