# python的非正式介绍

- 交互模式通过提示符（>>>和...）的出现与否来区分输入和输出。有的就是输入，没有的就是输出。
需要注意的是，某行中出现第二个提示符意味着必须键入一个空白行；这是用来结束多行命令的。

- python中的注释以`#`开头，并一直延伸到本行结束为止。
注释可以出现在一行的开头或空白和代码的后边，但是不能出现在字符串中间。字符串中的#就是#。
注释时为了阐明代码，不会被python解释（就是会在执行的时候被忽略）。

---

## 3.1 Python作为计算器使用

### 3.1.1 数字

- 表达式的语法很简单`+、-、*、/`，还有括`()`号用来分组。

- 整数有`int`类型
- 小数有`float`类型
- 除法运算`/`永远返回浮点数类型。
- 地板除`//`返回整数，小数部分忽略。
- 计算余数`%`
- 幂运算`**`
- `=`用来给变量赋值，例如

```py
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

如果使用一个没有被定义（赋值）的变量，会报错。

- 多种混合类型运算数的运算，返回结果为浮点数。因为python提供浮点数的完整支持。

- 在交互模式下，上一次打印出来的表达式被赋值给变量`_`。
    这意味着把python当计算器用的时候，继续计算会比较简单。
例如：

```py
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

**注**：这个变量应该被当做是只读变量。不要向它显式的赋值——你会创建和它名字相同独立的本地变量，他会使用魔法行为屏蔽内部变量。

除了 int 和 float ，python也支持其他的数字类型，例如 Decimal 或者 Fraction。python也内置对 复数 的支持，使用后缀j或者J就可以表示虚数部分（例如 3+5j）。

---

### 3.1.2 字符串

- 字符串有多种形式。可以用单引号或双引号来包含字符串。`\`可以用来转义。

```py
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

- 如果不想用`\`转义，在字符串引号前加`r`即可。

```py
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

- 字符串跨行连续输入。一种方式是三重引号：`"""..."""` 或 `'''...'''`。字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 `\` 即可。如下例:

```py
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
----------------------------------
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

**注意**：最上面的换行符没有包括进来。

- 字符串 + 运算。 —— 连接字符串（中间不会有空格，除非字符串引号中有）。
- 字符串 * 运算。 —— 重复字符串（只能是字符串和数字相乘）。

- 相邻的两个或多个字符串面值（引号引起来的字符）将会自动连接到一起。

```py
>>> 'Py' 'thon'
'Python'
```

- 很长的字符串可以拆开分别输入，很有用的：

```py
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

**注意**只能对字面值这样操作，变量和表达式不行。

- 如果想要连接变量，或连接变量和字面值，可以用`+`号：

```py
>>> prefix = 'Py'
>>> prefix + 'thon'
'Python'
```

- 字符串是可以被索引的（下标访问），第一个字符索引是0.单个字符并没有特殊的类型，只是一个长度为一的字符串：

```py
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```

- 索引也可以倒着数。从右往左：

```py
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
```

**注意**：-0和0是一样的，所以复数索引从-1开始数。

- 切片：除了索引，字符串可以切片。索引是得到单个字符，切片可以获取子字符串：

```py
>>> word = 'Python'
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

**注意**切片的开始总是被包括在结果中，而结束不被包括。这使得`s[:i] + s[i:]`总是等于s。

```py
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

- 切片的索引默认值：省略开始索引时默认为0，省略结束索引时默认到字符串结束。

- 理解切片的另一张方式：
将索引视作指向字符之间，第一个字符的左侧标为0，最后一个字符的右侧标为n，其中n是字符串长度。如：

```py
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

第一行标注了字符串非负的索引的位置
第二行标注了对应的负的索引。
那么从i到j的切片就标有i和j的位置之间的所有字符。

对于使用负索引的切片，如果索引不越界，那么得到的切片长度就是起止索引之差。例如，word[1:3]的长度为2。

- 使用过大的索引，会报错：

