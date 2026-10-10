# Threepp.DirectionalLight

平行光（类似太阳光的光）

从无限远处平行照射的光源。可以投射阴影。

## 成员列表

### 构造函数

- [DirectionalLight](#directionallight)

### 属性

- [type](#type)

### 方法

- [setShadowMapSize](#setshadowmapsize)
- [setShadowBias](#setshadowbias)
- [setShadowNormalBias](#setshadownormalbias)
- [setShadowRadius](#setshadowradius)
- [setShadowNearFar](#setshadownearfar)
- [setShadowOrthoBounds](#setshadoworthobounds)
- [dispose](#dispose)

---

### DirectionalLight

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `0xffffff` | 光的颜色 (0xRRGGBB) |
| `intensity` | `void` | 光的强度 |

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

"DirectionalLight"（只读）

---

### setShadowMapSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**说明**

--- 阴影 (ShadowMap) --- 要用该光源投射阴影，需要设置 castShadow=true、 renderer.setShadowMapEnabled(true)，并且阴影接收侧需要 receiveShadow=true。 平行光的阴影由正交相机烘焙，因此要用 setShadowOrthoBounds 指定覆盖场景的范围。

---

### setShadowBias

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

**说明**

防止阴影痤疮的偏置 (例 -0.0005)

---

### setShadowNormalBias

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

**说明**

法线方向偏置

---

### setShadowRadius

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |

**说明**

软阴影半径 (PCF)

---

### setShadowNearFar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

**说明**

阴影用相机的 near/far

---

### setShadowOrthoBounds

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` |  |
| `right` | `&nbsp;` |  |
| `top` | `&nbsp;` |  |
| `bottom` | `&nbsp;` |  |

**说明**

平行光的阴影范围 (正交投影)

---

### dispose

方法

**说明**

释放资源

---
