# 基本用法

## 编译

可以使用 Borland C++ 5.5 及以后版本 (C++ Builder 5 及以后版本) 进行编译。



编译需要 boost.org 的 regex++。



安装 regex++ 之后，请编译各个 cpp 文件。



使用 C++ Builder 时，只需把 tjs2 的各个 cpp 文件全部添加到项目中即可。



也可以用 gcc 3 及以后版本编译 (2.95 也能编译，但需要修改 wstring 相关部分)。

## 简单示例

```
#include <stdio.h>
#include "tjs.h"
#include "tjsError.h"

int main(int argc, char* argv[])
{
	setlocale(LC_ALL, ""); // ロケールを設定

	tTJS *tjsengine = new tTJS(); // TJS2 スクリプトエンジンを作成

	try
	{
		tTJSVariant result; // 結果を受け取るための変数

		tjsengine->ExecScript(
			TJS_W(
				"function test(x, y) { return x*y; } \n"
				"return test(4, 5);\n"),
				&result, NULL,
				TJS_W("test code"));	// テストスクリプトを実行

		printf("結果 : %d\n", (int)result); // 結果を表示
	}
	catch(eTJSError &e)
	{
		printf("エラーが発生しました : %ls\n", e.GetMessage().c_str());
	}
	catch(...)
	{
		printf("エラーが発生しました\n");
	}

	tjsengine->Shutdown(); // TJS2 スクリプトエンジンをシャットダウン
	tjsengine->Release(); // TJS2 スクリプトエンジンを解放

	return 0;
}
```

- **第 2~3 行**  
  正在读取使用 TJS2 所需的头文件。tjsError.h 中包含与 TJS 的 C++ 异常相关的声明。
- **第 7 行**  
  正在用 setlocale 指定区域设置。如果不指定区域设置，就会变成 "C" 区域设置，因此日文字符的窄字符与宽字符之间的转换会无法正常进行。
- **第 9 行**  
  正在用 new 运算符创建 TJS2 脚本引擎。
- **第 11 行**  
  进入了 try 块。TJS2 的错误通过异常来通知，因此需要谨慎进行异常处理。
- **第 13 行**  
  声明用于接收执行脚本所得结果的 tTJSVariant 型变量。
- **第 15~20 行**  
  使用 tTJS::ExecScript 执行脚本。
  
  第 1 个参数指定要执行的脚本。为了以 tjs_char * 型传递，使用 TJS_W 宏把字符串字面量转换为宽字符串。脚本中定义了函数 test，并返回调用该函数的结果。
  
  这个示例中通过 return 语句返回执行结果，并用 result 变量接收；如果不需要接收结果，则 return 语句和 tTJS::ExecScript 的第 2 个参数都不需要 (这种情况下第 2 个参数指定为 NULL)。
  
  tTJS::ExecScript 的第 3 个参数是执行上下文，这里指定为 NULL。指定 NULL 时，脚本会在 global 上下文上执行。
  
  tTJS::ExecScript 的第 4 个参数指定该脚本的名称。为 NULL 时被视为匿名。名称必须是人类可读的。
- **第 22 行**  
  正在显示结果。这里把 tTJSVariant 强制转换为 int 型。
- **第 24 行**  
  正在接收 eTJSError 型的异常。
- **第 26 行**  
  使用 eTJSError::GetMessage 显示异常的原因。为了把消息转换为 const tjs_char *，使用了 tTJSString::c_str。由于 tjs_char 是宽字符，printf 的转换说明符指定为 %ls。
- **第 28 行**  
  正在接收其他异常。
- **第 33~34 行**  
  正在释放 TJS2 脚本引擎。在释放之前，使用 tTJS::Shutdown 关闭 TJS2 脚本引擎。

## 调用 TJS2 侧的函数

这是从 C++ 调用在 TJS2 侧声明的函数的方法。

试着将前面 try 块中的内容写成如下形式。

