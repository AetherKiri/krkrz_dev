# RichTextRenderBase

TextRender 兼容的文本渲染类

提供与 ../textrender 的 TextRender 类 API 兼容的接口。
内部使用 richtext 库（StyledLayout）进行绘制。

接收带有 TextRender 转义记法的文本，将布局结果以
字符信息、时间信息、链接信息的形式返回。

输入用特殊文本格式:
\n      换行
\t      制表符
\i      开始缩进（从下一行起）※不支持
\r      解除缩进（从下一行起）※不支持
\w      将显示位置前进相当于空白的距离
\k      生成按键输入等待信息
\x      相当于 nul 字符
\字符   转义指定（禁用特殊功能）
[xxxx]         注音指定（作用于接下来的 1 个字符）
[xxxx,字符数]  注音指定（作用于接下来的指定数量个字符）

字体指定:
%f名称;     字体名指定
%bX         粗体指定（0:off 1:on 其他:默认）
%iX         斜体指定（0:off 1:on 其他:默认）
%sX         阴影指定（0:off 1:on 其他:默认）
%eX         描边指定（0:off 1:on 其他:默认）
%数值;      字体大小指定（相对于默认值的百分比）
%B          大号字体
%S          小号字体
#xxxxxx;    颜色指定（16 进制 RGB）
%s#xxxxxx;  阴影色指定
%e#xxxxxx;  描边色指定
%r          重置字体

样式指定:
%C          居中
%R          右对齐
%L          左对齐
%p数值;     间距（字距）

特殊指定:
%d数值;     每个字符的显示时间（相对于标准的百分比，100 为标准速度）
%a数值;     每个字符的显示时间（ms）
%w数值;     等待时间（相对于 1 个字符时间的百分比，100 相当于 1 个字符的时间）
%t数值;     等待时间（ms）
%D数值;     时间同步指定（ms）
%D$xxx;     时间同步指定（标签参照）

$xxx;       嵌入指定（变量名）※由 onEval 处理
&xxx;       图形字符指定（图像名）※由 onGetGraphSize 处理

链接指定:
%l链接名;  开始链接指定
%l;          解除链接指定

不支持:
竖排、rubyoffset、断词控制（%k0/%k1）

使用流程:
clear() → setFont/setStyle → render() [可多次] → done()
→ 通过 getCharacters() / calcShowCount() / getKeyWait() 等获取结果

使用示例:
var tr = new TextRenderBase();
tr.setDefault(%[ face: "MSゴシック", fontsize: 24, color: 0xFFFFFF ]);
tr.setRenderSize(400, 300);
tr.clear();
tr.render("こんにちは%B世界%r！\n2行目", 0, 30, 0, false);
tr.done();

var chars = tr.getCharacters(0, 0);  // 获取全部字符信息
var count = tr.calcShowCount(500);    // 500ms 时刻的显示字符数

## 成员列表

### 属性

