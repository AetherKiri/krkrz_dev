# RichText.Appearance

绘制外观类

相当于 Illustrator 的外观。
通过叠加多个填充（Fill）和描边（Stroke）来实现装饰效果。
先添加的会绘制在下方（里层）。

典型的使用顺序:
1. 阴影（addShadow，或用带偏移的 addFill）
2. 描边（addStroke）
3. 主体的填充（addFill）

## 成员列表

### 构造函数

- [Appearance](#appearance)

### 属性

- [isEmpty](#isempty)
- [count](#count)

### 方法

- [addFill](#addfill)
- [addStroke](#addstroke)
- [addShadow](#addshadow)
- [setColor](#setcolor)
- [addColor](#addcolor)
- [setOutline](#setoutline)
- [addOutline](#addoutline)
- [setShadow](#setshadow)
- [clear](#clear)
- [clone](#clone)

---

### Appearance

构造函数

**说明**

构造函数

---

### isEmpty

属性 \ 访问: `r/w`

**说明**

样式是否为空（只读）

---

### count

属性 \ 访问: `r/w`

**说明**

样式数量（只读）

---

### addFill

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB 色值 (例: 0xFFFFFFFF = 白, 0xFF000000 = 黑) |
| `offsetX` | `0` | X 方向偏移（省略时为 0） |
| `offsetY` | `0` | Y 方向偏移（省略时为 0） |

**说明**

添加填充

使用示例:
app.addFill(0xFFFFFFFF);  // 用白色填充
app.addFill(0x80000000, 2, 2);  // 用半透明黑实现阴影效果

---

### addStroke

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB 色值 |
| `width` | `&nbsp;` | 线宽 |
| `offsetX` | `0` | X 方向偏移（省略时为 0） |
| `offsetY` | `0` | Y 方向偏移（省略时为 0） |

**说明**

添加描边（Stroke）

使用示例:
app.addStroke(0xFF000000, 2);  // 黑色 2px 的描边

---

### addShadow

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 阴影色（ARGB） |
| `offsetX` | `&nbsp;` | X 方向偏移 |
| `offsetY` | `&nbsp;` | Y 方向偏移 |

**说明**

添加阴影

阴影会自动添加到最下层（最里层）。
使用示例:
app.addShadow(0x80000000, 2, 2);  // 半透明黑的阴影

---

### setColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB 色值 |

**说明**

设置文本颜色（替换现有的普通 Fill）

将现有的普通 Fill（偏移为 0,0 的 Fill）替换为指定颜色。
若不存在普通 Fill，则新增一个。
使用示例:
app.setColor(0xFFFF0000);  // 将文本颜色改为红色

---

### addColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB 色值 |
| `offsetX` | `0` | X 方向偏移（省略时为 0） |
| `offsetY` | `0` | Y 方向偏移（省略时为 0） |

**说明**

添加文本颜色（添加到最上层）

与 addFill 相同，但会添加到最上层。

---

### setOutline

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB 色值 |
| `width` | `&nbsp;` | 线宽 |
| `offsetX` | `0` | X 方向偏移（省略时为 0） |
| `offsetY` | `0` | Y 方向偏移（省略时为 0） |

**说明**

设置描边（替换现有的 Stroke）

将现有的 Stroke 替换为指定的 Stroke。
若不存在 Stroke，则新增一个。

---

### addOutline

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | ARGB 色值 |
| `width` | `&nbsp;` | 线宽 |
| `offsetX` | `0` | X 方向偏移（省略时为 0） |
| `offsetY` | `0` | Y 方向偏移（省略时为 0） |

**说明**

添加描边（作为最底层的 Stroke 添加）

---

### setShadow

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `color` | `&nbsp;` | 阴影色（ARGB） |
| `offsetX` | `&nbsp;` | X 方向偏移 |
| `offsetY` | `&nbsp;` | Y 方向偏移 |

**说明**

设置阴影（替换现有的阴影 Fill）

将现有的阴影（带偏移的 Fill）替换为指定的阴影。

---

### clear

方法

**说明**

清除所有样式

---

### clone

方法

**返回值**

复制后的 Appearance 对象

**说明**

复制外观

---