```
		tTJSVariant result; // 結果を受け取るための変数

		tjsengine->ExecScript(
			TJS_W("function test(x, y) { return x*y; }"), NULL, NULL, TJS_W("test"));

		tjsengine->EvalExpression(TJS_W("test(4, 5)"), &result, NULL, NULL);
			// tTJS::EvalExpression を使って式を実行

		printf("結果 : %d\n", (int)result); // 結果を表示

		iTJSDispatch2 * global = tjsengine->GetGlobalNoAddRef();
			// グローバルオブジェクトを取得

		tTJSVariant param[] = { 4, 5 }; // パラメータとして渡す変数
		tTJSVariant *p_param[] = { param + 0, param + 1 }; // 変数へのポインタの配列

		TJS_THROW_IF_ERROR(global->FuncCall(0, TJS_W("test"), NULL, &result, 2, p_param, NULL));
			// test を関数として呼び出す

		printf("結果 : %d\n", (int)result); // 結果を表示
```

- **第 3~4 行**  
  声明了函数 test。test 会被注册到 global。
- **第 6 行**  
  使用 tTJS::EvalExpression 执行表达式。如果对速度的要求不是那么严格，像这样把表达式作为字符串传入并接收其结果会比较轻松。
  
  顺便一提，如果是简单的表达式 (不包含函数声明等其他执行单位的那种)，编译结果会有一定程度的缓存，第 2 次以后的表达式求值可以高速进行。
- **第 11 行**  
  正在获取全局对象。tTJS::GetGlobal 与 tTJS::GetGlobalNoAddRef 的区别在于，前者会递增 global 对象的引用计数，而后者不会递增。
  
  递增引用计数、用完后再递减，意味着在此期间对该对象加锁，使其不会被销毁。像这个示例这样，在不必担心 global 对象被销毁的情况下，无需操作引用计数，因此可以使用 tTJS::GetGlobalNoAddRef。另外，这种情况下用完时也不需要 Release。
- **第 14~15 行**  
  正在准备传递给函数的参数。iTJSDispatch::FuncCall 需要 tTJSVariant 型指针的数组作为传递给函数的参数，因此需要做这样的准备。
- **第 17 行**  
  使用 iTJSDispatch2::FuncCall 调用函数 "test"。
  
  FuncCall 的最后一个参数是传递给函数 test 的 this (执行上下文)，但这个示例中声明的 test 内部没有使用 this，所以指定 NULL 也没问题。如果有应当执行的上下文，则需要指定该对象。
  
  TJS_THROW_IF_ERROR 是一个宏：当 tjs_error 型的结果为错误时，连同与之对应的错误消息一起抛出异常。

## 原生函数

可以创建原生实现 (用 C++ 等实现的函数)，并从 TJS2 侧访问它。

即使不是 C++，只要是能实现 iTJSDispatch2 的语言，用任何语言编写的函数都可以调用，不过 C++ 大概是最轻松的。



用 C++ 编写函数时，从 tTJSNativeFunction (记述于 tjsNative.h) 派生类会比较轻松 (但是，只实现 iTJSDispatch2 的 FuncCall 也可以作为函数运行)。



试着实现一个把给定的 2 个参数相乘并返回的简单函数。

```
class TestFunc : public tTJSNativeFunction
{
public:
	tjs_error Process(tTJSVariant *result, tjs_int numparams,
		tTJSVariant **param, iTJSDispatch2 *objthis)
	{
		if(numparams < 2) return TJS_E_BADPARAMCOUNT; // 引数が足りない

		if(!result) return TJS_S_OK; // 結果を格納しなくて良い場合はそのままもどる

		*result = *param[0] * *param[1]; // 計算

		return TJS_S_OK; // 正常に終わったことを示すため TJS_S_OK を返す
	}
};
```

如上面所述，继承 tTJSNativeFunction 的类中需要实现的只有 Process 方法。

Process 方法的参数如下。

- **tTJSVariant *result**  
  会传入指向用于存放函数结果的 tTJSVariant 型变量的指针。**调用方不需要结果时会传入 NULL**，请注意。
- **tjs_int numparams**  
  传递给函数的参数个数。
- **tTJSVariant **param**  
  存放传递给函数的参数的 tTJSVariant 型变量指针的数组。
