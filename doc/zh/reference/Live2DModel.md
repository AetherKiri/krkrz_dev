# Live2DModel

信息参照与操作用模型

可以在没有设备 (OpenGL 上下文) 的情况下生成
可以进行模型的信息参照、参数操作与动作控制
要进行绘制，请使用 Live2DPlayer

## 成员列表

### 构造函数

- [Live2DModel](#live2dmodel)

### 方法

- [clear](#clear)
- [load](#load)
- [clone](#clone)
- [getExpressionCount](#getexpressioncount)
- [getExpressionName](#getexpressionname)
- [setExpression](#setexpression)
- [getExpression](#getexpression)
- [fixExpression](#fixexpression)
- [getMotionGroupCount](#getmotiongroupcount)
- [getMotionGroupName](#getmotiongroupname)
- [getMotionCount](#getmotioncount)
- [getMotionName](#getmotionname)
- [getMotionType](#getmotiontype)
- [setMotionType](#setmotiontype)
- [startMotion](#startmotion)
- [stopMotion](#stopmotion)
- [getCurrentMotions](#getcurrentmotions)
- [getParameterCount](#getparametercount)
- [getParameterInfo](#getparameterinfo)
- [getParameterValue](#getparametervalue)
- [setParameterValue](#setparametervalue)
- [setParameterType](#setparametertype)
- [setDiffParameterValue](#setdiffparametervalue)
- [progress](#progress)
- [canSync](#cansync)
- [sync](#sync)
- [addLipSyncId](#addlipsyncid)
- [addEyeBlinkId](#addeyeblinkid)
- [isPlaying](#isplaying)
- [getPartCount](#getpartcount)
- [getPartInfo](#getpartinfo)
- [getPartValue](#getpartvalue)
- [setPartValue](#setpartvalue)
- [setPartFadeTime](#setpartfadetime)
- [getEventCount](#geteventcount)
- [getEventName](#geteventname)
- [addVriableMotion](#addvriablemotion)
- [delVariableMotion](#delvariablemotion)
- [getVariableMotionCount](#getvariablemotioncount)
- [getVariableMotionName](#getvariablemotionname)
- [getVariableMotionInfo](#getvariablemotioninfo)
- [setVariable](#setvariable)
- [getVariable](#getvariable)
- [isMosaicModel](#ismosaicmodel)

---

### Live2DModel

构造函数

**说明**

构造函数

无需指定设备

---

### clear

方法

**说明**

清空内容

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` |  |

---

### clone

方法

**说明**

复制

---

### getExpressionCount

方法

---

### getExpressionName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### setExpression

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getExpression

方法

---

### fixExpression

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `id` | `&nbsp;` |  |

---

### getMotionGroupCount

方法

---

### getMotionGroupName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getMotionCount

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getMotionName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `no` | `&nbsp;` |  |

---

### getMotionType

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### setMotionType

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `type` | `&nbsp;` |  |

---

### startMotion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |
| `no_or_name` | `&nbsp;` |  |
| `loop` | `&nbsp;` |  |
| `fadeIn` | `&nbsp;` |  |
| `fadeOut` | `&nbsp;` |  |

---

### stopMotion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getCurrentMotions

方法

---

### getParameterCount

方法

---

### getParameterInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getParameterValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### setParameterValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### setParameterType

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `type` | `&nbsp;` |  |

---

### setDiffParameterValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### progress

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `tick` | `&nbsp;` |  |

---

### canSync

方法

---

### sync

方法

---

### addLipSyncId

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### addEyeBlinkId

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### isPlaying

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `group` | `&nbsp;` |  |

---

### getPartCount

方法

---

### getPartInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### getPartValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |

---

### setPartValue

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no_or_name` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### setPartFadeTime

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fadeTime` | `&nbsp;` |  |

---

### getEventCount

方法

---

### getEventName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` |  |

---

### addVriableMotion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |
| `group` | `&nbsp;` |  |
| `no_or_name` | `&nbsp;` |  |
| `min` | `&nbsp;` |  |
| `max` | `&nbsp;` |  |
| `descrete` | `&nbsp;` |  |

---

### delVariableMotion

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |

---

### getVariableMotionCount

方法

---

### getVariableMotionName

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### getVariableMotionInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `index` | `&nbsp;` |  |

---

### setVariable

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |
| `value` | `&nbsp;` |  |

---

### getVariable

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `varname` | `&nbsp;` |  |

---

### isMosaicModel

方法

---
