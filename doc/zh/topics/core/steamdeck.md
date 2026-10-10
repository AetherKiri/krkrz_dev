# Steam Deck 实机确认 ( 发布前检查 )

这是一套只用命令行完成面向 Steam 发布的 Linux 原生构建、以及在 Steam Deck
实机上进行运行确认的步骤。作为**发布前检查的一个项目**使用。

工具是 [steamdev](https://github.com/wamsoft/steamdev) ( 无头 Steam Deck
控制 CLI + sniper 交叉构建环境 )。umbrella 根目录的 `deckproject.toml` 是
krkrz 的构建、素材构建、启动的定义。

- 构建环境的内容与**二进制的合格标准**见
  [LinuxBuild.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LinuxBuild.md)
  ( engine 侧 SSOT )
- steamdev 侧的详情见 `docs/WORKFLOW.md` / `docs/DECKPROJECT.md` /
  `deckbuild/README.md`
- 把作品整理为发布用文件夹 / tar.gz 的是
  [Linux 版发布包 ( krkrz_linux )](linux_package.md)。其输出也可以
  用相同的步骤发送到 Deck 进行确认

---

## 0. 准备 ( 每个环境 1 次 )

| 要求 | 确认命令 |
|---|---|
| steamdev CLI ( editable 安装 ) | `steamdev --version` |
| WSL2 + docker + sniper 构建镜像 | `wsl -e docker images \| grep deckbuild-sniper` |
| 与 Deck 已配对 ( devkit 密钥 ) | `steamdev discover` → `steamdev -d <ip> status` |

尚未整备时，请按照 steamdev 的 README“初始设置”进行
( 镜像创建需要下载数 GB，仅首次 )。

**从 Linux 主机使用** ( 不使用 WSL ) 时的差异:

- steamdev 用 `uv tool install --editable <steamdev> --with zeroconf` 安装
  ( 在 Debian / Ubuntu 系上即使没有 python3-venv，用 uv 也能装 )。镜像用
  `bash <steamdev>/deckbuild/deckbuild.sh image`
- devkit 密钥是 `~/.config/steamos-devkit/devkit_rsa`。即使已经在 Windows 官方客户端上
  配对过，这个主机也需要另行配对。**先在 Deck 侧打开
  “設定 → 開発者 → Pair new host”**，再执行 `steamdev -d <ip> register`
  ( 不打开会返回 HTTP 403 )
- Deck 的 `~/devkit-utils` 来自官方客户端。Linux 主机没有随附的 utils，
  因此只要曾从 Windows 传输过一次，就不需要 `sync-utils`
- Deck 也可以用 `avahi-browse -rpt _steamos-devkit._tcp` 发现
- 容器以 root 运行，因此在 Linux 主机上 `bin/x64-linux/` 会变成 root 所有
  ( 恢复方法见 LinuxBuild.md )

可以固定 Deck 的 IP，无需每次输入。

```powershell
$env:STEAMDEV_DEVICE = "192.168.x.x"
```

---

## 1. 检查步骤

### 1-1. Linux 构建 ( sniper 容器 )

```bash
steamdev project -p . build linux
```

在 Valve 官方 Steam Linux Runtime 3.0 “sniper” SDK ( Debian 11 / glibc 2.31 /
gcc-14 ) 的容器中构建。**这是 Linux 构建的合格判定标准**，
即使 WSL 的 Ubuntu 等环境直接构建能通过，也不算确认过
( 因为 glibc 太新，在发布目标上无法运行 )。

成果物会被安装到 `bin/x64-linux/Release/`。

### 1-2. 二进制的合格标准

```bash
wsl -e bash -lc "cd /mnt/d/.../bin/x64-linux/Release && \
  objdump -T krkrz | grep -o 'GLIBC_[0-9.]*' | sort -uV | tail -1 && \
  objdump -T krkrz | grep -c GLIBCXX"
# Linux ホストなら wsl -e を外してそのまま
readelf -d bin/x64-linux/Release/krkrz | grep RPATH     # (RPATH) [$ORIGIN]
```

- 要求的 glibc 最大值为 **2.31 以下**
- **GLIBCXX 依赖为 0** ( libstdc++ 为静态链接 )
- 可执行文件带有 **`$ORIGIN` 的 RPATH** ( 为了可靠地读取随附的 SDL3。插件为
  `$ORIGIN:$ORIGIN/..` )

### 1-3. 传输与启动

