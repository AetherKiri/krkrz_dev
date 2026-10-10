# Date 类

## Date 类

从字符串创建 Date 对象的功能以及从对象创建字符串的功能尚未实现，其他方面则与 JavaScript 的 Date 基本兼容。



构造函数的语法如下。

```
new Date();
new Date(<日付文字列>);
new Date(<年>, <月(0～)=0>, <日=1>, <時=0>, <分=0>, <秒=0>);
```

第 1 种语法不需要参数。这种情况下，将保持该构造函数执行时的当前日期时间。

第 2 种语法用于指定日期字符串。日期字符串必须指定为 ANSI C 的 asctime() 格式、RFC1123 中定义的格式、RFC1036 中定义的格式、“年/月/日 时:分:秒”形式中的任意一种。日期字符串的识别会自动进行，在一定程度上支持格式的变形，但与预期格式差异过大时可能无法识别。

第 3 种语法用于指定年月日时分秒。



已实现的方法 (与 JavaScript 兼容)：

setYear/getYear (按本地时间设置/获取 4 位数的公历年份)

setMonth/getMonth (按本地时间设置/获取月份)

setDate/getDate (按本地时间设置/获取日)

setHours/getHours (按本地时间设置/获取小时)

setMinutes/getMinutes (按本地时间设置/获取分钟)

setSeconds/getSeconds (按本地时间设置/获取秒)

setTime/getTime (设置/获取从 1970 年 1 月 1 日 0:00 起经过的毫秒数)

getDay (获取星期)

parse (解析日期字符串)
