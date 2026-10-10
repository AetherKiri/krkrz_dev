# Console

Debug.console 扩展

## 成员列表

### 方法

- [restoreMaxmimize](#restoremaxmimize)
- [maxmimize](#maxmimize)
- [getRect](#getrect)
- [setPos](#setpos)
- [getPlacement](#getplacement)
- [setPlacement](#setplacement)
- [bringAfter](#bringafter)

---

### restoreMaxmimize

方法

**说明**

窗口最大化的还原（用于解决保持最大化状态退出会导致下次尺寸错乱的问题）

---

### maxmimize

方法

**说明**

将窗口最大化

---

### getRect

方法

**说明**

获取坐标、大小

---

### setPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` |  |
| `y` | `&nbsp;` |  |
| `w` | `&nbsp;` |  |
| `h` | `&nbsp;` |  |

**说明**

设置坐标、大小

---

### getPlacement

方法

**说明**

获取 WindowPlacement

---

### setPlacement

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dict` | `&nbsp;` |  |

**说明**

设置 WindowPlacement

---

### bringAfter

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `win` | `&nbsp;` |  |

**说明**

※ 启动后若不先令 visible=true 生成一次窗口就会失败 更改优先级

---
