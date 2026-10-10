# 存储系统

## 关于存储系统

在吉里吉里中，对于文件、归档内的文件以及其他资源，不用“文件”而特意称为“存储”。

## 统一存储名

统一存储名是仅在吉里吉里内部使用的、表示存储的名称，以类似 URI 的方式来表示存储。

表记方式为



`メディア://ドメイン/パス`



的形式。路径的分隔符使用 / (斜杠)。

## 本地存储

表示本地存储 (本地文件) 的统一存储名，媒体使用 file，域使用 . (点)。此外，在 Windows 的情况下，路径的开头为驱动器盘符。



例如，C:\Program Files\Game\game.exe 会成为

`file://./c/program files/game/game.exe`

的形式。



[Storages.getFullPath](../reference/Storages.md#getfullpath) 方法可以将 OS 使用的文件名转换为统一存储名。在此过程中，文件名中的大写字母会全部转换为小写 (对于本地存储，不区分大小写)。此外，如果路径分隔符中使用了 \，则会被转换为 /。

[Storages.getLocalName](../reference/Storages.md#getlocalname) 方法可以将统一存储名转换为 OS 使用的文件名。在把存储名传递给吉里吉里以外的应用程序等场合，需要使用此方法。

## 归档存储

指定归档内的存储时，用 > 分隔，> 之前的部分指定为归档存储的存储名，> 之后的部分指定为归档内的路径。



例如，如果是 file://./c/program files/game/game.xp3 内的 image/base.jpg 这个存储，则会成为

`file://./c/program files/game/game.xp3>image/base.jpg`

的形式。

从 2.19 beta 14 起，归档的分隔符从 '#' 变为 '>'。



吉里吉里标准情况下可以处理 XP3 这种吉里吉里独有格式的归档存储 (因为它是 XPK 第 3 代的格式，所以叫 XP3)。关于 XP3 格式归档的创建方法

请参照。

## 项目文件夹

使用吉里吉里制作游戏或工具等时，一般会把所有必要的文件汇总到“项目文件夹”中进行开发。吉里吉里在启动时会把项目文件夹设置为当前文件夹。

只要全部用项目文件夹内的相对路径来指定，即使通过 Releaser 打包成单一的可执行文件等，也不需要更改路径指定。

## 数据保存位置

数据保存位置是

的 -datapath 选项所指定的文件夹。可以通过 [System.dataPath](../reference/System.md#datapath) 属性获取。

吉里吉里输出的各种日志以及每个用户的设置文件都会输出到这里。

不指定 -datapath 时，Windows 下为可执行文件旁边的 `savedata`，**Linux 版为 `~/.local/share/<orgname>/<appname>/`** (从 2026-10 起)。详情请参照[命令行选项](CommandLine.md)的 -datapath。

此外，用户制作游戏或工具等时，建议将数据保存到这里。
