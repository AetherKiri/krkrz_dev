# 吉里吉里Z 中删除的功能
即使是从吉里吉里Z 引擎本体中删除的功能，只要加入插件等也可以使用。

## KagParser 类
连接吉里吉里Z 仓库中随附的 KAGParser.dll 后即可使用。

## Menu 类
连接吉里吉里Z 仓库中随附的 menu.dll 后即可使用。

## Pad 类
加载吉里吉里Z 仓库中随附的 Krkr2Compat 后即可使用。

## 控制台窗口(Debug.console)
加载吉里吉里Z 仓库中随附的 Krkr2Compat 后即可使用。

## 脚本编辑器
加载吉里吉里Z 仓库中随附的 Krkr2Compat 后即可使用。

## 字体选择对话框(Font.doUserSelect)
加载吉里吉里Z 仓库中随附的 Krkr2Compat 后即可使用。

## 单行输入对话框(System.inputString)
加载吉里吉里Z 仓库中随附的 Krkr2Compat 后即可使用。

## Layer.hint
可以用 TJS 实现。详情请参照[工具提示的显示方法](./tooltip.md)。

## Layer 类的 obsolete 方法
affineBlend/affinePile/blendRect/pileRect/stretchBlend/stretchPile 方法可以用如下 TJS 实现。

```
Layer.affineBlend = function(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, opa=255, type=stNearest) {
    this.operateAffine(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, omOpaque, opa, type);
};
Layer.affinePile = function(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, opa=255, type=stNearest) {
    this.operateAffine(src, sleft, stop, swidth, sheight, affine, A, B, C, D, E, F, omAuto, opa, type);
};
Layer.blendRect = function(dleft, dtop, src, sleft, stop, swidth, sheight, opa=255) {
    this.operateRect(dleft, dtop, src, sleft, stop, swidth, sheight, omOpaque, opa);
};
Layer.pileRect = function(dleft, dtop, src, sleft, stop, swidth, sheight, opa=255) {
    this.operateRect(dleft, dtop, src, sleft, stop, swidth, sheight, omAuto, opa);
};
Layer.stretchBlend = function(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, opa=255, type=stNearest) {
    this.operateStretch(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, omOpaque, opa, type);
};
Layer.stretchPile = function(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, opa=255, type=stNearest) {
    this.operateStretch(dleft, dtop, dwidth, dheight, src, sleft, stop, swidth, sheight, omAuto, opa, type);
};
```
