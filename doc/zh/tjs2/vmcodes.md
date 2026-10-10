# 虚拟机

## TJS2 VM

TJS2 会先将脚本编译为供虚拟机 (TJS2 **VM**) 使用的二进制代码，然后再执行。

发生异常或进行转储时，会显示这个 TJS2 VM 的代码的反汇编结果，因此下面对这个虚拟机做简要说明。

## 指令码

TJS2 VM 中，函数、属性等每个执行单元都是独立的，某个函数不会与其他函数共享指令码空间、寄存器空间、标志和常量区。

指令指针 (ip) 在函数等执行单元的开头必定从 0 开始。

把指令码用让人容易阅读的简单名称来表示，这种名称称为助记符。

## 寄存器

TJS2 VM 的寄存器在助记符中以 %(数字) 表示。数字也可能是负数。寄存器数量没有限制。局部变量以及计算过程中的临时值等全部记录在寄存器中。不存在主内存 (main memory) 和栈。

寄存器所表示的值与 TJS2 中所谓的变量相同，可以表示整数、实数、对象、字符串、字节序列、void。

在当前版本中，寄存器 %0 始终为 void。寄存器 %-1 为 this。寄存器 %-2 是称为 **this proxy** 的特殊对象，对该对象进行成员引用时，会先查看 this，如果那里没有，则去查看 global。this proxy 在 global 层级的执行单元中不存在。函数等的参数会预先存入 %-3、%-4 等寄存器，然后开始执行。

除这类用途预先确定、或执行前已预先存入值的寄存器之外，其余寄存器的值在执行开始时是不确定的。

## 标志

TJS2 VM 只有一个标志，用于存放比较结果。标志只取真或假的值。

## 常量区

TJS2 VM 的常量区是存放常量的地方，在助记符中以 *(数字) 表示。常量区是只读的，要把这个常量区的值移入寄存器，需要使用 const 指令。此外，函数名、属性名等用于按名称访问对象成员的“名称”也存放在这个常量区中。

## VM 助记符一览

有些指令的操作数具有 `%obj.*name` 或 `%obj.%name` 的形式，这些指令都伴随对象成员引用。

操作数具有 `%obj.*name` 形式的指令进行直接引用，从寄存器 `%obj` 所表示的对象中引用具有 `*name` 所表示名称的成员。

操作数具有 `%obj.%name` 形式的指令进行间接引用，从寄存器 `%obj` 所表示的对象中引用具有 `%name` 所表示名称的成员。

这类指令的助记符带有 d 或 pd (direct / property direct)、以及 i 或 pi (indirect / property indirect) 的后缀。

后缀中带 p 的指令会使目标寄存器的属性处理器运行 (执行单目 '*' 运算符的行为)。

- ****nop**  
(no operation)**  
  什么也不做。
- ****const**  
(copy constant value)**  
  格式: `const %dest, *src`
  
  
  将 *src 所表示的常量区的值复制到 %dest 所表示的寄存器。
- ****cp**  
(copy register)**  
  格式: `cp %dest, %src`
  
  
  将 %src 所表示的寄存器的值复制到 %dest 所表示的寄存器。
- ****cl**  
(clear register)**  
  格式: `cl %dest`
  
  
  将 %dest 所表示的寄存器设为 void。
- ****ccl**  
(clear register)**  
  格式: `ccl %low-%high`
  
  
  将 %low 所表示的寄存器到 %high 所表示的寄存器为止的范围全部设为 void。
- ****tt**  
(test true)**  
  格式: `tt %reg`
  
  
  如果 %reg 所表示的寄存器表示真，则将标志设为真，如果表示假，则将标志设为假。
- ****tf**  
(test false)**  
  格式: `tf %reg`
  
  
  与 tt 相反，如果 %reg 所表示的寄存器表示真，则将标志设为假，如果表示假，则将标志设为真。
