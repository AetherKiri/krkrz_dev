# Threepp.Texture

纹理基类

表示图像纹理。
============================================================ Texture 类 ============================================================

## 成员列表

### 构造函数

- [Texture](#texture)

### 属性

- [id](#id)
- [name](#name)
- [mapping](#mapping)
- [wrapS](#wraps)
- [wrapT](#wrapt)
- [magFilter](#magfilter)
- [minFilter](#minfilter)
- [anisotropy](#anisotropy)
- [format](#format)
- [offset](#offset)
- [repeat](#repeat)
- [center](#center)
- [rotation](#rotation)
- [matrixAutoUpdate](#matrixautoupdate)
- [generateMipmaps](#generatemipmaps)
- [premultiplyAlpha](#premultiplyalpha)
- [unpackAlignment](#unpackalignment)
- [encoding](#encoding)

### 方法

- [updateMatrix](#updatematrix)
- [dispose](#dispose)
- [needsUpdate](#needsupdate)
- [version](#version)

---

### Texture

构造函数

**说明**

构造函数

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

### mapping

属性 \ 访问: `r/w`

**说明**

映射类型

---

### wrapS

属性 \ 访问: `r/w`

**说明**

S 方向的环绕

---

### wrapT

属性 \ 访问: `r/w`

**说明**

T 方向的环绕

---

### magFilter

属性 \ 访问: `r/w`

**说明**

放大过滤器

---

### minFilter

属性 \ 访问: `r/w`

**说明**

缩小过滤器

---

### anisotropy

属性 \ 访问: `r/w`

**说明**

各向异性过滤

---

### format

属性 \ 访问: `r/w`

**说明**

格式

---

### offset

属性 \ 访问: `r/w`

**说明**

偏移 (Vector2、只读)

---

### repeat

属性 \ 访问: `r/w`

**说明**

重复 (Vector2、只读)

---

### center

属性 \ 访问: `r/w`

**说明**

中心 (Vector2、只读)

---

### rotation

属性 \ 访问: `r/w`

**说明**

旋转

---

### matrixAutoUpdate

属性 \ 访问: `r/w`

**说明**

矩阵的自动更新

---

### generateMipmaps

属性 \ 访问: `r/w`

**说明**

是否生成 mipmap

---

### premultiplyAlpha

属性 \ 访问: `r/w`

**说明**

Alpha 预乘

---

### unpackAlignment

属性 \ 访问: `r/w`

**说明**

解包对齐

---

### encoding

属性 \ 访问: `r/w`

**说明**

编码

---

### updateMatrix

方法

**说明**

更新矩阵

---

### dispose

方法

**说明**

释放资源

---

### needsUpdate

方法

**说明**

设置更新标志

---

### version

方法

**说明**

获取版本

---
