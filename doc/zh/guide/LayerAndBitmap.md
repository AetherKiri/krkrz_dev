# Layer、Bitmap 与 ImageFunction

在吉里吉里Z 中处理图像的类有 [Layer](../reference/Layer.md) 和 [Bitmap](../reference/Bitmap.md) 的
2 个，再加上一个只有方法的类 [ImageFunction](../reference/ImageFunction.md)。
本文总结这三者是什么关系，以及何时该用哪一个。

## 用三行话概括

- **Layer** 是“会被显示的图像”。除了图像缓冲区之外，还拥有父子树、显示位置、不透明度、输入事件、重绘通知。
- **Bitmap** 是“不会显示的一张图像缓冲区”。可以读取、保存、访问像素，但**完全没有绘制方法**。
- **ImageFunction** 是从 Layer 所拥有的绘制方法中去掉 *Layer 固有因素* (显示属性、裁剪矩形、更新通知)，
  **使其可以直接对 Bitmap 调用的静态方法集合**。是填补 Bitmap 没有绘制方法这一空缺的类。

## 结构

从 TJS2 可见的类有 3 个，但实际持有并加工像素的引擎内部实体 (`tTVPBaseBitmap`) 只有 1 种。
Layer 和 Bitmap 都只是持有它而已，绘制算法 (Blt / StretchBlt / AffineBlt / 填充 / 文字绘制 …) 是完全共通的。

```text
 TJS2 レベル
 ┌────────────────────────────────┐   ┌──────────────────────────────┐   ┌───────────────────────┐
 │ Layer                          │   │ Bitmap                       │   │ ImageFunction         │
 │  ・親子ツリー / 表示位置       │   │  ・画像 1 枚だけ             │   │  ・全メソッド static  │
 │  ・visible / opacity / type    │   │  ・width / height / buffer   │   │  ・インスタンスを     │
 │  ・face / holdAlpha / clip*    │   │  ・load / loadAsync / save   │   │    作る意味は無い     │
 │  ・入力イベント / フォーカス   │   │  ・getPixel / setPixel       │   │                       │
 │  ・描画メソッド多数            │   │  ・独自の描画メソッドは無い  │   │                       │
 │  ・描画すると update() が走る  │   │                              │   │                       │
 └───────────────┬────────────────┘   └───────────────┬──────────────┘   └───────────┬───────────┘
                 │ MainImage                          │                              │
                 │ ProvinceImage (領域画像)           │ (1 枚だけ)                   │ 第 1 引数に
                 ▼                                    ▼                              │ Bitmap を取る
 C++ レベル  ┌───────────────────────────────────────────────────────────┐           │
             │ tTVPBaseBitmap                                            │◀──────────┘
             │  ピクセルバッファ本体 (32bpp / 8bpp、コピーオンライト共有)│
             │  Blt / StretchBlt / AffineBlt / Fill / DrawText / Blur …  │
             └───────────────────────────────────────────────────────────┘
```

也就是说，**ImageFunction 是“Layer 绘制方法的 Bitmap 版”**。
内部调用的处理与 Layer 版完全相同，不同的只有“由谁来决定参数”。

## 为什么需要 Bitmap 和 ImageFunction

Layer 无法单独创建。它的构造函数需要 [Window](../reference/Window.md) (或
[BitmapLayerTreeOwner](../reference/BitmapLayerTreeOwner.md)) 和父图层，
每次绘制都会触发重绘区域的通知 (`update`)，并成为整棵树合成的对象。
对于“不想显示在画面上但想加工的图像”——素材预处理、缓存、截图加工、异步加载——来说，它太重了。

Bitmap 就是那个轻量的承接容器，只需 `new Bitmap(w, h)` 就能创建，与显示和树都毫无关系。
不过 Bitmap 自身没有绘制方法，因此提供了 ImageFunction，作为在 Bitmap 上进行合成、文字绘制、滤镜处理的手段。

