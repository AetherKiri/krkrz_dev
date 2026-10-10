# 向 krkr 案件集成 Elements UI — 集成参考文档

`elements` skill 本体是 **Elements 单独的使用方法** (Dialog API / 布局 JSON /
navigator)。这里是**实际搭载到吉里吉里Z 的游戏 (KAG/kag 机制) 上时**的
集成知识 — 汇总 engine 侧的事实与约束、TJS 配线的类型、生命周期的陷阱、
素材的搜索、验证手段、未解决事项。

**案件固有的值 (画面名・kag 属性对照表・驱动列表) 请查看各案件的资料**。
这里写的只是所有案件共通的部分。

## 0. 层构成

```
 KAG シナリオ / kag / SystemAction        ← ゲーム進行・設定値の実体
        │ syshook / kag.process() / kag.*
 画面ドライバ (案件ごと。例 uielements.tjs)   ← 「押したら何をするか」を書く層
        │ extends / show() / setVar()
 基盤 TJS (例 ElementsUI.tjs)               ← 触る頻度は低い。基底クラスと初期化
        │ showFile / onAction / onClose
 native ElementsDialog クラス (elements_modal)      ← engine
        │ 読む
 画面資材 <name>.jsonc + atlas PNG          ← uitool で生成
```

要点是分开基盘与画面驱动。基盘 = 即使在不支持 Elements 的 exe 上也不会坏掉的
防护与共通基类，驱动 = 案件的行为。

## 1. 启动与存在判定

- **类名是 `ElementsDialog`** (2026-09-04 从旧名 `Dialog` 改名。因为与游戏侧
  TJS 的类名实际冲突。没有兼容别名)。与旧 exe (类名
  `Dialog`) 混用的期间，初始化时用
  `if (typeof global.ElementsDialog != "Object" && typeof global.Dialog == "Object") global.ElementsDialog = global.Dialog;`
  归拢到新名后，以后只用 `ElementsDialog` 即可两全。
- 加载改为条件式以保护不支持的 exe:
  `KAGLoadScript("...") if (typeof global.ElementsDialog == "Object");`
- **字体注册 (`setupFont()` 相当) 在 show 之前做一次**。krkr 无法生成多个文件夹的
  字体列表，所以采用**在一处批量注册**的方针
  (engine 侧是 `fonts.json` 声明 + 首次使用时延迟加载，glyphware 已统一)。

## 2. 显示路径的选择 (最先决定的设计决策)

- **非模态 (`showFile` / `showJson` / `showDict`) + 回调**是原则。
  `showModal*` 会进入嵌套泵，因此 **REPL 或事件会停住**。
- `{"type":"button","close_on_click":true}` 的决定通过 **`onClose(action=按钮id)`**
  送达 (不是 `onAction`)。Esc/× 是 `action=""`。选择系菜单这种形式是定式。
- **TJS 子类需要显式 `super.ElementsDialog()` (旧 exe 是 `super.Dialog()`)**。
  没有显式构造函数就 `new` 的话，显示和导航虽然有效，但
  `onAction`/`onClose`/`onScreen` 完全不来
  (因为 engine 侧 `Owner` 只能通过构造函数设置)。
- **`showFile` 不参与 Storages 的 autopath 搜索** — 只写文件名会
  失败。要带路径 (`"system/foo.jsonc"`) 传入。★engine 侧 需调查
- **overlay 的显示尺寸** — overlay 路径没有尺寸参数，画面 JSON 的
  top-level `"size"` 是上限。**不写 `"size"` 则以 surface (游戏画面)
  全面为上限**，所以全屏级的画面也能正常组建 (旧: 固定 400x220 导致
  被裁剪)。实际尺寸由 fit-to-content 决定 (`size` 是上限指定)。
  top-level `"size"` 的提取**只看深度为 1 的键** (2026-08-29 修正、
  src/core `7352157f`)。以前会先拾取嵌套数组 `"size"` — `spacer` 的 `[w,h]` 或
  9-slice thumb 的 `[w,h]` — 导致对话框缩成那个大小。

## 3. 乘到 KAG 的对话框 / 面板框架上 (宿主图层方式)

为了几乎无改造地使用既有的 `openDialog` / `showPanel` 机制，**把 Elements 的
session 用透明的 DialogLayer / PanelLayer 派生 (宿主) 包装**。