- **iTJSDispatch2 *objthis**  
  函数应当在其上执行的上下文。如果实现不依赖上下文，可以忽略。

为了让 TJS2 能够访问原生函数，必须把它注册到 TJS2 内部可访问的对象上。下面的示例中，以 "test" 这个名字注册到 global。此外，还实际调用了该函数。

```
		iTJSDispatch2 * global = tjsengine->GetGlobalNoAddRef();
			// グローバルオブジェクトを取得

		iTJSDispatch2 *func = new TestFunc(); // TestFunc のオブジェクトを作成
		tTJSVariant func_var(func); // tTJSVariant 型 func_var にオブジェクトを設定
		func->Release(); // func を Release

		TJS_THROW_IF_ERROR(
			global->PropSet(TJS_MEMBERENSURE, TJS_W("test"), NULL, &func_var, NULL));
				// 登録

		tTJSVariant result; // 結果を受け取るための変数
		tjsengine->EvalExpression(TJS_W("test(4, 5)"), &result, NULL, NULL);
			// tTJS::EvalExpression を使って式を実行

		printf("結果 : %d\n", (int)result); // 結果を表示
```

- **第 4~6 行**  
  创建实现了原生函数的类 TestFunc 的对象，并把它转换为 tTJSVariant 型。
  
  第 5 行把它转换为 tTJSVariant 型，此时 tTJSVariant 型会自动管理函数对象的引用计数，所以在第 6 行 Release 了函数对象。
- **第 8~9 行**  
  把函数以 "test" 这个名字注册到 global 对象。这里调用了 global 对象的 iTJSDispatch2::PropSet，调用时带有 TJS_MEMBERENSURE 标志，以便新建成员。
- **第 12~16 行**  
  实际调用函数并显示结果。

## 原生类

TJS2 拥有用于处理用 C++ 等语言编写的原生类的机制。

每个对象 (iTJSDispatch2 接口) 都可以注册一个被称为原生实例的 iTJSNativeInstance 型对象，并可以从对象中取出它。

原生实例以唯一的类 ID 来标识，创建原生类时需要获取类 ID。



不过，用于进行这些操作的宏群定义在 tjsNative.h 中，利用它们会比较轻松。

下面的示例使用这些宏实现一个简单的类。



首先，是原生实例的实现。要实现原生实例，需要从 tTJSNativeInstance 派生类。tTJSNativeInstance 是在 tjsNative.cpp / tjsNative.h 中实现的类，实现了 iTJSNativeInstance 的基本行为。

```
class NI_Test : public tTJSNativeInstance // ネイティブインスタンス
{
public:
	NI_Test()
	{
		// コンストラクタ
		Value = 0;
	}

	tjs_error TJS_INTF_METHOD
		Construct(tjs_int numparams, tTJSVariant **param, iTJSDispatch2 *tjs_obj)
	{
		// TJS2 オブジェクトが作成されるときに呼ばれる

		// 引数があればそれを初期値として Value に入れる
		if(numparams >= 1 && param[0]->Type() != tvtVoid)
			Value = (tjs_int)*param[0];

		return S_OK;
	}

	void TJS_INTF_METHOD Invalidate()
	{
		// オブジェクトが無効化されるときに呼ばれる
	}

	void SetValue(tjs_int n) { Value = n; }
	tjs_int GetValue() const { return Value; }

	tjs_int GetSquare() const { return Value*Value; }
	void Add(tjs_int n) { Value += n; }
	void Print() const { printf("%d\n", Value); }

private:
	tjs_int Value; // 値
};
```

- **第 35 行**  
  这里顺序有些颠倒，这是数据成员。原生实例中可以自由地写所需的数据成员。
- **第 4~8 行**  
  这是 NI_Test 的构造函数。作为 C++ 类的初始化，建议在这里而不是后面叙述的 Construct 中完成，并把 Construct 中的初始化控制在最小限度。
  
  这个示例中，把数据成员 Value 的初始值设置为 0。
- **第 10~20 行**  
  在用 new 运算符创建 TJS2 对象时被调用。numparams 和 param 参数表示传递给 new 运算符的参数。
  
  tjs_obj 参数是所创建的 TJS 对象。
  
  这个示例中，如果有参数 (并且它不是 void)，就把它设置为 Value 的初始值。
