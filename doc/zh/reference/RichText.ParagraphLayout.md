# RichText.ParagraphLayout

段落（多行）文本布局类

保存多行文本的布局计算结果。
通过将布局与绘制分离，可以复用测量结果，以及
用于逐字显示（指定 maxChars）。

使用示例:
var pl = new RichText.ParagraphLayout();
pl.layout("较长的文本...", 300, style);
Debug.message("行数: " + pl.lineCount);
layer.drawParagraphLayout(pl, 10, 10, 300, 200,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP, style, app);

## 成员列表

### 构造函数

- [ParagraphLayout](#paragraphlayout)

### 属性

- [lineCount](#linecount)
- [totalHeight](#totalheight)
- [maxWidth](#maxwidth)
- [totalCharCount](#totalcharcount)
- [lineSpacing](#linespacing)
- [breakStrategy](#breakstrategy)

### 方法

- [layout](#layout)
- [getLineInfo](#getlineinfo)
- [clone](#clone)

---

### ParagraphLayout

构造函数

**说明**

构造函数

---

### lineCount

属性 \ 访问: `r/w`

**说明**

行数（只读）

---

### totalHeight

属性 \ 访问: `r/w`

**说明**

所有行的高度总和（只读）

---

### maxWidth

属性 \ 访问: `r/w`

**说明**

最大行宽（只读）

---

### totalCharCount

属性 \ 访问: `r/w`

**说明**

所有行的字符数总和（只读）

---

### lineSpacing

属性 \ 访问: `r/w`

**说明**

行距

默认值: 0

---

### breakStrategy

属性 \ 访问: `r/w`

**说明**

断行策略

RichText.BREAK_GREEDY / BREAK_HIGH_QUALITY / BREAK_BALANCED
默认值: BREAK_HIGH_QUALITY

---

### layout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文本 |
| `maxWidth` | `&nbsp;` | 最大宽度 |
| `style` | `&nbsp;` | RichText.Style 对象 |

**说明**

执行段落的布局（测量）

---

### getLineInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` | 行索引（0~lineCount-1） |

**返回值**

行信息的字典 %[startIndex, endIndex, width, height]

**说明**

获取行信息

---

### clone

方法

**返回值**

复制后的 ParagraphLayout 对象

**说明**

复制

---
