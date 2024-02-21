# describe
    一个简单的查看电脑性能的小工具

# operate
    长按鼠标右键 可以实现拖动
    双击鼠标右键 关闭程序
    双击鼠标左键 调整透明度; 透明度小于0时,自动结束程序

# bugs:
    打包成独立程序时, 会频繁的闪烁终端
    不知道为什么关闭程序之后,程序还是在后台运行; 但是把 widget.py 
    文件里的 Widget class 的 __init__ 函数的 
    self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool) 
    改成 self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)就不会出现这样的问题
    