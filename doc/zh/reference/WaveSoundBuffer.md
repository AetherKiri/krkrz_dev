# WaveSoundBuffer

WaveSoundBuffer 类是管理 PCM 播放的类。

WaveSoundBuffer 类可以读取并处理用 [循环调谐器](../guide/LoopTuner.md) 创建的 .sli 文件。详情请参阅循环调谐器的说明。

## 成员列表

### 构造函数

- [WaveSoundBuffer](#wavesoundbuffer)

### 属性

- [position](#position)
- [paused](#paused)
- [totalTime](#totaltime)
- [looping](#looping)
- [volume](#volume)
- [volume2](#volume2)
- [status](#status)
- [bits](#bits)
- [channels](#channels)
- [filters](#filters)
- [flags](#flags)
- [frequency](#frequency)
- [globalFocusMode](#globalfocusmode)
- [globalVolume](#globalvolume)
- [labels](#labels)
- [pan](#pan)
- [posX](#posx)
- [posY](#posy)
- [posZ](#posz)
- [samplePosition](#sampleposition)
- [useVisBuffer](#usevisbuffer)
- [use3D](#use3d)
- [minDistance](#mindistance)
- [maxDistance](#maxdistance)
- [rolloffFactor](#rollofffactor)
- [dopplerFactor](#dopplerfactor)
- [attenuationModel](#attenuationmodel)

### 方法

- [open](#open)
- [play](#play)
- [stop](#stop)
- [fade](#fade)
- [stopFade](#stopfade)
- [freeDirectSound](#freedirectsound)
- [getVisBuffer](#getvisbuffer)
- [getSoundLevel](#getsoundlevel)
- [getSoundSpectrum](#getsoundspectrum)
- [getVowel](#getvowel)
- [setPos](#setpos)
- [set3DPosition](#set3dposition)
- [set3DVelocity](#set3dvelocity)
- [set3DConeDirection](#set3dconedirection)
- [set3DCone](#set3dcone)
- [setGainQueryCallback](#setgainquerycallback)

### 事件

- [onStatusChanged](#onstatuschanged)
- [onFadeCompleted](#onfadecompleted)
- [onLabel](#onlabel)

---

### WaveSoundBuffer

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `owner` | `&nbsp;` | 指定事件的产生目标。 |

**说明**

构建 WaveSoundBuffer 对象

构建 WaveSoundBuffer 类的对象。

事件发生时，会调用由 owner 指定的对象的 action 方法。将 owner 指定为 null 时，不会调用 action 方法。通常将 [Window](Window.md) 类的对象指定为 owner。

---

### position

属性 \ 访问: `r/w`

**说明**

播放位置

以 ms 为单位表示播放位置。设置值后会移动到该位置。

---

### paused

属性 \ 访问: `r/w`

**说明**

是否处于暂停状态

表示是否处于暂停状态。也可以设置值。

为真时表示处于暂停状态。

---

### totalTime

属性 \ 访问: `r`

**说明**

媒体的播放时间

以 ms 为单位表示媒体的总播放时间。

---

### looping

属性 \ 访问: `r/w`

**说明**

是否进行循环播放

表示是否进行循环播放。也可以设置值。

指定为真时进行循环播放。

即使指定为假，只要正在播放的媒体带有循环信息，也会使用该循环信息。

---

### volume

属性 \ 访问: `r/w`

**说明**

音量

表示播放音量。也可以设置值。

用 0 ~ 100000 的数值指定，0 为完全静音，100000 为 100% 音量。

---

### volume2

属性 \ 访问: `r/w`

**说明**

第二音量

表示播放音量。可以设置值。

与 [WaveSoundBuffer.volume](WaveSoundBuffer.md#volume) 属性不同的是，该属性不会因 [WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) 方法而变化。

最终音量由 volume 属性与该属性的乘积决定。volume 属性为 100000 (100%)、volume2 属性也为 100000 (100%) 时，100% × 100% = 100%，以 100% 的音量播放。volume 属性为 50000 (50%)、volume2 属性为 75000 (75%) 时，50% × 75% = 37.5%，以 37.5% 的音量播放。

---

### status

属性 \ 访问: `r`

**说明**

状态

表示当前状态。

状态用字符串表示，取以下值。

`"**unload**"   : ` 媒体尚未打开

`"**play**"     : ` 媒体正在播放

`"**stop**"     : ` 媒体已停止

---

### bits

属性 \ 访问: `r`

**说明**

量化位数

表示当前正在播放的声音的量化位数。
与 CD 相同的量化位数时为 16。
媒体未打开的状态下可能无法返回正常值。

---

### channels

属性 \ 访问: `r`

**说明**

声道数

表示当前正在播放的声音的声道数。
单声道时为 1，立体声时为 2。
媒体未打开的状态下可能无法返回正常值。

---

### filters

属性 \ 访问: `r`

**说明**

滤波器数组

是持有插入式滤波器对象的数组 (Array 类的实例)。
通过向该数组注册滤波器对象，可以在播放中对音频实时施加各种效果。
对滤波器数组的更改只有在执行 WaveSoundBuffer.open 方法时才会被反映。
在此之前，即使对该数组进行更改也不会被反映。
例:
```
var buf = new WaveSoundBuffer(window);
(略)
buf.filters.clear();
// フィルタ配列をクリア
buf.filters.add(new WaveSoundBuffer.PhaseVocoder());
// PhaseVocoderフィルタを追加
buf.filters[0].time = 0.5;
// 倍速再生
```

---

### flags

属性 \ 访问: `r`

**说明**

标志

可以获得表示标志的对象。
该对象拥有 0 ~ 15 的属性，分别表示各标志的值。
可以使用间接成员选择运算符 ('[ ]' 运算符) 访问这些属性。
也可以为这些属性设置值。
值的范围是 0 ~ 9999，不能低于或高于该范围。
该对象的 count 属性总是返回 16。
该对象拥有 reset 方法，执行该方法后，所有标志都会被重置为 0。
未打开媒体时，即使为该对象的属性设置值也会被忽略。
该对象乍看之下也像是数组对象，但不是所谓的 TJS 数组对象 ('Array' 类的对象)。
标志会在 WaveSoundBuffer.open 方法中被全部重置为 0。
例:

```
var buf = new WaveSoundBuffer(window);
(略)
buf.flags.reset();
// 全てのフラグを 0 にリセット
var cnt = buf.flags.count;
// cnt には 16 が入る
buf.flags[4] = 34;
// 4番のフラグに34を代入
```

---

### frequency

属性 \ 访问: `r/w`

**说明**

采样频率

表示当前正在播放的声音的采样频率。
也可以设置值。
与 CD 相同的采样频率时为 44100。
媒体未打开的状态下可能无法返回正常值。
设置值后，会以该频率播放。

---

### globalFocusMode

属性 \ 访问: `r/w`

**说明**

焦点模式

表示焦点模式。
也可以设置值。
焦点模式是让应用程序在最小化或变为非活动状态时静音的模式。

+ 指定 sgfmNeverMute 时，应用程序无论处于何种状态都不会静音。
+ 指定 sgfmMuteOnMinimize 时，应用程序在最小化时静音。
+ 指定 sgfmMuteOnDeactivate 时，应用程序在变为非活动状态时静音。

该属性只存在于 WaveSoundBuffer 类上 (在由 WaveSoundBuffer 创建的对象上不存在该属性)。
使用时请写作 WaveSoundBuffer.globalFocusMode。

---

### globalVolume

属性 \ 访问: `r/w`

**说明**

全局音量

表示全局音量 (主音量)。
也可以设置值。
该音量会影响所有 WaveSoundBuffer。
用 0 ~ 100000 的数值指定，0 为完全静音，100000 为 100% 音量。
默认值是 100000。
该属性只存在于 WaveSoundBuffer 类上 (在由 WaveSoundBuffer 创建的对象上不存在该属性)。
使用时请写作 WaveSoundBuffer.globalVolume。

---

### labels

属性 \ 访问: `r`

**说明**

标签

可以获得表示标签的对象。
该对象是字典数组，其中包含以循环信息中的标签名为成员名的元素。
每个元素也是字典数组，name 成员表示标签名，position 成员表示以毫秒为单位的标签位置，samplePosition 表示以采样数为单位的标签位置。
请认为该字典数组是只读的。
即使赋值或创建新成员，也不会被反映。
例:

```
var buf = new WaveSoundBuffer(window);
(略)
debug.message(buf.labels['start'].position);
// 'start' というラベル名の位置をミリ秒単位で
debug.message(buf.labels['start'].samplePosition);
// 'start' というラベル名の位置をサンプル数単位で
```

---

### pan

属性 \ 访问: `r/w`

**说明**

声像

表示声像 (音频平衡)。
也可以设置值。
可以指定声音能听到的左右位置。
用 -100000 ~ 0 ~ 100000 的数值指定，-100000 为完全左，0 为中央，100000 为完全右。

---

### posX

属性 \ 访问: `r/w`

**类型**: `Real`

**说明**

3D 音源位置 (X 坐标)

获取 / 设置 3D 声音播放时音源位置的 X 坐标。
也可以用 `WaveSoundBuffer.setPos` 一次性设置 3 个轴。

**相关:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### posY

属性 \ 访问: `r/w`

**类型**: `Real`

**说明**

3D 音源位置 (Y 坐标)

获取 / 设置 3D 声音播放时音源位置的 Y 坐标。

**相关:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### posZ

属性 \ 访问: `r/w`

**类型**: `Real`

**说明**

3D 音源位置 (Z 坐标)

获取 / 设置 3D 声音播放时音源位置的 Z 坐标。

**相关:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### samplePosition

属性 \ 访问: `r/w`

**说明**

播放位置

以采样数单位表示播放位置。
设置值后会移动到该位置。

---

### useVisBuffer

属性 \ 访问: `r/w`

**说明**

是否使用可视化用缓冲区

表示是否使用可视化用缓冲区。
也可以设置值。
指定为真后可视化用缓冲区变为可用，WaveSoundBuffer.getVisBuffer 方法也随之可用。
默认为假。
请注意，指定为真时会比指定为假消耗更多的内存和 CPU 时间。

---

### use3D

属性 \ 访问: `r/w`

**说明**

3D 定位 (spatializer) 的启用/禁用

表示是否为该 WaveSoundBuffer 启用基于 miniaudio 的 3D 定位 (距离衰减、声像、多普勒、指向性锥体)。
启用时用 [set3DPosition](#set3dposition) 等赋予音源位置。

---

### minDistance

属性 \ 访问: `r/w`

**说明**

最小距离

在该距离以内不会发生距离衰减 (音量为最大)。

**相关:** [WaveSoundBuffer.maxDistance](WaveSoundBuffer.md#maxdistance)

---

### maxDistance

属性 \ 访问: `r/w`

**说明**

最大距离

超过该距离后，距离衰减达到上限。

**相关:** [WaveSoundBuffer.minDistance](WaveSoundBuffer.md#mindistance)

---

### rolloffFactor

属性 \ 访问: `r/w`

**说明**

距离衰减的强度

表示距离衰减的强度 (滚降系数)。越大衰减越急剧。

---

### dopplerFactor

属性 \ 访问: `r/w`

**说明**

多普勒效应的强度

表示多普勒效应的强度 (0 为无效，1 为标准)。

**相关:** [WaveSoundBuffer.set3DVelocity](WaveSoundBuffer.md#set3dvelocity)

---

### attenuationModel

属性 \ 访问: `r/w`

**说明**

距离衰减模型

表示距离衰减模型的整数。对应 0 = 无、1 = 倒数平方 (inverse)、2 = 线性 (linear)、3 = 指数 (exponential)。

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 指定想要播放的存储。 |

**说明**

打开媒体

打开指定的媒体。该方法不会开始播放。

如果存在在指定存储名后附加 .sli 的文件名，则将其作为声音循环信息读取。

---

### play

方法

**说明**

播放媒体

开始播放媒体。

---

### stop

方法

**说明**

停止媒体

停止媒体。

---

### fade

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `to` | `&nbsp;` | 指定要达到的音量。<br>关于音量的指定，请参阅<br>[WaveSoundBuffer.volume](WaveSoundBuffer.md#volume) 属性。 |
| `time` | `&nbsp;` | 指定淡化所需的时间，单位为 ms。 |
| `delay` | `0` | 指定开始淡化之前的等待时间，单位为 ms。 |

**说明**

开始淡化

开始淡化 (连续的音量变化)。

---

### stopFade

方法

**说明**

停止淡化

强制停止用 [WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) 方法开始的淡化。

音量保持为停止时的值。

---

### freeDirectSound

方法

**说明**

DirectSound 的释放 (兼容用，不执行任何操作)

这是为旧 DirectSound 实现准备的方法。
当前吉里吉里Z 的音频输出使用 miniaudio (WASAPI 共享模式)，不使用 DirectSound，因此即使调用该方法也不会执行任何操作。
仅为与过去的脚本保持兼容而保留。
该方法只存在于 WaveSoundBuffer 类上 (在由 WaveSoundBuffer 创建的对象上不存在该方法)。
使用时请写作 WaveSoundBuffer.freeDirectSound();。

---

### getVisBuffer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `buffer` | `&nbsp;` | 指定用于写入输出数据的缓冲区。<br>缓冲区是 16bit 有符号整数的数组，其元素个数需要足够写入由 numsamples 参数和 channels 参数指定的采样 (numsamples * channels 以上)。<br>当 channels 指定为 1 以外的值时，各声道的采样会被交错存储 (立体声时按 右 左 右 左 …… 的顺序)。<br>需要指定指向数组首个元素的指针，但请将其强制转换为整数类型后再传入。 |
| `numsamples` | `&nbsp;` | 指定要获取的采样数。 |
| `channel` | `&nbsp;` | 指定要获取的声道数。<br>指定 1 时，若为单声道则直接获得原数据，否则可获得下混为 1 声道的数据。<br>指定 1 以外的数值时，需要指定与正在播放的声音相同的声道数。<br>这种情况下可以获得原样的数据。 |
| `ahead` | `0` | 指定要预读的采样数。<br>可以从距当前播放位置由该参数指定的采样数之处开始获取。<br>指定 0 或省略该参数时，从当前播放位置获取。 |

**返回值**

返回成功获取的采样数。

**说明**

获取可视化用数据

为可视化获取 PCM 数据。
从当前播放位置读取 PCM 数据，并写入 buffer 参数指定的数组。
不过，根据缓冲区的状态或播放格式，也有可能无法正常读取数据。
该方法设想由用 C 或 C++ 等编写的插件使用，因此不能进行例如给 buffer 参数指定 TJS 数组之类的操作。
使用该方法需要将 WaveSoundBuffer.useVisBuffer 属性指定为真。

---

### getSoundLevel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ahead` | `0` | 指定要预读的采样数 (默认 0 = 当前播放位置)。<br>用于希望配合绘制延迟前后调整唇形同步的场合。 |
| `windowSamples` | `0` | 指定用于计算音量的窗口采样数 (默认 0 = 引擎默认值)。 |

**返回值**

返回 `%[ rms:実効値, peak:ピーク値 ]` 字典。两者均为 0.0 ~ 1.0，
`rms` 可以直接用作嘴部张合量。

**说明**

音量电平的获取 (唇形同步用)

获取当前播放位置附近的音量。无需像 `getVisBuffer` 那样取出原始
PCM 并在 TJS 侧计算，引擎会在 C++ 侧计算并返回。
使用前需要将 `WaveSoundBuffer.useVisBuffer` 设为真 (未设置时
会自动启用，该次返回 0)。

**相关:** [WaveSoundBuffer.getVowel](WaveSoundBuffer.md#getvowel) / [WaveSoundBuffer.getSoundSpectrum](WaveSoundBuffer.md#getsoundspectrum)

---

### getSoundSpectrum

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `numbands` | `&nbsp;` | 指定要获取的频段数 (1 ~ 256)。 |
| `ahead` | `0` | 指定要预读的采样数 (默认 0)。 |

**返回值**

返回存放各频段能量的数组 (元素数为 numbands)。
各频段按对数方式排列 (从低频到高频)。

**说明**

频谱的获取 (唇形同步用)

用 FFT 解析当前播放位置附近的频谱，并作为对数排列的
频段能量返回。可用于元音判定或均衡器显示等。
需要将 `WaveSoundBuffer.useVisBuffer` 设为真。

**相关:** [WaveSoundBuffer.getVowel](WaveSoundBuffer.md#getvowel)

---

### getVowel

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `ahead` | `0` | 指定要预读的采样数 (默认 0)。 |

**返回值**

返回 `%[ a:, i:, u:, e:, o:, voiced: ]` 字典。a~o 为各元音的
推定权重 (总和约为 1.0)，`voiced` 为有声 (元音频段有能量) 时返回 1，
无声时为 0。

**说明**

元音推定的获取 (唇形同步用)

解析当前播放位置附近的频谱，根据共振峰频段的能量比，推定并返回
日语 5 个元音 (a、i、u、e、o) 的相似程度。可以用作口型
(viseme) 的混合权重。请注意这只是简易推定。
需要将 `WaveSoundBuffer.useVisBuffer` 设为真。

**相关:** [WaveSoundBuffer.getSoundLevel](WaveSoundBuffer.md#getsoundlevel)

---

### setPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定 X 坐标。 |
| `y` | `&nbsp;` | 指定 Y 坐标。 |
| `z` | `&nbsp;` | 指定 Z 坐标。 |

**说明**

3D 音源位置的批量设置

一次性设置 3D 声音播放时的音源位置 (X / Y / Z)。

**相关:** [WaveSoundBuffer.posX](WaveSoundBuffer.md#posx) / [WaveSoundBuffer.posY](WaveSoundBuffer.md#posy) / [WaveSoundBuffer.posZ](WaveSoundBuffer.md#posz)

---

### set3DPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | X 坐标。 |
| `y` | `&nbsp;` | Y 坐标。 |
| `z` | `&nbsp;` | Z 坐标。 |

**说明**

设置 3D 音源位置

设置 3D 定位的音源位置 (在 [use3D](#use3d) 有效时起作用)。

**相关:** [WaveSoundBuffer.setPos](WaveSoundBuffer.md#setpos)

---

### set3DVelocity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `vx` | `&nbsp;` | X 方向的速度。 |
| `vy` | `&nbsp;` | Y 方向的速度。 |
| `vz` | `&nbsp;` | Z 方向的速度。 |

**说明**

设置 3D 音源的速度矢量

设置用于多普勒计算的音源速度矢量。

**相关:** [WaveSoundBuffer.dopplerFactor](WaveSoundBuffer.md#dopplerfactor)

---

### set3DConeDirection

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `dx` | `&nbsp;` | 朝向的 X 分量。 |
| `dy` | `&nbsp;` | 朝向的 Y 分量。 |
| `dz` | `&nbsp;` | 朝向的 Z 分量。 |

**说明**

设置指向性锥体的朝向

设置指向性锥体 ([set3DCone](#set3dcone)) 的朝向矢量。

---

### set3DCone

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `innerAngleRad` | `&nbsp;` | 内侧锥体的总角度 (弧度)。在该内侧不会衰减。 |
| `outerAngleRad` | `&nbsp;` | 外侧锥体的总角度 (弧度)。 |
| `outerGain` | `&nbsp;` | 外侧的衰减增益 (0.0 ~ 1.0)。 |

**说明**

设置指向性锥体

设置音源的指向性锥体。角度以弧度为单位，在锥体外部会衰减到 outerGain
的增益。希望变为全方位 (无指向) 时，设为 inner = outer = 2*PI。

**相关:** [WaveSoundBuffer.set3DConeDirection](WaveSoundBuffer.md#set3dconedirection)

---

### setGainQueryCallback

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | 指定接收 URL (存储名) 作为 1 个参数、并返回要应用的<br>附加增益 (dB) 的函数。指定 null 时解除。 |

**说明**

按曲目获取增益的回调设置 (类方法)

注册解码 ogg (Vorbis) / opus 文件时返回按文件应用的
**附加增益 (dB)** 的回调函数。这是类
方法，注册结果会在所有 WaveSoundBuffer 之间共享。它把旧 wuvorbis /
wuopus 插件的同名 API 整合到了引擎本体内置解码器中。
回调会在打开文件时 (open 时、脚本线程) 被调用 1 次，
其返回值的 dB 会应用到解码输出。可用于让每首曲目的音量一致
(响度归一化) 等用途。

例 :

`WaveSoundBuffer.setGainQueryCallback(function(url) {`

`  return url.indexOf("loud_") != -1 ? -6.0 : 0.0; // 特定曲だけ -6dB`

`});`

增益除此之外，还有通过启动时命令行选项设置的整体增益以及对
ReplayGain 标签的支持 (参见 [命令行](../guide/CommandLine.md)
的“声音的增益”)。

**按编解码器的差异 / 推荐**

opus 按规格在头部带有输出增益 (R128)，由解码器内部准确、
低成本地应用 (CLI / 回调的增益也会加算到其上)。而
Vorbis 的格式中没有增益概念，因此引擎本体在 float 域中
缩放输出 PCM 来应用 (实用上的性能差异几乎没有)。**积极
处理增益或响度时，推荐使用 opus。**

---

### onStatusChanged

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `status` | `&nbsp;` | 新的状态。<br>请参阅 [WaveSoundBuffer.status](WaveSoundBuffer.md#status) 属性。 |

**说明**

状态已更改

播放的状态发生变化时发生。

---

### onFadeCompleted

事件

**说明**

淡化已结束

用 [WaveSoundBuffer.fade](WaveSoundBuffer.md#fade) 方法开始的淡化结束时发生。

---

### onLabel

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | 通过的标签名。 |

**说明**

已通过标签

播放位置通过标签时发生。

---

## 插件扩展: getSample

基于伪代码的手册

### 成员列表

#### 属性

- [sampleValue](#samplevalue)
- [sampleCount](#samplecount)
- [sampleAhead](#sampleahead)

#### 方法

- [getSample](#getsample)

---

### sampleValue

属性 \ 访问: `r`

**说明**

采样值的获取 (新方式)

用 getVisBuffer(buf, sampleCount, 1, sampleAhead) 获取采样，
并取得 (value/32768)^2 的最大值。(以 0 ~ 1 的实数返回)
※读取该属性时会隐式地将 useVisBuffer 设为 true

---

### sampleCount

属性 \ 访问: `r/w`

**说明**

新方式的缓冲区获取用参数属性 (参见 sampleValue)

默认值由 setDefaultCounts/setDefaultAheads 决定
※读写该属性时会隐式地将 useVisBuffer 设为 true

---

### sampleAhead

属性 \ 访问: `r/w`

---

### getSample

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `n` | `&nbsp;` | 要获取的采样数。省略时为 100 |

**返回值**

平均值
※ 请预先设置 useVisBuffer=true

**说明**

采样值的获取 (旧方式)

从当前播放位置获取指定数量的采样，并返回其平均值。
值为负的采样值会被忽略。

---
