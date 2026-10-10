# WIN32DialogEX

将 WIN32Dialog 针对吉里吉里做得稍微更易用的类
以 Scripts.execStorage("win32dialog.tjs") 的方式使用。
详情请参考相应源码或示例等。

继承自: [WIN32Dialog](WIN32Dialog.md)

## 成员列表

### 方法

- [store](#store)
- [setInitParams](#setinitparams)
- [open](#open)
- [setCenterPosition](#setcenterposition)
- [loadResource](#loadresource)
- [DefPushButton](#defpushbutton)
- [PushButton](#pushbutton)
- [AutoCheckBox](#autocheckbox)
- [CheckBox](#checkbox)
- [AutoRadioButton](#autoradiobutton)
- [RadioButton](#radiobutton)
- [GroupBox](#groupbox)
- [LText](#ltext)
- [CText](#ctext)
- [RText](#rtext)
- [Icon](#icon)
- [EditText](#edittext)
- [ListBox](#listbox)
- [ComboBox](#combobox)

---

### store

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 模板用字典数组<br>elm = %[ helpID, exStyle, style, x, y, cx, cy, menu, windowClass, title, pointSize, weight, italic, charset, typeFace,<br>items: [ 控件1, 控件2, ... ] ]; |

**说明**

灌入模板

控件会调用用于生成控件的函数。

---

### setInitParams

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 参数字典 |

**说明**

设置项的初始化参数

务必在 store() 之后调用。参数详情请参考 win32dialog.tjs 或 testscript.tjs

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `parent` | `&nbsp;` |  |

**返回值**

%[ result:EndDialog 的 nResult 值, items:项的状态字典 ];

**说明**

显示对话框

注意其返回值与 WIN32Dialog.open 不同

---

### setCenterPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `win` | `parent` | 窗口 ( 省略时针对 open 时的参数窗口 )<br>传入 null 则相对于屏幕居中 |

**说明**

将对话框移动到指定窗口的中央位置

---

### loadResource

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dllfile` | `&nbsp;` | dll 文件 ( 自动进行 Storages.getPlacedPath/getLocalName 处理 ) |
| `resource` | `&nbsp;` | 对话框资源名 |

**说明**

加载对话框资源 ( 重写 )

---

### DefPushButton

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 文本 |
| `id` | `&nbsp;` | 控件 ID |
| `x` | `&nbsp;` | x 坐标 ( 对话框坐标单位 ) |
| `y` | `&nbsp;` | y 坐标 ( 对话框坐标单位 ) |
| `w` | `&nbsp;` | 宽度 ( 对话框坐标单位 ) |
| `h` | `&nbsp;` | 高度 ( 对话框坐标单位 ) |
| `style` | `&nbsp;` | 样式 |
| `ex` | `&nbsp;` | 扩展样式 |

**说明**

用于生成各种控件的函数

---

### PushButton

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### AutoCheckBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### CheckBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### AutoRadioButton

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### RadioButton

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### GroupBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### LText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### CText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### RText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### Icon

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` |  |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### EditText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### ListBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---

### ComboBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |
| `style` | `&nbsp;` |  |
| `ex` | `&nbsp;` |  |

---
