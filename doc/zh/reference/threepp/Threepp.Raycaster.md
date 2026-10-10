# Threepp.Raycaster

射线投射器

使用射线进行与对象的相交判定。

## 成员列表

### 构造函数

- [Raycaster](#raycaster)

### 属性

- [nearPlane](#nearplane)
- [farPlane](#farplane)

### 方法

- [set](#set)
- [setFromCameraNDC](#setfromcamerandc)
- [setFromCameraPixel](#setfromcamerapixel)
- [intersectObjects](#intersectobjects)

---

### Raycaster

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `origin` | `&nbsp;` | 原点 |
| `direction` | `&nbsp;` | 方向 |
| `near` | `0` | 近裁剪 |
| `far` | `Infinity` | 远裁剪 |

**说明**

构造函数

---

### nearPlane

属性 \ 访问: `r/w`

**说明**

近裁剪

---

### farPlane

属性 \ 访问: `r/w`

**说明**

远裁剪

---

### set

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `origin` | `&nbsp;` |  |
| `direction` | `&nbsp;` |  |

**说明**

设置原点和方向 (direction 假定已归一化)

---

### setFromCameraNDC

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ndcX` | `&nbsp;` | 归一化设备坐标 X [-1,1] (画面左端 -1，右端 +1) |
| `ndcY` | `&nbsp;` | 归一化设备坐标 Y [-1,1] (画面下端 -1，上端 +1) |
| `camera` | `&nbsp;` | PerspectiveCamera 或 OrthographicCamera |

**说明**

根据相机和归一化设备坐标设置射线 (相当于 three.js 的 setFromCamera)

---

### setFromCameraPixel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `px` | `&nbsp;` | 像素 X (左上为原点。吉里吉里图层坐标) |
| `py` | `&nbsp;` | 像素 Y (左上为原点。向下为 +) |
| `viewW` | `&nbsp;` | 视口宽度 (绘制图层的宽度) |
| `viewH` | `&nbsp;` | 视口高度 (绘制图层的高度) |
| `camera` | `&nbsp;` | 相机 |

**说明**

根据像素坐标 (左上为原点) + 视口尺寸设置射线的便捷版

可以直接传入鼠标坐标。内部会将其转换为 NDC。

---

### intersectObjects

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `objects` | `&nbsp;` | 判定对象的 Object3D 数组 (例: [vrm.getScene(), boxMesh]) |
| `recursive` | `true` | 是否递归判定到子孙对象 (省略时为 true) |

**返回值**

命中数组。各元素为字典:
object   … 传入的参数数组中“命中的根对象”(同一实例)。
即使通过 recursive 命中了子孙对象，也返回参数数组中对应的祖先对象。
distance … 到射线原点的距离
x, y, z  … 世界坐标的命中点
数组按距离升序排列 (result[0] 为最靠前)。无命中时 count=0。

**说明**

对对象群进行相交判定，并按距离从近到远的顺序返回命中数组

---
