# SoundListener

SoundListener 类是在 3D 音频定位中控制“听者”的类。无法从该类创建对象。与 System 相同，以 `SoundListener.setPosition(...)` 这样直接调用的方式使用。

该类控制基于 miniaudio 的 3D 音频定位中由引擎共享的听者 (listener 0)。音源侧通过 WaveSoundBuffer 的 [use3D](WaveSoundBuffer.md#use3d) 和 set3DPosition 等设置。

坐标系遵循 miniaudio (右手系、Y up、任意单位，默认情况下 forward = -Z, up = +Y，锥体角度为弧度)。

另外，不支持 HRTF。在立体声环境下无法区分前后，只会反映 L / R 声像与基于距离的衰减。

## 成员列表

### 属性

- [enabled](#enabled)

### 方法

- [setPosition](#setposition)
- [setDirection](#setdirection)
- [setWorldUp](#setworldup)
- [setVelocity](#setvelocity)
- [setCone](#setcone)

---

### enabled

属性 \ 访问: `r/w`

**说明**

是否启用听者 (3D 定位)

表示是否启用听者 (3D 定位)。也可以设置值。

**相关:** [WaveSoundBuffer.use3D](WaveSoundBuffer.md#use3d)

---

### setPosition

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定位置的 X 分量。 |
| `y` | `&nbsp;` | 指定位置的 Y 分量。 |
| `z` | `&nbsp;` | 指定位置的 Z 分量。 |

**说明**

听者位置的设置

设置听者的位置。

---

### setDirection

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定 forward 矢量的 X 分量。 |
| `y` | `&nbsp;` | 指定 forward 矢量的 Y 分量。 |
| `z` | `&nbsp;` | 指定 forward 矢量的 Z 分量。 |

**说明**

听者朝向的设置

设置听者的朝向 (forward 矢量)。

---

### setWorldUp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定 up 矢量的 X 分量。 |
| `y` | `&nbsp;` | 指定 up 矢量的 Y 分量。 |
| `z` | `&nbsp;` | 指定 up 矢量的 Z 分量。 |

**说明**

世界坐标上方向矢量的设置

设置世界坐标的上方向 (up) 矢量。

---

### setVelocity

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `x` | `&nbsp;` | 指定速度的 X 分量。 |
| `y` | `&nbsp;` | 指定速度的 Y 分量。 |
| `z` | `&nbsp;` | 指定速度的 Z 分量。 |

**说明**

听者速度的设置

设置用于多普勒计算的听者速度。

---

### setCone

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `innerAngleRad` | `&nbsp;` | 以弧度指定锥体的内侧角度。 |
| `outerAngleRad` | `&nbsp;` | 以弧度指定锥体的外侧角度。 |
| `outerGain` | `&nbsp;` | 指定锥体外侧的增益 (0~1)。 |

**说明**

听者指向性锥体的设置

设置听者的指向性锥体。角度以弧度为单位指定。

---