也有只有 Bitmap 才有的功能。其代表是**异步图像加载** ([Bitmap.loadAsync](../reference/Bitmap.md#loadasync))，
Layer 没有对应的方法。读取之后
用 [Layer.copyFromBitmapToMainImage](../reference/Layer.md#copyfrombitmaptomainimage) 交给 Layer 是标准做法。

## 方法对应表

| 处理 | Layer | ImageFunction (对象为 Bitmap) | Bitmap 自身 |
| --- | --- | --- | --- |
| 矩形填充 | `fillRect` | `fillRect` | — |
| 半透明、遮罩填充 | `colorRect` | `colorRect` | — |
| 文字绘制 | `drawText` | `drawText` (显式指定 Font) | — |
| 字形绘制 | `drawGlyph` | `drawGlyph` | — |
| 整形文本绘制 | `drawShapedText` / `drawShapedTextArea` | **无** | — |
| 竖排文字绘制 | `drawVerticalTextArea` | **无** | — |
| 矩形复制 | `copyRect` | `operateRect` + `omOpaque` / `dfOpaque` | — |
| 矩形运算合成 | `operateRect` | `operateRect` | — |
| 缩放复制 | `stretchCopy` | `operateStretch` + `omOpaque` / `dfOpaque` | — |
| 缩放运算合成 | `operateStretch` | `operateStretch` | — |
| 仿射复制 | `affineCopy` | `operateAffine` + `omOpaque` / `dfOpaque` | — |
| 仿射运算合成 | `operateAffine` | `operateAffine` | — |
| 9patch 复制 | `copy9Patch` | `copy9Patch` | — |
| 矩形模糊 | `doBoxBlur` | `doBoxBlur` | — |
| 伽马校正 | `adjustGamma` | `adjustGamma` | — |
| 灰度化 | `doGrayScale` | `doGrayScale` | — |
| 左右 / 上下翻转 | `flipLR` / `flipUD` | `flipLR` / `flipUD` | — |
| 树合成复制 | `piledCopy` | **无** (没有子图层的概念) | — |
| 像素读写 | `getMainPixel` / `setMainPixel` / `getMaskPixel` / `setMaskPixel` | — | `getPixel` / `setPixel` / `getMaskPixel` / `setMaskPixel` |
| 图像读取 | `loadImages` | — | `load` / `loadAsync` / `loadHeader` |
| 图像保存 | `saveLayerImage` | — | `save` |
| 解除共享 | `independMainImage` | — | `independ` |
| 更改图像大小 | `setImageSize` | — | `setSize` |

!!! note "复制类方法在 ImageFunction 中不存在的原因"
    与 `copyRect` / `stretchCopy` / `affineCopy` 相当的专用方法在 ImageFunction 中并不存在。
    因为指定 `mode = omOpaque`, `face = dfOpaque`, `hda = false` 的 `operate*` 本身就会成为单纯拷贝 (`bmCopy`)。
    不过，与 `affineCopy` 的 `clear` 参数 (清除变换后范围外区域的功能) 相当的功能并不存在。

## Layer 隐式使用的值，在 ImageFunction 中全部是显式参数

即使是同样的绘制处理，Layer 版也会从自身的属性组装参数。Bitmap 没有这些属性，
因此在 ImageFunction 中由调用方全部显式传入。**移植时容易出现差异的地方就在这里。**

| Layer 隐式使用的东西 | ImageFunction 中的对应 |
| --- | --- |
| [Layer.face](../reference/Layer.md#face) | `face` 参数 (默认 `dfAlpha`) |
| [Layer.holdAlpha](../reference/Layer.md#holdalpha) | `hda` 参数 (默认 `false`) |
| [Layer.clipLeft](../reference/Layer.md#clipleft) 及其他裁剪矩形 | `cliprect` 参数 (默认是**整张图像**，`null` 表示不裁剪) |
| [Layer.font](../reference/Layer.md#font) | `drawText` 的 `font` 参数。必须指定 [Font](../reference/Font.md) 对象 (可用 `new Font()` 单独生成) |
| 根据运算源 [Layer.type](../reference/Layer.md#type) 解析 `omAuto` | 因为没有解析目标，**`omAuto` 总是落到 `omAlpha`** |
| 绘制后通过 `update()` 发出重绘通知 | **无** (Bitmap 不显示，所以不需要) |
| [Layer.imageModified](../reference/Layer.md#imagemodified) | 无 |

!!! warning "`omAuto` 的处理"
    `omAuto` 的意思是“根据运算源 **Layer** 的 `type` 属性决定合成方法”。
    Bitmap 没有 `type`，所以在 ImageFunction 中 `omAuto` 会无条件变成 `omAlpha`。
    把 **Bitmap 作为运算源传入** `Layer.operateRect` 等时也会发生同样的情况
    (这种情况下 `omAuto` 也被当作 `omAlpha`)。想做加法合成或滤色合成时，请显式指定 `mode`。

## Layer ⇄ Bitmap 的往来

### 向 Layer 的绘制方法传入 Bitmap (1.1.0 及以后)

以下 Layer 方法在复制源/运算源 (`src`) 中可以指定 **Layer 或 Bitmap 皆可**。

`copyRect` / `copy9Patch` / `operateRect` / `stretchCopy` / `operateStretch` / `affineCopy` / `operateAffine`

把素材以 Bitmap 形式保存，再从它绘制到 Layer 的用途，这是最省事的方法。
另外 `piledCopy` (包含子图层的合成复制) 和 `assignImages` 是 Layer 专用的，不能传入 Bitmap。

### Layer → Bitmap

```tjs
var bmp = new Bitmap();
layer.copyToBitmapFromMainImage(bmp);   // メイン画像を bmp へ
```

内部只是进行**写时复制 (copy-on-write) 的共享**，不会发生像素的实际拷贝，因此速度很快
(在任意一方写入时就会自动分离)。包含遮罩 (alpha) 的 32bpp 会原样传递，
但**不会传递区域图像 (province)**。

### Bitmap → Layer

```tjs
layer.copyFromBitmapToMainImage(bmp);   // bmp をレイヤのメイン画像に
```

这边同样是写时复制共享，但在 Layer 侧会有以下副作用:

- 图层的图像大小会被更改为 Bitmap 的大小
- 裁剪矩形会被重置
- `update` 被触发并重绘

如果想在保持图层图像大小的情况下只替换一部分，请使用向
`copyRect` / `operateRect` 传入 Bitmap 的做法。

### 不能向 ImageFunction 传递 Layer

ImageFunction 的各方法**只接受 Bitmap 对象**。传入 Layer 会抛出参数非法的异常。
想用 ImageFunction 加工 Layer 的图像时，先用 `copyToBitmapFromMainImage` 接到 Bitmap 中，
加工后再用 `copyFromBitmapToMainImage` 写回。

### 用 Bitmap 获取图层树的合成结果

想在不准备 Window 的情况下组建图层树，并把其合成结果作为 Bitmap 取出时，
使用 [BitmapLayerTreeOwner](../reference/BitmapLayerTreeOwner.md)。
把它代替 Window 传给 Layer 构造函数的第 1 个参数，就能从
`BitmapLayerTreeOwner.bitmap` 得到该树的绘制结果作为 Bitmap。

## 陷阱

**不会被重绘**
: Bitmap 不是显示要素，所以即使通过 ImageFunction 写入，画面也不会有任何变化。
  只有反映到 Layer 之后才会变得可见。

**写时复制共享**
: `Bitmap.copyFrom` / `assignImages` / `copyToBitmapFromMainImage` 等只是共享实际缓冲区。
  通常会在写入前自动分离，所以无须在意；但如果确定要整面覆写，
  可以给 [Bitmap.independ](../reference/Bitmap.md#independ) 传 `false` 先进行分离，从而省去无谓的拷贝。

**直接访问缓冲区**
: [Bitmap.buffer](../reference/Bitmap.md#buffer) 是只读指针，要写入请使用
  [Bitmap.bufferForWrite](../reference/Bitmap.md#bufferforwrite) (在引用时会解除共享)。
  [Bitmap.bufferPitch](../reference/Bitmap.md#bufferpitch) **可能为负值** (自下而上存储)。
  另外 Bitmap 还有与 Layer 同名的别名属性 (`imageWidth` / `imageHeight` / `mainImageBuffer` /
  `mainImageBufferForWrite` / `mainImageBufferPitch`)，以便插件和 DrawDevice
  无需区分 Layer 和 Bitmap 就能获取图像。

**8bpp 的 Bitmap**
: 用 `new Bitmap(w, h, 8)` 也能创建 8bpp 的图像，但以颜色和 alpha 为前提的处理
  (`operate*` 系列、`fillRect` 的一部分等) 对 8bpp 会抛出异常。8bpp 面向区域图像 (province) 相当的用途。

**破坏 alpha 通道**
: 乘法、加法、滤色等运算类合成在 `hda` (= Layer 的 `holdAlpha`) 为假时不会保护合成目标的 alpha。
  对相当于 `ltAlpha` 的带 alpha 图像进行运算合成时，请指定 `hda = true`。
  忘记指定会导致结果变成纯黑色 (alpha 变为 0) 之类的症状。

**整形文本绘制仅限 Layer**
: `drawShapedText` / `drawShapedTextArea` / `measureShapedText` 系列，以及竖排的
  `drawVerticalTextArea` / `measureVerticalTextArea` 只有 Layer 才有。
  需要对 Bitmap 进行复杂的文本排版时，只能先绘制到 Layer，再接收为 Bitmap。

## 典型模式

### 不显示到画面，先合成素材再交给 Layer

```tjs
// 640x480 の作業用 Bitmap を作り、不透明な黒でクリア
var work = new Bitmap(640, 480);
ImageFunction.fillRect(work, 0xff000000);          // isalpha=true なので 0xAARRGGBB

// 背景素材を単純コピー (copyRect 相当)
var bg = new Bitmap("bg.png");
ImageFunction.operateRect(work, 0, 0, bg, null, null, omOpaque, dfOpaque);

// 文字を載せる (Font は明示的に用意する)
var font = new Font();
font.face   = "IPAGothic";
font.height = 24;
ImageFunction.drawText(work, font, 16, 16, "スコア: 1200", 0xffffff);

// できあがった画像をレイヤへ (ここで初めて画面に反映される)
layer.copyFromBitmapToMainImage(work);
```

### 异步加载图像并流入图层

```tjs
class AsyncImage extends Bitmap {
    var target;
    function AsyncImage(target) {
        super.Bitmap();
        this.target = target;
    }
    function onLoaded(meta, async, error, message) {
        if (error) { Debug.message("読み込み失敗: " + message); return; }
        if (target !== null && target isvalid) target.copyFromBitmapToMainImage(this);
    }
}

var img = new AsyncImage(layer);
img.loadAsync("bg.png");    // 完了は onLoaded に通知される
```

!!! warning
    异步加载过程中，访问 [Bitmap.loading](../reference/Bitmap.md#loading) 以外的成员会抛出异常。
    另外，`onLoaded` 被调用时目标 Layer 可能已经失效，因此请像上面的例子那样确认有效性。

### 加工 Layer 的图像并写回

```tjs
var tmp = new Bitmap();
layer.copyToBitmapFromMainImage(tmp);    // 共有されるだけなので速い
ImageFunction.doGrayScale(tmp);          // ここで初めて実体が分離される
ImageFunction.doBoxBlur(tmp, 4, 4);
layer.copyFromBitmapToMainImage(tmp);    // 書き戻し (update が走る)
```

## 参考

- [Layer 类参考文档](../reference/Layer.md)
- [Bitmap 类参考文档](../reference/Bitmap.md)
- [ImageFunction 类参考文档](../reference/ImageFunction.md)
- [BitmapLayerTreeOwner 类参考文档](../reference/BitmapLayerTreeOwner.md)
- [图形系统](GraphicSystem.md) — 图层类型、绘制方式 (`df*`)、运算模式 (`om*`) 的含义