- ****ceq**  
(compare equal)**  
  格式: `ceq %reg1, %reg2`
  
  
  如果 %reg1 与 %reg2 以普通比较 (== 运算符的行为) 一致，则将标志设为真，否则设为假。
- ****cdeq**  
(compare distinct equal)**  
  格式: `cdeq %reg1, %reg2`
  
  
  如果 %reg1 与 %reg2 以识别比较 (=== 运算符的行为) 一致，则将标志设为真，否则设为假。
- ****clt**  
(compare littler than)**  
  格式: `clt %reg1, %reg2`
  
  
  如果 %reg1 > %reg2，则将标志设为真，否则设为假。
- ****cgt**  
(compare greater than)**  
  格式: `cgt %reg1, %reg2`
  
  
  如果 %reg1 < %reg2，则将标志设为真，否则设为假。
- ****setf**  
(set flag)**  
  格式: `setf %dest`
  
  
  如果标志为真，则将 %dest 设为真 (整数非 0)，如果为假，则将 %dest 设为假 (整数 0)。
- ****setnf**  
(set not flag)**  
  格式: `setnf %dest`
  
  
  与 setf 相反，如果标志为假，则将 %dest 设为真 (整数非 0)，如果为真，则将 %dest 设为假 (整数 0)。
- ****lnot**  
(logical not)**  
  格式: `lnot %reg`
  
  
  翻转 %reg 的真伪。
- ****nf**  
(not flag)**  
  格式: `nf`
  
  
  翻转标志的真伪。
- ****jf**  
(jump if flag)**  
  格式: `jf ip`
  
  
  如果标志为真，则跳转到 ip。
- ****jnf**  
(jump if not flag)**  
  格式: `jnf ip`
  
  
  如果标志为假，则跳转到 ip。
- ****inc**, **incpd**, **incpi**, **incp**  
(increment)**  
  格式: `inc %reg`
  
  格式: `incpd %res, %obj.*name`
  
  格式: `incpi %res, %obj.%name`
  
  格式: `incp %res, %propobj`
  
  
  
  将 %reg、%obj.*name、%obj.%name 或 %propobj 递增。
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****dec**, **decpd**, **decpi**, **decp**  
(decrement)**  
  格式: `dec %reg`
  
  格式: `decpd %res, %obj.*name`
  
  格式: `decpi %res, %obj.%name`
  
  格式: `decp %res, %propobj`
  
  
  
  将 %reg、%obj.*name、%obj.%name 或 %propobj 递减。
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****lor**, **lorpd**, **lorpi**, **lorp**  
(logical or)**  
  格式: `lor %dest, %src`
  
  
  取 %dest 与 %src 的逻辑或，将结果存入 %dest。
  
  
  格式: `lorpd %res, %obj.*name, %src`
  
  
  取 %obj.*name 与 %src 的逻辑或，将结果存入 %obj.*name。
  
  
  格式: `lorpi %res, %obj.%name, %src`
  
  
  取 %obj.%name 与 %src 的逻辑或，将结果存入 %obj.%name。
  
  
  格式: `lorp %res, %propobj, %src`
  
  
  取 %propobj 与 %src 的逻辑或，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****land**, **landpd**, **landpi**, **landp**  
(logical and)**  
  格式: `land %dest, %src`
  
  
  取 %dest 与 %src 的逻辑与，将结果存入 %dest。
  
  
  格式: `landpd %res, %obj.*name, %src`
  
  
  取 %obj.*name 与 %src 的逻辑与，将结果存入 %obj.*name。
  
  
  格式: `landpi %res, %obj.%name, %src`
  
  
  取 %obj.%name 与 %src 的逻辑与，将结果存入 %obj.%name。
  
  
  格式: `landp %res, %propobj, %src`
  
  
  取 %propobj 与 %src 的逻辑与，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****bor**, **borpd**, **borpi**, **borp**  
