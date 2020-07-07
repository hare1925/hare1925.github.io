# css text(文本)

## 文本颜色

颜色属性被用来设置文字的颜色。  
颜色是通过css最常用的指定：
- 十六进制：#ff0000
- 一个RGB值：RGB(255,0,0)
- 颜色的名称：red

实例：
```css
body{color: red;}
h1{color: #00ff00;}
h2{color: rgb(255,0,0);}
```

**A Tip:对于W3C标准的CSS：如果定义了颜色属性，还必须定义背景色属性。**  

---

## 文本的对齐方式

文本排列属性是用来设置文本的水平对齐方式。  
文本可居中或对齐到左或右，两段对齐。  
当 text-align 设置为“justify”，每一行被展开为宽度相等，左右外边距是对齐（两端对齐）。  

```css
h1{text-align: center;}
p.data{text-align: right;}
p.main{text-align: justify;}
```

---

## 文本修饰

text-decoration属性用来设置或删除文本的装饰。  
从设计的角度看 text-decoration属性主要是用来删除链接的下划线： 

```css
a{text-decoration: none;}
h1{text-decoration: overline;}
h2{text-decoration: line-through;}
h3{text-decoration: underline;}
```

**A Tip: 不建议强调指出不是链接的文本，因为这常常混淆用户。**  

---

## 文本转换

文本转换属性是用来指定在一个文本中的大写和小写字母。  
可用于所有子句编程大写或小写字母，或每个单词的首字母大写。  

```css
p.uppercase{text-transform: uppercase;}
p.lowercase{text-transform: lowercase;}
p.capitalize{text-transform: capitalize;}
```

---

## 文本缩进

文本缩进属性是用来指定文本的第一行的缩进。  

```css
p{text-indent: 50px;}
```
