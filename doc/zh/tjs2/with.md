# with 语句

## with 语句

**with** 语句用于指定省略 `.` (点) 运算符的左侧 (对象) 时所引用的对象。



语法如下。

```
with(expression)
	ステートメントまたはブロック
```

在“语句或块”内，当使用了省略左侧的 `.` (点) 运算符时，该 `.` (点) 运算符所引用的对象就会成为 with 语句的 expression 中指定的对象。

```
	with(obj) .member = 1; // obj.member = 1; と同じ

	with(obj)
	{
		.member1 = 1; // obj.member1 に 1 を代入
		.member2 = 2; // obj.member2 に 2 を代入
		.member3++; // obj.member3 をインクリメント
		.method(); // obj.method を呼び出す
	}
```

该语句在向对象设置大量属性、或连续调用方法时，尤其可以减少打字量。



例如

```
	var object = new Foo();
	object.setPos(0, 0);
	object.setSize(100, 100);
	object.name = "名前無し";
	object.color = 0xffffffff;
```

这样的脚本，可以改写成下面这样。

```
	var object = new Foo();
	with(object)
	{
		.setPos(0, 0);
		.setSize(100, 100);
		.name = "名前無し";
		.color = 0xffffffff;
	}
```

## with 语句与对象

with 语句中指定的 expression 只在 with 开始执行时求值 1 次，之后只是引用它。



例如，

```
this.dic = %[];
with(this.dic)
{
	.member = 1; // this.dic.member に 1 を代入
	this.dic = 0; // dic に何か別の物を代入
	.member = 2; // this.dic.member に 2 を代入
}
```

这样写，第 2 次对 .member 的赋值也会成功。因为是在 with 开始执行时的状态下对 this.dic 求值，之后使用的都是该求值结果。并不是每次都去求值 this.dic。



由于只在最开始求值 1 次，在需要多次引用对象的用途中，不会再每次生成用于引用对象的代码，有时可以提高速度。



可以认为，上面的例子会生成与以下等价的代码。

```
this.dic = %[];
{
	var 無名の特別なローカル変数 = this.dic;
	無名の特別なローカル変数.member = 1;
	this.dic = 0;
	無名の特別なローカル変数.member = 2;
}
```

在 with 语句中，expression 的求值结果会被赋值给只能用省略左侧的 . (点) 运算符访问的无名特殊局部变量，此后，省略左侧的 . (点) 运算符时，就会引用该“无名特殊局部变量”。

保存 expression 求值结果的作用域，也可以视为与上述“无名特殊局部变量”的局部变量作用域相同 (with 语句影响的范围也同样如此)。

## with 语句之外的 . 运算符

在 with 语句之外，如果省略 `.` (点) 运算符的左侧，就会引用全局对象。

例如，在 with 语句之外



`.foo = 1;`



这样书写的话，就与



`global.foo = 1;`



的含义相同。
