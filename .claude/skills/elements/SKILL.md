---
name: elements
description: 吉里吉里Z 上の Elements ベース汎用ダイアログ/画面 UI (cycfi/elements + elements_modal) の作り方リファレンス。TJS で JSON / Dictionary 定義のダイアログを作る・出す・イベントを受ける・複数画面フロー(navigator)や常駐メニューを組む・入力/フォーカス/モーダルを制御する・Agent で動作検証する、といった場面で使う。基本的なダイアログ画面の作り方(最小例・レイアウト JSON スキーマ・ウィジェット一覧)から、モーダル/非モーダル/独立ウィンドウ/常駐フロー、複数インスタンス/z-order、DrawDevice 登録タイミング等のハマりどころまで網羅。Win32 ネイティブの WIN32Dialog(win32dialog プラグイン)とは別物。TJS2 言語仕様は skill `tjs2`、本体クラス API は `krkrz`、REPL/Agent 駆動は `krkrz-repl` を参照。中文说明：用 TJS 制作基于 Elements 的对话框/画面 UI（JSON/Dictionary 定义、事件、多画面流程、常驻菜单、输入/焦点/模态控制、Agent 运行验证）的参考。触发词：Elements、对话框、JSON 布局、控件、模态、navigator 流程、常驻菜单、焦点控制、Agent 验证、ElementsDialog。
---

> **路径基点**: 正文的相对路径以 **engine 根目录**为基准 (krkrz_dev 中需前置 `src/core/`，见下)。工作目录不是 krkrz_dev (如 krkrz_android / krkrz_ios 等外围仓库或项目文件夹) 时，请**前置 `${KRKRZ_BASE}/krkrz_dev/`** 再读取 (用 `echo $KRKRZ_BASE` 确认实际路径。每台机器的值不同，所以不要写入绝对路径)。

# 基于 Elements 的对话框 / 画面 UI (krkrz)

