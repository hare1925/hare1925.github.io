# python 学习笔记

学习网址： https://docs.python.org/zh-cn/3/

PyInstaller墙内地址： https://pypi.douban.com/simple/
`sudo pip install -i https://pypi.douban.com/simple/`  
万恶的GFW，麻痹...

- 运行exe文件的时候，会弹出一个dos命令窗口，这个窗口可以看到一些打印信息，如果想只运行tkinter 页面，去掉dos窗口需要在打包的时候 加上 -w 参数

`eg.   pyinstaller -F XX.py -w`

