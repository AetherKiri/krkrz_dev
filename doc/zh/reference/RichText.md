# RichText

基于伪代码的手册

richtext - 吉里吉里用富文本渲染插件

通过 minikin (Android 文本布局引擎) 进行排版，并由吉里吉里Z 引擎本体的
统一字体引擎 (glyphware) 进行字形绘制，从而提供高质量的文本
渲染。由于字体的实体、字形的光栅化与引擎本体共享，
因此外观与 Layer.drawText 及 Elements 对话框保持一致。

特点:
- 支持多字体回退
- 支持多语言（含 RTL）
- 支持 emoji
- 通过类 HTML 标签指定样式
- 描边、阴影等装饰效果
- 段落布局（自动换行）
- 支持逐字显示（使用 ParagraphLayout / StyledLayout）

## 成员列表

### 方法

- [registerFont](#registerfont)
- [registerVariableFont](#registervariablefont)
- [unregisterFont](#unregisterfont)
- [registerCollection](#registercollection)
- [unregisterCollection](#unregistercollection)
- [registerLocale](#registerlocale)

### 常量

- [HALIGN_LEFT](#halign_left)
- [HALIGN_CENTER](#halign_center)
- [HALIGN_RIGHT](#halign_right)
- [HALIGN_JUSTIFY](#halign_justify)
- [VALIGN_TOP](#valign_top)
- [VALIGN_MIDDLE](#valign_middle)
- [VALIGN_BOTTOM](#valign_bottom)
- [BREAK_GREEDY](#break_greedy)
- [BREAK_HIGH_QUALITY](#break_high_quality)
- [BREAK_BALANCED](#break_balanced)
- [BIDI_LTR](#bidi_ltr)
- [BIDI_RTL](#bidi_rtl)
- [BIDI_DEFAULT_LTR](#bidi_default_ltr)
- [BIDI_DEFAULT_RTL](#bidi_default_rtl)

---

### registerFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `index` | `0` |  |

---

### registerVariableFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `&nbsp;` |  |
| `weight` | `&nbsp;` |  |
| `italic` | `false` |  |
| `index` | `0` |  |

---

### unregisterFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### registerCollection

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `collectionName` | `&nbsp;` |  |
| `fontNames` | `&nbsp;` |  |

---

### unregisterCollection

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `collectionName` | `&nbsp;` |  |

---

### registerLocale

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `locale` | `&nbsp;` |  |

---

### HALIGN_LEFT

常量

值: `0`

---

### HALIGN_CENTER

常量

值: `1`

**说明**

左对齐

---

### HALIGN_RIGHT

常量

值: `2`

**说明**

居中对齐

---

### HALIGN_JUSTIFY

常量

值: `3`

**说明**

右对齐

---

### VALIGN_TOP

常量

值: `0`

---

### VALIGN_MIDDLE

常量

值: `1`

**说明**

上对齐

---

### VALIGN_BOTTOM

常量

值: `2`

**说明**

居中对齐

---

### BREAK_GREEDY

常量

值: `0`

---

### BREAK_HIGH_QUALITY

常量

值: `1`

**说明**

高速（对每个换行候选立即判断）

---

### BREAK_BALANCED

常量

值: `2`

**说明**

高品质（Knuth-Plass 算法）

---

### BIDI_LTR

常量

值: `0`

---

### BIDI_RTL

常量

值: `1`

**说明**

从左到右

---

### BIDI_DEFAULT_LTR

常量

值: `2`

**说明**

从右到左

---

### BIDI_DEFAULT_RTL

常量

值: `3`

**说明**

默认从左到右

---
