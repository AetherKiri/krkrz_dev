# Live2DDevice

## 成员列表

### 构造函数

- [Live2DDevice](#live2ddevice)

### 方法

- [onBeginScene](#onbeginscene)
- [onEndScene](#onendscene)
- [prepareShaders](#prepareshaders)

---

### Live2DDevice

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `oglbase` | `&nbsp;` | 持有 GetProcAddress 的对象<br>可以指定以下任意一个:<br>- krkrgles 插件提供的 OpenGL 上下文对象<br>- 新版吉里吉里Z 的 OGLDrawDevice（引擎本体内置的 OpenGL 绘制设备）<br>针对当前的 OGL 上下文进行初始化 |

---

### onBeginScene

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` |  |
| `height` | `&nbsp;` |  |

**说明**

在整体绘制开始时只调用 1 次

※请在生成时的上下文中调用

---

### onEndScene

方法

**说明**

在整体绘制完成时只调用 1 次

---

### prepareShaders

方法

**说明**

执行着色器的预编译

未调用时会在首次绘制时集中编译并产生数秒左右的等待时间，
因此推荐在启动时等时机预先调用。
※请在生成时的上下文中调用

---
