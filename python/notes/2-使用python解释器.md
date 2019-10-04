# 使用python解释器

## 调用解释器

在linux系统中，只要安装了python，直接在terminal输入python就好啦。
```
> python                                                  21:27:55
Python 3.7.4 (default, Jul 16 2019, 07:12:58)
[GCC 9.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

## 传入参数

没搞明白

## 交互模式

上面的代码就是交互模式的界面喽！ ↑↑↑

---

# 解释器的运行环境

## 源文件的字符编码

python默认时utf-8编码。

世界上大多数语言的字符都可以同时用于字符串面值、变量或函数名称一级注释中——尽管标准库中只用常规的ascii字符作为变量或函数名，而且任何可移植的代码都应该遵守此约定。

想要正确显示这些字符，编辑器必须能识别utf-8编码，而且必须使用能支持打开的文件中所有字符的字体。

如果不使用默认编码，需要声明一下，方法就是在文件的第一行写成注释，如下：

`# -*- coding: encoding -*-`

这个encoding可以时python支持的任意一种编码（codecs）。

例如，用windows-1252编码，要写成：

`# -*- coding: cp1252 -*-`

**例外**

第一行规则的一种例外情况就是，源码以UNIX "shebang" 行开头。这种情况，编码声明就要写在文件的第二行。例如：

```py
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

附： 在unix系统中。python3.x解释器默认安装后的执行文件并不叫python，这样才不会与同时安装python2.x冲突。































