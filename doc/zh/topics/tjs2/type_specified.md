# 类型指定语法

吉里吉里Z 中可以执行带类型指定的 TJS。
指定类型也只是不会报错，脚本的运行与不指定类型时完全相同。用于利用编辑器的智能提示等场景。

语法如下例所示。

## 变量声明
在变量名后加冒号，然后可以指定类型。
```
var i:int;
var win:Window = new Window();
```

## 函数定义
在参数名后加冒号，然后可以指定类型。
返回值可以在参数列表之后指定。
```
function add(param1:int, param2:int) : int {
    return param1 + param2;
}
```

## 函数表达式
与函数定义一样，可以指定参数与返回值的类型。
```
var f = function(param1:string) : void {};
```

## 属性定义
可以分别指定 setter 的参数与 getter 的返回值类型。
```
property prop {
    setter(value:int) {}
    getter:int { return 0; }
}
```
