# Elements UI 机制的整体图景

吉里吉里Z 的 [ElementsDialog](../../reference/ElementsDialog.md) ( 基于 Elements 的 UI ) 由**4 个层**
叠加而成。这里汇总了哪个层里有什么、应该修改哪个层、应该阅读哪些文档。
具体用法请参阅 [对话框 ( 指南 )](../../guide/ElementsDialog.md)，
API 请参阅 [ElementsDialog 类参考](../../reference/ElementsDialog.md)。

## 层结构

```
┌─────────────────────────────────────────────────────────────┐
│ ④ ゲーム / TJS 側の UI コード                                  │
│    画面の出し入れ、ゲーム状態との接続、画面遷移の方針           │
│    ※ 共有の枠組みは無く、プロジェクトごとに書かれている         │
├─────────────────────────────────────────────────────────────┤
│ ③ krkrz 本体 ( src/core/common/visual/elements/ )             │
│    TJS ElementsDialog クラス / DrawDevice への描画接続 / 入力ルーティング │
│    複数インスタンスと z-order / モーダルの nested ループ         │
│    ホスト資源との接続 ( Storages・フォント・ソフトキーボード )    │
├─────────────────────────────────────────────────────────────┤
│ ② elements_modal ( external/elements/external/elements_modal ) │
│    画面 JSON の仕様と構築、変数 store、named action、画面遷移     │
│    overlay_session ( 描画先バッファと入力を受け取るだけの口 )     │
│    ※ 吉里吉里に依存しない。単体アプリからも同じ JSON が動く      │
├─────────────────────────────────────────────────────────────┤
│ ① elements ( cycfi/elements の派生 )                          │
│    ウィジェットの土台、レイアウト計算、フォーカス、ThorVG 描画    │
└─────────────────────────────────────────────────────────────┘
```

**①与②可以脱离吉里吉里Z 独立运行**。画面 JSON 在单独的宿主应用中也能同样地
显示与操作，③的作用则是把它搭载到游戏画面之上，并与游戏的输入和资源连接起来。

## 应该修改哪个层 ( 速查表 )

| 想做的事 | 要修改的层 | 具体位置 |
|---|---|---|
| 更改画面的外观、布局、文案 | 画面 JSON | 项目的画面 JSON |
| 增加控件 / 给现有控件添加属性 | ② | `json_layout.cpp` + elements_modal README |
| 更改变量联动、输入绑定、画面迁移的规格 | ② | 同上 |
| 控件绘制本身、布局计算、焦点移动 | ① | elements 本体 ( `lib/` ) |
| 增加 TJS 的 API ( `ElementsDialog.*` ) | ③ | `DialogIntf.cpp` + `doc/manual/ElementsDialog.manual.tjs` |
| 显示目标 ( DrawDevice ) 与输入路径、多个实例的处理 | ③ | `ElementsDialogManager.cpp` |
| 画面如何显示与收起、如何与游戏状态连接 | ④ | 游戏侧脚本 |

犹豫时的判断基准是“**这个功能在没有吉里吉里Z 的情况下是否仍然有意义**”。
如果有意义就是②或①，如果牵扯到游戏侧的情况就是③或④。

## 数据流

**绘制**：在游戏帧的末尾从 `DrawDevice::Show()` 调用 `PaintOverlay`，
② 绘制到像素缓冲区，③ 再将其转送到各 DrawDevice 的纹理 ( SDL / OpenGL /
D3D11 ) 并显示在游戏画面之上。不需要重绘的帧会直接呈现上一次的纹理，
只重绘发生变化的矩形。

**输入**：窗口的鼠标 / 按键 / 手柄输入由③拦截，并传递给正在显示的对话框。
只有②未处理的输入才会流向游戏 ( 图层 ) ( 非模态时 )。

