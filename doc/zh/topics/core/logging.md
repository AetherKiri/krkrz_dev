# 日志输出

吉里吉里Z 会将运行中的动作日志输出到控制台 / 文件。
输出级别与格式可以通过多种途径控制。

详细规格与设计请参照 src/core 侧的指南：

- [doc/Logging.md](https://github.com/wamsoft/krkrz_develop/blob/master/doc/Logging.md)

---

## 日志级别

吉里吉里Z 具有以下 5 个阶段的日志级别 ( 越靠上重要度越高 )。

- `error` — 错误
- `warning` — 警告 ( `TVPAddImportantLog` )
- `info` — 常规日志 ( `TVPAddLog` )
- `debug` — 调试信息
- `off` — 全部抑制

构建时的默认值如下：

| 构建 | 默认级别 |
|---|---|
| `MASTER` | `warning` |
| Release ( 非 MASTER ) | `info` |
| Debug | `debug` |

想在运行时覆盖时，请使用启动选项
[`-loglevel=<level>`](../../guide/CommandLine.md)。
在发布用二进制中临时采集详细日志时很方便。

```
krkrz64 -loglevel=debug data/
```

---

## 相关选项

| 选项 | 功能 |
|---|---|
| `-loglevel=<level>` | 动态指定日志级别 |
| `-debug=yes` | 调试模式 ( 启用调试辅助功能 ) |
| `-forcelog=yes` | 将控制台日志始终输出到文件 |
| `-logerror=yes` | 将出错时的日志输出到文件 |
| `-memstatinterval=N` | 定期输出内存统计日志 |
| `-memstatonexit=1` | 退出时输出统计日志 |
| `-cachelistonexit=<mode>` | 退出时输出 cache 列表日志 |
