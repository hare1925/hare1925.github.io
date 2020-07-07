# CSS 列表

CSS 列表属性作用如下：  
- 设置不同的列表项标记为有序列表
- 设置不同的列表项标记为无序列表
- 设置列表项标记为图像

---

## 列表

在 html 中，有两种类型的列表：  
- 有序列表，列表项标记用特殊图形（如小黑点、小方框等）
- 有序列表，列表项的标记有数字或字母

使用css，可以列出进一步的样式，并可用图像作为列表项标记。  

---

## 不同的列表项标记  

list-style-type 属性指定列表项标记的类型是：  

```css
ul.a{list-style-type: circle;}
ul.b{list-style-type: square;}

ol.c{list-style-type: upper-roman;}
ol.d{list-style-type: lower-alpha;}
```

一些值是无序列表，以及有些是有序列表。  

---

## 作为列表项标记的图像

要指定列表项标记的图像，使用列表样式图像属性：  

```css
ul{
    list-style-image: url('sqpurple.fig');
}
```

这个例子在所有浏览器中显示并不同， ie 和 opear 显示图像标记比火狐，chrom和safari更高一点点。  
如果想在所有浏览器放置相同的样式，就应该使用浏览器兼容性解决方案，过程如下：  

---

## 浏览器兼容性解决方案

同样在所有的浏览器，下面例子会显示的图像标记：  
```css
ul{
    list-style-type: none;
    padding: 0px;
    margin: 0px;
}
ul li{
    background-image: url('sqpurple.gif');
    background-repeat: no-repeat;
    background-position: 0px 5px;
    padding-left: 14px;
}
```

**解释：**  
- ul：
    - 设置列表类型为没有列表项标记
    - 设置填充和边距 0px（浏览器兼容性）
- ul中所有li：
    - 设置图像的 url，并设置它只显示一次（无重复）
    - 你需要的定位图像位置（左 0px 和 上下 5px）
    - 用 padding-left 属性吧文本置于列表中

---

## 列表-简写属性

在单个属性中指定所有的列表属性。这就是所谓的简写属性。  
为列表使用简写属性，例如：  
```css
ul{
    list-style: square url('sqpurple.gif');
}
```

可以按顺序设置如下属性：  
- list-style-type
- [list-style-position](https://www.runoob.com/cssref/pr-list-style-position.html)
- list-style-image

如果上述值丢失一个，其余仍在指定的顺序，就没有关系。  