**值**：画面 JSON 中的变量挂在一棵 store 上。从 TJS 可以用
[setVar](../../reference/ElementsDialog.md#setvar) 写入，用 [getVar](../../reference/ElementsDialog.md#getvar)
读取，用 [onVar](../../reference/ElementsDialog.md#onvar) 接收变化。按钮按下与值更改通过
[onAction](../../reference/ElementsDialog.md#onaction) 送达。**日常使用中，这 4 个就是③与④
之间的全部接口** ( 此外还有图像与图集的替换、会话共享变量的读写等
“只有宿主才能做的事”的入口。见下节 )。

## 设计方针：让 UI 的处理在画面数据侧完结

鉴于多个项目开始在④中各自编写独有的 UI 框架，我们采取了这样的方针：
**让 UI 的处理在②与画面 JSON 中完结，④只负责“调用 / 供给值 / 执行动作”**。
划界的准则是“**是否会触及游戏的状态**”。

| 画面数据侧 ( ②+ 画面 JSON ) | 宿主侧 ( ③④ ) |
|---|---|
| 画面迁移、标签页、列表的滚动与选择 | 设置值与存档数据的实体 |
| 值的整形与区分显示、焦点、演出 | 存档 / 读档的执行、SE 的实际播放 |
| 跨画面保持值 ( `shared_vars` ) | 与宿主对话框机制的协调 |

因此，下面这些**无需编写宿主的回调，仅靠画面 JSON 就能运行**。

- **`"shared_vars": ["cfg_*"]`** — 把匹配的变量跨画面保持下来
  ( 在设置画面中来回切换标签页，滑块也不会回到原位 )
- **`"value_var"`** — 让 `checkbox` / `toggle_button` / `slide_switch` 的 ON/OFF 与变量联动
- **`"image_var"`** — 用变量替换 `image` 的图像本身 ( 存档列表翻页等 )
- **可替换图集** — 保持同一画面不动，只替换图像集合 ( CG 鉴赏的分组标签页等 )

宿主侧剩下的工作只有“写入存档数据”，其入口是
[getSharedVars](../../reference/ElementsDialog.md#getsharedvars) /
[setSharedVar](../../reference/ElementsDialog.md#setsharedvar) /
[clearSharedVars](../../reference/ElementsDialog.md#clearsharedvars)，
图集替换是 [setAtlasImage](../../reference/ElementsDialog.md#setatlasimage)。

## 文档地图

| 文档 | 层 | 内容 |
|---|---|---|
| [对话框 ( 指南 )](../../guide/ElementsDialog.md) | ③④ | 显示模式、流程、列表、变量、输入绑定的用法 |
| [ElementsDialog 类参考](../../reference/ElementsDialog.md) | ③ | TJS API 的全部成员 |
| [ElementsDialog.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/ElementsDialog.md) | ③ | **本体侧的实现 SSOT**。DrawDevice 连接、输入路由、多个实例、部分重绘、测量 |
| [elements_modal README](https://github.com/wamsoft/elements/blob/develop/external/elements_modal/README.md) | ② | **画面 JSON 规格的 SSOT**。控件列表、变量联动、主题、图集、迁移、演出 |
| [elements 仓库](https://github.com/wamsoft/elements) | ① | 库本体 ( 派生来源是 cycfi/elements ) |
| [手柄输入](gamepad.md) | ③ | 手柄的按键转换 ( 对话框的手柄操作也构建在这之上 ) |
| [虚拟光标位置](https://github.com/wamsoft/krkrz_develop/blob/master/doc/VirtualCursor.md) | ③ | hover 判定与光标参照的基准。按键 / 手柄的导航不会移动实际的 OS 光标 |

## 术语

- **overlay** … 叠加显示在游戏画面之上的形式。非模态和模态默认都是这种形式
- **独立窗口 modal** … 另外打开 OS 窗口并以阻塞方式显示的形式
- **流程 ( navigator )** … 让多个画面 JSON 相互迁移的机制。迁移目标由画面 JSON 侧的
  声明决定，宿主不编写迁移
- **画面 JSON** … 一个画面的布局定义。也可以用 TJS 的 Dictionary 编写
- **变量 store** … 在画面中共享的带名称的值。以字符串形式持有
- **会话共享变量** … 跨画面保持的变量。由画面 JSON 的
  `"shared_vars"` 声明“携带哪些值” ( 不需要宿主实现 )
- **named action** … 分配给按键 / 手柄 / 鼠标的命名操作。内置名称在
  对话框内处理，其他名称则通知给宿主
