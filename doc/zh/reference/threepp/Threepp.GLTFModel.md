# Threepp.GLTFModel

已加载的 glTF 模型 (GLTFLoader 的返回值)

保存模型的场景图与动画信息。

## 成员列表

### 方法

- [getScene](#getscene)
- [getAnimationCount](#getanimationcount)
- [getAnimationName](#getanimationname)
- [getAnimationDuration](#getanimationduration)
- [getPartCount](#getpartcount)
- [getPartGeometry](#getpartgeometry)
- [getPartMaterial](#getpartmaterial)
- [getPartName](#getpartname)

---

### getScene

方法

**说明**

-> Threepp.Group (add 到 Scene 后绘制)

---

### getAnimationCount

方法

**说明**

-> int (内置动画剪辑数)

---

### getAnimationName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**说明**

(i) -> string (剪辑名)

---

### getAnimationDuration

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**说明**

(i) -> float (秒)

---

### getPartCount

方法

**说明**

--- 部件 (网格) 的提取 --- 想排列几百个相同模型时，若按数量读取 GLB 并排列 Mesh，draw call 就会直接等于个数。从这里取出并汇总到 InstancedMesh，则只需 1 个。

---

### getPartGeometry

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**说明**

(i) -> BufferGeometry

---

### getPartMaterial

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**说明**

(i) -> Material (共享原始对象。因为持有纹理)

---

### getPartName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `i` | `&nbsp;` |  |

**说明**

(i) -> string (用于分辨是哪个部件)

---
