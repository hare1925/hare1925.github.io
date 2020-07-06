# CSS id 和 class 选择器

- 想要在html元素中设置css样式，需要在元素中设置“id”和“class”选择器。

---

## id 选择器

- id 选择器可以为标有特定 id 的 html 元素指定特定的样式。
- html 元素以 id 属性来设置 id 选择器 .CSS 中 id 选择器以 “#”来定义。
- 例如： id="para1"

```css
#para1{
    color: red;
}
```

- ps. ID属性不要以数字开头，数字开头的ID在 mozilla/firefox 浏览器中不起作用。


---

## class 选择器

- class 选择器用于描述一组元素的样式，clss选择器有别于 id 选择器， class 选择器可以在多个元素中使用。
- class 选择器在 html 中以 class 属性表示，在CSS中，选择器以一个点"."号显示：
- 例如：所有 center 类的 html 元素设置为居中。

```css
.center{
    text-align: center;
}
```

- 也可以指定特定的标签使用class选择器
    - 只有是p标签并且class是.center的class才会被选中

```css
p.center{
    text-align: center;
}
```

*类名的第一个字母也不可以是数字！他在 Mozilla/Firefox 中不起作用*