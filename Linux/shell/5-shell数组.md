# Shell 数组

数组中可以存放多个值。 bash shell 只支持一维数组（不支持多维数组），初始化时不需要定义数组大小（与php类似）。
与大部分语言类似，数组元素的下标由0开始。
shell数组用括号来表示，元素用“空格”符号分隔开，语法格式如下：

`arrar_name=(vauel ... valuen)

**实例**

```sh
#!bin/bash

ma_array=(A B "C" D)
```

我们也可以用下标来定义数组：

```
array_name[0]=value0
array_name[1]=value1
array_name[2]=value2
```

**读取数组**
格式为：

`${array_name[index]}`

**实例**

```sh
#!/bin/bash

my_array=(A B "C" D)

echo "第一个元素为: ${my_array[0]}"
echo "第二个元素为: ${my_array[1]}"
echo "第三个元素为: ${my_array[2]}"
echo "第四个元素为: ${my_array[3]}"
```

执行脚本，结果为：

```
$ chmod +x test.sh
$ ./test.sh
第一个元素为: A
第二个元素为: B
第三个元素为: C
第四个元素为: D
```

## 获取数组中的所有元素

使用 @ 或 \* 可以获取数组中所有的元素：如：

```
my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组的元素为: ${my_array[*]}"
echo "数组的元素为: ${my_array[@]}"
```

执行脚本，结果为：

```
$ chmod +x test.sh
$ ./test.sh
数组的元素为: A B C D
数组的元素为: A B C D
```

## 获取数组的长度

获取数组长度方法与获取字符串长度的方法相同，如：

```sh
#!/bin/bash

my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组元素个数为: ${#my_array[*]}"
echo "数组元素个数为: ${#my_array[@]}"
```

执行脚本，结果为：

```
$ chmod +x test.sh 
$ ./test.sh
数组元素个数为: 4
数组元素个数为: 4
```




























































