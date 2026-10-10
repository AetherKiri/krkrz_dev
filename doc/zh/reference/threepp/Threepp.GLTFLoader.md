# Threepp.GLTFLoader

通用 glTF/GLB 加载器

不解析 VRM 扩展，作为普通 glTF 读取。GLB(自包含) 更可靠。
蒙皮网格会以绑定姿势 (T 姿势) 读取。播放骨骼动画需要
另外的动画机制 (目前尚不支持模型自身的动画播放。面向姿势固定的小物件/
地形/建筑，以及在 TJS 侧驱动变换的用途)。
============================================================ 通用 glTF / GLB 加载器 (用于 VRM 以外的模型) 读取非 VRM 的一般 3D 模型 (小物件/地形/建筑/带动画的模型)。 将 GLTFLoader.loadStorage() 返回的 GLTFModel 的 getScene() (Group) add 到 Scene，并用 setPosition/setScale/setRotation 自然地放置。 ============================================================

## 成员列表

### 构造函数

- [GLTFLoader](#gltfloader)

### 方法

- [load](#load)
- [loadStorage](#loadstorage)

---

### GLTFLoader

构造函数

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `osPath` | `&nbsp;` |  |

**说明**

从 OS 路径 (.gltf+外部资源也可解析) -> GLTFModel

---

### loadStorage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storageName` | `&nbsp;` |  |

**说明**

从吉里吉里存储名 (推荐 GLB) -> GLTFModel

---
