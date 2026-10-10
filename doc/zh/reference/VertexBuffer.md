# VertexBuffer

VertexBuffer 是保存顶点信息的类。

在想要细致设置位置指定、UV 坐标、顶点颜色等时使用。
在想要进行并非单纯矩形的网格变形等，或想要使用点精灵等情况下也会使用。

为了能用插件直接修改顶点数组，也可以进行指针访问 (但需 OpenGL ES 3.0 及以后)。
通过着色器 + TJS2 脚本 + 插件进行顶点操作，可以确保以往那样的 Layer 扩展性。
与以往几乎在插件内完成的方案相比，会稍微复杂一些。

## 成员列表

### 构造函数

- [VertexBuffer](#vertexbuffer)
- [VertexBuffer](#vertexbuffer)

### 属性

- [size](#size)
- [dataType](#datatype)
- [updateType](#updatetype)
- [isIndex](#isindex)
- [nativeHandle](#nativehandle)

### 方法

- [setVertex](#setvertex)
- [lock](#lock)
- [unlock](#unlock)

### 常量

- [dtByte](#dtbyte)
- [dtUByte](#dtubyte)
- [dtShort](#dtshort)
- [dtUShort](#dtushort)
- [dtInt](#dtint)
- [dtUInt](#dtuint)
- [dtFixed](#dtfixed)
- [dtFloat](#dtfloat)
- [utStream](#utstream)
- [utStatic](#utstatic)
- [utDynamic](#utdynamic)
- [ptPoints](#ptpoints)
- [ptLineStrip](#ptlinestrip)
- [ptLineLoop](#ptlineloop)
- [ptLines](#ptlines)
- [ptTriangleStrip](#pttrianglestrip)
- [ptTriangleFan](#pttrianglefan)
- [ptTriangles](#pttriangles)

---

### VertexBuffer

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `size` | `int` | `&nbsp;` | 缓冲区的字节数 |
| `dataType` | `int` | `&nbsp;` | 数据类型。dtByte/dtUByte/dtShort/dtUShort/dtInt/dtFloat |
| `updateType` | `int` | `&nbsp;` | 数据更新频率。utStream/utStatic/utDynamic |
| `isIndex` | `bool` | `false` | 是否为索引缓冲区。顶点缓冲区则为 false |

**说明**

创建未初始化的顶点缓冲区

---

### VertexBuffer

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | `Array` | `&nbsp;` | 顶点数组。缓冲区大小为该数组的元素数 × 数据类型大小。 |
| `dataType` | `int` | `&nbsp;` | 数据类型。dtByte/dtUByte/dtShort/dtUShort/dtInt/dtFloat |
| `updateType` | `int` | `&nbsp;` | 数据更新频率。utStream/utStatic/utDynamic |
| `isIndex` | `bool` | `false` | 是否为索引缓冲区。顶点缓冲区则为 false |

**说明**

指定顶点数组来创建顶点缓冲区

---

### size

属性 \ 访问: `r/w`

**说明**

缓冲区大小 (readonly)

---

### dataType

属性 \ 访问: `r/w`

**说明**

顶点数据的类型 (readonly)

---

### updateType

属性 \ 访问: `r/w`

**说明**

数据更新频率 (readonly)

---

### isIndex

属性 \ 访问: `r/w`

**说明**

是否为索引缓冲区 (readonly)

---

### nativeHandle

属性 \ 访问: `r/w`

**说明**

原生句柄

---

### setVertex

方法

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `array` | `Array` | `&nbsp;` | 顶点数组 |
| `offset` | `int` | `0` | 开始修改的数组偏移索引 (非字节大小) |

**说明**

设置/更新顶点数据

为 Static 时失败 (异常)。

---

### lock

方法

**返回值**

指向顶点数据的指针，锁定失败时为 null

**说明**

锁定顶点数据，并返回指向数据的指针 (read/write 指定)

供插件使用 (仅 OpenGL ES 3.0 及以后可用)

---

### unlock

方法

**说明**

解除顶点数据的锁定

供插件使用 (仅 OpenGL ES 3.0 及以后可用)。
数据传递结束后，在该缓冲区被使用之前调用。
不要维持 lock，更新后立即 unlock 较为理想。

---

### dtByte

常量

**说明**

数据类型常量 (byte)

---

### dtUByte

常量

**说明**

数据类型常量 (unsigned byte)

---

### dtShort

常量

**说明**

数据类型常量 (short)

---

### dtUShort

常量

**说明**

数据类型常量 (unsigned short)

---

### dtInt

常量

**说明**

数据类型常量 (int) 需要 ES3.0 及以后

---

### dtUInt

常量

**说明**

数据类型常量 (unsinged int) 需要 ES3.0 及以后

---

### dtFixed

常量

**说明**

数据类型常量 (fixed:定点小数)

---

### dtFloat

常量

**说明**

数据类型常量 (float)

---

### utStream

常量

**说明**

更新频率常量:每帧更新

---

### utStatic

常量

**说明**

更新频率常量:无更改

---

### utDynamic

常量

**说明**

更新频率常量:会被频繁更新

---

### ptPoints

常量

**说明**

图元类型常量 (点列表)

---

### ptLineStrip

常量

**说明**

图元类型常量 (线段带)

---

### ptLineLoop

常量

**说明**

图元类型常量 (线段环)

---

### ptLines

常量

**说明**

图元类型常量 (线段列表)

---

### ptTriangleStrip

常量

**说明**

图元类型常量 (三角形带)

---

### ptTriangleFan

常量

**说明**

图元类型常量 (三角形扇)

---

### ptTriangles

常量

**说明**

图元类型常量 (三角形列表)

---
