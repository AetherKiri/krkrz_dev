# Threepp.SpotLight

聚光灯

从一个点呈圆锥状照射的光源。

## 成员列表

### 构造函数

- [SpotLight](#spotlight)

### 属性

- [type](#type)
- [distance](#distance)
- [angle](#angle)
- [penumbra](#penumbra)
- [decay](#decay)

### 方法

- [getPower](#getpower)
- [setPower](#setpower)
- [setShadowMapSize](#setshadowmapsize)
- [setShadowBias](#setshadowbias)
- [setShadowNormalBias](#setshadownormalbias)
- [setShadowRadius](#setshadowradius)
- [setShadowNearFar](#setshadownearfar)
- [dispose](#dispose)

---

### SpotLight

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `0xffffff` | 光的颜色 (0xRRGGBB) |
| `intensity` | `void` | 光的强度 |
| `distance` | `0` | 光的照射距离 |
| `angle` | `PI/3` | 照射角度（弧度） |
| `penumbra` | `0` | 半影（模糊） |
| `decay` | `1` | 衰减率 |

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

"SpotLight"（只读）

---

### distance

属性 \ 访问: `r/w`

**说明**

光的照射距离

---

### angle

属性 \ 访问: `r/w`

**说明**

照射角度

---

### penumbra

属性 \ 访问: `r/w`

**说明**

半影

---

### decay

属性 \ 访问: `r/w`

**说明**

衰减率

---

### getPower

方法

**说明**

获取光的功率

---

### setPower

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `power` | `&nbsp;` |  |

**说明**

设置光的功率

---

### setShadowMapSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**说明**

--- 阴影 (ShadowMap) --- 聚光灯的阴影用透视相机烘焙 (角度取决于 angle)

---

### setShadowBias

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

---

### setShadowNormalBias

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `bias` | `&nbsp;` |  |

---

### setShadowRadius

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `radius` | `&nbsp;` |  |

---

### setShadowNearFar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `near` | `&nbsp;` |  |
| `far` | `&nbsp;` |  |

---

### dispose

方法

**说明**

释放资源

---