- [timeScale](#timescale)
- [fontScale](#fontscale)
- [defaultFace](#defaultface)
- [defaultFontSize](#defaultfontsize)
- [defaultBigFontSize](#defaultbigfontsize)
- [defaultSmallFontSize](#defaultsmallfontsize)
- [defaultLineSize](#defaultlinesize)
- [defaultLineSpacing](#defaultlinespacing)
- [defaultPitch](#defaultpitch)
- [defaultAlign](#defaultalign)
- [defaultValign](#defaultvalign)
- [defaultRubySize](#defaultrubysize)
- [defaultColor](#defaultcolor)
- [defaultShadow](#defaultshadow)
- [defaultShadowColor](#defaultshadowcolor)
- [defaultEdge](#defaultedge)
- [defaultEdgeColor](#defaultedgecolor)
- [defaultBold](#defaultbold)
- [defaultItalic](#defaultitalic)
- [renderOver](#renderover)
- [renderLines](#renderlines)
- [renderCount](#rendercount)
- [renderDelay](#renderdelay)
- [renderLeft](#renderleft)
- [renderTop](#rendertop)
- [renderRight](#renderright)
- [renderBottom](#renderbottom)
- [renderText](#rendertext)

### 方法

- [TextRenderBase](#textrenderbase)
- [setOption](#setoption)
- [setDefault](#setdefault)
- [setRenderSize](#setrendersize)
- [clear](#clear)
- [setFont](#setfont)
- [resetFont](#resetfont)
- [setStyle](#setstyle)
- [resetStyle](#resetstyle)
- [render](#render)
- [newline](#newline)
- [done](#done)
- [onEval](#oneval)
- [onLabel](#onlabel)
- [onGetGraphSize](#ongetgraphsize)
- [getKeyWait](#getkeywait)
- [calcShowCount](#calcshowcount)
- [calcLineOffset](#calclineoffset)
- [getCharacters](#getcharacters)
- [getLinkNames](#getlinknames)
- [getLinkRects](#getlinkrects)
- [getLinkCharacters](#getlinkcharacters)
- [isLinkContains](#islinkcontains)
- [getLinkOfPosition](#getlinkofposition)
- [drawToLayer](#drawtolayer)

---

### timeScale

属性 \ 访问: `r/w`

**说明**

渲染时间补正

---

### fontScale

属性 \ 访问: `r/w`

**说明**

字体大小补正倍率

---

### defaultFace

属性 \ 访问: `r/w`

**说明**

默认值属性

---

### defaultFontSize

属性 \ 访问: `r/w`

---

### defaultBigFontSize

属性 \ 访问: `r/w`

---

### defaultSmallFontSize

属性 \ 访问: `r/w`

---

### defaultLineSize

属性 \ 访问: `r/w`

---

### defaultLineSpacing

属性 \ 访问: `r/w`

---

### defaultPitch

属性 \ 访问: `r/w`

---

### defaultAlign

属性 \ 访问: `r/w`

---

### defaultValign

属性 \ 访问: `r/w`

---

### defaultRubySize

属性 \ 访问: `r/w`

---

### defaultColor

属性 \ 访问: `r/w`

---

### defaultShadow

属性 \ 访问: `r/w`

---

### defaultShadowColor

属性 \ 访问: `r/w`

---

### defaultEdge

属性 \ 访问: `r/w`

---

### defaultEdgeColor

属性 \ 访问: `r/w`

---

### defaultBold

属性 \ 访问: `r/w`

---

### defaultItalic

属性 \ 访问: `r/w`

---

### renderOver

属性 \ 访问: `r/w`

**说明**

/ 渲染结果是否超出区域

---

### renderLines

属性 \ 访问: `r/w`

**说明**

/ 渲染结果的行数

---

### renderCount

属性 \ 访问: `r/w`

**说明**

/ 渲染结果的字符数

---

### renderDelay

属性 \ 访问: `r/w`

**说明**

/ 渲染结果的总显示时间

---

### renderLeft

属性 \ 访问: `r/w`

**说明**

/ 渲染结果的区域信息

---

### renderTop

属性 \ 访问: `r/w`

---

### renderRight

属性 \ 访问: `r/w`

---

### renderBottom

属性 \ 访问: `r/w`

---

### renderText

属性 \ 访问: `r/w`

**说明**

/ 渲染结果文本（已去除转义）

---

### TextRenderBase

方法

**说明**

构造函数

---

### setOption

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 字典 |

**说明**

渲染选项的设置

可设置的键:
ignore_color  忽略颜色指定
ignore_size   忽略大小指定
ignore_type   忽略字体种类指定（bold/italic/shadow/edge）
ignore_face   忽略字体名指定
ignore_style  忽略样式指定（align/pitch）
ignore_ruby   忽略注音指定
ignore_delay  忽略时间指定
width_time_scale  按字符宽度进行时间补正（0:不进行 1:进行）
locale        区域设置字符串（例: "ja_JP"）

---

### setDefault

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 字典 |

**说明**

默认值的设置

仅字典中包含的键会被反映（未包含的键维持当前值）。
调用 setDefault 后，内部会执行相当于 resetFont() / resetStyle() 的处理，
当前的字体、样式状态会同步为默认值。

可设置的键:
face          字体名
除 registerCollection 注册的字体集合名之外，
还可以用 registerFont 的注册名、字体文件内的 family 名
（例: "Noto Sans JP"）、"family Style" 连接名
（例: "Noto Sans JP Bold"）来指定。
fontsize      字体大小
bigfontsize   大号字体大小（用于 %B）
smallfontsize 小号字体大小（用于 %S）
bold          粗体
italic        斜体
color         文字颜色（RGB）
shadow        阴影指定
shadowcolor   阴影色
edge          描边指定
edgecolor     描边色
linespacing   行距
pitch         字符间距
linesize      行大小
align         水平对齐（-1:左 0:居中 1:右）
valign        垂直对齐（-1:上 0:居中 1:下）
rubysize      注音大小

---

### setRenderSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 区域宽度（0 表示无限制） |
| `height` | `&nbsp;` | 区域高度（0 表示无限制） |

**说明**

渲染区域的大小指定

---

### clear

方法

**说明**

清除渲染结果

---

### setFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 字典 |

**说明**

字体指定

可设置的键:
face, fontsize, bold, italic, color, shadow, shadowcolor, edge, edgecolor

---

### resetFont

方法

**说明**

将字体状态恢复为默认值

---

### setStyle

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `elm` | `&nbsp;` | 字典 |

**说明**

样式指定

可设置的键:
linespacing, pitch, linesize, align, valign

---

### resetStyle

方法

**说明**

将样式指定恢复为默认值

---

### render

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `str` | `&nbsp;` | 要渲染的字符串（含转义记法） |
| `autoIndent` | `0` | 自动缩进指定（0:无效 1:有效 -1:反向缩进）※当前不支持 |
| `diff` | `0` | 每个字符的显示时间（ms） |
| `all` | `0` | 总时间指定（0 为自动，ms） |
| `noResetDelay` | `false` | 为 true 时维持以前的显示时间 |

**返回值**

未超出范围并成功渲染时为 true

**说明**

渲染文本

在 clear() 之后可以多次调用。在调用 done() 之前结果不会确定。

---

### newline

方法

**说明**

另起新行

---

### done

方法

**说明**

渲染完成

对 render() 累积的文本进行一次性布局，
并确定时间信息、链接等信息。

---

### onEval

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 变量名 |

**返回值**

变量值（字符串）

**说明**

渲染过程中的变量参照处理

当通过 $xxx; 记法被参照时调用。
可以继承并重写。

---

### onLabel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 标签名 |

**返回值**

tick 值（ms）

**说明**

渲染过程中的标签参照处理

当通过 %D$xxx; 记法被参照时调用。

---

### onGetGraphSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 图像名 |

**返回值**

%[width: 宽度, height: 高度]

**说明**

获取图形字符的大小信息

当通过 &xxx; 记法被参照时调用。

---

### getKeyWait

方法

**返回值**

[%[pos: 字符位置, time: 时间], ...]

**说明**

返回按键等待信息的数组

---

### calcShowCount

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `time` | `&nbsp;` | 时间（ms） |

**返回值**

显示字符数

**说明**

返回指定时间时的显示字符数

---

### calcLineOffset

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `lineno` | `&nbsp;` | 行号 |

**返回值**

偏移值

**说明**

返回指定行的偏移值

---

### getCharacters

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `start` | `&nbsp;` | 起始字符位置 |
| `num` | `&nbsp;` | 获取字符数（0 表示到末尾） |

**返回值**

绘制信息的数组

**说明**

获取渲染结果的字符信息

各元素为字典，包含以下键:
text       要显示的文本
graph      图形显示时的图像名（普通字符为 void）
x          显示坐标 X
y          显示坐标 Y
cw         显示宽度
size       字体大小
face       字体名
color      显示颜色
bold       BOLD 指定
italic     ITALIC 指定
shadow     阴影指定
edge       描边指定
shadowColor  阴影颜色
edgeColor    描边颜色
delay      显示时机（自显示开始起经过的时间）
link       链接编号（没有时为 -1）
linkName   链接名（没有时为 void）
ruby       注音数组 [%[text, x, y, size], ...]

---

### getLinkNames

方法

**返回值**

链接名的数组（重复的名称也原样列出）

**说明**

返回所包含链接名的一览

---

### getLinkRects

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `link` | `&nbsp;` | 链接编号 |

**返回值**

区域信息的数组 [%[left, top, width, height], ...]

**说明**

获取链接的区域信息

跨多行时会返回多个矩形

---

### getLinkCharacters

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `link` | `&nbsp;` | 链接编号 |

**返回值**

绘制信息的数组（与 getCharacters 同格式）

**说明**

获取属于链接的字符信息

---

### isLinkContains

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `link` | `&nbsp;` | 链接编号 |
| `x` | `&nbsp;` | X 位置 |
| `y` | `&nbsp;` | Y 位置 |

**返回值**

包含在链接中时为 true

**说明**

判断是否包含在链接中

---

### getLinkOfPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X 位置 |
| `y` | `&nbsp;` | Y 位置 |

**返回值**

链接编号（-1:无）

**说明**

返回指定位置的链接编号

---

### drawToLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 绘制目标图层对象 |
| `x` | `&nbsp;` | 绘制开始 X 坐标 |
| `y` | `&nbsp;` | 绘制开始 Y 坐标 |
| `maxChars` | `-1` | 要绘制的字符数上限（-1 表示全部，省略时: -1） |

**返回值**

绘制区域的数组 [x, y, width, height]

**说明**

将渲染结果绘制到图层

将 done() 确定的渲染结果绘制到指定图层。
通过指定 maxChars 可以实现逐字显示动画。

使用示例:
tr.render("テキスト", 0, 50, 0);
tr.done();
tr.drawToLayer(layer, 10, 10);

// 逐字显示
var count = tr.calcShowCount(elapsed);
tr.drawToLayer(layer, 10, 10, count);

---
