# 调试

## 关于应用程序的调试

调试是指定位并修复应用程序中的 bug (功能不全或产生意外行为的原因) 的工作。

吉里吉里具备若干调试支援功能，使用这些功能来调试应用程序。下面说明其方法。

## 调试消息输出

吉里吉里提供了若干用于支援调试的消息输出目标。

- **[控制台](Console.md)**  
  从命令行启动时，可以把吉里吉里的系统以及用户脚本输出的各种调试用消息显示在终端上。

特别是在控制台中，会显示用户程序通过 [Debug.message](../reference/Debug.md#message) 在程序内输出的消息。可以在程序中的任意位置调用该方法，显示变量的内容，观察运行中变量的内容。

关于消息显示的方法以及把日志写入文件的方法，请参阅[命令行选项](CommandLine.md)的“调试相关选项”与 [Debug 类](../reference/Debug.md)。

## 调试模式

在[命令行选项](CommandLine.md)中指定 `-debug` (把“调试模式”置为 ' 有效 ') 后，可以让吉里吉里以调试模式运行。

在调试模式下，TJS2 的运行速度会变慢，但一些便于调试的功能会被启用。

- **类型信息追踪功能**  
  TJS2 对象的相关信息会得到增强。
  
  非调试模式下，例如即使想获取某个对象的方法 obj.doAction 的信息，
  
  ```
  コンソール : obj.doAction = (object)(object 0x0279E130:0x01EB0BD4)
  ```
  
  也只能得到以上结果；而在启用调试模式时，则可以得到
  
  ```
  コンソール : obj.doAction = (object)(object 0x0279E130[(function) MyClass.doAction]:0x01EB0BD4[instance of class MyClass])
  ```
  
  这样的类型信息。(':' 分隔的 2 个部分中，前面部分是对象的类型，后面部分是该对象运行的上下文)。
  
  使用调试器进行跟踪时，这几乎是必需的选项。
  
  此功能 (在当前版本中) 会在对象转换为字符串的所有过程中生效。
- **对象泄漏检测功能**  
  会在退出时对未被删除 (未被释放) 的对象发出警告的功能将被启用。
  
  TJS2 本来通过垃圾回收功能自动删除创建出的对象，不需要显式指示删除。但是，由于插件或吉里吉里引擎本体的 bug、循环引用等原因，对象可能会保持未被删除的状态 (泄漏)。
  
  在调试模式下，到了退出时仍未释放的对象会被写入控制台的日志文件。
  
  哪怕只有 1 个对象未被释放，由于与该对象相关的所有对象都会被检出，日志文件可能会变得非常巨大，请注意。
  
  
  
  [System.exit](../reference/System.md#exit) 方法是以接近强制结束的形式结束应用程序，用该方法结束应用程序会导致许多对象泄漏、记录大量日志，请注意。
  
  > **注：**
  > 循环引用是指 A 引用着 B、B 引用着 A 这样的状况。
  >
  > 例如，以下脚本会生成循环引用。
  >
  > ```
  > var a = %[], b = %[];
  > a.b = b; b.a = a;
  > ```
  >
  > 在这种情况下，对象 a 需要 b，对象 b 需要 a。TJS2 采用的垃圾回收方法 (引用计数) 难以检出这种情况并释放对象，因此 TJS2 不会检出这种情况。这样一来，这些对象无论过多久都不会被删除 (显式地用 invalidate 运算符将其中一方的对象无效化，即可切断循环引用)。
  >
  >
  >
  > 在插件中，如果错误地处理引用计数，对象可能会泄漏。创建插件并在其中处理 TJS2 对象时，请对引用计数的处理十分注意。
- **对正在删除的对象执行脚本的警告**  
  对象在删除或无效化时，会调用 finalize 方法。
  
  对象被删除的时机在 TJS2 中“无法预知”，因此 finalize 方法可能会在奇怪的时机被调用，表现出意料之外的行为。在调试模式下，对于这种“不稳定的时机”，即未被无效化的对象被垃圾回收删除、finalize 方法被调用时，会在控制台显示警告。
  
  警告如下所示。
  
  ```
  警告: anonymous@0x016DFA7C(9)[(function) finalize]: 削除中のオブジェクト 0x0167DD44[instance of class A] 上でコードが実行されています。このオブジェクトの作成時の呼び出し履歴は以下の通りです:
                       anonymous@0x016DFA7C(13)[(top level script) global]
  ```
  
  为防止这种状况，建议用 new 创建的对象在使用完毕后，显式地用 invalidate 运算符无效化。
  
  不过，对于像 Array、Dictionary、Date 这样没有 finalize 方法，或者 finalize 方法不会引起特别问题行为的类的对象，有时不需要显式无效化。
  
  上述警告会在以下情况显示：对象在没有显式无效化的情况下即将被删除，并试图在其上下文上执行 TJS2 脚本时。
- **调用历史获取功能**  
  可以从脚本获取 TJS2 的函数 / 方法调用历史。
  
  为此使用 [Scripts.getTraceString](../reference/Scripts.md#gettracestring) 方法。
  
  当程序中间出现某些问题、不知道某方法是从哪里被调用的时候，可以使用此方法把调用历史输出到控制台等。

## 使用 VSCode 进行 TJS2 调试

吉里吉里Z 内置 **Debug Adapter Protocol (DAP)** 服务器，
与专用的 VSCode 扩展 [krkrz-vscode](https://github.com/wamsoft/krkrz-vscode)
组合使用，就能以与普通编程语言相同的感觉调试 TJS2 脚本。

### 所需环境

- 吉里吉里Z 引擎本体: 使用构建时选项 `KRKRZ_ENABLE_DAP=ON` ( 默认 ON )
  构建出的二进制文件
- VSCode 1.75 或更高版本
- [krkrz-vscode](https://github.com/wamsoft/krkrz-vscode) 扩展

旧的 `ENABLE_DEBUGGER` ( Win32 专用的基于 `WM_COPYDATA` 的独有协议 ) 已于
2026-04-25 废止，统一改用 DAP。

### 安装扩展

由于尚未在 Marketplace 公开，目前从仓库直接构建并安装。

```bash
git clone https://github.com/wamsoft/krkrz-vscode.git
cd krkrz-vscode
npm install
npm run package         # → krkrz-vscode-X.Y.Z.vsix を生成
code --install-extension krkrz-vscode-0.0.1.vsix
```

如果想在开发用的 Extension Development Host 中运行，请在 `npm run compile`
之后用 VSCode 打开本文件夹并按 **F5**。

### 启动方法

以附带 `-dap=<port>` 的方式启动吉里吉里Z。指定 `-dap=yes` 时
使用默认端口 ( 6635 )。

```
krkrz64.exe -dap=6635 path\to\data
```

在 VSCode 侧选择“运行和调试” → “创建 launch.json” → “Kirikiri Z”
后，会提供代码片段。有 `Attach` ( 连接到已启动的 krkrz ) 与
`Launch` ( spawn krkrz 并连接 ) 2 种形式。

`launch.json` 的主要设置项:

| 项目 | 类型 | 默认 | 说明 |
|---|---|---|---|
| `request` | string | — | `attach` 或 `launch` |
| `host` | string | `127.0.0.1` | DAP 服务器的主机 |
| `port` | number | `6635` | TCP 端口 |
| `stopOnEntry` | bool | `false` | 在连接后的第一个 VM 行处停止 |
| `program` | string | — | `launch` 时启动的 krkrz 可执行文件绝对路径 |
| `data` | string | — | `launch` 时的 data 文件夹 |
| `args` | string[] | `[]` | 额外的 krkrz 选项 ( 例: `["-debug", "-loglevel=DEBUG"]` ) |
| `cwd` | string | program 所在的目录 | 工作目录 |
| `env` | object | `{}` | 环境变量的添加 |

### 支持的功能

- 断点 ( 支持条件断点 / log point )
- 单步执行 ( Over / In / Out )
- 暂停 / 继续
- 多帧调用栈 ( 显示各帧的 Locals / `this` / Globals )
- 变量 inspect ( Object / Array / Dictionary 可展开子级 )
- 在 Watch / Hover / Debug Console 中进行表达式求值
- 异常停止 ( Uncaught Exceptions 过滤器 )
- 在 TJS 的 `debugger;` 语句处停止
- 将 TJS 的日志输出转发到 Debug Console

### 已知限制

- 只有 TJS VM 执行的 `.tjs` 脚本的行才能设置 BP
  ( 不经过 TJS VM hook 的行无法设置 BP )
- 异常 / BP 停止期间，整个 krkrz ( 绘制、ContinuousHandler 等 ) 都会停止。
  解除停止可以通过 VSCode 的 Continue / 停止按钮，或吉里吉里Z 内置的
  [REPL](Console.md#repl) ( 停止期间 REPL 输入也会被处理 )
- 对条件断点 / Watch / Hover 的求值结果对象进行的 mutation 不会
  反映到帧上 ( 因为经由 snapshot )
- `setBreakpoints` 的 verified 始终返回 `true`，因此即使把 BP 放在
  不存在的行上，也不会被检测为无效
- TJS class 名不会反映到 `exceptionInfo.typeName` ( 目前固定为 "Exception" )
- 不支持 Hit count BP

关于详细用法、扩展的构建方法以及最新的支持功能，请参阅
[krkrz-vscode 的 README](https://github.com/wamsoft/krkrz-vscode)。
TJS2 的语法高亮也随该扩展一同提供。
