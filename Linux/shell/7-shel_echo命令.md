# sehll echo 命令

shell的echo指令与php的echo指令类似，都是用于字符串的输出。
命令格式为：

`echo string`

您可以使用echo实现更复杂的输出格式控制。

## 1.显示普通字符：

`echo "It is a test"`

这里的双引号完全可以省略，以下命令与上面实例效果一致：

`echo It is a test`

## 2.显示转义字符

`echo "\" It is a test\""`

结果将是:

`"It is a test"`

同样，双引号可以省略

## 3.显示变量

read命令从标准输入中读取一行，并把输入行的每个字段的值指定给shell变量

```sh
#!/bin/bash
read name
echo "$name It is a test"
```

以上代码保存为 test.sh ， name接收标准输入的变量，结果将是：

```sh
[root@www ~]# sh test.sh
OK          #标准输入
OK          #输出
```

## 4.显示换行

```sh
echo -e "OK! \n"        # -e 开启转义
echo "It is a test"
```

输出结果：

```
OK
It is a test
```

## 5.显示不换行

```sh
#!/bin/bash
echo -e "OK! \c"        #-e 开启转义 \c 不换行
echo "It is a test"
```

输出结果：

`OK! It is a test`

## 6.显示结果定向至文件

`OK! It is a test" > myfile`

## 7.原样输出字符串，不进行转义或取变量（用单引号）

`echo '$name\"'`

输出结果：

`$name\"`

## 8.显示命令执行结果

`echo \`date\``

**注意**:这里使用的反引号`\``,而不是单引号`'`。
结果将显示当前日期

`Thu Jul 24 17:00:34 CST 2019`












