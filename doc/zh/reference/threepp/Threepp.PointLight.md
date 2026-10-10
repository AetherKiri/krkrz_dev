# Threepp.PointLight

点光源

从一点向所有方向照射的光源。

## 成员列表

### 构造函数

- [PointLight](#pointlight)

### 属性

- [type](#type)
- [distance](#distance)
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

### PointLight

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `0xffffff` | 光的颜色 (0xRRGGBB) |
| `intensity` | `void` | 光的强度 |
| `distance` | `0` | 光能到达的距离（0 表示无限） |
| `decay` | `1` | 衰减率 |

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

"PointLight"（只读）

---

### distance

属性 \ 访问: `r/w`

**说明**

光能到达的距离

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

--- 阴影 (ShadowMap) --- ※ setShadowOrthoBounds 是平行光专用 (对点光源无效)

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
