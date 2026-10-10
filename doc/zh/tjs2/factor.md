# 项

## 项

项是表达式求值中优先级最高的。它们除了普通的字面量、标识符  ( → [token](token.md) ) 之外，还有以下内容。

## true 与 false

`true` 与 `false` ( **真与假** ) 分别被作为持有 `1` 和 `0` 值的整数值处理。



请避免把 `true` 与 `false` 和其他表达式进行比较。例如，不要写成 `if(true != getBoolean())` 这样，而请写成 `if(!getBoolen())` 这样。在逻辑式中，“0 为假”、“0 以外为真”，而不是“`1` 为真”，另外，TJS2 不持有逻辑类型 (Boolean)，因此不会进行自动的数值←→逻辑类型的类型转换。

## void

`void` 表示“什么都没有”。用于表示“什么都没有”的各种场合。与 `null` 不同。

刚声明的变量 ( 尚未代入任何内容的变量 ) 就是该值。

被当作字符串处理时，会成为空字符串 ( '' )。被当作数值处理时，会成为 0。



`void` 之间的比较建议使用 `===` 或 `!==` ( 识别 ) 运算符。

## null

`null` 虽然是对象，但表示“没有指向任何对象”。与 `void` 不同。

试图访问 null 对象时会出错。

使用 incontextof 运算符把上下文更改为 null 后，该函数就会在调用位置的上下文上执行。

```
	var objmethod = obj.method;
	objmethod(); // obj のコンテキスト上で実行される
	objmethod = objmethod incontextof null; // コンテキストを null に変更
	objmethod(); // this (つまり呼び出した位置におけるコンテキスト) 上で実行される
```

## Infinity

`Infinity` 表示无穷大。表示负无穷大时使用 `-Infinity`。

## NaN

`NaN` 表示非数 (Not a Number)。非数是在计算结果无效等情况下得到的数值。

## super

`super` 在类的方法/属性内表示该类的超类。在不是类的方法/属性的地方、或者正在进行多重继承的类内尝试引用时会出错。

## global

`global` 表示全局对象。可以访问在所有块之外声明的变量、类、以及不是类的方法的函数等。

```
	var v;
	function test(v)
	{
		global.v=v;  // global の v に、引数の v を設定する
	}
```

## this

`this` 在类的方法或属性内，通常表示该类的对象自身。

调用时被显式或隐式指定的“上下文”会被指定为 `this`。

## 表达式中的函数

使用 `function`，可以在表达式中书写函数。

详情请参阅 [函数](function.md)。

## 表达式中的数组

使用 `**[ ]**`，可以在表达式中就地书写 `Array` 类的对象。

详情请参阅 [Array 类](array.md)。

## 表达式中的字典数组

使用 `**%[ ]**`，可以在表达式中就地书写 `Dictionary` 类的对象。

详情请参阅 [Dictionary 类](dictionary.md)。