(bitwise or)**  
  格式: `bor %dest, %src`
  
  
  取 %dest 与 %src 的按位或，将结果存入 %dest。
  
  
  格式: `borpd %res, %obj.*name, %src`
  
  
  取 %obj.*name 与 %src 的按位或，将结果存入 %obj.*name。
  
  
  格式: `borpi %res, %obj.%name, %src`
  
  
  取 %obj.%name 与 %src 的按位或，将结果存入 %obj.%name。
  
  
  格式: `borp %res, %propobj, %src`
  
  
  取 %propobj 与 %src 的按位或，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****bxor**, **bxorpd**, **bxorpi**, **bxorp**  
(bitwise xor)**  
  格式: `bxor %dest, %src`
  
  
  取 %dest 与 %src 的按位异或，将结果存入 %dest。
  
  
  格式: `bxorpd %res, %obj.*name, %src`
  
  
  取 %obj.*name 与 %src 的按位异或，将结果存入 %obj.*name。
  
  
  格式: `bxorpi %res, %obj.%name, %src`
  
  
  取 %obj.%name 与 %src 的按位异或，将结果存入 %obj.%name。
  
  
  格式: `bxorp %res, %propobj, %src`
  
  
  取 %propobj 与 %src 的按位异或，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****band**, **bandpd**, **bandpi**, **bandp**  
(bitwise and)**  
  格式: `band %dest, %src`
  
  
  取 %dest 与 %src 的按位与，将结果存入 %dest。
  
  
  格式: `bandpd %res, %obj.*name, %src`
  
  
  取 %obj.*name 与 %src 的按位与，将结果存入 %obj.*name。
  
  
  格式: `bandpi %res, %obj.%name, %src`
  
  
  取 %obj.%name 与 %src 的按位与，将结果存入 %obj.%name。
  
  
  格式: `bandp %res, %propobj, %src`
  
  
  取 %propobj 与 %src 的按位与，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****sar**, **sarpd**, **sarpi**, **sarp**  
(shift arithmetic right)**  
  格式: `sar %dest, %src`
  
  
  将 %dest 按 %src 所表示的次数进行算术右移，将结果存入 %dest。
  
  
  格式: `sarpd %res, %obj.*name, %src`
  
  
  将 %obj.*name 按 %src 所表示的次数进行算术右移，将结果存入 %obj.*name。
  
  
  格式: `sarpi %res, %obj.%name, %src`
  
  
  将 %obj.%name 按 %src 所表示的次数进行算术右移，将结果存入 %obj.%name。
  
  
  格式: `sarp %res, %propobj, %src`
  
  
  将 %propobj 按 %src 所表示的次数进行算术右移，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****sal**, **salpd**, **salpi**, **salp**  
(shift arithmetic left)**  
  格式: `sal %dest, %src`
  
  
  将 %dest 按 %src 所表示的次数进行算术左移，将结果存入 %dest。
  
  
  格式: `salpd %res, %obj.*name, %src`
  
  
  将 %obj.*name 按 %src 所表示的次数进行算术左移，将结果存入 %obj.*name。
  
  
  格式: `salpi %res, %obj.%name, %src`
  
  
  将 %obj.%name 按 %src 所表示的次数进行算术左移，将结果存入 %obj.%name。
  
  
  格式: `salp %res, %propobj, %src`
  
  
  将 %propobj 按 %src 所表示的次数进行算术左移，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****sr**, **srpd**, **srpi**, **srp**  
(shift bitwise right)**  
  格式: `sr %dest, %src`
  
  
  将 %dest 按 %src 所表示的次数进行位右移，将结果存入 %dest。
  
  
  格式: `srpd %res, %obj.*name, %src`
  
  
  将 %obj.*name 按 %src 所表示的次数进行位右移，将结果存入 %obj.*name。
  
  
  格式: `srpi %res, %obj.%name, %src`
  
  
  将 %obj.%name 按 %src 所表示的次数进行位右移，将结果存入 %obj.%name。
  
  
  格式: `srp %res, %propobj, %src`
  
  
  将 %propobj 按 %src 所表示的次数进行位右移，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****add**, **addpd**, **addpi**, **addp**  
