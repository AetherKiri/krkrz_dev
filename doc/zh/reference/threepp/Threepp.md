# Threepp

threepp 插件 基于伪代码的手册

threepp 是 three.js 的 C++ 移植版。
提供 3D 图形渲染功能。

## 成员列表

### 常量

- [Side_Front](#side_front)
- [Side_Back](#side_back)
- [Side_Double](#side_double)
- [Blending_None](#blending_none)
- [Blending_Normal](#blending_normal)
- [Blending_Additive](#blending_additive)
- [Blending_Subtractive](#blending_subtractive)
- [Blending_Multiply](#blending_multiply)
- [Blending_Custom](#blending_custom)
- [CullFace_None](#cullface_none)
- [CullFace_Back](#cullface_back)
- [CullFace_Front](#cullface_front)
- [CullFace_FrontBack](#cullface_frontback)
- [ShadowMap_Basic](#shadowmap_basic)
- [ShadowMap_PFC](#shadowmap_pfc)
- [ShadowMap_PFCSoft](#shadowmap_pfcsoft)
- [ShadowMap_VSM](#shadowmap_vsm)
- [ToneMapping_None](#tonemapping_none)
- [ToneMapping_Linear](#tonemapping_linear)
- [ToneMapping_Reinhard](#tonemapping_reinhard)
- [ToneMapping_Cineon](#tonemapping_cineon)
- [ToneMapping_ACESFilmic](#tonemapping_acesfilmic)
- [ToneMapping_Custom](#tonemapping_custom)
- [Encoding_Linear](#encoding_linear)
- [Encoding_sRGB](#encoding_srgb)
- [Encoding_Gamma](#encoding_gamma)
- [TextureWrapping_Repeat](#texturewrapping_repeat)
- [TextureWrapping_ClampToEdge](#texturewrapping_clamptoedge)
- [TextureWrapping_MirroredRepeat](#texturewrapping_mirroredrepeat)
- [Filter_Nearest](#filter_nearest)
- [Filter_Linear](#filter_linear)
- [Filter_NearestMipmapNearest](#filter_nearestmipmapnearest)
- [Filter_NearestMipmapLinear](#filter_nearestmipmaplinear)
- [Filter_LinearMipmapNearest](#filter_linearmipmapnearest)
- [Filter_LinearMipmapLinear](#filter_linearmipmaplinear)
- [Loop_Once](#loop_once)
- [Loop_Repeat](#loop_repeat)
- [Loop_PingPong](#loop_pingpong)
- [Loop_Once](#loop_once)
- [Loop_Repeat](#loop_repeat)
- [Loop_PingPong](#loop_pingpong)
- [CatmullRomCurve3_CurveType_centripetal](#catmullromcurve3_curvetype_centripetal)
- [CatmullRomCurve3_CurveType_chordal](#catmullromcurve3_curvetype_chordal)
- [CatmullRomCurve3_CurveType_catmullrom](#catmullromcurve3_curvetype_catmullrom)

---

### Side_Front

常量

值: `0`

**说明**

============================================================ Side 定义 (材质的绘制面) ============================================================

---

### Side_Back

常量

值: `1`

**说明**

仅绘制表面

---

### Side_Double

常量

值: `2`

**说明**

仅绘制背面

---

### Blending_None

常量

值: `0`

**说明**

双面绘制 ============================================================ Blending 定义 (混合模式) ============================================================

---

### Blending_Normal

常量

值: `1`

---

### Blending_Additive

常量

值: `2`

---

### Blending_Subtractive

常量

值: `3`

---

### Blending_Multiply

常量

值: `4`

---

### Blending_Custom

常量

值: `5`

---

### CullFace_None

常量

值: `0`

**说明**

============================================================ CullFace 定义 (剔除) ============================================================

---

### CullFace_Back

常量

值: `1`

---

### CullFace_Front

常量

值: `2`

---

### CullFace_FrontBack

常量

值: `3`

---

### ShadowMap_Basic

常量

值: `0`

**说明**

============================================================ ShadowMap 定义 (阴影贴图类型) ============================================================

---

### ShadowMap_PFC

常量

值: `1`

---

### ShadowMap_PFCSoft

常量

值: `2`

---

### ShadowMap_VSM

常量

值: `3`

---

### ToneMapping_None

常量

值: `0`

**说明**

============================================================ ToneMapping 定义 (色调映射) ============================================================

---

### ToneMapping_Linear

常量

值: `1`

---

### ToneMapping_Reinhard

常量

值: `2`

---

### ToneMapping_Cineon

常量

值: `3`

---

### ToneMapping_ACESFilmic

常量

值: `4`

---

### ToneMapping_Custom

常量

值: `5`

---

### Encoding_Linear

常量

值: `3000`

**说明**

============================================================ Encoding 定义 (输出编码) ============================================================

---

### Encoding_sRGB

常量

值: `3001`

---

### Encoding_Gamma

常量

值: `3007`

---

### TextureWrapping_Repeat

常量

值: `1000`

**说明**

============================================================ TextureWrapping 定义 (纹理环绕) ============================================================

---

### TextureWrapping_ClampToEdge

常量

值: `1001`

---

### TextureWrapping_MirroredRepeat

常量

值: `1002`

---

### Filter_Nearest

常量

值: `1003`

**说明**

============================================================ Filter 定义 (纹理过滤器) ============================================================

---

### Filter_Linear

常量

值: `1006`

---

### Filter_NearestMipmapNearest

常量

值: `1004`

---

### Filter_NearestMipmapLinear

常量

值: `1005`

---

### Filter_LinearMipmapNearest

常量

值: `1007`

---

### Filter_LinearMipmapLinear

常量

值: `1008`

---

### Loop_Once

常量

值: `2200`

**说明**

============================================================ Loop 定义 (动画循环) ============================================================

---

### Loop_Repeat

常量

值: `2201`

---

### Loop_PingPong

常量

值: `2202`

---

### Loop_Once

常量

值: `2200`

**说明**

Loop 模式常量 (传给 AnimationAction.setLoop)

---

### Loop_Repeat

常量

值: `2201`

**说明**

播放一次后停止

---

### Loop_PingPong

常量

值: `2202`

**说明**

循环 (ModelAnimator.play 的默认值)

---

### CatmullRomCurve3_CurveType_centripetal

常量

值: `0`

**说明**

往返

---

### CatmullRomCurve3_CurveType_chordal

常量

值: `1`

---

### CatmullRomCurve3_CurveType_catmullrom

常量

值: `2`

---
