# 类

## 类

类是创建对象时的模板。属于类的变量称为成员变量，属于类的函数称为成员函数或方法，属于类的属性称为成员属性。

类基本上按如下方式声明。

```
**class** classname
{
	// メンバやメンバメソッドやメンバプロパティを記述

	function classname() // コンストラクタ
	{
	}

	function **finalize**()
	{
	}
}
```

类名指定为标识符。

在类内记述创建该类的对象时会成为成员的变量、方法与属性。

类内必定有一个与类同名的方法，称为**构造函数**。当使用 **new** 运算符创建对象时，这个函数会随 new 运算符的参数一起被调用。

类内同样有一个名为 finalize 的特殊方法。这是对象消亡时被调用的方法，可以省略。不写也没有关系。

```
	class test
	{
		function test()
		{
			// コンストラクタ
			// ここに、オブジェクトが作成されるときに処理する内容を書く
			variable = 0;
		}

		function finalize()
		{
			// finalize メソッド
			// ここに、オブジェクトが破棄されるときに処理する内容を書く
		}

		function method1()
		{
			// メソッド
			System.inform(variable);
		}

		var variable; // メンバ変数

		property prop // メンバプロパティ
		{
			getter() { return variable; }
		}
	}
```

对类伴随 "Class" 使用 instanceof 运算符时为真 (就上例而言，test instanceof "Class" 为真)。

## 创建对象

要创建已声明的类的对象，使用 new 运算符。

在 new 运算符之后，与函数调用一样，指定类名以及传递给构造函数的参数。

```
	class Test
	{
		var variable1 = getValue(); // メンバ変数の初期化

		function Test(arg1, arg2) // コンストラクタ
		{
			// ここでは new 演算子で指定した引数が arg1 と arg2 にわたっている
		}
	}

	var newobject = new Test(1, 2); // 引数に 1, 2 を渡して test クラスのオブジェクトを作成
```

创建对象时的处理顺序如下。

1. 首先创建一个空对象
2. 注册方法、属性
3. 创建成员变量 (此时需要初始化的变量会被初始化)
4. 执行构造函数

> **Note:**
> 即使构造函数没有参数，也不能省略 new 运算符的 ( )。不能像 JavaScript 那样写成 new Test。必须写成 new Test( )。

特别是，在类的方法或属性内创建该类的对象时，或者创建该类的超类的对象时，按如下写法会出错。

```
	class Test
	{
		function Test() // コンストラクタ
		{
		}

		function func()
		{
			return new Test(); // エラー
		}
	}
```

这是因为，在类的方法或属性内只写 Test 时，构造函数 Test 在作用域上比类 Test 更近，因此会引用到构造函数 Test。在这种情况下，为避免这一点，需要像下面这样显式地使用 global. (因为类被注册在 global 中)。

```
	class Test
	{
		function Test() // コンストラクタ
		{
		}

		function func()
		{
			return new global.Test(); // これならば OK
		}
	}
```

## 对象的无效化

在 TJS2 中，对象被删除时会经历对象的**无效化**与对象的删除两个阶段。

对象被无效化时，会调用 finalize 方法，并给该对象打上“无效”标记。之后对该对象的所有访问都会失败，并发生异常。对象是否已被无效化，可以用 **isvalid** 运算符检查。

可以使用 **invalidate** 运算符使对象无效化。

```
	class Test
	{
		var variable;

		function Test()
		{
			// コンストラクタ
			variable = new AnotherClass();
		}

		function finalize()
		{
			// finalize メソッドは無効化された時に呼ばれる
			invalidate variable;
		}
	}

	var object = new Test(); // オブジェクトを作成

	(略)

	invalidate object; // オブジェクトを無効化
```

即使不使用 invalidate 运算符，对象在不再被需要时也会被删除。此时，如果尚未被无效化，会在该时点被无效化。

在 TJS2 中，对象何时被删除没有明确规定，删除或无效化“随时都可能发生”。因此，未被无效化的对象会在删除时被无效化，finalize 方法有可能在意想不到的时点被调用。为避免这种情况，建议对象使用完毕后用 invalidate 运算符将其无效化。

> **Note:**
> invalidate 运算符的作用与 C++ 的 delete 运算符相近。
>
> TJS2 的 delete 运算符与 C++ 的 delete 运算符不同，是用于删除成员或局部变量的运算符。它不会使对象本身无效化或删除对象，但有时会因删除了成员或局部变量，结果上引发对象的无效化或删除。

## 访问对象

对已创建对象的成员变量、方法、成员属性，使用 **.** (成员选择) 运算符或 **[ ]** (间接成员选择运算符) 进行访问。

```
	var obj=new MyLayer(window,window.prmaryLayer)
	obj.method1(); // メソッドの呼び出し  obj['method1']() でも同じ
	obj.num = 3; // メンバ変数へ代入  obj['num']=3 でも同じ
	obj.prop1++; // メンバプロパティにアクセス  obj['prop1']++ でも同じ
```

