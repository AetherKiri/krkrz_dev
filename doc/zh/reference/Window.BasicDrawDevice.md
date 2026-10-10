# Window.BasicDrawDevice

Window.BasicDrawDevice 类是用于将该实例注册到 [Window.drawDevice](Window.md#drawdevice) 中使用的 DrawDevice，提供标准的绘制功能。

## 成员列表

### 构造函数

- [BasicDrawDevice](#basicdrawdevice)

### 属性

- [interface](#interface)
- [videoPresenterHost](#videopresenterhost)
- [dialogRendererHost](#dialogrendererhost)
- [viewportBackgroundHost](#viewportbackgroundhost)
- [d3d11Device](#d3d11device)

### 方法

- [recreate](#recreate)

---

### BasicDrawDevice

构造函数

**说明**

构建 BasicDrawDevice 对象

构建 Window.BasicDrawDevice 类的对象。

初始状态下，`Window.drawDevice` 中已注册该类的实例，因此无需重新注册。

---

### interface

属性 \ 访问: `r`

**说明**

获取接口对象

用于让插件等使用 DrawDevice 对象。

---

### videoPresenterHost

属性 \ 访问: `r`

**说明**

叠加视频 presenter 注册入口 (指针值)

这是叠加视频侧 (VideoOverlay) 为了以 pull 型合成到该 DrawDevice 的 D3D11 后台缓冲区而读取的、指向 `iTVPVideoPresenterHost` 的指针值。
若为非 0，则注册 presenter 并进入 pull 合成；若为 0/未定义，则回退到子窗口 present。
通常由引擎内部/插件使用。

---

### dialogRendererHost

属性 \ 访问: `r`

**说明**

Elements 对话框 renderer host (指针值)

这是用于获取 Elements 覆盖层绘制适配器的、指向 `iTVPDialogRendererHost` 的指针值。
通常由引擎内部/插件使用。

---

### viewportBackgroundHost

属性 \ 访问: `r`

**说明**

视口余白涂色填充注册入口 (指针值)

这是用于接收游戏画面未覆盖整个绘制区域时的余白 ( [Window.viewportBgColor](Window.md#viewportbgcolor) /
[Window.setViewportWallpaper](Window.md#setviewportwallpaper) ) 的、指向
`iTVPViewportBackgroundHost` 的指针值。Window 仅在该属性为非 0
时才反映余白设置 ( 在不具有该属性的绘制设备上，余白的涂色填充不会
生效，仍保持该设备默认的填充 )。通常由引擎内部/插件
使用。

---

### d3d11Device

属性 \ 访问: `r`

**说明**

ID3D11Device 指针 (指针值)

这是硬件视频 (IMFMediaEngine) 为了与引擎的 D3D11 设备绑定进行硬件解码而公开的、指向 `ID3D11Device` 的指针值 ( VIDEO_SUPPORT + 已完成多线程保护 )。
仅限 WINVER (D3D11) 构建。通常由引擎内部/插件使用。

---

### recreate

方法

**说明**

内部设备重新生成

执行内部设备的重新生成。

通常不会使用。

---
