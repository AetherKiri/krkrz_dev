# RegExp 类

## RegExp 类

RegExp 类是处理**正则表达式模式**的类。

正则表达式模式中可以指定 perl 兼容的模式。

虽然与 JavaScript 的 RegExp 类相似，但兼容性较低。



构造函数的语法如下。

```
new RegExp(<パターン文字列>, <フラグ文字列=''>);
```

模式字符串是正则表达式模式。请注意，模式中指定的 \ 在字符串字面量中书写时要写成 \\。

标志字符串是 g i l 字符的组合。

g 是全局搜索标志。加上此标志后，在 match、exec、replace 的各方法中，会对模式匹配到的字符串部分全部进行处理。

i 标志不区分英文字母的大小写。

l 标志是进行本地化排序的标志。

```
	var re = new RegExp("[a-z]+[0-9]*", "gi");
	var re = new RegExp("\\.\\.\\."); // /\.\.\./ ( ... にマッチさせたい )
```

## 正则表达式模式

可以在由 / 和 / 围起的部分中指定正则表达式模式。

请参照。

## compile

compile 方法为正则表达式对象设置新的正则表达式模式。

参数与向 RegExp 类的构造函数指定的内容相同。

## test

test 方法返回参数中指定的字符串是否匹配模式。

```
構文 : test(<文字列>)
```

匹配模式则返回真，不匹配则返回假。

此方法会更新此对象的各属性值。

## exec

exec 方法对参数中指定的字符串进行正则表达式模式匹配，返回包含匹配结果的数组。

```
構文 : exec(<文字列>)
```

不匹配模式时，数组的元素个数为 0。

匹配时，元素 0 (最初的元素) 是匹配到的整个部分，之后的元素中则是各匹配部分 (正则表达式模式中由 (  ) 指定的部分)。

此方法会更新此对象的各属性值。

## match

match 方法除了不更新此对象的属性值以外，与 exec 方法相同。

```
構文 : match(<文字列>)
```

## replace

replace 方法进行字符串的替换，返回替换后的字符串。

```
構文 : replace(<対象文字列>, <置き換え文字列>)
```

对目标字符串进行匹配，将匹配的部分用替换字符串替换，返回替换后的字符串。

作为替换字符串，如果不传字符串而传函数，则会为了替换操作而调用该函数。函数接受一个参数，会向其传递表示目标字符串中匹配部分的数组对象 (关于此数组，请参照 exec 方法)。目标字符串中匹配的部分会被替换为函数返回的字符串。

此方法会忽略 start 属性。

## split

split 方法在目标字符串中匹配正则表达式模式的位置处进行分割。

```
構文 : split(<対象文字列>, <(予約)>, <空の要素を無視するか=false>)
```

返回保存了字符串分割结果的数组对象。

当模式中包含捕获组 ( `(...)` ) 时，会在各匹配区间的字符串之后，继续将该匹配所捕获的子字符串也按顺序存入数组 (与 JavaScript 的 String.split 及吉里吉里2 行为相同)。未匹配的组会作为空字符串存入。

将第 3 个参数指定为 true 时，会从结果中去除空元素 (区间、捕获组双方) (默认为 false)。

String 类的 split 方法也请参照。

## matches

matches 属性是表示包含各匹配部分的数组的只读属性。

不匹配模式时，数组的元素个数为 0。

匹配时，元素 0 (最初的元素) 是匹配到的整个部分，之后的元素中则是各匹配部分 (正则表达式模式中由 (  ) 指定的部分)。

## start

表示字符串的搜索开始位置的属性。也可以设置值。

## index

表示匹配部分的首字符位置的只读属性。0 表示开头，因此如果它是匹配目标字符串的开头字符，则为 0。

## lastIndex

表示匹配部分的最后一个字符的下一个字符位置的只读属性。0 表示开头。

## input

表示匹配目标字符串的只读属性。

## leftContext

表示匹配目标字符串中位于匹配部分左侧的字符串的只读属性。

## rightContext

表示匹配目标字符串中位于匹配部分右侧的字符串的只读属性。

## lastMatch

表示匹配目标字符串。与 matches[0] 相同。

## lastParen

返回匹配到的各部分中最后的部分。与 matches[matches.count-1] 相同。

## RegExp.last

最后执行了 test 或 exec 方法的 RegExp 类的实例。

```
例 : if(/pat(\d+)/.test(target)) { return RegExp.last.matches[1]; }
```

## Copyright notice

正则表达式功能的实现使用了 John Maddock 先生的 [Regex++](http://ourworld.compuserve.com/homepages/John_Maddock/regexpp.htm)。在此感谢公开了这款实用库的先生。



Copyright (c) 1998-2001



Dr John Maddock



Permission to use, copy, modify, distribute and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. Dr John Maddock makes no representations about the suitability of this software for any purpose. It is provided "as is" without express or implied warranty.
