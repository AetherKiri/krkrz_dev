# 著作权等

## 第三方许可证的确认与显示

引擎、插件内置的第三方组件 ( 库 / 字体 ) 的
许可证文本，可以在运行时从 TJS 获取：

```tjs
var list = System.getLicenseList();   // [%[name, group, source], ...]
var text = System.getLicenseText("FreeType");
```

除了引擎本体内置的部分之外，插件注册的部分，以及**放在项目的 `licenses`
文件夹中的文本** ( 附加字体的许可证等 ) 也会合并到同一列表中。
获取方法、显示方式、素材的添加步骤
汇总在 **[许可证信息的获取与显示](Licenses.md)** 中。

- 使用启动选项 [-license](CommandLine.md) 也可以查看列表 / 全文
  ( `-about` 的对话框中也会列出列表 )。
- **哪个组件采用哪个许可证**
  汇总在 [随附许可证列表](BundledLicenses.md) 中
  ( 分为引擎本体 / 插件 / 字体三部分。由 manifest 自动生成 )。

## 著作权/许可证

请参阅 SDK 附带的 license.txt。

以下是关于著作权和许可证的 FAQ，以及许多人可能会感到疑问的事项。

原则上以 license.txt 中所述的内容为准，请务必过目 license.txt。

如果这里所写的内容与 license.txt 中所写的内容有出入，以 license.txt 中所写的内容优先。

- **需要向吉里吉里的作者支付费用吗……**  
  没有这个必要。
- **想用于商业用途 ( 含共享软件 )……**  
  也可以用于商业用途。
  
  即使是商业用途，使用也不需要许可费等费用。可以免费使用。