(add)**  
  格式: `add %dest, %src`
  
  
  将 %src 加到 %dest 上，将结果存入 %dest。
  
  
  格式: `addpd %res, %obj.*name, %src`
  
  
  将 %src 加到 %obj.*name 上，将结果存入 %obj.*name。
  
  
  格式: `addpi %res, %obj.%name, %src`
  
  
  将 %src 加到 %obj.%name 上，将结果存入 %obj.%name。
  
  
  格式: `addp %res, %propobj, %src`
  
  
  将 %src 加到 %propobj 上，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****sub**, **subpd**, **subpi**, **subp**  
(subtract)**  
  格式: `sub %dest, %src`
  
  
  从 %dest 中减去 %src，将结果存入 %dest。
  
  
  格式: `subpd %res, %obj.*name, %src`
  
  
  从 %obj.*name 中减去 %src，将结果存入 %obj.*name。
  
  
  格式: `subpi %res, %obj.%name, %src`
  
  
  从 %obj.%name 中减去 %src，将结果存入 %obj.%name。
  
  
  格式: `subp %res, %propobj, %src`
  
  
  从 %propobj 中减去 %src，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****mod**, **modpd**, **modpi**, **modp**  
(modulo)**  
  格式: `mod %dest, %src`
  
  
  将 %dest 除以 %src 所得的余数存入 %dest。
  
  
  格式: `modpd %res, %obj.*name, %src`
  
  
  将 %obj.*name 除以 %src 所得的余数存入 %obj.*name。
  
  
  格式: `modpi %res, %obj.%name, %src`
  
  
  将 %obj.%name 除以 %src 所得的余数存入 %obj.%name。
  
  
  格式: `modp %res, %propobj, %src`
  
  
  将 %propobj 除以 %src 所得的余数存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****div**, **divpd**, **divpi**, **divp**  
(real divide)**  
  格式: `div %dest, %src`
  
  
  用 %src 对 %dest 进行实数除法，将结果存入 %dest。
  
  
  格式: `divpd %res, %obj.*name, %src`
  
  
  用 %src 对 %obj.*name 进行实数除法，将结果存入 %obj.*name。
  
  
  格式: `divpi %res, %obj.%name, %src`
  
  
  用 %src 对 %obj.%name 进行实数除法，将结果存入 %obj.%name。
  
  
  格式: `divp %res, %propobj, %src`
  
  
  用 %src 对 %propobj 进行实数除法，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****idiv**, **idivpd**, **idivpi**, **idivp**  
(integer divide)**  
  格式: `idiv %dest, %src`
  
  
  用 %src 对 %dest 进行整数除法，将结果存入 %dest。
  
  
  格式: `idivpd %res, %obj.*name, %src`
  
  
  用 %src 对 %obj.*name 进行整数除法，将结果存入 %obj.*name。
  
  
  格式: `idivpi %res, %obj.%name, %src`
  
  
  用 %src 对 %obj.%name 进行整数除法，将结果存入 %obj.%name。
  
  
  格式: `divp %res, %propobj, %src`
  
  
  用 %src 对 %propobj 进行整数除法，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****mul**, **mulpd**, **mulpi**, **mulp**  
(multiply)**  
  格式: `mul %dest, %src`
  
  
  将 %dest 与 %src 相乘，将结果存入 %dest。
  
  
  格式: `mulpd %res, %obj.*name, %src`
  
  
  将 %obj.*name 与 %src 相乘，将结果存入 %obj.*name。
  
  
  格式: `mulpi %res, %obj.%name, %src`
  
  
  将 %obj.%name 与 %src 相乘，将结果存入 %obj.%name。
  
  
  格式: `mulp %res, %propobj, %src`
  
  
  将 %propobj 与 %src 相乘，将结果存入 %propobj。
  
  
  在上述指令中，带有 %res 参数的指令，如果 res 不为 0，则还会将结果存入 %res。