- 宿主整体透明 (`hitType=htMask`, `hitThreshold=0`)，所以会吸收 widget 外
  漏过的输入，防止漏到下方的 UI。KAG 侧的键类输入也会被遮蔽。
- **`finalize()` 中必须执行 native 的 close**。`closeDialog` 批量・
  强制销毁・直接 invalidate 无论哪条路径都不能把 Elements 侧留下。
- **双重关闭幂等化**: Esc 由 Elements 侧 (`onClose`) 还是 KAG 侧
  (`onKeyDown`/`onRightClicked`) 先吃到，存在 exe 差异。
  用 `_done` 标志 + `isvalid` 保护。
- conductor 因为 `openDialog` 会 interrupt，「打开=停止 / 关闭=重启」自动成立。
- **z 顺序的结构性约束**: overlay (ElementsDialog) 是 native overlay，所以
  **总是显示在 KAG 图层群之上**。Elements 面板显示中打开旧 DialogLayer 的话，
  逻辑 z 与外观会不一致。
  → **本命是 `ElementsPanel`** (2026-09 之后的 exe): 把同一个画面 JSON 绘制到 KAG 图层的
  位图上，所以 z 顺序・`[trans]`・piledCopy 遵循图层的机制，
  这个约束本身消失 (skill 正文 §3 参照)。事件 / 变量 API 同形，所以
  驱动基本可以复用 (输入从宿主图层的 onMouse* 流向 `panel.mouse*`)。
  旧 exe 则沿用以往「旧对话框显示中临时 hide Elements 侧
  的 hook」或避免同时使用来运营。

## 4. 画面驱动的类型

1 画面 = 1 个 jsonc 非模态显示，把动作/关闭中继到派生类的
基类持有 1 个。最小接口:

| 成员 | 作用 |
|---|---|
| `show(vars)` | 显示 + 紧接着灌入的变量字典 |
| `closeScreen()` | **显式关闭**。不触发 `onClosed` |
| `setVar(name, value)` | 更新显示中的变量 store (`text_var` / `value_var` 联动) |
| `onOpen()` / `onAction(id, payload)` / `onClosed(action)` | 供 override 的 hook |

**陷阱**:

- **区分显式关闭与自动关闭**。自己关闭 (`closeScreen`) 时
  `onClosed` 不会来。只在 Esc/×/engine 原因关闭时来。
- **常驻画面的「关闭后重新显示」用状态标志保护**。`onClosed` 中无条件
  `show()` 的话，**进入游戏本编后也会复活并夺取输入**
  (别的 Elements 对话框进进出出会诱发 `onClosed`)。
  用 `wantVisible` 等持有「现在是否应该显示这个画面」，在 syshook 中切换。
- **不要把标签页切换的连带影响做成恢复处理**。「关闭当前画面再打开下一个」的方式中，
  切换时关闭的旧画面的 `onClosed` 在注册表侧吸收，与 `current` 不一致的
  忽略。

## 5. 值的传递

- 显示时用 `show(vars)` 批量注入，显示中用 `setVar()`。
- **状态用变量读写** — `atlas_toggle` / `atlas_slider` 用 `value_var`
  (`"v_" + id` 的命名规约容易处理)。`atlas_toggle` 的 `value_var` 支持需要
  **2026-08-10 之后的 exe**。
- **滑块的数值显示用 `display_var`** + 格式 (`min`/`max`/`step`/`digits`/`suffix`)。
  engine 会把格式化好的字符串写入变量，无需宿主实现。**显示会四舍五入**，所以
  驱动侧的 `payload` → 实值换算也统一四舍五入 (用向下取整的话
  会出现「显示 65% 但保存值是 64」的偏差)。格式的范围与实值的换算公式保持一致。
- **动态图像 (存档缩略图・CG) 转成 PNG 后注入**:
  ```tjs
  lay.saveLayerImage(tmp, "png");            // ★engine のデコーダは krkr の BMP を読めない
  ElementsDialog.registerImage("id", tmp);   // "mem://id" で参照
  ```
  替换只需**重新 register** 就能立即反映到显示中的画面
  (2026-09 之后的 exe。engine 用 `refresh_mem_image` 重新解码已构建的 widget)。
  旧 exe 只在 build 时读一次，所以重新 register 后
  要重新打开画面。无论哪种，**在注册前 build 的 widget 都是空显示**，所以
  首次要在打开画面前 register。

## 6. 素材的搜索与文件 I/O