- **想在作品中写上您的名字……**  
  并不特别需要在文档等中写明使用了吉里吉里。
  
  当然，写上也没有关系 (^^;
  
  如果没有特别记载，则不能删除通过 -about 显示的许可证显示。
  
  如果按照修改版 BSD 许可证在文档等中记载了许可证显示，则也可以删除通过 -about 显示的许可证显示。
- **作品完成后必须通知吉里吉里的作者吗……**  
  没有通知使用了吉里吉里的义务。即使是商业用途，也没有通知义务。
  
  不过，如果能说一声的话，作者一定会很高兴的，是的。
- **想挪用吉里吉里的源代码……**  
  吉里吉里Z 采用修改版 BSD 许可证。也可以按照修改版 BSD 许可证挪用源代码。

## 致谢

吉里吉里2 以及吉里吉里Z 是在众多人士的协助下才得以成立的。感谢各位的厚意。

特别是在吉里吉里相关方面，PIA 少尉先生给予了许多建议。非常感谢。



吉里吉里Z 是通过众筹、由众多人士的资金支援开发而成的。

提供支援的各位 (排名不分先后，敬称略) 是：W.Dee, casper, 有限会社MCF, Biscrat, 青猫, nagai, ルー, 高際 雅之, 永劫, ゆんゆん探偵, りょうご（如今已不复存在的那颗星）, AZ-UME, 京 秋人, Katsumasa Tsuneyoshi, 小池潤, miahmie, サークル獏, アザナシ, はっしぃ, 棚中製作所, わっふる/waffle, Wamsoft, TYPE-MOON, 有限会社エムツー。



Win32Ole 插件为首的各种插件是由 Go Watanabe 氏提供的。非常感谢。



Photoshop 兼容的混合函数群由 Kenjo 氏提供。非常感谢。



手柄支持代码由 Kiyobee 氏提供。非常感谢。



KAGParser 类的文档、KAGParser 的扩展由 Kouhei Yanagita 氏提供。非常感谢。



吉里吉里的图标由 MIK 氏制作。非常感谢。



通过图层进行的视频播放等与视频播放相关的各种功能，整合了井元 武則 氏的“视频扩展”。非常感谢。

[http://www.kaede-software.com/](http://www.kaede-software.com/)



模糊处理的实现以 yun 氏提供的代码为基础。非常感谢。



mey 氏提供了 Pad 相关的功能增强补丁、String.reverse() 等的实现。非常感谢。



以下是吉里吉里使用的编程库 / 辅助软件的列表 (排名不分先后，敬称略)。感谢公开了这些有用库的各位。

- **IJG JPEG Library (Independent JPEG Group)**  
  [http://www.ijg.org/](http://www.ijg.org/)
  
  This software is based in part on the work of the Independent JPEG Group.
- **libpng (Guy Eric Schalnat, Andreas Dilger, Glenn Randers-Pehrson,  and others)**  
  [http://www.libpng.org/pub/png/libpng.html](http://www.libpng.org/pub/png/libpng.html)
- **zlib (Jean-loup Gailly, Mark Adler)**  
  [http://www.gzip.org/zlib/](http://www.gzip.org/zlib/)
- **ERINA-Library (L.Entis)**  
  [http://www.entis.jp/eri/](http://www.entis.jp/eri/)
  
  ERINA-Library Copyright (C) 2001 Leshade Entis, Entis-soft.
- **Regex++ (Dr John Maddock)**  
  [http://ourworld.compuserve.com/homepages/John_Maddock/regexpp.htm](http://ourworld.compuserve.com/homepages/John_Maddock/regexpp.htm)
  
  Regex++ Copyright (c) 1998-2000 Dr John Maddock
- **UPX (Markus F.X.J. Oberhumer & Laszlo Molnar)**  
  [http://upx.sourceforge.net/](http://upx.sourceforge.net/)
- **Shell Component Library (伊藤 隆志)**  
  [http://www.bekkoame.ne.jp/~itotaka/](http://www.bekkoame.ne.jp/~itotaka/)
- **NASM, The Netwide Assembler (Simon Tatham, Julian Hall and others)**  
  [http://nasm.sourceforge.net/](http://nasm.sourceforge.net/)
- **alink (Anthony A.J. Williams)**  
  [http://alink.home.dhs.org/](http://alink.home.dhs.org/)
- **md5.c (L. Peter Deutsch)**  
  Copyright (C) 1999, 2000, 2002 Aladdin Enterprises.  All rights reserved.
- **libogg/libvorbis (Xiph.Org Foundation)**  
  [http://www.xiph.org/](http://www.xiph.org/)
  
  
  
  Copyright (c) 2002, Xiph.org Foundation
  
  
  
  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:
  
  
  
  - Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
  
  
  
  - Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
  
  
  
  - Neither the name of the Xiph.org Foundation nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
  
  
  
  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
  A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR
  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
- **Ogg Vorbis 加速项目**  
  吉里吉里2 在 Phase Vocoder 内部使用了 blacksword 氏的 Ogg Vorbis 加速项目公开的、支持 SSE 的 FFT 运算代码。
  [http://homepage3.nifty.com/blacksword/](http://homepage3.nifty.com/blacksword/)
- **A C-program for MT19937 (Makoto Matsumoto and Takuji Nishimura)**  
  [http://www.math.keio.ac.jp/matumoto/emt.html](http://www.math.keio.ac.jp/matumoto/emt.html)
  
  
  
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
  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
- **LibTomCrypt (Tom St Denis)**  
  [http://libtomcrypt.org/](http://libtomcrypt.org/)
- **AGG (Anti-Grain Geometry)**  
  [http://antigrain.com/](http://antigrain.com/)
  
  
  
  The Anti-Grain Geometry Project
  
  A high quality rendering engine for C++
  
  http://antigrain.com
  
  
  
  Anti-Grain Geometry - Version 2.3
  
  Copyright (C) 2002-2005 Maxim Shemanarev (McSeem)
  
  
  
  Permission to copy, use, modify, sell and distribute this software
  is granted provided this copyright notice appears in all copies.
  This software is provided "as is" without express or implied
  warranty, and with no claim as to its suitability for any purpose.
- **Expat**  
  [http://expat.sourceforge.net/](http://expat.sourceforge.net/)
  
  
  
  Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
  and Clark Cooper
  
  Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006 Expat maintainers.
  
  
  
  Permission is hereby granted, free of charge, to any person obtaining
  a copy of this software and associated documentation files (the
  "Software"), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so, subject to
  the following conditions:
  
  
  
  The above copyright notice and this permission notice shall be included
  in all copies or substantial portions of the Software.
  
  
  
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
- **Oniguruma**  
  [http://www.geocities.jp/kosako3/oniguruma/index_ja.html](http://www.geocities.jp/kosako3/oniguruma/index_ja.html)
  
  
  
  Copyright (c) 2002-2007  K.Kosako ( sndgk393 AT ybb DOT ne DOT jp )
  All rights reserved.
  
  
  
  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:
  
  1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
  
  THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
  OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
  OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
  SUCH DAMAGE.
- **FreeType**  
  [http://www.freetype.org/](http://www.freetype.org/)
  
  Copyright 1996-2002, 2006 by David Turner, Robert Wilhelm, and Werner Lemberg
- **picojson**  
  [https://github.com/kazuho/picojson](https://github.com/kazuho/picojson)
  
  
  
  Copyright 2009 Cybozu Labs, Inc.
  
  
  
  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:
  
  1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
  
  THIS SOFTWARE IS PROVIDED BY CYBOZU LABS, INC. ``AS IS'' AND ANY EXPRESS OR
  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
  EVENT SHALL CYBOZU LABS, INC. OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  
  
  
  The views and conclusions contained in the software and documentation are
  those of the authors and should not be interpreted as representing official
  policies, either expressed or implied, of Cybozu Labs, Inc.
