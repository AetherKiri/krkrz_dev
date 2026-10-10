# Threepp.Euler

欧拉角类

表示旋转的欧拉角。

## 成员列表

### 构造函数

- [Euler](#euler)

### 属性

- [x](#x)
- [y](#y)
- [z](#z)

### 方法

- [getOrder](#getorder)
- [setOrder](#setorder)
- [set](#set)
- [copy](#copy)
- [setFromRotationMatrix](#setfromrotationmatrix)
- [setFromQuaternion](#setfromquaternion)
- [setFromVector3](#setfromvector3)
- [equals](#equals)

---

### Euler

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `0` | X 轴旋转（弧度） |
| `y` | `0` | Y 轴旋转（弧度） |
| `z` | `0` | Z 轴旋转（弧度） |

**说明**

构造函数

---

### x

属性 \ 访问: `r/w`

**说明**

X 轴旋转（只读）

---

### y

属性 \ 访问: `r/w`

**说明**

Y 轴旋转（只读）

---

### z

属性 \ 访问: `r/w`

**说明**

Z 轴旋转（只读）

---

### getOrder

方法

**说明**

获取旋转顺序

---

### setOrder

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `order` | `&nbsp;` |  |

**说明**

设置旋转顺序

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

设置值

---

### copy

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**说明**

复制

---

### setFromRotationMatrix

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `m` | `&nbsp;` |  |

**说明**

从旋转矩阵设置

---

### setFromQuaternion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `q` | `&nbsp;` |  |

**说明**

从四元数设置

---

### setFromVector3

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `v` | `&nbsp;` |  |

**说明**

从 Vector3 设置

---

### equals

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `euler` | `&nbsp;` |  |

**说明**

相等判定

---
