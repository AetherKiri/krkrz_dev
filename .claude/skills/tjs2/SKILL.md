---
name: tjs2
description: TJS2 (吉里吉里Z 内蔵スクリプト言語) の言語仕様と組み込みクラスのリファレンス。.tjs ファイル / *.ks (KAG) 内の埋め込みスクリプト / TJS2 コード断片 を扱う、書く、レビューする、デバッグするときに使う。JavaScript / TypeScript に似ているが文法と意味論が違うので、JS の感覚で書くと壊れる場合が多い。組み込みクラス (Array / Dictionary / Date / Math / RegExp / Exception) の API もここに集約。**呼び出されたら必ず「JS との主な違い」セクションを最初に確認し、その上で必要な詳細リファレンスを Read で取りに行くこと。** 吉里吉里Z 本体のクラス API (Window / Layer / System / Storages / Bitmap 等) や engine 内部はこのスキルの対象外。中文说明：TJS2 语言规格与内置类的参考文档，在编写、审阅、调试 .tjs 文件 / *.ks（KAG）内嵌脚本 / TJS2 代码片段时使用。触发词：TJS2 语法、脚本语言、tjs2、TJS 代码、吉里吉里Z 脚本、内置类、JS 区别、KAG 脚本。
---

> **路径基点**：本文的相对路径以 **krkrz_dev 仓库根目录**为基准。工作目录不在 krkrz_dev（如 krkrz_android / krkrz_ios 等外围仓库或项目文件夹）时，请**在前面加上 `${KRKRZ_BASE}/krkrz_dev/`** 再读取（用 `echo $KRKRZ_BASE` 确认实际路径。不同机器取值不同，因此不要写入绝对路径）。

# TJS2 语言参考文档

TJS2（TJS Just Script 2）是吉里吉里 / 吉里吉里Z（kirikiri Z）内嵌的
脚本语言。本技能是 TJS2 **语言规格** 与 **内置类** 的
信息来源，引擎本体 API（Layer / System / Window 等）不在其范围内。

## 重要：开始工作之前

1. **不要按 JS 或 Python 的习惯写**。务必先查看下方的「与 JS 的主要区别」
2. **细节请 Read 文件**。从下方的「文件索引」打开对应文档
3. **有疑问时以参考文档为准**。比起记忆或类推，更相信文档原文

## 与 JS 的主要区别（高频陷阱）

### 变量与类型

- 变量**必须用 `var` 声明**。`let` / `const` **不存在**。不能使用未声明的变量。
- 同名变量 `var` 声明两次也不会报错。第二次带有初始值时会被赋值。
- 内部类型有 6 种：`void` / `Integer`（64bit）/ `Real`（double）/ `String`（UTF-16LE，支持代理对）/ `Object` / `Octet`（二进制序列）。
- **`void` 与 JS 的 undefined / null 不同**。未初始化的变量是 `void` 类型。
- `void` 之间的比较用 `===`（等同运算符）。用 `==` 会被卷入数值比较。
- `typeof` 返回字符串 `"void"` / `"Integer"` / `"Real"` / `"String"` / `"Object"` / `"Octet"`。

### 字面量

- 数组字面量是 `[1, 2, 3]`（Array 类）
- **数组字面量的末尾逗号表示「再追加 1 个 void 元素」**（与 JS 正好相反）。`[a, b,]` 是 `count == 3`，其中 `[2] == void`。改写 `[]` 的内容时若在末尾留下 `,`，会混入空元素导致下游出错，务必去掉
- **字典字面量是 `%[ "key" => "value", "k2" => v2 ]`**（正确写法是 `%[ ... ]`，不是 JS 的 `{}`。分隔符是 `=>`，不是 `:`）
- **字典字面量的末尾逗号无害**（与 Array 行为不同，注意区分）
- 正则表达式字面量是 `/pat/flags`（RegExp 类）
- 字符串字面量是 `"..."` 或 `'...'`
- 整数可用 `0x`（16 进制）、`0o`（8 进制）、`0b`（2 进制）字面量。也可用 `123_456` 这样的 `_` 做数位分隔

### 运算符

