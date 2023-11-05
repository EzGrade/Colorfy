class Colorfy:
    def __init__(self, string=""):
        self.text = string
        self.effects = []
        self.hash_codes = {"black": "\u001b[{}0m",
                           "red": "\u001b[{}1m",
                           "green": "\u001b[{}2m",
                           "yellow": "\u001b[{}3m",
                           "blue": "\u001b[{}4m",
                           "magenta": "\u001b[{}5m",
                           "cyan": "\u001b[{}6m",
                           "white": "\u001b[{}7m"}

        self.format = {"bold": "\u001b[1m",
                       "underline": "\u001b[4m",
                       "reverse": "\u001b[7m",
                       "reset": "\u001b[0m",
                       "italic": "\u001b[3m",
                       "crossed": "\u001b[9m"}

    class Hints:
        class Color:
            black = "black"
            red = "red"
            green = "green"
            yellow = "yellow"
            blue = "blue"
            magenta = "magenta"
            cyan = "cyan"
            white = "while"

        class Style:
            bold = "bold"
            underline = "underline"
            reverse = "reverse"
            reset = "reset"
            italic = "italic"
            crossed = "crossed"

    def paint(self, color="", string="", background=False):
        self.text = string if string else self.text
        if not color.startswith("\u001b"):
            self.effects += self.hash_codes[color.lower()].format('4' if background else '3')
        else:
            self.effects += color.format('4' if background else '3')
        return self

    def style(self, style="", string=""):
        self.text = string if string else self.text
        self.effects += self.format[style]
        return self

    @staticmethod
    def help(visualise=False):
        p = Colorfy()
        h = Colorfy.Hints()
        color_list = ["Black",
                      "Red",
                      "Green",
                      "Yellow",
                      "Blue",
                      "Magenta",
                      "Cyan",
                      "White"]

        styles_list = ["Reset",
                       "Bold",
                       "Italic",
                       "Underline",
                       "Reverse",
                       "Crossed"]

        if visualise:
            color_res = []
            for i in color_list:
                color = Colorfy(i)
                color_res += [color.paint(color=i.lower())]
            color_res = ", ".join(map(str, color_res))

            style_res = []
            for i in styles_list:
                style = Colorfy(i)
                style_res += [style.style(style=i.lower())]

            style_res = ", ".join(map(str, style_res))
            print(
                f"{p.paint(string='Colors:', color=h.Color.red)}: {color_res}"
                f"\n{p.paint(string='Styles:', color=h.Color.red)} {style_res}")
        else:
            print(
                f"{p.paint(string='Colors:', color=h.Color.red)} "
                f"{p.paint(string=', '.join(color_list), color=h.Color.blue)}"
                f"\n{p.paint(string='Styles:', color=h.Color.red)} "
                f"{p.paint(string=', '.join(styles_list), color=h.Color.blue)}")

    def show(self):
        print("".join(self.effects) + self.text + self.format['reset'])

    def __str__(self):
        return "".join(self.effects) + self.text + self.format['reset']

    def __repr__(self):
        return "".join(self.effects) + self.text + self.format['reset']