- **第 22~25 行**  
  这是在对象被无效化时调用的方法。在这里写结束处理比较好。
  
  这个示例中什么都不做。
- **第 27~32 行**  
  这是用于操作数据成员的一组公开方法。在后面叙述的原生类中，会编写利用它们的代码。

要创建对象就需要类，所以下面记述类。类以派生 tTJSNativeClass 的形式实现。tTJSNativeClass 拥有 iTJSDispatch2 接口，并实现了作为原生类运作所需的基本行为。

TJS 可访问的方法和属性记述在原生类的构造函数内。

```
class NC_Test : public tTJSNativeClass // ネイティブクラス
{
public:
	NC_Test(); // コンストラクタ; 下に記述

	static tjs_uint32 ClassID; // クラスID

private:
	tTJSNativeInstance *CreateNativeInstance()
	{
		return new NI_Test(); // ネイティブインスタンスを作成して返す
	}
};
tjs_uint32 NC_Test::ClassID = (tjs_uint32)-1; // クラスID
```

- **第 4 行**  
  这是该类的构造函数。实现将在后面叙述。
- **第 6 行**  
  这是用于保存该类类 ID 的变量。其实体在第 14 行。
- **第 9~12 行**  
  CreateNativeInstance 方法是在应当创建原生实例的时机被调用的方法。这里创建并返回 NI_Test 类的对象。

```
NC_Test::NC_Test() : tTJSNativeClass(TJS_W("Test"))
{
	TJS_BEGIN_NATIVE_MEMBERS(/*TJS class name*/Test)

		TJS_DECL_EMPTY_FINALIZE_METHOD

		TJS_BEGIN_NATIVE_CONSTRUCTOR_DECL(
			/*var.name*/_this,
			/*var.type*/NI_Test,
			/*TJS class name*/Test)
		{
			// NI_Test::Construct にも内容を記述できるので
			// ここでは何もしない
			return TJS_S_OK;
		}
		TJS_END_NATIVE_CONSTRUCTOR_DECL(/*TJS class name*/Test)

		TJS_BEGIN_NATIVE_METHOD_DECL(/*func. name*/print) // print メソッド
		{
			TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
				/*var. type*/NI_Test);

			_this->Print();

			return TJS_S_OK;
		}
		TJS_END_NATIVE_METHOD_DECL(/*func. name*/print)

		TJS_BEGIN_NATIVE_METHOD_DECL(/*func. name*/add) // add メソッド
		{
			TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
				/*var. type*/NI_Test);

			if(numparams < 1) return TJS_E_BADPARAMCOUNT;

			_this->Add((tjs_int)*param[0]);

			return TJS_S_OK;
		}
		TJS_END_NATIVE_METHOD_DECL(/*func. name*/add)

		TJS_BEGIN_NATIVE_PROP_DECL(value) // value プロパティ
		{
			TJS_BEGIN_NATIVE_PROP_GETTER
			{
				TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
					/*var. type*/NI_Test);
				*result = _this->GetValue();
				return TJS_S_OK;
			}
			TJS_END_NATIVE_PROP_GETTER

			TJS_BEGIN_NATIVE_PROP_SETTER
			{
				TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
					/*var. type*/NI_Test);
				_this->SetValue((tjs_int)*param);
				return TJS_S_OK;
			}
			TJS_END_NATIVE_PROP_SETTER
		}
		TJS_END_NATIVE_PROP_DECL(value)

		TJS_BEGIN_NATIVE_PROP_DECL(square) // square 読み出し専用プロパティ
		{
			TJS_BEGIN_NATIVE_PROP_GETTER
			{
				TJS_GET_NATIVE_INSTANCE(/*var. name*/_this,
					/*var. type*/NI_Test);

				*result = _this->GetSquare();

				return TJS_S_OK;
			}
			TJS_END_NATIVE_PROP_GETTER

			TJS_DENY_NATIVE_PROP_SETTER
		}
		TJS_END_NATIVE_PROP_DECL(square)

	TJS_END_NATIVE_MEMBERS
}
```

