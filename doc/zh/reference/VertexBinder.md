# VertexBinder

VertexBinder 是用于将 VertexBuffer 与输入到着色器的顶点信息相关联的类。
在 ShaderProgram 的属性中设置该类的实例。
设置到 ShaderProgram 中的 VertexBinder 会在 Canvs.drawMesh 调用时作为顶点信息传递给着色器。

## 成员列表

### 构造函数

- [VertexBinder](#vertexbinder)

### 属性

- [vertexBuffer](#vertexbuffer)
- [stride](#stride)
- [componentCount](#componentcount)
- [offset](#offset)
- [normalize](#normalize)

---

### VertexBinder

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `vertex` | `VertexBuffer` | `&nbsp;` | 要关联的 VertexBuffer |
| `stride` | `int` | `0` | 以字节数指定每个顶点的步长。如果用 float 型传递 XY 坐标，由于是 sizeof(float)*2，所以指定 8。 |
| `componentCount` | `int` | `4` | 传递顶点元素数。如果传递 XY 坐标则指定 2。如果是 RGBA 颜色则为 4。 |
| `offset` | `int` | `0` | 以字节数指定从 VertexBuffer 开头的偏移量。在一个 VertexBuffer 中保存多个顶点信息时使用。 |
| `normalize` | `bool` | `false` | 指定是否进行规范化。为 true 时，非 float 型会规范化到 [-1.0~0.0~1.0] 之间并发送到着色器。 |

**说明**

构造函数

---

### vertexBuffer

属性 \ 访问: `r/w`

**说明**

顶点缓冲区 (VertexBuffer 类 readonly)

---

### stride

属性 \ 访问: `r/w`

**说明**

每个顶点的步长 (字节数)

默认为 0。

---

### componentCount

属性 \ 访问: `r/w`

**说明**

顶点元素数 (1~4)

默认为 4
XY 坐标时指定 2。

---

### offset

属性 \ 访问: `r/w`

**说明**

顶点缓冲区偏移量 (字节数)

默认为 0。
指定从 VertexBuffer 开头的字节偏移量。
在一个 VertexBuffer 中保存多个顶点信息时使用。

---

### normalize

属性 \ 访问: `r/w`

**说明**

是否进行规范化

默认为 false。
为 true 时，非 float 型会规范化到 [-1.0~0.0~1.0] 之间并发送到着色器。
在颜色信息等以 ubyte 型用 0~255 指定颜色、并将其规范化到 0.0~1.0 后在着色器中使用等情况下指定。

---
