from PyQt5 import QtGui


class MyFont:
    def __init__(self):
        self.font = QtGui.QFont()
        self.font.setFamily("Tahoma")
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(75)
