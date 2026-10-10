# 许可证信息的获取与显示

吉里吉里Z 把本体和插件所内嵌的第三方组件 (库、
字体等) 的许可证文本保存在可执行文件之中。这些内容
都可以从 TJS 取出列表和全文，因此游戏内的制作人员名单画面或许可证
显示画面都可以在脚本侧自由构建。

## 3 个来源

列表是把以下 3 个系统合并而成的。从脚本角度看，区别只有
`source` 成员的值，获取方法相同。

| `source` | 内容 | 提供方式 |
|---|---|---|
| `builtin` | 本体内嵌的部分 (引擎使用的库、随附字体) | 压缩后已嵌入可执行文件 |
| `plugin` | 插件注册的部分 | 插件 DLL 在加载时注册 |
| `storage` | 项目自带的部分 | 放在项目 `licenses` 文件夹中的文本 |

同名内容存在于多个来源时会被合并为 1 条
(优先级为 `plugin` > `builtin` > `storage`)。

## 从 TJS 获取

### 获取列表

[System.getLicenseList](../reference/System.md#getlicenselist) 返回字典的
数组。各元素拥有 `name` (显示名) `group` (分类) `source` (提供来源)。

```tjs
var list = System.getLicenseList();
for (var i = 0; i < list.count; i++) {
	var e = list[i];
	Debug.message(e.name + " / " + e.group + " / " + e.source);
}
```

`group` 是用于分类的字符串，本体内嵌的部分使用以下值。插件或
项目注册的部分可能是任意字符串，因此**不要写以穷举为前提的
`switch`** (对未知值采取原样显示等处理)。

| `group` | 内容 |
|---|---|
| `engine` | 引擎基础 (zlib / libpng / Oniguruma 等) |
| `font-engine` | 字体引擎 (FreeType / HarfBuzz 等) |
| `audio` | 音频 (libogg / libvorbis / Opus 等) |
| `video` | 视频 (libvpx / libyuv 等) |
| `ui` | UI 绘制 (Elements / ThorVG) |
| `platform` | 平台 (SDL3 / ANGLE 等) |
| `font` | 随附字体 |
| `data` | 放在项目 `licenses` 文件夹中的部分 |

### 获取全文

把 `name` 传给 [System.getLicenseText](../reference/System.md#getlicensetext)，
就会以字符串返回整个许可证文本。**找不到时返回 void**。

```tjs
var text = System.getLicenseText("FreeType");
if (text !== void) {
	Debug.message(text);
}
```

!!! warning "不要用 `if (text)` 判定"
    在 TJS2 中，把无法转换为数值的字符串放在条件表达式里会**始终为假**。
    像许可证文本这样的字符串请用 `text !== void` 判定。

### 把列表和全文汇总为一个字符串

这是想用文本一次性显示制作人员名单时的示例。

```tjs
function buildLicenseText()
{
	var list = System.getLicenseList();
	var buf = [];
	for (var i = 0; i < list.count; i++) {
		var name = list[i].name;
		var text = System.getLicenseText(name);
		if (text === void) continue;
		buf.add("======== " + name + " ========");
		buf.add(text);
	}
	return buf.join("\n");
}
```

### 按分类汇总

```tjs
var byGroup = %[];
var list = System.getLicenseList();
for (var i = 0; i < list.count; i++) {
	var e = list[i];
	if (byGroup[e.group] === void) byGroup[e.group] = [];
	byGroup[e.group].add(e.name);
}
```

读取字典中不存在的成员时会返回 void，因此可以像上面那样初始化。

### 与 System.licenseText 的区分使用

[System.licenseText](../reference/System.md#licensetext) 是把
“版本行 + 吉里吉里Z 本体条款 + 随附组件列表”
合成一个字符串的内容，面向**直接显示**的用途。
它不包含各个组件的全文，因此需要全文时请
使用 `getLicenseText`。

| 想做的事 | 使用的东西 |
|---|---|
| 直接显示本体条款 | `System.licenseText` |
| 想列出包含哪些内容 | `System.getLicenseList()` |
| 需要特定组件的全文 | `System.getLicenseText(name)` |

## 使用内置查看器

在可使用 ElementsDialog 的构建中，可以直接使用示例实现
`data/ui/license_dialog.tjs`。它采用左侧窗格 = 按分类的
项目列表、右侧窗格 = 许可证正文的 2 窗格结构。

```tjs
Scripts.execStorage("ui/license_dialog.tjs");
showLicenseDialog(win);          // モーダル。閉じるまでブロック
showLicenseDialog(win, false);   // 非モーダル ( 戻り値 = ElementsDialog )
```

可以复制到项目中并修改。没有 ElementsDialog 的构建
( `KRKRZ_USE_ELEMENTS=OFF` ) 中它什么也不做，返回 void。

## 把项目的素材加入列表

在项目的 `licenses` 文件夹中按 **1 个素材 = 1 个文本** 放置，
启动时就会自动并入列表 ( `source` 为 `storage`、`group` 为 `data` )。
扩展名支持 `.txt` 和 `.md`。

```
licenses/kenney-input-prompts.txt
licenses/myfont-regular.txt
```

- **显示名 ( `name` ) 是文件名去掉扩展名后转为小写的结果**。
  `MyFont-Regular.txt` 会以 `myfont-regular` 排列。想整理
  显示标题时，在文件正文第 1 行写上素材名会比较友好。
- `System.getLicenseText(name)` 也可以用同样的名字获取
  ( `licenses/<name>.txt` → 如果没有则 `.md` 的顺序查找 )。
- 文件请以 UTF-8 放置 ( 带 BOM 也可以 )。

### 记述示例

如果要随附常用于手柄按钮显示的
[Kenney Input Prompts](https://kenney.nl/assets/input-prompts) ( CC0 )，
就以 `licenses/kenney-input-prompts.txt` 的形式:

```
Input Prompts (Kenney)

This product includes "Input Prompts" by Kenney (www.kenney.nl),
released under Creative Commons Zero (CC0 1.0 Universal).

  https://kenney.nl/assets/input-prompts
  https://creativecommons.org/publicdomain/zero/1.0/

Attribution is not required, but appreciated:
  "Input Prompts" by Kenney (www.kenney.nl)
```

把 pack 随附的 License.txt 原样放置也可以。CC0 没有署名义务，
但放入列表可以让素材的来源管理和制作人员名单显示变得轻松。

## 通过启动选项确认

想不写脚本就确认内容时，可以使用启动选项
[-license](CommandLine.md)。它适合开发过程中的确认，以及检查
分发物中包含哪些内容。

```
krkrz64.exe -license            # 一覧
krkrz64.exe -license=FreeType   # 1 件の全文
krkrz64.exe -license=all        # 全件の全文
```

指定项目启动的话，该项目 `licenses` 文件夹中的
内容也会加入列表。`-about` 的“バージョン・著作権・環境情報”对话框
中也会显示同样的列表。

## 分发物中包含的文件

用 `make install` 生成的分发物中，除了运行时的列表之外，许可证原文
还会作为文件写出。

| 路径 | 内容 |
|---|---|
| `license.txt` | 吉里吉里Z 本体的条款 |
| `licenses/<名称>.txt` | 本体内嵌的第三方组件的原文 |
| `licenses/plugins/<名称>.txt` | 随附插件所内嵌部分的原文 |

哪个组件对应哪个许可证的对照表汇总在
[随附许可证列表](BundledLicenses.md) 中。

## 从插件注册

插件侧内嵌的许可证文本，通过 `tp_stub` 中公开的注册函数
并入列表 ( 注册后会作为 `source` 为 `plugin` 的条目出现 )。

| 函数 | 用途 |
|---|---|
| `TVPRegisterLicense(name, group, deflated, deflatedSize, originalSize)` | 注册已压缩的文本 ( 数据以引用方式保持 ) |
| `TVPRegisterLicenseText(name, group, text)` | 注册原始文本 ( 适合较短的内容 ) |
| `TVPGetLicenseText(name, &text)` | 按名称获取全文 |
| `TVPEnumLicenses(sink)` | 枚举全部条目 |

注册用的源码可以从 manifest 生成。机制和生成步骤请
参照引擎侧的 `src/core/doc/LicenseSystem.md`。