- ****bnot**  
(bitwise not)**  
  格式: `bnot %reg`
  
  
  将 %reg 按位取反，并再次存入 %reg。
- ****asc**  
(make ascii string)**  
  格式: `asc %reg`
  
  
  生成与 %reg 所表示的数值相当的 1 个字符，并再次存入 %reg。
- ****chr**  
(cheracter code)**  
  格式: `chr %reg`
  
  
  将 %reg 所表示的字符串的第一个字符的字符编码存入 %reg。
- ****num**  
(number)**  
  格式: `num %reg`
  
  
  将 %reg 所表示的寄存器转换为数值。
- ****chs**  
(change sign)**  
  格式: `chs %reg`
  
  
  将 %reg 所表示的寄存器的数值的正负取反。
- ****inv**  
(invalidate)**  
  格式: `inv %reg`
  
  
  将 %reg 所表示的对象无效化。
- ****chkinv**  
(invalidate)**  
  格式: `chkinv %reg`
  
  
  如果 %reg 所表示的对象未被无效化，则将 %reg 设为真，否则设为假。
- ****int**  
(convert to integer)**  
  格式: `int %reg`
  
  
  将 %reg 所表示的寄存器转换为整数。
- ****real**  
(convert to real)**  
  格式: `real %reg`
  
  
  将 %reg 所表示的寄存器转换为实数。
- ****string**  
(convert to string)**  
  格式: `string %reg`
  
  
  将 %reg 所表示的寄存器转换为字符串。
- ****octet**  
(convert to octet)**  
  格式: `octet %reg`
  
  
  将 %reg 所表示的寄存器转换为字节序列。
- ****typeof**, **typeofd**, **typeofi**  
(check type)**  
  格式: `typeof %reg`
  
  格式: `typeofd %obj.*name`
  
  格式: `typeofi %obj.%name`
  
  
  
  检查 %reg、%obj.*name 或 %obj.%name 的类型，并将表示该类型的字符串再次存入 %reg、%obj.*name 或 %obj.%name。
- ****eval**  
(evaluate expression)**  
  格式: `eval %reg`
  
  
  将 %reg 所表示的字符串作为表达式执行，并将结果再次存入 %reg。
- ****eexp**  
(execute expression)**  
  格式: `eexp %reg`
  
  
  将 %reg 所表示的字符串作为表达式执行，并丢弃结果。
- ****chkins**  
(check instance)**  
  格式: `chkins %reg, %classname`
  
  
  如果 %reg 所表示的对象是 %classname 所表示的类名的类的实例，则向 %reg 存入真，否则存入假。
- ****call**, **calld**, **calli**  
(function call)**  
  格式: `call %dest, %func(%arg1, %arg2, %arg3, ...)`
  
  格式: `calld %dest, %obj.*name(%arg1, %arg2, %arg3, ...)`
  
  格式: `calli %dest, %obj.%name(%arg1, %arg2, %arg3, ...)`
  
  
  
  以 %arg1, %arg2, %arg3 ... 为参数，调用 %func、%obj.*name 或 %obj.%name 所表示的函数对象，并将结果存入 %dest。如果 %dest 为 %0，则结果会被 ( 不存入 %0 而 ) 丢弃。
- ****new**  
(create new)**  
  格式: `new %dest, %func(%arg1, %arg2, %arg3, ...)`
  
  
  以 %arg1, %arg2, %arg3 ... 为参数，构造 %func 所表示的类对象，并将结果存入 %dest。
- ****gpd**, **gpds**  
(get property direct)**  
  格式: `gpd %dest, %obj.*name`
  
  格式: `gpds %dest, %obj.*name`
  
  
  
  从 %obj 所表示的对象中引用 *name 所表示的成员，并将该值复制到 %dest。
  
  gpd 会调用属性处理器，而 gpds 不调用属性处理器，直接获取属性对象本身。
