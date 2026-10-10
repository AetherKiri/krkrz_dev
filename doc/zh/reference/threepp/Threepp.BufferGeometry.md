# Threepp.BufferGeometry

缓冲几何体基类

存储顶点数据的几何体的基类。

## 成员列表

### 构造函数

- [BufferGeometry](#buffergeometry)

### 属性

- [type](#type)
- [id](#id)
- [name](#name)

### 方法

- [hasIndex](#hasindex)
- [hasAttribute](#hasattribute)
- [computeBoundingBox](#computeboundingbox)
- [computeBoundingSphere](#computeboundingsphere)
- [computeVertexNormals](#computevertexnormals)
- [normalizeNormals](#normalizenormals)
- [rotateX](#rotatex)
- [rotateY](#rotatey)
- [rotateZ](#rotatez)
- [translate](#translate)
- [scale](#scale)
- [center](#center)
- [dispose](#dispose)

---

### BufferGeometry

构造函数

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

几何体的类型（只读）

---

### id

属性 \ 访问: `r/w`

**说明**

ID（只读）

---

### name

属性 \ 访问: `r/w`

**说明**

名称

---

### hasIndex

方法

**说明**

是否具有索引

---

### hasAttribute

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**说明**

是否具有指定的属性

---

### computeBoundingBox

方法

**说明**

计算包围盒

---

### computeBoundingSphere

方法

**说明**

计算包围球

---

### computeVertexNormals

方法

**说明**

计算顶点法线

---

### normalizeNormals

方法

**说明**

归一化法线

---

### rotateX

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**说明**

绕 X 轴旋转

---

### rotateY

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**说明**

绕 Y 轴旋转

---

### rotateZ

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `angle` | `&nbsp;` |  |

**说明**

绕 Z 轴旋转

---

### translate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

平移

---

### scale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

缩放

---

### center

方法

**说明**

移动到中心

---

### dispose

方法

**说明**

释放资源

---
