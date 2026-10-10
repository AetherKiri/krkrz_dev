# if 语句

## if 语句

if 语句是像“如果○○则执行●●”这样、根据条件判断来决定是否执行脚本一部分的语法。

语法如下。

```
if(expression)
	ステートメントまたはブロック
else
	ステートメントまたはブロック
```

最初的“语句或块”是在对 expression 求值的结果为真时执行的，第 2 个“语句或块”是在求值的结果为假时执行的。不需要 **else** 之后的部分时可以不写。

```
	if(a==b)
		inform("a と b は同じです");

	if(a<b)
	{
		var t;
		t=a; a=b; b=t; // a と b を入れ替える
	}

	if(a==b)
		inform("a と b は同じです");
	else
		inform("a と b は違います");
```

## if 与 else 的对应

else 具有“对应前面的、尚未与 else 对应的 if”这一规则。



例如，

```
	if(expr) // ★
		if(expr) // ●
			statement;
		else // ●
			statement;
	else // ★
		statement;
```

这样编写时，★ 的 else 会对应 ★ 的 if，● 的 else 会对应 ● 的 if。

像 TJS2 这样的自由格式语言，即使把缩进弄错、写成

```
	if(expr) // ★
		if(expr) // ●
			statement;
	else // ●
		statement;
```

这样，对应关系也如上所述，因此需要注意。

希望明确区分对应关系时，

```
	if(expr) { // ★
		if(expr) // ●
			statement;
	}
	else // ★
		statement;
```

请采用像这样用块包围的方法。
