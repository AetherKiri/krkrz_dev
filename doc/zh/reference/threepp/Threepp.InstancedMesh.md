# Threepp.InstancedMesh

实例化网格

使用相同的几何体和材质绘制多个实例。

## 成员列表

### 构造函数

- [InstancedMesh](#instancedmesh)

### 属性

- [type](#type)
- [count](#count)

### 方法

- [getMatrixAt](#getmatrixat)
- [setMatrixAt](#setmatrixat)
- [getColorAt](#getcolorat)
- [setColorAt](#setcolorat)
- [computeBoundingBox](#computeboundingbox)
- [computeBoundingSphere](#computeboundingsphere)
- [dispose](#dispose)

---

### InstancedMesh

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `geometry` | `&nbsp;` | 几何体 (BufferGeometry) |
| `material` | `&nbsp;` | 材质 (Material) |
| `count` | `&nbsp;` | 实例数 |

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

"InstancedMesh"（只读）

---

### count

属性 \ 访问: `r/w`

**说明**

实例数

---

### getMatrixAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `matrix` | `&nbsp;` |  |

**说明**

获取实例的变换矩阵

---

### setMatrixAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `matrix` | `&nbsp;` |  |

**说明**

设置实例的变换矩阵

---

### getColorAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `color` | `&nbsp;` |  |

**说明**

获取实例的颜色

---

### setColorAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |
| `color` | `&nbsp;` |  |

**说明**

设置实例的颜色

---

### computeBoundingBox

方法

**说明**

计算边界框

---

### computeBoundingSphere

方法

**说明**

计算边界球

---

### dispose

方法

**说明**

释放资源

---
