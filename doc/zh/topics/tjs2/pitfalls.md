# 常见陷阱 (TJS2 / 引擎 API)

这是编写核心演示 (`src/core/data/*`) 时实际踩过的坑的实践笔记。
每一条都属于“不报错、却默默产生不同结果”的类型，
因此整理成可以从症状反查的形式。

---

## TJS2 语言

### 取出字符用 `str[i]`，而 `str[i, 1]` 是另一回事

`str[i, 1]` 会先求值逗号表达式 `(i, 1)`，从而 **总是变成 `str[1]`**。
由于不会报错，直到字符串处理的结果“全部变成同一个字符”时才会察觉。

```tjs
var s = "abcdef";
var c1 = s[2];        // "c"      … 正しい
var c2 = s.charAt(2); // "c"      … 範囲外でも例外にならない版
var c3 = s[2, 1];     // "b" (!)  … カンマ式なので常に s[1]
```

→ [针对字符串的操作](../../tjs2/string.md)

### `Math.floor()` 等返回实数

即使打算取整为整数，类型也仍然是实数，所以进行字符串连接时会输出成
`"1.000000000000000"` 这样。若用于显示或下标，请加上 `(int)`。

```tjs
var n = Math.floor(payload + 0.5);
dm("index = " + n);        // "index = 1.000000000000000"
dm("index = " + (int)n);   // "index = 1"
```

### 匿名函数不会捕获外层的局部变量

TJS2 的函数表达式不是闭包。想从回调中使用的值请放在
**成员变量或 global** 中。

```tjs
function start() {
    var scene = this;                       // これはコールバックから見えない
    var t = new Timer(function() {
        scene.close();                      // → 例外: メンバ "scene" が見つかりません
    }, "");
}
```

```tjs
// メンバ変数にするか、global に置く
global.__scene = this;
var t = new Timer(function() { global.__scene.close(); }, "");
```

### 非数值字符串的 `if` 总是为假

`if("abc")` 不会为真 ( 会被数值化为 0 )。
存在性判断请用 `typeof` 或 `!== void`。

```tjs
if (typeof System.appDataPath != "undefined") { ... }   // 正しい
if (obj.name !== void) { ... }                          // 正しい
```

---

## 图层 / 绘制

### `Layer.visible` 的默认值是 false

只是生成并不会显示。演示中“什么都不显示”的原因大多都是这个。

### `hitType` 只有 `htMask` 和 `htProvince` 两个值

“矩形全面命中”的设置不是 `htRect`，而是 **`hitThreshold = 0`**。

### `drawText` 的颜色是 24bit RGB

请用 `0xRRGGBB` 的 6 位来指定。传入 8 位 ( `0xAARRGGBB` ) 时会被当作系统颜色指定处理，从而意外变成黑色。

### `Layer.invalidate` 不会使子图层无效化

子图层只是“从父图层被切离出来”而继续存活，绘制也会默默成功。
如果要连同整个子树一起丢弃，请递归地 invalidate
( demolib 的 `invalidateLayerTree` 是实现示例 )。

### `operateRect` 的乘法系列需要 `holdAlpha`

`omMultiplicative` 等会把转送目标的 Alpha 置为 0，因此对 `ltAlpha` 图层使用时会变成全黑。
要保留转送目标的话，请指定 `holdAlpha = true`。

### 更新矩形应保持在必要最小限度

如果有不带参数调用 `update()` ( = 全面 ) 的习惯，即使是静止画面也会每帧持续把整个画面转送到 GPU。
只对“要擦除的矩形”“要绘制的矩形”执行 update，转送量就会有数量级的差别
( 实测见核心演示 `perf_stats` / 解说见 `src/core/doc/ScreenTransfer.md` )。

---

## 因构建而存在与否会变化的 API

如果要在 Windows 原生 ( WINVER ) 构建和 SDL3 构建上运行同一个脚本，
下面这些请先用 `typeof` 确认存在再使用。