在吉里吉里Z 中嵌入的 [Elements](https://github.com/wamsoft/elements) (基于 ThorVG/cycfi 的 C++ GUI) 上，显示**以 JSON / TJS Dictionary 定义的对话框或画面**的机制。通过 `ElementsDialog` 类使用。在所有桌面变种 (SDL3 / WINVER / OGL) 上运行。

> **与 Win32 的 `WIN32Dialog`(win32dialog 插件)不是一回事**。那边是 Win32 原生对话框。这边是全平台通用的 Elements UI。

## 路径的读法
正文的引擎路径以 engine 根目录为相对基准 (`common/...`、`data/...`、`doc/...`、`external/...`)。
本 skill 所在的 **umbrella (`krkrz_dev`) 中需前置 `src/core/`** 再读取
(例: `src/core/doc/ElementsDialog.md`、`src/core/data/ui/`、`src/core/external/elements/`)。
单独检出 engine 时则直接使用。

## 集成到游戏 (KAG/kag) 中时
**先读 [`references/krkr_integration.md`](references/krkr_integration.md)** — 装入案件时的集成知识: 层构成 (基盘 TJS + 画面驱动) / 显示路径的选择与 engine 侧的约束 (overlay 的尺寸上限・`showFile` 不经过 autopath・子类的 `super.ElementsDialog()`) / 乘到 KAG 的 openDialog 框架上的宿主图层方式与 z 顺序 / 驱动的类型与生命周期的陷阱 (常驻画面的重新显示・标签页切换) / 值与动态图像的注入 / 素材搜索与字体批量注册 / 转场效果 / Agent 验证的癖性 / 未解决的 engine TODO。

## 应当最先阅读的一手资料 (SSOT)
- **`doc/ElementsDialog.md`** — 整体机制・API 路径・输入路由・多实例・阶段状态。**先读这个**。
- **`external/elements/external/elements_modal/README.md`** — **JSON 布局的全部控件/属性目录**(下面的列表是摘要)。
- 实例: `data/ui/about.json` / `data/ui/menu/*.json` + `data/ui/menu/app.jsonc`(navigator 流程) / `data/elements_gallery/` / `data/transition_demo/` / `data/startup.tjs`(`FlowMenuDialog` 常驻菜单)。

---

## 1. 基本对话框的做法 (最小示例)

继承 `ElementsDialog`，在 `onAction` 中对按钮等作出反应，用 `showJson`(或 `showDict`)显示，用 `close()` 关闭。**非模态 (覆盖层) 是基本形态**。

```tjs
class MyDialog extends ElementsDialog {
    function onAction(id, payload) {
        // state widget の値変化 / button click で発火 (payload: 値、button は void)
        switch (id) {
        case "ok":     System.inform("OK が押されました"); close(); break;
        case "cancel": close(); break;
        }
    }
}
var dlg = new MyDialog();
dlg.showJson('{
    "size": [360, 200],
    "background": [30, 30, 60, 245],
    "input": { "arrow_focus_nav": true },
    "content": { "type": "margin", "padding": 20, "child": {
        "type": "vtile", "children": [
            { "type": "align_center",
              "child": { "type": "label", "text": "こんにちは", "size_scale": 1.3 } },
            { "type": "vspacer", "height": 20 },
            { "type": "htile", "children": [
                { "type": "button", "id": "ok",     "text": "OK",     "initial_focus": true },
                { "type": "hspacer", "width": 12 },
                { "type": "button", "id": "cancel", "text": "キャンセル" }
            ] }
        ]
    } }
}');
```

### 用 Dictionary 书写 (showDict) — 无需书写 JSON 字符串
`common/visual/elements/VariantJsonUtil.cpp` 会把 Dictionary 转换为 JSON 后送入同一条路径。可以不加转义直接书写 JSON，可读性更高。

```tjs
dlg.showDict(%[
    size: [360, 200], background: [30, 30, 60, 245],
    input: %[ arrow_focus_nav: true ],
    content: %[ type: "margin", padding: 20, child: %[
        type: "vtile", children: [
            %[ type: "label", text: "こんにちは", size_scale: 1.3 ],
            %[ type: "vsize", height: 40,
               child: %[ type: "button", id: "ok", text: "OK", close_on_click: true ] ],
        ] ] ]
]);
```
- **`ElementsDialog.dictToJson(value)`** 可以取得转换结果的 JSON (调试 / 素材导出)。
- **TJS Dictionary 的两个约束**(重要):
  1. **没有 bool**: `true` 等于整数 1。`close_on_click: true` 会变成 JSON 的 `1` (elements 侧把 0/非0 作为真伪接受)。
  2. **空字符串键不可用**: navigator 的默认迁移 `"": "<exit>"` 无法用 Dict 书写 → 用未定义 action 的回退 (entry=exit / 子画面=pop) 是否足够，或者该画面单独用 JSON 字符串。

---

## 2. 布局 JSON 模式

### 顶层
| 键 | 类型 | 说明 |
|---|---|---|
| `size` | `[w,h]` | **期望逻辑尺寸 (上限)**。实际尺寸会适配收缩到 content 的自然尺寸 (防顶部留白) |
| `background` | `[r,g,b,a]` | 绘制 content 前的填充 (省略=透明・无边框) |
| `align` | `"center"`(默认)/`top`/`bottom`/`left`/`right`/`top_left`/`bottom_right` 等 | 在 overlay 上的布置。输入坐标也同步修正，不会有点击偏移。对所有 overlay 路径有效 |
| `margin` | int | 与非居中侧表面边缘的留白 px (默认 0)。例: 左上角菜单 = `"align":"top_left","margin":24` |
| `locale` | `"ja-JP"` 等 | label 未指定 locale 时的默认 (区分 CJK 同形字) |
| `content` | element | 根元素 |
| `input` | object | 键/手柄导航设置 (§6) |
| `vars` | `{name:string}` | 变量 store 初始值 (`label.text_var` / `vars_on_focus` 引用) |
| `transitions` | `{action:target}` | navigator 的迁移定义 (§5)。也可以 object 形式声明画面切换效果 (`effect`/`duration`/`rule`/`vague`) |
| `pad_theme` | `xbox`/`ps`/`switch`/`keyboard`/`none` | pad_icon 的名称解析 |
| `atlases` | `{name:spec}` | 纹理图集预加载 (`atlas_*` 引用) |
| `font_scale` | number | 没有显式 size 的 button/toggle/check_box/label 的默认字体倍率 (默认 1.0) |
| `style` | object | **布局密度的批量指定**: `%[font_scale, tile_gap(未指定 gap 的瓦片默认), row_height(button 系/input_box/selection_menu 的默认最小高度), padding(content 外侧留白)]`。全部省略=与以往一致。可以在不写 spacer 的情况下消除默认「拥挤」的外观 |

### 控件 ("type") 摘要 (完整列表见 elements_modal/README.md)
**布局**: `vtile`/`htile`(`children`,`gap`=子元素间隙 px・省略时 style.tile_gap→0) / `margin`(`padding`,`child`) / `hsize`/`vsize`(`width`|`height`,`child`) / `hspacer`/`vspacer`(`width`|`height`) / `spacer`(`size`) / `align_center`/`align_left`/`align_right`/`align_top`/`align_middle`/`align_bottom`/`align_center_middle`(`child`) / `box`(`color`) / `band`(`color`+任意`child`) / `layer`(`children`,开头=最前层) / `group`(`title`,`child`) / `scroller`(`child`) / `filler` / `floating`(`at:[x,y,w,h]`,`child`) / `canvas`(`children` 中带 `at`，面向 PSD 绝对布置。`choice_nav:true` 把子 choice 组变成 1 个焦点的左右切换，子元素的 `at_var` 可以用变量驱动布置)。
**注意**: `hsize`/`vsize` 的指定值会被 **clamp 到 child 的 limits** (cycfi fixed_size 规范)。直接包裹 label 等带固定 max 的 child 也无法扩展到期望尺寸 → 想确定整体尺寸的画面，应显式指定各部件宽度，让自然尺寸=期望值，这样最可靠。
**长文本**: `text_box` — 多行・自动折行的静态文本 (`text`,`size`|`size_scale`,`color`,`mono`=等宽,`text_var`=用 setVar 整体替换正文)。宽度由父级 (`hsize`) 决定，高度跟随折行。长文本在父级上放 `scroller`。比起大量生成行 label 更轻。实例=`data/ui/license_dialog.tjs` (showLicenseDialog: 左=列表/右=text_box 的双窗格全屏模态，模态中 onAction→setVar 也能同步生效)。
**矩形文本/字幕**: `text_area` — 灌入矩形的静态文本 (`text`/`text_id`/`text_var`/`text_list_id`+`index_var` 与 label 同规约, `size`|`size_scale`, `color`, `font`=逗号分隔的 families, `align`=left/center/right, `line_spacing`=行距追加 px, `base`=auto/ltr/rtl, **`count_var`=字符送进** (-1=全部))。**折行・行首行尾禁则・count 与引擎本体 `Layer.drawShapedTextArea` 使用同一逻辑**，所以同样的正文・同样的宽度下**换行位置一致** (glyphware `layoutBlock`)。折行在全文确定后再应用 count=送进也不会重排。计数的单位是簇 (`Layer.shapedTextCount` 相同)。`text_box` 保持以往兼容 (朴素折行・无禁则)，所以**既有画面的换行不会改变**。⚠ 用 `floating` 的绝对坐标放置时**必须书写** top-level `"size":[w,h]` (省略的话对话框会缩到内容最小尺寸，**什么都看不见**)。规范=elements `docs/block-text.md`。
**输入/state**: `label`(`text`,`size`=px 绝对 or `size_scale`=倍率,`color`,`text_var`,`text_id`=i18n,`text_list`+`index_var`=显示指定编号、`index`+`index_offset_var`=«N 行的窗口»〔每行固定 index + 行共享的开头位置。取的位置=index+offset、窗口模式范围外为空字符串〕、`text_list_var`=整体替换列表数据本身) / `button`(`text`,`id`) / `checkbox`|`check_box`(`text`,`id`,`value`) / `toggle_button` / `input_box`(`placeholder`,`id`,`size`,`max_chars`=最大字符数〔以 codepoint 为单位，别名 `maxlength`，0/省略=无限制。打满后按键被忽略・paste 只取放得下的部分〕,`text`/`value`=初始值〔build 时全选=直接输入会替换〕) / `selection_menu`(`id`,`options`,`selected`) / `slider`(0..1 的原始滑块。`id`,`initial`,`vertical`,`thumb_color`/`track_color`〔默认=主题保留色 `@slider_thumb` 白 / `@slider_track` 黑〕,`value_var`,`display`/`display_var`) / `invert_button` / `ring_button` / `labeled_row`(`label`,`label_width`,`child`) / `tab_view`(`tabs`,`initial`) / picker 系 `cycle_picker`/`framed_cycle_picker`/`segmented_picker`(`options`|`options_id`=i18n,`initial`,`font_size`,`font`=显示文本的 family[#axes]・省略则主题默认,`index_var`=把选中 index 写入变量)。
**装饰/图像**: `pad_icon`(手柄图标) / `sprite_button` / `atlas_image`(`rect` or `rect_list`+`index_var`=用变量切换矩形、`focus_link`=链接目标 id 获得焦点时切换 `frames.normal`/`frames.hilite` 的装饰〔`normal` 可省略=非焦点时不绘制任何内容・用于单张素材的焦点指示器。默认带有「hover 装饰→焦点移到链接目标」的代理并会夺走点击，所以与控件重叠的布置请设置 `"hover_focus_link": false`〕)/`atlas_button`/`atlas_toggle`/`atlas_choice`(排他)/`atlas_slider`(thumb 型式或 `fill`+`fill_at` 量表式、`value_var`。两端的增减箭头=`dec`/`inc`+`dec_at`/`inc_at`〔+`track_at`/`step`/`repeat*`/`flash_ms`，名称按减/增的含义，left/right/up/down 等几何名是别名。atlas_scrollbar 也使用相同键〕)/`atlas_progress`/`atlas_cycle_picker`(图像箭头选择器、焦点=箭头 hilite、可指定 `font`)/`animated_sprite` / `gizmo_image`(9patch)。
- 颜色是 `[r,g,b,a]` 数组 (0–255)。字体大小是 **`size`=px 绝对 / `size_scale`=倍率**(相对主题默认约 14px)。支持 JSON/JSONC(注释+末尾逗号)。
- **i18n**: top-level `strings`(`{id:{lang:str}}`) + `lang`。`text_id`/`options_id`/`text_list_id` 按当前语言解析。**从 TJS 运行时切换用 `ElementsDialog.language = "en"`**(立即反映到所有显示中的对话框・无需重新打开，picker 保持选中 index。也是之后打开的画面的默认)。
- **变量联动**: picker `index_var`(**双向**: 选择变更时写入 + setVar 时安静跟随) ↔ `text_list`/`rect_list` 的 `index_var`(读) 同名时选择联动 (机型选择→SPEC/截图等)。`value_var`=十进制小数、`at_var`=`"x,y[,w,h]"`。picker `enabled_var`=选项的有效/无效 mask(`'0'`/`'1'` 字符串，step/click 跳过无效 index。用于未开放机型的区分显示)。choice (`atlas_choice`/`radio_button`) 的 `selected_var`+`selected_value`=单选组变量(组内全部使用同一 var + 不同 value，var==value 的一个被选中，双向)。从 TJS 用 `dlg.setVar(name, value)` 驱动。
- **跨画面保持的变量**: top-level `"shared_vars": ["cfg_*","ui_lang"]`(完全一致或末尾 `*` 的前缀一致)。匹配的变量会与会话共享 store **双向**同步，并带到下一个画面(共享侧的值优先于画面的 `"vars"` 默认)。**无需宿主实现**。保存/加载用 static API `ElementsDialog.setSharedVar(name,value)` / `getSharedVars()`(字典)/ `clearSharedVars()`。只有「作为变化被写出的」值会到共享侧，widget 的初始值(`initial`/`value`)不会出去。本来用途是防止「在设置画面来回切换标签页时滑块被重置」。
- **二值 toggle 的 `value_var`**: `checkbox`/`check_box`/`toggle_button`/`slide_switch` 与变量 store 双向同步(`""`/`"0"`/`"false"`=off)。未设置时以 `"value"` 播种，已有则用它覆盖初始状态。`setVar` 跟随时不触发 `on_click`。可以在没有宿主回调的情况下写出设置的 ON/OFF。
- **用变量替换图片的 `image_var`**: 用变量整体替换 `image` 的图片。值直接就是图片路径(`"resources/x.png"` / `"mem://thumb_3"` / 空=不绘制)。构建时变量值优先于静态 `"image"`，未设置则以 `"image"` 播种。**存档列表翻页时缩略图变化 / 推送 CG 查看器的图片**都可以不重建画面实现。空路径或读不出的路径也会保留 widget，所以放入正确的路径就能恢复。
- **可替换图集**: 声明 top-level `"atlases": { "cg": { "path": "atlas/cg_g0.png", "swappable": true } }` 后，`ElementsDialog.setAtlasImage("cg","atlas/cg_g1.png")`(static，path 以画面的 `resource_base` 为起点，返回值=是否替换成功)可以**画面不变只替换图片束**。widget 不会重建，所以布局/焦点保持不变。⚠**必须矩形划分相同**(frames/rect 不变，位置错开就会显示别的图片)。列表用 `ElementsDialog.swappableAtlases()`。swappable 不上按路径的缓存(避免连累其他画面)。
- **向模态注入初始 vars**: `dlg.showModalFile(path, %[name=>value,...])`(showModalJson/Dict 同理，第 2 参数 Dictionary)。在 build 后、pump 前灌入变量 store(模态中 TJS 被阻塞，无法 setVar)。模态中 onAction 也能同步送达。
- **pad_icon/字体 setup (static)**: `ElementsDialog.setPadIconBase(dir)`(Kenney SVG 的 base storage 路径。未设置则显示灰色占位)/`ElementsDialog.setPadTheme("xbox"|"ps"|"switch"|"keyboard"|"auto")`(`"auto"`=从已连接手柄的系别〔`System.padStyle`〕自动选择。当场检测连接数/系别变化并重新决定，所以拔插立即跟随〔显示中的画面也重绘〕。系别不明的平台在连接 1 台以上手柄时用 `"xbox"`，0 台时用 `"keyboard"`)/`ElementsDialog.setPadIconAlias(theme, name, basename)`(把逻辑名→Kenney basename 的默认表〔a=Enter/b=Esc/dpad=方向键〕按主题覆盖。例: 取消是 BackSpace 时 `setPadIconAlias("keyboard","b","keyboard_backspace")`。basename 为空则单独解除，name 为空则解除该主题全部)/`ElementsDialog.registerFontDir(dir)`/`ElementsDialog.defaultFontFamily = "Open Sans, Roboto, Noto Sans JP, ..."`(显式设置不会被自动 theme 排列覆盖。Emoji 系务必放在末尾)。
- **元素的启用/禁用与变量联动**: button 系(`button`/`atlas_button`/`invert_button`/`ring_button`)的 `enabled_var`。值为 `"0"` 时禁用，其他(默认)启用。禁用期间点击/按键决定无效，绘制用 `disabled` frame，没有则半透明。用于随进度解锁的菜单项(未通关则「特典」置灰)等。

### static 设置一览 (对整个类生效。`ElementsDialog.xxx`)

⚠ **在继承 `ElementsDialog` 的类的方法内访问时要写 `global.ElementsDialog.xxx`**。裸写 `ElementsDialog` 会作为父类引用，对 static 属性的赋值会报「找不到成员」。

| 属性 | 默认 | 用途 |
|---|---|---|
| `language` | `""` | i18n 显示语言。赋值后立即反映到所有显示中的画面(见上文 i18n) |
| `focusRing` | `false` | 绘制在焦点元素上的通用边框(蓝色圆角)。**krkrz 宿主初始化时默认 OFF**(策略是用 authored 画面的 focused frame / focus_link 装饰来表现)。想用时设 `true`(启动时的显式设置不会被初始化覆盖)。对象为 button/slider/dial/thumbwheel。OFF 时焦点本身仍然有效，所以键/手柄操作与 `hilite` 切换不变 |
| `renderCache` | `true` | 省略无变化帧的重新栅格化+重新上传。闲置变成零成本。`false` 用于负载对比 |
| `partialRedraw` | `true` | 只重绘变化的矩形(脏矩形)。`false` 为全量 |
| `baseSize` | 未设置 | UI 的 author 基准面尺寸 `[w,h]`(overlay 缩放 fit 的分母)。void 时默认回到游戏基准面(primaryLayer)。**以与游戏画面不同分辨率 author UI 时**设置后，局部面板的缩放以 author 基准进行，不会被游戏侧基准面的变更卷进去 |
| `renderScale` | `0` | 栅格化密度。0=auto(以 present 尺寸直接绘制)/`>0`=按 authored×倍率绘制后缩放 |
| `renderStats` / `renderStatsReset()` | — | 绘制管线的分段测量(frames/rasters/partials/updateUs/rasterUs/uploadUs/presentUs 等)。是累计值，要读两次取差值。测量画面=`data/elements_bench`(`-benchauto` 无操作巡回) |
| `renderCount` | — | 累计栅格化次数。闲置时不增加说明 renderCache 生效 |
| `atlasCacheStats` | — | 图集解码缓存的常驻量 `%[bytes, count, budget]`。设计上**关闭画面也不释放**，所以用于在场景切换时观察积存量的场合 |
| `trimAtlasCache(budget=0)` | — | 裁剪图集缓存(0=全部释放未使用部分)。返回值=释放的字节数。⚠**显示中的画面正在使用的部分因为引用还在所以不会释放**→在关闭画面后调用 |
| `atlasCacheBudget` | 192MB | 图集缓存预算。赋值后永久变更(调低会当场裁剪)。0 时缓存无效 |

### interactive 属性 (focusable widget 通用)
- **`"id"`** — `onAction` / `result.values` / shortcut / setVar 的引用键。
- **`"initial_focus": true`** — 启动时焦点候选。**可指定多个**，首个候选被 `enabled_var` 禁用时落到下一个有效候选。写成数值则显式指定优先级(越小越优先・`true`=0，同值按 build 顺序)。候选要等到显示后的 idle 才确定，所以 show 后用 `setVar` 注入启用/禁用的运用也会按注入后的状态判定。
- **`"close_on_click": true`** — **默认 false**。只有 true 的 button 点击时「关闭并确定」(`result.action=id`)。false 只触发 `onAction` 不关闭 → 只加在 OK/Cancel 等「关闭按钮」上。

---

## 3. 显示路径的选用 (`ElementsDialog` 方法)

| 方法 | 模式 | 用途 |
|---|---|---|
| `showJson(json[, grabFocus=true[, modal=grabFocus]])` / `showFile(path, ...)` | overlay・非阻塞 | 普通对话框。`onAction` 逐次，`close()` 结束。**`showJson(json, true, false)`=非模态+带焦点(推荐用于操作面板)** |
| `showDict(dict, ...)` | 同上方法的 Dictionary 版 | 不写 JSON |
| `showModalJson(json)` / `showModalDict(dict)` | overlay 模态・**阻塞** | 在游戏画面上 nested 循环。返回值 `%[action, values]` |
| `showModalJson(json, title, w, h)` | **独立 OS 窗口**模态・阻塞 | 独立窗口。SDL=run_modal / WINVER=专用 Win32 窗口 |
| `showFlow(manifest)` / `showFlowScreens(dict, entry)` | overlay・阻塞・多画面 | navigator 流程(§5) |
| `startFlow(manifest)` / `startFlowScreens(dict, entry)` | overlay・**非阻塞・常驻** | 长期显示菜单。与后台运行并存(§5) |

- **阻塞 (showModal*/showFlow)** 返回 `result`: `result.action`=关闭时的 button id(Esc/× 为 `""`)、`result.values`=state widget 最终值映射。
- `showFile`/`showFlow` 的路径是 **Storages 解析但不参与 autopath 搜索** — 只写文件名会失败，要带路径(`"system/foo.jsonc"`)传入。画面文件的相对素材以该画面文件的目录为起点。

### 绘制到宿主图层: `ElementsPanel` (与 overlay 并行的框架)

用 `new ElementsPanel(layer)` + `showFile/showJson/showDict`，把**同一个画面 JSON 绘制到 Layer 的位图**。z 顺序・`[trans]`・piledCopy・输入的归属都**遵循图层的机制**，所以不想盖在正文之上、要放到转场上的画面、想混入 KAG 图层 z 顺序的画面请用它 (overlay 永远在最前面)。

```tjs
var lay = new Layer(win, win.primaryLayer);
lay.setImageSize(400, 300); lay.setSizeToImageSize();
lay.type = ltAlpha; lay.hitThreshold = 0; lay.visible = true;
var panel = new ElementsPanel(lay);
panel.onAction = function(id, payload) { ... };
panel.showFile("ui/hud.jsonc");
// 入力はレイヤから手で流す (座標はレイヤ local をそのまま)
lay.onMouseDown = function(x, y, b, f) { panel.mouseDown(x, y, b, f); };
lay.onMouseUp   = function(x, y, b, f) { panel.mouseUp(x, y, b, f); };
lay.onMouseMove = function(x, y, f)    { panel.mouseMove(x, y, f); };
```

- **事件 / 变量 API 与 ElementsDialog 同形** (`onAction`/`onDrag`/`onVar`/`onClose`/`setVar`/`getVar`/`listVars`/`watchVars`/`focus`/`activate`)。既有驱动基本可以直接搬用。
- **没有的东西**: 模态结果 / navigator 流程 / 虚拟键盘 / 宿主热键表 / 也不会出现在 `Agent.dialogs()` 中。1 面板=1 画面，切换靠重新调用 showJson(交叉淡化用 2 张图层+`[trans]`)。
- **默认不接收键/手柄**。只对想生效的画面流 `keyDown/keyUp/text`(返回值=是否消费)。
- 改变图层的图像尺寸后调用 `notifyResized()`。`invalidate()` 是显式全面重绘(通常不需要)。
- 主题 / 显示语言 / `registerImage` 的 mem:// store 在整个进程共享(面板也立即反映)。

---

## 4. 事件 (子类化 ElementsDialog 后 override)
```tjs
class D extends ElementsDialog {
    function onAction(id, payload)      { /* 値変化 / click。payload=値(buttonはvoid) */ }
    function onClose(action)            { /* teardown 完了。action=閉じた button id(外部要因は空) */ }
    function onScreen(name)             { /* フロー: 画面 enter */ }
    function onScreenLeave(name, act)   { /* フロー: 画面 leave */ }
    function onDrag(e)                  { /* ドラッグ。e=%[id,phase,x,y,dx,dy,startX,startY,modifiers] */ }
}
```
- `onAction` 在**所有 button 点击与 state widget 值变化**时触发(TVPPostEvent 经由)。
- **`onDrag`** 对画面 JSON 中写了 `"drag_events": true` 的 widget 的 按下→移动→松开 触发。
  `e.phase` 是 `"begin"` / `"move"` / `"end"`(因为 TJS Dictionary 没有 bool，所以用字符串)。
  坐标是画面 JSON 的坐标系。积存的 `move` 折叠到最新 1 条(`begin`/`end` 不折叠)。
  ⚠ **只是要让抓住的图片跟手的话不需要 `onDrag`**: 在 widget 上写
  `"drag_at_var": "名字"` 即可把位置写成 `"x,y"` 变量，canvas 子元素的 `"at_var"` 只
  要插入同一个变量就能跟随(在 C++ 内完成，帧同步)。`"drag_bounds": [x,y,w,h]` 还能
  限制可动范围。`onDrag` 用于「在哪里松开」等**判断**。
- **子类必须调用 `super.ElementsDialog()`**(构造函数)。不调用 native 实例就不会初始化。
- 宿主→UI 的值反映: **`dlg.setVar(name, value)`**(订阅了 `vars`/`text_var` 的 label 在下一帧更新)。用于软键盘的输入显示等。
- 程序化移动焦点: **`dlg.focus(id)`**(input_box 是编辑焦点=插入符+接收 text。用于用 `at_var` 的 park/unpark 重组画面后的输入目标移动。不检查 id 是否存在/非激活时返回 false)。initial_focus / focus_by_id 对 input_box「必须点击一次才生效」的问题已修复。

---

## 5. 多画面流程 (navigator) 与常驻菜单
在 1 个 overlay 上迁移多个画面 (JSON)。各画面的 top-level `"transitions"` 定义「关闭触发 action id → 下一步」:
- target 词汇: `"name"`(push・不需要尖括号)/ `"<back>"`(pop)/ `"<replace:name>"` / `"<stay>"` / `"<exit>"`(或空)。未定义 action 回退为 entry=exit / 子=pop。
- 画面迁移的按钮是 **`close_on_click:true` + `transitions`**。当场动作(不关闭)的按钮不写 `close_on_click`(仅 `onAction`)。
- **画面切换效果** (krkrz overlay 已配线・CPU 合成，所有 DrawDevice 行为一致): 把 entry 写成 object 形式 `%[target:"s2", effect:"fade", duration:300]` / `%[target:"<back>", effect:"universal", rule:"rule.png", vague:64, duration:500]`。`rule` 是灰度图像(值越小的像素越先切到下一画面)，解析顺序=声明画面相对→Storages→autopath。不支持的 effect / rule 缺失时警告+立即切换(rule 缺失时回退 fade)。演示: `src/core/data/elements_flow/`。
- **退场 (exit) 演出**: 给元素的 `"animate"` 加上 `"on":"exit"` 后，关闭/迁移时先播放演出再 finish(session 内自动协调)。TJS `ElementsDialog.close()` 也会触发(演出完成后关闭，不解析 transitions，流程结束)。`"animate"` 是用 `from`/`to`/`frames`/`easing` 指定 move/scale/rotate/fade 的部件演出(触发 `on`: enter(默认)/focus/select/exit/hover/change)。

```tjs
// ブロッキング複数画面: マニフェスト or インライン辞書
var r = dlg.showFlow("ui/app.jsonc");
var r = dlg.showFlowScreens(%[ "menu": '{...}', "settings": '{...}' ], "menu");

// 常駐(非ブロッキング)メニュー: 出しっぱなしで背景動作と併存
dlg.startFlow("ui/menu/app.jsonc");   // 即 return(戻り値=起動成否)
// dlg.active … この dlg が今アクティブか(getter)   dlg.close() … 閉じる
```
实例: `data/startup.tjs` 的 `FlowMenuDialog` + `data/ui/menu/*.json`。

---

## 6. 输入・焦点・模态・多实例
- **投递优先级**: `最上位热键(System.registerHotKey・泵入口) > 模态(全部消费) > 宿主热键(ElementsDialog.registerHotKey・旁路) > 焦点面板(handled 直通) > 游戏`。
- **多实例可同时显示**(z-order。开头=最底层/末尾=最顶层)。各实例有 `modal` 标志。
  - `modal=true`(showJson 默认/showModal*/showFlow): 独占全部输入(不传给下方・游戏)。
  - `modal=false`(startFlow/startFlowScreens、showJson 系可用第 3 参数指定): 未命中的输入**直通**到下方/游戏。
- **三种用途**: 模态 `showJson(json)` / **操作面板 `showJson(json, true, false)`**(键/手柄送达面板，未处理部分直通宿主。手柄十字=焦点导航/A=确定) / 仅显示用 HUD `showJson(json, false)`(完全不接收键)。
- **键盘焦点**: modal 或 `wants_focus` 的最顶层持有。后打开的 focus-grab 自然到前面，关闭后回到之前。文本输入 widget 获得焦点时即使 grabFocus=false 也能收到键/文本(focus_consumes_text 回退)。
- **最上位热键 `System.registerHotKey(key, mods, callback)`** / `System.unregisterHotKey(key, mods)`: 在事件泵入口对照，所以是**模态显示中・文本输入中也有效**的唯一层级(比下面的 ElementsDialog.registerHotKey 更上游)。callback 返回 `false` 则不消费，直通到普通 dispatch。repeat 只消费・up 只对照 key。模态的有无用 **`ElementsDialog.modalActive`**(只读・不含常驻 overlay)判定。WINVER / SDL3 两个构建都可用(WINVER 于 2026-09-26 配线)。
- **宿主热键 `ElementsDialog.registerHotKey(key, shift=0, duringTextInput=false)`** / `unregisterHotKey` / `clearHotKeys`: 注册键(VK_PAD*・VK_RBUTTON 等鼠标也在同一空间)不送到面板，直达 `Window.onKeyDown/onMouseDown`(旁路方式・无专用事件)。文本输入中默认抑制(`duringTextInput=true` 时有效)。模态中无效。用于确保 ESC/PgUp/PgDn 等「shell 必须收下的键」(实例=demolib DemoShell)。
- 用 `input`(top-level)设置方向键/手柄导航(`arrow_focus_nav` / `dpad_mode` / `shortcuts`〔key/pad→id〕/ `pad_bindings`)。默认 bind: A=Enter / B=Esc / X=Shift+Tab / Y=Tab / D-Pad=方向键。`"bindings": [{key|pad|mouse|wheel, action}]` 可替换 named-action(`"none"`=消费并禁用，`"passthrough"`=不消费直通宿主=常驻 overlay 声明「这个输入属于下面的游戏」用)。pad 名除面键外还可使用 `"lb"`(`"l1"`)/`"rb"`(`"r1"`)/**`"lt"`(`"l2"`/`"lt_click"`)/`"rt"`(`"r2"`/`"rt_click"`)**/`"l3"`/`"r3"`/`"back"`/`"start"`/`"dpad_*"`(两个扳机要经过 krkrz 侧的 VK_PAD7/VK_PAD8 转换后才会送达)。面键有刻印(`"a"`/`"b"`/`"x"`/`"y"`)和位置(`"face_south"`/`"face_east"`/`"face_west"`/`"face_north"`)两套，按下一次两边都会送达。显示侧的 `pad_icon` 的 name 也有同样两套，所以分配与显示用同一基准配对(任天堂系 X/Y 的位置与 Xbox 相反)。
- **列表用 `list` 组合(行模板)**: `"rows": N` + `"row": {…树…}` + `"row_size"`/`"pitch"`。字符串值的 **`#index` 展开为行号**(`"id": "row#index"` / `"visible_var": "rhov#index"`)，带 `text_list_var` 等的元素会自动插入 `"index"` 和 `"index_offset_var"`(= 成为«窗口»)。行内的 widget 先接收点击，谁都没接收就作为**行点击**触发 `onAction(id, 数据index)`。传入 `count_var` 后，**没有数据的行连绘制和命中都消失**。hover/选择用每行标志(`row_hover_var`/`row_select_var` → 用 `visible_var` 接收)或宿主侧拾取 `hover_var`/`select_var`(`onVar`)。
- **滚动条用 `atlas_scrollbar`**: 把 `"thumb"`(可 9-slice)+ `"track"`(可省略)直连到 `index_offset_var`(+`count`/`count_var`，可见行数用 `visible` 数值或 `visible_count_var`〔⚠ 从旧 `visible_var` 改名: 与全 widget 共用的显示/隐藏键冲突〕)或 `value_var`。滑块长度按「可见行数 ÷ 总件数」比例，**沟槽点击翻页・滚轮・拖拽**都内置。只插入与 `list` 相同的 `index_offset_var` 即可联动。两端的增减按钮是 `dec`/`inc`(与 atlas_slider 相同键，送进量=与滚轮相同)。
- **滑块素材的 9-slice / 1 个变量驱动多张**: `atlas_slider`/`atlas_scrollbar` 的 `"thumb"` 用 `{"rect":…,"insets":[l,t,r,b],"size":[w,h]}` 可以不压扁两端盖延伸。canvas 子元素用 `"at_var_offset": [dx,dy,dw,dh]` 可以用 **1 个 `at_var` 驱动多张**(上盖+躯干+下盖等)。
- **变量既能读也能拾取变化**: `setVar` 的反向是 **`getVar(name)`**(未知返回 void)，列表是 **`listVars()`**(`name`/`value`/`usedBy`=`%[id,kind]`)。变化通知只送达**实现了 `onVar(name, value)` 的对话框**(未实现则无成本)。`vars_on_hover` / `vars_on_focus` / slider 的 `value_var` / `drag_at_var` / 列表的 `index_offset_var` 等**画面侧写入的值也在同一个 store**，都能读到 → 可以构成「**图片用宿主侧的图层、命中判定只交给 elements**」并把 hover 接到宿主处理。通知延迟 1 帧+同名折叠为最新 1 条(需要当前值就用 `getVar`)。想缩小对象范围用 `dlg.watchVars = ["a","b"]`(`"*"`=全部 / `[]`=停止 / `void`=默认)。
- **named action 的通知形式**: `bindings` 中写了**非内置**名称时，通知是 `onAction(id, payload)` 的 **`id` 固定为 `"<action>"`・起的名字在 `payload`**(`onAction("<action>", "prev_page")`)。内置名(`accept`/`cancel`/`nav_*`/`focus_*`/`page_*`/`scroll_*`/`none`/`passthrough`)在会话内处理，不会到宿主。**以为 id 会来自己的名字而编写的话，那个输入只会默默无响应**(用滚轮替换时容易踩到)。
- **无焦点时按方向键进入的位置**: `input.arrow_focus_enter` = `"first"`(默认・收集顺序的开头)/ `"directional"`(按下方向的边缘。按右键则是最右)。用于不放置 `initial_focus` 的确认对话框。
- 多个 ElementsDialog 的 ownership: `close()` 只关闭**自己的实例**(`IsHandlerActive(this)` 门控)。阻塞 pump 也用自己 handler 判定结束。

---

## 6.5 朗读 (屏幕阅读器)
显示中的画面会被 OS 的屏幕阅读器(讲述人 / VoiceOver / Orca)**无需任何操作就能读出**(名称取自 text / labeled_row.label / group.title 等，角色取自 type，自动。输入框按字符・单词・行)。整体用法见 umbrella 的 `doc/guide/Accessibility.md`。
- **画面 JSON 的 `"a11y"` 键** (全 widget 通用): 字符串=名称的短缩形，字典=`label`/`label_id` (名称) / `description`/`description_id` / `role` (`"heading"` 等覆盖) / `value_var` / `live` (`"polite"`/`"assertive"`、朗读 text_var 的变化) / `hidden` (连同子元素一起排除)。top-level `"a11y": {"title"|"title_id"}` = 画面名。**只有图片的按钮 (`sprite_button` / `atlas_*`) 没有文本，必须给名称**。从 TJS 字典传入时 true 会变成 1，但 bool 键也接受数值。
- **static** (整个类): `announce(text[, assertive])` (朗读任意语句。AT 未连接也接受) / `a11yActive` (只读。Windows 在窗口成为前台前为假) / `onA11yActiveChanged(active)` (给类赋函数) / `a11yMode` (`"auto"`/`"off"`) / `a11yLabel` (根的名称)。
- **游戏本体 (绘制在 Layer 上的 UI)**: `setGameA11y(nodes[, focus])` (整体传入节点表。`%[id, role, name, value, states, rect=primary 坐标, parent, num_*]`) + `onGameA11yAction(id, action, arg)` (本体不移动焦点 → 改变状态后重新调用 setGameA11y) / `clearGameA11y()` / `a11yLayers = true` (自动挂载焦点链的 Layer。名称=hint，给 Layer 挂 `a11yName`/`a11yRole`/`a11yValue`/`a11yStates`/`a11yHidden`/`onA11yAction` 补充)。游戏的节点在对话框之下・模态中隐藏。
- ⚠ 都是 static，所以**离开场景时要还原** (`clearGameA11y()` / `a11yLayers = false` / `onGameA11yAction = void`)。对象只有主窗口 (`showModalJson` 的专用窗口・第 2 张及以后的 Window 不支持)。
- 实例: `data/a11y` (候选值用 setGameA11y、按钮类用 a11yLayers、面板的 `"a11y"` 键)。验证见 §8 的 `.a11y` / `.a11ylog` / `.a11ydo`。

---

## 7. 坑点 (源自 memory・重要)
- **DrawDevice 注册时机**: 启动直后(首帧之前)overlay renderer 未注册，**`showJson` 有时返回 false**。首次显示延迟到 `Window.onContinuousHandler` 等，**重试直到成功**(参照 `data/demolib`)。[[reference_elements_dialog_drawdevice_timing]]
- **GL DrawDevice 上不显示**: 宿主解析没有跟随当前设备时，GL 画面上面板不显示/无法操作。引擎已修复，但注意演示侧的「面板重试自毁(shellClosePanel 会消掉 pending)」。[[reference_elements_on_gl_drawdevice]]
- **尺寸**: `size` 是**上限**，fit-to-content。无法全屏化(有 BeginScreen 实现的固定值)。已知: size 的 peek 会误中 widget "size" 属性。[[reference_elements_overlay_dialog_sizing]]
- **焦点夺取 / 通用热键**: ✅已解决(2026-08-11)。操作面板用 `showJson(json, true, false)`+宿主的必需键用 `ElementsDialog.registerHotKey` 确保(§6)。旧的回避策 grabFocus=false 用于仅显示 HUD。[[project_elements_global_shortcut]]
- **子类必须 `super.ElementsDialog()`**。`showFile` 有 autopath 不支持的场合(注意相对解析)。
- **子类内访问 static 用 `global.ElementsDialog.xxx`**。裸写 `ElementsDialog` 会作为父类引用，`ElementsDialog.focusRing = false` 等会报「找不到成员」。
- **输入/导航/部分重绘的排查用 `-navlog`**(只要指定就生效)。带 ms 输出焦点移动・cursor-warp・手柄方向键的到达，超过 100ms 的帧的分段明细(`slow frame`)、栅格每次的「能否部分重绘/原因」(`raster partial=` / `no-partial:`)。测量画面=`data/elements_audit`(`-audittest` 自动巡回，并用 `-ignoremouse=yes` 不会被真实鼠标打扰)。
- **觉得绘制重时**先看 `ElementsDialog.renderStats` 的差值(`renderCount` 闲置时是否在增加)。`data/elements_bench` 有按更新模式区分的测量画面。overlay 绘制的支配项是文本的栅格化，相同内容的文本会自动位图缓存(每帧内容变化的 HUD 计数器故意不缓存)。
- **case-name 规约**: 共享/公开仓库(krkrz_dev/elements)中**不要写案件专有名称**。elements 仓库的注释等把宿主写成「使用 SDL 的宿主应用」等通用表达。[[feedback_elements_repo_project_agnostic]] [[feedback_no_case_names_in_shared_repo]]

---

## 8. 运行验证 (Agent / REPL)
GUI 用 `krkrz-repl` skill 的文件通道 + Agent API 驱动・目视确认:
- `Agent.dialogs()` — 活动对话框数组(index/modal/active/screen/rect)。
- `Agent.dialogClick(i, id)` — **按 id 启动按钮**(不需要坐标・可靠)。`Agent.click(x,y)` 是按坐标。
- `Agent.text(str)` — 向活动对话框输入文本(input_box)。
- `Agent.captureScreen(path)` — 含 overlay 的实际画面 PNG(下一帧)。→ 用 Read 目视。
- 点命令: `.dlg` / `.dlgclose` / `.click X Y` / `.cap`。
- 朗读: `.a11y` (朗读树 JSON = `Agent.a11yTree()`) / `.a11ylog [N]` (大致会读成什么) / `.a11ydo <node> <action> [arg]` (走与 AT 相同的路径操作 = `Agent.a11yAction`) / `.say <text>`。没有屏幕阅读器也能确认。
- 验证注意: REPL eval 是表达式求值。持久变量用 `global.x = ...`。多重 primary layer 不可用(第 2 张及以后用 `new Layer(win, primary)`)。详见 skill `krkrz-repl`。

---

## 9. 实现位置 (深入挖掘时)
- TJS `ElementsDialog` 绑定: `common/visual/elements/DialogIntf.cpp`(showJson/showDict/showFlow/startFlow/close/onAction/onClose/setVar/registerFont/`active`/`defaultFontFamily`/`language`/`focusRing`/`renderCache`/`partialRedraw`/`renderScale`/`renderStats` 等)。
- 管理器: `common/visual/elements/`(`tTVPElementsDialogManager` = z-order 实例列表)。
- 渲染器提供口: `iTVPDialogRenderer`/`iTVPDialogRendererHost`(tp_stub 公开)。SDL=`SDLDialogRenderer` / OGL=`OGLDialogRenderer` / WINVER=`D3D11DialogRenderer` / 独立窗口=`WinElementsModalRunner`。
- JSON→UI: elements_modal(`json_layout.cpp` / `navigator` / `overlay_session`)。面向插件的 C ABI: `tp_dialog_service.h`。
- 相关 doc: `doc/Gamepad.md`(pad↔key)、`doc/D3D11Migration.md`(DestRect)、`external/elements/external/elements_modal/README.md`。

## 相关 skill
- `tjs2`(TJS 语言)/ `krkrz`(引擎本体类 API)/ `krkrz-repl`(REPL・Agent 驱动・captureScreen)。