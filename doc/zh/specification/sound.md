# 音频播放功能

记载吉里吉里Z 支持的音频播放功能。

### 目录

[概要](#overview)

[规格参数](#spec)

[支持的格式](#format)

[无缝循环 (.sli)](#loop)

[3D 定位 (spatializer)](#spatializer)

[唇形同步/解析 API](#analysis)

[时间伸缩/变调](#phasevocoder)

## 概要 { #overview }

现行的吉里吉里Z 在所有构建中把 **miniaudio** 作为单一音频引擎使用 (旧的 DirectSound 实现已被移除)。

- **WINVER** — miniaudio 持有输出设备，直接向设备输出。
- **SDL(GENERIC)** — 让 miniaudio 以设备 I/O 禁用 (no-device) 模式运行并生成 PCM，输出设备由 SDL3 持有。

无论哪个系列，解码、混音、效果、3D 定位等音频处理核心都是共通的。

## 规格参数 { #spec }

| &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- |
| 值 | 量化位数 | 整数: 8bit ~ 32bit<br>浮点数: 32bit |
| 值 | 声道数 | 1ch, 2ch, 4ch, 6ch(5.1ch) |
| 值 | 采样频率 | 取决于源 (44.1kHz / 48kHz 等) |
| 可设置值 | 音量 | 0 ~ 100000<br>0: 完全静音<br>100000: 100% |
| 可设置值 | 音频平衡<br>(声像) | -100000 ~ 0 ~ 100000<br>-100000: 完全左<br>0: 中央<br>100000: 完全右 |
| 可设置值 | 播放位置 | 毫秒、采样编号 |

## 支持的格式 { #format }

WaveSoundBuffer 标准支持的格式如下。

| 格式 | 扩展名 | 备注 |
| --- | --- | --- |
| WAV (RIFF PCM) | .wav | 支持 WAVE_FORMAT_PCM (8~32bit 整数)、WAVE_FORMAT_IEEE_FLOAT (32bit float)、WAVE_FORMAT_EXTENSIBLE (PCM / IEEE_FLOAT 子类型)。 |
| Ogg Vorbis | .ogg | Vorbis 解码。 |
| Opus | .opus | Opus 解码。 |

整数 PCM 不会降低位深度，直接进行播放 (8bit = 无符号 / 16、24、32bit = 有符号。24bit 保持 3 字节打包处理)。WAVE_FORMAT_EXTENSIBLE 中有效位数小于容器宽度时 (如 32bit 容器左对齐存放 24bit 等)，按容器宽度读取。

解码器侧的分配经由 **SoundAllocator** 的 TLSF 池。池大小可用 `-soundpoolsize` 指定，默认是 16MB。

支持的格式可以通过插件扩展。

## 无缝循环 (.sli) { #loop }

通过使用声音循环信息文件 (`.sli` 文件)，可以实现感觉不到接缝的无缝循环播放。包含循环位置指定的 `.sli` 文件用循环调谐器创建。

## 3D 定位 (spatializer) { #spatializer }

具备基于 miniaudio 的 3D 定位功能。

- 启用 `WaveSoundBuffer.use3D` 后，该缓冲区会被当作 3D 音源处理。
- 音源侧用 `set3DPosition` / `set3DVelocity` / `set3DCone` 等设置位置、速度、指向性。
- 听者侧用 `SoundListener` 控制位置、朝向、速度等。

距离衰减模型可以从以下 4 种中选择。

| 模型 | 说明 |
| --- | --- |
| amNone | 无距离衰减 |
| amInverse | 倒数衰减 |
| amLinear | 线性衰减 |
| amExponential | 指数衰减 |

另外，不支持 HRTF，因此无法区分前后。

## 唇形同步/解析 API { #analysis }

具备用于解析正在播放的音频的 API。可用于唇形同步与音频可视化。

| API | 内容 |
| --- | --- |
| getSoundLevel | 获取 RMS / 峰值的音量电平。 |
| getSoundSpectrum | 获取各频段的频谱。 |
| getVowel | 获取日语 5 个元音的推定权重。 |
| getVisBuffer | 获取播放位置周边的原始 PCM。 |

## 时间伸缩/变调 { #phasevocoder }

支持基于 Phase Vocoder 的时间伸缩 (速度变更) 与变调。通过 `WaveSoundBuffer.filters` 应用。
