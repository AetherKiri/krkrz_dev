# GdiPlus

该类由多个插件扩展。

## 插件扩展: layerExDraw

基于伪代码的手册

### 成员列表

#### 方法

- [addPrivateFont](#addprivatefont)
- [getFontList](#getfontlist)

#### 常量

- [Ok](#ok)
- [GenericError](#genericerror)
- [InvalidParameter](#invalidparameter)
- [OutOfMemory](#outofmemory)
- [ObjectBusy](#objectbusy)
- [InsufficientBuffer](#insufficientbuffer)
- [NotImplemented](#notimplemented)
- [Win32Error](#win32error)
- [WrongState](#wrongstate)
- [Aborted](#aborted)
- [FileNotFound](#filenotfound)
- [ValueOverflow](#valueoverflow)
- [AccessDenied](#accessdenied)
- [UnknownImageFormat](#unknownimageformat)
- [FontFamilyNotFound](#fontfamilynotfound)
- [FontStyleNotFound](#fontstylenotfound)
- [NotTrueTypeFont](#nottruetypefont)
- [UnsupportedGdiplusVersion](#unsupportedgdiplusversion)
- [GdiplusNotInitialized](#gdiplusnotinitialized)
- [PropertyNotFound](#propertynotfound)
- [PropertyNotSupported](#propertynotsupported)
- [ProfileNotFound](#profilenotfound)
- [FontStyleRegular](#fontstyleregular)
- [FontStyleBold](#fontstylebold)
- [FontStyleItalic](#fontstyleitalic)
- [FontStyleBoldItalic](#fontstylebolditalic)
- [FontStyleUnderline](#fontstyleunderline)
- [FontStyleStrikeout](#fontstylestrikeout)
- [BrushTypeSolidColor](#brushtypesolidcolor)
- [BrushTypeHatchFill](#brushtypehatchfill)
- [BrushTypeTextureFill](#brushtypetexturefill)
- [BrushTypePathGradient](#brushtypepathgradient)
- [BrushTypeLinearGradient](#brushtypelineargradient)
- [DashCapFlat](#dashcapflat)
- [DashCapRound](#dashcapround)
- [DashCapTriangle](#dashcaptriangle)
- [DashStyleSolid](#dashstylesolid)
- [DashStyleDash](#dashstyledash)
- [DashStyleDot](#dashstyledot)
- [DashStyleDashDot](#dashstyledashdot)
- [DashStyleDashDotDot](#dashstyledashdotdot)
- [HatchStyleHorizontal](#hatchstylehorizontal)
- [HatchStyleVertical](#hatchstylevertical)
- [HatchStyleForwardDiagonal](#hatchstyleforwarddiagonal)
- [HatchStyleBackwardDiagonal](#hatchstylebackwarddiagonal)
- [HatchStyleCross](#hatchstylecross)
- [HatchStyleDiagonalCross](#hatchstylediagonalcross)
- [HatchStyle05Percent](#hatchstyle05percent)
- [HatchStyle10Percent](#hatchstyle10percent)
- [HatchStyle20Percent](#hatchstyle20percent)
- [HatchStyle25Percent](#hatchstyle25percent)
- [HatchStyle30Percent](#hatchstyle30percent)
- [HatchStyle40Percent](#hatchstyle40percent)
- [HatchStyle50Percent](#hatchstyle50percent)
- [HatchStyle60Percent](#hatchstyle60percent)
- [HatchStyle70Percent](#hatchstyle70percent)
- [HatchStyle75Percent](#hatchstyle75percent)
- [HatchStyle80Percent](#hatchstyle80percent)
- [HatchStyle90Percent](#hatchstyle90percent)
- [HatchStyleLightDownwardDiagonal](#hatchstylelightdownwarddiagonal)
- [HatchStyleLightUpwardDiagonal](#hatchstylelightupwarddiagonal)
- [HatchStyleDarkDownwardDiagonal](#hatchstyledarkdownwarddiagonal)
- [HatchStyleDarkUpwardDiagonal](#hatchstyledarkupwarddiagonal)
- [HatchStyleWideDownwardDiagonal](#hatchstylewidedownwarddiagonal)
- [HatchStyleWideUpwardDiagonal](#hatchstylewideupwarddiagonal)
- [HatchStyleLightVertical](#hatchstylelightvertical)
- [HatchStyleLightHorizontal](#hatchstylelighthorizontal)
- [HatchStyleNarrowVertical](#hatchstylenarrowvertical)
- [HatchStyleNarrowHorizontal](#hatchstylenarrowhorizontal)
- [HatchStyleDarkVertical](#hatchstyledarkvertical)
- [HatchStyleDarkHorizontal](#hatchstyledarkhorizontal)
- [HatchStyleDashedDownwardDiagonal](#hatchstyledasheddownwarddiagonal)
- [HatchStyleDashedUpwardDiagonal](#hatchstyledashedupwarddiagonal)
- [HatchStyleDashedHorizontal](#hatchstyledashedhorizontal)
- [HatchStyleDashedVertical](#hatchstyledashedvertical)
- [HatchStyleSmallConfetti](#hatchstylesmallconfetti)
- [HatchStyleLargeConfetti](#hatchstylelargeconfetti)
- [HatchStyleZigZag](#hatchstylezigzag)
- [HatchStyleWave](#hatchstylewave)
- [HatchStyleDiagonalBrick](#hatchstylediagonalbrick)
- [HatchStyleHorizontalBrick](#hatchstylehorizontalbrick)
- [HatchStyleWeave](#hatchstyleweave)
- [HatchStylePlaid](#hatchstyleplaid)
- [HatchStyleDivot](#hatchstyledivot)
- [HatchStyleDottedGrid](#hatchstyledottedgrid)
- [HatchStyleDottedDiamond](#hatchstyledotteddiamond)
- [HatchStyleShingle](#hatchstyleshingle)
- [HatchStyleTrellis](#hatchstyletrellis)
- [HatchStyleSphere](#hatchstylesphere)
- [HatchStyleSmallGrid](#hatchstylesmallgrid)
- [HatchStyleSmallCheckerBoard](#hatchstylesmallcheckerboard)
- [HatchStyleLargeCheckerBoard](#hatchstylelargecheckerboard)
- [HatchStyleOutlinedDiamond](#hatchstyleoutlineddiamond)
- [HatchStyleSolidDiamond](#hatchstylesoliddiamond)
- [HatchStyleTotal](#hatchstyletotal)
- [HatchStyleLargeGrid](#hatchstylelargegrid)
- [HatchStyleMin](#hatchstylemin)
- [HatchStyleMax](#hatchstylemax)
- [LinearGradientModeHorizontal](#lineargradientmodehorizontal)
- [LinearGradientModeVertical](#lineargradientmodevertical)
- [LinearGradientModeForwardDiagonal](#lineargradientmodeforwarddiagonal)
- [LinearGradientModeBackwardDiagonal](#lineargradientmodebackwarddiagonal)
- [LineCapFlat](#linecapflat)
- [LineCapSquare](#linecapsquare)
- [LineCapRound](#linecapround)
- [LineCapTriangle](#linecaptriangle)
- [LineCapNoAnchor](#linecapnoanchor)
- [LineCapSquareAnchor](#linecapsquareanchor)
- [LineCapRoundAnchor](#linecaproundanchor)
- [LineCapDiamondAnchor](#linecapdiamondanchor)
- [LineCapArrowAnchor](#linecaparrowanchor)
- [LineJoinMiter](#linejoinmiter)
- [LineJoinBevel](#linejoinbevel)
- [LineJoinRound](#linejoinround)
- [LineJoinMiterClipped](#linejoinmiterclipped)
- [PenAlignmentCenter](#penalignmentcenter)
- [PenAlignmentInset](#penalignmentinset)
- [WrapModeTile](#wrapmodetile)
- [WrapModeTileFlipX](#wrapmodetileflipx)
- [WrapModeTileFlipY](#wrapmodetileflipy)
- [WrapModeTileFlipXY](#wrapmodetileflipxy)
- [WrapModeClamp](#wrapmodeclamp)
- [MatrixOrderPrepend](#matrixorderprepend)
- [MatrixOrderAppend](#matrixorderappend)
- [ImageTypeUnknown](#imagetypeunknown)
- [ImageTypeBitmap](#imagetypebitmap)
- [ImageTypeMetafile](#imagetypemetafile)
- [RotateNoneFlipNone](#rotatenoneflipnone)
- [Rotate90FlipNone](#rotate90flipnone)
- [Rotate180FlipNone](#rotate180flipnone)
- [Rotate270FlipNone](#rotate270flipnone)
- [RotateNoneFlipX](#rotatenoneflipx)
- [Rotate90FlipX](#rotate90flipx)
- [Rotate180FlipX](#rotate180flipx)
- [Rotate270FlipX](#rotate270flipx)
- [RotateNoneFlipY](#rotatenoneflipy)
- [Rotate90FlipY](#rotate90flipy)
- [Rotate180FlipY](#rotate180flipy)
- [Rotate270FlipY](#rotate270flipy)
- [RotateNoneFlipXY](#rotatenoneflipxy)
- [Rotate90FlipXY](#rotate90flipxy)
- [Rotate180FlipXY](#rotate180flipxy)
- [Rotate270FlipXY](#rotate270flipxy)
- [SmoothingModeInvalid](#smoothingmodeinvalid)
- [SmoothingModeDefault](#smoothingmodedefault)
- [SmoothingModeHighSpeed](#smoothingmodehighspeed)
- [SmoothingModeHighQuality](#smoothingmodehighquality)
- [SmoothingModeNone](#smoothingmodenone)
- [SmoothingModeAntiAlias](#smoothingmodeantialias)
- [TextRenderingHintSystemDefault](#textrenderinghintsystemdefault)
- [TextRenderingHintSingleBitPerPixelGridFit](#textrenderinghintsinglebitperpixelgridfit)
- [TextRenderingHintSingleBitPerPixel](#textrenderinghintsinglebitperpixel)
- [TextRenderingHintAntiAliasGridFit](#textrenderinghintantialiasgridfit)
- [TextRenderingHintAntiAlias](#textrenderinghintantialias)
- [TextRenderingHintClearTypeGridFit](#textrenderinghintcleartypegridfit)

---

### addPrivateFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `fontFileName` | `&nbsp;` | 字体文件名 |

**说明**

私有字体的添加 (static)

添加应用程序固有的字体。
也可以注册吉里吉里归档中的字体。

---

### getFontList

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `privateOnly` | `&nbsp;` | 为 true 时仅获取私有字体 |

**说明**

字体列表的获取

---

### Ok

常量

值: `0`

---

### GenericError

常量

值: `1`

---

### InvalidParameter

常量

值: `2`

---

### OutOfMemory

常量

值: `3`

---

### ObjectBusy

常量

值: `4`

---

### InsufficientBuffer

常量

值: `5`

---

### NotImplemented

常量

值: `6`

---

### Win32Error

常量

值: `7`

---

### WrongState

常量

值: `8`

---

### Aborted

常量

值: `9`

---

### FileNotFound

常量

值: `10`

---

### ValueOverflow

常量

值: `11`

---

### AccessDenied

常量

值: `12`

---

### UnknownImageFormat

常量

值: `13`

---

### FontFamilyNotFound

常量

值: `14`

---

### FontStyleNotFound

常量

值: `15`

---

### NotTrueTypeFont

常量

值: `16`

---

### UnsupportedGdiplusVersion

常量

值: `17`

---

### GdiplusNotInitialized

常量

值: `18`

---

### PropertyNotFound

常量

值: `19`

---

### PropertyNotSupported

常量

值: `20`

---

### ProfileNotFound

常量

值: `21`

---

### FontStyleRegular

常量

值: `0`

---

### FontStyleBold

常量

值: `1`

---

### FontStyleItalic

常量

值: `2`

---

### FontStyleBoldItalic

常量

值: `3`

---

### FontStyleUnderline

常量

值: `4`

---

### FontStyleStrikeout

常量

值: `8`

---

### BrushTypeSolidColor

常量

值: `0`

---

### BrushTypeHatchFill

常量

值: `1`

---

### BrushTypeTextureFill

常量

值: `2`

---

### BrushTypePathGradient

常量

值: `3`

---

### BrushTypeLinearGradient

常量

值: `4`

---

### DashCapFlat

常量

值: `0`

---

### DashCapRound

常量

值: `2`

---

### DashCapTriangle

常量

值: `3`

---

### DashStyleSolid

常量

值: `0`

---

### DashStyleDash

常量

值: `1`

---

### DashStyleDot

常量

值: `2`

---

### DashStyleDashDot

常量

值: `3`

---

### DashStyleDashDotDot

常量

值: `4`

---

### HatchStyleHorizontal

常量

值: `0`

---

### HatchStyleVertical

常量

值: `1`

---

### HatchStyleForwardDiagonal

常量

值: `2`

---

### HatchStyleBackwardDiagonal

常量

值: `3`

---

### HatchStyleCross

常量

值: `4`

---

### HatchStyleDiagonalCross

常量

值: `5`

---

### HatchStyle05Percent

常量

值: `6`

---

### HatchStyle10Percent

常量

值: `7`

---

### HatchStyle20Percent

常量

值: `8`

---

### HatchStyle25Percent

常量

值: `9`

---

### HatchStyle30Percent

常量

值: `10`

---

### HatchStyle40Percent

常量

值: `11`

---

### HatchStyle50Percent

常量

值: `12`

---

### HatchStyle60Percent

常量

值: `13`

---

### HatchStyle70Percent

常量

值: `14`

---

### HatchStyle75Percent

常量

值: `15`

---

### HatchStyle80Percent

常量

值: `16`

---

### HatchStyle90Percent

常量

值: `17`

---

### HatchStyleLightDownwardDiagonal

常量

值: `18`

---

### HatchStyleLightUpwardDiagonal

常量

值: `19`

---

### HatchStyleDarkDownwardDiagonal

常量

值: `20`

---

### HatchStyleDarkUpwardDiagonal

常量

值: `21`

---

### HatchStyleWideDownwardDiagonal

常量

值: `22`

---

### HatchStyleWideUpwardDiagonal

常量

值: `23`

---

### HatchStyleLightVertical

常量

值: `24`

---

### HatchStyleLightHorizontal

常量

值: `25`

---

### HatchStyleNarrowVertical

常量

值: `26`

---

### HatchStyleNarrowHorizontal

常量

值: `27`

---

### HatchStyleDarkVertical

常量

值: `28`

---

### HatchStyleDarkHorizontal

常量

值: `29`

---

### HatchStyleDashedDownwardDiagonal

常量

值: `30`

---

### HatchStyleDashedUpwardDiagonal

常量

值: `311`

---

### HatchStyleDashedHorizontal

常量

值: `32`

---

### HatchStyleDashedVertical

常量

值: `33`

---

### HatchStyleSmallConfetti

常量

值: `34`

---

### HatchStyleLargeConfetti

常量

值: `35`

---

### HatchStyleZigZag

常量

值: `36`

---

### HatchStyleWave

常量

值: `37`

---

### HatchStyleDiagonalBrick

常量

值: `38`

---

### HatchStyleHorizontalBrick

常量

值: `39`

---

### HatchStyleWeave

常量

值: `40`

---

### HatchStylePlaid

常量

值: `41`

---

### HatchStyleDivot

常量

值: `42`

---

### HatchStyleDottedGrid

常量

值: `43`

---

### HatchStyleDottedDiamond

常量

值: `44`

---

### HatchStyleShingle

常量

值: `45`

---

### HatchStyleTrellis

常量

值: `46`

---

### HatchStyleSphere

常量

值: `47`

---

### HatchStyleSmallGrid

常量

值: `48`

---

### HatchStyleSmallCheckerBoard

常量

值: `49`

---

### HatchStyleLargeCheckerBoard

常量

值: `50`

---

### HatchStyleOutlinedDiamond

常量

值: `51`

---

### HatchStyleSolidDiamond

常量

值: `52`

---

### HatchStyleTotal

常量

值: `53`

---

### HatchStyleLargeGrid

常量

值: `HatchStyleCross`

---

### HatchStyleMin

常量

值: `HatchStyleHorizontal`

---

### HatchStyleMax

常量

值: `HatchStyleTotal - 1`

---

### LinearGradientModeHorizontal

常量

值: `0`

**说明**

LinearGradientMode 定义

---

### LinearGradientModeVertical

常量

值: `1`

---

### LinearGradientModeForwardDiagonal

常量

值: `2`

---

### LinearGradientModeBackwardDiagonal

常量

值: `3`

---

### LineCapFlat

常量

值: `0`

---

### LineCapSquare

常量

值: `1`

---

### LineCapRound

常量

值: `2`

---

### LineCapTriangle

常量

值: `3`

---

### LineCapNoAnchor

常量

值: `0x10`

---

### LineCapSquareAnchor

常量

值: `0x11`

---

### LineCapRoundAnchor

常量

值: `0x12`

---

### LineCapDiamondAnchor

常量

值: `0x13`

---

### LineCapArrowAnchor

常量

值: `0x14`

---

### LineJoinMiter

常量

值: `0`

---

### LineJoinBevel

常量

值: `1`

---

### LineJoinRound

常量

值: `2`

---

### LineJoinMiterClipped

常量

值: `3`

---

### PenAlignmentCenter

常量

值: `0`

---

### PenAlignmentInset

常量

值: `1`

---

### WrapModeTile

常量

值: `0`

---

### WrapModeTileFlipX

常量

值: `1`

---

### WrapModeTileFlipY

常量

值: `2`

---

### WrapModeTileFlipXY

常量

值: `3`

---

### WrapModeClamp

常量

值: `4`

---

### MatrixOrderPrepend

常量

值: `0`

---

### MatrixOrderAppend

常量

值: `1`

---

### ImageTypeUnknown

常量

值: `0`

---

### ImageTypeBitmap

常量

值: `1`

---

### ImageTypeMetafile

常量

值: `2`

---

### RotateNoneFlipNone

常量

值: `0`

---

### Rotate90FlipNone

常量

值: `1`

---

### Rotate180FlipNone

常量

值: `2`

---

### Rotate270FlipNone

常量

值: `3`

---

### RotateNoneFlipX

常量

值: `4`

---

### Rotate90FlipX

常量

值: `5`

---

### Rotate180FlipX

常量

值: `6`

---

### Rotate270FlipX

常量

值: `7`

---

### RotateNoneFlipY

常量

值: `Rotate180FlipX`

---

### Rotate90FlipY

常量

值: `Rotate270FlipX`

---

### Rotate180FlipY

常量

值: `RotateNoneFlipX`

---

### Rotate270FlipY

常量

值: `Rotate90FlipX`

---

### RotateNoneFlipXY

常量

值: `Rotate180FlipNone`

---

### Rotate90FlipXY

常量

值: `Rotate270FlipNone`

---

### Rotate180FlipXY

常量

值: `RotateNoneFlipNone`

---

### Rotate270FlipXY

常量

值: `Rotate90FlipNone`

---

### SmoothingModeInvalid

常量

值: `-1`

**说明**

SmoothingMode 指定

---

### SmoothingModeDefault

常量

值: `0`

---

### SmoothingModeHighSpeed

常量

值: `1`

---

### SmoothingModeHighQuality

常量

值: `2`

---

### SmoothingModeNone

常量

值: `0`

---

### SmoothingModeAntiAlias

常量

值: `1`

---

### TextRenderingHintSystemDefault

常量

值: `0`

**说明**

TextRenderingHint 指定

---

### TextRenderingHintSingleBitPerPixelGridFit

常量

值: `1`

---

### TextRenderingHintSingleBitPerPixel

常量

值: `2`

---

### TextRenderingHintAntiAliasGridFit

常量

值: `3`

---

### TextRenderingHintAntiAlias

常量

值: `4`

---

### TextRenderingHintClearTypeGridFit

常量

值: `5`

---

## 插件扩展: layerExVector

基于伪代码的手册

基于 thorvg 的矢量绘制插件
这是用 thorvg 重新实现基于 GDI+ 的 LayerExDraw 的产物。
部分 GDI+ 固有功能已被移除。

### 成员列表

#### 方法

- [loadFont](#loadfont)
- [unloadFont](#unloadfont)

#### 常量

- [BrushTypeSolidColor](#brushtypesolidcolor)
- [BrushTypePathGradient](#brushtypepathgradient)
- [BrushTypeLinearGradient](#brushtypelineargradient)
- [LineCapFlat](#linecapflat)
- [LineCapSquare](#linecapsquare)
- [LineCapRound](#linecapround)
- [LineCapTriangle](#linecaptriangle)
- [LineJoinMiter](#linejoinmiter)
- [LineJoinBevel](#linejoinbevel)
- [LineJoinRound](#linejoinround)
- [LineJoinMiterClipped](#linejoinmiterclipped)
- [MatrixOrderPrepend](#matrixorderprepend)
- [MatrixOrderAppend](#matrixorderappend)

---

### loadFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `path` | `&nbsp;` |  |
| `name` | `void` |  |

---

### unloadFont

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `name` | `&nbsp;` |  |

---

### BrushTypeSolidColor

常量

值: `0`

---

### BrushTypePathGradient

常量

值: `3`

---

### BrushTypeLinearGradient

常量

值: `4`

---

### LineCapFlat

常量

值: `0`

---

### LineCapSquare

常量

值: `1`

---

### LineCapRound

常量

值: `2`

---

### LineCapTriangle

常量

值: `3`

---

### LineJoinMiter

常量

值: `0`

---

### LineJoinBevel

常量

值: `1`

---

### LineJoinRound

常量

值: `2`

---

### LineJoinMiterClipped

常量

值: `3`

---

### MatrixOrderPrepend

常量

值: `0`

---

### MatrixOrderAppend

常量

值: `1`

---