```bash
steamdev project -p . stage linux            # 資材構築 (.deckstage/linux)
steamdev project -p . deploy linux --start   # 転送 + Steam 登録 + 起動
# 1-1〜1-3 をまとめて: steamdev project -p . ship linux
```

### 1-4. 启动确认要看“进程 + 画面”两点

```bash
steamdev exec -- "pgrep -a krkrz"
steamdev screenshot -o deck.png
```

有进程也不一定是在前面 ( gamescope 会把最后启动的放到前面 )。
**一定要看到截图为止**。`run-game` 刚执行后，Steam 侧的处理会有
数秒到十数秒的延迟，所以等待后再确认。

### 1-4b. 核心演示全部场景的显示确认 ( 推荐 )

替换启动参数，在 Deck 上运行 `-demotest -demotestcap`，就会巡回演示的全部场景并
截取 PNG，结束后自行退出。用 `steamdev deploy` 临时替换启动命令
( 参数会在注册时被固化，因此结束后用
`steamdev project -p . deploy linux` 恢复原状 )。

```bash
steamdev project -p . stage linux
steamdev deploy --gameid krkrz_linux --dir .deckstage/linux --clean --start \
    --command "./krkrz data -demotest -demotestcap=/home/deck/krkrz_demotest -loglevel=info"
# 終了待ち: steamdev exec -- "pgrep -x krkrz" が空になるまで
steamdev exec -- "ls /home/deck/krkrz_demotest | wc -l"     # シーン数
steamdev exec -- "grep -a '@demotest:' ~/.local/share/Steam/logs/console-linux.txt | tail -2"
steamdev ssh-command      # 表示された ssh のオプションで rsync -e "ssh ..." すればキャプチャを回収できる
steamdev project -p . deploy linux                            # 起動コマンドを戻す
```

从 Steam 启动的应用的标准输出会进入 Deck 的
`~/.local/share/Steam/logs/console-linux.txt` ( 因为会混入二进制内容，所以
用 `grep -a` )。已加载的 .so 可以通过 `/proc/$(pgrep -x krkrz)/maps` 确认。

### 1-5. 用 REPL 确认内部情况 ( 可选 )

`deckproject.toml` 的启动命令里带有 `-replweb`，因此会在 Deck 上的
127.0.0.1:8899 启动 REPL 服务器。由于绑定 localhost，必须使用隧道。

```bash
steamdev tunnel -L 18899:8899        # 別ターミナルで開いたまま
# (deckproject.toml で -replwebidle=no にしてあるので、ブラウザを閉じても落ちない)
curl -s http://127.0.0.1:18899/state                       # コントローラ
curl -s -X POST -d 'System.getTickCount()' http://127.0.0.1:18899/pad/exec
curl -s -X POST -d 'op=add&expr=System.osName' http://127.0.0.1:18899/watch
```

用浏览器打开 `http://127.0.0.1:18899/` 即可直接使用 Console / Watch / Pad 的
UI。详情见 [REPL](repl.md)。

### 1-6. 善后清理 ( 必须执行 )

```bash
steamdev exec -- "pgrep -a krkrz"     # PID を確認
steamdev exec -- "kill -9 <PID>"      # 先に止める (下記の注意)
steamdev delete krkrz_linux
steamdev exec -- "ls ~/devkit-game/"  # 残骸が無いか確認
```

---

## 2. Windows ( Proton ) 目标

用相同的机制，可以让 Windows 构建在 Proton 上运行来确认。

```bash
steamdev project -p . ship windows
```

`compat_tool` 指定 **Deck 上已安装的 Proton**
( `deckproject.toml` 是 `proton-stable` )。指定未安装的
`proton-experimental` 等会**无声地启动失败**。
Proton 首次启动因生成 prefix 需要数十秒，这是正常的。

---

## 3. 常见陷阱 ( 实测 )

