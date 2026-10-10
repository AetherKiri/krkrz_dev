# 视频的播放方法

吉里吉里Z TJS2 的示例脚本。
以 mixer(VMR9) 模式播放视频。
在最前面播放视频时，这种方法是标准方法。


```
class MainWindow extends Window {
	var video;
	function MainWindow( width, height ) {
		super.Window();
		video = new VideoOverlay(this);
		video.mode = vomMixer;
		video.open("test.mpg");
		setInnerSize( video.originalWidth, video.originalHeight );
		video.play();
		video.width = video.originalWidth;
		video.height = video.originalHeight;
		video.visible = true;
		add( video );
	}
};
var win = new MainWindow(640,480);
win.visible = true;

```