- ****gpi**, **gpis**  
(get property indirect)**  
  格式: `gpi %dest, %obj.%name`
  
  格式: `gpis %dest, %obj.%name`
  
  
  
  从 %obj 所表示的对象中引用 %name 所表示的成员，并将该值复制到 %dest。
  
  gpi 会调用属性处理器，而 gpis 不调用属性处理器，直接获取属性对象本身。
- ****spd**, **spde**, **spdeh**, **spds**  
(set property direct)**  
  格式: `spd %obj.*name`
  
  格式: `spde %obj.*name`
  
  格式: `spdeh %obj.*name`
  
  格式: `spds %obj.*name`
  
  
  
  将 %src 的值赋给 %obj 所表示的对象的 *name 所表示的成员。
  
  spd 进行普通访问，但如果成员不存在则会发生异常。
  
  如果成员不存在，spde 会新建成员。
  
  spdeh 将成员设置为隐藏成员。在当前版本中没有意义。
  
  spds 不调用属性处理器，直接替换属性对象本身。
- ****spi**, **spie**, **spis**  
(set property indirect)**  
  格式: `spi %obj.%name`
  
  格式: `spie %obj.%name`
  
  格式: `spis %obj.%name`
  
  
  
  将 %src 的值赋给 %obj 所表示的对象的 %name 所表示的成员。
  
  spi 进行普通访问，但如果成员不存在则会发生异常。
  
  如果成员不存在，spie 会新建成员。
  
  spis 不调用属性处理器，直接替换属性对象本身。
- ****getp****  
  格式: `getp %reg, %propobj`
  
  
  
  使 %propobj 所表示的属性对象的 getter 运行，获取属性的值并代入 %reg。执行单目 '*' 运算符的行为。
- ****setp****  
  格式: `setp %propobj, %reg`
  
  
  
  使 %propobj 所表示的属性对象的 setter 运行，设置 %reg 的值。执行单目 '*' 运算符的行为。
- ****deld**, **deli**  
(delete member)**  
  格式: `deld %reg, %obj.*name`
  
  格式: `deli %reg, %obj.%name`
  
  
  
  删除 %obj 所表示的对象的 *name 或 %name 所表示的成员。
  
  将删除是否成功的布尔值存入 %reg，但如果 %reg 为 %0，则丢弃结果。
- ****srv**  
(set result value)**  
  格式: `srv %reg`
  
  
  将 %reg 的值作为函数的返回值 ( 函数的返回值将成为 %reg 所表示的值 )。
- ****ret**  
(return)**  
  格式: `ret`
  
  
  返回到调用方。
- ****entry**  
(enter try block)**  
  格式: `entry ip, %reg`
  
  
  进入受异常保护的块。发生异常时，跳转到 ip，并将异常对象设置到 %reg。
- ****extry**  
(exit from try block)**  
  格式: `extry`
  
  
  退出受异常保护的块。
- ****throw**  
(throw exception object)**  
  格式: `throw %reg`
  
  
  将 %reg 所表示的对象作为异常对象抛出。
- ****chgthis**  
(change this)**  
  格式: `chgthis %dest, %src`
  
  
  将 %dest 所表示的对象的闭包部分更改为 %src 所表示的对象。
- ****global**  
(get global object)**  
  格式: `global %dest`
  
  
  将全局对象存入 %dest。
- ****addci**  
(add class instance information)**  
  格式: `addci %dest, %info`
  
  
  向 %dest 所表示的对象的类实例信息中添加 %info。
- ****regmember**  
(register members)**  
  格式: `regmember`
  
  
  将类的成员注册到 "this" 对象。供内部使用。
- ****debugger**  
(call debugger)**  
  格式: `debugger`
  
  
  中断执行，调用调试器。在当前版本的实现中，调用的不是 TJS2 调试器，而是原生调试器。
