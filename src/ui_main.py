import functools
from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from src.myfont import MyFont
from src.object_names import ObjNames
from src.style_builder import StyleBuilder


class Matrix(Enum):
    A = 0
    B = 1


def checkIntInput(input_: QtWidgets.QLineEdit, minVal: int, maxVal: int):
    try:
        if int(input_.text()) < minVal:
            input_.setText(f"{minVal}")
        elif int(input_.text()) > maxVal:
            input_.setText(f"{maxVal}")
        else:
            input_.setText(str(int(input_.text())))
    except ValueError:
        input_.setText("0")


def checkFloatInput(input_: QtWidgets.QLineEdit, minVal: float, maxVal: float):
    try:
        if float(input_.text()) < minVal:
            input_.setText(f"{minVal:.1f}")
        elif float(input_.text()) > maxVal:
            input_.setText(f"{maxVal:.1f}")
        else:
            input_.setText(str(float(input_.text())))
    except ValueError or IndexError:
        input_.setText("0.0")


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
                                 "QWidget#centralWidget {\n"
                                 "    background-color: #121212;\n"
                                 "}")
        # Главный виджет
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(str(ObjNames.centralWidget.value))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
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
        self.labelHeaderA = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeaderA.sizePolicy().hasHeightForWidth())
        self.labelHeaderA.setSizePolicy(sizePolicy)
        self.labelHeaderA.setStyleSheet(StyleBuilder().addFont(14, "Tahoma").build())
        self.labelHeaderA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeaderA.setObjectName(str(ObjNames.labelHeaderA.value))
        self.verticalLayoutA.addWidget(self.labelHeaderA)

        # Подзаголовок матрицы А
        self.labelSubHeaderA = QtWidgets.QLabel(self.centralWidget)
        sizePolicy.setHeightForWidth(self.labelSubHeaderA.sizePolicy().hasHeightForWidth())
        self.labelSubHeaderA.setSizePolicy(sizePolicy)
        self.labelSubHeaderA.setStyleSheet(StyleBuilder().addFont(10, "Tahoma").build())
        self.labelSubHeaderA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSubHeaderA.setObjectName(str(ObjNames.labelSubHeaderA.value))
        self.verticalLayoutA.addWidget(self.labelSubHeaderA)

        # Сетка Layout
        self.gridLayout2A = QtWidgets.QGridLayout()
        self.gridLayout2A.setObjectName(str(ObjNames.gridLayout2A.value))

        # Горизонтальный Layout
        self.horizontalLayout4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout4.setObjectName(str(ObjNames.horizontalLayout4.value))

        # Кнопка Умножить
        self.pushButtonMultiplyA = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMultiplyA.sizePolicy().hasHeightForWidth())
        self.pushButtonMultiplyA.setSizePolicy(sizePolicy)
        self.pushButtonMultiplyA.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonMultiplyA.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonMultiplyA.setObjectName(str(ObjNames.pushButtonMultiplyA.value))
        self.horizontalLayout4.addWidget(self.pushButtonMultiplyA)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout4.addItem(spacerItem2)

        # Текст Ограничение значений множителя
        self.labelMultiplierValLimitA = QtWidgets.QLabel(self.centralWidget)
        self.labelMultiplierValLimitA.setStyleSheet(StyleBuilder().addFont(10, "Tahoma").build())
        self.labelMultiplierValLimitA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMultiplierValLimitA.setObjectName(str(ObjNames.labelMultiplierValLimitA.value))
        self.horizontalLayout4.addWidget(self.labelMultiplierValLimitA)

        # Ввод множителя
        self.inputMultiplyA = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputMultiplyA.sizePolicy().hasHeightForWidth())
        self.inputMultiplyA.setSizePolicy(sizePolicy)
        self.inputMultiplyA.setMinimumSize(QtCore.QSize(0, 45))
        self.inputMultiplyA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputMultiplyA.setFont(MyFont().font)
        self.inputMultiplyA.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputMultiplyA.setStyleSheet(StyleBuilder().addBgColor((255, 255, 255))
                                          .addColor((0, 0, 0)).addBorderStyle("solid").addBorderRadius(5)
                                          .addBorderWidth(2).addBorderColor("black").build())
        self.inputMultiplyA.setAlignment(QtCore.Qt.AlignCenter)
        self.inputMultiplyA.setObjectName(str(ObjNames.inputMultiplyA.value))
        self.inputMultiplyA.clear()
        self.inputMultiplyA.setText("{:.1f}".format(1))
        self.inputMultiplyA.setMaxLength(4)
        self.inputMultiplyA.returnPressed.connect(lambda: checkFloatInput(self.inputMultiplyA, -9.9, 9.9))
        self.inputMultiplyA.editingFinished.connect(lambda: checkFloatInput(self.inputMultiplyA, -9.9, 9.9))
        self.horizontalLayout4.addWidget(self.inputMultiplyA)
        self.gridLayout2A.addLayout(self.horizontalLayout4, 2, 1, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName(str(ObjNames.horizontalLayout.value))

        # Текст
        self.textSizeA = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSizeA.sizePolicy().hasHeightForWidth())
        self.textSizeA.setSizePolicy(sizePolicy)
        self.textSizeA.setObjectName(str(ObjNames.textSizeA.value))
        self.horizontalLayout.addWidget(self.textSizeA)

        # Выпадающий список
        self.comboBoxSizeA1 = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSizeA1.sizePolicy().hasHeightForWidth())
        self.comboBoxSizeA1.setSizePolicy(sizePolicy)
        self.comboBoxSizeA1.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSizeA1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxSizeA1.setObjectName(str(ObjNames.comboBoxSizeA1.value))
        for x in range(9):
            self.comboBoxSizeA1.addItem("")
        self.comboBoxSizeA1.setCurrentIndex(2)
        self.horizontalLayout.addWidget(self.comboBoxSizeA1)

        # Текст
        self.textXA = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textXA.sizePolicy().hasHeightForWidth())
        self.textXA.setSizePolicy(sizePolicy)
        self.textXA.setObjectName(str(ObjNames.textXA.value))
        self.horizontalLayout.addWidget(self.textXA)

        # Выпадающий список
        self.comboBoxSizeA2 = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSizeA2.sizePolicy().hasHeightForWidth())
        self.comboBoxSizeA2.setSizePolicy(sizePolicy)
        self.comboBoxSizeA2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSizeA2.setObjectName(str(ObjNames.comboBoxSizeA2.value))
        for x in range(9):
            self.comboBoxSizeA2.addItem("")
        self.comboBoxSizeA2.setCurrentIndex(2)
        self.horizontalLayout.addWidget(self.comboBoxSizeA2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.gridLayout2A.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        # Кнопка Очистить
        self.pushButtonClearA = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClearA.sizePolicy().hasHeightForWidth())
        self.pushButtonClearA.setSizePolicy(sizePolicy)
        self.pushButtonClearA.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonClearA.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonClearA.setObjectName(str(ObjNames.pushButtonClearA.value))
        self.gridLayout2A.addWidget(self.pushButtonClearA, 0, 0, 1, 1)

        # Отрисовка матрицы A
        self.inputA = []
        self.redrawMatrix(Matrix.A)

        # Кнопка Транспонировать
        self.pushButtonTransposeA = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTransposeA.sizePolicy().hasHeightForWidth())
        self.pushButtonTransposeA.setSizePolicy(sizePolicy)
        self.pushButtonTransposeA.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonTransposeA.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonTransposeA.setObjectName(str(ObjNames.pushButtonTransposeA.value))
        self.gridLayout2A.addWidget(self.pushButtonTransposeA, 1, 0, 1, 1)

        # Кнопка Найти определитель
        self.pushButtonDeterminantA = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeterminantA.sizePolicy().hasHeightForWidth())
        self.pushButtonDeterminantA.setSizePolicy(sizePolicy)
        self.pushButtonDeterminantA.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonDeterminantA.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonDeterminantA.setObjectName(str(ObjNames.pushButtonDeterminantA.value))
        self.gridLayout2A.addWidget(self.pushButtonDeterminantA, 2, 0, 1, 1)

        # Кнопка Найти ранг
        self.pushButtonRankA = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRankA.sizePolicy().hasHeightForWidth())
        self.pushButtonRankA.setSizePolicy(sizePolicy)
        self.pushButtonRankA.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonRankA.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonRankA.setObjectName(str(ObjNames.pushButtonRankA.value))
        self.gridLayout2A.addWidget(self.pushButtonRankA, 3, 0, 1, 1)

        # Кнопка Обратная матрица
        self.pushButtonReverseA = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonReverseA.sizePolicy().hasHeightForWidth())
        self.pushButtonReverseA.setSizePolicy(sizePolicy)
        self.pushButtonReverseA.setMinimumSize(QtCore.QSize(40, 45))
        self.pushButtonReverseA.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonReverseA.setObjectName(str(ObjNames.pushButtonReverseA.value))
        self.gridLayout2A.addWidget(self.pushButtonReverseA, 3, 1, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName(str(ObjNames.horizontalLayout2.value))

        # Кнопка Возвести в степень
        self.pushButtonPowerA = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPowerA.sizePolicy().hasHeightForWidth())
        self.pushButtonPowerA.setSizePolicy(sizePolicy)
        self.pushButtonPowerA.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonPowerA.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonPowerA.setObjectName(str(ObjNames.pushButtonPowerA.value))
        self.horizontalLayout2.addWidget(self.pushButtonPowerA)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(spacerItem4)

        # Текст Ограничение значений множителя
        self.labelPowValLimitA = QtWidgets.QLabel(self.centralWidget)
        self.labelPowValLimitA.setStyleSheet(StyleBuilder().addFont(10, "Tahoma").build())
        self.labelPowValLimitA.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPowValLimitA.setObjectName(str(ObjNames.labelPowValLimitA.value))
        self.horizontalLayout2.addWidget(self.labelPowValLimitA)

        # Ввести показатель степени
        self.inputPowerA = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPowerA.sizePolicy().hasHeightForWidth())
        self.inputPowerA.setSizePolicy(sizePolicy)
        self.inputPowerA.setMinimumSize(QtCore.QSize(0, 45))
        self.inputPowerA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputPowerA.setFont(MyFont().font)
        self.inputPowerA.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputPowerA.setStyleSheet(StyleBuilder().addBgColor((255, 255, 255))
                                       .addColor((0, 0, 0)).addBorderStyle("solid").addBorderRadius(5)
                                       .addBorderWidth(2).addBorderColor("black").build())
        self.inputPowerA.setText("")
        self.inputPowerA.setMaxLength(2)
        self.inputPowerA.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPowerA.setPlaceholderText("")
        self.inputPowerA.setObjectName(str(ObjNames.inputPowerA.value))
        self.horizontalLayout2.addWidget(self.inputPowerA)
        self.inputPowerA.clear()
        self.inputPowerA.setText(str(1))
        self.inputPowerA.setMaxLength(2)
        self.inputPowerA.returnPressed.connect(lambda: checkIntInput(self.inputPowerA, -9, 9))
        self.inputPowerA.editingFinished.connect(lambda: checkIntInput(self.inputPowerA, -9, 9))
        self.gridLayout2A.addLayout(self.horizontalLayout2, 1, 1, 1, 1)
        self.verticalLayoutA.addLayout(self.gridLayout2A)
        self.horizontalLayoutAB.addLayout(self.verticalLayoutA)

        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAB.addItem(spacerItem6)

        # Вертикальный Layout
        self.verticalLayoutButtonsAB = QtWidgets.QVBoxLayout()
        self.verticalLayoutButtonsAB.setObjectName(str(ObjNames.verticalLayoutButtonsAB.value))
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutButtonsAB.addItem(spacerItem7)

        # Кнопка Сложить матрицы
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonAdd.setObjectName(str(ObjNames.pushButtonAdd.value))
        self.verticalLayoutButtonsAB.addWidget(self.pushButtonAdd)

        # Кнопка Вычесть матрицы
        self.pushButtonSub = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSub.setObjectName(str(ObjNames.pushButtonSub.value))
        self.verticalLayoutButtonsAB.addWidget(self.pushButtonSub)

        # Кнопка Перемножить матрицы
        self.pushButtonMul = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonMul.setObjectName(str(ObjNames.pushButtonMul.value))
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
        self.labelHeaderB = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeaderB.sizePolicy().hasHeightForWidth())
        self.labelHeaderB.setSizePolicy(sizePolicy)
        self.labelHeaderB.setStyleSheet(StyleBuilder().addFont(14, "Tahoma").build())
        self.labelHeaderB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeaderB.setObjectName(str(ObjNames.labelHeaderB.value))
        self.verticalLayoutB.addWidget(self.labelHeaderB)

        # Подзаголовок матрицы B
        self.labelSubHeaderB = QtWidgets.QLabel(self.centralWidget)
        sizePolicy.setHeightForWidth(self.labelSubHeaderA.sizePolicy().hasHeightForWidth())
        self.labelSubHeaderB.setSizePolicy(sizePolicy)
        self.labelSubHeaderB.setStyleSheet(StyleBuilder().addFont(10, "Tahoma").build())
        self.labelSubHeaderB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSubHeaderB.setObjectName(str(ObjNames.labelSubHeaderB.value))
        self.verticalLayoutB.addWidget(self.labelSubHeaderB)

        # Сетка Layout
        self.gridLayout2B = QtWidgets.QGridLayout()
        self.gridLayout2B.setObjectName(str(ObjNames.gridLayout2B.value))

        # Кнопка Очистить
        self.pushButtonClearB = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClearB.sizePolicy().hasHeightForWidth())
        self.pushButtonClearB.setSizePolicy(sizePolicy)
        self.pushButtonClearB.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonClearB.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonClearB.setObjectName(str(ObjNames.pushButtonClearB.value))
        self.gridLayout2B.addWidget(self.pushButtonClearB, 0, 0, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout3.setObjectName(str(ObjNames.horizontalLayout3.value))

        # Текст Размер
        self.textSizeB = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSizeB.sizePolicy().hasHeightForWidth())
        self.textSizeB.setSizePolicy(sizePolicy)
        self.textSizeB.setObjectName(str(ObjNames.textSizeB.value))
        self.horizontalLayout3.addWidget(self.textSizeB)

        # Выпадающий список
        self.comboBoxSizeB1 = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSizeB1.sizePolicy().hasHeightForWidth())
        self.comboBoxSizeB1.setSizePolicy(sizePolicy)
        self.comboBoxSizeB1.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSizeB1.setObjectName(str(ObjNames.comboBoxSizeB1.value))
        for x in range(9):
            self.comboBoxSizeB1.addItem("")
        self.comboBoxSizeB1.setCurrentIndex(2)
        self.horizontalLayout3.addWidget(self.comboBoxSizeB1)

        # Текст Х
        self.textXB = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textXB.sizePolicy().hasHeightForWidth())
        self.textXB.setSizePolicy(sizePolicy)
        self.textXB.setObjectName(str(ObjNames.textXB.value))
        self.horizontalLayout3.addWidget(self.textXB)

        # Выпадающий список
        self.comboBoxSizeB2 = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSizeB2.sizePolicy().hasHeightForWidth())
        self.comboBoxSizeB2.setSizePolicy(sizePolicy)
        self.comboBoxSizeB2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBoxSizeB2.setObjectName(str(ObjNames.comboBoxSizeB2.value))
        for x in range(9):
            self.comboBoxSizeB2.addItem("")
        self.comboBoxSizeB2.setCurrentIndex(2)
        self.horizontalLayout3.addWidget(self.comboBoxSizeB2)
        self.horizontalLayout3.setStretch(0, 1)
        self.horizontalLayout3.setStretch(1, 1)
        self.horizontalLayout3.setStretch(3, 1)
        self.gridLayout2B.addLayout(self.horizontalLayout3, 0, 1, 1, 1)

        # Отрисовка матрицы B
        self.inputB = []
        self.redrawMatrix(Matrix.B)

        # Кнопка Транспонировать
        self.pushButtonTransposeB = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTransposeB.sizePolicy().hasHeightForWidth())
        self.pushButtonTransposeB.setSizePolicy(sizePolicy)
        self.pushButtonTransposeB.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonTransposeB.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonTransposeB.setObjectName(str(ObjNames.pushButtonTransposeB.value))
        self.gridLayout2B.addWidget(self.pushButtonTransposeB, 1, 0, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout5.setObjectName(str(ObjNames.horizontalLayout5.value))

        # Кнопка Возвести в степень
        self.pushButtonPowerB = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPowerB.sizePolicy().hasHeightForWidth())
        self.pushButtonPowerB.setSizePolicy(sizePolicy)
        self.pushButtonPowerB.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonPowerB.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonPowerB.setObjectName(str(ObjNames.pushButtonPowerB.value))
        self.horizontalLayout5.addWidget(self.pushButtonPowerB)

        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout5.addItem(spacerItem10)

        # Текст Ограничение значений показателя степени
        self.labelPowValLimitB = QtWidgets.QLabel(self.centralWidget)
        self.labelPowValLimitB.setStyleSheet(StyleBuilder().addFont(10, "Tahoma").build())
        self.labelPowValLimitB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPowValLimitB.setObjectName(str(ObjNames.labelPowValLimitB.value))
        self.horizontalLayout5.addWidget(self.labelPowValLimitB)

        # Ввод показателя степени
        self.inputPowerB = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPowerB.sizePolicy().hasHeightForWidth())
        self.inputPowerB.setSizePolicy(sizePolicy)
        self.inputPowerB.setMinimumSize(QtCore.QSize(0, 45))
        self.inputPowerB.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ft = MyFont()
        self.inputPowerB.setFont(ft.font)
        self.inputPowerB.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputPowerB.setStyleSheet(StyleBuilder().addBgColor((255, 255, 255))
                                       .addColor((0, 0, 0)).addBorderStyle("solid").addBorderRadius(5)
                                       .addBorderWidth(2).addBorderColor("black").build())
        self.inputPowerB.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPowerB.setObjectName(str(ObjNames.inputPowerB.value))
        self.inputPowerB.clear()
        self.inputPowerB.setText(str(1))
        self.inputPowerB.setMaxLength(2)
        self.inputPowerB.returnPressed.connect(lambda: checkIntInput(self.inputPowerB, -9, 9))
        self.inputPowerB.editingFinished.connect(lambda: checkIntInput(self.inputPowerB, -9, 9))
        self.horizontalLayout5.addWidget(self.inputPowerB)
        self.gridLayout2B.addLayout(self.horizontalLayout5, 1, 1, 1, 1)

        # Кнопка Найти определитель
        self.pushButtonDeterminantB = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonDeterminantB.sizePolicy().hasHeightForWidth())
        self.pushButtonDeterminantB.setSizePolicy(sizePolicy)
        self.pushButtonDeterminantB.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonDeterminantB.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonDeterminantB.setObjectName(str(ObjNames.pushButtonDeterminantB.value))
        self.gridLayout2B.addWidget(self.pushButtonDeterminantB, 2, 0, 1, 1)

        # Горизонтальный Layout
        self.horizontalLayout6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout6.setObjectName(str(ObjNames.horizontalLayout6.value))

        # Кнопка Умножить
        self.pushButtonMultiplyB = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonMultiplyB.sizePolicy().hasHeightForWidth())
        self.pushButtonMultiplyB.setSizePolicy(sizePolicy)
        self.pushButtonMultiplyB.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonMultiplyB.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonMultiplyB.setObjectName(str(ObjNames.pushButtonMultiplyB.value))
        self.horizontalLayout6.addWidget(self.pushButtonMultiplyB)

        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout6.addItem(spacerItem12)

        # Текст Ограничение значений показателя степени
        self.labelMultiplierValLimitB = QtWidgets.QLabel(self.centralWidget)
        self.labelMultiplierValLimitB.setStyleSheet(StyleBuilder().addFont(10, "Tahoma").build())
        self.labelMultiplierValLimitB.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMultiplierValLimitB.setObjectName(str(ObjNames.labelMultiplierValLimitB.value))
        self.horizontalLayout6.addWidget(self.labelMultiplierValLimitB)

        # Ввод множителя
        self.inputMultiplyB = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputMultiplyB.sizePolicy().hasHeightForWidth())
        self.inputMultiplyB.setSizePolicy(sizePolicy)
        self.inputMultiplyB.setMinimumSize(QtCore.QSize(0, 45))
        self.inputMultiplyB.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.inputMultiplyB.setFont(MyFont().font)
        self.inputMultiplyB.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.inputMultiplyB.setStyleSheet(StyleBuilder().addBgColor((255, 255, 255))
                                          .addColor((0, 0, 0)).addBorderStyle("solid").addBorderRadius(5)
                                          .addBorderWidth(2).addBorderColor("black").build())
        self.inputMultiplyB.setAlignment(QtCore.Qt.AlignCenter)
        self.inputMultiplyB.setObjectName(str(ObjNames.inputMultiplyB.value))
        self.inputMultiplyB.clear()
        self.inputMultiplyB.setText("{:.1f}".format(1))
        self.inputMultiplyB.setMaxLength(4)
        self.inputMultiplyB.returnPressed.connect(lambda: checkFloatInput(self.inputMultiplyB, -9.9, 9.9))
        self.inputMultiplyB.editingFinished.connect(lambda: checkFloatInput(self.inputMultiplyB, -9.9, 9.9))
        self.horizontalLayout6.addWidget(self.inputMultiplyB)
        self.gridLayout2B.addLayout(self.horizontalLayout6, 2, 1, 1, 1)

        # Кнопка Найти ранг
        self.pushButtonRankB = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRankB.sizePolicy().hasHeightForWidth())
        self.pushButtonRankB.setSizePolicy(sizePolicy)
        self.pushButtonRankB.setMinimumSize(QtCore.QSize(165, 45))
        self.pushButtonRankB.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonRankB.setObjectName(str(ObjNames.pushButtonRankB.value))
        self.gridLayout2B.addWidget(self.pushButtonRankB, 3, 0, 1, 1)

        # Кнопка Обратная матрица
        self.pushButtonReverseB = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonReverseB.sizePolicy().hasHeightForWidth())
        self.pushButtonReverseB.setSizePolicy(sizePolicy)
        self.pushButtonReverseB.setMinimumSize(QtCore.QSize(40, 30))
        self.pushButtonReverseB.setStyleSheet(StyleBuilder().addMarginTop(2).addMarginBottom(2).build())
        self.pushButtonReverseB.setObjectName(str(ObjNames.pushButtonReverseB.value))
        self.gridLayout2B.addWidget(self.pushButtonReverseB, 3, 1, 1, 1)
        self.verticalLayoutB.addLayout(self.gridLayout2B)
        self.horizontalLayoutAB.addLayout(self.verticalLayoutB)

        spacerItem14 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAB.addItem(spacerItem14)

        self.verticalLayout.addLayout(self.horizontalLayoutAB)
        MainWindow.setCentralWidget(self.centralWidget)

        self.reTranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def reTranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelHeaderA.setText(_translate("MainWindow", "Введите матрицу А"))
        self.labelSubHeaderA.setText(_translate("MainWindow", "Введите числа от -99.9 до 99.9"))
        self.pushButtonMultiplyA.setText(_translate("MainWindow", "Умножить"))
        self.labelMultiplierValLimitA.setText(_translate("MainWindow", "min -9.9\nmax 9.9"))
        self.textSizeA.setText(_translate("MainWindow", "Размер"))
        self.comboBoxSizeA1.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSizeA1.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSizeA1.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSizeA1.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSizeA1.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSizeA1.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSizeA1.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSizeA1.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSizeA1.setItemText(8, _translate("MainWindow", "9"))
        self.textXA.setText(_translate("MainWindow", "x"))
        self.comboBoxSizeA2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSizeA2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSizeA2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSizeA2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSizeA2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSizeA2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSizeA2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSizeA2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSizeA2.setItemText(8, _translate("MainWindow", "9"))
        self.pushButtonClearA.setText(_translate("MainWindow", "Очистить"))
        self.pushButtonTransposeA.setText(_translate("MainWindow", "Транспонировать"))
        self.pushButtonDeterminantA.setText(_translate("MainWindow", "Найти определитель"))
        self.pushButtonRankA.setText(_translate("MainWindow", "Найти ранг"))
        self.pushButtonReverseA.setText(_translate("MainWindow", "Обратная матрица"))
        self.pushButtonPowerA.setText(_translate("MainWindow", "Возвести в степень"))
        self.labelPowValLimitA.setText(_translate("MainWindow", " min -9 \n max 9 "))
        self.pushButtonAdd.setText(_translate("MainWindow", "A + B"))
        self.pushButtonSub.setText(_translate("MainWindow", "A - B"))
        self.pushButtonMul.setText(_translate("MainWindow", "A x B"))
        self.labelHeaderB.setText(_translate("MainWindow", "Введите матрицу B"))
        self.labelSubHeaderB.setText(_translate("MainWindow", "Введите числа от -99.9 до 99.9"))
        self.pushButtonClearB.setText(_translate("MainWindow", "Очистить"))
        self.textSizeB.setText(_translate("MainWindow", "Размер"))
        self.comboBoxSizeB1.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSizeB1.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSizeB1.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSizeB1.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSizeB1.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSizeB1.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSizeB1.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSizeB1.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSizeB1.setItemText(8, _translate("MainWindow", "9"))
        self.textXB.setText(_translate("MainWindow", "x"))
        self.comboBoxSizeB2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxSizeB2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxSizeB2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxSizeB2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxSizeB2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxSizeB2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxSizeB2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxSizeB2.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxSizeB2.setItemText(8, _translate("MainWindow", "9"))
        self.pushButtonTransposeB.setText(_translate("MainWindow", "Транспонировать"))
        self.pushButtonPowerB.setText(_translate("MainWindow", "Возвести в степень"))
        self.labelPowValLimitB.setText(_translate("MainWindow", " min -9 \n max 9 "))
        self.pushButtonDeterminantB.setText(_translate("MainWindow", "Найти определитель"))
        self.pushButtonMultiplyB.setText(_translate("MainWindow", "Умножить"))
        self.labelMultiplierValLimitB.setText(_translate("MainWindow", "min -9.9\nmax 9.9"))
        self.pushButtonRankB.setText(_translate("MainWindow", "Найти ранг"))
        self.pushButtonReverseB.setText(_translate("MainWindow", "Обратная матрица"))

    def redrawMatrix(self, m: Matrix):
        if m.value == 1:
            # Сетка Layout
            self.gridLayout1B = QtWidgets.QGridLayout()
            self.gridLayout1B.setObjectName(str(ObjNames.gridLayout1B.value))
            gridlayout = self.gridLayout1B
            self.verticalLayoutB.insertLayout(2, self.gridLayout1B)
            combobox1 = self.comboBoxSizeB1
            combobox2 = self.comboBoxSizeB2
            lst = self.inputB
            lst.clear()
        else:
            # Сетка Layout
            self.gridLayout1A = QtWidgets.QGridLayout()
            self.gridLayout1A.setObjectName(str(ObjNames.gridLayout1A.value))
            gridlayout = self.gridLayout1A
            self.verticalLayoutA.insertLayout(2, self.gridLayout1A)
            combobox1 = self.comboBoxSizeA1
            combobox2 = self.comboBoxSizeA2
            lst = self.inputA
            lst.clear()

        for i in range(combobox1.currentIndex() + 1):
            buf = []
            for j in range(combobox2.currentIndex() + 1):
                lineInput = QtWidgets.QLineEdit(self.centralWidget)
                buf.append(lineInput)
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
                lst[i][j].setObjectName(str(ObjNames.inputA.value) + str(i) + str(j))
                gridlayout.addWidget(lst[i][j], i, j + 1, 1, 1)
                lst[i][j].clear()
                lst[i][j].setText("{:.1f}".format(0))
                lst[i][j].setMaxLength(5)
                lst[i][j].returnPressed.connect(
                    (functools.partial(checkFloatInput, lst[i][j], -99.9, 99.9)))
                lst[i][j].editingFinished.connect(
                    (functools.partial(checkFloatInput, lst[i][j], -99.9, 99.9)))


