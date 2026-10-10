# ElementsPanel

!!! warning "实验中 ( 不在稳定性保证范围内 )"
    这个 API 的形式尚未固定。**有可能在无预告的情况下被更改或删除**
    ( 即使是非兼容更改，主版本号也不会提升 )。
    关于版本提升方式，请参阅 [版本管理](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)。

    基于 Elements 的 UI 机制形式尚未固定。事件 / 变量相关的 API 可能会与 ElementsDialog 保持一致地更改。

把 Elements 画面绘制到宿主图层上的面板

将 [ElementsDialog](ElementsDialog.md) 相同的画面 JSON 不绘制到覆盖层 ( 始终在最前面 )，
而是**绘制到指定的 [Layer](Layer.md) 的位图**上的类。
z 顺序、转场 ( `[trans]` )、截图 ( piledCopy )、输入的
归属全部遵循吉里吉里的图层机制，因此可用于不让 UI 盖住
正文的 HUD、作为游戏画面一部分的 UI、想搭载到转场上的画面等。

```tjs
var lay = new Layer(win, win.primaryLayer);
lay.setImageSize(400, 300);
lay.setSizeToImageSize();
lay.type = ltAlpha;      // ltAddAlpha なら変換なしでさらに軽い
lay.hitThreshold = 0;    // すべてのマウスメッセージを受ける
lay.visible = true;

var panel = new ElementsPanel(lay);
panel.onAction = function(id, payload) { ... };
panel.showFile("ui/hud.jsonc");

// レイヤの入力をパネルへ流す ( Layer 派生で 1 回書けばよい )
lay.onMouseDown = function(x, y, b, f) { panel.mouseDown(x, y, b, f); };
lay.onMouseUp   = function(x, y, b, f) { panel.mouseUp  (x, y, b, f); };
lay.onMouseMove = function(x, y, f)    { panel.mouseMove(x, y, f); };
```

