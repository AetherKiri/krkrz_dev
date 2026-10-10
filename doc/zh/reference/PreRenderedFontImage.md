# PreRenderedFontImage

字体图像（※此类实际上并不存在！）

定义要附加到通过 callback 返回的图层对象上的附加信息。
请对普通的图层对象赋值后再传入。
图层的图像只参照 (0,0)-(blackbox_x-1,blackbox_y-1) 区域的 Alpha 信息，并被重采样为 65 个等级（0~64）。

即使将同一个实例作为 callback 的返回值反复使用也没有问题。

继承自: [Layer](Layer.md)

## 成员列表

### 属性

- [blackbox_x](#blackbox_x)
- [blackbox_y](#blackbox_y)
- [origin_x](#origin_x)
- [origin_y](#origin_y)
- [inc_x](#inc_x)
- [inc_y](#inc_y)
- [inc](#inc)

---

### blackbox_x

属性 \ 访问: `r/w`

**说明**

GLYPHMETRICS.gmBlackBoxX

---

### blackbox_y

属性 \ 访问: `r/w`

**说明**

GLYPHMETRICS.gmBlackBoxY

---

### origin_x

属性 \ 访问: `r/w`

**说明**

GLYPHMETRICS.gmptGlyphOrigin.x

---

### origin_y

属性 \ 访问: `r/w`

**说明**

GLYPHMETRICS.gmptGlyphOrigin.y

---

### inc_x

属性 \ 访问: `r/w`

**说明**

GLYPHMETRICS.gmCellIncX

---

### inc_y

属性 \ 访问: `r/w`

**说明**

GLYPHMETRICS.gmCellIncY

---

### inc

属性 \ 访问: `r/w`

**说明**

GetTextExtentPoint32 返回的尺寸的 SIZE.cx

---