```py
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

- 但是，切片中的越界索引会被自动处理：

```py
>>> word[4:42]
'on'
>>> word[42:]
''
```

- python中的字符串不能被修改，他们是 immutable 的。因此，向字符串的某个索引位置赋值会产生错误：

```py
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
**so**如果需要一个不同的字符串，新建一个就好了。

```py
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```

- 内建函数 len() 返回一个字符串的长度：

```py
>>> s = 'woyidingyaochibaomihua'
>>> len(s)
22
```

更多部分读：
```
参见
文本序列类型 --- str
字符串是一种 序列类型 ，因此也支持序列类型的各种操作。

字符串的方法
字符串支持许多变换和查找的方法。

格式化字符串字面值
内嵌表达式的字符串字面值。

格式字符串语法
使用 str.format() 进行字符串格式化。

printf 风格的字符串格式化
这里详述了使用 % 运算符进行字符串格式化。
```

---

### 3.1.3 列表

Python中可以通过组合一些值得到多种**复合**数据类型。

其中最常用的**列表**，可以通过方括号、逗号分隔的一组值得到。

一个列表可以包含不同类型的元素，但通常使用时哥哥元素类型相同：

```py
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

- 列表支持索引和切片。
和字符串（一级各种内置 sequence 类型）一样。

```py
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:
某度的翻译-所有切片操作都返回包含请求元素的新列表。这意味着以下切片将返回列表的新（浅层）副本：

```py
>>> squares[:]
[1, 4, 9, 16, 25]
```

- 列表支持拼接操作：

```py
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

- 与 immutable 的字符串不同, 列表是一个 mutable 类型，就是说，它自己的内容可以改变:
简单点说就是列表跟上面的字符不一样，这个是可以改变索引或切片的值的

```py
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

- 可以在列表结尾，通过 append() 方法添加新元素（后面再学）：

```py
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```

- 可以给切片赋值，这样甚至可以改变列表大小，或者把列表整个清空：

```py
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

- 内置函数len()也可以作用到列表上：

```py
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

- 也可以嵌套列表（创建包含其他列表的列表),例如：

```py
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

---

## 3.2 走向编程的第一步

当然，我们可以将 Python 用于更复杂的任务，而不是仅仅两个和两个一起添加。 例如，我们可以编写 斐波那契数列 的初始子序列，如下所示:

```py
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
```

这个例子引入了几个新的特点。

- 第一行含有一个 多重赋值: 变量 a 和 b 同时得到了新值 0 和 1. 最后一行又用了一次多重赋值, 这体现出了右手边的表达式，在任何赋值发生之前就被求值了。右手边的表达式是从左到右被求值的。

- while 循环只要它的条件（这里指： a < 10）保持为真就会一直执行。Python 和 C 一样，任何非零整数都为真；零为假。这个条件也可以是字符串或是列表的值，事实上任何序列都可以；长度非零就为真，空序列就为假。在这个例子里，判断条件是一个简单的比较。标准的比较操作符的写法和 C 语言里是一样： < （小于）、 > （大于）、 == （等于）、 <= （小于或等于)、 >= （大于或等于）以及 != （不等于）。

- 循环体 是 缩进的 ：缩进是 Python 组织语句的方式。在交互式命令行里，你得给每个缩进的行敲下 Tab 键或者（多个）空格键。实际上用文本编辑器的话，你要准备更复杂的输入方式；所有像样的文本编辑器都有自动缩进的设置。交互式命令行里，当一个组合的语句输入时, 需要在最后敲一个空白行表示完成（因为语法分析器猜不出来你什么时候打的是最后一行）。注意，在同一块语句中的每一行，都要缩进相同的长度。

- print() 函数将所有传进来的参数值打印出来. 它和直接输入你要显示的表达式(比如我们之前在计算器的例子里做的)不一样， print() 能处理多个参数，包括浮点数，字符串。 字符串会打印不带引号的内容, 并且在参数项之间会插入一个空格, 这样你就可以很好的把东西格式化, 像这样:

```py
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
```

关键字参数 end 可以用来取消输出后面的换行, 或是用另外一个字符串来结尾:

```py
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```





