# Pad

Pad 扩展

## 成员列表

### 方法

- [registerExEvent](#registerexevent)

---

### registerExEvent

方法

**说明**

启用扩展事件（注册失败会抛出异常）

作为扩展事件会发生以下内容：
onClose  关闭按钮被按下

※注意：因 borderStyle 等更改导致窗口被重建后，事件将不再发生
⇒这种情况下请再次调用 registerExEvent()

---
