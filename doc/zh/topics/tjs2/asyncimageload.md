# 异步图像加载

标准图像加载在请求读取时会等待该读取完成后再继续处理，而异步加载可以在后台进行
图像读取的同时执行其他处理。  
因此，也可以做到让来自磁盘的读取这种较慢的处理不太被察觉。  

## 规格
* 异步读取使用 Bitmap.loadAsync(filename) 和 Bitmap.onLoaded(meta,async,error,message) 进行。
* 用 loadAsync 请求读取，用 onLoaded 接收读取完成。
* 是否正在异步读取可以用 Bitmap.loading 判断。
* 异步读取中，访问 Bitmap 的其他成员会抛出异常。
* loadAsync 的参数 filename 需要包含扩展名，与可以省略的 Layer.loadImages 不同，请注意。

### onLoaded 接收到的各个值 (meta,async,error,message) 分别如下
* meta : 与用 Layer.loadImages 的返回值能接收到的内容相同。标签信息的字典数组。
* async : 是否是通过异步读取的。如果已在缓存中，则在请求读取后直接通过 onLoaded 返回。
* error : 是否发生了读取错误。
* message : 错误消息。发生错误时，会传递错误消息。

读取到的图像可以通过 Layer.copyFromBitmapToMainImage(Bitmap) 从 Bitmap 复制到 Layer。  
虽说是复制，但在被更改之前是共享的，所以一瞬间就能完成。  
读取处理是异步的，因此在读取完成时，接收该图像的 Layer 可能已经被无效化。  
在 onLoaded 中访问其他对象时，最好确认它没有被无效化。  
或者，需要保证在 onLoaded 完成之前不会被无效化。  

## 示例脚本

```
/*
image0.png ～ image9.png を10回非同期で読み込む
*/
System.setArgument("-contfreq", 60);
System.graphicCacheLimit = 0;
// キャッシュが有効だと無意味なので画像キャッシュ切る

class Bitmap2Layer extends Bitmap {
	var target;
	var tag;
	function Bitmap2Layer(layer,filename) {
		super.Bitmap();
		this.target = layer;
		this.tag = filename;
	}
	function onLoaded(meta,async,error,message) {
		Debug.message("Exit load async:"+async+", error:"+error+", message:"+message);
		if( !error && isvalid(target) ) { // 非同期なので、既に無効化されいないことを確認する
			target.copyFromBitmapToMainImage(this);
			target.setSizeToImageSize();
		}
	}
};

class MainWindow extends Window {
	var base;
	var layer;
	var layermove;
	var addval;
	var bmps;

	function MainWindow( width, height ) {
		super.Window();
		setSize( width, height );
		setInnerSize( width, height );

		base = new Layer(this, null);
		base.setSize(width,height);
		base.setSizeToImageSize();
		base.name = "base";
		base.visible = true;
		add( base );

		layer = new Layer(this,base);
		layer.setSize(100,100);
		layer.setSizeToImageSize();
		layer.colorRect(0,0,100,100,0x00ff00,128);
		layer.visible = true;
		add( layer );

		layermove = new Layer(this,base);
		layermove.setSize(100,100);
		layermove.setPos(0,height-100);
		layermove.setSizeToImageSize();
		layermove.colorRect(0,0,100,100,0xff0000,128);
		layermove.drawText( 0, 40, "テスト文字列描画", 0xffffff );
		layermove.visible = true;
		add( layermove );

		bmps = new Array();
		for( var j = 0; j < 10; j++ ) {
		for( var i = 0; i < 10; i++ ) {
			var filename = "image"+i+".png";
			var bmp = new Bitmap2Layer(layer,filename);
			bmp.loadAsync(filename);
			bmps.add(bmp);
		}
		}
		add( bmps );

		addval = 1;
		System.addContinuousHandler(onMoveImage);
	}
	function finalize() {
		System.removeContinuousHandler(onMoveImage);
		super.finalize();
	}
	function onMoveImage() {
		layermove.left += addval;
		if( addval > 0 ) {
			if( layermove.left >= (this.width-layermove.width) ) {
				addval = -1;
			}
		} else {
			if( layermove.left <= 0 ) {
				addval = 1;
			}
		}
	}
};

var win = new MainWindow(640,480);
win.visible = true;
```

[与 GitHub 上的相同](https://github.com/krkrz/SampleScript/blob/master/asyncimageload/startup.tjs)
