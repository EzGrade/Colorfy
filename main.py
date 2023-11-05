class Colorfy:
    def __init__(self, string=""):
        self.text = string
        self.effects = []
        self.__setup()

    def __setup(self):
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

    class hints:
        class color:
            black = "black"
            red = "red"
            green = "green"
            yellow = "yellow"
            blue = "blue"
            magenta = "magenta"
            cyan = "cyan"
            white = "while"

        class style:
            bold = "bold"
            underline = "underline"
            reverse = "reverse"
            reset = "reset"
            italic = "italic"
            crossed = "crossed"

    def paint(self, color="", string="", background=False):
        self.text = string if string else self.text
        self.effects += self.hash_codes[color].format('4' if background else '3')
        return self

    def style(self, style="", string=""):
        self.text = string if string else self.text
        self.effects += self.format[style]
        return self

    @staticmethod
    def help():
        p = Colorfy()
        h = ColorfyHints()
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
                       "Underlined",
                       "Inverted",
                       "Crossed"]

        print(
            f"{p.paint(string='Colors:', color=h.red)} {p.paint(string=', '.join(color_list), color=h.blue)}"
            f"\n{p.paint(string='Styles:', color=h.red)} {p.paint(string=', '.join(styles_list), color=h.blue)}")

    def show(self):
        print("".join(self.effects) + self.text + self.format['reset'])

    def __str__(self):
        return "".join(self.effects) + self.text + self.format['reset']


text = Colorfy('Template')
text.paint(Colorfy.hints.color.red)
text.style(Colorfy.hints.style.italic)
text.show()
