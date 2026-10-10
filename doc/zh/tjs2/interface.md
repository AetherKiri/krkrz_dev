# iTJSDispatch2 接口

## 什么是 iTJSDispatch2

iTJSDispatch2 是为 TJS2 中的“对象”提供接口的抽象基类。

TJS2 的“对象”包括函数对象、类、属性对象、数组(字典数组) 等。

对 TJS2 的几乎所有操作都可以通过这个接口进行。



下文将以使用该接口的一方为视角进行说明。

## 按序数调用

iTJSDispatch2 的方法中，有一些方法名以 ByNum 结尾。这类方法按序数进行调用；例如，将成员名指定为 "23" 调用 FuncCall，与将序数指定为 23 调用 FuncCallByNum 是等价的。

在访问数组对象时会比较方便。



以 ByNum 结尾的方法没有末尾不带 ByNum 的同名方法的 membername 参数和 hint 参数，取而代之的是 tjs_int num。请在参数 num 中指定序数。



下文省略按序数进行调用的方法的详细说明 (请参照末尾不带 ByNum 的同名方法的说明)。

## AddRef

tjs_uint iTJSDispatch2::AddRef(void)



递增对象的引用计数。

TJS2 的各个对象都由引用计数管理。

返回值是递增后的引用计数值，但不推荐信任这个值。

## Release

tjs_uint iTJSDispatch2::Release(void)



递减对象的引用计数。

返回值是递减后的引用计数值，返回 0 时表示对象已被释放。但是，不推荐信任这个值。

## FuncCall