| 症状 | 原因与处理 |
|---|---|
| **`steamdev delete` 后应用仍在运行** | delete 只删除素材和快捷方式，**不会停止进程**。要先 kill |
| `pkill -f krkrz_linux` 无效 / 误杀自己 | 模式也会匹配到自己的远程 shell。即使用括号 ( `krkrz_[l]inux` ) 也可能排除不掉，所以**用 `pgrep -a` 查看 PID 再 `kill -9 <PID>`** 最可靠 |
| Linux 二进制启动即死 / 随附 SDL3 没有被使用 | 随附 `.so` 的解析交给 exe 的 `$ORIGIN` (DT_RPATH) 与安装时生成的 soname 链接 `libSDL3.so.0`。如果 `readelf -d krkrz` 里没有 `(RPATH) [$ORIGIN]` 的旧构建，就会读到进入 Steam 的 `LD_LIBRARY_PATH` 的 `/usr/lib` 中的 SteamOS 版 SDL3 ( 被读到的 .so 可通过 `/proc/<pid>/maps` 确认 ) |
| 更改了启动参数却没有反映 | 参数会在注册快捷方式时被固化到 Steam 侧。改写设备上的 `<gameid>-argv.json` 也没有用，**必须重新部署** |
| curl `-d 'expr=a+b'` 的 `+` 变成空白 | form-urlencoded 的规格。`+` 要写成 **`%2B`** |
| 构建因 `_mm256_*` 未定义而失败 | sniper SDK 默认的 gcc-10 太旧。deckbuild 把 gcc-14 设为默认 |
| `deckbuild.sh image` 因 apt 的 404 而失败 | Debian 11 的 LTS 结束，`bullseye-security` 从 deb.debian.org 消失了。steamdev `adc1343` 之后的 Dockerfile 已重新指向 archive.debian.org |
| 在主机上以 Wayland 启动时 SDL 初始化发生 segfault | 画面 ( 合成器 ) 处于睡眠状态。这不是构建的问题，请让画面恢复后再执行 |
| 明明已移除的环境变量仍然有效 | Deck 侧的 devkit-utils 在 env 为空时不会删除 `~/devkit-game/<gameid>-env.json`。steamdev `e39d1d9` 之后的 `deploy` 在 env 为空时会删除 ( 用旧 steamdev 注册的 title 会在重新部署时消失 ) |
| deploy 因 `invalid gameid` 失败 | gameid 只能是英数字、`_`、`.` ( 不可用连字符 ) |
| 找不到存档数据 | 从 2026-10 起，Linux 版的默认保存位置是 `~/.local/share/<orgname>/<appname>/` ( Deck 的话是 `/home/deck/.local/share/…` )。`deckproject.toml` 的构成没有 `.cf`，因此是 `wamsoft/krkrz` |

### 使用 `-replweb` 时的注意 ( 2026-09-06 起 )

`-replwebidle` **默认变为启用 ( 5 秒 )**。如果保持默认，**用浏览器
打开 `http://127.0.0.1:18899/` 再关闭的时刻，Deck 上的应用也会退出**
( 因为一旦有过连接就会武装，只用 curl 确认不会退出 )。

实机确认会反复“查看、关闭、再查看”，因此 `deckproject.toml` 的启动
命令中**加入了 `-replwebidle=no`**。只有在希望关闭浏览器就
结束的用法下才去掉它。

---

## 4. 已确认的实绩

2026-09-06 已把本步骤完整实测 ( SteamOS 3.8.16 / Deck 实机 )。

- 在 sniper 容器中 Linux 构建成功，GLIBC ≤ 2.30 / 无 GLIBCXX 依赖
- 183 个文件 stage → 传输 → 启动，用截图确认了演示启动器的显示
- 经由隧道 `/state` `/watch` `/pad/exec` `/` ( 浏览器 UI ) 全部有响应
- 善后清理也已完成

2026-10-06 又从 Linux 主机 ( 无 WSL ) 重新确认 ( SteamOS 3.8.16 )。

- sniper 构建: GLIBC ≤ 2.30 ( 插件也 ≤ 2.31 ) / 无 GLIBCXX 依赖
- 用 `-demotest -demotestcap` 全部 24 个场景 ok
- 用 `/proc/<pid>/maps` 确认了随附 SDL3 ( 3.4.0 ) 通过 RPATH 被读取
  ( 支持 RPATH 之前读到的是 SteamOS 的 `/usr/lib/libSDL3.so.0` ( 3.2.18 ) )
- krkrz_linux 的示例项目包 ( `krkrz-sample` ) 也同样全部 24 个场景 ok。
  保存位置与 `.cf` 的 `orgname` / `appname` 一致，为 `/home/deck/.local/share/wamsoft/krkrz-sample/`

## 相关

- [REPL ( 交互式 TJS shell )](repl.md) — `-replweb` 的 HTTP API 与浏览器 UI
- [LinuxBuild.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LinuxBuild.md)
  — sniper 构建环境的内容与合格标准 ( engine 侧 SSOT )
- [Linux 版发布包 ( krkrz_linux )](linux_package.md) — 把作品整理为发布用
- umbrella 根目录的 `deckproject.toml` — 构建 / 素材 / 启动的定义
