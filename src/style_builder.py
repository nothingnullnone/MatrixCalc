class StyleBuilder:
    def __init__(self):
        self.result = ""

    def addMarginTop(self, value):
        self.result += f"margin-top: {value}px;\n"
        return self

    def addMarginBottom(self, value):
        self.result += f"margin-bottom: {value}px;\n"
        return self

    def addFont(self, size, family):
        self.result += f"font: {size}pt {family};\n"
        return self

    def addBgColor(self, color):
        self.result += f"background-color: rgb{color};\n"
        return self

    def addColor(self, color):
        self.result += f"color: rgb{color};\n"
        return self

    def addBorderStyle(self, style):
        self.result += f"border-style: {style};\n"
        return self

    def addBorderRadius(self, value):
        self.result += f"border-radius: {value}px;\n"
        return self

    def addBorderWidth(self, value):
        self.result += f"border-width: {value}px;\n"
        return self

    def addBorderColor(self, color):
        self.result += f"border-color: {color};\n"
        return self

    def build(self):
        return self.result
