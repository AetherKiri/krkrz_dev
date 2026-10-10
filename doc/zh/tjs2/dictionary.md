# Dictionary 类

## Dictionary 类

Dictionary 类是处理**字典数组**的类。



字典数组也被称为**关联数组**，是一种把名字和与之绑定的值作为一个对、并保存多个这样的对的对象。

与数组一样，用 **[ ]** (间接引用) 运算符访问，但使用字符串代替下标，该字符串就是名字。如果名字作为标识符有效，也可以使用 **.** (直接引用) 运算符。

另外，参照不存在的名字时会变为 void。

要删除元素，使用 delete 运算符。

```
	var d=new Dictionary();
	d["sat"] = 1; // d.sat = 1 と同じ
	d["sun"] = 2; // d.sun = 2 と同じ
	d["mon"] = 3; // d.mon = 3 と同じ
	d["name"] ="value!"; // d.name = "value!" と同じ
	d["continue"] = 4; // continue は識別子ではないが OK
	d.continue = 4; // continue は識別子ではないのでエラー

	var sat = d["sat"]; // 1 が代入される
	var none = d["none"]; // void が代入される

	delete d.sat; // sat を削除
	delete d["continue"]; // continue を削除
```

## 表达式中的字典数组

使用 `**%[ ]**`，可以在表达式中就地书写 `Dictionary` 类的对象。把 元素名 => 元素的值 用逗号分隔，列举作为初始元素的表达式。例如，

`
var dic = %["a" => 1, "b" => 2, "c" => 3];

`

这样编写，就会给 `dic` 代入对 `Dictionary` 类对象的引用，该对象的元素名与元素的组分别为 `"a":1`、 `"b":2`、 `"c":3`。

在内部，`=>` 与逗号完全相同，但考虑到易读性，`=>` 也可以使用 ( 与 perl 相同 )。

## 对 Dictionary 类方法的访问

Dictionary 类的对象在被创建的状态下，一个成员也不持有。

例如，想使用 assign 方法时，即使对 Dictionary 类的对象 dict 写成 `dict.assign(src)` 这样，由于 dict 不持有名为 assign 的方法，也会出错。

因此，使用 **incontextof** 运算符，把直接属于 Dictionary 类的方法，以作为目标的 Dictionary 类的对象为上下文来执行。

```
	var a = %[];
	var b = %[];
	(Dictionary.assign incontextof a)(b); // b を a にコピー
	(Dictionary.clear incontextof b)(); // b の内容をクリア
```

## saveStruct

saveStruct 执行向文件输出结构化数据的操作。

请参阅同方法。

## assign

assign 方法复制字典数组。

```
構文 : assign(<コピー元辞書配列>, <内容をクリアするか=true>)
```

原样复制由参数指定的其他字典数组的内容。

“是否清除内容”为假时，不清除复制目标 ( 执行方法的对象 ) 的内容，而是用复制源字典数组的内容覆盖它。复制目标字典数组中若有与复制源字典数组同名的成员，复制目标会被复制源的内容覆盖。



在把数组 ( Array 类的对象 ) 指定为复制源数组时，视为该数组中按名字、值的顺序排列着应成为当前字典数组成员的内容，把该数组的内容复制到当前字典数组中。

## assignStruct

assignStruct 方法复制字典数组。

```
構文 : assignStruct(<コピー元辞書配列>)
```

原样复制由参数指定的其他字典数组的内容。

与 assign 方法不同，成员中若有数组或字典数组，也会递归复制其内容 ( assign 方法的情况下只复制引用 )。

## clear

clear 方法消去字典数组的全部内容。
