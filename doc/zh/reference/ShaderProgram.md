# ShaderProgram

这是保存将 Vertex/Fragment 着色器编译/链接后结果的类。
编译/链接在构造函数中执行，有错误时会抛出异常，因此请查看日志进行修正。
用于着色器输入的参数会被添加到成员中，因此可以通过成员设置值。
从着色器获取变量名的操作使用反射进行。
Texture 等的指定已预先作为固定的保留字定好，并使用该名称创建。
作为顶点信息的 Attribute 属性值，只有在 drawMesh 中使用 VertexBuffer/VertexBindre 时才能通过成员设置。
ShaderProgram 原本就有的成员函数和属性必然不能用作着色器内的输入变量名 (因此目前只添加了最低限度的成员)。

如果为作为着色器内定义输入名而追加的属性设置好值，绘制时会设置该值。
追加的属性只能设置值，不能获取。
值会被一直保持，因此使用同一个着色器时，需要在绘制前改成想要指定的值。
属性的类型从着色器脚本获取。
vec4 等会作为 real 型数组传递给 Array 类。

保留字会在绘制执行时由内部自动设置，因此无需显式设置值 (drawMesh 除外)。
ex. 会向 s_tex0 传递第 1 个 texture id。
自动设置的值取决于绘制命令。

如果着色器能从脚本指定并自由替换，就可以预测：不必像以往那样为了给 Layer 扩展功能而编写插件，仅用 TJS2 脚本就能以比以往的 CPU 处理更快的速度追加演出。
目前没有相当于 Layer 的功能，但只要充实用 TJS2 脚本实现 Layer/Sprite 等所需的外围功能，那部分就能用脚本编写，从而比以往减少原生 (C++) 插件的出场机会。
如果把着色器与处理它的、实现 Sprite 等的 TJS2 脚本成套发布，就能以此强化演出。

以文件方式输入着色器脚本时，请使用 UTF-8 编写。


着色器内不能使用的 (内部定义的) 变量名

+ ShaderProgram
+ finalize

自动设置的值的名称

+ 纹理 : s_tex0, s_tex1, s_tex2, s_tex3...
+ 顶点坐标 : a_pos(vec2)
+ 纹理坐标 : a_texCoord(vec2)
+ 矩阵 : a_modelMat4(mat4)


初期阶段不支持 GLSL 的结构体和数组。

## 成员列表

### 构造函数

- [ShaderProgram](#shaderprogram)

---

### ShaderProgram

构造函数

**参数**

| 参数 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `vertex` | `string` | `&nbsp;` | 指定顶点着色器。<br>file 为 true 时为文件名，为 false 时直接指定字符串。 |
| `fragment` | `string` | `&nbsp;` | 指定片段着色器。<br>file 为 true 时为文件名，为 false 时直接指定字符串。 |
| `vsfile` | `boolean` | `true` | 选择 vertex 指定的字符串是文件名还是直接指定脚本。 |
| `fsfile` | `boolean` | `true` | 选择 fragment 指定的字符串是文件名还是直接指定脚本。 |

**说明**

构造函数

---
