# EffekseerPlayer

播放用播放器

负责 1 个特效实例的播放、配置与绘制。

## 成员列表

### 构造函数

- [EffekseerPlayer](#effekseerplayer)

### 属性

- [device](#device)
- [effect](#effect)
- [loaded](#loaded)
- [playing](#playing)
- [instanceCount](#instancecount)
- [renderScale](#renderscale)
- [left](#left)
- [top](#top)
- [z](#z)
- [zoomX](#zoomx)
- [zoomY](#zoomy)
- [angle](#angle)
- [speed](#speed)
- [color](#color)
- [paused](#paused)
- [shown](#shown)
- [spawnDisabled](#spawndisabled)
- [layer](#layer)
- [meta](#meta)

### 方法

- [load](#load)
- [loadEffect](#loadeffect)
- [clear](#clear)
- [play](#play)
- [stop](#stop)
- [stopRoot](#stoproot)
- [progress](#progress)
- [moveToFrame](#movetoframe)
- [render](#render)
- [setRenderMatrix](#setrendermatrix)
- [getRenderMatrix](#getrendermatrix)
- [setRenderScale](#setrenderscale)
- [getRenderScale](#getrenderscale)
- [setCoord](#setcoord)
- [getCoord](#getcoord)
- [setZoom](#setzoom)
- [getZoom](#getzoom)
- [setAngleDeg](#setangledeg)
- [getAngleDeg](#getangledeg)
- [setAngleRad](#setanglerad)
- [getAngleRad](#getanglerad)
- [setRotate](#setrotate)
- [getRotate](#getrotate)
- [setSpeed](#setspeed)
- [getSpeed](#getspeed)
- [setTargetLocation](#settargetlocation)
- [setRandomSeed](#setrandomseed)
- [setDynamicInput](#setdynamicinput)
- [setDynamicInputByName](#setdynamicinputbyname)
- [getDynamicInputByName](#getdynamicinputbyname)
- [findDynamicInput](#finddynamicinput)
- [readMeta](#readmeta)
- [getDynamicInput](#getdynamicinput)
- [sendTrigger](#sendtrigger)

---

### EffekseerPlayer

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `device` | `&nbsp;` | EffekseerDevice 实例 |

**说明**

构造函数

---

### device

属性 \ 访问: `r/w`

**说明**

只读

---

### effect

属性 \ 访问: `r/w`

**说明**

只读: 通过 loadEffect() 分配的 EffekseerEffect

---

### loaded

属性 \ 访问: `r/w`

**说明**

只读

---

### playing

属性 \ 访问: `r/w`

**说明**

只读: 是否正在播放

---

### instanceCount

属性 \ 访问: `r/w`

**说明**

只读: 该特效的粒子数

---

### renderScale

属性 \ 访问: `r/w`

---

### left

属性 \ 访问: `r/w`

---

### top

属性 \ 访问: `r/w`

---

### z

属性 \ 访问: `r/w`

---

### zoomX

属性 \ 访问: `r/w`

---

### zoomY

属性 \ 访问: `r/w`

---

### angle

属性 \ 访问: `r/w`

**说明**

度

---

### speed

属性 \ 访问: `r/w`

---

### color

属性 \ 访问: `r/w`

**说明**

整体颜色 0xAARRGGBB (默认 0xFFFFFFFF)。会与整个特效相乘。

---

### paused

属性 \ 访问: `r/w`

**说明**

暂停

---

### shown

属性 \ 访问: `r/w`

**说明**

显示/隐藏

---

### spawnDisabled

属性 \ 访问: `r/w`

**说明**

停止生成新粒子

---

### layer

属性 \ 访问: `r/w`

**说明**

所属图层 (0~31)

---

### meta

属性 \ 访问: `r/w`

**说明**

正在播放的素材的附属信息 (与 EffekseerEffect.meta 相同)

通过 player.load() 加载时也做了桥接，使其可以访问。

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 存储名 (.efkzip / .efkefc / .efk) |
| `magnification` | `&nbsp;` | 加载时的放大率 (省略时为 1.0) |
| `entry` | `&nbsp;` | .efkzip 内的特效文件名 (可省略) |

**说明**

加载特效文件 (该播放器专用)

参数与 EffekseerEffect.load 相同 (支持 .efkzip)

---

### loadEffect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `effect` | `&nbsp;` | EffekseerEffect 实例 |

**说明**

分配已加载的 EffekseerEffect

---

### clear

方法

**说明**

解除分配 (正在播放时则停止)

---

### play

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `startFrame` | `&nbsp;` | 起始帧 (省略时为 0) |

**说明**

开始播放。如果正在播放，则先停止后再重新开始。

---

### stop

方法

**说明**

立即停止 (粒子也会消失)

---

### stopRoot

方法

**说明**

仅停止根节点。停止生成新粒子，剩余粒子自然消亡。

想要“让特效漂亮地结束”时，请使用该方法。

---

### progress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tick` | `&nbsp;` | 经过时间(毫秒)<br>配置相关的设置请在 progress() 之前进行。 |

**说明**

推进

---

### moveToFrame

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `frame` | `&nbsp;` | 帧数 (以 60fps 为基准) |

**说明**

移动到指定帧 (从头重新计算，因此速度较慢)

---

### render

方法

**说明**

绘制。在 OpenGL 上下文上，于 device.onBeginScene()~onEndScene() 之间调用。

---

### setRenderMatrix

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m11` | `&nbsp;` |  |
| `m12` | `&nbsp;` |  |
| `m13` | `&nbsp;` |  |
| `m21` | `&nbsp;` |  |
| `m22` | `&nbsp;` |  |
| `m23` | `&nbsp;` |  |

**说明**

设置绘制矩阵 (外部的仿射变换)

X' = m11*x + m12*y + m13
Y' = m21*x + m22*y + m23

---

### getRenderMatrix

方法

**说明**

%[ m11:, m12:, m13:, m21:, m22:, m23: ]

---

### setRenderScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**说明**

作用于绘制矩阵线性部分的倍率 (默认 1.0)

---

### getRenderScale

方法

---

### setCoord

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |

**说明**

显示位置 (相对画面中央的像素偏移)

---

### getCoord

方法

**说明**

%[ x:, y:, z: ]

---

### setZoom

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `zx` | `&nbsp;` |  |
| `zy` | `&nbsp;` |  |

**说明**

缩放 (默认 1.0)

---

### getZoom

方法

**说明**

%[ x:, y: ]

---

### setAngleDeg

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `degree` | `&nbsp;` |  |

**说明**

画面内旋转。角度为正时在画面上为顺时针方向。

---

### getAngleDeg

方法

---

### setAngleRad

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `radian` | `&nbsp;` |  |

---

### getAngleRad

方法

---

### setRotate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

3 轴旋转(度)。z 与 setAngleDeg 相同，为画面内旋转。

x / y 是深度方向的倾斜，与透视投影组合使用时更容易看出效果。

---

### getRotate

方法

**说明**

%[ x:, y:, z: ]

---

### setSpeed

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `speed` | `&nbsp;` |  |

**说明**

播放速度 (1.0 为等速)

---

### getSpeed

方法

---

### setTargetLocation

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

目标位置 (在特效侧使用“依赖目标”的情况下)

坐标与配置相同，为以画面中央为原点的像素坐标。

---

### setRandomSeed

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `seed` | `&nbsp;` |  |

**说明**

固定随机数种子

---

### setDynamicInput

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 特效侧定义的动态输入编号 (从 0 开始)<br>超出范围的 index 会被忽略 (获取时返回 0)。 |
| `value` | `&nbsp;` |  |

**说明**

动态参数 (Effekseer 编辑器的 Dynamic Input)

---

### setDynamicInputByName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

**说明**

按名称注入 / 读取动态参数

对应关系会从 .efkzip 的 effect.json 自动载入
(也可以通过 EffekseerEffect.setDynamicInputNames() 替换)。
传入未知名称时会抛出异常。

player.setDynamicInputByName("emitter.x", 120);

---

### getDynamicInputByName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### findDynamicInput

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**说明**

确认是否为可注入的名称。未知时返回 -1

---

### readMeta

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### getDynamicInput

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### sendTrigger

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 特效侧定义的触发器编号 (从 0 开始) |

**说明**

发送触发器 (Effekseer 编辑器的 Trigger)

---
