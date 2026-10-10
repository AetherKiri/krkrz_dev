# AlphaMovie

基于伪代码的手册

吉里吉里Z AlphaMovie 插件。

播放带 Alpha 通道的视频容器 .amv (Alpha Movie)，并将各帧直接
（含 Alpha）覆盖绘制到目标 Layer 的主图像缓冲区。

使用示例:
var mov = new AlphaMovie();
mov.open("video/explosion.amv");
mov.setPosition(100, 80);
mov.loop = true;
// 每帧:
var no = mov.showNextImage(layer);

showNextImage 每次调用都会前进 1 帧，并返回已绘制的帧号。
若在末尾且 loop=true，则会倒回开头。若 loop=false 且已到末尾，
则会持续返回末尾帧号（若有 setNextMovieFile 预约，则自动切换到下一段视频）。
各帧只覆盖与帧固有矩形（left,top,width,height）对应的区域，因此
未被绘制的区域会保留 Layer 上前一帧的内容。

## 成员列表

### 构造函数

- [AlphaMovie](#alphamovie)

### 属性

- [numOfFrame](#numofframe)
- [frame](#frame)
- [loop](#loop)
- [nextLoop](#nextloop)
- [preloadSamples](#preloadsamples)
- [left](#left)
- [top](#top)
- [screenWidth](#screenwidth)
- [screenHeight](#screenheight)
- [FPSScale](#fpsscale)
- [FPSRate](#fpsrate)

### 方法

- [open](#open)
- [clear](#clear)
- [showNextImage](#shownextimage)
- [isPlaying](#isplaying)
- [play](#play)
- [stop](#stop)
- [setPosition](#setposition)
- [setNextMovieFile](#setnextmoviefile)

---

### AlphaMovie

构造函数

**说明**

构造函数 ( 无参数 )

---

### numOfFrame

属性 \ 访问: `r`

**说明**

总帧数（只读）

---

### frame

属性 \ 访问: `r/w`

**说明**

当前帧号。设置后会定位到该位置

---

### loop

属性 \ 访问: `r/w`

**说明**

是否循环播放

---

### nextLoop

属性 \ 访问: `r/w`

**说明**

下一段视频（setNextMovieFile）的循环设置

---

### preloadSamples

属性 \ 访问: `r/w`

**说明**

预读缓冲区数量（本实现仅保存值，默认 5）

---

### left

属性 \ 访问: `r/w`

**说明**

显示位置左（= setPosition 的 X）

---

### top

属性 \ 访问: `r/w`

**说明**

显示位置上（= setPosition 的 Y）

---

### screenWidth

属性 \ 访问: `r`

**说明**

视频的宽度（只读）

---

### screenHeight

属性 \ 访问: `r`

**说明**

视频的高度（只读）

---

### FPSScale

属性 \ 访问: `r`

**说明**

FPS 的分子。FPS = FPSScale / FPSRate（只读）

---

### FPSRate

属性 \ 访问: `r`

**说明**

FPS 的分母。FPS = FPSScale / FPSRate（只读）

---

### open

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 目标存储（.amv） |

**说明**

打开 amv

---

### clear

方法

**说明**

清除已解码队列（本实现为同步解码，因此为 no-op）

---

### showNextImage

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 绘制目标 Layer（需要为 hasImage） |

**返回值**

已绘制的帧号（整数）

**说明**

将下一帧绘制到目标 Layer

---

### isPlaying

方法

**返回值**

true=播放中 / false=停止中

**说明**

返回是否正在播放

---

### play

方法

**说明**

开始播放（倒回到开头帧，进入播放状态）

---

### stop

方法

**说明**

停止播放

---

### setPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 显示位置 X |
| `y` | `&nbsp;` | 显示位置 Y |

**说明**

设置显示位置（左上）

---

### setNextMovieFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 下一段要播放的 amv 存储 |

**说明**

预约下一段要播放的 amv（当前视频结束时自动切换）

---