class MyMessageBox(QtWidgets.QMessageBox):
    def __init__(self, result=None):
        if result is None:
            result = []
        self.rows = len(result) if isinstance(result, list) else 0
        self.columns = len(result[0]) if isinstance(result, list) else 0
        self.rnd = lambda x: str(float(f"{x:.10f}")) if abs(float(f"{x}") - float(f"{x:.10f}")) < 1e-10 else str(
            float(f"{x}"))
        self.maxElemLen = max([max([len(self.rnd(result[i][j]))
                                    for i in range(self.rows)])
                               for j in range(self.columns)]) if isinstance(result, list) else 0
        QtWidgets.QMessageBox.__init__(self)
        self.setSizeGripEnabled(True)
        self.setWindowTitle("Результат")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon_matrix.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def addTableWidget(self, parentItem: QMessageBox, result: list):
        self.layout = QtWidgets.QHBoxLayout()
        self.tableWidget = QtWidgets.QTableWidget(parentItem)
        self.tableWidget.setObjectName(str(ObjNames.tableWidget.value))
        self.tableWidget.setColumnCount(self.columns)
        self.tableWidget.setRowCount(self.rows)
        for x in range(self.rows):
            for y in range(self.columns):
                self.tableWidget.setColumnWidth(y, (self.maxElemLen + 2) * 9)
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
        self.tableWidget.resize(self.columns * ((self.maxElemLen + 2) * 9) + 2, (self.rows * 30) + 2)
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
        if self.rows != 0 and self.columns != 0 and self.maxElemLen > 1:
            self.resize(self.columns * ((self.maxElemLen + 2) * 9) + 6, (self.rows * 30) + 48)
        return result
