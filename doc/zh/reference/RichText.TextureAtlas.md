# RichText.TextureAtlas

纹理图集类

这是一个将字形预渲染后存入图层（纹理），
并通过复制矩形数组按显示顺序转送的类。
同一字形会被去重，从而可以高效利用纹理。

向构造函数传入图层后，该图层会被用作纹理。

使用流程:
1. 传入图层创建图集
2. 用 addLayout / addParagraphLayout / addStyledLayout 添加字形
3. 用 commit() 写入纹理
4. 用 getCopyRects() 获取复制矩形数组
5. 根据复制矩形从图集图层复制到显示目标

使用示例:
var atlasLayer = new Layer(window, window.primaryLayer);
atlasLayer.setImageSize(1024, 1024);
var atlas = new RichText.TextureAtlas(atlasLayer);

var sl = new RichText.StyledLayout();
sl.layout(text, 400, 300, RichText.HALIGN_LEFT, RichText.VALIGN_TOP, style, app);
atlas.addStyledLayout(sl);
atlas.commit();

var rects = atlas.getCopyRects(sl, 10, 10);
for (var i = 0; i < rects.count; i++) {
var r = rects[i];
// r.srcX, r.srcY, r.srcWidth, r.srcHeight: 图集图层内的源矩形
// r.dstX, r.dstY: 显示目标的坐标
// r.displayIndex: 显示顺序
targetLayer.copyRect(r.dstX, r.dstY, atlasLayer,
r.srcX, r.srcY, r.srcWidth, r.srcHeight);
}

## 成员列表

### 构造函数

- [TextureAtlas](#textureatlas)

### 方法

- [clear](#clear)
- [addLayout](#addlayout)
- [addParagraphLayout](#addparagraphlayout)
- [addStyledLayout](#addstyledlayout)
- [commit](#commit)
- [getCopyRects](#getcopyrects)

---

### TextureAtlas

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 用作纹理的图层 |

**说明**

构造函数

---

### clear

方法

**说明**

清除图集（删除所有字形）

---

### addLayout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layout` | `&nbsp;` | RichText.Layout 对象 |
| `appearance` | `&nbsp;` | RichText.Appearance 对象 |

**返回值**

成功时为 true

**说明**

将 TextLayout 的字形添加到图集

---

### addParagraphLayout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `paraLayout` | `&nbsp;` | RichText.ParagraphLayout 对象 |
| `style` | `&nbsp;` | RichText.Style 对象 |
| `appearance` | `&nbsp;` | RichText.Appearance 对象 |

**返回值**

成功时为 true

**说明**

将 ParagraphLayout 的字形添加到图集

---

### addStyledLayout

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `styledLayout` | `&nbsp;` | RichText.StyledLayout 对象 |

**返回值**

成功时为 true

**说明**

将 StyledLayout 的字形添加到图集

---

### commit

方法

**说明**

将图集写入纹理（图层）

会将通过 addLayout / addParagraphLayout / addStyledLayout 添加的
字形渲染到图层。

---

### getCopyRects

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `/* overloaded */` | `&nbsp;` |  |

**返回值**

复制矩形的数组。每个元素是字典:
%[srcX, srcY, srcWidth, srcHeight, dstX, dstY, displayIndex, charIndex, delay, linkIndex]
charIndex: 原文本中的字符位置
delay: 显示时机（ms，未设置时不包含）
linkIndex: 链接编号（未设置时不包含）

**说明**

获取用于显示的复制矩形数组

有 3 个重载:

1) getCopyRects(layout, x, y, appearance, maxChars=-1)
- layout: RichText.Layout
- x, y: 绘制位置
- appearance: RichText.Appearance
- maxChars: 最大字符数（-1 表示全部）

2) getCopyRects(paraLayout, x, y, width, height, hAlign, vAlign, style, appearance, maxChars=-1)
- paraLayout: RichText.ParagraphLayout
- x, y, width, height: 绘制区域
- hAlign, vAlign: 对齐
- style: RichText.Style
- appearance: RichText.Appearance
- maxChars: 最大字符数（-1 表示全部）

3) getCopyRects(styledLayout, x, y, maxChars=-1)
- styledLayout: RichText.StyledLayout
- x, y: 绘制位置
- maxChars: 最大字符数（-1 表示全部）

---
