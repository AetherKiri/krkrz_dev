# ActiveX

生成可操作 ActiveX 的对象。
可以直接调用 ActiveX 通过 IDispatch 持有的方法。

继承自: [WIN32OLE](WIN32OLE.md)

## 成员列表

### 构造函数

- [ActiveX](#activex)

### 属性

- [isValidWindow](#isvalidwindow)
- [left](#left)
- [top](#top)
- [width](#width)
- [height](#height)
- [visible](#visible)

### 方法

- [setPos](#setpos)
- [setSize](#setsize)
- [setExternalUI](#setexternalui)
- [onCreate](#oncreate)
- [onDestroy](#ondestroy)

---

### ActiveX

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 用字符串指定识别名或 CLSID。※注意，与 WIN32OLE 的指定相比 CLSID 的格式不同，此处为 CAxWindow::CreateControl 的格式 |
| `win` | `null` | 指定后会在该窗口之上生成。省略时成为独立窗口。 |
| `left` | `0` | 显示坐标。指定了窗口且省略时，为窗口客户区的左上角 |
| `top` | `0` | 显示坐标。指定了窗口且省略时，为窗口客户区的左上角 |
| `width` | `100` | 显示大小。指定了窗口且省略时，为父窗口客户区的大小 |
| `height` | `100` | 显示大小。指定了窗口且省略时，为父窗口客户区的大小 |

**说明**

构造函数

---

### isValidWindow

属性 \ 访问: `r`

**说明**

窗口是否有效 (只读)

---

### left

属性 \ 访问: `r/w`

**说明**

左端坐标

---

### top

属性 \ 访问: `r/w`

**说明**

上端坐标

---

### width

属性 \ 访问: `r/w`

**说明**

宽度

---

### height

属性 \ 访问: `r/w`

**说明**

高度

---

### visible

属性 \ 访问: `r/w`

**说明**

显示状态

---

### setPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 左端坐标 |
| `top` | `&nbsp;` | 上端坐标 |

**说明**

坐标指定

---

### setSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 宽度 |
| `height` | `&nbsp;` | 高度 |

**说明**

大小指定

---

### setExternalUI

方法

**说明**

扩展 UI 指定

仅在 IE 组件中有意义。在当前版本中，调用它会抑制
上下文菜单。

---

### onCreate

方法

**说明**

窗口生成完成后被调用的事件

在初始生成或全屏处理等情况下窗口生成后会被调用
重建后，已注册的事件会被全部丢弃，其他各种内容也会
被初始化，因此需要在此事件内重新设置必要的内容。
---------------------------------------------------------

---

### onDestroy

方法

**说明**

窗口销毁前被调用的事件

在全屏处理或对象销毁等导致窗口被销毁前会被调用。

---
