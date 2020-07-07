# css 表格

css可以使用html表格更美观。  

---

## 表格边框

指定css表格边框，使用 border 属性。  
下面的例子指定了一个表格 th 和 td 元素的黑色边框：  

```css
table, th, td{
    border: 1px solid black;
}
```

注意，在上例子中的表格有双边框。这是因为表和 th/td 元素有独立的边界。  
为了显示一个表的单个边框，使用 border-collapse 属性。  

---

## 折叠边框  

border-collapse 属性设置表格的边框是否被折叠成一个单一的边框或隔开：  
```css
table{
    border-collapse: collapse;
}
table, th, td{
    border: 1px solid black;
}
```

---

## 表格宽度和高度

width 和 height 属性定义表格的宽度和高度。  
下例是设置100%的宽度，50夏素的th元素高度的表格：  
```css
table{
    width: 100%;
}
th{
    height: 50px;
}
```

---

## 表格文字对齐

表格中的文本对齐和垂直对齐属性。  
text-align属性设置水平对齐方式，向左，右，或居中：  
```css
td{
    text-align: right;
}
```

垂直对齐属性设置垂直对齐，例如顶部，底部或中间：  
```css
td{
    heigth: 50px;
    vertical-align: bottom;
}
```

---

## 表格填充

如果在表的内容中控制空格之间的边框，应该用 td 和 th 云阿瑟的填充属性：  
```css
td{
    padding: 15px;
}
```

---

## 表格颜色

下例指定边框的颜色，和 th 元素的文本和背景颜色：  

```css
table, td, th{
    border: 1px solid green;
}
th{
    background-color: green;
    color: white;
}
```
