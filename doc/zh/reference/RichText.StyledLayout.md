# RichText.StyledLayout

带样式标签的文本布局类

保存带样式标签的文本的布局计算结果。
通过将布局与绘制分离，可以高效地实现同一文本的重绘以及
字符送进动画。

使用示例:
var sl = new RichText.StyledLayout();
sl.layout(
"<style:bold>粗体</style>与普通文本",
400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
%[ "default": normalStyle, "bold": boldStyle ],
%[ "default": normalApp, "bold": boldApp ]
);
layer.drawStyledLayout(sl, 10, 10);

## 成员列表

### 构造函数

- [StyledLayout](#styledlayout)

### 属性

- [lineCount](#linecount)
- [totalCharCount](#totalcharcount)
- [maxWidth](#maxwidth)
- [maxHeight](#maxheight)
- [isValid](#isvalid)
- [totalRenderDelay](#totalrenderdelay)

### 方法

- [layout](#layout)
- [resolveAllTimings](#resolvealltimings)
- [calcShowCount](#calcshowcount)
- [getKeyWaits](#getkeywaits)
- [getResolvedTimings](#getresolvedtimings)

---

### StyledLayout

构造函数

**说明**

构造函数

---

### lineCount

属性 \ 访问: `r/w`

**说明**

行数（只读）

---

### totalCharCount

属性 \ 访问: `r/w`

**说明**

总字符数（只读）

用作字符送进动画的上限值

---

### maxWidth

属性 \ 访问: `r/w`

**说明**

布局的最大宽度（只读）

---

### maxHeight

属性 \ 访问: `r/w`

**说明**

布局的最大高度（只读）

---

### isValid

属性 \ 访问: `r/w`

**说明**

布局是否有效（只读）

调用 layout() 后变为 true

---

### totalRenderDelay

属性 \ 访问: `r/w`

**说明**

整体的最大显示延迟时间（ms）（只读）

是全部字符显示完成所需的时间。
用作字符送进动画的计时器上限。

---

### layout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 带样式标签的文本 |
| `maxWidth` | `&nbsp;` | 最大宽度 |
| `maxHeight` | `&nbsp;` | 最大高度 |
| `hAlign` | `&nbsp;` | 水平对齐 (RichText.HALIGN_LEFT/CENTER/RIGHT) |
| `vAlign` | `&nbsp;` | 垂直对齐 (RichText.VALIGN_TOP/MIDDLE/BOTTOM) |
| `styles` | `&nbsp;` | 单个 Style，或样式名 → Style 的字典 |
| `appearances` | `&nbsp;` | 单个 Appearance，或样式名 → Appearance 的字典 |
| `lineSpacing` | `0` | 行距（省略时为 0） |

**说明**

计算文本的布局

向 styles / appearances 传入单个对象时，会被当作 "default" 键处理。

使用示例:
// 单个样式
sl.layout(text, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
style, appearance);

// 多个样式
sl.layout(text, 400, 300,
RichText.HALIGN_LEFT, RichText.VALIGN_TOP,
%[ "default": normalStyle, "bold": boldStyle ],
%[ "default": normalApp, "bold": boldApp ]);

---

### resolveAllTimings

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `timeScale` | `1.0` | 时间缩放系数（省略时为 1.0） |
| `widthTimeScale` | `false` | 是否进行按字符宽度的时间补偿（省略时为 false） |

**说明**

解析时机信息

解析由 layout() 生成的时机信息（<start>, <delay>, <wait>, <sync>, <keywait> 标签），
并计算各字符的显示开始时间。

即使不显式调用，在首次访问 getResolvedTimings / getKeyWaits / totalRenderDelay /
calcShowCount 时，也会使用默认值（timeScale=1.0, widthTimeScale=false）
自动进行解析。

使用示例:
sl.resolveAllTimings(1.0, false);
// 倍速显示
sl.resolveAllTimings(0.5, false);

---

### calcShowCount

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `time` | `&nbsp;` | 经过时间（ms） |

**返回值**

应显示的字符数

**说明**

计算在指定时间之前应显示的字符数

将其传给 drawStyledLayout 的 maxChars 参数，
即可实现基于时间的字符送进动画。

使用示例:
var count = sl.calcShowCount(elapsed);
layer.drawStyledLayout(sl, x, y, count);

---

### getKeyWaits

方法

**返回值**

按键等待信息的数组

**说明**

获取按键等待信息

每个元素都是字典 %[pos, time]。
- pos: 字符位置（charIndex）
- time: 该时间点的经过时间（ms）

返回 <keywait/> 标签的位置，以及到该处为止的累计显示时间。

---

### getResolvedTimings

方法

**返回值**

时机信息的数组

**说明**

获取已解析的时机信息

每个元素都是字典 %[charIndex, delay]。
- charIndex: 字符位置
- delay: 显示开始时间（ms）

这是各字符在何时显示的详细信息。

---
