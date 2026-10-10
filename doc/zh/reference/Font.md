# Font

Font 类是用于管理**字体**的类。

## 成员列表

### 构造函数

- [Font](#font)

### 属性

- [face](#face)
- [height](#height)
- [bold](#bold)
- [italic](#italic)
- [strikeout](#strikeout)
- [underline](#underline)
- [angle](#angle)
- [rasterizer](#rasterizer)
- [emojiMode](#emojimode)
- [weight](#weight)
- [variations](#variations)
- [defaultUseVarStyle](#defaultusevarstyle)
- [defaultEmojiMode](#defaultemojimode)
- [emojiFaceName](#emojifacename)
- [colorEmojiFaceName](#coloremojifacename)
- [defaultFaceName](#defaultfacename)
- [faceIsFileName](#faceisfilename)

### 方法

- [getTextWidth](#gettextwidth)
- [getTextHeight](#gettextheight)
- [getEscWidthX](#getescwidthx)
- [getEscWidthY](#getescwidthy)
- [getEscHeightX](#getescheightx)
- [getEscHeightY](#getescheighty)
- [getGlyphDrawRect](#getglyphdrawrect)
- [getList](#getlist)
- [mapPrerenderedFont](#mapprerenderedfont)
- [unmapPrerenderedFont](#unmapprerenderedfont)
- [addFont](#addfont)
- [registerFontFile](#registerfontfile)
- [queryFonts](#queryfonts)
- [getFontInfo](#getfontinfo)
- [getVarAxes](#getvaraxes)
- [setDefaultVariations](#setdefaultvariations)
- [getDefaultVariations](#getdefaultvariations)

---

### Font

构造函数

**说明**

构造函数

Layer 成员的 font 是向其参数传入 Layer 的特殊版本。
单独使用时，以无参数方式生成。

---

### face

属性 \ 访问: `r/w`

**说明**

字体名

表示字体名。也可以设置值。

可以用逗号分隔来指定多个候选。此时会使用实际存在的字体，写在越前面的越优先。字体是否实际存在，通过参照 OS 的字体列表来判断。与任何候选都不匹配时，会使用默认字体 (当前版本固定为 "ＭＳ Ｐゴシック")。

如果将开头写成逗号、紧接着写字体名，那么即使 OS 未枚举该字体，也会尝试向 OS 指定该字体 (例如 ",My Original Font")。由此，可以使用通过 AddFontResource Win32 API 等注册的、无法枚举的字体。

对于可变字体，可以在字体名后附加 `#tag=val[,tag=val...]` 来指定可变轴实例 (例 `"MyFont#wght=700"`、`"MyFont#wght=700,wdth=75"`)。可以对回退链的每个元素单独指定，与 [variations](#variations) 不同，它以 face 为单位生效。仅在 glyphware 路径 ([Layer.drawShapedText](Layer.md#drawshapedtext) 系与 [rasterizer](#rasterizer) = 2) 下有效。

未附加轴而引用可变字体时，会被规范化为相当于 wght=400 (与 CSS 的 font-weight 默认值相同)。想更改未指定时的默认值时，请使用 [setDefaultVariations](#setdefaultvariations)。

---

### height

属性 \ 访问: `r/w`

**说明**

字体高度

以像素为单位表示所绘制的文字的高度。也可以设置值。

---

### bold

属性 \ 访问: `r/w`

**说明**

粗体

表示是否为粗体 (bold)。也可以设置值。

指定为真时变为粗体。

---

### italic

属性 \ 访问: `r/w`

**说明**

斜体

表示是否为斜体 (italic)。也可以设置值。

指定为真时变为斜体。

---

### strikeout

属性 \ 访问: `r/w`

**说明**

删除线

表示是否绘制删除线。也可以设置值。

指定为真时在文字上绘制删除线。

---

### underline

属性 \ 访问: `r/w`

**说明**

下划线

表示是否绘制下划线 (底线或旁线)。也可以设置值。

指定为真时绘制下划线。

---

### angle

属性 \ 访问: `r/w`

**说明**

文字绘制角度

表示文字绘制角度。也可以设置值。

单位为角度 (degree) 的 10 倍值。取值为 0~3600。

进行竖排时，需要将字体名指定为竖排用字体名，并为此属性指定 2700。

---

### rasterizer

属性 \ 访问: `r/w`

**说明**

字符串绘制方式

表示 [Layer.drawText](Layer.md#drawtext) 所使用的光栅化器 (字符串绘制方式)。也可以设置值。

值为整数索引，编号在**所有构建中通用**:

`**0**` : FreeType 光栅化器 (所有构建均搭载。SDL / 通用构建的默认值)

`**1**` : GDI 光栅化器 (仅 WINVER 搭载。WINVER 的默认值)

`**2**` : glyphware (统一字体引擎。FreeType + HarfBuzz)。不改变默认值，仅在选中时 drawText 的字形生成经由 glyphware (不是内嵌位图，而是轮廓绘制、支持彩色 emoji)。另外，drawText 路径是按 1 个码点逐字的字格步进，**不进行整形** (需要 BiDi / 复杂文字系统的整形时，请使用 [Layer.drawShapedText](Layer.md#drawshapedtext))。

设置该构建未搭载的编号 (例: SDL / 通用构建中设置 1) 时，会回退到 FreeType (0)，读回时会返回回退后的实际值。因此，可以通过“设置后读回、值不一致 = 该光栅化器未搭载”来检测。

指定 FreeType / glyphware 时，仅支持横排。其他方式不支持。

此属性是静态属性。请使用 Font.rasterizer 来设置值。

---

### emojiMode

属性 \ 访问: `r/w`

**说明**

emoji 的绘制模式

表示将相应的码点回退到 emoji 字体来绘制的模式。也可以设置值。

`**-1** ` : 遵循全局默认值 (`Font.defaultEmojiMode`) (默认)

`** 0** ` : 不使用 emoji 字体 (仅原字体)

`** 1** ` : 使用单色 emoji 字体绘制

`** 2** ` : 使用彩色 emoji 字体绘制

此功能仅在使用 FreeType 光栅化器 (`rasterizer` = 0) 时有效。在 GDI 光栅化器 (WINVER 默认) 下没有效果。

emoji 字体已标准内嵌到可执行文件中 (单色 = Noto Emoji，彩色 = Noto Color Emoji)。也可以用 `emojiFaceName` / `colorEmojiFaceName` 与 `addFont` 替换为任意 emoji 字体。

注: 对于 ★ 或 ❤ 等原字体中也拥有字形的码点，可能会优先使用原字体一侧，从而显示为单色。

想按字符单位明确指定时，请在文本中于目标字符之后紧接着添加变体选择符。附加 **VS16** (U+FE0F) 时仅该 1 个字符优先使用 emoji 字体，附加 **VS15** (U+FE0E) 时强制使用原字体 (文本显示)。(例: "❤"+U+FE0F 为彩色、"❤"+U+FE0E 为单色)。不进行无选择符时的自动判定 (Emoji_Presentation 默认) (高级多语言处理不在支持范围内)。

---

### weight

属性 \ 访问: `r/w`

**说明**

字重 (可变字体)

表示字体的字重。也可以设置值。指定 100~900 的数值，或 void (未指定 = 字体默认值)。

对可变字体中拥有 `wght` 轴的 face 作为可变轴生效 (在 [variations](#variations) 中显式指定了 `wght` 时以那里为优先)。

生效的只有 glyphware 路径 — [Layer.drawShapedText](Layer.md#drawshapedtext) 系 (始终) 与 [rasterizer](#rasterizer) = 2 时的 [Layer.drawText](Layer.md#drawtext) —，在旧的 FreeType / GDI 光栅化器下会被忽略 (启动后警告 1 次)。

---

### variations

属性 \ 访问: `r/w`

**说明**

可变轴指定 (可变字体)

以 `"wght=700,wdth=87.5"` 格式指定可变字体的可变轴。也可以设置值。用 void 或空字符串清除。

设置时会被规范化: 标签转为小写、按标签升序排列、同标签后者优先、值被量化 (`wght` 以 1 为步长，其他轴以 0.5 为步长 — 以免轴动画使缓存无限增长)。非法格式会引发异常。

实际会应用的只有“回退链的各 face 实际拥有的同名轴”。可用的轴可以通过 [getVarAxes](#getvaraxes) 查询。适用范围 (仅 glyphware 路径) 与 [weight](#weight) 相同。

---

### defaultUseVarStyle

属性 \ 访问: `r/w`

**说明**

bold / italic 的可变轴映射 (类属性)

设为真时，对于能用可变轴表现 `bold` / `italic` 指定的 face (拥有 `wght` / `slnt` / `ital` 轴的可变字体)，会使用轴 (wght=700 / slnt=-10 / ital=1) 代替合成粗体 / 合成斜体，并为了防止重复应用而禁用合成样式。默认值为假 (为了不改变现有外观)。

轴的有无以回退链开头的 (primary) face 判定。仅在 glyphware 路径下生效。

---

### defaultEmojiMode

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

emoji 绘制模式的全局默认值

获取 / 设置应用于 `emojiMode` 为 -1 的字体的默认 emoji 绘制模式。值与 `emojiMode` 相同 (0 = 不使用 / 1 = 单色 / 2 = 彩色)。此属性是静态属性。

---

### emojiFaceName

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

单色 emoji 回退所使用的 face 名

获取 / 设置在 `emojiMode` = 1 (单色) 时使用的 emoji 字体的 face 名。默认是内嵌的 Noto Emoji ("Noto Emoji Regular")。可以指定通过 `addFont` 注册的任意字体的 face 名。此属性是静态属性。

---

### colorEmojiFaceName

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

彩色 emoji 回退所使用的 face 名

获取 / 设置在 `emojiMode` = 2 (彩色) 时使用的 emoji 字体的 face 名。默认是内嵌的 Noto Color Emoji ("Noto Color Emoji Regular")。彩色 emoji 支持 COLRv0 / CBDT / sbix 格式 (COLRv1 不支持)。此属性是静态属性。

---

### defaultFaceName

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

默认字体的 face 名

获取 / 设置未指定字体时所使用的默认字体的 face 名。作为类静态属性，由所有图层共享。

---

### faceIsFileName

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

是否将 face 名作为文件名处理

设为真时，会把 `face` 属性中指定的名称作为字体文件名打开 (仅在使用 FreeType 时有效)。

注: 在将此标志设为真的图层中启用 IME 时，IME 的输入框会使用 `DEFAULT_GUI_FONT`。

---

### getTextWidth

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要获取宽度的字符串。 |

**返回值**

以像素为单位返回指定字符串的宽度

**说明**

获取字符串的宽度

此方法可以获取以当前字体设置绘制指定字符串时所需的宽度。

**相关:** [Font.getTextHeight](Font.md#gettextheight)

---

### getTextHeight

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要获取高度的字符串。 |

**返回值**

以像素为单位返回指定字符串的高度

**说明**

获取字符串的高度

此方法可以获取以该字体绘制指定字符串时所需的高度。

**相关:** [Font.getTextWidth](Font.md#gettextwidth)

---

### getEscWidthX

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要获取文字横向 X 坐标移动量的字符串。 |

**返回值**

以像素为单位返回文字横向的 X 坐标移动量

**说明**

文字横向的 X 坐标移动量

可以获取以当前字体设置绘制指定文字时所需的文字绘制位置移动量。

此方法可以获取相对于文字绘制方向横向 (左) 前进时，在 X 坐标上的移动量。

**相关:** [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightX](Font.md#getescheightx) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscWidthY

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要获取文字横向 Y 坐标移动量的字符串。 |

**返回值**

以像素为单位返回文字横向的 Y 坐标移动量

**说明**

文字横向的 Y 坐标移动量

可以获取以当前字体设置绘制指定文字时所需的文字绘制位置移动量。

此方法可以获取相对于文字绘制方向横向 (左) 前进时，在 Y 坐标上的移动量。

**相关:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscHeightX](Font.md#getescheightx) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscHeightX

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要获取文字纵向 X 坐标移动量的字符串。 |

**返回值**

以像素为单位返回文字纵向的 X 坐标移动量

**说明**

文字纵向的 X 坐标移动量

可以获取以当前字体设置绘制指定文字时所需的文字绘制位置移动量。

此方法可以获取相对于文字绘制方向纵向 (下) 前进时，在 X 坐标上的移动量。

**相关:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightY](Font.md#getescheighty)

---

### getEscHeightY

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要获取文字纵向 Y 坐标移动量的字符串。 |

**返回值**

以像素为单位返回文字纵向的 Y 坐标移动量

**说明**

文字纵向的 Y 坐标移动量

可以获取以当前字体设置绘制指定文字时所需的文字绘制位置移动量。

此方法可以获取相对于文字绘制方向纵向 (下) 前进时，在 Y 坐标上的移动量。

**相关:** [Font.getEscWidthX](Font.md#getescwidthx) / [Font.getEscWidthY](Font.md#getescwidthy) / [Font.getEscHeightX](Font.md#getescheightx)

---

### getGlyphDrawRect

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 指定要获取范围的字符串。 |

**返回值**

字符串的实际绘制范围

**说明**

字符串的实际绘制范围

可以获取以当前字体设置绘制指定文字时，字形图像被绘制的范围。

得到的范围是以 0,0 坐标为基准的 Rect 类的对象。

仅支持横向。

**相关:** [Rect](Rect.md)

---

### getList

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `flags` | `&nbsp;` | 指定如何枚举字体。<br>请按以下值的按位逻辑或组合指定。<br>`**fsfFixedPitch**    ` : 仅枚举等宽字体<br>`**fsfSameCharSet**   ` : 仅枚举相同字符集的字体<br>`**fsfNoVertical**    ` : 不枚举竖排用字体<br>`**fsfTrueTypeOnly**  ` : 仅枚举 TrueType 字体<br>`**fsfIgnoreSymbol**  ` : 排除符号字符集<br>指定 fsfSameCharSet 时，会枚举与当前选中的字体相同字符集的<br>字体。 |

**返回值**

以字体名 (字符串) 为各元素存储的数组

**说明**

枚举字体名

枚举字体名，并以数组形式返回。

---

### mapPrerenderedFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fontstorage` | `&nbsp;` | 指定预渲染字体存储。 |

**说明**

预渲染字体的分配

对当前选中的字体名进行**预渲染字体**的分配。

此后，对于相同设置的字体，会改为使用指定的预渲染字体。

该设置对所有图层有效。

**相关:** [Font.unmapPrerenderedFont](Font.md#unmapprerenderedfont)

---

### unmapPrerenderedFont

方法

**说明**

解除预渲染字体的分配

解除对当前选中的字体名的**预渲染字体**分配。

**相关:** [Font.mapPrerenderedFont](Font.md#mapprerenderedfont)

---

### addFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 字体文件名 |

**返回值**

以数组返回文件中包含的 face 名。

**说明**

向字体系统添加字体。

---

### registerFontFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 字体文件名 |
| `family` | `&nbsp;` | 要注册的字体名 (省略时立即加载) |

**返回值**

省略 family 时为收录的 face 名数组，指定时为 void

**说明**

注册字体 (支持延迟注册版)。

省略 `family` 时，与 `addFont` 一样立即加载字体文件，并返回收录的 face 名数组。

指定 `family` 时，**不打开文件，仅注册名称** (相当于 `fonts.json` 的 1 个条目的延迟注册)。实际文件会在该名称首次被使用时加载。希望在不让大字体影响启动时间的情况下注册时使用。

---

### queryFonts

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `query` | `&nbsp;` | 检索条件的字典 (可省略) |

**返回值**

匹配的字体信息 (字典) 的数组

**说明**

对已注册字体进行丰富检索。

从 `fonts.json` 声明以及通过 `addFont`/`registerFontFile` 运行时注册的字体中，按排名顺序 (匹配度从高到低) 返回符合条件的 face。检索条件全部可省略，省略的项不构成约束。连参数本身都省略时，返回所有已注册字体。

+ `name` : 字体名 (family / 别名 / fullName / PostScript 名)
+ `weight` : 字重 (100~900，400=Regular / 700=Bold)
+ `slant` : 0=normal, 1=italic, 2=oblique
+ `italic` : 为真则为斜体 (slant 的简易指定)
+ `script` : ISO-15924 文字系统标签 (例 "Jpan" "Hans" "Zsye")
+ `containsText` : 收录了此字符串的全部码点
+ `monospace` : 是否为等宽
+ `color` : 是否为彩色 emoji 字体

返回数组的各元素是与 `getFontInfo` 相同格式的字典。

---

### getFontInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | 字体名或存储路径 |

**返回值**

元数据字典 (无法解析则为 void)

**说明**

获取字体的元数据。

解析字体名 (声明名、SFNT 实名) 或存储路径，返回 SFNT 元数据的字典。无法解析时返回 void。

字典的成员:
+ `key` : 字体键 (存储路径等)
+ `faceIndex` : TTC 内的 face 编号
+ `family` / `subfamily` / `fullName` / `postScriptName` : 名称信息
+ `weight` : 100~900
+ `slant` : 0=normal, 1=italic, 2=oblique
+ `bold` / `color` / `monospace` / `scalable` : 属性 (0/1)

可变字体时还会包含以下内容 (非 VF 时省略):
+ `axes` : 可变轴的数组 (与 [getVarAxes](#getvaraxes) 同格式)
+ `namedInstances` : fvar named instance 的数组
`%[ name : "SemiBold", coords : %[ wght : 600, ... ] ]`

(`queryFonts` 为了保持“不打开字体、按声明值判定”的性质，不返回轴信息。轴请通过本方法或 getVarAxes 获取)

---

### getVarAxes

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | 字体名或存储路径 |

**返回值**

可变轴的数组 (无法解析则为 void)

**说明**

获取可变字体的可变轴列表。

解析字体名 (声明名、SFNT 实名) 或存储路径，以数组返回 fvar 的可变轴。各元素是
`%[ tag : "wght", name : "Weight", min : 300, default : 400, max : 700 ]`
的字典。不是可变字体时为空数组，无法解析时返回 void。

```tjs
var axes = Font.getVarAxes("MyFont");
for (var i = 0; i < axes.count; i++)
Debug.message(axes[i].tag + ": " + axes[i].min + ".." + axes[i].max);
```

---

### setDefaultVariations

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | 字体名或存储路径 (与 face 指定相同写法，不含后缀) |
| `axes` | `&nbsp;` | 默认轴 ("tag=val,..." 格式 / 用 void 或空字符串解除) |

**说明**

注册可变字体的默认轴 (类方法)。

注册在未显式指定轴时按字体名单位补充的默认可变轴。`axes` 为 `"wght=300,wdth=87.5"` 格式。用 void 或空字符串解除。

以未指定 wght 的方式引用可变字体时的默认值相当于 wght=400 (与 CSS 的 font-weight 默认值相同的规则。fvar 默认实例不是 Regular 的字体，在未指定时也会显示为相当于 Regular)。此注册比它更强，而 `#tag=val` 后缀 / [variations](#variations) / [weight](#weight) / fonts.json 的声明轴会更强地胜出。

```tjs
Font.setDefaultVariations("Noto Sans JP", "wght=350");  // 無指定を少し細く
Font.setDefaultVariations("Noto Sans JP", void);        // 解除 (=400 に戻る)
```

---

### getDefaultVariations

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nameOrPath` | `&nbsp;` | 字体名或存储路径 |

**返回值**

已注册的默认轴字符串 (没有则为空字符串)

**说明**

获取 setDefaultVariations 当前的注册值 (类方法)。

---
