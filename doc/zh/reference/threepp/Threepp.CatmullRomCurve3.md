# Threepp.CatmullRomCurve3

CatmullRom 样条曲线

生成通过控制点的平滑曲线。

## 成员列表

### 构造函数

- [CatmullRomCurve3](#catmullromcurve3)

### 属性

- [closed](#closed)
- [tension](#tension)

### 方法

- [getLength](#getlength)
- [getPoint](#getpoint)

---

### CatmullRomCurve3

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `points` | `&nbsp;` | 控制点数组 (Vector3 的数组或 [x,y,z] 的数组) |
| `closed` | `false` | 是否为闭合曲线 |
| `curveType` | `0` | 曲线类型 (centripetal, chordal, catmullrom) |
| `tension` | `0.5` | 张力值 (用于 catmullrom 类型) |

**说明**

构造函数

---

### closed

属性 \ 访问: `r/w`

**说明**

闭合曲线标志

---

### tension

属性 \ 访问: `r/w`

**说明**

张力

---

### getLength

方法

**说明**

获取曲线长度

---

### getPoint

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `t` | `&nbsp;` |  |

**说明**

获取参数 t (0-1) 处的点

---
