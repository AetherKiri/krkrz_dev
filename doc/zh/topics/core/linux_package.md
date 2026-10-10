# Linux 版的发布包 (krkrz_linux)

这是把吉里吉里Z 本体与作品的数据汇总到一起，制作面向 Linux 的发布物的方法。
工具是外围仓库 [krkrz_linux](https://github.com/wamsoft/krkrz_linux)。
它与 krkrz_android / krkrz_ios / krkrz_web 一样，引擎通过 `KRKRZ_BASE` 引用
krkrz_dev，只负责 Linux 特有的构建与打包。

## Linux 的发布格式与方针

Linux 没有像 Android 的 APK 那样“一个就够”的应用格式，分发目标不同，格式就不同。
不过，无论哪种都是给“可以直接运行的文件夹”附上 freedesktop 的
元数据 ( `.desktop` / 图标 / AppStream ) 后重新包装出来的。

| 格式 | 主要分发目标 | krkrz_linux |
|---|---|---|
| 文件夹 / tar.gz | Steam 的 depot、itch.io、GOG、Humble | ✅ 输出 |
| AppImage | 自有网站、itch.io | 未实现 ( 可以从同一个文件夹制作。`.desktop` 与图标已生成 ) |
| Flatpak | Flathub | 未定 ( 需要 AppStream 元数据与清单 ) |

Steam 在游戏方面很重要，而它接收的就是文件夹本身，因此方针是**把文件夹作为正式的
交付物，其他格式都只是它的重新包装**。

## 构建环境

在 Valve 的 **Steam Linux Runtime 3.0 "sniper" SDK** ( Debian 11 / glibc 2.31 ) 的
容器中构建。生成的二进制可在 SteamOS 原生、Steam Linux Runtime、glibc 2.31 及以后
的一般发行版上运行。镜像使用 [steamdev](https://github.com/wamsoft/steamdev) 的
`deckbuild/deckbuild.sh image` 生成的 `deckbuild-sniper`。合格标准 ( 要求 glibc ≤ 2.31 /
无 GLIBCXX 依赖 ) 以引擎侧的 `src/core/doc/LinuxBuild.md` 为 SSOT。

## 使用方法

```bash
export KRKRZ_BASE=~/kirikiri                 # krkrz_dev のある親フォルダ
cd ~/kirikiri/krkrz_linux
make all                                     # サンプル案件 (コアデモ)
PROJECT_DIR=/path/to/mygame make all         # 自分の案件
```

输出位于 `${PROJECT_DIR}/build/linux/` 下。

- `package/<exeName>/` … 可以直接运行的文件夹
- `dist/<exeName>-<version>-linux-x86_64.tar.gz` … 将它打包的结果

项目的定义文件是 `${PROJECT_DIR}/linux-config.json`。`cmake` ( 插件构成 ) 与
`assetPack` ( 素材的引入，先到先得 ) 采用与 krkrz_android 的 `app-config.json` 相同的
书写格式，因此可以共享项目文件夹的素材定义。条目一览请参阅 krkrz_linux 的
README。

## 包的内容

```
mygame/
  mygame                 実行ファイル ( KRKRZ_EXE_NAME )
  libSDL3.so.0 ( .x.y )  同梱 SDL3
  plugin/*.so            プラグイン
  mygame.cf              orgname / appname ほか ( 生成 )
  <id>.desktop, <id>.svg freedesktop のメタデータ ( 生成 )
  license.txt, licenses/
  data/ または data.xp3  引数なしで起動すると自動検出される
```

### 随附 .so 的解析 ( RPATH )

可执行文件中以 **DT_RPATH** 嵌入了 `$ORIGIN`，用 `krkrz_plugin()` 生成的插件则
嵌入了 `$ORIGIN:$ORIGIN/..`。随附的 SDL3 以及插件依赖的 .so ( 放在 `plugin/` 或
可执行文件所在文件夹中 ) 无需 `LD_LIBRARY_PATH`，也不需要启动脚本就会被读取。

从 Steam 启动时，`LD_LIBRARY_PATH` 的开头会被加入 Steam 运行时与 `/usr/lib`，
因此使用 RUNPATH ( 新版链接器的默认值 ) 或 `LD_LIBRARY_PATH=.` 时，会先读取到
SteamOS 侧的同名 .so。DT_RPATH 的搜索顺序在它们之前，所以能确保使用随附版。
用自定义 CMake 附加 RPATH 的插件请使用 `--disable-new-dtags`
( 如果带有 RUNPATH，可执行文件侧的 DT_RPATH 也会失效 )。

## 存档数据的位置 ( 2026-10~ )

!!! warning "重要 (2026-10 的更改)"
    Linux 版默认的数据保存位置 ( 未指定 `-datapath` 时 ) 已从可执行文件旁边的
    `savedata` 改为 **`~/.local/share/<orgname>/<appname>/`** ( 如果有
    `$XDG_DATA_HOME`，则在其下 )。详情请参阅
    [命令行选项的 -datapath](../../guide/CommandLine.md)。

- **从项目的设置中取得 `orgname` / `appname` 并写入 `<exeName>.cf`** 是既定做法。
  krkrz_linux 会从 `linux-config.json` 的 `orgName` / `appName` 自动写入。
  这样每个作品都会有不同的文件夹
- 因为不会写到可执行文件旁边，所以放在只读位置 ( AppImage、Flatpak、
  `/opt` 等 ) 也能运行
- `System.dataPath` 是本地路径 ( `file://./home/…` )，因此也可以使用
  `Storages.getLocalName()`
- 实际的保存位置可以通过启动日志中的 `datapath (Linux default, …)` 行确认

### Steam Cloud

使用 Steamworks 的 Auto-Cloud 时，请把 Linux 的根设置为 `LinuxXdgDataHome`
( = `~/.local/share` )，子目录设置为 `<orgname>/<appname>`。它与 Windows 版的
保存位置不同，同时发布两者时请用“根覆盖”按 OS 分别指定 ( 根类型的名称请在
Steamworks 的设置画面确认 )。

## 在 Steam Deck 上确认

krkrz_linux 的输出文件夹可以用 steamdev 直接发送到 Deck。

```bash
steamdev -d <deck> deploy --gameid mygame_linux \
    --dir build/linux/package/mygame --command "./mygame" --start
```

gameid 只能使用字母数字、`_`、`.` ( 不能使用连字符 )。2026-10-06 已用 krkrz_linux 的
示例项目 ( 核心演示 ) 确认：在 Deck 上原生运行时 `-demotest` 全部 24 个场景 ok、
随附的 SDL3 被读取、保存位置为 `/home/deck/.local/share/wamsoft/krkrz-sample/`。

整体步骤与坑点请参阅 [Steam Deck 实机确认](steamdeck.md)。

## 今后

- AppImage 输出 ( 加上 `AppRun` 后用 `appimagetool` 打包 )
- xp3 归档与 krkrz_android 一样由项目侧预先制作，用 `assetPack` 的
  `flatten` 引入 ( 不在外围仓库中制作 )。计划在 krkrz_dev 侧准备一个
  生成未加密的普通 xp3 的通用 CLI
- Flatpak 等到有需求时再说
- macOS ( .app ) / Windows / Xbox 也在调查之中，方向是用统一了
  `*-config.json` 的 `cmake` / `assetPack` 书写格式的外围仓库来对齐

## 相关

- [krkrz_linux](https://github.com/wamsoft/krkrz_linux) — README 中有设置条目一览
- [Steam Deck 实机确认 ( 发布前检查 )](steamdeck.md)
- [命令行选项](../../guide/CommandLine.md) — `-datapath` / `-orgname` / `-appname` 与 `.cf` 的格式