- **`new` 必须带括号**：`new Foo()` 可以，`new Foo` 是**语法错误**
- `>>>` 是无符号右移（唯一把左操作数当作 unsigned int 处理的运算符）
- `<->` 是 **swap 运算符**（交换左右，不产生结果）
- `,`（逗号）是顺序求值运算符（从左求值，结果为最后一个值）
- 后置 `if` 运算符：`a = b if b != 0;`（仅当右侧为真时才求值左侧）
- 用 `incontextof` 替换对象的上下文（相当于 this）来创建闭包
- 用 `instanceof "Class"` 这样**以字符串指定类名**。如 `instanceof "Array"`
- **`#` 运算符获取字符编码**（`#c` 返回 `c` 首字符的 char code），`$n` 相反（字符编码 → 单字符字符串）。相当于 JS 的 `charCodeAt` / `String.fromCharCode`

### 类与函数

- 类主体：`class Foo { var x; function Foo() { ... } function finalize() { ... } property p { getter() { ... } setter(v) { ... } } }`
- **构造函数是与类同名的方法**（不是 JS 的 `constructor` 关键字）
- `finalize()` 是在 GC / 显式销毁时被调用的可省略析构函数
- 在方法内部**`new` 同一个类时要写 `global.Foo()`**（写 `new Foo()` 会引用构造函数自身而报错）
- 属性声明使用专用语法 `property name { getter() { ... } setter(v) { ... } }`，不是 JS 的 `get` / `set` 关键字语法
- 函数参数末尾写 `*` 即为可变长参数（`function foo(a, b*)` 中的 `b` 相当于 arguments）

### 布尔值

- 0 / 空字符串 / `void` 为假
- 其他字符串**若能成功转换为数值，该数值即为真伪；转换失败则为假**
- → 直接对字符串做 truthy 判定时，行为有时会与 JS 不同（例：`"foo"` 因数值转换失败而为假）

### 作用域

- 在块 `{ ... }` 内用 `var` 声明是**块级作用域**（与 JS 的 `var` 不同，不是函数作用域，行为相当于 `let`）
- 允许同名遮蔽（shadowing），离开块后即消失
- 最外层（全局作用域）的 `var` 会成为 `global` 对象的成员

### 字符串操作（按 JS 常识写容易出错）

- **`String` 类实际上不存在**（`typeof "abc" == "String"`，但实体是特化后的值）
- 获取字符编码**没有 `charCodeAt`** → 使用 **`#c` 运算符**（`c` 是单字符字符串）。调用不存在的方法会抛出运行时异常 "メンバ `charCodeAt` が見つかりません"（找不到成员 `charCodeAt`）
- 取出单字符用 `str.charAt(n)`（越界返回空字符串）或 `str[n]`（越界抛异常）
- ASCII 判定可以用 `c >= "0" && c <= "9"` 这样的**字符串间比较**（按宽字符编码序比较）。要写相当于 `isDigit` 的逻辑时，这种写法最省事

### 闭包的陷阱（TJS 的作用域捕获）

- **匿名函数（函数字面量）内部大多无法引用外侧函数的局部变量**
- 尤其是给插件（相当于 `Scripts.foreach` / `Array.some`）传回调时，回调的执行上下文在调用方插件一侧，**引用外侧局部变量会抛运行时异常**（"メンバ 'foo' が見つかりません"，找不到成员 'foo'）
- 对策 1：通过插件的附加参数机制传数据（例：`Scripts.foreach(obj, func, arg1, arg2, ...)` → `function(k, v, arg1, arg2)`）
- 对策 2：先用 `Scripts.getObjectKeys(obj)` 取得 keys 数组，再用普通 `for` 循环迭代（普通作用域生效）
- 对策 3：用 `function() { ... } incontextof this` 捕获 `this`（但外侧局部变量仍然不可引用）
- **推荐**：拿不准时用「朴素的 for 循环 + Scripts.getObjectKeys」即可。比依赖插件的回调机制更可靠

### 文件读取（文本编码）

kirikiri 的文本流（`tTVPTextReadStream`）行为（出自 `src/core/common/base/TextStream.cpp`）：

1. **BOM 判定最优先**
   - `EF BB BF` → 按 UTF-8 进行 decode
   - `FF FE` → 直接按 UTF-16 LE 加载
   - `FE FE` → 加密文本（相当于 `c` 模式）/ 压缩文本（相当于 `z` 模式）
2. **无 BOM**：按 **`DefaultReadEncoding`** 进行 decode
   - "UTF-8" → 按 UTF-8 进行 decode（失败则抛 `TJSNarrowToWideConversionError`）
   - "Shift_JIS" → 按 SJIS 进行 decode（失败同上）
   - 其他 → throw `TVPUnsupportedEncoding`