事件 ( [onAction](#onaction) / [onDrag](#ondrag) / [onVar](#onvar) /
[onClose](#onclose) ) 与变量 store 的 API ( [setVar](#setvar) /
[getVar](#getvar) / [listVars](#listvars) / [watchVars](#watchvars) ) 与
ElementsDialog 同形，因此现有的画面驱动几乎可以原样搭载。

与 ElementsDialog ( 覆盖层 ) 的区别:

- 不影响输入拦截与窗口关闭抑制
- 不会出现在 `Agent.dialogs()` / `closeAllDialogs()` 中
- 不持有模态结果、navigator 流程、虚拟键盘、宿主热键表
  ( 1 个面板 = 1 个画面。画面切换请重新调用 showJson，或
  将图层分成 2 张并交给 `[trans]` )
- 键 / 手柄输入默认不接收。只有想使其有效的画面，
  才从脚本中传入 [keyDown](#keydown) / [keyUp](#keyup) / [text](#text)

主题、显示语言、[ElementsDialog.registerImage](ElementsDialog.md#registerimage)
的运行时图像 store 在整个进程中共享，也会反映到面板上。

## 成员列表

### 构造函数

- [ElementsPanel](#elementspanel)

### 属性

- [active](#active)
- [focused](#focused)
- [watchVars](#watchvars)

### 方法

- [showFile](#showfile)
- [showJson](#showjson)
- [showDict](#showdict)
- [close](#close)
- [notifyResized](#notifyresized)
- [mouseDown](#mousedown)
- [mouseUp](#mouseup)
- [mouseMove](#mousemove)
- [mouseWheel](#mousewheel)
- [mouseLeave](#mouseleave)
- [keyDown](#keydown)
- [keyUp](#keyup)
- [text](#text)
- [setVar](#setvar)
- [getVar](#getvar)
- [listVars](#listvars)
- [invalidate](#invalidate)
- [focus](#focus)
- [activate](#activate)

### 事件

- [onAction](#onaction)
- [onDrag](#ondrag)
- [onVar](#onvar)
- [onClose](#onclose)

---

### ElementsPanel

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 绘制目标的 [Layer](Layer.md)。 |

**说明**

构建 ElementsPanel 对象

指定绘制目标的图层来构建面板。绘制会铺满图层的图像尺寸。

---

### active

属性 \ 访问: `r`

**说明**

是否已打开画面

---

### focused

属性 \ 访问: `r`

**说明**

当前处于焦点的控件 id

没有焦点时为空字符串。

---

### watchVars

属性 \ 访问: `r/w`

**说明**

通过 onVar 接收哪些变量的变化

与 [ElementsDialog.watchVars](ElementsDialog.md#watchvars) 相同。
void (默认) = 仅在实现了 onVar 时接收所有变量 / `"*"` = 所有变量 /
`[]` = 不观测 / `[名前, ...]` = 仅该变量。

---

### showFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 画面 JSON 的统一存储路径。 |

**返回值**

是否成功打开。

**说明**

从文件打开画面 JSON

从文件读取画面 JSON ( 可使用 jsonc )，开始向图层绘制。
画面内的相对素材路径以该 JSON 所在目录为起点解析。

---

### showJson

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `json` | `&nbsp;` | 画面 JSON 字符串。 |

**返回值**

是否成功打开。

**说明**

从字符串打开画面 JSON

---

### showDict

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dict` | `&nbsp;` | 布局的 Dictionary。 |

**返回值**

是否成功打开。

**说明**

打开用 Dictionary 写的布局

打开用 TJS 的 Dictionary / Array 写的布局 (
与 [ElementsDialog.showDict](ElementsDialog.md#showdict) 相同的形式 )。

---

### close

方法

**说明**

关闭面板

销毁画面并停止绘制。图层本身会保留 ( 最后的绘制内容也
不会消失 )，因此需要时请在宿主侧清除。

---

### notifyResized

方法

**说明**

将图层的尺寸更改通知给面板

在更改绘制目标图层的图像尺寸后调用。从下一帧起将以新的
尺寸绘制。

---

### mouseDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 图层 local X 坐标。 |
| `y` | `&nbsp;` | 图层 local Y 坐标。 |
| `button` | `0` | = 0 鼠标按钮 ( 0 = 左 / 1 = 右 / 2 = 中 )。 |
| `shift` | `0` | = 0 Shift 状态的位标志。 |

**说明**

将鼠标按下传递给面板

坐标是图层 local ( Layer.onMouseDown 的参数原样 )。

---

### mouseUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 图层 local X 坐标。 |
| `y` | `&nbsp;` | 图层 local Y 坐标。 |
| `button` | `0` | = 0 鼠标按钮。 |
| `shift` | `0` | = 0 Shift 状态的位标志。 |

**说明**

将鼠标释放传递给面板

---

### mouseMove

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 图层 local X 坐标。 |
| `y` | `&nbsp;` | 图层 local Y 坐标。 |
| `shift` | `0` | = 0 Shift 状态的位标志。 |

**说明**

将鼠标移动传递给面板

---

### mouseWheel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `delta` | `&nbsp;` | 旋转量 ( 120 单位 )。 |
| `x` | `&nbsp;` | 图层 local X 坐标。 |
| `y` | `&nbsp;` | 图层 local Y 坐标。 |
| `shift` | `0` | = 0 Shift 状态的位标志。 |

**说明**

将滚轮旋转传递给面板

---

### mouseLeave

方法

**说明**

将鼠标离开图层的情况传递给面板

---

### keyDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 虚拟键码。 |
| `shift` | `0` | = 0 Shift 状态的位标志。 |

**返回值**

面板是否消费了该输入。

**说明**

将按键按下传递给面板

面板默认不获取键盘焦点，因此只有想使按键有效的
画面才从脚本中传入。

---

### keyUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 虚拟键码。 |
| `shift` | `0` | = 0 Shift 状态的位标志。 |

**返回值**

面板是否消费了该输入。

**说明**

将按键释放传递给面板

---

### text

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 要输入的字符串。 |

**说明**

将文本输入传递给面板

对 input_box 的文本输入 ( 相当于 IME / 粘贴 )。

---

### setVar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变量名。 |
| `value` | `&nbsp;` | 要设置的值 ( 字符串 )。 |

**返回值**

是否成功写入。

**说明**

改写显示中画面的变量

与 [ElementsDialog.setVar](ElementsDialog.md#setvar) 相同。

---

### getVar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变量名。 |

**返回值**

变量的值 ( 字符串 )。未知的变量 / 未打开时为 void。

**说明**

读取显示中画面的变量

与 [ElementsDialog.getVar](ElementsDialog.md#getvar) 相同。

---

### listVars

方法

**返回值**

变量描述 Dictionary 的数组。未打开时为空数组。

**说明**

获取显示中画面的变量列表

与 [ElementsDialog.listVars](ElementsDialog.md#listvars) 相同。

---

### invalidate

方法

**说明**

请求显式重绘

在下一帧重绘整个画面。通常不需要 ( 画面的变化会
自动反映 )。

---

### focus

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 焦点要移到的控件的 id。 |

**返回值**

是否成功发起请求。未打开时为 false。

**说明**

将焦点移到指定 id 的控件

与 [ElementsDialog.focus](ElementsDialog.md#focus) 相同。input_box 会变为
编辑焦点 ( 插入符显示 + 文本受理 )。

---

### activate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 要执行的控件的 id。 |

**返回值**

是否成功执行。id 未知 / 未打开时为 false。

**说明**

执行指定 id 的控件

移动焦点并执行 ( 相当于 Enter )。
与 [ElementsDialog.activate](ElementsDialog.md#activate) 相同。

---

### onAction

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 被操作的控件的 id。 |
| `payload` | `&nbsp;` | 值 ( 按钮点击为 void，状态控件为实际值 )。 |

**说明**

控件操作的通知

与 [ElementsDialog.onAction](ElementsDialog.md#onaction) 相同。

---

### onDrag

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `payload` | `&nbsp;` | 拖拽信息的 Dictionary。 |

**说明**

拖拽通知

与 [ElementsDialog.onDrag](ElementsDialog.md#ondrag) 相同。

---

### onVar

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变量名。 |
| `value` | `&nbsp;` | 新的值 ( 字符串 )。 |

**说明**

变量变化的通知

与 [ElementsDialog.onVar](ElementsDialog.md#onvar) 相同。

---

### onClose

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `action` | `&nbsp;` | 成为关闭契机的 action。 |

**说明**

画面关闭时的通知

与 [ElementsDialog.onClose](ElementsDialog.md#onclose) 相同。

---
