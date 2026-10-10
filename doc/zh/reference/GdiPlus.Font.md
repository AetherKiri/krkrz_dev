# GdiPlus.Font

该类由多个插件扩展。

## 插件扩展: layerExDraw

字体信息

### 成员列表

#### 构造函数

- [Font](#font)

#### 属性

- [familyName](#familyname)
- [emSize](#emsize)
- [style](#style)
- [forceSelfPathDraw](#forceselfpathdraw)
- [ascent](#ascent)
- [descent](#descent)
- [lineSpacing](#linespacing)
- [ascentLeading](#ascentleading)
- [descentLeading](#descentleading)

---

### Font

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `familyName` | `&nbsp;` | 字体家族 |
| `emSize` | `&nbsp;` | 字体大小 |
| `style` | `&nbsp;` | 字体样式 |

**说明**

构造函数

---

### familyName

属性 \ 访问: `r/w`

**说明**

字体家族

---

### emSize

属性 \ 访问: `r/w`

**说明**

字体大小

---

### style

属性 \ 访问: `r/w`

**说明**

字体样式

---

### forceSelfPathDraw

属性 \ 访问: `r/w`

**说明**

设置是否不使用 GDI+ 的字体绘制机制，而是自行获取路径来进行字体绘制。

---

### ascent

属性 \ 访问: `r`

**说明**

ascent (只读)

---

### descent

属性 \ 访问: `r`

**说明**

descent (只读)

---

### lineSpacing

属性 \ 访问: `r`

**说明**

行距长度 (只读)。

---

### ascentLeading

属性 \ 访问: `r`

**说明**

ascent 侧的 internalLeading (只读)

---

### descentLeading

属性 \ 访问: `r`

**说明**

descent 侧的 internalLeading (只读)

---

## 插件扩展: layerExVector

字体信息

保存用于使用通过 loadFont() 注册的字体来绘制文本的设置

### 成员列表

#### 构造函数

- [Font](#font)

#### 属性

- [fontFamily](#fontfamily)
- [fontSize](#fontsize)
- [italic](#italic)
- [letterSpacing](#letterspacing)
- [lineSpacing](#linespacing)

---

### Font

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fontFamily` | `&nbsp;` | 字体家族名（通过 loadFont() 注册的名称） |
| `fontSize` | `&nbsp;` | 字体大小 |

**说明**

构造函数

---

### fontFamily

属性 \ 访问: `r/w`

**说明**

字体家族名（通过 loadFont() 注册的名称）

---

### fontSize

属性 \ 访问: `r/w`

**说明**

字体大小

---

### italic

属性 \ 访问: `r/w`

**说明**

斜体倾斜 (0=无，0.18=标准)

---

### letterSpacing

属性 \ 访问: `r/w`

**说明**

字符间距缩放 (1.0=标准，值越大越宽)

---

### lineSpacing

属性 \ 访问: `r/w`

**说明**

行间距缩放 (1.0=标准，值越大越宽)

---
