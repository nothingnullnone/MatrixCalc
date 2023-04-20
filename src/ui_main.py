import functools
from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from src.object_names import ObjNames


class Matrix(Enum):
    A = 0
    B = 1


class MyFont:
    def __init__(self):
        self.font = QtGui.QFont()
        self.font.setFamily("Tahoma")
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(75)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(str(ObjNames.mainWindow.value))
        MainWindow.resize(949, 444)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon_matrix.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    background-color: #121212;\n"
                                 "    color: lime;\n"
                                 "    margin: 7px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    background-color: 0, 0, 0, 0;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit {\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "    font: 75 10pt 'Tahoma';\n"
                                 "    color: rgb(0, 0, 0);\n"
                                 "    border-style: solid;\n"
                                 "    border-radius: 5px;\n"
                                 "    border-width: 2px;\n"
                                 "    border-color: black;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox{\n"
                                 "    margin: 1px;\n"
                                 "    padding: 3px;\n"
                                 "    border: 2px solid gray;\n"
                                 "    border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    border: 2px solid gray;\n"
                                 "    border-radius: 5px;\n"
                                 "    padding: 7px;\n"
                                 "    font: 75 10pt 'Tahoma';\n"
                                 "    margin: 7px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    border-color: #090;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    border: 4px solid #090;\n"
                                 "    border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:checked {\n"
                                 "    background-color: #006300;\n"
                                 "    border-color: #090;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget#centralwidget {\n"
                                 "    background-color: #121212;\n"
                                 "}")
        # Главный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(str(ObjNames.centralWidget.value))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(str(ObjNames.verticalLayout.value))

        # Основной горизонтальный Layout
        self.horizontalLayoutAB = QtWidgets.QHBoxLayout()
        self.horizontalLayoutAB.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayoutAB.setObjectName(str(ObjNames.horizontalLayoutAB.value))

        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAB.addItem(spacerItem)
        self.verticalLayoutA = QtWidgets.QVBoxLayout()
        self.verticalLayoutA.setObjectName(str(ObjNames.verticalLayoutA.value))

        # Заголовок матрицы А
        self.labelHeaderA = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeaderA.sizePolicy().hasHeightForWidth())
        self.labelHeaderA.setSizePolicy(sizePolicy)
        self.labelHeaderA.setStyleSheet("font: 14pt 'Tahoma';")
        self.labelHeaderA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeaderA.setObjectName(str(ObjNames.labelHeaderA.value))
        self.verticalLayoutA.addWidget(self.labelHeaderA)

        # Подзаголовок матрицы А
        self.labelsubHeaderA = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.labelsubHeaderA.sizePolicy().hasHeightForWidth())
        self.labelsubHeaderA.setSizePolicy(sizePolicy)
        self.labelsubHeaderA.setStyleSheet("font: 10pt 'Tahoma';")
        self.labelsubHeaderA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelsubHeaderA.setObjectName("labelsubHeaderA")
        self.verticalLayoutA.addWidget(self.labelsubHeaderA)

        # Сетка Layout
        self.gridLayout2_a = QtWidgets.QGridLayout()
        self.gridLayout2_a.setObjectName("gridLayout2_a")

        # Горизонтальный Layout
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Кнопка Умножить
        self.pushButtonMultiply_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMultiply_a.sizePolicy().hasHeightForWidth())
        self.pushButtonMultiply_a.setSizePolicy(sizePolicy)
        self.pushButtonMultiply_a.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonMultiply_a.setStyleSheet("margin-top: 2px;\n"
                                                "margin-bottom: 2px")
        self.pushButtonMultiply_a.setObjectName("pushButtonMultiply_a")
        self.horizontalLayout_4.addWidget(self.pushButtonMultiply_a)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)

        # Текст Ограничение значений множителя
        self.labelmulvaluelimitA = QtWidgets.QLabel(self.centralwidget)
        self.labelmulvaluelimitA.setStyleSheet("font: 10pt 'Tahoma';")
        self.labelmulvaluelimitA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelmulvaluelimitA.setObjectName("labelmulvaluelimitA")
        self.horizontalLayout_4.addWidget(self.labelmulvaluelimitA)

        # Ввод множителя
        self.inputMultiply_a = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputMultiply_a.sizePolicy().hasHeightForWidth())
        self.inputMultiply_a.setSizePolicy(sizePolicy)
        self.inputMultiply_a.setMinimumSize(QtCore.QSize(0, 45))
        self.inputMultiply_a.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ft = MyFont()
        self.inputMultiply_a.setFont(ft.font)
        self.inputMultiply_a.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputMultiply_a.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-style: solid;\n"
                                           "border-radius: 5px;\n"
                                           "border-width: 2px;\n"
                                           "border-color: black;")
        self.inputMultiply_a.setAlignment(QtCore.Qt.AlignCenter)
        self.inputMultiply_a.setObjectName("inputMultiply_a")
        self.inputMultiply_a.clear()
        self.inputMultiply_a.setText("1.0")
        self.inputMultiply_a.setMaxLength(4)
        self.inputMultiply_a.returnPressed.connect(lambda: self.checkFloatInput(self.inputMultiply_a, -9.9, 9.9))
        self.inputMultiply_a.editingFinished.connect(lambda: self.checkFloatInput(self.inputMultiply_a, -9.9, 9.9))
        self.horizontalLayout_4.addWidget(self.inputMultiply_a)
        self.gridLayout2_a.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Текст
        self.textSize_a = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSize_a.sizePolicy().hasHeightForWidth())
        self.textSize_a.setSizePolicy(sizePolicy)
        self.textSize_a.setObjectName("textSize_a")
        self.horizontalLayout.addWidget(self.textSize_a)

        # Выпадающий список
        self.comboBoxSize_a1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSize_a1.sizePolicy().hasHeightForWidth())
        self.comboBoxSize_a1.setSizePolicy(sizePolicy)
        self.comboBoxSize_a1.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSize_a1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxSize_a1.setStyleSheet("")
        self.comboBoxSize_a1.setObjectName("comboBoxSize_a1")
        for x in range(9):
            self.comboBoxSize_a1.addItem("")
        self.comboBoxSize_a1.setCurrentIndex(2)
        self.horizontalLayout.addWidget(self.comboBoxSize_a1)

        # Текст
        self.textX_a = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textX_a.sizePolicy().hasHeightForWidth())
        self.textX_a.setSizePolicy(sizePolicy)
        self.textX_a.setObjectName("textX_a")
        self.horizontalLayout.addWidget(self.textX_a)

        # Выпадающий список
        self.comboBoxSize_a2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSize_a2.sizePolicy().hasHeightForWidth())
        self.comboBoxSize_a2.setSizePolicy(sizePolicy)
        self.comboBoxSize_a2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSize_a2.setObjectName("comboBoxSize_a2")
        for x in range(9):
            self.comboBoxSize_a2.addItem("")
        self.comboBoxSize_a2.setCurrentIndex(2)
        self.horizontalLayout.addWidget(self.comboBoxSize_a2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.gridLayout2_a.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        # Кнопка Очистить
        self.pushButtonClear_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClear_a.sizePolicy().hasHeightForWidth())
        self.pushButtonClear_a.setSizePolicy(sizePolicy)
        self.pushButtonClear_a.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonClear_a.setStyleSheet("margin-top: 2px;\n"
                                             "margin-bottom: 2px")
        self.pushButtonClear_a.setObjectName("pushButtonClear_a")
        self.gridLayout2_a.addWidget(self.pushButtonClear_a, 0, 0, 1, 1)

        # Отрисовка матрицы A
        self.input_a = []
        self.redrawMatrix(Matrix.A)

        # Кнопка Транспонировать
        self.pushButtonTranspond_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTranspond_a.sizePolicy().hasHeightForWidth())
        self.pushButtonTranspond_a.setSizePolicy(sizePolicy)
        self.pushButtonTranspond_a.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonTranspond_a.setStyleSheet("margin-top: 2px;\n"
                                                 "margin-bottom: 2px")
        self.pushButtonTranspond_a.setObjectName("pushButtonTranspond_a")
        self.gridLayout2_a.addWidget(self.pushButtonTranspond_a, 1, 0, 1, 1)

        # Кнопка Найти определитель
        self.pushButtonDeterminant_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeterminant_a.sizePolicy().hasHeightForWidth())
        self.pushButtonDeterminant_a.setSizePolicy(sizePolicy)
        self.pushButtonDeterminant_a.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonDeterminant_a.setStyleSheet("margin-top: 2px;\n"
                                                   "margin-bottom: 2px")
        self.pushButtonDeterminant_a.setObjectName("pushButtonDeterminant_a")
        self.gridLayout2_a.addWidget(self.pushButtonDeterminant_a, 2, 0, 1, 1)

        # Кнопка Найти ранг
        self.pushButtonRank_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRank_a.sizePolicy().hasHeightForWidth())
        self.pushButtonRank_a.setSizePolicy(sizePolicy)
        self.pushButtonRank_a.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonRank_a.setStyleSheet("margin-top: 2px;\n"
                                            "margin-bottom: 2px")
        self.pushButtonRank_a.setObjectName("pushButtonRank_a")
        self.gridLayout2_a.addWidget(self.pushButtonRank_a, 3, 0, 1, 1)

        # Кнопка Обратная матрица
        self.pushButtonReverse_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonReverse_a.sizePolicy().hasHeightForWidth())
        self.pushButtonReverse_a.setSizePolicy(sizePolicy)
        self.pushButtonReverse_a.setMinimumSize(QtCore.QSize(40, 45))
        self.pushButtonReverse_a.setStyleSheet("margin-top: 2px;\n"
                                               "margin-bottom: 2px")
        self.pushButtonReverse_a.setObjectName("pushButtonReverse_a")
        self.gridLayout2_a.addWidget(self.pushButtonReverse_a, 3, 1, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Кнопка Возвести в степень
        self.pushButtonPower_a = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPower_a.sizePolicy().hasHeightForWidth())
        self.pushButtonPower_a.setSizePolicy(sizePolicy)
        self.pushButtonPower_a.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonPower_a.setStyleSheet("margin-top: 2px;\n"
                                             "margin-bottom: 2px")
        self.pushButtonPower_a.setObjectName("pushButtonPower_a")
        self.horizontalLayout_2.addWidget(self.pushButtonPower_a)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        # Текст Ограничение значений множителя
        self.labelpowvaluelimitA = QtWidgets.QLabel(self.centralwidget)
        self.labelpowvaluelimitA.setStyleSheet("font: 10pt 'Tahoma';")
        self.labelpowvaluelimitA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpowvaluelimitA.setObjectName("labelpowvaluelimitA")
        self.horizontalLayout_2.addWidget(self.labelpowvaluelimitA)

        # Ввести показатель степени
        self.inputPower_a = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPower_a.sizePolicy().hasHeightForWidth())
        self.inputPower_a.setSizePolicy(sizePolicy)
        self.inputPower_a.setMinimumSize(QtCore.QSize(0, 45))
        self.inputPower_a.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ft = MyFont()
        self.inputPower_a.setFont(ft.font)
        self.inputPower_a.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputPower_a.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-style: solid;\n"
                                        "border-radius: 5px;\n"
                                        "border-width: 2px;\n"
                                        "border-color: black;")
        self.inputPower_a.setText("")
        self.inputPower_a.setMaxLength(2)
        self.inputPower_a.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPower_a.setPlaceholderText("")
        self.inputPower_a.setObjectName("inputPower_a")
        self.horizontalLayout_2.addWidget(self.inputPower_a)
        self.inputPower_a.clear()
        self.inputPower_a.setText("1")
        self.inputPower_a.setMaxLength(2)
        self.inputPower_a.returnPressed.connect(lambda: self.checkIntInput(self.inputPower_a, -9, 9))
        self.inputPower_a.editingFinished.connect(lambda: self.checkIntInput(self.inputPower_a, -9, 9))
        self.gridLayout2_a.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayoutA.addLayout(self.gridLayout2_a)
        self.horizontalLayoutAB.addLayout(self.verticalLayoutA)

        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAB.addItem(spacerItem6)

        # Вертикальный Layout
        self.verticalLayoutButtonsAB = QtWidgets.QVBoxLayout()
        self.verticalLayoutButtonsAB.setObjectName("verticalLayoutButtonsAB")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutButtonsAB.addItem(spacerItem7)

        # Кнопка Сложить матрицы
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.verticalLayoutButtonsAB.addWidget(self.pushButtonAdd)

        # Кнопка Вычесть матрицы
        self.pushButtonSub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSub.setObjectName("pushButtonSub")
        self.verticalLayoutButtonsAB.addWidget(self.pushButtonSub)

        # Кнопка Перемножить матрицы
        self.pushButtonMul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMul.setObjectName("pushButtonMul")
        self.verticalLayoutButtonsAB.addWidget(self.pushButtonMul)

        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutButtonsAB.addItem(spacerItem8)
        self.horizontalLayoutAB.addLayout(self.verticalLayoutButtonsAB)
        spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAB.addItem(spacerItem9)

        # Вертикальный Layout
        self.verticalLayoutB = QtWidgets.QVBoxLayout()
        self.verticalLayoutB.setObjectName("verticalLayoutB")

        # Заголовок матрицы B
        self.labelHeaderB = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeaderB.sizePolicy().hasHeightForWidth())
        self.labelHeaderB.setSizePolicy(sizePolicy)
        self.labelHeaderB.setStyleSheet("font: 14pt 'Tahoma';")
        self.labelHeaderB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeaderB.setObjectName("labelHeaderB")
        self.verticalLayoutB.addWidget(self.labelHeaderB)

        # Подзаголовок матрицы B
        self.labelsubHeaderB = QtWidgets.QLabel(self.centralwidget)
        sizePolicy.setHeightForWidth(self.labelsubHeaderA.sizePolicy().hasHeightForWidth())
        self.labelsubHeaderB.setSizePolicy(sizePolicy)
        self.labelsubHeaderB.setStyleSheet("font: 10pt 'Tahoma';")
        self.labelsubHeaderB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelsubHeaderB.setObjectName("labelsubHeaderB")
        self.verticalLayoutB.addWidget(self.labelsubHeaderB)

        # Сетка Layout
        self.gridLayout2_b = QtWidgets.QGridLayout()
        self.gridLayout2_b.setObjectName("gridLayout2_b")

        # Кнопка Очистить
        self.pushButtonClear_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClear_b.sizePolicy().hasHeightForWidth())
        self.pushButtonClear_b.setSizePolicy(sizePolicy)
        self.pushButtonClear_b.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonClear_b.setStyleSheet("margin-top: 2px;\n"
                                             "margin-bottom: 2px")
        self.pushButtonClear_b.setObjectName("pushButtonClear_b")
        self.gridLayout2_b.addWidget(self.pushButtonClear_b, 0, 0, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Текст Размер
        self.textSize_b = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSize_b.sizePolicy().hasHeightForWidth())
        self.textSize_b.setSizePolicy(sizePolicy)
        self.textSize_b.setObjectName("textSize_b")
        self.horizontalLayout_3.addWidget(self.textSize_b)

        # Выпадающий список
        self.comboBoxSize_b1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSize_b1.sizePolicy().hasHeightForWidth())
        self.comboBoxSize_b1.setSizePolicy(sizePolicy)
        self.comboBoxSize_b1.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSize_b1.setObjectName("comboBoxSize_b1")
        for x in range(9):
            self.comboBoxSize_b1.addItem("")
        self.comboBoxSize_b1.setCurrentIndex(2)
        self.horizontalLayout_3.addWidget(self.comboBoxSize_b1)

        # Текст Х
        self.textX_b = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textX_b.sizePolicy().hasHeightForWidth())
        self.textX_b.setSizePolicy(sizePolicy)
        self.textX_b.setObjectName("textX_b")
        self.horizontalLayout_3.addWidget(self.textX_b)

        # Выпадающий список
        self.comboBoxSize_b2 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSize_b2.sizePolicy().hasHeightForWidth())
        self.comboBoxSize_b2.setSizePolicy(sizePolicy)
        self.comboBoxSize_b2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSize_b2.setObjectName("comboBoxSize_b2")
        for x in range(9):
            self.comboBoxSize_b2.addItem("")
        self.comboBoxSize_b2.setCurrentIndex(2)
        self.horizontalLayout_3.addWidget(self.comboBoxSize_b2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.gridLayout2_b.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        # Отрисовка матрицы B
        self.input_b = []
        self.redrawMatrix(Matrix.B)

        # Кнопка Транспонировать
        self.pushButtonTranspond_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTranspond_b.sizePolicy().hasHeightForWidth())
        self.pushButtonTranspond_b.setSizePolicy(sizePolicy)
        self.pushButtonTranspond_b.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonTranspond_b.setStyleSheet("margin-top: 2px;\n"
                                                 "margin-bottom: 2px")
        self.pushButtonTranspond_b.setObjectName("pushButtonTranspond_b")
        self.gridLayout2_b.addWidget(self.pushButtonTranspond_b, 1, 0, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # Кнопка Возвести в степень
        self.pushButtonPower_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPower_b.sizePolicy().hasHeightForWidth())
        self.pushButtonPower_b.setSizePolicy(sizePolicy)
        self.pushButtonPower_b.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonPower_b.setStyleSheet("margin-top: 2px;\n"
                                             "margin-bottom: 2px")
        self.pushButtonPower_b.setObjectName("pushButtonPower_b")
        self.horizontalLayout_5.addWidget(self.pushButtonPower_b)

        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)

        # Текст Ограничение значений показателя степени
        self.labelpowvaluelimitB = QtWidgets.QLabel(self.centralwidget)
        self.labelpowvaluelimitB.setStyleSheet("font: 10pt 'Tahoma';")
        self.labelpowvaluelimitB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpowvaluelimitB.setObjectName("labelpowvaluelimitB")
        self.horizontalLayout_5.addWidget(self.labelpowvaluelimitB)

        # Ввод показателя степени
        self.inputPower_b = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPower_b.sizePolicy().hasHeightForWidth())
        self.inputPower_b.setSizePolicy(sizePolicy)
        self.inputPower_b.setMinimumSize(QtCore.QSize(0, 45))
        self.inputPower_b.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ft = MyFont()
        self.inputPower_b.setFont(ft.font)
        self.inputPower_b.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputPower_b.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-style: solid;\n"
                                        "border-radius: 5px;\n"
                                        "border-width: 2px;\n"
                                        "border-color: black;")
        self.inputPower_b.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPower_b.setObjectName("inputPower_b")
        self.inputPower_b.clear()
        self.inputPower_b.setText("1")
        self.inputPower_b.setMaxLength(2)
        self.inputPower_b.returnPressed.connect(lambda: self.checkIntInput(self.inputPower_b, -9, 9))
        self.inputPower_b.editingFinished.connect(lambda: self.checkIntInput(self.inputPower_b, -9, 9))
        self.horizontalLayout_5.addWidget(self.inputPower_b)
        self.gridLayout2_b.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        # Кнопка Найти определитель
        self.pushButtonDeterminant_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeterminant_b.sizePolicy().hasHeightForWidth())
        self.pushButtonDeterminant_b.setSizePolicy(sizePolicy)
        self.pushButtonDeterminant_b.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonDeterminant_b.setStyleSheet("margin-top: 2px;\n"
                                                   "margin-bottom: 2px")
        self.pushButtonDeterminant_b.setObjectName("pushButtonDeterminant_b")
        self.gridLayout2_b.addWidget(self.pushButtonDeterminant_b, 2, 0, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Кнопка Умножить
        self.pushButtonMultiply_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMultiply_b.sizePolicy().hasHeightForWidth())
        self.pushButtonMultiply_b.setSizePolicy(sizePolicy)
        self.pushButtonMultiply_b.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonMultiply_b.setStyleSheet("margin-top: 2px;\n"
                                                "margin-bottom: 2px")
        self.pushButtonMultiply_b.setObjectName("pushButtonMultiply_b")
        self.horizontalLayout_6.addWidget(self.pushButtonMultiply_b)

        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)

        # Текст Ограничение значений показателя степени
        self.labelmulvaluelimitB = QtWidgets.QLabel(self.centralwidget)
        self.labelmulvaluelimitB.setStyleSheet("font: 10pt 'Tahoma';")
        self.labelmulvaluelimitB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelmulvaluelimitB.setObjectName("labelmulvaluelimitB")
        self.horizontalLayout_6.addWidget(self.labelmulvaluelimitB)

        # Ввод множителя
        self.inputMultiply_b = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputMultiply_b.sizePolicy().hasHeightForWidth())
        self.inputMultiply_b.setSizePolicy(sizePolicy)
        self.inputMultiply_b.setMinimumSize(QtCore.QSize(0, 45))
        self.inputMultiply_b.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ft = MyFont()
        self.inputMultiply_b.setFont(ft.font)
        self.inputMultiply_b.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputMultiply_b.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-style: solid;\n"
                                           "border-radius: 5px;\n"
                                           "border-width: 2px;\n"
                                           "border-color: black;")
        self.inputMultiply_b.setAlignment(QtCore.Qt.AlignCenter)
        self.inputMultiply_b.setObjectName("inputMultiply_b")
        self.inputMultiply_b.clear()
        self.inputMultiply_b.setText("1.0")
        self.inputMultiply_b.setMaxLength(4)
        self.inputMultiply_b.returnPressed.connect(lambda: self.checkFloatInput(self.inputMultiply_b, -9.9, 9.9))
        self.inputMultiply_b.editingFinished.connect(lambda: self.checkFloatInput(self.inputMultiply_b, -9.9, 9.9))
        self.horizontalLayout_6.addWidget(self.inputMultiply_b)
        self.gridLayout2_b.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)

        # Кнопка Найти ранг
        self.pushButtonRank_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRank_b.sizePolicy().hasHeightForWidth())
        self.pushButtonRank_b.setSizePolicy(sizePolicy)
        self.pushButtonRank_b.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonRank_b.setStyleSheet("margin-top: 2px;\n"
                                            "margin-bottom: 2px")
        self.pushButtonRank_b.setObjectName("pushButtonRank_b")
        self.gridLayout2_b.addWidget(self.pushButtonRank_b, 3, 0, 1, 1)

        # Кнопка Обратная матрица
        self.pushButtonReverse_b = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonReverse_b.sizePolicy().hasHeightForWidth())
        self.pushButtonReverse_b.setSizePolicy(sizePolicy)
        self.pushButtonReverse_b.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButtonReverse_b.setStyleSheet("margin-top: 2px;\n"
                                               "margin-bottom: 2px")
        self.pushButtonReverse_b.setObjectName("pushButtonReverse_b")
        self.gridLayout2_b.addWidget(self.pushButtonReverse_b, 3, 1, 1, 1)
        self.verticalLayoutB.addLayout(self.gridLayout2_b)
        self.horizontalLayoutAB.addLayout(self.verticalLayoutB)

        spacerItem14 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAB.addItem(spacerItem14)

        self.verticalLayout.addLayout(self.horizontalLayoutAB)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelHeaderA.setText(_translate("MainWindow", "Введите матрицу А"))
        self.labelsubHeaderA.setText(_translate("MainWindow", "Введите числа от -99.9 до 99.9"))
        self.pushButtonMultiply_a.setText(_translate("MainWindow", "Умножить"))
        self.labelmulvaluelimitA.setText(_translate("MainWindow", "min -9.9\nmax 9.9"))
        self.textSize_a.setText(_translate("MainWindow", "Размер"))
        self.comboBoxSize_a1.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSize_a1.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSize_a1.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSize_a1.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSize_a1.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSize_a1.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSize_a1.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSize_a1.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSize_a1.setItemText(8, _translate("MainWindow", "9"))
        self.textX_a.setText(_translate("MainWindow", "x"))
        self.comboBoxSize_a2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSize_a2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSize_a2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSize_a2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSize_a2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSize_a2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSize_a2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSize_a2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSize_a2.setItemText(8, _translate("MainWindow", "9"))
        self.pushButtonClear_a.setText(_translate("MainWindow", "Очистить"))
        self.pushButtonTranspond_a.setText(_translate("MainWindow", "Транспонировать"))
        self.pushButtonDeterminant_a.setText(_translate("MainWindow", "Найти определитель"))
        self.pushButtonRank_a.setText(_translate("MainWindow", "Найти ранг"))
        self.pushButtonReverse_a.setText(_translate("MainWindow", "Обратная матрица"))
        self.pushButtonPower_a.setText(_translate("MainWindow", "Возвести в степень"))
        self.labelpowvaluelimitA.setText(_translate("MainWindow", " min -9 \n max 9 "))
        self.pushButtonAdd.setText(_translate("MainWindow", "A + B"))
        self.pushButtonSub.setText(_translate("MainWindow", "A - B"))
        self.pushButtonMul.setText(_translate("MainWindow", "A x B"))
        self.labelHeaderB.setText(_translate("MainWindow", "Введите матрицу B"))
        self.labelsubHeaderB.setText(_translate("MainWindow", "Введите числа от -99.9 до 99.9"))
        self.pushButtonClear_b.setText(_translate("MainWindow", "Очистить"))
        self.textSize_b.setText(_translate("MainWindow", "Размер"))
        self.comboBoxSize_b1.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSize_b1.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSize_b1.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSize_b1.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSize_b1.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSize_b1.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSize_b1.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSize_b1.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSize_b1.setItemText(8, _translate("MainWindow", "9"))
        self.textX_b.setText(_translate("MainWindow", "x"))
        self.comboBoxSize_b2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSize_b2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSize_b2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSize_b2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSize_b2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSize_b2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSize_b2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSize_b2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSize_b2.setItemText(8, _translate("MainWindow", "9"))
        self.pushButtonTranspond_b.setText(_translate("MainWindow", "Транспонировать"))
        self.pushButtonPower_b.setText(_translate("MainWindow", "Возвести в степень"))
        self.labelpowvaluelimitB.setText(_translate("MainWindow", " min -9 \n max 9 "))
        self.pushButtonDeterminant_b.setText(_translate("MainWindow", "Найти определитель"))
        self.pushButtonMultiply_b.setText(_translate("MainWindow", "Умножить"))
        self.labelmulvaluelimitB.setText(_translate("MainWindow", "min -9.9\nmax 9.9"))
        self.pushButtonRank_b.setText(_translate("MainWindow", "Найти ранг"))
        self.pushButtonReverse_b.setText(_translate("MainWindow", "Обратная матрица"))

    def redrawMatrix(self, m: Matrix):
        if m.value == 1:
            # Сетка Layout
            self.gridLayout1_b = QtWidgets.QGridLayout()
            self.gridLayout1_b.setObjectName("gridLayout1_b")
            gridlayout = self.gridLayout1_b
            self.verticalLayoutB.insertLayout(2, self.gridLayout1_b)
            combobox1 = self.comboBoxSize_b1
            combobox2 = self.comboBoxSize_b2
            lst = self.input_b
            lst.clear()
        else:
            # Сетка Layout
            self.gridLayout1_a = QtWidgets.QGridLayout()
            self.gridLayout1_a.setObjectName("gridLayout1_a")
            gridlayout = self.gridLayout1_a
            self.verticalLayoutA.insertLayout(2, self.gridLayout1_a)
            combobox1 = self.comboBoxSize_a1
            combobox2 = self.comboBoxSize_a2
            lst = self.input_a
            lst.clear()

        for i in range(combobox1.currentIndex() + 1):
            buf = []
            for j in range(combobox2.currentIndex() + 1):
                lineinput = QtWidgets.QLineEdit(self.centralwidget)
                buf.append(lineinput)
            lst.append(buf)

        for i in range(combobox1.currentIndex() + 1):
            for j in range(combobox2.currentIndex() + 1):
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(1)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(lst[i][j].sizePolicy().hasHeightForWidth())
                lst[i][j].setSizePolicy(sizePolicy)
                lst[i][j].setMinimumSize(QtCore.QSize(0, 45))
                ft = MyFont()
                lst[i][j].setFont(ft.font)
                lst[i][j].setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
                lst[i][j].setAlignment(QtCore.Qt.AlignCenter)
                lst[i][j].setObjectName("input_a" + str(i) + str(j))
                gridlayout.addWidget(lst[i][j], i, j + 1, 1, 1)
                lst[i][j].clear()
                lst[i][j].setText("0.0")
                lst[i][j].setMaxLength(5)
                lst[i][j].returnPressed.connect(
                    (functools.partial(self.checkFloatInput, lst[i][j], -99.9, 99.9)))
                lst[i][j].editingFinished.connect(
                    (functools.partial(self.checkFloatInput, lst[i][j], -99.9, 99.9)))

    def checkFloatInput(self, input_: QtWidgets.QLineEdit, minVal: float, maxVal: float):
        try:
            if float(input_.text()) < minVal:
                input_.setText(f"{minVal:.1f}")
            elif float(input_.text()) > maxVal:
                input_.setText(f"{maxVal:.1f}")
            else:
                input_.setText(str(float(input_.text())))
        except ValueError or IndexError:
            input_.setText("0.0")

    def checkIntInput(self, input_: QtWidgets.QLineEdit, minVal: int, maxVal: int):
        try:
            if int(input_.text()) < minVal:
                input_.setText(f"{minVal}")
            elif int(input_.text()) > maxVal:
                input_.setText(f"{maxVal}")
            else:
                input_.setText(str(int(input_.text())))
        except ValueError:
            input_.setText("0")


