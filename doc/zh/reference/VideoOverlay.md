# VideoOverlay

VideoOverlay 类是创建用于显示视频的显示区域的类。也可以显示到吉里吉里的图层上。

视频播放机制 (krmovie) 已集成到引擎本体的可执行文件中，无需另行附带 DLL。
播放不使用 DirectShow，WebM 由 movie-player (libvpx)、MPEG-1 由 pl_mpeg、其他 (WMV/ASF/MP4 等) 由
Media Foundation 解码。MP4/WMV 等 Media Foundation 原生格式默认进行硬件解码
(可通过命令行选项 -mediaengine=no 禁用)。不支持旧的 theora (krdstheora.dll)。

除图层播放外，在通过叠加进行播放时，VideoOverlay 类的显示区域显示在所有图层的最前面，且不能透明显示。

与叠加播放相比，图层播放时处理器负载往往更高。

在 SDL 版及其他版本 (Windows 原生版以外) 中能播放的只有 WebM 和 MPEG-1。

**播放的结束方式 (图层播放)**: 最终帧也与其他帧一样，
显示相同的时间 (1 帧的时间) 之后，才结束 (onStatusChanged 的 `"stop"`) 或进行循环的倒回 (onPeriod 的 `perLoop`)。
结束后图层上仍会保留最终帧。制作循环动画时，
无需为了接缝而在最后补上与开头相同的画面 (补上会导致开头的画面连续 2 帧)。

## 成员列表

### 构造函数

