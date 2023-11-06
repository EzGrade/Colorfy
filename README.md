# Main Functions
## Text and Background painting
```Colorfy.paint(color=Colorfy.Hints.Color, background: bool)```

Paints text or background(if background = True) due to color arg. To ```color``` you can pass color name(like ```"blue"```), ```Colorfy.Hints.Color``` or ascii escape code. ```background: bool``` to paint background.

---
## Text Style
```Colorfy.style(style=Colorfy.Hints.Style)```

Formats text due to style param. To style you can pass style name(such as ```"italic"```) or ```Colorfy.Hints.Style```.

---
## Help
You can easily call ```Colorfy.help()``` to see all available colors and styles. Can be pass ```visualise: bool``` to see how different colors or styles will look like, ```mix: bool``` to see how different color will look like with different styles(pairs created randomly).
