# tTJS

## 什么是 tTJS

TJS2 脚本引擎的类。通过这个类的对象可以操作 TJS2。

## 构造函数

tTJS 的构造函数没有参数。

不能将 tTJS 的对象创建为自动变量。必须使用 new 运算符创建。

刚创建后的引用计数为 1。也就是说，直接调用 Release 方法即可释放 tTJS 的对象。

## 析构函数

tTJS 的析构函数位于 protected 区域，无法访问。

要释放 tTJS 的对象，请使用 Release 方法。

另外，推荐在释放 tTJS 的对象之前调用 Shutdown 方法。

## AddRef

void tTJS::AddRef()



递增 TJS2 脚本引擎的引用计数。

## Release

void tTJS::Release()



递减 TJS2 脚本引擎的引用计数。

引用计数变为 0 时，tTJS 对象会被释放。

## Shutdown

void tTJS::Shutdown()



执行脚本引擎的关闭。



推荐在释放 TJS2 脚本引擎时，在 Release 方法之前调用这个方法。

## GetGlobal

iTJSDispatch2 * tTJS::GetGlobal()



获取 **global 对象**。

返回该类型的对象。

这个方法在返回 global 对象时，会递增其引用计数。

## GetGlobalNoAddRef

iTJSDispatch2 * tTJS::GetGlobalNoAddRef()



获取 global 对象。与 GetGlobal 的不同之处在于，不递增 global 对象的引用计数。

## SetConsoleOutput

void tTJS::SetConsoleOutput(iTJSConsoleOutput *console);



指定**控制台**的输出目标。

控制台是输出 TJS2 产生的错误消息等的地方。



参数如下。

- **console**  
  指定定义控制台输出目标的 **iTJSConsoleOutput** 类型的对象。
  
  iTJSConsoleOutput 类型是在 tjs.h 中定义的基本抽象类，具有以下方法。
  
  - **void iTJSConsoleOutput::**ExceptionPrint**(const tjs_char *msg)**  
    用于输出异常相关信息的方法。msg 表示消息。
  - **void iTJSConsoleOutput::**Print**(const tjs_char *msg)**  
    用于输出其他信息的方法。msg 表示消息。

## GetConsoleOutput

tTJSConsoleOutput * tTJS::GetConsoleOutput() const



获取控制台的输出目标。

## OutputToConsole

void tTJS::OutputToConsole(const tjs_char *msg) const



向控制台输出字符串。msg 是要输出的消息。

## OutpuExceptionToConsole

void tTJS::OutpuExceptionToConsole(const tjs_char *msg) const



向控制台输出异常的字符串。msg 是要输出的消息。

## OutputToConsoleWithCentering

void tTJS::OutputToConsoleWithCentering(const tjs_char *msg, tjs_uint width) const



将字符串居中后输出到控制台。msg 是要输出的消息，width 是宽度。

在要输出的消息的字符数少于该宽度时，会居中输出到指定宽度的中央
( 不过由于将所有字符的宽度视为相同，混入全角字符时显示会错位 )

## OutputToConsoleSeparator

void tTJS::OutputToConsoleSeparator(const tjs_char *text, tjs_uint count) const



将由 text 指示的分隔符输出 count 个到控制台。

## Dump

void tTJS::Dump(tjs_uint width = 80) const



将 TJS2 的状态输出到控制台。

会显示各脚本块中虚拟机代码的反汇编结果等。

width 指定输出的宽度。

## ExecScript

void tTJS::ExecScript(

const tjs_char *script,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL,

tjs_int lineofs = 0

)



void tTJS::ExecScript(

const ttstr &script,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL,

tjs_int lineofs = 0

)



执行脚本。



参数如下。

- **const tjs_char *script**
- **const ttstr &script**  
  指定要执行的脚本。
- **tTJSVariant *result**  
  指定用于接收结果的、指向 tTJSVariant 类型变量的指针。
  
  也可以指定 NULL，但为 NULL 时无法接收结果。
- **iTJSDispatch2 *context**  
  指定执行该脚本的上下文。
  
  指定 NULL 时，脚本会在 global 上下文上执行。
  
  通常指定 NULL，但如果想在特定的上下文中执行脚本，请指定作为该上下文的对象。
- **const tjs_char *name**  
  指定脚本的名称。通常指定该脚本的文件名。
  
  用于在异常通知时告知异常发生在哪个脚本等目的。
- **tjs_int lineofs**  
  指定脚本中该脚本的起始行(0~)。
  
  像嵌入在其他文档中的 TJS 脚本那样，当 TJS 脚本被嵌入外部文本中时，指定该 TJS 脚本的起始行。
  
  用于在异常通知时告知异常发生在哪个脚本等目的。

## EvalExpression

void tTJS::EvalExpression(

const tjs_char *expression,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL

tjs_int lineofs = 0

)



void tTJS::EvalExpression(

const ttstr &expression,

tTJSVariant *result = NULL,

iTJSDispatch2 *context = NULL,

const tjs_char *name = NULL

tjs_int lineofs = 0

)



对表达式求值。

参数请参照 ExecScript。



对于像 **if 运算符**那样无法获得表达式结果的运算符，如果试图获得结果而为 result 指定非 NULL，就会发生异常。这种情况下必须为 result 指定 NULL。

## SetPPValue

void tTJS::SetPPValue(const tjs_char *name, const tjs_int32 value)



设置**条件编译**用的变量。name 是变量的名称，value 是要设置的值。

## GetPPValue

tjs_int32 tTJS::GetPPValue(const tjs_char *name)



获取条件编译用的变量。name 是变量的名称。未找到变量时返回 0。

## DoGarbageCollection

tjs_int32 tTJS::DoGarbageCollection()



执行**垃圾回收**。清除 TJS2 持有的缓存，并完成尚未处理的清理工作。