- [VideoOverlay](#videooverlay)

### 属性

- [position](#position)
- [frame](#frame)
- [loop](#loop)
- [width](#width)
- [height](#height)
- [left](#left)
- [top](#top)
- [visible](#visible)
- [fps](#fps)
- [numberOfFrame](#numberofframe)
- [totalTime](#totaltime)
- [layer1](#layer1)
- [layer2](#layer2)
- [mode](#mode)
- [playRate](#playrate)
- [segmentLoopStartFrame](#segmentloopstartframe)
- [segmentLoopEndFrame](#segmentloopendframe)
- [periodEventFrame](#periodeventframe)
- [audioBalance](#audiobalance)
- [audioVolume](#audiovolume)
- [numberOfAudioStream](#numberofaudiostream)
- [enabledAudioStream](#enabledaudiostream)
- [mixingMovieAlpha](#mixingmoviealpha)
- [mixingMovieBGColor](#mixingmoviebgcolor)
- [contrastRangeMin](#contrastrangemin)
- [contrastRangeMax](#contrastrangemax)
- [contrastDefaultValue](#contrastdefaultvalue)
- [contrastStepSize](#contraststepsize)
- [contrast](#contrast)
- [brightnessRangeMin](#brightnessrangemin)
- [brightnessRangeMax](#brightnessrangemax)
- [brightnessDefaultValue](#brightnessdefaultvalue)
- [brightnessStepSize](#brightnessstepsize)
- [brightness](#brightness)
- [hueRangeMin](#huerangemin)
- [hueRangeMax](#huerangemax)
- [hueDefaultValue](#huedefaultvalue)
- [hueStepSize](#huestepsize)
- [hue](#hue)
- [saturationRangeMin](#saturationrangemin)
- [saturationRangeMax](#saturationrangemax)
- [saturationDefaultValue](#saturationdefaultvalue)
- [saturationStepSize](#saturationstepsize)
- [saturation](#saturation)
- [originalWidth](#originalwidth)
- [originalHeight](#originalheight)
- [enabledVideoStream](#enabledvideostream)
- [numberOfVideoStream](#numberofvideostream)

### 方法

- [open](#open)
- [play](#play)
- [stop](#stop)
- [pause](#pause)
- [rewind](#rewind)
- [prepare](#prepare)
- [setSegmentLoop](#setsegmentloop)
- [cancelSegmentLoop](#cancelsegmentloop)
- [close](#close)
- [setPeriodEvent](#setperiodevent)
- [cancelPeriodEvent](#cancelperiodevent)
- [setPos](#setpos)
- [setSize](#setsize)
- [setBounds](#setbounds)
- [selectAudioStream](#selectaudiostream)
- [setMixingLayer](#setmixinglayer)
- [resetMixingLayer](#resetmixinglayer)

### 事件

- [onStatusChanged](#onstatuschanged)
- [onPeriod](#onperiod)
- [onFrameUpdate](#onframeupdate)
- [onCallbackCommand](#oncallbackcommand)

---

### VideoOverlay

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `window` | `&nbsp;` | 指定将持有该图层的窗口 ( [Window](Window.md) 类的<br>对象 )。 |

**说明**

构建 VideoOverlay 对象

构建 VideoOverlay 类的对象。

---

### position

属性 \ 访问: `r/w`

**说明**

播放位置

以 ms 为单位表示媒体的播放位置。也可以设置值。

以开头帧的位置为 0。

**相关:** [VideoOverlay.frame](VideoOverlay.md#frame) / [VideoOverlay.totalTime](VideoOverlay.md#totaltime)

---

### frame

属性 \ 访问: `r/w`

**说明**

当前帧

以帧为单位表示媒体的播放位置。也可以设置值。

以开头帧为 0。

**相关:** [VideoOverlay.position](VideoOverlay.md#position) / [VideoOverlay.numberOfFrame](VideoOverlay.md#numberofframe)

---

### loop

属性 \ 访问: `r/w`

**说明**

是否进行循环播放

表示是否启用循环播放。也可以设置值。

为真则循环，为假则不循环。

在循环播放中，显示最终帧 1 帧的时间后回到开头，此时发生 onPeriod (`perLoop`)。
循环期间不会发生 onStatusChanged 的 `"stop"`。在 SDL 版及其他版本中也有效。

---

### width

属性 \ 访问: `r/w`

**说明**

播放矩形的宽度

表示播放矩形的宽度。也可以设置值。

该属性在当前版本中，图层播放时不可使用 (尺寸始终与视频的尺寸相同)。

**相关:** [VideoOverlay.height](VideoOverlay.md#height) / [VideoOverlay.setSize](VideoOverlay.md#setsize)

---

### height

属性 \ 访问: `r/w`

**说明**

播放矩形的高度

表示播放矩形的高度。也可以设置值。

该属性在当前版本中，图层播放时不可使用 (尺寸始终与视频的尺寸相同)。

**相关:** [VideoOverlay.width](VideoOverlay.md#width) / [VideoOverlay.setSize](VideoOverlay.md#setsize)

---

### left

属性 \ 访问: `r/w`

**说明**

播放矩形的左端位置

表示播放矩形的左端位置。也可以设置值。

**相关:** [VideoOverlay.top](VideoOverlay.md#top) / [VideoOverlay.setPos](VideoOverlay.md#setpos)

---

### top

属性 \ 访问: `r/w`

**说明**

播放矩形的上端位置

表示播放矩形的上端位置。也可以设置值。

**相关:** [VideoOverlay.left](VideoOverlay.md#left) / [VideoOverlay.setPos](VideoOverlay.md#setpos)

---

### visible

属性 \ 访问: `r/w`

**说明**

是否可见

指定播放区域是否可见。也可以设置值。

为真则可见，为假则不可见。

---

### fps

属性 \ 访问: `r`

**说明**

帧率

表示帧率 (帧/秒)。

对于文件中未记录帧率 (或帧率是小于 1fps 的非法值) 的 WebM，该值为 0，
此时 frame / numberOfFrame 也为 0。

---

### numberOfFrame

属性 \ 访问: `r`

**说明**

全部帧数

表示全部帧数。

---

### totalTime

属性 \ 访问: `r`

**说明**

总时长

以 ms 为单位表示总时长。

---

### layer1

属性 \ 访问: `r/w`

**说明**

绘制图层指定 1

表示图层绘制模式下要绘制的图层。也可以设置值。

通过把 layer1 属性与 layer2 属性设置为不同的图层，可以同时把相同的视频显示到 2 个图层上。

---

### layer2

属性 \ 访问: `r/w`

**说明**

绘制图层指定 2

表示图层绘制模式下要绘制的图层。也可以设置值。

---

### mode

属性 \ 访问: `r/w`

**说明**

播放模式的指定

表示播放方式。请在打开前设置 (打开后的更改无效)。

- **vomOverlay** (默认，叠加): 把视频显示在整个画面的最前面。在 Windows 中
mp4/H.264/HEVC/wmv/asf 等默认使用硬件解码 (Media Foundation 的
IMFMediaEngine)，影像会直接合成到绘制设备 (BasicDrawDevice) 的 Direct3D11 后台
缓冲区。webm/mpeg 为软件解码。在该模式下，
不会进行由 {@link VideoOverlay.setMixingLayer setMixingLayer} 进行的追加图像合成。
- **vomMixer** (混合器): 叠加 + 追加图像合成。不使用硬件解码，
必定走软件合成路径，可以利用 {@link VideoOverlay.setMixingLayer setMixingLayer}
进行的图像合成 (音频也变为内部处理，音量控制可以可靠生效)。
- **vomLayer** (图层绘制): 把视频作为图层 ({@link VideoOverlay.layer1 layer1} /
{@link VideoOverlay.layer2 layer2}) 的图像进行绘制。
- **vomMFEVR**: 旧 Media Foundation + EVR 模式。现在与 vomOverlay 的行为相同
(该值是为了兼容而保留的)。

硬件解码可以通过命令行选项 **-mediaengine=no** 禁用，这种
情况下所有格式都会变为软件解码。

---

### playRate

属性 \ 访问: `r/w`

**说明**

播放速度

设置媒体的播放速度。

指定 1.0 时为通常的播放速度，0.5 为一半的播放速度，2 为 2 倍的播放速度。

可设置的范围取决于解码器 / 编解码器。

参考 : 带音频的视频，大致可以设置从大于 0.0 到 2.0 的值。无音频的视频，可以设置从大于 0.0 起、double 范围内的值，但实际的播放速度上限由处理速度决定。

---

### segmentLoopStartFrame

属性 \ 访问: `r`

**说明**

区间循环的开始帧

区间循环的始端帧。

**相关:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop) / [VideoOverlay.cancelSegmentLoop](VideoOverlay.md#cancelsegmentloop)

---

### segmentLoopEndFrame

属性 \ 访问: `r`

**说明**

区间循环的开始帧

区间循环的始端帧。

**相关:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### periodEventFrame

属性 \ 访问: `r/w`

**说明**

Period 事件帧

引发 Period 事件的帧。

未设置时为负值。

---

### audioBalance

属性 \ 访问: `r/w`

**说明**

音频平衡 (声像)

表示声像 (音像位置)。也可以设置值。

可以指定听到声音的左右位置。

以 -100000 ~ 0 ~ 100000 的数值指定，-100000 为完全左、0 为中央、100000 为完全右。

播放立体声的源时，声像通过衰减左右其中一个声道来实现 (指定 0 时两个声道都会输出，指定 -100000 时只输出左声道)。

---

### audioVolume

属性 \ 访问: `r/w`

**说明**

音频音量

表示播放的音量。也可以设置值。

以 0 ~ 100000 的数值指定，0 为完全静音，100000 为 100% 的音量。

---

### numberOfAudioStream

属性 \ 访问: `r`

**说明**

音频流数量

仅 MPEG 文件可用。
可以获取音频流数量。

**相关:** [VideoOverlay.selectAudioStream](VideoOverlay.md#selectaudiostream) / [VideoOverlay.enabledAudioStream](VideoOverlay.md#enabledaudiostream)

---

### enabledAudioStream

属性 \ 访问: `r`

**说明**

播放目标音频流编号

仅 MPEG 文件可用。
可以获取播放目标的音频流编号。
找不到音频流时返回 -1。

**相关:** [VideoOverlay.selectAudioStream](VideoOverlay.md#selectaudiostream) / [VideoOverlay.numberOfAudioStream](VideoOverlay.md#numberofaudiostream)

---

### mixingMovieAlpha

属性 \ 访问: `r/w`

**说明**

视频的透明度

以 0.0 (完全透明) ~ 1.0 (完全不透明) 的范围表示视频的透明度。

仅在混合模式下可用。

---

### mixingMovieBGColor

属性 \ 访问: `r/w`

**说明**

视频的背景色

表示视频的背景色。

仅在混合模式下可用。

---

### contrastRangeMin

属性 \ 访问: `r`

**说明**

视频的对比度范围最小值

表示对比度范围的最小值。

仅在混合模式下可用。

---

### contrastRangeMax

属性 \ 访问: `r`

**说明**

视频的对比度范围最大值

表示对比度范围的最大值。

仅在混合模式下可用。

---

### contrastDefaultValue

属性 \ 访问: `r`

**说明**

视频的对比度默认值

表示对比度的默认值。

仅在混合模式下可用。

---

### contrastStepSize

属性 \ 访问: `r`

**说明**

视频的对比度增减步进值

表示从 contrastRangeMin 到 contrastRangeMax 的有效增量。

可以按该值为单位更改对比度。

仅在混合模式下可用。

---

### contrast

属性 \ 访问: `r/w`

**说明**

视频的对比度

表示视频的对比度。

仅在混合模式下可用。

---

### brightnessRangeMin

属性 \ 访问: `r`

**说明**

视频的亮度范围最小值

表示亮度范围的最小值。

仅在混合模式下可用。

---

### brightnessRangeMax

属性 \ 访问: `r`

**说明**

视频的亮度范围最大值

表示亮度范围的最大值。

仅在混合模式下可用。

---

### brightnessDefaultValue

属性 \ 访问: `r`

**说明**

视频的亮度默认值

表示亮度的默认值。

仅在混合模式下可用。

---

### brightnessStepSize

属性 \ 访问: `r`

**说明**

视频的亮度增减步进值

表示从 brightnessRangeMin 到 brightnessRangeMax 的有效增量。

可以按该值为单位更改亮度。

仅在混合模式下可用。

---

### brightness

属性 \ 访问: `r/w`

**说明**

视频的亮度

表示视频的亮度。

仅在混合模式下可用。

---

### hueRangeMin

属性 \ 访问: `r`

**说明**

视频的色相范围最小值

表示色相范围的最小值。

仅在混合模式下可用。

---

### hueRangeMax

属性 \ 访问: `r`

**说明**

视频的色相范围最大值

表示色相范围的最大值。

仅在混合模式下可用。

---

### hueDefaultValue

属性 \ 访问: `r`

**说明**

视频的色相默认值

表示色相的默认值。

仅在混合模式下可用。

---

### hueStepSize

属性 \ 访问: `r`

**说明**

视频的色相增减步进值

表示从 hueRangeMin 到 hueRangeMax 的有效增量。

可以按该值为单位更改色相。

仅在混合模式下可用。

---

### hue

属性 \ 访问: `r/w`

**说明**

视频的色相

表示视频的色相。

仅在混合模式下可用。

---

### saturationRangeMin

属性 \ 访问: `r`

**说明**

视频的饱和度范围最小值

表示饱和度范围的最小值。

仅在混合模式下可用。

---

### saturationRangeMax

属性 \ 访问: `r`

**说明**

视频的饱和度范围最大值

表示饱和度范围的最大值。

仅在混合模式下可用。

---

### saturationDefaultValue

属性 \ 访问: `r`

**说明**

视频的饱和度默认值

表示饱和度的默认值。

仅在混合模式下可用。

---

### saturationStepSize

属性 \ 访问: `r`

**说明**

视频的饱和度增减步进值

表示从 saturationRangeMin 到 saturationRangeMax 的有效增量。

可以按该值为单位更改饱和度。

仅在混合模式下可用。

---

### saturation

属性 \ 访问: `r/w`

**说明**

视频的饱和度

表示视频的饱和度。

仅在混合模式下可用。

---

### originalWidth

属性 \ 访问: `r`

**说明**

视频的实际宽度

所存储的视频的宽度。

---

### originalHeight

属性 \ 访问: `r`

**说明**

视频的实际高度

所存储的视频的高度。

---

### enabledVideoStream

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

当前启用的视频流编号

获取 / 设置当前用于播放的视频流的索引。
设置后会调用 `SelectVideoStream`，切换到对应的流。

**相关:** [VideoOverlay.numberOfVideoStream](VideoOverlay.md#numberofvideostream)

---

### numberOfVideoStream

属性 \ 访问: `r/w`

**类型**: `Integer`

**说明**

视频流数量

返回已打开的视频中包含的视频流的条数。只读。

**相关:** [VideoOverlay.enabledVideoStream](VideoOverlay.md#enabledvideostream)

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `storage` | `&nbsp;` | 打开所指定的媒体。 |

**说明**

打开媒体

打开所指定的媒体。

可播放的主要格式有 WebM (VP8/VP9，支持 Alpha)、MPEG-1 (扩展名 .mpeg / .mpg / .mpv)、
WMV / ASF、MP4 (.mp4 / .m4v / .mov，H.264 / HEVC)、AVI (取决于内部编解码器)。

WebM 支持带透明 (Alpha) 的视频。MP4 / WMV 等默认进行硬件解码。

MPEG-1 在规格上，帧率仅限于 23.976 / 24 / 25 / 29.97 / 30 / 50 / 59.94 / 60 fps。
对于 8fps 之类的低帧率素材，请重复相同帧使其变为 24fps 等之后再转换。

打开时也会向 onStatusChanged 发送 `"stop"`。检测播放结束时，
请只把前一个为 `"play"` 的 `"stop"` 视为结束。

---

### play

方法

**说明**

开始播放

开始播放媒体。

暂停中时从当前位置继续，停止后或播放到最后之后则从开头开始播放。

---

### stop

方法

**说明**

停止播放

停止媒体的播放。

---

### pause

方法

**说明**

暂停

暂停媒体的播放。

---

### rewind

方法

**说明**

倒回

把媒体的播放位置移动到开头。

---

### prepare

方法

**说明**

播放准备

把媒体的第 1 帧绘制到所指定的图层，并在绘制结束时引发 onPeriod 事件。
请在 prepare 方法调用后等待 onPeriod 事件，然后再进行播放。

仅在 mode 为 `vomLayer` (图层模式) 时有意义。

准备期间不播放音频。准备完成时媒体停在开头位置，
因此在接收到 onPeriod (perPrepare) 后再调用 play，就会从开头开始播放。

**相关:** [VideoOverlay.onPeriod](VideoOverlay.md#onperiod)

---

### setSegmentLoop

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `comeFrame` | `&nbsp;` | 循环移动目标帧 (循环的始端帧)。播放到达 goFrame 时，播放头会移动到该帧。 |
| `goFrame` | `&nbsp;` | 循环终点帧 (循环的终端帧)。该帧的前一帧显示结束时，播放头会移动到 comeFrame。 |

**说明**

帧间循环的设置

在指定的帧之间进行循环处理。

在循环终点 (goFrame) 会引发 onPeriod 事件。

必须预先在视频文件中为 comeFrame 的帧设置关键帧。

未设置时，
从循环终点移动到始点时，播放位置会移动到距所指定帧最近的关键帧。

**相关:** [VideoOverlay.cancelSegmentLoop](VideoOverlay.md#cancelsegmentloop) / [VideoOverlay.onPeriod](VideoOverlay.md#onperiod) / [VideoOverlay.segmentLoopStartFrame](VideoOverlay.md#segmentloopstartframe) / [VideoOverlay.segmentLoopEndFrame](VideoOverlay.md#segmentloopendframe)

---

### cancelSegmentLoop

方法

**说明**

帧间循环的解除

解除由 setSegmentLoop 方法指定的区间循环。

**相关:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### close

方法

**说明**

关闭媒体

关闭媒体。

为播放媒体而确保的资源等也会全部释放。

**相关:** [VideoOverlay.setSegmentLoop](VideoOverlay.md#setsegmentloop)

---

### setPeriodEvent

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `eventFrame` | `&nbsp;` | 指定引发 onPeriod 事件的帧。 |

**说明**

在指定帧引发事件的设置

在指定的帧引发 onPeriod 事件。

onPeriod 事件一旦引发就会被解除。希望再次引发时，请重新用该方法设置。

**相关:** [VideoOverlay.cancelPeriodEvent](VideoOverlay.md#cancelperiodevent) / [VideoOverlay.onPeriod](VideoOverlay.md#onperiod)

---

### cancelPeriodEvent

方法

**说明**

在指定帧引发事件的解除

解除由 setPeriodEvent 方法设置的事件引发。

**相关:** [VideoOverlay.setPeriodEvent](VideoOverlay.md#setperiodevent)

---

### setPos

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 指定用于播放媒体的矩形区域的左端位置。 |
| `top` | `&nbsp;` | 指定用于播放媒体的矩形区域的上端位置。 |

**说明**

指定播放矩形的左上位置

指定用于播放媒体的矩形区域的左上位置。

坐标为窗口客户区 ( 可显示图层的区域 ) 内的坐标，以像素为单位指定。

---

### setSize

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `width` | `&nbsp;` | 指定用于播放媒体的矩形区域的宽度。 |
| `height` | `&nbsp;` | 指定用于播放媒体的矩形区域的高度。 |

**说明**

指定播放矩形的大小

以像素为单位指定用于播放媒体的矩形区域的大小。

在当前版本中，图层播放时不能使用该方法。

---

### setBounds

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `left` | `&nbsp;` | 指定用于播放媒体的矩形区域的左端位置。 |
| `top` | `&nbsp;` | 指定用于播放媒体的矩形区域的上端位置。 |
| `width` | `&nbsp;` | 指定用于播放媒体的矩形区域的宽度。 |
| `height` | `&nbsp;` | 指定用于播放媒体的矩形区域的高度。 |

**说明**

指定播放矩形的位置与大小

指定用于播放媒体的矩形区域的位置与大小。

坐标为窗口客户区 ( 可显示图层的区域 ) 内的坐标，以像素为单位指定。

在当前版本中，图层播放时用该方法能指定的只有位置，大小会被忽略。

---

### selectAudioStream

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `streamNumber` | `&nbsp;` | 指定音频流编号。 |

**说明**

音频流的选择

启用所指定的音频流编号。

在不包含多条音频流的视频中不能使用。

**相关:** [VideoOverlay.numberOfAudioStream](VideoOverlay.md#numberofaudiostream) / [VideoOverlay.enabledAudioStream](VideoOverlay.md#enabledaudiostream)

---

### setMixingLayer

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 图层 |

**说明**

混合目标图层的设置

进行所指定图层与视频的混合。

混合是针对调用该方法时的图层图像进行的。

要使图层图像的更新得到反映，需要重新调用该方法。

使用 VideOverlay.OnFrameUpdate，
检查图层图像是否已更新并调用该方法，就可以自动反映更新。
如果在 onFrameUpdate 中每帧都调用该方法，会产生相当大的负载，因此最好避免那样做。

仅在混合模式下可用。

---

### resetMixingLayer

方法

**说明**

混合目标图层的设置解除

解除视频与图层的混合。

仅在混合模式下可用。

---

### onStatusChanged

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `status` | `&nbsp;` | 表示状态字符串。<br>为以下之一。<br>`"**unload**"   : ` 媒体未打开<br>`"**ready**"    : ` 媒体准备已完成<br>`"**play**"     : ` 媒体正在播放<br>`"**stop**"     : ` 媒体处于停止中<br>`"**pause**"    : ` 媒体处于暂停中 |

**说明**

状态已更改

在该对象的状态发生更改时发生。

ready 仅在 vomMFEVR 模式下发生。

---

### onPeriod

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `type` | `&nbsp;` | 表示 Period 事件的类型。<br>为以下之一。<br>`**perLoop**    : ` (通常)到达循环的终点。显示最终帧 1 帧的时间后，<br>在倒回开头时，每循环 1 周发生 1 次<br>`**perSegLoop** : ` 到达区间循环的终点<br>`**perPeriod**  : ` 到达由 setPeriodEvent 方法指定的帧<br>`**perPrepare** : ` 由 prepare 方法进行的播放准备已完成 |

**说明**

Period 事件已发生

在到达循环的终点或由 setPeriodEvent 指定的帧时，或由 prepare 方法完成播放准备时调用的方法。

在到达循环的终点或由 setPeriodEvent 指定的帧而调用该事件时，根据播放状况，播放位置有时可能已经超过了所指定的位置。要获取当前实际的播放位置，请参照 frame 属性。

**相关:** [VideoOverlay.setPeriodEvent](VideoOverlay.md#setperiodevent) / [VideoOverlay.prepare](VideoOverlay.md#prepare) / [VideoOverlay.frame](VideoOverlay.md#frame)

---

### onFrameUpdate

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `frame` | `&nbsp;` | 视频的帧编号 |

**说明**

视频帧已更新

在视频帧更新之后调用的方法。

作为参数的 frame 不一定与当前正在显示的视频帧完全一致。

显示开头帧 (帧 0) 时也会发生。帧编号以开头帧为 0 开始计数
(即使像 MP4 那样时间戳从 0 之后开始的素材，开头帧也是 0)。

仅在图层绘制模式、混合模式下可用。

---

### onCallbackCommand

事件

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `command` | `&nbsp;` | 指定命令名。 |
| `arg` | `&nbsp;` | 指定随命令附带的参数。 |

**说明**

自定义命令回调 ( 事件 )

从视频播放器接收到任意命令通知时触发的事件。

---