- **第 1 行**  
  这是 NC_Test 的构造函数。向父类 tTJSNativeClass 的构造函数指定在 TJS2 内使用的类名。
- **第 3 行**  
  这是 TJS_BEGIN_NATIVE_MEMBERS 宏。参数中指定在 TJS2 内使用的类名。
  
  在这个宏与 TJS_END_NATIVE_MEMBERS 宏夹着的位置，记述应成为类成员的方法和属性。
- **第 4 行**  
  声明空的 finalize 方法。相当于 finalize 的处理也可以通过重写 tTJSNativeInstance::Invalidate 来实现，所以通常空方法就足够了。
- **第 7~16 行**  
  声明 (TJS 的) 构造函数。相当于用 TJS 编写类时，在类内声明与类同名的方法的部分。
  
  
  
  TJS_BEGIN_NATIVE_CONSTRUCTOR_DECL 宏的第 1 个参数是要分配给原生实例的变量名，第 2 个参数是该变量的类型名。在这个示例的该块内，可以使用 NI_Test * _this 这个变量来访问原生实例。
  
  宏的第 3 个参数指定在 TJS 内使用的类名。TJS_END_NATIVE_CONSTRUCTOR_DECL 宏的参数也一样。
  
  这里也一样，相当于构造函数的处理可以通过重写 tTJSNativeInstance::Construct 来实现，所以这里什么都不做，返回 S_OK。
- **第 18~27 行**  
  声明 print 方法。方法名必须在 TJS_BEGIN_NATIVE_METHOD_DECL 与 TJS_END_NATIVE_METHOD_DECL 两个宏中指定相同的名字。
  
  该宏内可使用的变量有 tjs_int numparams 和 tTJSVariant **param，分别表示被传递的参数个数和参数。这个方法中没有使用它们。
  
  第 20~21 行是用于从对象取出原生实例的宏。在这个示例中，意思是把原生实例取出到 _this 这个 NI_Test * 型变量中。之后，就可以用 _this 变量访问原生实例。第 23 行调用了该原生实例的 Print 方法。
- **第 29~40 行**  
  声明 add 方法。这里使用了 numparams 和 param。
- **第 42~62 行**  
  声明 value 属性。与方法的声明一样，在 TJS_BEGIN_NATIVE_PROP_DECL 与 TJS_END_NATIVE_PROP_DECL 两个宏中指定属性名。
  
  
  
  在 TJS_BEGIN_NATIVE_PROP_GETTER 与 TJS_END_NATIVE_PROP_GETTER 宏夹着的位置，可以记述 getter。getter 内要写成对 tTJSVariant 型的 *result 设置值。
  
  同样，在 TJS_BEGIN_NATIVE_PROP_SETTER 与 TJS_END_NATIVE_PROP_SETTER 宏夹着的位置，可以记述 setter。setter 内保存着应设置到 tTJSVariant 型的 *param 中的值，使用它进行处理。
- **第 64~79 行**  
  这里声明只读属性。通过写 TJS_DENY_NATIVE_PROP_SETTER 代替 setter，可以创建只读属性。

原生类的注册与原生函数的注册相同。下面示例测试代码。

```
		iTJSDispatch2 * global = tjsengine->GetGlobalNoAddRef();
			// グローバルオブジェクトを取得

		iTJSDispatch2 *cls = new NC_Test(); // NC_Test のオブジェクトを作成
		tTJSVariant cls_var(cls); // tTJSVariant 型 cls_var にオブジェクトを設定
		cls->Release(); // cls を Release

		TJS_THROW_IF_ERROR(
			global->PropSet(TJS_MEMBERENSURE, TJS_W("Test"), NULL, &cls_var, NULL));
				// 登録

		tjsengine->ExecScript(TJS_W(
			"var test = new Test();\n"
			"test.value = 5;\n"
			"var test2 = new Test(test.square);\n"
			"test2.add(3);\n"
			"test2.print();\n\0"),
				NULL, NULL, NULL); // スクリプトを実行
```
