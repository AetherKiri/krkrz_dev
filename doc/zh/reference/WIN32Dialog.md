# WIN32Dialog

基于伪代码的手册

用于操作 Windows 原生对话框的类。
它只具备相当于 API 包装器程度的功能，因此非常难用，
但使用后述的用 TJS 记述的 WIN32DialogEX 就能轻松许多。

## 成员列表

### 构造函数

- [WIN32Dialog](#win32dialog)

### 属性

- [left](#left)
- [top](#top)
- [width](#width)
- [height](#height)
- [modeless](#modeless)
- [HWND](#hwnd)
- [icon](#icon)
- [isValid](#isvalid)
- [propsheet](#propsheet)
- [progress](#progress)
- [progressValue](#progressvalue)
- [progressCanceled](#progresscanceled)

### 方法

- [loadResource](#loadresource)
- [makeTemplate](#maketemplate)
- [open](#open)
- [close](#close)
- [getItem](#getitem)
- [getItemID](#getitemid)
- [getItemClassName](#getitemclassname)
- [setItemInt](#setitemint)
- [getItemInt](#getitemint)
- [setItemText](#setitemtext)
- [getItemText](#getitemtext)
- [setItemEnabled](#setitemenabled)
- [getItemEnabled](#getitemenabled)
- [setItemFocus](#setitemfocus)
- [setItemPos](#setitempos)
- [setItemSize](#setitemsize)
- [getItemLeft](#getitemleft)
- [getItemTop](#getitemtop)
- [getItemWidth](#getitemwidth)
- [getItemHeight](#getitemheight)
- [setItemBitmap](#setitembitmap)
- [sendItemMessage](#senditemmessage)
- [getBaseUnits](#getbaseunits)
- [mapRect](#maprect)
- [invalidateRect](#invalidaterect)
- [setPos](#setpos)
- [setSize](#setsize)
- [setActive](#setactive)
- [onInit](#oninit)
- [onCommand](#oncommand)
- [onHScroll](#onhscroll)
- [onVScroll](#onvscroll)
- [onNotify](#onnotify)
- [onKeyDown](#onkeydown)
- [onKeyUp](#onkeyup)
- [messageBox](#messagebox)
- [chooseColor](#choosecolor)
- [show](#show)
- [InitCommonControls](#initcommoncontrols)
- [InitCommonControlsEx](#initcommoncontrolsex)
- [openPropertySheet](#openpropertysheet)
- [propSheetMessage](#propsheetmessage)
- [setMessageResult](#setmessageresult)
- [openProgress](#openprogress)
- [closeProgress](#closeprogress)
- [insertTab](#inserttab)
- [deleteTab](#deletetab)
- [deleteAllTab](#deletealltab)
- [getCurSel](#getcursel)
- [selectTab](#selecttab)
- [setScrollInfo](#setscrollinfo)
- [getScrollInfo](#getscrollinfo)

---

### WIN32Dialog

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `owner` | `&nbsp;` | 设置用于事件回调的所有者。为 null 或 this 时发送给自身。 |

**说明**

构造函数

---

### left

属性 \ 访问: `r`

**说明**

获取对话框尺寸

只读。无法更改尺寸，请注意

---

### top

属性 \ 访问: `r`

---

### width

属性 \ 访问: `r`

---

### height

属性 \ 访问: `r`

---

### modeless

属性 \ 访问: `r/w`

**说明**

用于无模式对话框的标志

为 true 时以无模式状态打开对话框。
无模式时，如果未在对话框的 style 中指定 WS_VISIBLE，
在 open() 时不会自动显示，请注意。

---

### HWND

属性 \ 访问: `r`

**说明**

对话框的窗口句柄

---

### icon

属性 \ 访问: `r/w`

**说明**

对话框的图标图像

WIN32Dialog.Bitmap 类的实例:该图像
null:可执行文件的图标
void:无图标

---

### isValid

属性 \ 访问: `r`

**说明**

对话框是否已 open

---

### propsheet

属性 \ 访问: `r`

**说明**

是否正作为属性表显示

---

### progress

属性 \ 访问: `r`

**说明**

是否为进度状态

---

### progressValue

属性 \ 访问: `r/w`

**说明**

更新进度条 ( 0-100 的数值，为负数时为跑马灯状态的速度 )

---

### progressCanceled

属性 \ 访问: `r/w`

**说明**

进度是否已被取消 ( ※目标按钮固定为 IDCANCEL )

---

### loadResource

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dllfile` | `&nbsp;` | dll 文件 ( 本地存储形式 ) |
| `resource` | `&nbsp;` | 对话框资源名 |

**说明**

加载对话框资源

---

### makeTemplate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `header` | `&nbsp;` | 对话框模板头 ( 必须是 WIN32Dialog.Header 类的实例 ) |
| `items*` | `&nbsp;` | 对话框模板项 ( 必须是 WIN32Dialog.Items 类的实例 ) |

**说明**

生成对话框模板

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 父窗口 ( 吉里吉里的 Window 类 )，省略时或为 void 时没有父窗口 |

**说明**

打开对话框

需要事先通过 makeTemplate 生成对话框模板，
或已通过 loadResource 加载对话框资源。
注意 loadResource 的数据优先于 makeTemplate。

---

### close

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `result` | `&nbsp;` | 传给 EndDialog API 的结果值 |

**说明**

关闭对话框

---

### getItem

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |

**返回值**

对话框项的 HWND

**说明**

GetDlgItem 的包装器

---

### getItemID

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `hwnd` | `&nbsp;` | 对话框项的 HWND |

**返回值**

对话框项的 ID

**说明**

GetDlgCtrlID 的包装器

---

### getItemClassName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |

**返回值**

对话框项的类名

**说明**

GetClassName 的包装器

---

### setItemInt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |
| `value` | `&nbsp;` | 要设置的值 ( 仅 set 时 ) |

**返回值**

获取结果 ( 仅 get 时 )

**说明**

Get/SetDlgItemInt/Text 的包装器

---

### getItemInt

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### getItemText

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemEnabled

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |
| `value` | `&nbsp;` | 启用或禁用的设置 ( 仅 set 时 ) |

**返回值**

获取结果 ( 仅 get 时 )

**说明**

设置与获取项的启用或禁用状态

---

### getItemEnabled

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemFocus

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |

**说明**

设置项的焦点

---

### setItemPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |
| `x` | `&nbsp;` | 对话框项的 X 坐标 |
| `y` | `&nbsp;` | 对话框项的 Y 坐标 |

**说明**

更改与获取项的位置与大小

---

### setItemSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

---

### getItemLeft

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemTop

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemWidth

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getItemHeight

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### setItemBitmap

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |
| `bmp` | `&nbsp;` | 要设置为位图的 WIN32Dialog.Bitmap 的实例<br>WIN32DialogEX 中可指定 Layer 实例 |

**说明**

为项设置 Bitmap

---

### sendItemMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 对话框项的 ID |
| `msg` | `&nbsp;` | 要发送的消息 |
| `wparam` | `&nbsp;` | 要发送的 wparam |
| `lparam` | `&nbsp;` | 要发送的 lparam |

**返回值**

LRESULT

**说明**

SendDlgItemMessage 的包装器

---

### getBaseUnits

方法

**返回值**

结果字典(%[ h:水平单位, v:垂直单位 ])

**说明**

GetDialogBaseUnit 的包装器

---

### mapRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | 矩形区域字典数组(%[ left, top, right, bottom ]) |

**返回值**

结果字典数组(%[ left, top, right, bottom ])

**说明**

MapDialogRect 的包装器

---

### invalidateRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `rect` | `&nbsp;` | 矩形区域字典数组(%[ left, top, right, bottom ]) |
| `erase` | `&nbsp;` | 是否擦除的标志 |

**返回值**

成功时为 true

**说明**

InvalidateRect 的包装器

---

### setPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | x 坐标 |
| `y` | `&nbsp;` | y 坐标<br>非对话框显示期间会出错，请注意。请在 onInit 等中更改坐标 |

**说明**

设置对话框坐标

---

### setSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `w` | `&nbsp;` | 宽度 |
| `h` | `&nbsp;` | 高度<br>非对话框显示期间会出错，请注意。 |

**说明**

设置对话框的大小

---

### setActive

方法

**说明**

激活对话框

在此方法添加之前的版本中，存在 setPos/setSize 会将其激活的问题，请留意 ( 当前不会激活 )

---

### onInit

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc 的消息 == WM_INITDIALOG |
| `wparam` | `&nbsp;` | DlgProc 的 WPARAM |
| `lparam` | `&nbsp;` | DlgProc 的 LPARAM |

**说明**

WM_INITDIALOG 的回调

请注意，回调是对 owner 调用的。
如果 owner.onInit 未定义，则不做任何事。

---

### onCommand

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc 的消息 == WM_COMMAND |
| `wparam` | `&nbsp;` | DlgProc 的 WPARAM |
| `lparam` | `&nbsp;` | DlgProc 的 LPARAM |

**说明**

WM_COMMAND 的回调

请注意，回调是对 owner 调用的。
如果 owner.onCommand 未定义，则不做任何事。

---

### onHScroll

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc 的消息 == WM_HSCROLL |
| `wparam` | `&nbsp;` | DlgProc 的 WPARAM |
| `lparam` | `&nbsp;` | DlgProc 的 LPARAM |

**说明**

WM_HSCROLL 的回调

---

### onVScroll

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` | DlgProc 的消息 == WM_VSCROLL |
| `wparam` | `&nbsp;` | DlgProc 的 WPARAM |
| `lparam` | `&nbsp;` | DlgProc 的 LPARAM |

**说明**

WM_VSCROLL 的回调

---

### onNotify

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wparam` | `&nbsp;` | DlgProc 的 WPARAM |
| `lparam` | `&nbsp;` |  |

**说明**

WM_NOTIFY 的回调

---

### onKeyDown

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `wparam` | `&nbsp;` | DlgProc 的 WPARAM |
| `lparam` | `&nbsp;` | DlgProc 的 LPARAM |

**说明**

WM_KEYDOWN 的回调

---

### onKeyUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `wparam` | `&nbsp;` | DlgProc 的 WPARAM |
| `lparam` | `&nbsp;` | DlgProc 的 LPARAM |

**说明**

WM_KEYUP 的回调

---

### messageBox

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 所有者 window ( 不指定时请传 null ) |
| `text` | `&nbsp;` | 消息文本 |
| `caption` | `&nbsp;` | 对话框的标题 |
| `type` | `&nbsp;` | 要显示的按钮与图标的标志组合 |

**返回值**

被按下的按钮的 ID
若在 type 中设置独自的标志 MB_OWNER_CENTER，则会尝试显示在所有者窗口的中央
( 但如果对话框会超出屏幕，则显示在桌面的中央 )

**说明**

MessageBox 的包装器

---

### chooseColor

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 所有者 window ( 不指定时请传 null ) |
| `elm` | `&nbsp;` | 选项 ( 字典或可省略 )<br>%[ color:初始选中颜色, palette:[ 调色板颜色1, ... , 调色板颜色16 ],<br>disableCustomColor:禁用颜色创建, openCustomColor:使颜色创建从一开始就处于打开状态 ] |

**返回值**

选中的颜色(0xRRGGBB)，取消时为 void
如果传入了 elm.palette，其内容也会被更新

**说明**

ChooseColor 的包装器

---

### show

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nCmdShow` | `&nbsp;` | SW_* 标志 |

**说明**

ShowWindow 的包装器

主要用于无模式对话框。

---

### InitCommonControls

方法

**返回值**

是否成功 ( 仅 ~Ex )

**说明**

InitCommonControls, InitCommonControlsEx 的包装器

---

### InitCommonControlsEx

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `icc` | `&nbsp;` |  |

---

### openPropertySheet

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 所有者 window ( 不指定时请传 null ) |
| `sheets` | `&nbsp;` | 属性页信息 ( WIN32Dialog 实例的数组 ) |
| `elm` | `&nbsp;` | 选项 ( 字典或可省略 )<br>%[ caption:属性表标题, page:初始页码, icon:图标 ] |

**返回值**

::PropertySheet 的返回值

**说明**

显示属性表 ( 始终为模式状态：无模式尚未实现 )

---

### propSheetMessage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `msg` | `&nbsp;` |  |
| `wparam` | `&nbsp;` |  |
| `lparam` | `&nbsp;` |  |

**说明**

向属性表窗口发送 PSM_* 消息

---

### setMessageResult

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `value` | `&nbsp;` |  |

**说明**

设置 DWL_MSGRESULT 的值

---

### openProgress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 进度条的对话框项 ID ( 由 progressValue 属性更新的目标 ) |
| `window` | `&nbsp;` | [optional] 所有者 window (void=无所有者,null=Application) |
| `dsapp` | `(typeof window!="Object")` | [optional] 进度显示期间是否禁用应用程序窗口 |
| `breathe` | `(typeof window=="Object")` | [optional] progressValue 的 setter 是否执行 breathe |
| `activate` | `true` |  |

**返回值**

成功时为 true

**说明**

显示进度对话框

不要在进度对话框的 style 中指定 WS_VISIBLE
关闭时务必使用 closeProgress()
进度显示时，除 onInit 以外不会产生回调，请注意

---

### closeProgress

方法

**说明**

关闭进度对话框

---

### insertTab

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `pos` | `&nbsp;` |  |
| `label` | `&nbsp;` |  |

**说明**

使用标签页控件。

使用步骤正在研究之中
insertTab(IDC_TAB, 0, "基本"); // 添加标签页
// deleteTab(IDC_TAB, 0); // 删除标签页
// deleteAllTab(IDC_TAB); // 删除所有标签页
var dlg = new WIN32Dialog(); dlg.loadResource("resource.dll", "INNER"); // 设置为 Border=None, Style=Child 的对话框
selectTab(IDC_TAB, dlg); // 显示
insertTab(IDC_TAB, 1, "拡張");
var dlg2 = new WIN32Dialog(); dlg2.loadResource("resource.dll", "INNER2");
dlg.show(SW_HIDE);
selectTab(IDC_TAB, dlg2); // 切换
// 在 onNotify 中，当 notify->code == TCN_SELCHANGE 且 notify->idFrom == IDC_TAB 时，即为用户进行的标签页切换
// 用 getCurSel(tab_id) 获取标签页编号，对相应的对话框执行 SW_SHOW，其余执行 SW_HIDE
// 标签页编号与相应的对话框需要自行管理
※ dlg、dlg2 的 open 是在被 selectTab 时进行的，因此在 show(SW_HIDE) 时请用 isValid 确认是否已 open

---

### deleteTab

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `pos` | `&nbsp;` |  |

---

### deleteAllTab

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |

---

### getCurSel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |

---

### selectTab

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tab_id` | `&nbsp;` |  |
| `dialog` | `&nbsp;` |  |

---

### setScrollInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 滚动条的对话框项 ID |
| `pos` | `&nbsp;` | 滑块的位置 |
| `min` | `&nbsp;` | 可取的最小值 |
| `max` | `&nbsp;` | 可取的最大值 |
| `page` | `&nbsp;` | 页的值 |

**说明**

ScrollInfo 的设置

---

### getScrollInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 滚动条的对话框项 ID |

**返回值**

%[pos, min, max, page]

**说明**

ScrollInfo 的获取

---
