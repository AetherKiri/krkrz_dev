# TJS2 的基本类型

## 原始类型

tjsTypes.h 中定义了一些原始类型。

- ****tjs_int****  
  有符号整数 (至少 32bit)
- ****tjs_uint****  
  无符号整数 (至少 32bit)
- ****tjs_int8****  
  8bit 有符号整数
- ****tjs_uint8****  
  8bit 无符号整数
- ****tjs_int16****  
  16bit 有符号整数
- ****tjs_uint16****  
  16bit 无符号整数
- ****tjs_int32****  
  32bit 有符号整数
- ****tjs_uint32****  
  32bit 无符号整数
- ****tjs_int64****  
  64bit 有符号整数
- ****tjs_uint64****  
  64bit 无符号整数
- ****tjs_char****  
  宽字符 (作为 TJS2 字符串类型的原始类型使用)
- ****tjs_nchar****  
  窄字符
- ****tjs_real****  
  实数类型 (double)
- ****tTVInteger****  
  与 tjs_int64 相同
- ****tTVReal****  
  与 tjs_real 相同

## tTJSString

tTJSString 类型是 TJS2 中使用的字符串类型，处理 tjs_char 类型的零结尾字符串。定义在 tjsString.cpp / tjsString.h 中。另外，也可以使用 `ttstr` 这一简短的类型名。

该类型除了自动管理用于字符串的内存之外，

是与亲和性很高的类型。

## eTJS

eTJS 类型是 C++ 异常对象的基类型，定义在 tjsError.h 中。它有一个 **GetMessage** 方法，可以获取随异常一同抛出的消息字符串。

## TJS_W

这是用于把字符串字面量转换为 tjs_char * 类型的宏。



例: TJS_W("字符串字面量")