## 闭包

已创建对象的方法与成员属性，是在带有“该成员属于哪个对象”这一信息的状态下被注册到对象中的。

因此，即使把方法或成员属性带到对象外使用，也仍然会构成对原对象的访问。这一功能称为闭包。另外，访问目标对象称为**上下文**。

```
	var obj = new FooBarClass(); // オブジェクトを作成
	obj.method(); // オブジェクトのメソッドを普通に呼び出す
	var objmethod = obj.method; // オブジェクトのメソッドへの参照を objmethod に代入
	objmethod(); // objmethod を呼び出すが、obj.method() と同じく、obj に対するアクセスとなる
```

**incontextof** 运算符更改“是哪个对象的成员”这一信息，并提供了在任意上下文上执行方法的手段。

```
	(objmethod incontextof obj2)(); // obj2 に対する操作になる
	(objmethod incontextof this)(); // this に対する操作になる
```

## 继承

使用关键字 **extends**，可以使类从其他类继承。所谓继承，就是把继承来源类的成员承继过来。

作为继承来源的类称为**超类**，继承得到的类称为**子类**。

按如下方式声明类。

```
	class Class1 // スーパークラス
	{
		function Class1() // Class1 コンストラクタ
		{
		}

		function finalize() // Class1 finalize
		{
		}

		function method1() // method1
		{
		}
	}


	class Class2 extends Class1
	{
		function Class2() // Class2 コンストラクタ
		{
			super.Class1(); // Class1 コンストラクタを呼ぶ
		}

		function finalize() // Class2 finalize
		{
			super.finalize();
		}
	}

	var obj = new Class2(); // Class2 オブジェクトを作成
	obj.method1(); // Class2 は Class1 の method1 を継承しているので使用することができる
```

在上例中，Class2 继承了 Class1。也可以说 Class2 是**派生**自 Class1 的。

在 Class2 的构造函数中调用了 Class1 的构造函数，在 Class2 的 finalize 中调用了 Class1 的 finalize。**子类如果在这些方法内不调用超类中对应的同名方法，则行为未定义** (也就是说，当前版本并不会检查是否调用)，因此请务必写上。

要从子类引用超类，可以像上例那样使用关键字 **super**。该关键字只能在子类内使用，表示超类。

存在继承时，new 运算符创建对象时的初始化顺序如下。

1. 首先创建一个空对象
2. 注册方法、属性 (从超类开始，朝子类方向)
3. 创建成员变量 (从超类开始，朝子类方向)
4. 调用子类的构造函数
5. (从子类的构造函数内) 调用超类的构造函数

## 多重继承

在 extends 之后记述多个超类名，即可进行多重继承。

```
	class SubClass extends ClassA, ClassB
	{
		function SubClass() // SubClass コンストラクタ
		{
			ClassA(); // ClassA コンストラクタを呼ぶ
			ClassB(); // ClassB コンストラクタを呼ぶ
		}

		function finalize() // Class2 finalize
		{
			global.ClassA.finalize();
			global.ClassB.finalize();
		}
	}
```

由于不能使用 super 关键字，必须显式指定类。像示例那样在调用超类的方法时特意加上 global. 来访问类，是因为在子类内只写 ClassA 会指 ClassA 的构造函数。类本身被注册在 global 中，因此使用 global. 访问类。

存在多重继承时，new 运算符创建对象时的初始化顺序与不进行多重继承时相同，但超类的方法、属性的注册顺序按 extends 关键字之后书写的顺序进行。继承来源的类之间存在同名方法或属性时，后写的优先。被隐藏的方法或属性，可以像 global.ClassA.hiddenMethod() 这样显式写出类名来访问。

## 重写

在子类中声明与超类的方法或成员属性同名的东西，即可隐藏超类的方法。这称为重写。

上述说明中出现的 finalize 方法，重写了超类的 finalize 方法。

```
	class Class1 // スーパークラス
	{
		function Class1() // Class1 コンストラクタ
		{
		}

		function finalize() // Class1 finalize
		{
		}

		function method1() // method1
		{
			(略)
		}
	}


	class Class2 extends Class1
	{
		function Class2() // Class2 コンストラクタ
		{
			super.Class1(); // Class1 コンストラクタを呼ぶ
		}

		function finalize() // Class2 finalize
		{
			super.finalize();
		}

		function method1() // Class1.method1 をオーバーライド
		{
			(略)
			if(略) return super.method1();
			(略)
		}
	}

	var obj = new Class2(); // Class2 オブジェクトを作成
	obj.method1(); // Class2 の method1 が呼ばれる
```

在子类的方法或属性中，可以使用 super 关键字访问超类的方法或属性。

不能重写成员变量。成员变量是相对于一个对象注册的，因此如果子类与超类中存在同名的成员函数，子类的变量就会覆盖超类的变量。
