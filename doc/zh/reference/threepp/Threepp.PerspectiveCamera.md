# Threepp.PerspectiveCamera

透视投影相机

是进行类似人眼透视投影的相机。

## 成员列表

### 构造函数

- [PerspectiveCamera](#perspectivecamera)

### 属性

- [type](#type)
- [fov](#fov)
- [aspect](#aspect)
- [focus](#focus)
- [filmGauge](#filmgauge)
- [filmOffset](#filmoffset)

### 方法

- [setFocalLength](#setfocallength)
- [getFocalLength](#getfocallength)
- [getEffectiveFOV](#geteffectivefov)
- [getFilmWidth](#getfilmwidth)
- [getFilmHeight](#getfilmheight)
- [setViewOffset](#setviewoffset)
- [clearViewOffset](#clearviewoffset)
- [updateProjectionMatrix](#updateprojectionmatrix)

---

### PerspectiveCamera

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fov` | `60` | 视场角（度） |
| `aspect` | `1` | 宽高比 |
| `near` | `0.1` | 近裁剪面 |
| `far` | `2000` | 远裁剪面 |

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

"PerspectiveCamera"（只读）

---

### fov

属性 \ 访问: `r/w`

**说明**

视场角（度）

---

### aspect

属性 \ 访问: `r/w`

**说明**

宽高比

---

### focus

属性 \ 访问: `r/w`

**说明**

对焦距离

---

### filmGauge

属性 \ 访问: `r/w`

**说明**

胶片规格（mm）

---

### filmOffset

属性 \ 访问: `r/w`

**说明**

胶片偏移

---

### setFocalLength

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `focalLength` | `&nbsp;` |  |

**说明**

设置焦距

---

### getFocalLength

方法

**说明**

获取焦距

---

### getEffectiveFOV

方法

**说明**

获取有效视场角

---

### getFilmWidth

方法

**说明**

获取胶片宽度

---

### getFilmHeight

方法

**说明**

获取胶片高度

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
