# krkrthreepp (threepp 3D) 参考文档

本页是用于在吉里吉里Z 中操作 threepp (three.js 兼容的 C++ 3D 引擎) 的插件 `krkrthreepp` 所提供的类群参考文档。
收录了 3D 场景构建、几何体、材质、相机、灯光、曲线/形状、动画、VRM/glTF 加载器等共计 110 个类。

插件概要与使用示例请参见 `src/plugins/krkrthreepp/README.md`。

- [Threepp (命名空间)](Threepp.md) — threepp 插件 基于伪代码的手册

## 类列表

| 类 | 概要 |
|---|---|
| [AmbientLight](Threepp.AmbientLight.md) | 环境光 |
| [AnimationAction](Threepp.AnimationAction.md) | 正在播放的一个动画（由 ModelAnimator.clipAction/play 返回） |
| [ArrowHelper](Threepp.ArrowHelper.md) | 箭头辅助对象 |
| [AxesHelper](Threepp.AxesHelper.md) | 坐标轴辅助对象 |
| [Bone](Threepp.Bone.md) | 骨骼 |
| [Box2](Threepp.Box2.md) | 2D 轴对齐包围盒类 |
| [Box3](Threepp.Box3.md) | 轴对齐包围盒 (AABB) 类 |
| [BoxGeometry](Threepp.BoxGeometry.md) | 长方体（立方体）几何体 |
| [BoxHelper](Threepp.BoxHelper.md) | 盒辅助对象 |
| [BufferGeometry](Threepp.BufferGeometry.md) | 缓冲几何体基类 |
| [Camera](Threepp.Camera.md) | 相机基类 |
| [CameraHelper](Threepp.CameraHelper.md) | 相机辅助对象 |
| [CapsuleGeometry](Threepp.CapsuleGeometry.md) | 胶囊几何体 |
| [CatmullRomCurve3](Threepp.CatmullRomCurve3.md) | CatmullRom 样条曲线 |
| [CircleGeometry](Threepp.CircleGeometry.md) | 圆形（圆盘）几何体 |
| [Clock](Threepp.Clock.md) | 计时器类 |
| [Color](Threepp.Color.md) | 颜色类 |
| [ConeGeometry](Threepp.ConeGeometry.md) | 圆锥几何体 |
| [CubicBezierCurve](Threepp.CubicBezierCurve.md) | 2D 三次贝塞尔曲线 |
| [CubicBezierCurve3](Threepp.CubicBezierCurve3.md) | 3D 三次贝塞尔曲线 |
| [CylinderGeometry](Threepp.CylinderGeometry.md) | 圆柱几何体 |
| [Cylindrical](Threepp.Cylindrical.md) | 圆柱坐标类 |
| [DataTexture](Threepp.DataTexture.md) | 数据纹理 |
| [DirectionalLight](Threepp.DirectionalLight.md) | 平行光（类似太阳光的光） |
| [DirectionalLightHelper](Threepp.DirectionalLightHelper.md) | 平行光辅助对象 |
| [EdgesGeometry](Threepp.EdgesGeometry.md) | 边缘几何体 |
| [EllipseCurve](Threepp.EllipseCurve.md) | 椭圆曲线 |
| [Euler](Threepp.Euler.md) | 欧拉角类 |
| [ExtrudeGeometry](Threepp.ExtrudeGeometry.md) | ExtrudeGeometry（挤出几何体） |
| [Fog](Threepp.Fog.md) | 雾（线性） |
| [FogExp2](Threepp.FogExp2.md) | 雾（指数函数） |
| [GLRenderer](Threepp.GLRenderer.md) | OpenGL 渲染器 |
| [GLTFLoader](Threepp.GLTFLoader.md) | 通用 glTF/GLB 加载器 |
| [GLTFModel](Threepp.GLTFModel.md) | 已加载的 glTF 模型 (GLTFLoader 的返回值) |
| [GridHelper](Threepp.GridHelper.md) | 栅格辅助对象 |
| [Group](Threepp.Group.md) | 组类 |
| [HemisphereLight](Threepp.HemisphereLight.md) | 半球光 |
| [IcosahedronGeometry](Threepp.IcosahedronGeometry.md) | 正二十面体几何体 |
| [InstancedMesh](Threepp.InstancedMesh.md) | 实例化网格 |
| [LatheGeometry](Threepp.LatheGeometry.md) | 车削几何体 |
| [Light](Threepp.Light.md) | 灯光基类 |
| [Line](Threepp.Line.md) | 线对象 |
| [Line3](Threepp.Line3.md) | 3D 线段类 |
| [LineBasicMaterial](Threepp.LineBasicMaterial.md) | 线条基础材质 |
| [LineCurve](Threepp.LineCurve.md) | 2D 直线曲线 |
| [LineCurve3](Threepp.LineCurve3.md) | 3D 直线曲线 |
| [LineSegments](Threepp.LineSegments.md) | 线段对象 |
| [LOD](Threepp.LOD.md) | LOD (Level of Detail) |
| [Material](Threepp.Material.md) | 材质基类 |
| [Matrix3](Threepp.Matrix3.md) | 3x3 矩阵类 |
| [Matrix4](Threepp.Matrix4.md) | 4x4 矩阵类 |
| [Mesh](Threepp.Mesh.md) | 网格类 |
| [MeshBasicMaterial](Threepp.MeshBasicMaterial.md) | 基础材质 |
| [MeshDepthMaterial](Threepp.MeshDepthMaterial.md) | 深度材质 |
| [MeshLambertMaterial](Threepp.MeshLambertMaterial.md) | Lambert 材质 |
| [MeshMatcapMaterial](Threepp.MeshMatcapMaterial.md) | MatCap 材质 |
| [MeshNormalMaterial](Threepp.MeshNormalMaterial.md) | 法线材质 |
| [MeshPhongMaterial](Threepp.MeshPhongMaterial.md) | Phong 材质 |
| [MeshStandardMaterial](Threepp.MeshStandardMaterial.md) | Standard PBR 材质 |
| [MeshToonMaterial](Threepp.MeshToonMaterial.md) | 卡通（赛璐璐着色）材质 |
| [ModelAnimator](Threepp.ModelAnimator.md) | 模型动画播放器 (相当于 three.js 的 AnimationMixer) |
| [Object3D](Threepp.Object3D.md) | 3D 对象的基类 |
| [OctahedronGeometry](Threepp.OctahedronGeometry.md) | 正八面体几何体 |
| [OrthographicCamera](Threepp.OrthographicCamera.md) | 正交相机 |
| [Path](Threepp.Path.md) | 2D 路径 |
| [PerspectiveCamera](Threepp.PerspectiveCamera.md) | 透视投影相机 |
| [Plane](Threepp.Plane.md) | 平面类 |
| [PlaneGeometry](Threepp.PlaneGeometry.md) | 平面几何体 |
| [PlaneHelper](Threepp.PlaneHelper.md) | 平面辅助对象 |
| [PointLight](Threepp.PointLight.md) | 点光源 |
| [PointLightHelper](Threepp.PointLightHelper.md) | 点光源辅助对象 |
| [Points](Threepp.Points.md) | 点云对象 |
| [PointsMaterial](Threepp.PointsMaterial.md) | 点云材质 |
| [PolarGridHelper](Threepp.PolarGridHelper.md) | 极坐标栅格辅助对象 |
| [QuadraticBezierCurve](Threepp.QuadraticBezierCurve.md) | 2D 二次贝塞尔曲线 |
| [QuadraticBezierCurve3](Threepp.QuadraticBezierCurve3.md) | 3D 二次贝塞尔曲线 |
| [Quaternion](Threepp.Quaternion.md) | 四元数类 |
| [RawShaderMaterial](Threepp.RawShaderMaterial.md) | Raw 着色器材质 |
| [Ray](Threepp.Ray.md) | 光线类 |
| [Raycaster](Threepp.Raycaster.md) | 射线投射器 |
| [Reflector](Threepp.Reflector.md) | 反射面对象 |
| [RingGeometry](Threepp.RingGeometry.md) | 环形（环状）几何体 |
| [Scene](Threepp.Scene.md) | 场景类 |
| [ShaderMaterial](Threepp.ShaderMaterial.md) | 着色器材质 |
| [Shape](Threepp.Shape.md) | Shape（带孔的 2D 形状） |
| [ShapeGeometry](Threepp.ShapeGeometry.md) | ShapeGeometry（2D 形状几何体） |
| [Skeleton](Threepp.Skeleton.md) | 骨架 |
| [SkinnedMesh](Threepp.SkinnedMesh.md) | 蒙皮网格 |
| [Sky](Threepp.Sky.md) | 天空对象 |
| [Sphere](Threepp.Sphere.md) | 球类 |
| [SphereGeometry](Threepp.SphereGeometry.md) | 球几何体 |
| [Spherical](Threepp.Spherical.md) | 球面坐标类 |
| [SplineCurve](Threepp.SplineCurve.md) | 2D 样条曲线 |
| [SpotLight](Threepp.SpotLight.md) | 聚光灯 |
| [SpotLightHelper](Threepp.SpotLightHelper.md) | 聚光灯辅助对象 |
| [Sprite](Threepp.Sprite.md) | 精灵对象 |
| [SpriteMaterial](Threepp.SpriteMaterial.md) | 精灵材质 |
| [Texture](Threepp.Texture.md) | 纹理基类 |
| [TextureLoader](Threepp.TextureLoader.md) | 纹理加载器 |
| [TorusGeometry](Threepp.TorusGeometry.md) | 圆环（甜甜圈形状）几何体 |
| [TorusKnotGeometry](Threepp.TorusKnotGeometry.md) | 圆环纽结几何体 |
| [Triangle](Threepp.Triangle.md) | 三角形类 |
| [Vector2](Threepp.Vector2.md) | 2D 向量类 |
| [Vector3](Threepp.Vector3.md) | 3D 向量类 |
| [VRM](Threepp.VRM.md) | 1 个 VRM 模型 |
| [VRMAnimation](Threepp.VRMAnimation.md) | VRM 动画 (.vrma / VRMC_vrm_animation) |
| [VRMAnimationLoader](Threepp.VRMAnimationLoader.md) | VRM 动画加载器 |
| [VRMLoader](Threepp.VRMLoader.md) | VRM 加载器 |
| [Water](Threepp.Water.md) | 水面对象 |
| [WireframeGeometry](Threepp.WireframeGeometry.md) | 线框几何体 |
