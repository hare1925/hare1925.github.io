# CSS 背景

CSS背景属性用于定义html元素的背景。  
CSS属性定义北京效果：  
- background-color
- background-image
- background-repeat
- background-attachment
- background-positions

---

## 背景颜色

background-color属性定义了元素的背景颜色  
例如：在body的选择器中使用如下：  
```css
body{background-color: #f7f7f7;}
```

**CSS中，颜色值通常使用以下方式定义：**  
1. 十六进制 - 如：“#ff0000”
2. RGB - 如：“rgb(255,0,0)”
3. 颜色名称 - 如：“red”

---

## 背景图像

background-image 属性描述了元素的背景图像  
默认情况下，背景图像进行平铺重复显示，以覆盖整个元素实体  
例如:  
```CSS
body{background-image: url('paper.gif');}
```

---

## 背景图像-水平或垂直平铺

默认情况下 background-image 属性会在页面的水平或垂直方向平铺。  
例如：图像只在水平方向平铺(repeat-x)：  
```css
body{
    background-image: url('gradient2.png');
    background-repeat: repeat-x;
}
```

- 水平平铺：repeat-x
- 垂直平涂：repeat-y
- 不平铺：no-repeat

--- 

## 背景图像-设置定位与不平铺

**让背景图像不影响文本的排版**  
background-positions属性改变图像在背景中的位置：  
```css
body{
    background-image: url('img_tree.png');
    background-repeat: no-repeat;
    background-positions: right top;
}
```

positions的参数为两个：  
- 第一个为x轴参数，分别为：
    - left
    - center
    - right
- 第二个为y轴参数，分别为：
    - top
    - center
    - bottom

当只有一个参数时，第二个参数默认为 center

[position详解](https://www.runoob.com/cssref/pr-background-position.html)

---

## 背景-简写属性

在前面了解了页面的背景颜色通过很多的属性来控制。  
为了简化这些属性的代码，可以将这些属性合并在同一个属性中。  
背景简写案例：  
```css
body{background: #ffffff url('img_tree.png') no-repeat right top;}
```

**当使用简写属性时，属性值的顺序为：**
- background-color
- background-image
- background-repeat
- background-attachment
- background-position

以上属性无需全部使用，可以按照页面的市级需要使用。