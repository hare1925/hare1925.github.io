# shell流程控制

和java、php等语言一样，sh的流程控制不可为空，如（以下为php流程控制写法）：

```php
<?php
if (isset($_GET["q"])) {
    search(q);
}
else {
    // 不做任何事情
}
```

在sh/bash里可不能这么写，如果else分支没有语句执行，就不要写这个else。

## if else

if 语法格式：

```sh
if condition
then
    command1
    command2
    ...
    commandN
fi
```

写成一行（适用于终端命令提示符）：

`if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true";fi`

末尾的fi就是if倒过来拼写。

**if else**

if else语法格式：

```sh
if condition
then
    command1
    command2
    ...
    commandN
else
    command
fi
```

**if else-if slse**

if esle-if else语法格式：

```sh
if condition1
then
    command1
elif condition2
then
    command2
else
    commandN
fi
```

下面实例判断两个变量是否相等：

```sh
a=10
b=20
if [ $a == $b ]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi
```

输出结果：

`a 小于 b`

if else语句经常与test命令结合使用，如：

```sh
num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo '两个数字相等!'
else
    echo '两个数字不相等!'
fi
```

结果为：

`两个数字相等!`

## for循环

与其他变成语言类似，shell支持for循环。

for循环一般格式为：

```sh
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done
```

写成一行：

`for var in item1 item2 ... itemN; do command; command2... done;`

当变量值在列表里，for循环即执行一次所有命令，使用变量名获取列表中的当前取值。命令可为任何有效的shell命令和语句。in列表可以包含替换、字符串和文件名。

in列表是可选的，如果不用它，for循环使用命令行的位置参数。

例如，顺序输出当前列表中的数字：

```sh
for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done
```

输出结果：

```
The value is: 1
The value is: 2
The value is: 3
The value is: 4
The value is: 5
```

顺序输出字符串中的字符：

```
for str in 'This is a string'
do
    echo $str
done
```

输出结果：

`This is a string`

## while 语句

while循环用于不断执行一系列命令，也用于从输入文件中读取数据；命令通常为测试条件。其格式为：

```sh
while condition
do
    command
done
```

以下是一个基本的while循环，测试条件是：如果int小于等于5，那么条件返回真。int从0开始，每次循环处理时，int加1。运行上述脚本，返回数字1到5，然后终止。

```sh
#!/bin/bash
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
```

运行脚本，结果为：

```
1
2
3
4
5
```

以上实例使用了 Bash let 命令，它用于执行一个或多个表达式，变量计算中不需要加上 $ 来表示变量。
while循环可用于读取键盘信息。下面的例子中，输入信息被设置为变量FILM，按<Ctrl-D>结束循环。

```sh
echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
    echo "是的！$FILM 是一个好网站"
done
```

运行脚本，输出：

```sh
按下 <CTRL-D> 退出
输入你最喜欢的网站名:hare
是的！hare 是一个好网站
```

## 无限循环