tjs_error iTJSDispatch2::FuncCall(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

tTJSVariant *result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



进行函数调用。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  作为操作对象的成员名。
  
  为 NULL 时，表示对这个对象自身的操作。在这种情况下，这个对象必须具备函数的功能。
- **tjs_uint32 *hint**  
  指定用于存放“**提示**” (hint) 的变量区域。也可以为 NULL。
  
  提示用于高速进行第 2 次以后对相同成员名的搜索。将指向 tjs_uint32 型变量的指针指定给 hint 后，会在其中写入作为提示的数值。第 2 次以后将参考该数值来搜索成员。由于只是参考，提示的初始值可以是任意值 (推荐 0)。另外，由于这样的机制，提示与对应的成员名保持 1 对 1 对应关系时效率更高 (tTJSString 型拥有用于这种提示的机制)。
  
  根据对象的不同，也可能不具备利用提示的机制。
- **tTJSVariant *result**  
  指定用于存放函数调用结果的 tTJSVariant 型指针。
  
  不需要结果时可以指定 NULL。
- **tjs_int numparams**  
  指定传递给函数的参数个数。
- **tTJSVariant **param**  
  传递要传给函数的参数的指针数组。没有参数时可以为 NULL。
- **iTJSDispatch2 *objthis**  
  指定函数执行所处的上下文 (this 对象)。

## FuncCallByNum

tjs_error iTJSDispatch2::FuncCall(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



按序数进行函数调用。

## PropGet

tjs_error iTJSDispatch2::PropGet(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

tTJSVariant *result,

iTJSDispatch2 *objthis

)



获取属性或成员变量的值。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  作为操作对象的成员名。
  
   
  
  为 NULL 时，表示对这个对象自身的操作。在这种情况下，这个对象必须具备获取属性的功能。
  
  这个参数为 NULL 也能成功的对象，会被视为属性对象。通常，当这样的属性对象成为其他对象的成员时，使用的不是这个属性对象本身，而是对该属性对象执行 PropGet 得到的结果。这种行为可以通过在调用标志中指定 TJS_IGNOREPROP 来绕过。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **tTJSVariant *result**  
  指定用于存放结果的 tTJSVariant 型指针。不允许为 NULL。
- **iTJSDispatch2 *objthis**  
  指定这个方法执行所处的上下文 (this 对象)。

## PropGetByNum

tjs_error iTJSDispatch2::PropGetByNum(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

iTJSDispatch2 *objthis

)



按序数获取属性或成员变量的值。

## PropSet

tjs_error iTJSDispatch2::PropSet(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



设置属性或成员变量的值。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  作为操作对象的成员名。
  
   
  
  为 NULL 时，表示对这个对象自身的操作。在这种情况下，这个对象必须具备设置属性的功能。
  
  这个参数为 NULL 也能成功的对象，会被视为属性对象。通常，当这样的属性对象成为其他对象的成员时，不会使用这个属性对象本身，而是会对该属性对象调用 PropSet。这种行为可以通过在调用标志中指定 TJS_IGNOREPROP 来绕过。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **const tTJSVariant *param**  
  指定表示要设置的值的 tTJSVariant 型变量的指针。不允许为 NULL。
- **iTJSDispatch2 *objthis**  
  指定这个方法执行所处的上下文 (this 对象)。

## PropSetByVS

tjs_error iTJSDispatch2::PropSetByVS(

tjs_uint32 flag,

tTJSVariantString *membername,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



设置属性或成员变量的值。与 PropSet 的不同之处在于，成员名由 tTJSVariantString 引用。这是一个内部使用的方法。tTJSVariantString 拥有多个字符串对象共享同一字符串用内存区域的机制，因此通过这个方法设置属性 (在对象内创建成员) 时，可以防止用于成员名的字符串内存区域的内存增加。

如果不实现这个方法，请返回 TJS_E_NOTIMPL。此时将改为使用 PropSet。另外，如果调用这个方法返回了 TJS_E_NOTIMPL，请实现为改为使用 PropSet。

## PropSetByNum

tjs_error iTJSDispatch2::PropSetByNum(

tjs_uint32 flag,

tjs_int num,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



按序数设置属性或成员变量的值。

## GetCount

tjs_error iTJSDispatch2::GetCount(

tjs_int *result,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



返回对象持有的成员数量。



参数如下。

- **tjs_int *result**  
  指定用于存放结果的变量指针。不允许为 NULL。
- **const tjs_char * membername**  
  指定作为对象的成员名。
  
  为 NULL 时，返回这个对象自身持有的成员数量。
  
  指定了成员名时，如果该成员是对象，则返回该对象持有的成员数量。如果指定的成员不是对象型则失败。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **iTJSDispatch2 *objthis**  
  指定这个方法执行所处的上下文 (this 对象)。
  
  这个参数通常没有意义 (会被忽略)。

## GetCountByNum

tjs_error iTJSDispatch2::GetCount(

tjs_int *result,

tjs_int num,

iTJSDispatch2 *objthis

)



GetCount 的序数版本。

## DeleteMember

tjs_error iTJSDispatch2::DeleteMember(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



删除成员。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  指定作为对象的成员名。不允许为 NULL。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **iTJSDispatch2 *objthis**  
  指定这个方法执行所处的上下文 (this 对象)。
  
  这个参数通常没有意义 (会被忽略)。

## DeleteMemberByNum

tjs_error iTJSDispatch2::DeleteMemberByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



按序数删除成员。

## EnumMembers

tjs_error iTJSDispatch2::EnumMembers(

tjs_uint32 flag,

tTJSVariantClosure *callback,

iTJSDispatch2 *objthis

)



枚举对象内的成员。

callback 可以指定回调函数，但在当前版本中，如果在回调函数内创建或删除这个对象的成员，其行为不受保证。



参数如下。

- **tjs_uint32 flag**  
  调用标志。调用标志请指定下列标志的按位逻辑或，或者 0(零)。
  
  - **TJS_IGNOREPROP**  
    禁用属性访问。在枚举成员并获取值时，如果指定了这个标志，当成员是属性时，得到的是属性对象本身。如果不指定这个标志，得到的是通过属性对象得到的值。
  - **TJS_ENUM_NO_VALUE**  
    不获取值。指定这个标志时，传递给回调函数的参数为 2 个。指定时则为 3 个。
- **tTJSVariantClosure *callback**  
  指定回调函数。
  
  这个回调函数对每个成员各调用一次 callback->FuncCall。
  
  函数的参数为 2 个 (指定 TJS_ENUM_NO_VALUE 时) 或 3 个 (未指定 TJS_ENUM_NO_VALUE 时)。
  
  - 第 1 个参数为字符串型，是成员名
  - 第 2 个参数为整数型，是该成员的标志。将指定 TJS_HIDDENMEMBER 或 TJS_STATICMEMBER 的按位逻辑或组合，或者 0
  - 第 3 个参数仅在未指定 TJS_ENUM_NO_VALUE 时存在，表示该成员的值
- **iTJSDispatch2 *objthis**  
  指定这个方法执行所处的上下文 (this 对象)。
  
  这个参数在未指定 TJS_IGNOREPROP 标志时，会成为属性对象执行的默认上下文。

## Invalidate

tjs_error iTJSDispatch2::Invalidate(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



执行无效化。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  指定作为对象的成员名。
  
  为 NULL 时，这个对象自身会被无效化。
  
  指定了成员名时，如果该成员是对象，则该对象会被无效化。如果指定的成员不是对象型则失败。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **iTJSDispatch2 *objthis**  
  指定这个方法执行所处的上下文 (this 对象)。
  
  这个参数通常没有意义 (会被忽略)。

## InvalidateByNum

tjs_error iTJSDispatch2::InvalidateByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



按序数执行无效化。

## IsValid

tjs_error iTJSDispatch2::IsValid(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

iTJSDispatch2 *objthis

)



检查对象是否有效。

有效时返回 TJS_S_TRUE，反之则返回 TJS_S_FALSE。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  指定作为对象的成员名。
  
  为 NULL 时，可以检查这个对象自身的有效性。
  
  指定了成员名时，如果该成员是对象，则可以检查该对象的有效性。如果指定的成员不是对象型则失败。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **iTJSDispatch2 *objthis**  
  指定这个方法执行所处的上下文 (this 对象)。
  
  这个参数通常没有意义 (会被忽略)。

## IsValidByNum

tjs_error iTJSDispatch2::IsValidByNum(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 *objthis

)



按序数检查对象是否有效。

## CreateNew

tjs_error iTJSDispatch2::CreateNew(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

iTJSDispatch2 **result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



创建新对象。

这个方法与 FuncCall 方法相似，可以为创建新对象传递参数。

作为对象雏形的所谓“类对象”，必须实现这个方法。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  作为操作对象的成员名。
  
  为 NULL 时，为对这个对象自身的操作。在这种情况下，这个对象必须具备创建新对象的功能。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **iTJSDispatch2 **result**  
  指定用于存放新创建的对象的 iTJSDispatch * 型指针。不允许为 NULL。
- **tjs_int numparams**  
  指定创建新对象时传递的参数个数。
- **tTJSVariant **param**  
  传递创建新对象时传递的参数的指针数组。没有参数时可以为 NULL。
- **iTJSDispatch2 *objthis**  
  指定创建新对象时执行所处的上下文 (this 对象)。

## CreateNewByNum

tjs_error iTJSDispatch2::CreateNew(

tjs_uint32 flag,

tjs_int num,

iTJSDispatch2 **result,

tjs_int numparams,

tTJSVariant **param,

iTJSDispatch2 *objthis

)



按序数创建新对象。

## IsInstanceOf

tjs_error iTJSDispatch2::IsInstanceOf(

tjs_uint32 flag,

const tjs_char * membername,

tjs_uint32 *hint,

const tjs_char * classname,

iTJSDispatch2 *objthis

)



检查对象是否是特定类的实例。

类名通过 classname 参数以字符串形式传递。

由 TJS2 的 instanceof 运算符引用。

成功时，如果是指定类的实例则返回 TJS_S_TRUE，否则返回 TJS_S_FALSE。



参数如下。

- **tjs_uint32 flag**  
  调用标志 (参见下文)。
- **const tjs_char * membername**  
  作为操作对象的成员名。
  
  为 NULL 时，为对这个对象自身的操作。在这种情况下，这个对象必须具备创建新对象的功能。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **const tjs_char *classname**  
  以字符串指定类名。
- **iTJSDispatch2 *objthis**  
  指定创建新对象时执行所处的上下文 (this 对象)。

## IsInstanceOfByNum

tjs_error iTJSDispatch2::IsInstanceOfByNum(

tjs_uint32 flag,

tjs_int num,

const tjs_char * classname,

iTJSDispatch2 *objthis

)



按序数检查对象是否是特定类的实例。

## Operation

tjs_error iTJSDispatch2::Operation(

tjs_uint32 flag,

const tjs_char *membername,

tjs_uint32 *hint,

tTJSVariant *result,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



对成员进行运算。运算的种类由 flag 指定。



参数如下。

- **tjs_uint32 flag**  
  调用标志。除了下列通常的调用标志之外，还需要用按位 OR 附加以下标志之一，以指定运算的种类。
  
  
  
  另外，在本说明中，v 表示成员的值，p 表示由 param 参数传递的参数。
  
  - **TJS_OP_BAND**  
    按位 AND 运算
    
    v &= p
  - **TJS_OP_BOR**  
    按位 OR 运算
    
    v |= p
  - **TJS_OP_BXOR**  
    按位 XOR 运算
    
    v ^= p
  - **TJS_OP_SUB**  
    减法
    
    v -= p
  - **TJS_OP_ADD**  
    加法
    
    v += p
  - **TJS_OP_MOD**  
    模运算
    
    v %= p
  - **TJS_OP_DIV**  
    实数除法
    
    v /= p
  - **TJS_OP_IDIV**  
    整数除法
    
    v \= p
  - **TJS_OP_MUL**  
    乘法
    
    v *= p
  - **TJS_OP_LOR**  
    逻辑 OR
    
    v = v || p
  - **TJS_OP_LAND**  
    逻辑 AND
    
    v = v && p
  - **TJS_OP_SAR**  
    算术右移
    
    v >>= p
  - **TJS_OP_SAL**  
    算术左移
    
    v <<= p
  - **TJS_OP_SR**  
    位左移
    
    v >>>= p
  - **TJS_OP_INC**  
    递增
    
    v++
    
    param 参数被忽略
  - **TJS_OP_DEC**  
    递减
    
    v--
    
    param 参数被忽略
- **const tjs_char * membername**  
  作为操作对象的成员名。不允许为 NULL。
- **tjs_uint32 *hint**  
  指定用于存放提示的变量区域。也可以为 NULL。
  
  关于提示的说明请参照 FuncCall 的说明。
- **tTJSVariant *result**  
  指定用于存放运算结果的 tTJSVariant 型变量的指针。可以为 NULL。
- **tTJSVariant *param**  
  指定运算的参数。当运算的种类指定为 TJS_OP_INC 或 TJS_OP_DEC 时，可以为 NULL。
- **iTJSDispatch2 *objthis**  
  指定运算执行所处的上下文，但通常被忽略。

## OperationByNum

tjs_error iTJSDispatch2::OperationByNum(

tjs_uint32 flag,

tjs_int num,

tTJSVariant *result,

const tTJSVariant *param,

iTJSDispatch2 *objthis

)



使用序数对成员进行运算。

## NativeInstanceSupport

tjs_error iTJSDispatch2::NativeInstanceSupport(

tjs_uint32 flag,

tjs_int32 classid,

iTJSNativeInstance **pointer

)



将原生代码的实例与对象关联起来，或者从对象获取原生代码的实例。



参数如下。

- **tjs_uint32 flag**  
  指定调用标志。
  
  必须指定下列值之一。
  
  - ****TJS_NIS_REGISTER****  
    注册 *pointer 所示的原生代码实例。原生代码类的识别使用 classid。
  - ****TJS_NIS_GETINSTANCE****  
    将具有 classid 指定的类 ID 的原生代码实例写入 *pointer。
- **tjs_int32 classid**  
  指定原生代码的类 ID。
  
  原生代码的类 ID 的管理可以使用 TJSRegisterNativeClass
  TJSFindNativeClassID
  TJSFindNativeClassName，但通常，这些处理会由用于编写原生代码的
  支援代码群 (记述在 tjsNative.cpp/tjsNative.h 中) 自动处理。
- **iTJSNativeInstance **pointer**  
  指定 iTJSNativeInstance * 型变量的指针，用于传递或接收原生代码的实例。

## ClassInstanceInfo

tjs_error iTJSDispatch2::ClassInstanceInfo(

tjs_uint32 flag,

tjs_uint num,

tTJSVariant *value

)



操作 IsInstanceOf 方法所使用的类的实例信息的方法。

可以添加类名，以识别对象是哪个类的实例；也可以枚举类，以查明对象是哪个类的实例。



参数如下。

- **tjs_uint32 flag**  
  调用标志。请指定下列标志之一。
  
  - ****TJS_CII_ADD****  
    添加实例信息。
    
    value 中传递存放类名 (字符串) 的 tTJSVariant 型变量的指针。
    
    num 参数被忽略。
  - ****TJS_CII_GET****  
    获取实例信息。
    
    num 参数指定从 0 开始的整数。如果指定的 num 超过已设置的实例信息数量，将返回 TJS_E_FAIL。
    
    value 中传递用于接收类名的 tTJSVariant 型变量的指针。
- **tjs_uint num**  
  指定 flag 为 TJS_CII_GET 时的序数。
- **tTJSVariant *value**  
  flag 为 TJS_CII_ADD 时，传递存放类名的 tTJSVariant 型变量的指针。
  
  flag 为 TJS_CII_GET 时，传递用于接收类名的 tTJSVariant 型变量的指针。

## 调用标志

调用标志。

可以指定下列值的按位 OR 组合。

- **TJS_MEMBERENSURE**  
  指定的成员名未找到时，强制创建成员。作为对 PropSet 的调用标志有效。
  )
- **TJS_MEMBERMUSTEXIST**  
  指定的成员名未找到时，视为错误。这对 Dictionary 或 Array 这类在成员未找到时默认返回 void 的对象有效 (如果不是这样的对象，成员未找到时默认视为错误)。
- **TJS_IGNOREPROP**  
  绕过属性操作。
  
  TJS2 的对象通常在被指定的成员是对象，且对该成员的 PropSet 或 PropGet 成功时 (即属性对象时)，会把对该成员的 PropSet 或 PropGet 的结果当作该成员的替代来使用。
  
  指定这个标志后，这类处理会被绕过，因此即使被指定的成员是属性对象，也会变成对该属性对象本身的操作。
- **TJS_HIDDENMEMBER**  
  指定这个标志来创建成员时，成员将变为不可见。根据对象的不同，也可能不支持。
- **TJS_STATICMEMBER**  
  指定这个标志来创建成员时，成员将成为静态 (不依赖执行上下文)。根据对象的不同，也可能不支持。

## tjs_error

tjs_error 是 iTJSDispatch2 的各方法 (AddRef 和 Release 除外) 返回的错误类型。

它取下列值。另外，即使是不在此列的值，只要值为负，也必须视为错误。为了判断这些，可以使用 TJS_SUCCEEDED 以及 TJS_FAILED 宏。

- ****TJS_E_MEMBERNOTFOUND****  
  未找到指定的成员。
- ****TJS_E_NOTIMPL****  
  试图调用的功能尚未实现。
- ****TJS_E_INVALIDPARAM****  
  无效的参数。
- ****TJS_E_BADPARAMCOUNT****  
  参数个数无效。
- ****TJS_E_INVALIDTYPE****  
  不是函数，或属性的种类不同。
  
  试图调用不是函数的东西时，或试图把不是属性的东西当作属性处理时，返回这个值。
- ****TJS_E_INVALIDOBJECT****  
  对象已经被无效化。
- ****TJS_E_ACCESSDENYED****  
  试图对只读或只写属性执行不被允许的操作。
- ****TJS_E_NATIVECLASSCRASH****  
  执行上下文不同。
  
  在原生代码无法处理的上下文 (例如不同类的对象上) 中执行以原生代码实现的方法时，会返回这个值。
- ****TJS_S_TRUE****  
  不是错误，但表示结果为“真”。
- ****TJS_S_FALSE****  
  不是错误，但表示结果为“伪”。
- ****TJS_S_OK****  
  没有发生错误时，通常返回这个值。
- ****TJS_E_FAIL****  
  发生未定义的错误时，返回这个值。
- ****TJS_FAILED**(x)**  
  x 为错误值时结果为真的宏。
- ****TJS_SUCCEEDED**(x)**  
  x 不是错误值时结果为真的宏。

错误定义以及相关宏记述在 tjsErrorDef.h 中。

另外，有时抛出的不是错误，而是 (C++ 中的) 运行时异常。在编程时需要充分考虑运行时异常。
