import sys

from PyQt5 import QtWidgets
from matrix import *
from ui_main import Ui_MainWindow, MyMessageBox, Matrix, MyFont


class MatrixCalc(QtWidgets.QMainWindow):
    def __init__(self):
        super(MatrixCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Калькулятор матриц")

        self.ui.comboBoxSizeA1.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.A))
        self.ui.comboBoxSizeA2.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.A))

        self.ui.comboBoxSizeB1.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.B))
        self.ui.comboBoxSizeB2.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.B))

        self.ui.pushButtonClearA.clicked.connect(lambda: self.clear_matrix(Matrix.A))
        self.ui.pushButtonClearB.clicked.connect(lambda: self.clear_matrix(Matrix.B))

        self.ui.pushButtonTransposeA.clicked.connect(lambda: self.transponse_matrix(Matrix.A))
        self.ui.pushButtonTransposeB.clicked.connect(lambda: self.transponse_matrix(Matrix.B))

        self.ui.pushButtonMultiplyA.clicked.connect(lambda: self.scalarMulMatrix(Matrix.A))
        self.ui.pushButtonMultiplyB.clicked.connect(lambda: self.scalarMulMatrix(Matrix.B))

        self.ui.pushButtonPowerA.clicked.connect(lambda: self.power_matrix(Matrix.A))
        self.ui.pushButtonPowerB.clicked.connect(lambda: self.power_matrix(Matrix.B))

        self.ui.pushButtonDeterminantA.clicked.connect(lambda: self.determine_matrix(Matrix.A))
        self.ui.pushButtonDeterminantB.clicked.connect(lambda: self.determine_matrix(Matrix.B))

        self.ui.pushButtonRankA.clicked.connect(lambda: self.rank_matrix(Matrix.A))
        self.ui.pushButtonRankB.clicked.connect(lambda: self.rank_matrix(Matrix.B))

        self.ui.pushButtonReverseA.clicked.connect(lambda: self.invert_matrix(Matrix.A))
        self.ui.pushButtonReverseB.clicked.connect(lambda: self.invert_matrix(Matrix.B))

        self.ui.pushButtonAdd.clicked.connect(lambda: self.add_matrix(Matrix.A, Matrix.B))
        self.ui.pushButtonSub.clicked.connect(lambda: self.sub_matrix(Matrix.A, Matrix.B))
        self.ui.pushButtonMul.clicked.connect(lambda: self.mul_matrix(Matrix.A, Matrix.B))

    def clear_matrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                for i in range(len(self.ui.inputA)):
                    for j in range(len(self.ui.inputA[0])):
                        self.ui.inputA[i][j].clear()
                        self.ui.inputA[i][j].setText(str(0))
            case 1:
                for i in range(len(self.ui.inputB)):
                    for j in range(len(self.ui.inputB[0])):
                        self.ui.inputB[i][j].clear()
                        self.ui.inputB[i][j].setText(str(0))
            case _:
                pass

    def redraw_matrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                input_ = self.ui.inputA
                grid = self.ui.gridLayout1A
            case 1:
                input_ = self.ui.inputB
                grid = self.ui.gridLayout1B
            case _:
                return
        for i in range(len(input_)):
            for j in range(len(input_[0])):
                grid.removeWidget(input_[i][j])
                input_[i][j].deleteLater()
                grid.deleteLater()
        self.ui.redrawMatrix(m)

    def read_matrix(self, m: Matrix) -> list:
        match m.value:
            case 0:
                input_ = self.ui.inputA
            case 1:
                input_ = self.ui.inputB
            case _:
                input_ = self.ui.inputA
        matrix = []
        for i in range(len(input_)):
            lst = []
            for j in range(len(input_[0])):
                lst.append(float(input_[i][j].text()))
            matrix.append(lst)
        return matrix

    def transponse_matrix(self, m: Matrix) -> None:
        self.show_result(transponse(self.read_matrix(m)))

    def determine_matrix(self, m: Matrix) -> None:
        self.show_result(determinant(self.read_matrix(m)))

    def rank_matrix(self, m: Matrix) -> None:
        self.show_result(rank(self.read_matrix(m)))

    def scalarMulMatrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                n = float(self.ui.inputMultiplyA.text())
            case 1:
                n = float(self.ui.inputMultiplyB.text())
            case _:
                n = 1
        self.show_result(scalarmul(self.read_matrix(m), n))

    def power_matrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                n = int(self.ui.inputPowerA.text())
            case 1:
                n = int(self.ui.inputPowerB.text())
            case _:
                n = 1
        self.show_result(power(self.read_matrix(m), n))

    def add_matrix(self, m1: Matrix, m2: Matrix) -> None:
        self.show_result(matrix_add_sub(self.read_matrix(m1), self.read_matrix(m2)))

    def sub_matrix(self, m1: Matrix, m2: Matrix) -> None:
        self.show_result(matrix_add_sub(self.read_matrix(m1), self.read_matrix(m2), False))

    def mul_matrix(self, m1: Matrix, m2: Matrix) -> None:
        self.show_result(matrix_mul(self.read_matrix(m1), self.read_matrix(m2)))

    def invert_matrix(self, m: Matrix) -> None:
        self.show_result(invert(self.read_matrix(m)))

    def show_result(self, result):
        ft = MyFont()
        if isinstance(result, list):
            msg = MyMessageBox(result)
            msg.addTableWidget(msg, result)
        else:
            msg = MyMessageBox(result)
            result_txt = str(result)
            msg.setText(f"{result_txt}")
        msg.setFont(ft.font)
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MatrixCalc()
    window.show()
    sys.exit(app.exec())
