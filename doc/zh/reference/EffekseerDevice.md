# EffekseerDevice

绘制设备

每个 OpenGL(ES) 上下文生成 1 个。

## 成员列表

### 构造函数

- [EffekseerDevice](#effekseerdevice)

### 属性

- [instanceMax](#instancemax)
- [squareMaxCount](#squaremaxcount)
- [premultipliedAlpha](#premultipliedalpha)
- [projectionMode](#projectionmode)
- [frameRate](#framerate)
- [restorationOfStates](#restorationofstates)
- [clearDepth](#cleardepth)
- [verbose](#verbose)
- [surfaceWidth](#surfacewidth)
- [surfaceHeight](#surfaceheight)
- [totalInstanceCount](#totalinstancecount)
- [drawCallCount](#drawcallcount)
- [drawVertexCount](#drawvertexcount)
- [deviceInfo](#deviceinfo)

### 方法

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [update](#update)
- [beginUpdate](#beginupdate)
- [endUpdate](#endupdate)
- [onLostDevice](#onlostdevice)
- [onResetDevice](#onresetdevice)
- [stopAll](#stopall)
- [setCapacity](#setcapacity)
- [setPerspective](#setperspective)
- [setOrthographic](#setorthographic)
- [setCamera](#setcamera)
- [resetCamera](#resetcamera)
- [getGLError](#getglerror)

---

### EffekseerDevice

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `oglbase` | `&nbsp;` | 持有 GLGetProcAddress 的对象 (GetProcAddress 的提供来源)<br>可以指定以下任意一个:<br>- krkrgles 插件的 GLESAdaptor<br>- Window (使用引擎本体内置 OpenGL 绘制 = OGLDrawDevice 的构成时)<br>※ 实现只是读取传入对象的 GLGetProcAddress 属性。<br>OGLDrawDevice 自身没有这个属性，因此请传入 Window<br>(与传给 threepp 的 GLRenderer 的相同)<br>针对当前 OpenGL ES 上下文初始化。<br>※请在上下文为 current 的状态下生成 |

**说明**

构造函数

---

### instanceMax

属性 \ 访问: `r/w`

**说明**

只读

---

### squareMaxCount

属性 \ 访问: `r/w`

**说明**

只读

---

### premultipliedAlpha

属性 \ 访问: `r/w`

**说明**

是否以预乘 Alpha 绘制 (默认 false)。

更改后会重建管理器/渲染器 (与 setCapacity 同样的注意事项)。

---

### projectionMode

属性 \ 访问: `r/w`

**说明**

投影模式

EffekseerDevice.EffekseerProjectionOrthographic … 平行投影 (默认)
EffekseerDevice.EffekseerProjectionPerspective  … 透视投影

---

### frameRate

属性 \ 访问: `r/w`

**说明**

推进的基准帧率 (默认 60)。

用于将 progress(tick) / update(tick) 的毫秒换算为帧数。

---

### restorationOfStates

属性 \ 访问: `r/w`

**说明**

是否在绘制前后保存/恢复 GL 状态 (默认 true)。

与吉里吉里及其他插件的 GL 绘制混合使用时，请保持 true。

---

### clearDepth

属性 \ 访问: `r/w`

**说明**

是否在 onBeginScene 中清除深度缓冲区 (默认 true)

当特效侧的节点中深度测试 (ZTest) 有效时，会与绘制目标的深度值
进行比较。吉里吉里准备的离屏缓冲区深度有时未初始化
(krkrgles 的 capture 只清除颜色和模板)，
直接使用的话特效将完全不显示。
默认每帧用 1.0 初始化。仅在调用方自行管理深度时
设为 false。

---

### verbose

属性 \ 访问: `r/w`

**说明**

将素材的打开结果和 Effekseer 的详细日志输出到吉里吉里的日志 (默认 false)

用于排查纹理找不到等问题。

---

### surfaceWidth

属性 \ 访问: `r/w`

**说明**

只读: 最后一次 onBeginScene 的宽度

---

### surfaceHeight

属性 \ 访问: `r/w`

**说明**

只读: 同上的高度

---

### totalInstanceCount

属性 \ 访问: `r/w`

**说明**

只读: 全部粒子数

---

### drawCallCount

属性 \ 访问: `r/w`

**说明**

只读: 最近一次的绘制调用数

---

### drawVertexCount

属性 \ 访问: `r/w`

**说明**

只读: 最近一次的顶点数

---

### deviceInfo

属性 \ 访问: `r/w`

**说明**

只读: 整套设置值(字典)

---

### onBeginScene

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 绘制目标的宽度(像素) |
| `height` | `&nbsp;` | 绘制目标的高度(像素)<br>※请在生成时的上下文中调用 |

**说明**

开始绘制。更新投影矩阵并开始 Effekseer 的绘制。

---

### onEndScene

方法

**说明**

结束绘制。

---

### update

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tick` | `&nbsp;` | 经过时间(毫秒)<br>如果按播放器逐个调用 progress()，则无需调用该方法。 |

**说明**

让所有特效一并推进。

---

### beginUpdate

方法

**说明**

按播放器逐个推进的汇总处理

调用大量 EffekseerPlayer.progress() 时，用 beginUpdate()~endUpdate()
包围可以使内部的缓冲区交换只需 1 次。
device.beginUpdate();
for (...) players[i].progress(tick);
device.endUpdate();

---

### endUpdate

方法

---

### onLostDevice

方法

**说明**

GL 资源的释放/重建 (应对上下文丢失)

---

### onResetDevice

方法

---

### stopAll

方法

**说明**

停止所有正在播放的特效

---

### setCapacity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `instanceMax` | `&nbsp;` | 可同时存在的粒子数上限 (默认 4000) |
| `squareMaxCount` | `&nbsp;` | 每次绘制的精灵数上限 (默认 8192) |

**说明**

设置内部缓冲区容量。由于内部的管理器/渲染器会被重建，

※请在加载特效之前、生成播放器之前调用。
现有的 EffekseerEffect / EffekseerPlayer 将失效。

---

### setPerspective

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fovDegree` | `&nbsp;` | 垂直视场角(度)  默认 45 |
| `znear` | `&nbsp;` | 近裁剪面  默认 1 |
| `zfar` | `&nbsp;` | 远裁剪面  默认 10000<br>摄像机会被自动配置到“在 Z=0 平面上 1 世界单位 = 1 像素”的距离。 |

**说明**

切换到透视投影并设置参数

---

### setOrthographic

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `znear` | `&nbsp;` | 近裁剪面 |
| `zfar` | `&nbsp;` | 远裁剪面 |

**说明**

切换到平行投影并设置深度范围

---

### setCamera

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `px` | `&nbsp;` |  |
| `py` | `&nbsp;` |  |
| `pz` | `&nbsp;` |  |
| `tx` | `&nbsp;` |  |
| `ty` | `&nbsp;` |  |
| `tz` | `&nbsp;` |  |

**说明**

手动配置摄像机 (与配置相同，为以画面中央为原点的像素坐标)

默认会自动配置到从正面观看原点 (画面中央) 的位置。

---

### resetCamera

方法

**说明**

将摄像机恢复为自动配置

---

### getGLError

方法

**说明**

获取最近的 GL 错误代码 (读取后会被清除。为 0 表示没有错误)

---
