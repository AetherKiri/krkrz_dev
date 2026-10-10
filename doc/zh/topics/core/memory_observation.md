# 内存观测与泄漏调查

吉里吉里Z 的引擎中内置了一套机制，用于实时观察内存使用量与分配器的明细。本页是汇总其**入口**的指南。设计上的细节与依据请参照 src/core 侧的开发者文档。

- 详细指南：[doc/MemoryGuide.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/MemoryGuide.md)
- 设计与实现依据：[doc/MemoryDesign.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/MemoryDesign.md)
- 泄漏审计的运用：[doc/LeakAudit.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/LeakAudit.md)

---

## 分配器的构成

引擎内的内存按用途分为 4 个系统 + 外部进行测量。

| 分配器 | 主要用途 |
|---|---|
| **FileAllocator** | StorageCache (file 层缓存) 的二进制 |
| **BitmapAllocator** | `Bitmap` 的 bits 区域 |
| **SoundAllocator** | PCM / 环形缓冲区 / DSP 的工作区域 |
| **GlobalAlloc[Krkrz]** | 经由 `operator new` / `TJS_malloc` 的分配 (TLSF 池) |
| **GlobalAlloc[SDL]** | SDL3 内部的分配 (仅 `KRKRZ_SDLMEMORY_STAT=ON` 构建时) |
| 外部 | ANGLE / miniaudio / opus / libpng 等 C 库内部的 malloc、GL texture、直接 HeapAlloc |

`GlobalAlloc[Krkrz]` 还会按线程局部的 **标签** 分别汇总明细 ( `TJS2` / `GraphicsLoader` / `User` / `Unknown` )。

---

## 从 TJS2 观察

[System](../../reference/System.md) 类中有观测 API。

- [System.getSystemAllocatorInfo](../../reference/System.md#getsystemallocatorinfo) — 获取包含进程 RSS / VSize、系统空闲内存的字典。
- [System.resetMemoryPeak](../../reference/System.md#resetmemorypeak) — 将 peak 测量值重新对齐为当前值。
- [System.beginAllocTag](../../reference/System.md#beginalloctag) / [System.endAllocTag](../../reference/System.md#endalloctag) — 按标签分离测量源自脚本的分配。
- [System.setMemoryOverlay](../../reference/System.md#setmemoryoverlay) — 画面覆盖层的动态切换。

文件缓存 ( file 层 ) 与图像解码缓存 ( decode 层 ) 的观测 API 位于 [Storages](../../reference/Storages.md) 侧。

- [Storages.getFileCacheList](../../reference/Storages.md#getfilecachelist) / [Storages.getImageCacheList](../../reference/Storages.md#getimagecachelist) — 以字典数组获取条目列表
- [Storages.dumpFileCacheList](../../reference/Storages.md#dumpfilecachelist) / [Storages.dumpImageCacheList](../../reference/Storages.md#dumpimagecachelist) — 以 WARNING 级别转储到日志
- [Storages.pinCache](../../reference/Storages.md#pincache) / [Storages.unpinCache](../../reference/Storages.md#unpincache) / [Storages.isCachePinned](../../reference/Storages.md#iscachepinned) — 以条目为单位的 pin 管理
- [Storages.clearTransientCaches](../../reference/Storages.md#cleartransientcaches) / [Storages.clearAllCaches](../../reference/Storages.md#clearallcaches) — 批量清除

---

## 启动选项

新增了用于内存调查的启动选项 ( 详细：[命令行选项](../../guide/CommandLine.md) )。

| 选项 | 功能 |
|---|---|
| `-memoverlay=1` | 从启动时起在画面右上角以覆盖层显示内存状态 ( 绘制为 OGL 系 / SDL 的 DrawDevice。WINVER 默认的 D3D11 下不显示 ) |
| `-memstatinterval=N` | 每 N 秒将内存统计输出到日志 |
| `-memstatonexit=1` | 退出时将内存统计输出到日志 1 次 |
| `-cachelistonexit=<mode>` | 退出时转储 Storages cache 列表 ( `1`/`all`/`file`/`image`/`0`/`none` ) |

在 `KRKRZ_ENABLE_PERIODIC_DUMP=OFF` 构建中，周期转储类 ( `memstat*`/`cachelistonexit` ) 会被忽略。

---

## 从 REPL 观察

在启用了 [REPL](repl.md) 的构建中，可以从交互式 shell 直接窥视内存状态 ( `.mem` / `.memdump` / `.memoverlay` / `.mempeakclear` / `.sysalloc` / `.filecache` / `.imagecache` 等 )。

---

## 调查是什么占用了内存 ( 诊断构建 )

当 `GlobalAlloc[Krkrz]` 的 live 大到无法用 TJS 对象的数量解释时，使用 `KRKRZ_ENABLE_MEMSTAT_DETAIL=ON` 的诊断构建来调查明细。该功能不会进入产品构建 ( 仅 Windows )。

`.memdump` 的输出中会追加以下项目。

| 项目 | 内容 |
|---|---|
| `live by size` | 存活的分配按大小区分的数量与字节数 ( 以半倍频程为步长 ) |
| `member tables` / `per-class member table bytes` | TJS 对象的成员表 ( 哈希表的槽数组与链节点 ) 的合计以及按类的大小 |
| `string heap` | TJS 字符串堆的块数、填充率、相同内容字符串的重复 |

此外，如果加上启动选项 `-memstatsite=<段数>` ( `yes` 时为 16 段 )，会为每次分配采集栈，并按**调用方**统计存活字节数与数量。
在 `.memdump` 的末尾以及 REPL 的 `.memsites [件数] [関数名の一部]` 中，会跳过分配器内部，按第一个函数、按调用链从多到少列出。
有 PDB 的模块显示函数名与源码行，没有 PDB 的插件 DLL 则附带模块名显示。

- 由于每次分配都要采集栈，启动与处理会变得相当慢。
- 诊断构建会将分配头从 16 byte 扩大到 32 byte 以持有分配点编号，因此进程整体的内存量无法与产品构建比较 ( `GlobalAlloc[Krkrz]` 的 live 是请求大小的合计，所以可以比较 )。
- 日志会输出到控制台日志 ( `-forcelog=yes` )。