3. **`DefaultReadEncoding` 的初始值是 `Shift_JIS`**。可通过 `TVPSetDefaultReadEncoding("UTF-8")`（在 TJS 中相当于 `Scripts.textEncoding = "UTF-8"`）切换

**能否读取无 BOM 的 UTF-8 取决于项目的 `DefaultReadEncoding` 设置**。「新 engine 必须带 BOM」的说法是错误的，engine 实现历来如此。请确认项目侧的设置。

### 文件写出（文本类）

- `Array.save(filename)` 是**内置**功能，但**固定输出 UTF-16 LE + BOM**（无法选择编码）。git diff 可读性差 / 与外部工具兼容性差
- **想写 UTF-8 时请链接 `saveStruct.dll` 插件**并使用 `Array.save2(filename, utf8=true, newline=0)`（`newline` 中 0=CRLF, 1=LF）
- 用 `Dictionary.saveStruct2(filename, utf8=true, newline=0, option=ssoIndent|ssoSort)` 可以把 Dictionary 直接以 TJS 表示（saveStruct 格式）保存
- 功能相同的 `PackinOne.dll` 也存在，但 init 时有时会经 fstat throw `'/' must be specified at the end of given directory name.`（取决于调用顺序或环境）。写 standalone tool 时，**朴素的 `saveStruct.dll` 意外更少**
- `saveStruct.dll` / `PackinOne.dll` 还会为 Array / Dictionary / Scripts 增加 `toStructString(newline=1, option=0)`（在内存中字符串化）

## 内置类与类型

| 类 | 用途 | 详细 Read 位置 |
|---|---|---|
| Array | 有序列表、`[ ]` 字面量 | `tjs2/array.md` |
| Dictionary | 字符串键字典、`%[ k=>v ]` 字面量 | `tjs2/dictionary.md` |
| String | 字符串（UTF-16LE） | `tjs2/string.md` |
| Octet | 二进制序列 | `tjs2/octet.md` |
| Math | 数学函数 | `tjs2/math.md` |
| Math.RandomGenerator | 随机数 | `tjs2/randomgenerator.md` |
| Date | 日期/时间 | `tjs2/date.md` |
| RegExp | 正则表达式、`/.../` 字面量 | `tjs2/regexp.md` |
| Exception | 异常对象 | `tjs2/exception.md` |

## 文件索引（深入阅读时 Read）

文档位于 krkrz_dev 仓库根目录相对的 `doc/tjs2/` 下
（以下索引是该目录下的相对名称）。
在线版：<https://wamsoft.github.io/krkrz_dev/tjs2/> 。

### 语言规格

- `about.md` — TJS2 概要
- `simple.md` — 基本用法 / 嵌入 API
- `types.md` — 数据类型（void / Integer / Real / String / Object / Octet）
- `variant.md` — `tTJSVariant` 类型（与 C++ 协作时）
- `variable.md` — 变量 / `var` / 作用域
- `class.md` — 类、继承、构造函数、finalize
- `function.md` — 函数、参数、可变长
- `property.md` — 属性声明、getter/setter
- `interface.md` — `iTJSDispatch2`（C++ 侧的对象接口）
- `expr_and_op.md` — 表达式与运算符完整列表（含优先级）
- `factor.md` — 项（字面量等最小单位）
- `token.md` — 词元 / 保留字
- `statement_and_block.md` — 语句与块
- `if.md` / `for.md` / `while.md` / `switch.md` / `with.md` / `try.md` — 控制语法
- `pp.md` — 预处理器
- `style.md` — 推荐风格
- `vmcodes.md` — TJS2 虚拟机的指令码一览
- `ttjs.md` — `tTJS`（C++ 宿主侧 API）

### 内置类

- `basictypes.md` — 基本类型通用的方法/属性
- `array.md` — `Array`
- `dictionary.md` — `Dictionary`
- `string.md` — String 系方法
- `octet.md` — `Octet`
- `math.md` — `Math`
- `randomgenerator.md` — `Math.RandomGenerator`
- `date.md` — `Date`
- `regexp.md` — `RegExp`
- `exception.md` — `Exception`

### 周边信息（`doc/topics/tjs2/`）

- `tooltip.md` / `asyncimageload.md` / `playmovie.md` / `check_2_z.md` /
  `deleted.md` / `fileformat.md` / `type_specified.md`

## 相关技能

- 吉里吉里Z 引擎本体的类 API（Window / Layer / System / Storages / Bitmap 等）见 skill `krkrz`
- 吉里吉里Z 内部结构（engine internals）没有对应技能

这些不在本技能范围内。