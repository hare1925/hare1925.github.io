# css 创建

**当读到一个样式表时，浏览器会根据它来格式化html文档。**  

## 插入样式表的三种方式：

1. 外部样式表（external style sheet）
2. 内部样式表（Internal style sheet）
3. 内联样式（Inline style）

---

## 外部样式表

当需要应用很多页面时，外部样式表讲师理想的选择。  
在使用外部样式表的去哪个看下，你可以通过改变一个文件来改变整个站点的外观。  
每个页面使用<link>标签链接到样式表。  
<link>标签在（文档的）头部：  

```html
<head>
    <link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

浏览器会从文件 mystyle.css 中读取到样式声明，并根据它来格式文档。  
外部样式表可以在任何文本编辑器中进行编辑。文件不能包含任何的 html 标签。样式表应该以 .css 扩展名进行保存。  
例如：  

```css
ht{color: sienna;}
p{margin-left: 20px;}
body{background-image: url("/images/back40.gif");}
```

**Tips: 不要在属性值与单位之间留有空格（如："margin-left: 20 px"）,正确的写法是"margin-left: 20px"**  

---

## 内部样式表

当单个文档需要特殊的样式时，就应该使用内部样式表。  
可以使用`<style>`标签在文档头部定义头部样式表。例如：  

```html
<head>
    <style>
        hr{color: sienna;}
        p{margin-left: 20px;}
        body{background-image: url("images/back40.gif");}
    </style>
</head>
```

---

## 内联样式

由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优点。慎用这种方法，例如当样式仅需要在一个元素上应用一次时。  
要使用内联样式，需要在相关的标签内使用样式（style）属性。style属性可以包含任何 CSS 属性。  
例如：改变锻炼的颜色和左外边距：  

`<p style="color:sienna; margin-lesf: 20px;">这是一个锻炼。</p>`  

---

## 多种样式

如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被集成过来。  

例如：外部样式表用友针对 h3 选择器的三个属性：  

```css
h3
{
    color: red;
    text-align: left;
    font-size: 8pt;
}
```

而内部样式表用友针对 h3 选择器的两个属性：

```css
h3{
    text-align: right;
    font-size: 20pt;
}
```

加入用友内部样式表的这个页面同时与外部演示表链接，那么 h3 得到的样式是：  

```css
color: red;
text-align:right;
font-size: 20pt;
```

即颜色属性将被继承于外部样式表，
文字排列（text-alignment）和字体尺寸（font-size）会被内部样式表中的规则取代。  

---

## 多重样式表优先级  

样式表允许以多种方式规定样式信息。  
样式可以规定在单个的 html 元素中，在html页的头元素中，或在一个外部的CSS文件中。  
真挚与可以在同一个html文档内部引用多个外部样式表。  
一般情况，优先级如下：  
**（内联样式）Inline Style > （内部样式）Internal style sheet > （外部样式）External style sheet >浏览器默认样式**  

```html
<head>
    <!-- 外部样式 style.css -->
    <link rel="stylesheet" type="text/css" href="style.css">
    <!-- 设置： h3{color: blue;} -->
    <style type="text/css">
        /* 内部样式 */
        h3{color: green;}
    </style>
</head>
<body>
    <h3>测试！</h3>
</body>
```

**Tips: 如果外部样式表放在内部样式表的后面，则外部样式表将覆盖内部样式表。**