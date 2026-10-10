# RichText.Layout

单行文本布局类

保存单行文本的布局计算结果。
通过将布局与绘制分离，可以复用测量结果，以及
绘制已预先布局好的文本。

使用示例:
var tl = new RichText.Layout();
tl.layout("Hello World", style);
Debug.message("宽度: " + tl.width + ", 高度: " + tl.height);
layer.drawTextLayout(tl, 10, 50, appearance);

## 成员列表

### 构造函数

- [Layout](#layout)

### 属性

- [width](#width)
- [height](#height)
- [ascent](#ascent)
- [descent](#descent)
- [charCount](#charcount)

### 方法

- [layout](#layout)
- [clone](#clone)

---

### Layout

构造函数

**说明**

构造函数

---

### width

属性 \ 访问: `r/w`

**说明**

文本宽度（只读）

---

### height

属性 \ 访问: `r/w`

**说明**

文本高度（ascent + descent）（只读）

---

### ascent

属性 \ 访问: `r/w`

**说明**

ascent（从基线到上端，负值）（只读）

---

### descent

属性 \ 访问: `r/w`

**说明**

descent（从基线到下端，正值）（只读）

---

### charCount

属性 \ 访问: `r/w`

**说明**

字符数（只读）

---

### layout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文本 |
| `style` | `&nbsp;` | RichText.Style 对象 |

**说明**

执行文本的布局（测量）

---

### clone

方法

**返回值**

复制后的 Layout 对象

**说明**

复制

---
