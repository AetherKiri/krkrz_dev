# Steam

Steam 类 (static)

## 成员列表

### 属性

- [initialized](#initialized)
- [achievementsCount](#achievementscount)
- [steamID](#steamid)
- [accountID](#accountid)
- [loggedOn](#loggedon)
- [personaName](#personaname)
- [appID](#appid)
- [cloudEnabled](#cloudenabled)
- [coundFileCount](#coundfilecount)

### 方法

- [requestInitialize](#requestinitialize)
- [getAchievement](#getachievement)
- [setAchievement](#setachievement)
- [clearAchievment](#clearachievment)
- [getLanguage](#getlanguage)
- [RestartAppIfNecessary](#restartappifnecessary)
- [getCloudQuota](#getcloudquota)
- [getCloudFileInfo](#getcloudfileinfo)
- [deleteCloudFile](#deletecloudfile)
- [copyCloudFile](#copycloudfile)
- [triggerScreenshot](#triggerscreenshot)
- [hookScreenshots](#hookscreenshots)
- [writeScreenshot](#writescreenshot)
- [isBroadcasting](#isbroadcasting)
- [hookBroadcasting](#hookbroadcasting)
- [isIsSubscribedApp](#isissubscribedapp)
- [ssDlcInstalled](#ssdlcinstalled)
- [getDLCCount](#getdlccount)
- [getDLCData](#getdlcdata)

---

### initialized

属性 \ 访问: `r`

**说明**

成就信息已初始化

---

### achievementsCount

属性 \ 访问: `r`

**说明**

成就数量

---

### steamID

属性 \ 访问: `r`

**说明**

--------------------------------------------------------- 用户信息 --------------------------------------------------------- 设想用于按用户区分存档数据的存放位置。 Steam 自身的 userdata 文件夹按 32bit 的账户 ID 区分，因此若要与之保持一致，请使用 accountID。 SteamID (64bit) 的字符串。无法获取时为空字符串

---

### accountID

属性 \ 访问: `r`

**说明**

账户 ID (32bit 的整数)。与 Steam 的 userdata 文件夹名相同的值。 无法获取时为 0

---

### loggedOn

属性 \ 访问: `r`

**说明**

是否已登录 Steam

---

### personaName

属性 \ 访问: `r`

**说明**

显示名 (persona 名)。无法获取时为空字符串

---

### appID

属性 \ 访问: `r`

**说明**

正在运行的 AppID。无法获取时为 0

---

### cloudEnabled

属性 \ 访问: `r/w`

**说明**

--------------------------------------------------------- 云 --------------------------------------------------------- Steam 云的启用/禁用设置

---

### coundFileCount

属性 \ 访问: `r/w`

**说明**

Steam 云的文件数

---

### requestInitialize

方法

**返回值**

调用成功

**说明**

成就信息重新获取请求 ※启动时会被调用，通常无需调用

--------------------------------------------------------- 成就 ---------------------------------------------------------

---

### getAchievement

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `n` | `&nbsp;` |  |

---

### setAchievement

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `n` | `&nbsp;` |  |

---

### clearAchievment

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `n` | `&nbsp;` | 编号或识别名 |

**说明**

解除成就

---

### getLanguage

方法

**返回值**

获取当前 Steam 的语言

**说明**

静态方法

--------------------------------------------------------- 其他信息 ---------------------------------------------------------

---

### RestartAppIfNecessary

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `appid` | `&nbsp;` | 自己的 AppID |

**返回值**

若为 true，Steam 会重新启动，因此应立即退出应用

※只有此方法可以在不触发 Steam 初始化的情况下调用
(初始化在首次引用其他 Steam.* 时进行)

**说明**

检查是否需要经由 Steam 客户端重新启动

--------------------------------------------------------- 启动检查 ---------------------------------------------------------

---

### getCloudQuota

方法

**返回值**

%[total:总大小, available:可用容量]

**说明**

获取 Steam 云的容量信息

---

### getCloudFileInfo

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `n` | `&nbsp;` | 文件编号 |

**返回值**

%[filename:名称, size:大小, time:时间戳]

**说明**

获取单个 Steam 云文件的名称和大小信息

---

### deleteCloudFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**返回值**

成功则为 true

**说明**

删除 Steam 云文件

---

### copyCloudFile

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `src` | `&nbsp;` |  |
| `dest` | `&nbsp;` |  |

**返回值**

成功则为 true

**说明**

复制 Steam 云文件

---

### triggerScreenshot

方法

**说明**

从应用侧触发截图处理

--------------------------------------------------------- 截图 ---------------------------------------------------------

---

### hookScreenshots

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | 回调函数（为 void 时解除注册）<br>※在回调函数内调用 writeScreenshot |

---

### writeScreenshot

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `layer` | `&nbsp;` | 图像 |
| `location` | `&nbsp;` | "位置字符串" (为空字符串时不注册) |

**说明**

注册截图

---

### isBroadcasting

方法

**返回值**

正在直播时为真

**说明**

--------------------------------------------------------- 直播状态 ---------------------------------------------------------

---

### hookBroadcasting

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `callback` | `&nbsp;` | 回调函数 (function (is_start) {}) |

**说明**

直播状态改变时的回调

---

### isIsSubscribedApp

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `appID` | `&nbsp;` |  |

**说明**

--------------------------------------------------------- DLC --------------------------------------------------------- 仅当需要检查与自己游戏相关的另一款游戏（例如体验版）的所有权时才使用此成员

---

### ssDlcInstalled

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `appID` | `&nbsp;` |  |

**说明**

接收 DLC 的 AppID，检查用户是否拥有该 DLC 以及该 DLC 是否已安装

---

### getDLCCount

方法

**返回值**

返回 DLC 的数量

---

### getDLCData

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `no` | `&nbsp;` | DLC 的编号 |

---