| API | 状况 |
|---|---|
| `System.appDataPath` / `personalPath` | 2026-08-25 已追加到 SDL3 / 通用构建 ( 在 Windows 上与 WINVER 采用相同的解析 )。在其他 OS 上，从 2026-10 起返回 OS 标准文件夹 ( macOS `~/Library/Application Support/` / Linux `~/.local/share/` 等 ) ( 在此之前是与 `exePath` 相同的值 )。在此之前的引擎的通用构建中没有它，因此要用 `typeof` 确认。保存位置请使用 `System.dataPath` |
| `System.desktopLeft/Top/Width/Height` | 仅限 WINVER。只要分辨率的话可以用 `System.screenWidth/Height` |
| `System.readRegValue` / `writeRegValue` 等 | Windows 扩展。SDL3 构建中没有 ( `urlencode` / `urldecode` / `readEnvValue` / `writeEnvValue` / `expandEnvString` 于 2026-09-28 进入本体，在所有构建中可用 ) |
| `System.setMemoryOverlay` / `setPadOverlay` | 标志在所有构建中通用，但实际进行绘制的是 OGL 系 / SDL 的 DrawDevice ( WINVER 默认的 D3D11 下不会出现 ) |
| `Layer.imeMode` / `setAttentionPoint` | `imeMode` 在 SDL3 上也仅“是否为 `imDisable`”这一点有效 ( 仅在焦点位于其他图层期间接收文本输入 )。开闭与输入模式的细致指定以及 `setAttentionPoint` 有效的只有 WINVER |
| `Window.setZoom` | 2026-08-17 已在两种构建中统一行为 ( 把“图层尺寸 × 倍率”作为窗口的内侧尺寸 )。此前的 WINVER 只会记住倍率，因此如果也要支持旧引擎，请并用 [Window.setInnerSize](../../reference/Window.md#setinnersize) |
| `System.padButtonMapping` | 仅限 SDL3 / 通用构建。WINVER 基于 XInput，按键标识固定为 Xbox 系，因此设置本身并不需要 |
| `Dialog` 系 / `WebServer` | 取决于构建选项 ( `KRKRZ_USE_ELEMENTS` / `KRKRZ_REPL_WEB` ) |

---

## 输入

### 文字输入用 `onKeyPress`，按键用 `onKeyDown`

`onKeyDown` 处理的是虚拟键码，`onKeyPress` 处理的是字符本身 ( 包含 IME 已确定的字符 )。
把想收集字符的处理写在 `onKeyDown` 里就无法取得 IME 输入。

### Elements 面板显示期间，手柄输入会被面板吸走

`VK_PAD*` 会被面板的控件操作 ( 十字键 = 焦点移动 / A = 确定 ) 消费，不会到达游戏侧的 `onKeyDown`。
一定要由游戏接收的按钮，请用 [ElementsDialog.registerHotKey](../../reference/ElementsDialog.md#registerhotkey) 确保，这样会绕过面板
( 核心演示 `pad_advanced` 中有 ON/OFF 的对比 )。

### 摇杆即使无操作也不会变成 0

`System.getPadAxis` 即使无操作也会返回 ±0.05 左右的值。请在游戏侧加入死区处理。

### `Agent.keyPress` 不会产生文字输入事件

注入的只是按键事件 ( 因为字符会经过 OS 的文本输入路径 )。
要在自动测试中输入字符，请使用 Elements 的输入框 + `Agent.text`。

---

## 其他

### `Clipboard.asText` 在没有文本时返回 void

返回的不是空字符串而是 void。请用 `if (v === void)` 判断。

### 不要以插件为前提来组装 JSON

`Scripts.toJSONString` / `evalJSON` 是 json 插件的扩展。想仅用核心功能完成的话，
请手工组装，或者使用 `Dialog.dictToJson` ( Elements 启用时 )。

---

## 相关

- [TJS2 语言规范](../../tjs2/index.md)
- [类参考](../../reference/System.md)
- 核心演示 ( `src/core/data/` ) — 各演示的 `readme.txt` 中，分别写有该演示踩过的注意点
