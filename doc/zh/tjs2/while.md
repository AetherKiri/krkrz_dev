# while 语句

## while 语句

**while** 语句在指定条件为真期间，反复执行语句或块。可以创建循环。

语法如下。

```
while(expression)
	ステートメントまたはブロック
```

“语句或块”在作为条件表达式的 expression 为真期间，被反复执行。



其运行方式如下，

(1) 首先对 expression 求值，若为假，则不执行语句或块

(2) 执行语句或块

(3) 对 expression 求值，若结果为真则转到 (2)，否则 while 语句结束



也就是说，如果一开始 expression 就为假，则不会执行语句或块。另外，并不是总会对 expression 求值，而是每执行一次语句或块，就会检查一次 expression 的真假。

另外，在 (3) 的阶段，如果是块，则暂时从块中退出 ( 也就是说，变量等会被删除 )。

```
	while(func()) ;
	/* func() が真の間、何もしないで func() を評価し続ける */

	while(func()) i++;
	/* func() が真の間、i++ を実行し続ける */

	while(i < 5) // i が 5 より小さい間
	{
		func(i);
		i++;
	}
```

## break

break 语句用于希望中途结束 while 的情况。

```
	while(true) // break が実行されない限りは無限ループ
	{
		if(func()) break; // func() が真ならばwhile終了
		func2(); // ↑で break が実行されなければここにくる
	}
	// break が実行されると、ここにくる
```

## continue

continue 语句用于希望中途从条件表达式的求值重新开始的情况。

执行 continue 后，执行会转到 (3)。

```
	var i = 0;
	while(i < 5)
	{
		if(func1()) continue;
		// func1() が true ならば、i < 5 の条件式チェックがされ、真ならば
		// またブロックの先頭から実行される
		func2();
		i++;
	}
```

## do~while

do~while 语句与 while 语句相同，但最初不进行条件表达式的检查。

语法如下。

```
do
	ステートメントまたはブロック
while(expression);
```

由于最初不检查条件表达式，即使条件表达式在 do 的阶段为假，“语句或块”也会被执行。

一旦“语句或块”被执行，就会检查条件表达式，若为假则跳出循环，若为真则再次执行语句或块，如此反复。
