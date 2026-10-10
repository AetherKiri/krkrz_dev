# Threepp.VRM

单个 VRM 模型

将 getScene() 的 Group add 到 Scene。每帧调用 update(dt)。

## 成员列表

### 方法

- [getScene](#getscene)
- [getBoneCount](#getbonecount)
- [getBoneNode](#getbonenode)
- [getNormalizedBoneNode](#getnormalizedbonenode)
- [resetNormalizedPose](#resetnormalizedpose)
- [update](#update)
- [setExpression](#setexpression)
- [getExpression](#getexpression)
- [getExpressionCount](#getexpressioncount)
- [getExpressionName](#getexpressionname)
- [expressionListJson](#expressionlistjson)
- [setMorph](#setmorph)
- [clearMorphs](#clearmorphs)
- [getMorphCount](#getmorphcount)
- [getMorphName](#getmorphname)
- [morphListJson](#morphlistjson)
- [setLookAtTarget](#setlookattarget)
- [clearLookAtTarget](#clearlookattarget)
- [hasLookAt](#haslookat)
- [applyAnimation](#applyanimation)
- [applyAnimationBlend](#applyanimationblend)
- [applyPose](#applypose)
- [applyHipsOffset](#applyhipsoffset)
- [getHipsOffset](#gethipsoffset)
- [captureRestPose](#capturerestpose)
- [blendToRest](#blendtorest)
- [setOffset](#setoffset)
- [setColliderScale](#setcolliderscale)
- [getColliderScale](#getcolliderscale)
- [getMetaName](#getmetaname)
- [getMetaVersion](#getmetaversion)
- [getMetaLicenseUrl](#getmetalicenseurl)

---

### getScene

方法

**说明**

绘制用根节点 -> Threepp.Group (add 到 Scene)

---

### getBoneCount

方法

**说明**

raw 骨骼数 -> int

---

### getBoneNode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**说明**

VRM human bone 名 -> Threepp.Bone (没有则为 void)

---

### getNormalizedBoneNode

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**说明**

归一化骨架的节点 -> Threepp.Object3D

---

### resetNormalizedPose

方法

**说明**

将归一化姿势恢复到 rest

---

### update

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dt` | `&nbsp;` | 距上一帧的经过秒数 (用于摆动部件的物理积分。为 0 时摆动停止) |

**说明**

每帧更新。统一反映 humanoid 骨架转写 + 约束 (node_constraint) + 表情 + 视线 +

摆动部件 (springBone)。

---

### setExpression

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |

**说明**

--- 表情 (Expression) ---

---

### getExpression

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**说明**

-> float

---

### getExpressionCount

方法

**说明**

-> int

---

### getExpressionName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**说明**

第 i 个表情名 -> string (超出范围时为 "")

---

### expressionListJson

方法

**说明**

全部表情的汇总 JSON '[{"name":…,"weight":…},…]' (供 Web UI 用)

---

### setMorph

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |

**说明**

--- raw morph (直接指定 blend shape。在表情之后应用 override) ---

---

### clearMorphs

方法

**说明**

解除全部 raw morph

---

### getMorphCount

方法

**说明**

-> int

---

### getMorphName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

**说明**

第 i 个 morph 名 -> string

---

### morphListJson

方法

**说明**

全部 morph 名的汇总 JSON '["Fcl_ALL_Neutral",…]' (供 Web UI 用)

---

### setLookAtTarget

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

--- 视线 (LookAt) ---

---

### clearLookAtTarget

方法

**说明**

解除注视

---

### hasLookAt

方法

**说明**

是否具有视线功能 -> bool

---

### applyAnimation

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vrmAnimation` | `&nbsp;` | Threepp.VRMAnimation |
| `time` | `&nbsp;` | 秒 |

**说明**

在时刻 time(秒) 应用 VRM 动画。应用后通过 update(dt) 转写到 raw 骨骼。

--- 动画 ---

---

### applyAnimationBlend

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vrmAnimation` | `&nbsp;` |  |
| `time` | `&nbsp;` |  |
| `blend` | `&nbsp;` |  |

**说明**

用于交叉淡化 (blend 0..1)

---

### applyPose

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `arr` | `&nbsp;` |  |
| `blend` | `&nbsp;` | 0..1 (省略时为 1 = 立即) |

**说明**

应用姿势。arr 是 [骨骼名, qx, qy, qz, qw, …] 的平坦数组。

--- 姿势 (归一化骨架的局部旋转) ---

---

### applyHipsOffset

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dx` | `&nbsp;` |  |
| `dy` | `&nbsp;` |  |
| `dz` | `&nbsp;` |  |

**说明**

将 hips 设为相对 rest 的偏移 (根运动)

---

### getHipsOffset

方法

**说明**

-> Vector3

---

### captureRestPose

方法

**说明**

记录 rest 归一化姿势

---

### blendToRest

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

slerp 到 rest (恢复站立姿势)

---

### setOffset

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

平移整个角色

---

### setColliderScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `scale` | `&nbsp;` |  |

**说明**

springBone 碰撞体半径的统一缩放 (默认 1.0 = 忠实)。

由于 VRoid 系列的碰撞体贴合身体、躯干侧面较薄弱，当头发陷入衣服时，
调到 1.2~1.4 左右可以改善 (opt-in、非标准)。

--- 摆动部件 (SpringBone) ---

---

### getColliderScale

方法

**说明**

-> float

---

### getMetaName

方法

**说明**

--- 元信息 ---

---

### getMetaVersion

方法

**说明**

-> string

---

### getMetaLicenseUrl

方法

**说明**

-> string

---
