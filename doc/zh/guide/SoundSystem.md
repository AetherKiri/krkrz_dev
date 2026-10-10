# 声音系统

## 关于声音系统

吉里吉里的声音系统可以播放 Wave (PCM)。

Wave 播放可以同时播放多个，除了能够进行流式播放 (一边一点一点读取较长的声音一边播放) 之外，还可以使用声音循环信息文件 (.sli 文件) 实现感觉不到接缝的无缝循环播放 (声音循环信息文件用循环调谐器制作)。

## WaveSoundBuffer 可播放的格式

[WaveSoundBuffer](../reference/WaveSoundBuffer.md) 标准情况下可以播放无压缩的 RIFF Wave 格式 (扩展名为 .wav，Windows 标准格式)。可接受的格式如下。

- WAVE_FORMAT_PCM 格式，8bit 以上 32bit 以下的整数 PCM，且声道数为 1(单声道)、2(立体声)、4(quadraphonic)、6(5.1ch) 的
- WAVE_FORMAT_IEEE_FLOAT 格式，32bit 的浮点数 PCM，且声道数为 1(单声道)、2(立体声)、4(quadraphonic)、6(5.1ch) 的
- WAVE_FORMAT_EXTENSIBLE 格式，子类型为 KSDATAFORMAT_SUBTYPE_PCM 格式的 8bit 以上 32bit 以下的整数 PCM
- WAVE_FORMAT_EXTENSIBLE 格式，子类型为 KSDATAFORMAT_SUBTYPE_IEEE_FLOAT 格式的 32bit 浮点数 PCM

WaveSoundBuffer 可播放的格式可以通过插件扩展。

## WaveSoundBuffer 对 4ch 和 6ch 的处理

WAVE_FORMAT_EXTENSIBLE 在数据中包含“哪个声道被分配给了哪个扬声器”的信息，而 WAVE_FORMAT_PCM 和 WAVE_FORMAT_IEEE_FLOAT 的情况下则没有该信息。吉里吉里处理 WAVE_FORMAT_PCM 和 WAVE_FORMAT_IEEE_FLOAT 的 4ch 和 6ch 数据时，按如下方式解释。

- **4ch 时**  
  从声道开头起，分别被视为前左、前右、后左、后右的扬声器用数据
- **6ch 时**  
  从声道开头起，分别被视为前左、前中、前右、后左、后右、低频的扬声器用数据

另外，用 OggVorbis 播放 4ch 和 6ch 的声音时也适用同样的规则。
