# 工具提示的显示方法

工具提示是指鼠标悬停时显示的简单帮助。  
具体来说，是通过 Layer.hint 显示的内容。  
在吉里吉里内被称为提示（hint）。  
在吉里吉里2 中由 OS 的功能(严格来说是 VCL)显示，而在吉里吉里Z 中规格已改为显示任意图层。  
另外，在带有触摸屏的平板设备等上，鼠标悬停无法触发显示，因此需要能够用其他方式显示。  

## 规格
* 设置提示后，当光标停止一定时间、到达提示显示时机时，会触发 Window.onHintChanged(text:string,x:int,y:int,isshow:bool) 事件。  
* 光标停止时间可以通过 property:Window.hintDelay 指定。  
默认为 500 (msec)。  
以前是固定值，现在已可更改。  
* 绘制提示的图层要启用 property:Layer.ignoreHintSensing，使其忽略提示显示。
* 当 isshow 为 false 的事件到来时，将其隐藏。

这样，只要在 onHintChanged 中当 isshow 为 true 时把提示绘制到最前面的图层，并将提示图层设置为忽略鼠标消息，就能实现与以往相同的显示。  

以往只有标准的朴素显示，但通过允许在图层上任意绘制，不仅能使用文字，还能使用图像等进行显示。

## 示例
```
class MainWindow extends Window {
	var base;
	var layer;
	var hintlayer;

	function MainWindow( width, height ) {
		super.Window();
		setSize( width, height );
		setInnerSize( width, height );

		base = new Layer(this, null);
		base.setSize(width,height);
		base.setSizeToImageSize();
		base.name = "base";
		base.visible = true;

		layer = new Layer(this,base);
		layer.setPos(100,200);
		layer.setSize(100,100);
		layer.setSizeToImageSize();
		layer.colorRect(0,0,100,100,0xff0000,128);
		layer.drawText( 0, 40, "Draw Sample Text", 0xffffff );
		layer.hint = "Show Hint";
		layer.visible = true;

		// Hint Layer
		hintlayer = new Layer(this,base);
		hintlayer.visible = false;
		hintlayer.ignoreHintSensing = true;
		hintlayer.font.height = 14;
		hintlayer.hitThreshold = 256;

		// hintDelay = 500; // default
		// hintDelay = 0; // immediate
		// hintDelay = -1; // never
		// hintDelay = 1000; // slow
	}
	function onHintChanged(text,x,y,isshow) {
		if( isshow ) {
			var w = hintlayer.font.getTextWidth( text ) + 6;
			var h = hintlayer.font.getTextHeight( text ) + 4 + 4;
			hintlayer.setImageSize( w, h );
			hintlayer.setSizeToImageSize();

			if( (x+w) > innerWidth ) { x = innerWidth - w; }
			if( (y+h) > innerHeight ) { y = innerHeight - h; }
			hintlayer.setPos( x, y );

			hintlayer.fillRect( 0, 0, w, h, 0 );
			hintlayer.colorRect( 0, 0, w, h, clInfoBk, 196 );

			hintlayer.colorRect( 0, 0, 1, h, 0xFFFFFF );
			hintlayer.colorRect( 0, 0, w, 1, 0xFFFFFF );
			hintlayer.colorRect( w-1, 0, 1, h, 0xFFFFFF );
			hintlayer.colorRect( 0, h-1, w, 1, 0xFFFFFF );

			hintlayer.drawText( 2, 2, text, clInfoText, 220 );
			hintlayer.visible = true;
		} else {
			hintlayer.visible = false;
		}
	}
}
var win = new MainWindow(640,480);
win.visible = true;
```

[GitHub 上也有同样的示例。
](https://github.com/krkrz/SampleScript/blob/master/tooltip/startup.tjs)
