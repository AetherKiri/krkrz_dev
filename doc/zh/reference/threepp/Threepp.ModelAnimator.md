# Threepp.ModelAnimator

模型动画播放器（相当于 three.js 的 AnimationMixer）

由于会在内部持续保持目标 root（通常为 model.getScene()）存活，
所以只要一直持有 ModelAnimator，模型也不会被释放。
============================================================ 动画播放 (glTF/GLB 内置动画) 相当于 three.js 的 AnimationMixer。用 ModelAnimator 播放 GLTFModel 持有的动画剪辑。root 通常传入 model.getScene()。 必须每帧调用 update(dt 秒)。 ※ VRM 的动画(.vrma)属于另一体系。VRM 请使用 VRMLoader/VRMAnimation。 ModelAnimator 用于“VRM 以外的 glTF/GLB 模型自身的动画”。 ============================================================

## 成员列表

### 构造函数

- [ModelAnimator](#modelanimator)

### 方法

- [clipAction](#clipaction)
- [play](#play)
- [update](#update)
- [stopAll](#stopall)
- [setTimeScale](#settimescale)
- [getTimeScale](#gettimescale)

---

### ModelAnimator

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `root` | `&nbsp;` | 动画目标的 Object3D (通常为 model.getScene()) |

---

### clipAction

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `model` | `&nbsp;` |  |
| `index` | `&nbsp;` |  |

**说明**

(GLTFModel, 剪辑 index) -> AnimationAction (未播放)

---

### play

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `model` | `&nbsp;` |  |
| `index` | `&nbsp;` |  |

**说明**

(GLTFModel, index) -> AnimationAction (循环设置+reset+play 一并完成。常用写法)

---

### update

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dt` | `&nbsp;` |  |

**说明**

(经过秒数) 每帧调用以推进动画

---

### stopAll

方法

**说明**

停止全部动作

---

### setTimeScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `s` | `&nbsp;` |  |

**说明**

整体播放速度 (1.0=等速)

---

### getTimeScale

方法

**说明**

-> float

---