class MyMessageBox(QtWidgets.QMessageBox):
    def __init__(self, result=None):
        if result is None:
            result = []
        self.rows = len(result) if isinstance(result, list) else 0
        self.columns = len(result[0]) if isinstance(result, list) else 0
        self.rnd = lambda x: str(float(f"{x:.10f}")) if abs(float(f"{x}") - float(f"{x:.10f}")) < 1e-10 else str(
            float(f"{x}"))
        self.maxelem = max([max([len(self.rnd(result[i][j])) for i in range(self.rows)]) for j in range(self.columns)]) \
            if isinstance(result, list) else 0
        QtWidgets.QMessageBox.__init__(self)
        self.setSizeGripEnabled(True)
        self.setWindowTitle("Результат")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/ui/resources/icon_matrix.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def addTableWidget(self, parentItem: QMessageBox, result: list):
        self.layout = QtWidgets.QHBoxLayout()
        self.tableWidget = QtWidgets.QTableWidget(parentItem)
        self.tableWidget.setObjectName('tableWidget')
        self.tableWidget.setColumnCount(self.columns)
        self.tableWidget.setRowCount(self.rows)
        for x in range(self.rows):
            for y in range(self.columns):
                self.tableWidget.setColumnWidth(y, (self.maxelem + 2) * 9)
                res = result[x][y]
                if int(res) == res:
                    item = QTableWidgetItem(f"{res:.0f}")
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                else:
                    item = QTableWidgetItem(self.rnd(res))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                item.setTextAlignment(132)
                self.tableWidget.setItem(x, y, item)
        self.tableWidget.move(2, 2)
        self.tableWidget.resize(self.columns * ((self.maxelem + 2) * 9) + 2, (self.rows * 30) + 2)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def event(self, e):
        result = QtWidgets.QMessageBox.event(self, e)
        self.setMinimumWidth(130)
        self.setMaximumWidth(16777215)
        self.setMinimumHeight(80)
        self.setMaximumHeight(16777215)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        if self.rows != 0 and self.columns != 0 and self.maxelem > 1:
            self.resize(self.columns * ((self.maxelem + 2) * 9) + 6, (self.rows * 30) + 48)
        return result
