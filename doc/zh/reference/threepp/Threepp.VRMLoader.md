# Threepp.VRMLoader

VRM 加载器

读取 .vrm 并返回 VRM。同时支持 VRM 0.x / 1.0。
============================================================ VRM (VRoid/VRM 0.x、1.0 虚拟形象) ------------------------------------------------------------ 用 VRMLoader 读取 .vrm，将 getScene() 的 Group add 到 Scene 进行绘制。 每帧通过 update(dt) 反映 humanoid 骨架/表情/视线/摆动部件 (springBone)。 动画 (.vrma) 用 VRMAnimationLoader 读取，applyAnimation(anim, time) → update(dt)。 MToon (卡通)/轮廓线/matcap/normalMap/摆动部件/约束由内部自动处理。 ============================================================

## 成员列表

### 构造函数

- [VRMLoader](#vrmloader)

### 方法

- [load](#load)
- [loadStorage](#loadstorage)

---

### VRMLoader

构造函数

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `osPath` | `&nbsp;` | 文件系统上的绝对/相对路径 |

**返回值**

VRM  (失败时 void)

**说明**

从 OS 路径读取 (调试/独立运行用)。

---

### loadStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storageName` | `&nbsp;` | 存储名 (例 Storages.getPlacedPath("model.vrm")) |

**返回值**

VRM  (失败时 void)

**说明**

从吉里吉里存储名读取 (正式用。支持归档)。

---
