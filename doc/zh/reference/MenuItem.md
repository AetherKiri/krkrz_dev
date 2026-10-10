# MenuItem

此类由多个插件扩展。

## 插件扩展: menu

### 成员列表

#### 构造函数

- [MenuItem](#menuitem)

#### 属性

- [HMENU](#hmenu)
- [caption](#caption)
- [checked](#checked)
- [children](#children)
- [enabled](#enabled)
- [group](#group)
- [index](#index)
- [parent](#parent)
- [radio](#radio)
- [root](#root)
- [shortcut](#shortcut)
- [visible](#visible)
- [window](#window)

#### 方法

- [add](#add)
- [insert](#insert)
- [popup](#popup)
- [remove](#remove)
- [onClick](#onclick)

---

### MenuItem

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `window` | `Window` | `&nbsp;` | 指定创建此菜单项的窗口。 |
| `caption` | `string` | `""` | 指定菜单项的标题 (要显示的字符串)。<br>可通过 MenuItem.caption 属性设置/获取。 |

**说明**

MenuItem 对象的构造

构造 MenuItem 类的对象。
要将创建的菜单项添加到父菜单项，请使用父菜单项的 MenuItem.add 方法。

---

### HMENU

属性 \ 访问: `r`

**说明**

HMENU 菜单项句柄

表示 Windows API 中 HMENU 类型的菜单项句柄。
此属性用于插件等需要直接访问菜单项的情况。
从 TJS2 访问没有意义。
这里得到的是整数，但在插件等中使用此数值时，请强制转换为 HMENU 类型后使用。

---

### caption

属性 \ 访问: `r/w`

**说明**

标题

表示标题 ( 要显示的字符串 )。也可以设置值。
指定 '-' ( 连字符 ) 后会显示分隔线。

---

### checked

属性 \ 访问: `r/w`

**说明**

是否显示勾选标记

表示是否在菜单项旁显示勾选标记。也可以设置值。
指定为真时会显示勾选标记。
MenuItem.radio 属性为真时，显示的就不是勾选标记，而是黑色圆点。
在 MenuItem.group 中拥有相同组号、且拥有相同父项、此外 MenuItem.radio 属性为真的菜单项，不能将本属性同时有两个以上设为真。当其他菜单项的本属性变为真时，如果存在其他已为真的菜单项，则会自动将该菜单项的本属性设置为假。

---

### children

属性 \ 访问: `r`

**说明**

子菜单项

表示列出了子菜单项的数组对象。
向这里得到的数组写入值、或删除、添加项目等，都不会反映到实际的菜单项状态。请认为它只能读取。

---

### enabled

属性 \ 访问: `r/w`

**说明**

是否可选择

表示菜单项是否可选择。也可以设置值。
为真时菜单项可选择，为假时不可选择。

---

### group

属性 \ 访问: `r/w`

**说明**

组号

表示组号。也可以设置值。
拥有相同组号、且拥有相同父项、MenuItem.radio 属性为真的菜单项，不能将 MenuItem.checked 属性同时有两个以上设为真。

---

### index

属性 \ 访问: `r/w`

**说明**

顺序

表示拥有相同父项的菜单项之间的顺序，为 0 或正整数。
0 表示最前面。
在获取当前位置或更改位置时很方便。
设置值后，菜单项会移动到该位置。

---

### parent

属性 \ 访问: `r`

**说明**

父菜单项

表示父菜单项。

---

### radio

属性 \ 访问: `r/w`

**说明**

是否为单选项

指定是否为单选项。也可以设置值。
关于此项为真时的行为，请参照 MenuItem.checked 属性。

---

### root

属性 \ 访问: `r`

**说明**

根菜单项

表示根 (最顶层) 的菜单项 (MenuItem 类的实例)。

---

### shortcut

属性 \ 访问: `r/w`

**说明**

快捷键

表示快捷键。也可以设置值。
快捷键以字符串指定。以“修饰键+目标键名”的组合指定。不区分大小写。以下是有效快捷键的示例。

"Shift+Esc"
"Ctrl+S"
"Shift+Alt+E"
"Alt+Enter"
"Ctrl+F1"
"T" (也可以不指定修饰键)

指定无效的快捷键组合或 "" (空字符串) 时，快捷键将失效。
在当前版本中，指定 Tab 或 Shift+F1 等系统或吉里吉里预先确定了用途的部分键，以及部分键 (如 Shift 键本身等) 也不会响应。
指定快捷键后，与该键对应的 onKeyDown 等事件将不再发生，事件只会发生在指定了快捷键的菜单项上。

---

### visible

属性 \ 访问: `r/w`

**说明**

是否可见

表示菜单项是否可见。也可以设置值。
为真则显示，为假则隐藏。

---

### window

属性 \ 访问: `r`

**说明**

所有者窗口

表示拥有此菜单项的所有者窗口 (Window 类的对象)。

---

### add

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | `MenuItem` | `&nbsp;` | 指定要添加的子菜单项。<br>子菜单项会被添加到已经是子项的菜单项的最后。 |

**说明**

添加子菜单项

添加子菜单项。
菜单项成为其他菜单项的子项后，当父菜单项被禁用时，子菜单项也会自动被禁用。
此外，在菜单层级中也会拥有父子关系。

---

### insert

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | `MenuItem` | `&nbsp;` | 指定要插入的子菜单项。 |
| `index` | `int` | `&nbsp;` | 指定插入位置。指定 0 时插入到最前面。 |

**说明**

插入子菜单项

将子菜单项插入到指定位置。

---

### popup

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `flags` | `int` | `&nbsp;` | 表示菜单行为的标志。请指定以下值的按位逻辑或。<br>tpmLeftButton<br>tpmRightButton<br>tpmLeftAlign<br>tpmCenterAlign<br>tpmRightAlign<br>tpmTopAlign<br>tpmVCenterAlign<br>tpmBottomAlign<br>tpmHorizontal<br>tpmVertical<br>tpmNoNotify<br>tpmReturnCmd<br>tpmRecurse<br>tpmHorPosAnimation<br>tpmHorNegAnimation<br>tpmVerPosAnimation<br>tpmVerNegAnimation<br>tpmNoAnimation<br>关于这些标志的详细信息，请参照 MSDN 的相应页面。 |
| `x` | `int` | `&nbsp;` | 表示窗口客户区坐标上的 x 位置。 |
| `y` | `int` | `&nbsp;` | 表示窗口客户区坐标上的 y 位置。 |

**返回值**

当 flags 中指定了 tpmReturnCmd 时，以整数返回所选菜单项的 ID (不过，在当前版本中无法从吉里吉里侧设置此 ID，因此在 flags 中指定 tpmReturnCmd 没有意义)。
未选择任何项而取消时返回 0。

**说明**

弹出显示菜单项

弹出显示菜单项。此方法在菜单关闭之前不会返回。
请注意，在菜单关闭之前可能会发生其他异步事件。
Window.menu 本身不能弹出。
隐藏状态的菜单项不能弹出。
不是 Window.menu 的子项的菜单不能弹出。

---

### remove

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | `MenuItem` | `&nbsp;` | 指定要删除的子菜单项。 |

**说明**

删除子菜单项

从列表中删除指定的子菜单项。

---

### onClick

方法

**说明**

菜单项被选择时

在菜单项被选择 ( 被单击或按下 Enter 键 ) 时发生。

---

## 插件扩展: windowEx

MenuItem 扩展

### 成员列表

#### 属性

- [rightJustify](#rightjustify)
- [bmpChecked](#bmpchecked)
- [bmpUnchecked](#bmpunchecked)

#### 方法

- [popupEx](#popupex)

#### 常量

- [biSystem](#bisystem)
- [biRestore](#birestore)
- [biMinimize](#biminimize)
- [biClose](#biclose)
- [biCloseDisabled](#biclosedisabled)
- [biMinimizeDisabled](#biminimizedisabled)
- [biPopupClose](#bipopupclose)
- [biPopupRestore](#bipopuprestore)
- [biPopupMaximize](#bipopupmaximize)
- [biPopupMinimize](#bipopupminimize)

---

### rightJustify

属性 \ 访问: `r/w`

**说明**

菜单栏的右端分隔显示

为 true 时，该项及其之后的项目会被靠到右端
※ 必须位于 Window.menu 直下且为 visible，否则无法正确工作

---

### bmpChecked

属性 \ 访问: `r/w`

**说明**

图标的显示

设置内容为使用 MenuItem.bi* 常量，或传入图层对象
※ 注意，在设置值时，它必须是 Window.menu 的子项且为 visible，否则不会生效
另外，请注意，下拉菜单如果不通过 Window.registerExEvent() 注册扩展事件就不会显示
property bmpItem      { getter; setter }; //< 字符串位置图标（勾选／未勾选图标不能同时指定？） 勾选时图标 (0 为默认)

---

### bmpUnchecked

属性 \ 访问: `r/w`

**说明**

未勾选时图标 (0 为默认)

---

### popupEx

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `flags` | `&nbsp;` |  |
| `x` | `cursorX` |  |
| `y` | `cursorY` |  |
| `hwnd` | `this.root.window` | 所有者窗口（省略时为实例所属窗口） |
| `rect` | `&nbsp;` | 禁止重叠的范围（%[ x, y, w, h ]，省略时无禁止范围） |
| `menulist` | `this.children` | 菜单列表数组（不必是 MenuItem 的实例，也可以排列字典） |

**返回值**

被选择的对象

**说明**

弹出显示

与 MenuItem.popup 不同，不必属于窗口菜单，而且列表也可以传入字典的数组等
请注意，通过此函数的弹出显示不会使用 bmp* 属性显示图标

---

### biSystem

常量

**说明**

HBMMENU_SYSTEM

---

### biRestore

常量

**说明**

HBMMENU_MBAR_RESTORE

---

### biMinimize

常量

**说明**

HBMMENU_MBAR_MINIMIZE

---

### biClose

常量

**说明**

HBMMENU_MBAR_CLOSE

---

### biCloseDisabled

常量

**说明**

HBMMENU_MBAR_CLOSE_D

---

### biMinimizeDisabled

常量

**说明**

HBMMENU_MBAR_MINIMIZE_D

---

### biPopupClose

常量

**说明**

HBMMENU_POPUP_CLOSE

---

### biPopupRestore

常量

**说明**

HBMMENU_POPUP_RESTORE

---

### biPopupMaximize

常量

**说明**

HBMMENU_POPUP_MAXIMIZE

---

### biPopupMinimize

常量

**说明**

HBMMENU_POPUP_MINIMIZE

---
