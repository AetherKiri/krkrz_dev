# Threepp.Object3D

3D 对象的基类

是场景图中所有 3D 对象的基类。
============================================================ Core 类 ============================================================

## 成员列表

### 构造函数

- [Object3D](#object3d)

### 属性

- [type](#type)
- [id](#id)
- [name](#name)
- [visible](#visible)
- [castShadow](#castshadow)
- [receiveShadow](#receiveshadow)
- [frustumCulled](#frustumculled)
- [renderOrder](#renderorder)
- [position](#position)
- [rotation](#rotation)
- [quaternion](#quaternion)
- [scale](#scale)
- [up](#up)

### 方法

- [setPosition](#setposition)
- [setRotation](#setrotation)
- [setScale](#setscale)
- [add](#add)
- [remove](#remove)
- [removeFromParent](#removefromparent)
- [clear](#clear)
- [lookAt](#lookat)
- [rotateX](#rotatex)
- [rotateY](#rotatey)
- [rotateZ](#rotatez)
- [rotateOnAxis](#rotateonaxis)
- [rotateOnWorldAxis](#rotateonworldaxis)
- [translateX](#translatex)
- [translateY](#translatey)
- [translateZ](#translatez)
- [translateOnAxis](#translateonaxis)
- [updateMatrix](#updatematrix)
- [updateMatrixWorld](#updatematrixworld)
- [treeJson](#treejson)
- [getWorldPosition](#getworldposition)
- [getWorldQuaternion](#getworldquaternion)
- [getWorldScale](#getworldscale)

---

### Object3D

构造函数

**说明**

构造函数

---

### type

属性 \ 访问: `r/w`

**说明**

对象的类型（只读）

---

### id

属性 \ 访问: `r/w`

**说明**

对象 ID（只读）

---

### name

属性 \ 访问: `r/w`

**说明**

对象名称

---

### visible

属性 \ 访问: `r/w`

**说明**

显示/隐藏

---

### castShadow

属性 \ 访问: `r/w`

**说明**

是否投射阴影

---

### receiveShadow

属性 \ 访问: `r/w`

**说明**

是否接收阴影

---

### frustumCulled

属性 \ 访问: `r/w`

**说明**

是否执行视锥体剔除

---

### renderOrder

属性 \ 访问: `r/w`

**说明**

绘制顺序

---

### position

属性 \ 访问: `r/w`

**说明**

注意：position/rotation/scale/quaternion 的 getter 返回的是“值的副本”，因此即使写 obj.position.set(...) 或 obj.position.x = ...，也不会反映到对象本身。要更改位置、旋转、缩放，请使用下面的 setPosition/setRotation/setScale。

---

### rotation

属性 \ 访问: `r/w`

**说明**

旋转 (Euler，值为副本 = 实质只读)

---

### quaternion

属性 \ 访问: `r/w`

**说明**

旋转 (Quaternion，值为副本 = 实质只读)

---

### scale

属性 \ 访问: `r/w`

**说明**

缩放 (Vector3，值为副本 = 实质只读)

---

### up

属性 \ 访问: `r/w`

**说明**

上方向向量 (Vector3，值为副本)

---

### setPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

设置位置 (使用此方法代替 position.set)

---

### setRotation

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

设置旋转 (欧拉角，弧度)

---

### setScale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `z` | `&nbsp;` |  |

**说明**

设置缩放

---

### add

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 要添加的 Object3D |

**说明**

添加子对象

---

### remove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `object` | `&nbsp;` | 要删除的 Object3D |

**说明**

删除子对象

---

### removeFromParent

方法

**说明**

从父级中删除自身

---

### clear

方法

**说明**

删除所有子对象

---

### lookAt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X 坐标 |
| `y` | `&nbsp;` | Y 坐标 |
| `z` | `&nbsp;` | Z 坐标 |

**说明**

朝向指定的点

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

### rotateOnAxis

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**说明**

绕任意轴旋转（局部）

---

### rotateOnWorldAxis

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `angle` | `&nbsp;` |  |

**说明**

绕任意轴旋转（世界坐标）

---

### translateX

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**说明**

沿 X 轴平移

---

### translateY

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**说明**

沿 Y 轴平移

---

### translateZ

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `distance` | `&nbsp;` |  |

**说明**

沿 Z 轴平移

---

### translateOnAxis

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `axis` | `&nbsp;` |  |
| `distance` | `&nbsp;` |  |

**说明**

沿任意轴平移

---

### updateMatrix

方法

**说明**

更新局部矩阵

---

### updateMatrixWorld

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `force` | `&nbsp;` |  |

**说明**

更新世界矩阵

---

### treeJson

方法

**返回值**

JSON 字符串

**说明**

将子树以 JSON 字符串一次性转储 (用于外部检查器的场景树显示)。

1 个节点 = {id,name,type,visible,pos:[x,y,z],children:[…]}

---

### getWorldPosition

方法

**说明**

--- 世界变换的获取 (根据 matrixWorld 算出) --- 为使返回值保持最新，需要在之前先执行 render，或调用 updateMatrixWorld(true) (需要沿父级回溯以确定 world 矩阵)。用于在立绘取景中获取骨骼 (head/hips 等) 的 world 坐标。

---

### getWorldQuaternion

方法

**说明**

-> Quaternion (世界旋转)

---

### getWorldScale

方法

**说明**

-> Vector3 (世界缩放)

---
