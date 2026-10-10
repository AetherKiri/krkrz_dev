# 3D 图形系统

## 概要

吉里吉里Z 在[图形系统](GraphicSystem.md)中说明的常规图层绘制 (BasicDrawDevice / SDLDrawDevice) 之外，还拥有基于 OpenGL ES 的 GPU 绘制路径。该路径以 [OGLDrawDevice](../reference/OGLDrawDevice.md) 为中心，由 [Canvas](../reference/Canvas.md) / [Texture](../reference/Texture.md) / [ShaderProgram](../reference/ShaderProgram.md) / [Offscreen](../reference/Offscreen.md) 等类群构成，可以在 GPU 上直接处理纹理绘制、基于着色器的加工、转场等。

这些 GL 系类仅在 [OGLDrawDevice](../reference/OGLDrawDevice.md) 处于活动状态 (已设置到窗口上) 期间才能工作。这是因为它们绑定在 OGLDrawDevice 管理的 OpenGL 上下文上，在正在使用常规图层绘制设备 (BasicDrawDevice / SDLDrawDevice) 的状态下无法使用。

## 切换到 OGLDrawDevice

要使用 GPU 绘制，需要将 [OGLDrawDevice](../reference/OGLDrawDevice.md) 设置到 [Window.drawDevice](../reference/Window.md#drawdevice) 属性上，以切换绘制设备。

```tjs
var dev = new OGLDrawDevice();
window.drawDevice = dev;
```

刚构造完 OGLDrawDevice 时还不会生成 OpenGL 上下文。在设置到 `Window.drawDevice` 的时点，内部的 OpenGL ES 上下文会被延迟生成并初始化。此初始化以及之后的绘制周期通过以下事件处理。

| 事件 | 触发时机 | 用途 |
|---|---|---|
| [onInit](../reference/OGLDrawDevice.md#oninit) | GL 上下文的生成、初始化完成后立即 | 申请着色器、纹理等初始资源 |
| [onDraw](../reference/OGLDrawDevice.md#ondraw) | 每个绘制周期 | 发出帧绘制命令 |
| [onDone](../reference/OGLDrawDevice.md#ondone) | 分离设备 / 销毁上下文之前 | 释放 onInit 中申请的资源 |

## onDraw 中的绘制处理概要

每一帧的绘制都在 [onDraw](../reference/OGLDrawDevice.md#ondraw) 事件内进行。当 OGLDrawDevice 管理着 [Canvas](../reference/Canvas.md) 时，onDraw 会在内部被 Canvas 的 BeginDrawing ~ EndDrawing 夹住的状态下被调用。因此，在处理器内可以通过设备的 [canvas](../reference/OGLDrawDevice.md#canvas) 属性直接发出 drawTexture 等绘制命令 (不需要自己调用 BeginDrawing / EndDrawing)。

```tjs
class MyGLDevice extends OGLDrawDevice {
    var tex;
    function onInit() {
        tex = new Texture("image.png");   // 初期リソース確保
    }
    function onDraw() {
        canvas.drawTexture(tex);          // BeginDrawing〜EndDrawing の内側
    }
    function onDone() {
        if (tex !== void) invalidate tex; // リソース解放
        tex = void;
    }
}
```

配置与变形通过 Canvas 的 `matrix` ([Matrix32](../reference/Canvas.md) 系) 控制，合成方法通过 `blendMode` 控制。

## 后处理效果 / 裁剪

对 [Canvas](../reference/Canvas.md) 的绘制可以应用在 GPU 内闭环完成的后处理效果 (色调加工、模糊等) 与图像裁剪。其特点是不需要回读 CPU、处理在 GPU 上闭环完成，仅在 [OGLDrawDevice](../reference/OGLDrawDevice.md) 处于活动状态期间工作。

### 后处理效果

```tjs
canvas.beginEffect();
    canvas.drawTexture(tex);        // 捕捉対象 (何を描いてもよい)
canvas.endEffect([
    %[ cmd:"grayscale" ],
    %[ cmd:"gamma", value:1.3 ],
]);
```

把用 `beginEffect()` ~ `endEffect(commands)` 包围的绘制捕获到中间缓冲区 (已清除为透明) 中，依次应用 `commands` (加工命令数组) 后，以当前的 `blendMode` 合成到之前的绘制目标上。可以嵌套。省略 `commands` 时为直通合成。

加工命令大致分为点处理 (独立加工各像素。连续的会由内部融合为 1 个 pass) 与邻域处理 (参照周围像素的模糊)。

```
点処理 (連続すると 1 パスに融合):
  %[ cmd:"grayscale" ]
      グレースケール化  Y = (19*B + 183*G + 54*R) >> 8

  %[ cmd:"gamma", value:γ ]                         // 全チャンネル一括
  %[ cmd:"gamma", rgamma:.., rfloor:.., rceil:..,
                  ggamma:.., gfloor:.., gceil:..,
                  bgamma:.., bfloor:.., bceil:.. ]   // チャンネル別
      ガンマ補正  out = pow(in/255, 1/γ)*(ceil-floor)+floor
      (本体 Layer.adjustGamma 準拠。floor 既定 0 / ceil 既定 255)

  %[ cmd:"light", brightness:b, contrast:c ]
      明度 b(-255〜255) / コントラスト c(-100〜100)

  %[ cmd:"lut", table:[ ...256要素... ] ]
      全チャンネル共通の 256 段ルックアップテーブル

  %[ cmd:"colorize", hue:h, sat:s, blend:b ]
      色相 h(0〜255) / 彩度 s(0〜255) / 合成率 b(0〜1)

  %[ cmd:"modulate", hue:h, saturation:s, luminance:l ]
      色相 h(-180〜180) / 彩度 s(-100〜100) / 輝度 l(-100〜100)

  %[ cmd:"noise", level:n ]
      ノイズ付加 n(0〜255)

  %[ cmd:"generateWhiteNoise" ]
      グレースケールのホワイトノイズ生成 (α は保持)

  %[ cmd:"overcolor", color:0xAARRGGBB, type:mode, opacity:o ]
      指定色での全体塗りつぶし合成 (吉里吉里 fillOperateRect 準拠)。
      合成αは color 上位8bit(AA) × opacity(0〜255, 既定255)。
      type は吉里吉里の合成モード値 (tTVPBlendOperationMode)。

近傍処理 (中間バッファを介して H/V 2 パス):
  %[ cmd:"boxBlur", area:r, iter:n ]
      半径 r の一様ぼかしを n 回 (iter 既定 1)

  %[ cmd:"gaussianBlur", radius:r ]
      半径 r のガウスぼかし
```

各运算对齐吉里吉里引擎本体 ( `TVPDoGrayScale` / `TVPAdjustGamma` ) 或 layerExImage 插件的结果，但以下内容在原理上无法完全一致，目标是视觉上等效。

- `noise` / `generateWhiteNoise` — 由于 CPU 的 `rand()` 序列无法重现，用坐标哈希替代
- `boxBlur` / `gaussianBlur` 的最外周 — CPU 在边缘重新归一化权重，GPU 使用 `CLAMP_TO_EDGE`
- `colorize` — CPU 为整数 HSL 取整，GPU 为同一算法的浮点版本

### 裁剪

矩形裁剪直接使用现有的 `canvas.clipRect` (Rect) + `canvas.enableClipRect`。scissor 在效果 / 遮罩的合成时也会被应用。

基于图像 (任意形状) 的裁剪有 2 种方式。

```tjs
// mask 方式 (どんな描画にも安全)
canvas.beginMaskClip();
    canvas.drawTexture(src);
canvas.endMaskClip(maskTex, 100, 100);   // mask の α を乗算、矩形外は α=0
                                          // mask に void で素通し合成

// stencil 方式 (単純テクスチャ描画専用)
canvas.beginStencilClip(maskTex, 100, 100, 1);  // α 閾値 1〜255
    canvas.drawTexture(src);
canvas.endStencilClip();
```

- `endMaskClip(mask, x, y)` — mask 为 [Texture](../reference/Texture.md) / [Offscreen](../reference/Offscreen.md)。相当于 CPU 版 `Layer.clipAlphaRect` 的第 8 参数 0 (遮罩矩形外侧完全裁剪)。
- `beginStencilClip` 会把遮罩 α 写入模板缓冲并进行裁剪。它会与自行使用模板缓冲的绘制冲突，这种情况下请使用 mask 方式。

### 注意事项

- 着色器为 GLSL ES 3.00。在 GLES2 回退环境 (EGL 2.0 上下文) 中，效果会编译失败并变为直通 (会输出到日志)。遮罩 / 模板裁剪使用的是 ES2 着色器，可以工作。
- 忘记关闭 `beginEffect` / `beginMaskClip` 时，会在 EndDrawing (帧终点) 被丢弃，并输出警告日志。
- Canvas 默认着色器的 `a_opacity` uniform 默认值为 1.0 (在 Canvas 生成时设置)。只有希望设为半透明时才更改 `canvas.defaultShader.a_opacity`。在自定义着色器中声明了 `a_opacity` 时，与以往一样需要自行设置 (未设置的 uniform 为 GL 初始值 0 = 完全透明)。

## 转场绘制 ( drawTransition )

这是 Canvas 的内置功能：将正面 (front) 与背面 (back) 2 张纹理按进度 `phase` 合成并绘制。以着色器内置的方式提供交叉淡化与基于 rule 图像的通用转场。以往在 TJS 层自行生成 [ShaderProgram](../reference/ShaderProgram.md) 实现的转场，可以用 1 个方法替换。

```tjs
// クロスフェード
canvas.drawTransition(front, back, phase);

// ユニバーサルトランジション (rule 画像)
canvas.drawTransition(front, back, phase, ruleTex);        // vague 既定 64
canvas.drawTransition(front, back, phase, ruleTex, 128);   // vague 指定
```

| 参数 | 含义 |
|---|---|
| `front` / `back` | [Texture](../reference/Texture.md) / [Offscreen](../reference/Offscreen.md)。phase=0 时仅 front，1 时仅 back |
| `phase` | 进度 0.0~1.0 (超出范围会被钳制) |
| `rule` | rule 图像纹理。**用 `tcfAlpha` 创建** ( `new Texture("rule.png", tcfAlpha)` )。值越小的像素越早切换到 back。省略 / null 时为交叉淡化 |
| `vague` | 边界模糊宽度 (rule 值尺度 0~255，默认 64) |

- 配置、变形、混合与 `drawTexture` 相同规约 (遵循 `canvas.matrix` / `blendMode` / 裁剪)。
- 通用转场的阈值以 `phase * (1 + vague/255)` 扫描 (phase=1 时所有像素必定为 back)。与[对话框](ElementsDialog.md)的流程画面切换特效 (JSON `transitions` 的 `effect` / `rule` / `vague`) 具有相同语义，可以使用相同的 rule 素材。
- 内置着色器在首次使用时延迟生成并缓存。可以通过 `a_opacity` uniform (默认 1.0) 乘上整体不透明度。

### 使用示例 ( 画面切换 )

```tjs
// onDraw 内: old / cur は Offscreen (旧画面と新画面をそれぞれ描いたもの)
var t = (System.getTickCount() - startTick) / duration;
if (t < 1.0) {
    canvas.drawTransition(oldScreen, curScreen, t, ruleTex, 64);
} else {
    canvas.drawTexture(curScreen);
}
```

## 参考

- [ShaderProgram / 着色器的详细解说 ( multi_platform_design )](https://krkrz.github.io/multi_platform_design/shader_program.html) — 着色器程序的编写方法与设计细节
- [OGLDrawDevice](../reference/OGLDrawDevice.md) — OpenGL ES 绘制设备
- [Canvas](../reference/Canvas.md) — 绘制命令的发出入口
- [ShaderProgram](../reference/ShaderProgram.md) — 着色器程序
- [Texture](../reference/Texture.md) — GPU 纹理
- [Offscreen](../reference/Offscreen.md) — 离屏绘制目标
