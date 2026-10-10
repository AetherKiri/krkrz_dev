# switch 语句

## switch 语句

使用 switch 语句，可以简洁地编写 if ~ else if。它采用以下语法。

```
switch(base_expression)
{
**case** condition_expression1 :

case condition_expression2 :

:
:

**default**:

:
:
}
```

在 base_expression 中写表达式，首先对该表达式求值。在 switch 后面的块中 case 后面的 condition_expression? 中也写表达式。

condition_expression? 在块内被依次求值。若求值结果与 base_expression 相同，则从那里开始执行。与 condition_expression? 不一致时，其间写的语句会被忽略。另外，一致时，此后的 case 与 default 会被忽略。

default: 可以省略，但写了 default 时，default 之后的语句会被强制执行。

要跳出块，需写 **break**;。忘记写 break 而一直执行到下一个 case 的内容是常有的事，请注意。

```
	switch(a)
	{
	case 0:
		inform("a は 0 です");
		break;
	case 1:
		inform("b は 1 です");
		break;
	case 2:
		inform("b は 2 です");
		break;
	default:
		inform("b は 0 でも 1 でも 2 でもありません");
	}


	switch(a)
	{
	case 0:
	case 1: // break がないので case 0 の場合はここを通過する
		inform("a は 0 か 1 です");
		break;
	case 2:
		inform("a は 2 です");
	} // default がないので 0 1 2 以外の場合はなにも実行されない


	switch(a)
	{
	case b+1: // case の後には式も指定できる
		inform("a==b+1");
		break;
	case c+b:
		inform("a==c+b");
	}

	switch(str)
	{
	case "あいうえお": // 文字列も指定できる
		type=1;
		break;
	case "かきくけこ":
		type=2;
		break;
	}
```