- 画面素材 (`json/` + `atlas/`) 是 uitool 的运行时规定结构。案件中将
  **`uitool_project.json` 的 `runtime` 直接指向游戏的素材文件夹**，
  export 本身就变成素材 (uitool 侧 `docs/case_project_guide.md`)。
- **资源解析可以交给 krkr 低层** — 它会执行「带路径搜索 → 不带路径
  (唯一文件名) 搜索」，所以**注册搜索路径 + 保持文件名唯一**
  就够了。不需要在 elements 侧增加文件名搜索的对应 (2026-08-08 结论)。
  不过 `showFile` 本身不参与 autopath (§2)，所以调用时带路径。
- engine 的文件 I/O 已审计过健全: `ELEMENTS_FILE_IO_SUPPORT=OFF` +
  `TVG_FILE_IO=OFF` 强制 + 经 `StoragesResourceLoader` (图像/字体/JSON 全部)。
  无需新增独立的 I/O 接口。

## 7. 画面迁移与效果

- 多画面流程 (navigator / `showFlow`) 的切换可以指定 **fade / universal** 迁移
  (`rule` 图像 + `vague`)。CPU 合成，所以所有 DrawDevice 显示相同。
- **旧画面是 last_frame 方式** (finish 后的 session 无法重绘，用最近一帧的
  复制作为迁移来源)。不要期待迁移中旧画面会动。
- **退场 (exit) 演出与 `ElementsDialog.close()` 协调** (`close_after_exit`)。
  需要即时 teardown 时用 ForceClose 系。
- 想自己在 GPU 侧混合时用 `Canvas.drawTransition(front, back, phase, rule, vague)`。

## 8. 实机验证 (REPL / Agent)

```
<exe> -replfile=<チャネルdir>        # skill dev-toolkit:appctl の作法で起動・停止する
```

- `Agent.dialogs()` … 显示中对话框列表 (index / modal / screen / focused / rect)
- `Agent.dialogClick(index, "<id>")` … 按 id 启动按钮 (不需要坐标)
- `Agent.captureScreen("path.png")` … 含 overlay 的实际画面 PNG → 用 Read 目视确认
- **`Agent.dialogClick` 的遗漏**: choice_nav 组内的 `atlas_choice` 或
  多按钮 + vars_on_focus + 全屏布局时有时不会 activate。
  真实鼠标点击 (`Agent.click(x, y)`) / 真实键输入则正常。**注意自动测试的误诊**。
- **REPL 中的模态** (`inputString` / `confirm` 等) 会等待响应通道
  (默认 30 秒超时异常)。

## 9. 实际操作 (字符编码・配置)

- 案件的驱动 TJS **有时是 Shift-JIS**。**不要对 SJIS 文件直接使用 Edit/Write**
  (即使只插入 ASCII，整个文件也会被转换成 UTF-8 而损坏)。
  另外持有 UTF-8 原本，用 `iconv -f UTF-8 -t CP932` 配置。
  **全角破折号用 U+2015 (―)** (U+2014 无法转换到 CP932)。
- 布局 `.jsonc` 可以直接以 UTF-8 编辑 (支持注释・末尾逗号)。
- **发布包中 devmode 与引用目标有时不同** (看开发树的
  `sysscn/`，还是看包内的 `data/sysscn/`)。注意基盘 TJS 的同步遗漏。
- TJS 的语法见 skill `tjs2`。常踩的是**后置 `if` 只用于表达式**
  (`return X if (cond);` 是语法错误)。

## 10. 未解决 / engine 侧 TODO (★=需处理・需调查)

| 项目 | 状态 |
|---|---|
| overlay 不会铺满 surface 全面 (默认上限 400x220) | ✅ 已解决。`"size"` 未指定时以 surface 全面为上限 |
| top-level `"size"` 的 peek 误读 widget 的 `"size"` | ✅ 已解决 (2026-08-29 src/core `7352157f`)。只取深度为 1 的键 |
| `showFile` 不参与 autopath 搜索 | ★需调查。当前以带路径回避 |
| 子类没有显式 `super.ElementsDialog()` 时不触发事件 | ★需调查。当前务必书写 (2026-09-04 的类改名后构造函数名也变成 ElementsDialog) |
| `Agent.dialogClick` 存在不 activate 的条件 | ★需调查 (Agent 工具侧)。对实际运营无影响 |
| DrawDevice overlay 绘制口的通用开放 | 【预定】未着手 |
| 迁移的 GPU present 扩展 (Phase C) | 将来 optional (CPU 已足够) |