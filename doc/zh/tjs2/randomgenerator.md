# Math.RandomGenerator 类

## Math.RandomGenerator 类

Math.RandomGenerator 是用于生成基于 [Mersenne Twister 算法](http://www.math.keio.ac.jp/~matumoto/emt.html) 的随机数的类。


构造函数的语法如下。

```
new Math.RandomGenerator([<乱数種>]);
```

向构造函数指定数值时，随机数生成器会用该数值初始化。

向构造函数指定用 serialize 方法保存了状态的字典数组对象时，可以用该状态创建随机数生成器。

省略构造函数时，会用基于当前时间的随机数初始化随机数生成器 (在吉里吉里2 中，不是基于当前时间，而是用基于环境噪声的随机数生成器产生的随机数来初始化)。

## randomize

randomize 方法初始化随机数生成器。参数与向构造函数指定的内容相同。

## random

random 方法返回大于等于 0 且小于 1.0 的实数随机值。

## random32

random32 方法返回不小于 0 且不大于 4,294,967,295 (0xffffffff 以下) 的整数随机值。

## random63

random63 方法返回不小于 0 且不大于 9,223,372,036,854,775,807 (0x7fffffffffffffff 以下) 的整数随机值。

## random64

random64 方法返回不小于 -9,223,372,036,854,775,808 且不大于 9,223,372,036,854,775,807 的整数随机值。

## serialize

serialize 方法返回记录了当前状态的字典数组对象。把这个字典数组对象传递给构造函数或 randomize 方法，就可以再次重现当前状态。

## Copyright notice

Mersenne Twister 算法的实现使用了



A C-program for MT19937, with initialization improved 2002/2/10.
Coded by Takuji Nishimura and Makoto Matsumoto.



的改编版本。感谢两位公开了有用的程序源码。



Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura,

All rights reserved.



Redistribution and use in source and binary forms, with or without

modification, are permitted provided that the following conditions

are met:



1. Redistributions of source code must retain the above copyright

notice, this list of conditions and the following disclaimer.



2. Redistributions in binary form must reproduce the above copyright

notice, this list of conditions and the following disclaimer in the

documentation and/or other materials provided with the distribution.



3. The names of its contributors may not be used to endorse or promote

products derived from this software without specific prior written

permission.



THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS

"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT

LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR

A PARTICULAR PURPOSE ARE DISCLAIMED.	 IN NO EVENT SHALL THE COPYRIGHT OWNER OR

CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,

EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,

PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR

PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF

LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING

NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS

SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
