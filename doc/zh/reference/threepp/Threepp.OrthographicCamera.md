# Threepp.OrthographicCamera

正交相机

适合 2D 场景和等轴测视图的相机。

## 成员列表

### 构造函数

- [OrthographicCamera](#orthographiccamera)

### 属性

- [type](#type)
- [left](#left)
- [right](#right)
- [top](#top)
- [bottom](#bottom)

### 方法

- [setViewOffset](#setviewoffset)
- [clearViewOffset](#clearviewoffset)
- [updateProjectionMatrix](#updateprojectionmatrix)

---

### OrthographicCamera

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `-1` | 左端 |
| `right` | `1` | 右端 |
| `top` | `1` | 上端 |
| `bottom` | `-1` | 下端 |
| `near` | `0.1` | 近裁剪面 |
| `far` | `2000` | 远裁剪面 |

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

"OrthographicCamera"（只读）

---

### left

属性 \ 访问: `r/w`

**说明**

左端

---

### right

属性 \ 访问: `r/w`

**说明**

右端

---

### top

属性 \ 访问: `r/w`

**说明**

上端

---

### bottom

属性 \ 访问: `r/w`

**说明**

下端

---

### setViewOffset

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fullWidth` | `&nbsp;` |  |
| `fullHeight` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

设置视图偏移

---

### clearViewOffset

方法

**说明**

清除视图偏移

---

### updateProjectionMatrix

方法

**说明**

更新投影矩阵

---
