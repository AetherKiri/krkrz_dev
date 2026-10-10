# DrawThreadPool 利用率的测量 (DrawStats)

吉里吉里Z 的绘制在内部会经过 **DrawThreadPool** ( `TVPBeginThreadTask` /
`TVPExecThreadTask` / `TVPEndThreadTask` ) 这一并行线程池来执行。在
`KRKRZ_DRAW_STATS=ON` 构建中，其利用率通过原子计数器采集，可以从画面
覆盖层与日志中观察。

主要用途是 **定位“只有主 CPU 拥堵、其他核心空闲”现象的原因**。
这是一套装备，用于仅凭外部观察就排查在 Switch 等嵌入式环境中典型出现的
这一状况。

详细的使用方法与阅读方法汇总在 src/core 侧的指南中：

- [doc/DrawStats.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/DrawStats.md)

---

## 构建

通过 CMake 选项切换 OFF/ON。**默认 OFF ( 不影响产品构建 )**。

```bash
cmake --preset x64-windows -DKRKRZ_DRAW_STATS=ON
cmake --build build/x64-windows --config Release
```

OFF 时测量宏会展开为空，完全不会生成原子操作。

### 阈值调优

可以在构建时覆盖 `GetAdaptiveThreadNum` 的阈值判定
`pixelNum >= factor * SCALE` 中的 **SCALE**。

```bash
# 旧 PC 挙動 (1T 多め) で動かしたい場合
cmake --preset x64-windows -DKRKRZ_THREAD_PIXEL_SCALE=500
```

- **默认 100** ( 根据 Switch 实机上的比较决定 )
- 500 (旧规格) 时，在 Switch 上 1T 利用率占主导，工作线程得不到有效利用

---

## 显示与阅读方法

启用 [`-memoverlay=1`](../../guide/CommandLine.md) 后，DrawStats 会同时显示在
画面右上角。

在实机等环境中画面显示变化太快、无法看清时，可以用
[System.setDrawStatsLog](../../reference/System.md#setdrawstatslog) 切换为
500ms 周期的日志输出 ( 在 OFF 构建或 MemoryOverlay 未显示时，不会有实际
影响，什么也不会发生 )。

---

## 相关 API

- [System.setDrawStatsLog](../../reference/System.md#setdrawstatslog) — DrawStats 日志输出的动态切换
- [System.setMemoryOverlay](../../reference/System.md#setmemoryoverlay) — 同时显示的 MemoryOverlay 切换
- [System.drawThreadNum](../../reference/System.md#drawthreadnum) — 绘制线程数的获取、设置
