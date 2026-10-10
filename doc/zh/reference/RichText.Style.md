# RichText.Style

文本样式类

定义文本的逻辑样式（字体、大小、字重等）。
绘制外观（颜色、描边等）通过 Appearance 类设置。

## 成员列表

### 构造函数

- [Style](#style)

### 属性

- [fontSize](#fontsize)
- [fontWeight](#fontweight)
- [italic](#italic)
- [letterSpacing](#letterspacing)
- [wordSpacing](#wordspacing)
- [scaleX](#scalex)
- [skewX](#skewx)
- [fontWidth](#fontwidth)
- [bidi](#bidi)

### 方法

- [setFonts](#setfonts)
- [setLocale](#setlocale)
- [clone](#clone)

---

### Style

构造函数

**说明**

构造函数

---

### fontSize

属性 \ 访问: `r/w`

**说明**

字体大小（以像素为单位）

默认值: 16

---

### fontWeight

属性 \ 访问: `r/w`

**说明**

字重（粗细）

100~900 的值。400 = 普通，700 = 粗体
默认值: 400

---

### italic

属性 \ 访问: `r/w`

**说明**

斜体

默认值: false

---

### letterSpacing

属性 \ 访问: `r/w`

**说明**

字符间距（em 单位）

0.1 = 字体大小的 10% 的附加间距
默认值: 0

---

### wordSpacing

属性 \ 访问: `r/w`

**说明**

单词间距（em 单位）

默认值: 0

---

### scaleX

属性 \ 访问: `r/w`

**说明**

水平缩放

1.0 = 正常，0.5 = 一半的宽度
默认值: 1.0

---

### skewX

属性 \ 访问: `r/w`

**说明**

斜体倾斜值

0 = 正常，负值则向右倾斜
默认值: 0

---

### fontWidth

属性 \ 访问: `r/w`

**说明**

字体宽度（可变字体的 wdth 轴，百分比）

100 = 正常宽度。50 = 一半的宽度，200 = 2 倍的宽度。
仅在支持可变字体 wdth 轴的字体上有效。
默认值: 100

---

### bidi

属性 \ 访问: `r/w`

**说明**

双向文本控制

RichText.BIDI_LTR / BIDI_RTL / BIDI_DEFAULT_LTR / BIDI_DEFAULT_RTL
默认值: BIDI_DEFAULT_LTR

---

### setFonts

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `names` | `&nbsp;` | 字体名的数组（按优先级顺序） |

**说明**

字体集合的设置

数组的顺序即为回退优先级。
第一个字体无法绘制的字符会用下一个字体绘制。

数组的每个元素除了可以用 registerFont 指定的注册名之外，
注册名找不到时，还可以用字体文件内的 family 名
（例: "Noto Sans JP"）或 "family Style" 连接名
（例: "Noto Sans JP Bold"）来引用。
使用示例:
style.setFonts(["主字体", "emoji 字体", "回退字体"]);

---

### setLocale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `locale` | `&nbsp;` | 区域设置字符串 |

**说明**

区域设置

会影响避头尾处理等断行规则。
使用示例:
style.setLocale("ja_JP");

---

### clone

方法

**返回值**

复制后的 Style 对象

**说明**

复制样式

---
