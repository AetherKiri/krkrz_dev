# Threepp.VRMAnimationLoader

VRM 动画加载器

## 成员列表

### 构造函数

- [VRMAnimationLoader](#vrmanimationloader)

### 方法

- [load](#load)
- [loadStorage](#loadstorage)
- [exportPoseSeq](#exportposeseq)

---

### VRMAnimationLoader

构造函数

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `osPath` | `&nbsp;` |  |

**说明**

从 OS 路径 (调试用) -> VRMAnimation

---

### loadStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storageName` | `&nbsp;` |  |

**说明**

从吉里吉里存储名 (正式用) -> VRMAnimation

---

### exportPoseSeq

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `boneNames` | `&nbsp;` | [骨骼名,…] (nBones) |
| `times` | `&nbsp;` | [秒,…] (nKeys) |
| `quatsFlat` | `&nbsp;` | [(key,bone) 行优先的 qx,qy,qz,qw,…] (nKeys*nBones*4) |
| `hipsFlat` | `&nbsp;` | hips 偏移 [dx,dy,dz,…] (nKeys*3。空数组 = 无轨道) |
| `exprNames` | `&nbsp;` | 表情名 [] (省略/空 = 无表情轨道) |
| `exprWeightsFlat` | `&nbsp;` | 表情 weight (expr-major 平坦, nExpr*nKeys) |
| `path` | `&nbsp;` | 输出存储名 (裸名则直接位于 data/ 下) |

**说明**

将姿势序列导出为 1 个 VRMA (.vrma = glTF-JSON + base64)。

输入是平坦的并行数组。写出的文件可以用 loadStorage 读回。

---
