# tTJSVariant 型

## 什么是 tTJSVariant

tTJSVariant 型是用于处理 TJS2 中“变量”数据的类型。

tTJSVariant 型拥有内部类型，用单一类型就可以表示 void(未定义)、对象、整数、实数、字符串、字节序列。

另外，在运算方面，它会自动处理这些内部类型之间的转换。

## tTJSVariantType

这是表示 tTJSVariant 内部类型的枚举类型。可以通过 tTJSVariant::**Type** 方法获取。

- ****tvtVoid****  
  void 类型。用无参数的构造函数构造 tTJSVariant 型时就是这种类型。它不是 null。
- ****tvtObject****  
  对象类型。为 null 时就是这种内部类型。
- ****tvtString****  
  字符串类型。
- ****tvtOctet****  
  字节序列类型。
- ****tvtInteger****  
  整数类型。保存 tTVInteger 型的数值。
- ****tvtReal****  
  实数类型。保存 tTVReal 型的数值。

## 对象引用

在内部类型之中，对象采用引用计数方式进行管理。

tTJSVariant 本身会自动进行引用计数的管理，但从 tTJSVariant

获取的各方法，以及从用于获取 tTJSVariantClosure 型的方法中取出指向对象的指针之后的引用计数管理，它并不参与，请注意。

## 对象类型

**tTJSVariantClosure** 型是在 tTJSVariant 内部保持对象的类型。这个类型拥有保持 2 个 iTJSDispatch2 接口的机制，一个持有对象本身，另一个持有该对象被执行时所在的上下文的信息。

tTJSVariantClosure 型拥有 iTJSDispatch2 接口所拥有的各个方法。经由 tTJSVariantClosure 访问这些方法，就可以正确处理执行上下文。



为了从 tTJSVariant 型取出 tTJSVariantClosure 型，有 tTJSVariant::**AsObjectClosure** 和 tTJSVariant::**AsObjectClosureNoAddRef** 这 2 个方法。前者会递增对象的引用计数，后者不会递增。

tTJSVariantClosure 型不具备自动管理引用计数的机制，因此在从 tTJSVariant 型取出 tTJSVariantClosure 型之后，需要注意引用计数的管理。

## 字符串类型

TJS2 的字符串采用引用计数方式管理，单纯的复制等操作只会增加字符串的引用计数，不会复制字符串实体。

tTJSVariantString 型是 tTJSVariant 型和 **tTJSString** 型所使用的、用于管理字符串的类型。要从 tTJSVariant 型取出 tTJSVariantString 型，可以使用 tTJSVariant::**AsString** (这个方法会递增引用计数)。不过，tTJSVariantString 型本身不具备自动管理引用计数的机制，因此使用 tTJSVariantString 时需要小心。

如果是 tTJSString 型，则能够管理引用计数，所以转换为 tTJSString 型会比较轻松 (tTJSVariant 定义了与 tTJSString 之间的转换运算符)。

## 字节序列类型

TJS2 的字节序列也和字符串类型一样，采用引用计数方式管理。

**tTJSVariantOctet** 型是用于管理字节序列的类型。这个类型也和 tTJSVariantString、tTJSVariantClosure 一样，不具备管理引用计数的机制，请注意。要从 tTJSVariant 型取出 tTJSVariantOctet 型，可以使用 tTJSVariant::**AsOctet** (递增引用计数)、tTJSVariant::**AsOctetNoAddRef** (不递增引用计数)。

## 转换

tTJSVariant 定义了各种各样的转换运算符和构造函数，因此可以像原始类型一样处理。

如上所述，在与由引用计数管理的类型进行转换时，需要十分注意。

## 运算

各种运算符都被重载了，因此在运算方面也可以像原始类型一样进行。运算过程中所需的类型转换等会被自动处理。
