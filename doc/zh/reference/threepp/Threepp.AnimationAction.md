# Threepp.AnimationAction

正在播放的一个动画（由 ModelAnimator.clipAction/play 返回）

由 mixer 内部持有。在 ModelAnimator 存活期间有效。
链式方法以无返回值（void）形式公开。

## 成员列表

### 方法

- [play](#play)
- [stop](#stop)
- [reset](#reset)
- [isRunning](#isrunning)
- [setLoop](#setloop)
- [setEffectiveWeight](#seteffectiveweight)
- [setEffectiveTimeScale](#seteffectivetimescale)
- [fadeIn](#fadein)
- [fadeOut](#fadeout)
- [crossFadeTo](#crossfadeto)
- [setDuration](#setduration)

---

### play

方法

**说明**

开始播放

---

### stop

方法

**说明**

停止

---

### reset

方法

**说明**

倒回开头

---

### isRunning

方法

**说明**

-> bool

---

### setLoop

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `mode` | `&nbsp;` |  |
| `reps` | `&nbsp;` |  |

**说明**

mode: Loop_* 常量，reps: 重复次数（-1 表示无限）

---

### setEffectiveWeight

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |

**说明**

混合权重 (0..1)。用于多个动画的合成

---

### setEffectiveTimeScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

此动作的播放速度

---

### fadeIn

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**说明**

在 sec 秒内淡入

---

### fadeOut

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**说明**

在 sec 秒内淡出

---

### crossFadeTo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `other` | `&nbsp;` |  |
| `dur` | `&nbsp;` |  |
| `warp` | `&nbsp;` |  |

**说明**

在 dur 秒内交叉淡化到另一个 AnimationAction

---

### setDuration

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `sec` | `&nbsp;` |  |

**说明**

覆盖片段的有效长度

---
