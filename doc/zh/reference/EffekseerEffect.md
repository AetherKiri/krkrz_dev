# EffekseerEffect

特效素材

保存已加载的特效。由于可以被多个 EffekseerPlayer 共享，
需要同时播放多个相同特效时，复用该对象即可。

## 成员列表

### 构造函数

- [EffekseerEffect](#effekseereffect)

### 属性

- [device](#device)
- [meta](#meta)
- [loaded](#loaded)
- [filename](#filename)
- [magnification](#magnification)
- [termMin](#termmin)
- [termMax](#termmax)

### 方法

- [load](#load)
- [clear](#clear)
- [unloadResources](#unloadresources)
- [reloadResources](#reloadresources)
- [readMeta](#readmeta)
- [setDynamicInputNames](#setdynamicinputnames)
- [findDynamicInput](#finddynamicinput)

---

### EffekseerEffect

构造函数

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `device` | `&nbsp;` | EffekseerDevice 实例 |

**说明**

构造函数

---

### device

属性 \ 访问: `r/w`

**说明**

只读

---

### meta

属性 \ 访问: `r/w`

**说明**

.efkzip 中随附的附属信息 (effect.json)。没有时为 void

特效的二进制中不会保留“动态参数的名字”。其中只包含
默认值和已编译的代码，本来只能通过编号访问。因此
约定用 JSON 保存名字与编号的对应关系等。
加载 .efkzip 时会自动解析，因此加载侧不需要额外步骤。

只有以下 2 个具有确定的含义，其余原样传递:
dynamicInputs … [ %[ name:"emitter.x", index:0 ], ... ]
会作为 setDynamicInputByName() 的对应表自动导入
motions       … [ %[ name:"...", file:"motion/....json", ... ], ... ]

var meta = effect.meta;
if (meta !== void && meta.motions !== void)
var path = effect.readMeta(meta.motions[0].file);

---

### loaded

属性 \ 访问: `r/w`

**说明**

只读: 是否已加载

---

### filename

属性 \ 访问: `r/w`

**说明**

只读: 规范化后的存储名

---

### magnification

属性 \ 访问: `r/w`

**说明**

只读: 加载时的放大率

---

### termMin

属性 \ 访问: `r/w`

**说明**

只读: 预期播放长度的最小值(帧)

---

### termMax

属性 \ 访问: `r/w`

**说明**

只读: 预期播放长度的最大值(帧)

---

### load

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `filename` | `&nbsp;` | 存储名 (.efkzip / .efkefc / .efk) |
| `magnification` | `&nbsp;` | 加载时的放大率 (省略时为 1.0) |
| `entry` | `&nbsp;` | .efkzip 内的特效文件名 (可省略)<br>・.efkzip … 将特效主体与纹理/模型整套打包的 ZIP。<br>Effekseer 的特效素材会分成多个文件，因此通常使用这种格式<br>(与 Live2D 的 .l2d 思路相同)。素材按 ZIP 内的相对路径解析。<br>省略 entry 时使用 ZIP 内第一个 .efkefc (没有时使用 .efk)。<br>・.efkefc / .efk … 指定单个文件。素材以 filename 所在的目录为基准<br>解析，找不到时会仅用文件名在自动搜索路径中查找<br>(针对打包进 XP3 后目录结构被压平的情况)。<br>失败时会抛出异常。 |

**说明**

加载特效文件

---

### clear

方法

**说明**

清除内容

---

### unloadResources

方法

**说明**

素材(纹理/模型等)的释放与重新加载

---

### reloadResources

方法

---

### readMeta

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` | ZIP 内的路径 |

**返回值**

无法解析时为 void

**说明**

将 .efkzip 内的 JSON 文件作为字典 / 数组读取

---

### setDynamicInputNames

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `names` | `&nbsp;` |  |

**说明**

替换动态参数的名字与输入编号的对应关系

如果是 .efkzip，会自动从 effect.json 载入，通常无需调用。
在直接读取 .efk / .efkefc 时，或想更换名字时使用。

effect.setDynamicInputNames(%[ "emitter.x" => 0, "emitter.y" => 1 ]);
effect.setDynamicInputNames(["emitter.x", "emitter.y"]);  // 排列顺序即为编号
effect.setDynamicInputNames([ %[ name:"emitter.x", index:0 ] ]);

传入 void 会清除注册。

---

### findDynamicInput

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

**返回值**

找不到时为 -1

**说明**

从注册的对应关系中查出输入编号

---
