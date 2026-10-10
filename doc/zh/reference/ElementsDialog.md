# ElementsDialog

!!! warning "实验中 ( 不在稳定性保证范围内 )"
    这个 API 的形式尚未固定。**有可能在无预告的情况下被更改或删除**
    ( 即使是非兼容更改，主版本号也不会提升 )。
    关于版本提升方式，请参阅 [版本管理](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Versioning.md)。

    基于 Elements 的 UI 机制形式尚未固定。2026-09-04 已将类名本身从 `Dialog` 改名 ( 无兼容别名 )。

ElementsDialog 类是从 TJS 驱动基于 Elements 的通用对话框的类
( 支持 SDL3 / WINVER 两种构建 )。

传入 JSON / JSONC ( 允许注释与末尾逗号 ) 格式的布局定义，
即可显示包含按钮、复选框、开关、文本输入等的对话框。
动作模式有 3 种。

布局定义除了 JSON / JSONC 字符串之外，还可以使用能
直接传入 TJS 的 Dictionary / Array 的 Dict 系方法
( [showDict](#showdict) /
[showModalDict](#showmodaldict) )。

- **非模态 ( 覆盖层显示 )**
用 [showJson](#showjson) / [showFile](#showfile) 显示。显示期间
主循环也不会停止，每当有按钮按下或值更改时 [onAction](#onaction)
会逐次触发。会一直保留到显式调用 [close](#close)，
或对话框侧发生关闭事件为止。
- **阻塞式模态 ( 独立窗口 )**
调用 [showModalJson](#showmodaljson) / [showModalFile](#showmodalfile)
时传入标题 ( 以及宽度、高度 )，会打开新的原生窗口，
在关闭之前停止 TJS 的执行，并以 Dictionary 返回结果。
- **阻塞式模态 ( 叠加到游戏画面 )**
仅用 JSON 1 个参数调用 [showModalJson](#showmodaljson) /
[showModalFile](#showmodalfile) 时，不会打开独立窗口，而是叠加到既有
游戏画面上显示，并在关闭之前阻塞。

也支持驱动迁移多个画面的“流程”。阻塞
执行使用 [showFlow](#showflow) / [showFlowScreens](#showflowscreens)，
非模态 ( 常驻 ) 执行使用 [startFlow](#startflow) /
[startFlowScreens](#startflowscreens)。画面迁移的
时机触发 [onScreen](#onscreen) / [onScreenLeave](#onscreenleave)，
控件操作则依然通知到 [onAction](#onaction)。

非模态对话框可以同时显示多个 ( 带 z-order 叠加
绘制，鼠标进行命中测试，键盘按最前面的 handler 优先
转移焦点 )。将 `grabFocus` 参数指定为假时，
可以作为不获取焦点的常驻 HUD 显示。使用 `showJson(json, true, false)`
( 有焦点的非模态 ) 时可以用键 / 手柄操作面板，
同时未处理的键会放行给宿主；宿主必须接收的键
可以用 [registerHotKey](#registerhotkey) 确保。

JSON 规格的元素类型 ( label / button / input_box / checkbox / toggle /
text_box / text_area / vtile / htile / vspacer / hspacer 等 ) 与属性、
布局密度指定 ( `"gap"` / top-level `"style"` 块 ) 的详情请参阅
[elements_modal 的 README](https://github.com/wamsoft/elements/blob/develop/external/elements_modal/README.md)，
`"input"` 节点进行的键盘 / 手柄操作的设置详情请参阅
[键盘导航规格](https://github.com/wamsoft/elements/blob/develop/docs/keyboard-navigation.md)。

想把正文排入矩形时请使用 `text_area`。折行、行首行尾避头尾、
字符送进与 [Layer.drawShapedTextArea](Layer.md#drawshapedtextarea) 是
相同的逻辑，因此**相同正文、相同宽度时换行位置一致**。
给 `"count_var"` 指定变量名后，通过 [setVar](#setvar) 推进字符送进，
折行已对全文确定，因此送进时不会重排
( 面向字幕或台词窗口。原有的 `text_box` 为兼容而保持原样 )。

当前显示的画面可以被 OS 的屏幕阅读器 ( 讲述人 / VoiceOver / Orca )
朗读。用画面 JSON 的 `"a11y"` 键可以补充名称与角色。绘制到游戏本体
Layer 上的 UI 也可以通过 [setGameA11y](#setgamea11y) / [a11yLayers](#a11ylayers)
载入，用 [announce](#announce) 朗读任意语句。规格的整体请参阅
[无障碍 ( 屏幕阅读器 ) 支持](../specification/accessibility.md)。

用 `KRKRZ_USE_ELEMENTS=OFF` 构建的 exe 无法使用 ElementsDialog 类。
WINVER (Windows 原生 / D3D11) 构建也可以使用 ElementsDialog
( 支持非模态 / overlay 模态 / 独立窗口模态 / 流程 /
文本输入的全部形式 )。

## 成员列表

### 构造函数

- [ElementsDialog](#elementsdialog)

### 属性

- [defaultFontFamily](#defaultfontfamily)
- [active](#active)
- [modalActive](#modalactive)
- [atlasCacheStats](#atlascachestats)
- [atlasCacheBudget](#atlascachebudget)
- [language](#language)
- [watchVars](#watchvars)
- [fontLanguages](#fontlanguages)
- [virtualKeyboard](#virtualkeyboard)
- [hasPhysicalKeyboard](#hasphysicalkeyboard)
- [focusRing](#focusring)
- [baseSize](#basesize)
- [renderScale](#renderscale)
- [renderCache](#rendercache)
- [partialRedraw](#partialredraw)
- [renderCount](#rendercount)
- [renderStats](#renderstats)
- [a11yActive](#a11yactive)
- [a11yMode](#a11ymode)
- [a11yLabel](#a11ylabel)
- [a11yLayers](#a11ylayers)

### 方法

- [showJson](#showjson)
- [showFile](#showfile)
- [showDict](#showdict)
- [showModalJson](#showmodaljson)
- [showModalFile](#showmodalfile)
- [showModalDict](#showmodaldict)
- [dictToJson](#dicttojson)
- [showFlow](#showflow)
- [showFlowScreens](#showflowscreens)
- [startFlow](#startflow)
- [startFlowScreens](#startflowscreens)
- [close](#close)
- [registerFont](#registerfont)
- [registerFontDir](#registerfontdir)
- [registerHotKey](#registerhotkey)
- [unregisterHotKey](#unregisterhotkey)
- [clearHotKeys](#clearhotkeys)
- [beginKeyCapture](#beginkeycapture)
- [endKeyCapture](#endkeycapture)
- [registerImage](#registerimage)
- [unregisterImage](#unregisterimage)
- [clearImages](#clearimages)
- [setSharedVar](#setsharedvar)
- [getSharedVars](#getsharedvars)
- [clearSharedVars](#clearsharedvars)
- [setAtlasImage](#setatlasimage)
- [swappableAtlases](#swappableatlases)
- [setVar](#setvar)
- [getVar](#getvar)
- [listVars](#listvars)
- [focus](#focus)
- [activate](#activate)
- [trimAtlasCache](#trimatlascache)
- [setPadIconBase](#setpadiconbase)
- [setPadTheme](#setpadtheme)
- [setPadIconAlias](#setpadiconalias)
- [renderStatsReset](#renderstatsreset)
- [announce](#announce)
- [setGameA11y](#setgamea11y)
- [clearGameA11y](#cleargamea11y)

### 事件

- [onScreen](#onscreen)
- [onScreenLeave](#onscreenleave)
- [onAction](#onaction)
- [onDrag](#ondrag)
- [onVar](#onvar)
- [onClose](#onclose)
- [onKeyCapture](#onkeycapture)
- [onA11yActiveChanged](#ona11yactivechanged)
- [onGameA11yAction](#ongamea11yaction)

---

### ElementsDialog

构造函数

**说明**

构建 ElementsDialog 对象

构建 ElementsDialog 类的对象。

---

### defaultFontFamily

属性 \ 访问: `r/w`

**类型**: `string`

**说明**

默认字体家族

获取 / 设置应用到 Elements 的 theme 上的 label / button 等默认字体家族
名 ( 逗号分隔 )。值的 getter / setter 都在
Elements 运行时初始化之后 ( 首次显示对话框之后 )
才有意义。

---

### active

属性 \ 访问: `r`

**类型**: `bool`

**说明**

此 ElementsDialog 实例是否处于活动状态 ( 只读 )

用此 ElementsDialog 打开的非模态对话框 / 流程当前处于活动
状态时为真。调用 [close](#close) 之后 teardown 尚未
完成，因此仍为真，teardown 完成后切换为假。

用于“关闭非模态 UI 之后再启动下一个模态对话框”
这类时机控制。

---

### modalActive

属性 \ 访问: `r`

**类型**: `bool`

**说明**

模态对话框是否正在显示 ( 只读 )

[showModalJson](#showmodaljson) 系或模态流程打开的实例只要有
1 个处于活动状态就为真 ( 无论从哪个实例读取，返回的都是进程
整体的状态 )。不包含不获取焦点的常驻覆盖层 ( 字幕、HUD 等 )。

用于最上位热键 ( [System.registerHotKey](System.md#registerhotkey) ) 的
回调中判定“模态显示期间什么都不做、直接放行”。

**相关:** [ElementsDialog.active](ElementsDialog.md#active)

---

### atlasCacheStats

属性 \ 访问: `r/w`

**类型**: `Dictionary`

**说明**

图集的解码缓存的常驻量 ( 只读 )

图集图像以“路径 + 倍率”为键缓存已解码的图像并
反复使用。**即使切换画面也不会放手** — 这是为了
避免长时间游玩导致堆碎片化后取不到大的连续区域、解码失败，
从而组建出没有图像的画面。这是用于在场景分界处
确认到底持有了多少的属性 ( 相当于对类整体生效的 static )。

以字典返回 `bytes` ( RGBA 展开后的总字节数 ) / `count` ( 条目数 ) /
`budget` ( 当前预算 )。

```tjs
var st = global.ElementsDialog.atlasCacheStats;
Debug.message("アトラス常駐 %.1f MB (%d 件)".sprintf(st.bytes / 1048576.0, st.count));
```

**相关:** [ElementsDialog.trimAtlasCache](ElementsDialog.md#trimatlascache)

---

### atlasCacheBudget

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

图集的解码缓存的预算 ( 字节 )

赋值后会**永久**更改，调低时会当场进行裁剪。
设为 0 则缓存无效 ( 每次都重新解码 )。
默认为 192MB，是能够一直容纳 1 个画面的图集的大小
( 相当于对类整体生效的 static )。

**相关:** [ElementsDialog.trimAtlasCache](ElementsDialog.md#trimatlascache)

---

### language

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

i18n 的显示语言

读取画面 JSON 的 top-level `strings` ( textID → 各语言字符串 ) 时的键
( 相当于对类整体生效的 static )。`"ja"` / `"en"` / `"tc"` / `"sc"` 等，
直接指定 `strings` 侧使用的键。

```tjs
global.ElementsDialog.language = "en";     // 表示中の画面もその場で切り替わる
```

赋值后**立即应用到当前显示的所有对话框** ( 持有 `text_id` / `text_list_id` /
`options_id` 的控件会被重新解析，无需重新打开画面即可改变显示 )。
也会成为之后打开画面的默认值。picker 系会保持选择 index 不变，
只替换显示字符串。

读取时返回已设置的语言。未设置时为空字符串 ( = 遵循各画面 JSON 的
`lang` 指定 )。没有 `strings` 的画面不会发生任何变化。

---

### watchVars

属性 \ 访问: `r/w`

**说明**

变量变化通知的对象

用于筛选 / 显式指定通过 [onVar](#onvar) 接收的变量的属性。

- 变量名的数组 ... 仅通知该变量
- `"*"` ... 通知所有变量
- 空数组 ... 不通知 ( 显式停止 )
- void ... 恢复默认值

默认 ( 未设置 ) 是“只要实现了 [onVar](#onvar) 就通知所有变量”。
`"vars_on_hover"` 的变量与拖拽位置每帧都会被改写，因此
只需要特定变量时，列出名字会更轻量。显示中设置也会
立即生效。

---

### fontLanguages

属性 \ 访问: `r/w`

**类型**: `Object`

**说明**

语言联动字体替换表

在按文字系统使用不同字体 ( Noto Sans JP / TC / SC 等 ) 的多语言 UI 中，
用于根据显示语言在字体解析时替换家族的表
( 相当于对类整体生效的 static )。可以按显示语言用符合地区的字形
绘制日中共享码点的汉字。

以语言代码为键，代入持有 `map` ( 家族名或 [registerFont](#registerfont) 的
别名 → 替换目标家族 ) 与 `fallback` ( 任意。该语言下 theme 默认
家族链的排列 ) 的字典 ( 或同形的 JSON 字符串 )。

```tjs
global.ElementsDialog.fontLanguages = %[
"tc" => %[ "map" => %[ "Noto Sans JP" => "Noto Sans TC" ] ],
"sc" => %[ "map" => %[ "Noto Sans JP" => "Noto Sans SC" ] ] ];
global.ElementsDialog.language = "sc";   // 以後 "Noto Sans JP" 指定は SC フォントで描画
```

`map` 会应用到控件的 `"font"` 指定与 theme 默认链的各个家族 token，
`"#tag=val"` 的可变轴后缀会被保留 ( JP/TC/SC 如果是持有相同
轴的可变字体，字重指定就会原样继承 )。应用的语言在有控件的
显式 `"locale"` 时是它，没有时是 [language](#language)。
表中没有条目的语言不会被替换。

与画面 JSON / app.jsonc 的 top-level `"font_languages"` 是同一张表，
会按语言单位合并注册 ( 后设置的按语言覆盖 )。读取时以 JSON 字符串
返回最后代入的表 ( 未设置时为空字符串。不包含画面 JSON 侧的
声明 )。

`text_area` 在构建时确定字体，因此不会跟随显示中的语言切换
( 重新打开画面后会反映 )。

---

### virtualKeyboard

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

内置虚拟键盘的动作模式

指定文本栏 ( `input_box` 等 ) 获得 focus 时，是否用 Elements
内置的英数键盘代替 OS 的软件键盘。可设置的值如下。

| 值 | 含义 |
|---|---|
| `"auto"` | 默认。仅在未连接物理键盘时显示 |
| `"always"` | 即使有物理键盘也始终显示 ( 测试用。桌面环境也会显示 ) |
| `"never"` | 不显示 ( 交给 OS 侧 )。显示中则关闭 |

初始值在有环境变量 `KRKRZ_FORCE_VIRTUAL_KEYBOARD=1` 时为 `"always"`，
没有时为 `"auto"`。

显示的时机是 **Elements 的文本栏获得 focus 时**，游戏侧
自行绘制的输入框不会显示。按键不会积存，而是当场送入
输入目标，因此输入框会实时更新。
当前版本仅支持大写英数字。

可以确认动作的核心演示为 `softkey_ime`。

**相关:** [ElementsDialog.hasPhysicalKeyboard](ElementsDialog.md#hasphysicalkeyboard)

---

### hasPhysicalKeyboard

属性 \ 访问: `r`

**类型**: `Boolean`

**说明**

物理键盘的有无

返回是否连接了物理 ( 硬件 ) 键盘。只读。
桌面环境始终为真，主机等环境则取决于 USB 键盘的连接状态。
用于判断游戏侧是否显示自己的软件键盘。

**相关:** [ElementsDialog.virtualKeyboard](ElementsDialog.md#virtualkeyboard)

---

### focusRing

属性 \ 访问: `r/w`

**类型**: `Boolean`

**说明**

焦点框的显示

Elements 为焦点中的元素绘制的通用框 ( 蓝色圆角 ) 的显示
( 相当于对类整体生效的 static )。默认为 true。

```tjs
global.ElementsDialog.focusRing = false;    // アプリ全体で消す
```

button / slider / dial / thumbwheel 的框会一起消失。持有按状态
区分的图像 ( 普通 / 悬停 / 按下 / 无效 ) 作为素材的图像 UI 中，
通用框会与图像重叠造成妨碍，因此关闭它。**焦点本身仍然有效**，
键 / 手柄导航与切换到 hilite 帧仍照常工作。

这不是画面单位而是整个应用的设置 ( 全局主题的标志 )。

在类内部访问时写作 `global.ElementsDialog.focusRing`。在继承了 ElementsDialog 的
类的方法内直接写 `ElementsDialog` 会成为父类引用，对 static
属性赋值会变成“找不到成员”。

---

### baseSize

属性 \ 访问: `r/w`

**类型**: `Array`

**说明**

UI 的 author 基准面尺寸

以 `[w, h]` 数组指定作为覆盖层显示缩放率 ( fit ) 分母的基准面
尺寸。设置 void ( 或没有元素的数组 ) 会恢复默认 =
游戏基准面 ( primaryLayer 的尺寸 )。未设置时的 getter 为 void。

对以与游戏画面不同分辨率制作 UI 的作品 ( 游戏画面
640x400 / UI 1920x1080 等 ) 设置后，部分面板的缩放会遵照 author 基准，
也不会被游戏侧 primaryLayer 尺寸更改 ( 低分辨率机型的
模拟等 ) 牵连。显示中的画面也会从下一帧起反映。

**相关:** [ElementsDialog.renderScale](ElementsDialog.md#renderscale)

---

### renderScale

属性 \ 访问: `r/w`

**说明**

覆盖层的绘制密度模式

overlay 的绘制密度模式 ( 相当于对类整体生效的 static )。

- 0 ( 默认 ) = auto: 以最终 present 尺寸直接光栅化。
- >0 = authored 逻辑尺寸 × 此倍率绘制，present 时缩放 ( 1.0 = 原尺寸渲染→缩放显示，
2.0 = 相当于 supersampling )。

显示中的画面也会从下一帧起反映 ( 用于比较绘制质量 / 负载 )。

---

### renderCache

属性 \ 访问: `r/w`

**说明**

覆盖层的重新光栅化抑制

为 true ( 默认 ) 期间，无变化的帧会省略对话框的重新光栅化 ( CPU ) 与
纹理重新上传，直接呈现上一次的绘制结果
( 相当于对类整体生效的 static )。空闲时的 CPU 负载会大幅下降。

输入事件、焦点 / 悬停变化、部件演出播放中、setVar 的实际变化、
文本栏插入符闪烁、画面迁移特效中等会自动重新绘制。
设为 false 则照旧每帧重新绘制 ( 用于负载比较 / 问题排查 )。

---

### partialRedraw

属性 \ 访问: `r/w`

**说明**

覆盖层的部分重绘

为 true ( 默认 ) 期间，变化范围能用矩形特定时，**只重新光栅化该矩形**
并部分转送到纹理 ( 相当于对类整体生效的 static )。
能特定矩形的仅限于文本栏插入符闪烁等，输入、焦点
变化、部件演出、setVar 等仍照旧全面重绘。

仅在 [ElementsDialog.renderCache](ElementsDialog.md#rendercache) 有效时工作
( 前提是上一次的绘制结果仍在 )。设为 false 则变化的帧
始终全面重绘 ( 用于负载比较 / 问题排查 )。实际完成部分重绘的
次数可以用 [ElementsDialog.renderStats](ElementsDialog.md#renderstats) 的 "partials" 确认。

---

### renderCount

属性 \ 访问: `r/w`

**说明**

光栅化累计次数 ( 只读 )

实际进行光栅化 ( 重绘 ) 的累计次数 ( 整个类共用 )。
空闲时没有增加就说明 renderCache 在起作用 ( 用于验证 / 负载比较 )。

---

### renderStats

属性 \ 访问: `r/w`

**说明**

绘制管线的区间计测 ( 只读 )

以 Dictionary 返回覆盖层绘制的负载明细 ( 整个类共用的累计值 )。
时间全部为微秒：
%[ "frames" => 呈现帧数, "updates" => 状态更新次数,
"rasters" => 光栅化次数, "partials" => 其中部分重绘的次数,
"cachedPresents" => 省略光栅化的呈现次数,
"presents" => 呈现次数, "totalUs" => 绘制处理总计, "updateUs" => 状态更新,
"rasterUs" => CPU 光栅化, "acquireUs" => 缓冲区获取,
"uploadUs" => 纹理转送, "presentUs" => 呈现 ]

因为是累计值，读取 2 次取差分，与经过的实际时间之比即可计算
“Elements 消耗的时间、比例”
( 用 [ElementsDialog.renderStatsReset](ElementsDialog.md#renderstatsreset) 清零 )。
计测用的基准画面在核心演示 `elements_bench` 中
( 场景切换 + renderCache A/B + 每 500ms 的明细显示 )。

---

### a11yActive

属性 \ 访问: `r`

**类型**: `bool`

**说明**

屏幕阅读器是否已连接 ( 只读 )

OS 的屏幕阅读器等已查询过朗读树则为真
( 整个类共用 )。首次查询时变为真。在 Windows 上
窗口进入前台时会有查询到来，因此刚启动时仍为假。

用于“已连接的话就朗读正文”这类判定时，请不要缓存值，
而是在读取之前查看此属性，或通过
[onA11yActiveChanged](#ona11yactivechanged) 接收。
`KRKRZ_USE_A11Y=OFF` 的构建与 [a11yMode](#a11ymode) 为 `"off"` 时
始终为假。

**相关:** [ElementsDialog.onA11yActiveChanged](ElementsDialog.md#ona11yactivechanged)

---

### a11yMode

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

是否将朗读树输出到 OS

`"auto"` ( 默认 ) 仅在屏幕阅读器连接期间工作。`"off"` 不输出到
OS ( 相当于对类整体生效的 static )。`"off"` 时
[Agent.a11yTree](Agent.md#a11ytree) 等验证用的入口仍可使用。
代入其他字符串会被忽略并输出警告日志。

---

### a11yLabel

属性 \ 访问: `r/w`

**类型**: `String`

**说明**

朗读树的根 ( 窗口 ) 的名称

填入游戏名或场景名 ( 相当于对类整体生效的 static )。为空字符串 ( 默认 ) 时
使用最前面画面的名称 ( 画面 JSON 的 `"a11y"` 的 `title` )。

---

### a11yLayers

属性 \ 访问: `r/w`

**类型**: `bool`

**说明**

自动把 Layer 载入朗读树

设为真后，会从主窗口的 primary layer 向下遍历，添加游戏本体的
节点 ( 默认 false。相当于对类整体生效的 static )。

载入的是以下 Layer。

- 处于焦点链中的 Layer ( `focusable` 且 `joinFocusChain` )。
名称用 `hint`，角色为 button ( `CheckBoxLayer` 为 check_box、
`EditLayer` 为 text_input )
- 持有 `a11yName` 或 `a11yRole` 的 Layer ( 即使不能获取焦点也可以 )
- 绘制着 [ElementsPanel](ElementsPanel.md) 的 Layer ( 面板的部件
排列在其下方，操作也会到达面板 )

`visible` 为假的 Layer 与 `a11yHidden` 为真的 Layer 连子节点
也不会载入。可挂到 Layer 上的成员 ( `a11yName` / `a11yRole` / `a11yValue` /
`a11yDescription` / `a11yStates` / `a11yHidden` / `onA11yAction` ) 请
参阅 [Layer](Layer.md) 的类说明。

可以与 [setGameA11y](#setgamea11y) 并用。排列顺序是 setGameA11y 的节点在前，
焦点也优先使用传给 setGameA11y 的内容。重新读取最多每 150ms 1 次
( 焦点中的 Layer 变化时则立即 )，仅在屏幕阅读器连接期间或
REPL 正在采集朗读日志期间进行。WINVER 上在此期间，空闲时也会
持续轮转 continuous 事件。

**相关:** [ElementsDialog.setGameA11y](ElementsDialog.md#setgamea11y)

---

### showJson

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `json` | `&nbsp;` | 指定 JSON / JSONC 格式的布局定义字符串。 |
| `grabFocus` | `true` | 是否获取键盘焦点 ( 默认 true )。<br>为 true 时面板获取键盘焦点，可以向 input_box 等输入文字，<br>也可以用键 / 手柄操作控件。<br>为 false 时不获取焦点，键输入会传给宿主 ( Window )。<br>用于显示专用的常驻 HUD 式面板。这种情况下无法向面板内的 input_box 等<br>输入文字。鼠标操作与 grabFocus 无关，始终有效。 |
| `modal` | `grabFocus` | 是否设为模态 ( 独占输入 )。省略时出于向后兼容<br>与 grabFocus 取相同值。<br>`showJson(json, true, false)` = “非模态 + 有焦点”的中间状态，<br>键 / 手柄会送达面板并可操作控件 ( 手柄十字键 = 焦点<br>导航 / A = 确定 )，只有面板未处理的键会放行给宿主<br>( [Window.onKeyDown](Window.md#onkeydown) )。操作面板用途<br>推荐使用此指定。宿主必须接收的键请用<br>[registerHotKey](#registerhotkey) 确保。<br>用途 3 态: 模态对话框 `showJson(json)` / 操作面板<br>`showJson(json, true, false)` / 显示专用 HUD `showJson(json, false)`。 |

**返回值**

显示开始成功则返回真。

**说明**

用 JSON 字符串显示非模态对话框

从指定的 JSON / JSONC 格式布局定义构建对话框，
叠加显示到既有游戏画面上。显示期间主循环也不会
停止，每次用户操作都会触发 [onAction](#onaction)。
要结束显示请调用 [close](#close)。

**相关:** [ElementsDialog.showFile](ElementsDialog.md#showfile) / [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey) / [ElementsDialog.onAction](ElementsDialog.md#onaction) / [ElementsDialog.close](ElementsDialog.md#close)

---

### showFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定 JSON / JSONC 文件的路径。 |
| `grabFocus` | `true` | 是否获取键盘焦点 ( 默认 true )。详情参照 [showJson](#showjson)。 |
| `modal` | `grabFocus` | 是否设为模态 ( 省略时跟随 grabFocus )。详情参照 [showJson](#showjson)。 |

**返回值**

显示开始成功则返回真。

**说明**

从文件显示非模态对话框

从指定路径读取 JSON / JSONC 布局定义，以与 [showJson](#showjson)
相同的行为显示。路径可以使用经由 Storages 的路径指定。

**相关:** [ElementsDialog.showJson](ElementsDialog.md#showjson)

---

### showDict

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dict` | `&nbsp;` | 指定布局定义的 Dictionary。 |
| `grabFocus` | `true` | 是否获取键盘焦点 ( 默认 true )。详情参照 [showJson](#showjson)。 |
| `modal` | `grabFocus` | 是否设为模态 ( 省略时跟随 grabFocus )。详情参照 [showJson](#showjson)。 |

**返回值**

显示开始成功则返回真。

**说明**

用 Dictionary 显示非模态对话框

这是 [showJson](#showjson) 的布局不用 JSON 字符串，而是用 TJS 的
Dictionary / Array 直接指定的版本。内部转换为 JSON 后
以相同路径显示 ( 转换规格与 [dictToJson](#dicttojson) 相同 )。

**相关:** [ElementsDialog.showJson](ElementsDialog.md#showjson) / [ElementsDialog.dictToJson](ElementsDialog.md#dicttojson)

---

### showModalJson

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `json` | `&nbsp;` | 指定 JSON / JSONC 格式的布局定义字符串。 |
| `title` | `""` | 指定独立窗口的标题 ( 省略时切换到覆盖层模式 )。 |
| `width` | `800` | 以像素单位指定独立窗口的宽度 ( 默认值 800 )。 |
| `height` | `600` | 以像素单位指定独立窗口的高度 ( 默认值 600 )。 |

**返回值**

返回持有 action 与 values 的 Dictionary。

**说明**

用 JSON 字符串显示模态对话框

从指定的 JSON / JSONC 定义构建对话框，在关闭之前
停止 TJS 的执行并以阻塞方式显示。

- 仅用 JSON 1 个参数调用时，叠加显示到既有游戏画面
( in-game modal )。
- 传入 title 及之后的参数时，打开独立的新原生窗口
显示。

返回值是以下结构的 Dictionary。

%[
action: <閉じた button の id ( Esc / × は "" )>,
values: %[ <id>: <値>, ... ]   // state widget の最終値マップ
]

模态显示期间 [onAction](#onaction) 也会触发，但
关闭对话框的只有在指定了 `"close_on_click": true` 的 button 被按下时
( 以及通过 Esc / × 的中断 )。

**相关:** [ElementsDialog.showModalFile](ElementsDialog.md#showmodalfile) / [ElementsDialog.onAction](ElementsDialog.md#onaction)

---

### showModalFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` | 指定 JSON / JSONC 文件的路径。 |
| `title` | `""` | 指定独立窗口的标题 ( 省略时切换到覆盖层模式 )。 |
| `width` | `800` | 以像素单位指定独立窗口的宽度 ( 默认值 800 )。 |
| `height` | `600` | 以像素单位指定独立窗口的高度 ( 默认值 600 )。 |

**返回值**

返回持有 action 与 values 的 Dictionary。

**说明**

从文件显示模态对话框

从指定路径读取 JSON / JSONC 布局定义，以与 [showModalJson](#showmodaljson)
相同的行为显示。路径可以使用经由 Storages 的路径指定。

**相关:** [ElementsDialog.showModalJson](ElementsDialog.md#showmodaljson)

---

### showModalDict

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dict` | `&nbsp;` | 指定布局定义的 Dictionary。 |
| `title` | `""` | 指定独立窗口的标题 ( 省略时切换到覆盖层模式 )。 |
| `width` | `800` | 以像素单位指定独立窗口的宽度 ( 默认值 800 )。 |
| `height` | `600` | 以像素单位指定独立窗口的高度 ( 默认值 600 )。 |

**返回值**

返回持有 action 与 values 的 Dictionary。

**说明**

用 Dictionary 显示模态对话框

这是 [showModalJson](#showmodaljson) 的布局用 TJS 的 Dictionary /
Array 直接指定的版本。用 1 个参数调用时以覆盖层显示、传入
title 及之后的参数时以独立窗口显示的这一点，以及返回值的格式，
都与 [showModalJson](#showmodaljson) 相同。

**相关:** [ElementsDialog.showModalJson](ElementsDialog.md#showmodaljson) / [ElementsDialog.showDict](ElementsDialog.md#showdict)

---

### dictToJson

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `value` | `&nbsp;` | 指定要转换的值 ( Dictionary / Array / 基本类型 )。 |

**返回值**

返回 JSON 字符串。

**说明**

将 Dictionary / Array 转换为 JSON 字符串

原样调用 [showDict](#showdict) / [showModalDict](#showmodaldict) 内部
进行的转换的工具。可用于把用 Dictionary 组装的
布局保存为 JSON 素材、确认转换结果等
用途。无需创建实例，可以按 `ElementsDialog.dictToJson(...)`
的形式调用。

对应的值类型为 void / Integer / Real / String / Dictionary / Array。
除此之外 ( Octet 或一般对象、循环引用、非有限实数 )
会抛出异常。

**相关:** [ElementsDialog.showDict](ElementsDialog.md#showdict)

---

### showFlow

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `manifestPath` | `&nbsp;` | 指定 app.jsonc 清单的 Storages 路径。 |

**返回值**

返回持有 action 与 values 的 Dictionary。

**说明**

从清单以阻塞方式显示多画面流程

读取 `app.jsonc` 格式的清单 ( 经由 Storages 的路径指定 )，
在既有游戏画面上以覆盖层执行包含多个画面迁移的流程。
直到流程结束为止停止 TJS 的执行，最后返回关闭画面的 Dictionary
`%[ action, values ]`。

每当画面切换时 [onScreen](#onscreen) / [onScreenLeave](#onscreenleave)、
各控件的操作会触发 [onAction](#onaction)。

将画面 JSON 的 `transitions` 条目写成 object 形式，即可声明画面切换时的
过渡特效 ( `effect: "fade"` = 交叉淡入淡出 /
`effect: "universal"` = 基于 rule 图像的通用转场。
`duration` = 所需 ms ( 省略时 200 )，universal 还会追加 `rule` =
rule 图像路径 ( 从声明画面起的相对路径 / Storages 路径 / autopath 检索 )、
`vague` = 边界模糊宽度 0~255 ( 省略时 64 ) )。

```json
"transitions": {
"next": { "target": "s2", "effect": "fade", "duration": 300 },
"back": { "target": "<back>", "effect": "universal",
"rule": "rule.png", "vague": 64, "duration": 500 }
}
```

**相关:** [ElementsDialog.showFlowScreens](ElementsDialog.md#showflowscreens) / [ElementsDialog.startFlow](ElementsDialog.md#startflow)

---

### showFlowScreens

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `screensDict` | `&nbsp;` | 将画面名 ( 字符串 ) 映射到布局定义 ( JSON 字符串，或 Dictionary / Array ) 的 Dictionary。两种形式可以混用。 |
| `entry` | `&nbsp;` | 指定起点画面名 ( screensDict 的键 )。 |

**返回值**

返回持有 action 与 values 的 Dictionary。

**说明**

从内联定义以阻塞方式显示多画面流程

不经过文件 I/O，用 Dictionary 传入画面名 → 布局定义来
执行流程的 [showFlow](#showflow) 内联版。
行为与返回值与 [showFlow](#showflow) 相同。

**相关:** [ElementsDialog.showFlow](ElementsDialog.md#showflow) / [ElementsDialog.startFlowScreens](ElementsDialog.md#startflowscreens)

---

### startFlow

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `manifestPath` | `&nbsp;` | 指定 app.jsonc 清单的 Storages 路径。 |
| `grabFocus` | `true` | 为真时获取键盘 / 手柄焦点 ( 默认值 真 )。指定为假时作为不获取焦点的常驻 HUD 显示。 |

**返回值**

开始成功则返回真。

**说明**

开始非模态 ( 常驻 ) 多画面流程

以非模态 ( 非阻塞 ) 开始与 [showFlow](#showflow) 相同的清单，
并立即返回。可以在游戏画面上一直显示并推进，
适合主菜单或 HUD 这样的常驻 UI。

画面迁移由 JSON 侧的 `transitions` 定义进行。以按钮按下等为起点
在 TJS 侧处理时，请用未指定 `"close_on_click"` 的 button 的
[onAction](#onaction) 进行分流。显式结束请调用
[close](#close)，teardown 是否完成可以用
[active](#active) 判别。

**相关:** [ElementsDialog.startFlowScreens](ElementsDialog.md#startflowscreens) / [ElementsDialog.showFlow](ElementsDialog.md#showflow) / [ElementsDialog.active](ElementsDialog.md#active)

---

### startFlowScreens

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `screensDict` | `&nbsp;` | 将画面名 ( 字符串 ) 映射到 JSON 字符串的 Dictionary。 |
| `entry` | `&nbsp;` | 指定起点画面名 ( screensDict 的键 )。 |
| `grabFocus` | `true` | 为真时获取键盘 / 手柄焦点 ( 默认值 真 )。指定为假时作为不获取焦点的常驻 HUD 显示。 |

**返回值**

开始成功则返回真。

**说明**

从内联定义开始非模态 ( 常驻 ) 多画面流程

以非模态 ( 非阻塞 ) 开始与 [showFlowScreens](#showflowscreens) 相同的
Dictionary 形式画面定义的 [startFlow](#startflow)
内联版。

**相关:** [ElementsDialog.startFlow](ElementsDialog.md#startflow) / [ElementsDialog.showFlowScreens](ElementsDialog.md#showflowscreens)

---

### close

方法

**说明**

关闭对话框

关闭此实例打开的非模态 / 模态对话框 ( 含流程 )。
不会关闭其他实例打开的对话框。

内部 teardown 会在下一帧进行，因此调用 close 之后
一段时间内 [active](#active) 仍为真。想安全启动下一个模态时，
请等待 [active](#active) 变为假。

画面内元素带有 `"animate"` 的 `"on": "exit"` 指定 ( 退场演出 ) 时，
close 也会播放退场演出，完成后再关闭 ( 期间
[active](#active) 仍为真 )。流程执行中的 close 不会解析画面迁移
( transitions )，而是连同整个流程一起结束。

**相关:** [ElementsDialog.active](ElementsDialog.md#active)

---

### registerFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `family` | `&nbsp;` | 指定注册时使用的家族名。 |
| `path` | `&nbsp;` | 指定字体文件 ( .ttf / .otf ) 的 Storages 路径。 |
| `weight` | `40` | 指定 weight 值 ( 默认值 40 = normal )。 |
| `slant` | `0` | 指定 slant 值 ( 默认值 0 = normal )。 |
| `stretch` | `50` | 指定 stretch 值 ( 默认值 50 = normal )。 |

**返回值**

实际注册的 family 名 ( 优先 ThorVG embedded )。

**说明**

注册 Elements 用字体

经由 krkrz Storages 注册 Elements 对话框使用的字体。
返回 ThorVG 从文件读取到的 embedded family 名 ( 未取到时
为空字符串 )。脚本可以查看该返回值，用于向主题组装或
日志显示。

weight / slant / stretch 是 font_constants 的整数值 ( 详情
参照 `StoragesResourceLoader.h` )。

**相关:** [ElementsDialog.registerFontDir](ElementsDialog.md#registerfontdir)

---

### registerFontDir

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | 指定注册对象目录的 Storages 路径。 |

**返回值**

返回成功注册的字体数量。0 = 一本都没注册成功
( 没有目录 / 没有字体 )。不会抛出异常，
而是输出警告日志。

**说明**

批量注册 Elements 用字体

枚举并注册指定目录下的所有 .ttf / .otf ( 从文件
名推测 family / weight / slant / stretch )。dir 使用经由 Storages 的
路径指定，可以使用相对路径 ( "font/" )，也可以使用 `System.exePath + "data/font/"`
这样的规范化路径。指向 XP3 内的目录时请像
`"data.xp3>font/"` 这样显式指定归档
( 仅用 addAutoPath 挂载的话无法枚举目录 )。
直接传入 OS 路径 ( "D:/foo/font/" ) 会得到 0 本。

**相关:** [ElementsDialog.registerFont](ElementsDialog.md#registerfont)

---

### registerHotKey

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 虚拟键码 ( VK_ESCAPE 等 )。除键之外，手柄按钮<br>( VK_PAD1 ~ VK_PAD12 等 ) 与鼠标按钮 ( VK_LBUTTON / VK_RBUTTON /<br>VK_MBUTTON / VK_XBUTTON1 / VK_XBUTTON2 ) 也可以在同一空间指定。<br>不推荐注册可打印键 ( 到 onKeyPress 的字符事件为止<br>不会被抑制 )。 |
| `shift` | `0` | 修饰键的组合 ( ssShift \| ssAlt \| ssCtrl，默认 0 )。<br>键 down 以完全一致判定，up 仅以键的一致成对绕过。 |
| `duringTextInput` | `false` | 为真时，对话框内的文本输入控件<br>( input_box 等 ) 有插入符期间也有效。默认的假在<br>文本输入中会被抑制，不会从输入栏夺走 ESC / BackSpace 等。 |

**返回值**

没有返回值。相同 ( key, shift ) 的重新注册会
覆盖 duringTextInput。

**说明**

宿主热键的注册

这是“在把焦点交给对话框的同时，特定键一定要由宿主侧
接收”的绕过机制。注册的键不会交给对话框，
而是直接送往通常的游戏输入路径
( [Window.onKeyDown](Window.md#onkeydown) /
[Window.onMouseDown](Window.md#onmousedown) 等 )
( 没有专用事件 )。

输入的配送优先顺序如下一列。

1. 模态对话框 ( 独占全部输入。优先于热键 )
2. 宿主热键 ( 绕过对话框直达宿主 )
3. 持有焦点的非模态面板 ( 只放行未处理的键 )
4. 游戏 / 图层

设想用于在包含 slider 等的操作面板 ( `showJson(json, true, false)` )
显示期间，也让 ESC 的场景返回或 PageUp/Down 的画面切换
确实生效的用途。

**相关:** [ElementsDialog.unregisterHotKey](ElementsDialog.md#unregisterhotkey) / [ElementsDialog.clearHotKeys](ElementsDialog.md#clearhotkeys) / [ElementsDialog.showJson](ElementsDialog.md#showjson)

---

### unregisterHotKey

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | 指定虚拟键码。 |
| `shift` | `0` | 修饰键的组合 ( 默认 0 )。 |

**说明**

解除宿主热键

解除用 [registerHotKey](#registerhotkey) 注册的热键
( 删除 key 与 shift 都一致的条目 )。

**相关:** [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey)

---

### clearHotKeys

方法

**说明**

解除全部宿主热键

解除用 [registerHotKey](#registerhotkey) 注册的全部热键。

**相关:** [ElementsDialog.registerHotKey](ElementsDialog.md#registerhotkey)

---

### beginKeyCapture

方法

**返回值**

能开始捕获则返回真。对话框未显示 ( 未活动 ) 时返回假。

**说明**

开始键捕获

这是“原样接收下一个被按下的键”的方法。用于像按键分配设置画面中
显示“请按下要分配的键”时那样，不让键用于控件操作
( 焦点移动、确定、Esc 关闭等 )，而是想在 TJS 中判定的场景。

捕获中的对话框持有键盘焦点期间，所有的键按下都会
送达 [onKeyCapture](#onkeycapture)，不会传给控件。

- 即使在模态上，也优先于用 [registerHotKey](#registerhotkey) 注册的键。
但 [System.registerHotKey](System.md#registerhotkey) 的最上位热键
会先起作用。
- Shift / Ctrl / Alt 的单按、手柄按钮 ( `VK_PAD*` )、
自动重复 ( 带 `ssRepeat` ) 也会送达。是否忽略重复由接收方决定。
- 左键以外的鼠标按钮 ( 右 / 中 / X ) 的按下也会以 `VK_RBUTTON` 等送达
( 例如右键取消 )。左键照常送达控件。
- 松开键时的事件与文字输入在捕获期间会被丢弃。
- 即使按住捕获的键结束捕获 ( 或关闭对话框 )，重复也不会
泄漏到背面的画面。

调用 [endKeyCapture](#endkeycapture) 或关闭对话框后捕获结束。

在设置画面上以模态叠加只有说明文字的对话框，在该对话框中
捕获是典型用法。从 [onKeyCapture](#onkeycapture) 中调用
[close](#close) 也没有问题。

```tjs
var dlg = new ElementsDialog();
dlg.onKeyCapture = function(key, shift) {
if (shift & ssRepeat) return;          // リピートは無視
if (key == VK_RBUTTON) { close(); return; }   // 右クリックで取り消し
assignKey(key);
close();
} incontextof dlg;
dlg.showJson(promptJson);
dlg.beginKeyCapture();
```

**相关:** [ElementsDialog.endKeyCapture](ElementsDialog.md#endkeycapture) / [ElementsDialog.onKeyCapture](ElementsDialog.md#onkeycapture)

---

### endKeyCapture

方法

**返回值**

能结束则返回真。对话框未显示 ( 未活动 ) 时返回假。

**说明**

结束键捕获

结束用 [beginKeyCapture](#beginkeycapture) 开始的捕获。关闭对话框时
会自动结束，因此无需调用。

**相关:** [ElementsDialog.beginKeyCapture](ElementsDialog.md#beginkeycapture)

---

### registerImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 存储上的名称 ( 用 `mem://<name>` 引用 )。 |
| `path` | `&nbsp;` | 要注册的图像的统一存储路径。 |

**返回值**

是否成功读取、注册。

**说明**

注册运行时图像

把统一存储路径 path 的文件以 name 注册到运行时图像存储。从 jsonc 的
image 控件等用 `"mem://<name>"` 引用。这是用于把存档缩略图等运行时
变化的图像交给 Elements 的机制。显示中的画面如果有 `mem://<name>` 的
image 控件，重新注册时就会重新解码并立即反映
( 无需重新打开画面。面板也会反映 )。注册前 build 的
控件会保持空显示，因此首次请在打开画面之前注册。

---

### unregisterImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 要删除的图像的名称。 |

**说明**

删除运行时图像

从运行时图像存储删除用 [registerImage](#registerimage) 注册的 name。

---

### clearImages

方法

**说明**

清除所有运行时图像

清空运行时图像存储。

---

### setSharedVar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变量名。 |
| `value` | `&nbsp;` | 设置的值 ( 字符串 )。 |

**说明**

改写会话共享变量

改写画面 JSON 的 `"shared_vars"` 声明的“跨画面保持的变量”。
变量 store 每个画面都会重新创建，但符合 `"shared_vars"` 模式
( 完全一致，或末尾 `*` 的前缀一致 ) 的变量会与会话共享存储
双向连接，并继承到下一个打开的画面。画面未构建也可以写入。

要携带哪些值由画面侧决定，因此宿主实现不需要做什么，
但在将数据写入游戏存档 / 读取后灌入时使用此方法。

---

### getSharedVars

方法

**返回值**

变量名 => 值的字典数组。

**说明**

获取所有会话共享变量

以字典数组 ( 变量名 => 值 ) 返回会话共享变量的当前值。设想用于
写入存档。值为字符串。

会进入共享侧的只有“作为变化写入”的值，控件的初始值
( `"initial"` / `"value"` ) 不会出现。这是为了避免“谁都没碰过的项目”
被首次打开画面的默认值固定下来。

---

### clearSharedVars

方法

**说明**

丢弃所有会话共享变量

清空会话共享存储。在返回标题时、即将载入存档
之前等场合调用。

---

### setAtlasImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 画面 JSON 中声明的图集名。 |
| `path` | `&nbsp;` | 替换图像的路径 ( 以画面的 `resource_base` 为起点 )。 |

**返回值**

是否完成替换 ( 未声明 / 读取失败时为 false。显示不会改变 )。

**说明**

替换可替换图集的图像

把画面 JSON 的 `"atlases"` 中声明了 `"swappable": true` 的图集图像
在运行时替换为另一张。控件不会重新创建，因此布局与
焦点都保持原样。适用于像 CG 鉴赏的分组标签那样“同一画面、
不同图组”的切换用途。

替换目标必须具有**相同的矩形划分**。控件持有的
frames / rect 不会改变，因此图像位置错开就会显示别的图像。

---

### swappableAtlases

方法

**返回值**

图集名的数组。

**说明**

获取可替换的图集名列表

以数组返回当前可以用 [setAtlasImage](#setatlasimage) 替换的图集名。
用于验证面板或 REPL 确认。

---

### setVar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变量名。 |
| `value` | `&nbsp;` | 设置的值 ( 字符串 )。 |

**返回值**

是否成功写入。

**说明**

改写显示中对话框的变量

向显示中对话框的变量 store 写入值。JSON 中指定了 `"text_var": name` 的
label 等会在下一帧更新。自己的实例非活动时返回 false。

---

### getVar

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变量名。 |

**返回值**

变量的值 ( 字符串 )。未知变量则为 void。

**说明**

读取显示中对话框的变量

从显示中对话框的变量 store 读取值。不仅是用 [setVar](#setvar)
写入的值，画面侧写入的值 ( `"vars_on_hover"` /
`"vars_on_focus"` / slider 的 `"value_var"` / `"drag_at_var"` /
列表的 `"index_offset_var"` 等 ) 也可以从同一 store 读取。

未知的变量名，或自己的实例非活动时返回 void
( 可以与空字符串区分 )。想在变化的时点获知请实现
[onVar](#onvar)。

---

### listVars

方法

**返回值**

变量描述 Dictionary 的数组。非活动时为空数组。

**说明**

获取显示中对话框的变量列表

以按名称排序的数组返回显示中对话框使用的变量。元素是
持有 `name` / `value` / `usedBy` 的 Dictionary，`usedBy` 是
持有 `id` ( 最近的祖先控件 id ) 与 `kind` ( 引用的 JSON
键。`"text_var"` / `"visible_var"` / `"value_var"` 等 ) 的
Dictionary 的数组。

仅有引用而从未被写入的变量，反之没有引用但用
[setVar](#setvar) 创建的变量也会载入。用于调试面板或画面 JSON 的
验证。

---

### focus

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 要转移焦点的控件 id。 |

**返回值**

是否成功委托。非活动时返回 false。

**说明**

把焦点移到指定 id 的控件

把焦点移到显示中对话框的控件 ( 由 JSON 的 `"id"` 指定 )。
input_box 会变为编辑焦点 ( 显示插入符 + 接收文本 )。
设想用于 `at_var` 的 park / unpark 等重新组装画面之后，
显式转移输入目标的用途。

返回值是“是否成功向实例委托了焦点移动”，不确认 id 是否
存在。自己的实例非活动时返回 false。

---

### activate

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 要执行的控件 id。 |

**返回值**

是否成功执行。id 未知 / 非活动时返回 false。

**说明**

执行指定 id 的控件

把焦点移到显示中对话框的控件 ( 由 JSON 的 `"id"` 指定 ) 并
执行 ( 相当于 Enter )。这是 [Agent.dialogClick](Agent.md#dialogclick) 的
实例版，与 [ElementsPanel.activate](ElementsPanel.md#activate)
同形。

**相关:** [ElementsDialog.focus](ElementsDialog.md#focus)

---

### trimAtlasCache

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `budget` | `&nbsp;` | 裁剪上限 ( 字节 )。0 / 省略时释放所有未使用的部分。 |

**返回值**

成功释放的字节数。

**说明**

裁剪图集的解码缓存

把图集的解码缓存裁剪到 `budget` 字节。
传入 0 ( 默认 ) 会放手“所有未使用的部分”。
返回值是成功释放的字节数。

⚠ **显示中的画面正在使用的图集由于仍有引用，无法被丢弃。**
请在场景的分界 ( 关闭画面之后 ) 调用。

```tjs
dlg.close();
var freed = global.ElementsDialog.trimAtlasCache();   // 使っていない分を全部
```

预算本身不会改变 ( 临时裁剪 )。想永久调低时请向
[atlasCacheBudget](#atlascachebudget) 赋值。

**相关:** [ElementsDialog.atlasCacheStats](ElementsDialog.md#atlascachestats)

---

### setPadIconBase

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dir` | `&nbsp;` | pad_icon 素材的基础目录 ( 统一存储路径 )。 |

**说明**

设置 pad_icon 的基础目录

设置 pad_icon ( Kenney input prompts ) 的基础目录。dir 是统一存储
路径 ( XP3 内也可 )。设想其下有 xbox/ps/switch/keyboard 各目录 + vector/*.svg 的
结构。未设置时 pad_icon 会变成灰色占位符。

---

### setPadTheme

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 主题名。 |

**返回值**

是否能解释名称。

**说明**

设置 pad_icon 的整体主题

设置 pad_icon 的整体主题 ( `"xbox"` / `"ps"` / `"switch"` / `"keyboard"` / `"none"` )。
指定 `"auto"` 时会从连接的手柄的系列
( [System.padStyle](System.md#padstyle) ) 自动选择主题。无法
判定系列的平台 ( Windows 等 ) 上，只要有 1 个手柄
连接就用 `"xbox"`，1 个都没有则用 `"keyboard"`
( 因为没有手柄时显示手柄图像也不知道能按哪些键 )。

`"auto"` 的判定会监视手柄的连接数与系列，
**在变化时当场重新决定**。插拔控制器无需重新打开画面，
显示中画面的 pad_icon 也会在下次绘制时替换为新主题的图像。
画面 JSON 的 top-level `"pad_theme"` 有指定时以那边优先。

**相关:** [ElementsDialog.setPadIconAlias](ElementsDialog.md#setpadiconalias)

---

### setPadIconAlias

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `theme` | `&nbsp;` | 对象的主题名 ( `"xbox"` / `"ps"` / `"switch"` / `"keyboard"` )。 |
| `name` | `&nbsp;` | 要覆盖的逻辑名。空字符串则解除该主题的全部覆盖。 |
| `basename` | `&nbsp;` | 要分配的素材 basename。空字符串 / 省略则解除该名称的覆盖。 |

**返回值**

是否能解释主题名。

**说明**

按主题单位覆盖 pad_icon 的名称解析

按主题单位覆盖 pad_icon 的逻辑名 ( `"a"` / `"b"` / `"dpad"` 等 ) 到实际素材
文件名 ( Kenney pack 的 basename ) 的对应表。默认表
( `"a"` = Enter / `"b"` = Esc / `"dpad"` = 箭头 … ) 与作品实际的按键
分配不同时使用。

```tjs
// キャンセルが Esc ではなく BackSpace のタイトル
global.ElementsDialog.setPadIconAlias("keyboard", "b", "keyboard_backspace");
```

覆盖优先于默认表。给 basename 传空字符串只解除该名称的覆盖，
给 name 传空字符串则解除该主题的全部覆盖。两者都会
从下次绘制起反映到显示中的画面。

**相关:** [ElementsDialog.setPadTheme](ElementsDialog.md#setpadtheme)

---

### renderStatsReset

方法

**说明**

重置绘制计测计数器

把 [ElementsDialog.renderStats](ElementsDialog.md#renderstats) 的累计计数器清零。
在计测区间开始时调用。

---

### announce

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `text` | `&nbsp;` | 要朗读的字符串。 |
| `assertive` | `false` | 为真则指定打断 ( 默认 false )。实际如何处理<br>取决于屏幕阅读器。 |

**说明**

让屏幕阅读器朗读

让屏幕阅读器朗读 text ( 相当于对类整体生效的 static )。
会进入最前面对话框的 live region，1 个对话框都没有时
进入游戏本体的 live region。连续传入相同的句子也每次都会朗读。

屏幕阅读器未连接时也接受 ( 连接时会传入最新的状态 )。
REPL 运行中还会保留到朗读日志 ( [Agent.a11yLog](Agent.md#a11ylog) ) 中。

```tjs
global.ElementsDialog.announce("セーブしました");
global.ElementsDialog.announce("体力が残りわずかです", true);   // 割り込み
```

规格的整体请参阅 [无障碍 ( 屏幕阅读器 ) 支持](../specification/accessibility.md)。

**相关:** [ElementsDialog.a11yActive](ElementsDialog.md#a11yactive)

---

### setGameA11y

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `nodes` | `&nbsp;` | 节点的字典的数组。 |
| `focus` | `&nbsp;` | 放置焦点的节点的 `id` ( 省略则无 )。 |

**说明**

把游戏本体的 UI 载入朗读树

绘制到 Layer 上的选项、菜单、设置画面等在 Elements 之外，因此
从脚本传入节点的表，载入朗读树 ( 相当于对类整体生效的
static )。每次调用都会替换整张表 ( 差分由本体计算 )。

```tjs
global.ElementsDialog.setGameA11y([
%[ id:"choices", role:"list", name:"選択肢" ],
%[ id:"c1", role:"list_item", name:"北へ行く", parent:"choices", rect:[100,400,600,48] ],
%[ id:"c2", role:"list_item", name:"南へ行く", parent:"choices", rect:[100,460,600,48] ],
%[ id:"vol", role:"slider", name:"音量", value:"50%", num_value:50, num_min:0, num_max:100 ],
], "c1");
```

节点的字典的键:

- `id` ... 必需。唯一的字符串。为空或重复的节点会输出日志并跳过
- `role` ... `button` / `toggle_button` / `check_box` / `radio_button` / `tab` /
`menu_item` / `list` / `list_item` / `slider` / `spin_button` / `text_input` /
`label` / `heading` / `image` / `status` / `group` ( 省略与未知值均为 group )
- `name` / `value` / `description` ... 名称 / 值 / 补充说明
- `states` ... 数组或 `"focusable,checked"` 形式。`focusable` / `disabled` /
`checked` / `selected` / `expanded` / `read_only`
- `rect` ... primary layer 的坐标 `[x, y, w, h]`。省略时则为包围子节点的矩形。
窗口的缩放与黑边由本体换算
- `parent` ... 父节点的 `id`。省略则为最上位
- `num_value` / `num_min` / `num_max` / `num_step` ... slider / spin_button 的数值

游戏本体的节点排列在对话框之下，模态对话框显示期间会
隐藏。来自屏幕阅读器的操作会送达
[onGameA11yAction](#ongamea11yaction)。本体不会自己
移动焦点或值，因此请在脚本更改游戏状态之后再
重新调用 `setGameA11y`。仅以主窗口为对象。

**相关:** [ElementsDialog.clearGameA11y](ElementsDialog.md#cleargamea11y) / [ElementsDialog.a11yLayers](ElementsDialog.md#a11ylayers)

---

### clearGameA11y

方法

**说明**

移除所有游戏本体的节点

移除用 [setGameA11y](#setgamea11y) 载入的所有节点。游戏本体的
框架与 [announce](#announce) 使用的 live region 会保留。

---

### onScreen

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 进入的画面的名称 ( 清单的画面键 ) 。 |

**说明**

流程画面迁移通知 ( 进入画面 )

在用 [showFlow](#showflow) / [startFlow](#startflow) 系执行的
流程进入画面时触发。请在 TJS 侧重写。

**相关:** [ElementsDialog.onScreenLeave](ElementsDialog.md#onscreenleave)

---

### onScreenLeave

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 离开的画面的名称 ( 清单的画面键 ) 。 |
| `action` | `&nbsp;` | 成为离开画面契机的 button 的 id ( Esc / × 为空字符串 ) 。 |

**说明**

流程画面迁移通知 ( 离开画面 )

在用 [showFlow](#showflow) / [startFlow](#startflow) 系执行的
流程离开画面时触发。请在 TJS 侧重写。

**相关:** [ElementsDialog.onScreen](ElementsDialog.md#onscreen)

---

### onAction

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 发生源控件的 id 字符串。 |
| `payload` | `&nbsp;` | 控件伴随传递的值 ( 见上文 )。 |

**说明**

对话框上的操作通知

接收对话框上发生的操作 ( button click 或 state 控件的值
变化 ) 的事件。请在 TJS 侧重写。

非模态 ( [showJson](#showjson) / [showFile](#showfile) ) 中会
在显示期间持续触发。模态 ( [showModalJson](#showmodaljson) /
[showModalFile](#showmodalfile) ) 中，`"close_on_click": true` 关闭前
发生的操作也会依次通知到此事件。

payload 的内容随控件种类而不同。

- button click ... void
- checkbox / toggle ... bool ( 更改后的值 )
- input_box ... string ( 编辑后的文本 )
- slider 等 ... 各控件传递的值

---

### onDrag

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `payload` | `&nbsp;` | 表示拖拽状态的 Dictionary ( 见上文 )。 |

**说明**

拖拽通知

对画面 JSON 中指定了 `"drag_events": true` 的控件，按下 → 移动 →
松开会送达此事件。请在 TJS 侧重写。

payload 是 Dictionary，持有 `id` ( 发生源控件的 id )、`phase`
( `"begin"` / `"move"` / `"end"` )、`x` / `y` ( 当前位置 )、`dx` / `dy`
( 与上一次的差分 )、`startX` / `startY` ( 按下位置 )、`modifiers`
( Shift 状态 )。坐标是画面 JSON 中写的坐标系。

积存的 `"move"` 会合并为最新的 1 条 ( `"begin"` / `"end"` 不会
合并 )。

**只想让图像跟随拖拽的话不需要此事件**。在控件中写
`"drag_at_var"` 把拖拽位置输出到变量，在 canvas 子节点的 `"at_var"`
中插入相同变量，即可在引擎内完结 ( 用 `"drag_bounds"` 也可以
限制可动范围 )。此事件用于在 TJS 侧进行“在哪里松开”之类
判断的用途。

---

### onVar

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变化的变量名。 |
| `value` | `&nbsp;` | 变化后的值 ( 字符串 )。 |

**说明**

变量变化通知

显示中对话框的变量 store 的值变化时送达的事件。
请在 TJS 侧重写。不仅是由 [setVar](#setvar) 的自己写入，
画面侧写入的值 ( `"vars_on_hover"` / `"vars_on_focus"` /
slider 的 `"value_var"` / `"drag_at_var"` / 列表的 `"index_offset_var"`
等 ) 也会触发。

用于“图像在宿主侧图层、只有命中判定在对话框”的构成中，
把悬停或选择的更改连接到宿主处理 ( 例如排列太大而无法放入
图集的单张图像的列表 )。

通知延迟 1 帧，相同变量的连续变化 ( 悬停移动或拖拽中的
坐标写入 ) 会合并为最新的 1 条。需要“当前的值”时请不要等待
通知，而是用 [getVar](#getvar) 读取。

**只有实现了此事件的对话框才会成为观测对象**。
未实现的对话框完全不产生开销。想筛选接收的变量时，
请使用 [watchVars](#watchvars)。

---

### onClose

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `action` | `&nbsp;` | 成为关闭契机的 button 的 id ( 用 `close_on_click` / Esc 关闭的情况。<br>用 [close](#close) 等显式关闭时为空字符串 )。 |

**说明**

对话框 teardown 完成通知

在此实例的对话框完全关闭 ( teardown 完成 ) 的时机触发的
非阻塞路径事件。请在 TJS 侧重写。

---

### onKeyCapture

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `key` | `&nbsp;` | VK 码。左键以外的鼠标按钮为 `VK_RBUTTON` / `VK_MBUTTON` /<br>`VK_XBUTTON1` / `VK_XBUTTON2`，手柄按钮为 `VK_PAD*`。 |
| `shift` | `&nbsp;` | `ss*` 的组合。自动重复带 `ssRepeat`。 |

**说明**

捕获的键

接收 [beginKeyCapture](#beginkeycapture) 捕获中按下的键的事件。
请在 TJS 侧重写。默认什么都不做。

**相关:** [ElementsDialog.beginKeyCapture](ElementsDialog.md#beginkeycapture)

---

### onA11yActiveChanged

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `active` | `&nbsp;` | 连接中则为真。 |

**说明**

屏幕阅读器的连接状态发生了变化

[a11yActive](#a11yactive) 变化时被调用。向 `ElementsDialog` 类
代入函数接收 ( 在绘制之外调用，WINVER 的静止画面也会立即调用 )。

```tjs
global.ElementsDialog.onA11yActiveChanged = function(active) {
Debug.message("スクリーンリーダー: " + (active ? "接続" : "切断"));
};
```

---

### onGameA11yAction

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` | 被操作的节点的 `id`。 |
| `action` | `&nbsp;` | `"click"` / `"focus"` / `"increment"` / `"decrement"` / `"set_value"`。 |
| `arg` | `&nbsp;` | `"set_value"` 时的值 ( 字符串 )。 |

**说明**

对游戏本体的节点的操作

屏幕阅读器操作 [setGameA11y](#setgamea11y) 的节点时被调用。
向 `ElementsDialog` 类代入函数接收。无论操作来自哪个线程，
都会在绘制之外的主线程中被调用。

action 由节点的角色决定。可按下之物 ( button / check_box /
list_item 等 ) 为 `"click"`，slider / spin_button 为 `"increment"` /
`"decrement"` / `"set_value"`，text_input 为 `"set_value"`。所有角色
都会收到 `"focus"`，`disabled` 的节点只接收 `"focus"`。

```tjs
global.ElementsDialog.onGameA11yAction = function(id, action, arg) {
if (action == "focus") { selectChoice(id); updateA11y(); }
else if (action == "click") { decideChoice(id); }
};
```

---
