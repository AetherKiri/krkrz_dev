# 游戏画面的显示视野控制 ( 视口 )

可以把内侧游戏画面以任意的大小、位置、倍率
配置在外侧窗口 ( surface ) 之中，并用背景色或壁纸图像填充四周的余白。在保持游戏本来
分辨率的同时，让显示跟随窗口大小进行黑边
显示、整数倍放大、居中等时使用。

内部结构的详情请参照 src/core 侧的指南:

- [doc/Viewport.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Viewport.md)

!!! note "支持的构建 / 支持的 DrawDevice"
    配置的指定 ( fit / zoom / align / offset ) 在 **Windows 原生 ( WINVER )
    构建与 SDL3 / 通用构建双方**都可以使用 ( WINVER 支持为 2026-08-17 )。

    余白的**涂色填充** ( [Window.viewportBgColor](../../reference/Window.md#viewportbgcolor) /
    [Window.setViewportWallpaper](../../reference/Window.md#setviewportwallpaper) ) 只在
    绘制设备支持时才有效。随附的
    [BasicDrawDevice](../../reference/Window.BasicDrawDevice.md) ( WINVER 默认 ) /
    [SDLDrawDevice](../../reference/SDLDrawDevice.md) / SDLOGL /
    [OGLDrawDevice](../../reference/OGLDrawDevice.md) 全部支持。
    不支持的绘制设备 ( NullDrawDevice 以及插件制作的设备 ) 中，
    余白会保持该设备默认的填充
    ( 判定方式是 `drawDevice.viewportBackgroundHost` 是否为非 0 )。

---

## 想保持与以往相同的显示时

默认是 `fit = "contain"` / `align = 中央`。当窗口与内侧游戏画面
大小不同时，保持宽高比缩放并放置在中央。

想回到吉里吉里2 / 吉里吉里Z 以往的“即使把窗口拉宽，游戏仍保持原尺寸在左上”时，
请显式指定以下内容。

```tjs
window.setViewport("none", 1.0, 0, 0);   // fit=none, zoom=1.0, alignX=0, alignY=0
```

!!! tip "通常不会出现差异"
    只要用 [Window.setInnerSize](../../reference/Window.md#setinnersize) 把内侧尺寸
    始终保持为“primaryLayer 的大小 × [setZoom](../../reference/Window.md#setzoom) 的倍率”，
    无论哪种适应方式都会以等倍 1:1 显示。出现差异的是
    **用户调整窗口大小 / 最大化时**、**移动到放大率不同的显示器时**，
    以及**无法更改窗口大小的环境 ( 移动端 /
    主机 )**。

---

## 概念模型

```
[外側 surface] = Window.innerWidth / innerHeight = OS ウインドウ client
        │  ビューポート設定 (fit / zoom / align / offset)
        ▼
[内側ゲーム]  = primaryLayer のサイズ (TJS から setSize で指定)
```

- **外侧 surface** … [Window.innerWidth](../../reference/Window.md#innerwidth) /
  [Window.innerHeight](../../reference/Window.md#innerheight)。Elements UI
  覆盖层也是这个坐标系。
- **内侧游戏** … primaryLayer 的大小。由 `primaryLayer.setSize(w, h)` 决定，
  与 [Window.setInnerSize](../../reference/Window.md#setinnersize) 相互独立。
- 让两者一致就是以往那样的全面等倍。如果设为不同大小，游戏会按照设置
  被配置到 surface 内，并产生余白。

鼠标坐标会根据配置自动校正为游戏逻辑坐标，因此无论哪种 fit/zoom，
输入都会正确送达游戏内部。

---

## fit 方式

| 值 | 行为 |
|---|---|
| `"contain"` | 保持宽高比能容纳的最大 ( 黑边 )。**默认** |
| `"cover"` | 保持宽高比填满的最小 ( 超出部分裁剪 ) |
| `"fill"` | 无视宽高比拉伸到 surface 全面 |
| `"none"` | 原尺寸 ( 倍率 1.0 ) |
| `"integer"` | 在能容纳的范围内取最大整数倍 ( 最低 1 倍，保持像素等倍 ) |
| `"custom"` | 使用 [Window.viewportZoom](../../reference/Window.md#viewportzoom) 的倍率 |

---

## 固定窗口的宽高比 ( aspectLock )

viewport 决定的是“**在外侧 surface 中如何放置游戏画面**”，
而外侧 surface 的**形状本身**则取决于用户的调整或平台。
想固定它时使用 [Window.aspectLock](../../reference/Window.md#aspectlock)。

```tjs
window.aspectLock = "16:9";        // ウインドウの内側を 16:9 に固定
window.viewportFit = "integer";    // その中にゲーム画面をドットバイドットで配置
window.aspectLock = "";            // 固定を解除
```

在把游戏画面 ( primaryLayer ) 的比率与整个窗口的比率**分开**时
有效。例如即使游戏画面是 640x400 ( 8:5 )，也保持整个窗口为 16:9、
并在其中以整数倍放置，就是这样的构成。当 UI ( Elements 的覆盖层等 )
以 16:9 的基本大小制作时，如果窗口没有保持 16:9，
UI 与游戏画面的框就会错位，因此需要这个固定。

启用后会改变以下 2 点。

- 用户对窗口的调整大小会被约束到这个比率 ( 拖拽操作过程中也
  保持比率 )。
- [Window.setZoom](../../reference/Window.md#setzoom) 会从这个比率
  决定高度 ( 以往是“primaryLayer 的大小 × 倍率”，因此
  每次设置倍率都会回到图层自身的比率 )。

设置时刻的内侧尺寸也会**以宽度为基准**被调整到这个比率。

!!! warning "SDL3 / 通用构建专用"
    Windows 原生 ( WINVER ) 构建中不执行任何操作。即使设置也会被忽略，
    读取时始终返回空字符串。

---

## TJS API

[Window](../../reference/Window.md) 类中添加了以下成员。

### 属性

| 成员 | 说明 |
|---|---|
| [viewportFit](../../reference/Window.md#viewportfit) | fit 方式 ( 字符串 )。默认 `"contain"` |
| [viewportZoom](../../reference/Window.md#viewportzoom) | `"custom"` 时的倍率。默认 1.0 |
| [viewportAlignX](../../reference/Window.md#viewportalignx) | 水平配置 0=左 / 0.5=中央 / 1=右 |
| [viewportAlignY](../../reference/Window.md#viewportaligny) | 垂直配置 0=上 / 0.5=中央 / 1=下 |
| [viewportOffsetX](../../reference/Window.md#viewportoffsetx) | 水平偏移 ( px ) |
| [viewportOffsetY](../../reference/Window.md#viewportoffsety) | 垂直偏移 ( px ) |
| [viewportBgColor](../../reference/Window.md#viewportbgcolor) | 余白的背景色 `0xRRGGBB` |
| [aspectLock](../../reference/Window.md#aspectlock) | 固定窗口自身的宽高比 ( `"16:9"` 等 )。默认 `""` = 不固定。**SDL3 / 通用构建专用** |

### 方法

| 成员 | 说明 |
|---|---|
| [setViewport](../../reference/Window.md#setviewport)(fit [,zoom [,alignX [,alignY [,offsetX [,offsetY]]]]]) | 一次性设置配置 |
| [setViewportWallpaper](../../reference/Window.md#setviewportwallpaper)(image [,fit [,alignX [,alignY]]]) | 设置余白的壁纸图像 |
| [clearViewportWallpaper](../../reference/Window.md#clearviewportwallpaper)() | 解除壁纸 |

壁纸的 `image` 除了存储名 ( 字符串 ) 之外，也可以直接传递 [Layer](../../reference/Layer.md) /
[Bitmap](../../reference/Bitmap.md) 对象 ( 会被保持引用 )。

---

## 使用示例

```tjs
var win = new Window();
win.setInnerSize(1280, 720);       // 外側ウインドウ

var lay = new Layer(win, null);    // primaryLayer
lay.setSize(640, 400);             // 内側ゲーム解像度
win.add(lay);

win.viewportBgColor = 0xff203060;  // 余白の色
win.viewportFit = "integer";       // 整数倍 (640x400 → 1280x800 は不可なので 1 倍)

// または 180% センタリング:
win.setViewport("custom", 1.8);

// 余白に壁紙 (ストレージ名でもオブジェクトでも可):
win.setViewportWallpaper("bg_pattern.png", "cover");
// win.setViewportWallpaper(myBitmap, "cover");   // Layer / Bitmap を直接渡す
```
