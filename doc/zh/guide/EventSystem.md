# 事件系统

## 关于事件系统

用吉里吉里编写 TJS 脚本时，必须采用事件驱动型的编程模型。

事件是在“发生了某件事”时，为了向其他对象或自己的对象内通知该事而发生的。在事件处理器中要编写响应它的处理。

在吉里吉里中，一个事件处理器花费不必要的长时间并不好。希望等待一段时间时，建议使用 [Timer](../reference/Timer.md) 类。

## 同步事件与异步事件

同步事件是指，例如在声音缓冲区中开始播放时，在 play 方法内发生 onStatusChanged 事件那样，对对象进行操作后立即当场发生的事件。

与此相对，异步事件会暂时积存在吉里吉里内部的事件队列 ( 存放即将发生的事件的地方 ) 中。此类事件在所有其他事件处理器的处理结束之前不会发生，也不会在其他事件处理器内发生 ( 不过存在例外，请参阅下面的 Note )。计时器周期到来时发生的 onTimer 事件，以及由用户输入发生的所有事件，都是异步事件。

> **Note:**
> 像 Window.showModal 这样一部分试图获取用户输入的功能，可能会驱动事件队列 ( 分发事件 )。因此，在事件处理器中可能会发生其他异步事件。

为了通过脚本操作发生异步事件，提供了 [AsyncTrigger](../reference/AsyncTrigger.md) 类。

## 反映到画面的时机

将图层显示到窗口时反映到画面的时机与异步事件相同，是在所有其他事件处理器的处理结束之后。在一个事件处理器内无论绘制多少次，虽然已经绘制到内部的图像缓冲区中，但不会立即反映到画面上。只有从事件处理器出来、吉里吉里获得绘制时机时，内容才会被绘制并反映到窗口上。

## 类内的事件处理器

在类内发生的事件，可以通过在该类内重写超类的事件处理器来进行处理。

例如，可以从 Timer 类创建子类，如下所示创建事件处理器。

```
class MyTimer extends Timer
{
	function MyTimer()
	{
		super.Timer(...);
	}

	function onTimer()
	{
		// ( ここに onTimer の処理 )
		super.onTimer(...); // スーパークラスのメソッドは一応呼び出す
	}
}
```

超类的方法并不需要调用，但一般会调用。另外，如果不调用超类的方法，就无法通过后述的 action 方法进行事件处理。

## action 方法

[Layer](../reference/Layer.md) 类和 [WaveSoundBuffer](../reference/WaveSoundBuffer.md) 类等具有向构造函数中指定的 owner 的 action 方法发生事件的功能。

action 方法会接收一个字典数组对象的参数，事件的信息就在其中。

在字典数组的成员中，target 表示事件的产生源对象。type 表示事件名。

其他成员因事件而异。例如，[Layer.onClick](../reference/Layer.md#onclick) 事件则有 x 和 y 这两个成员，表示图层上被点击的位置。

```
例:
class MyWindow extends Window
{
	var layer;
	(略)
	function MyWindow()
	{
		super.Window(...);
		add(layer = new Layer(this /* this = オーナー */, null));
		layer.visible = true;
	}
	(略)
	function action(ev)
	{
		if(ev.type == "onClick" && ev.target == layer)
		{
			// layer がクリックされた
			System.inform(ev.x, ev.y);
		}
	}
}
```
