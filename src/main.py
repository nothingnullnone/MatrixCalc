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

        self.ui.comboBoxSize_a1.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.A))
        self.ui.comboBoxSize_a2.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.A))

        self.ui.comboBoxSize_b1.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.B))
        self.ui.comboBoxSize_b2.currentIndexChanged.connect(lambda: self.redraw_matrix(Matrix.B))

        self.ui.pushButtonClear_a.clicked.connect(lambda: self.clear_matrix(Matrix.A))
        self.ui.pushButtonClear_b.clicked.connect(lambda: self.clear_matrix(Matrix.B))

        self.ui.pushButtonTranspond_a.clicked.connect(lambda: self.transponse_matrix(Matrix.A))
        self.ui.pushButtonTranspond_b.clicked.connect(lambda: self.transponse_matrix(Matrix.B))

        self.ui.pushButtonMultiply_a.clicked.connect(lambda: self.scalarmul_matrix(Matrix.A))
        self.ui.pushButtonMultiply_b.clicked.connect(lambda: self.scalarmul_matrix(Matrix.B))

        self.ui.pushButtonPower_a.clicked.connect(lambda: self.power_matrix(Matrix.A))
        self.ui.pushButtonPower_b.clicked.connect(lambda: self.power_matrix(Matrix.B))

        self.ui.pushButtonDeterminant_a.clicked.connect(lambda: self.determine_matrix(Matrix.A))
        self.ui.pushButtonDeterminant_b.clicked.connect(lambda: self.determine_matrix(Matrix.B))

        self.ui.pushButtonRank_a.clicked.connect(lambda: self.rank_matrix(Matrix.A))
        self.ui.pushButtonRank_b.clicked.connect(lambda: self.rank_matrix(Matrix.B))

        self.ui.pushButtonReverse_a.clicked.connect(lambda: self.invert_matrix(Matrix.A))
        self.ui.pushButtonReverse_b.clicked.connect(lambda: self.invert_matrix(Matrix.B))

        self.ui.pushButtonAdd.clicked.connect(lambda: self.add_matrix(Matrix.A, Matrix.B))
        self.ui.pushButtonSub.clicked.connect(lambda: self.sub_matrix(Matrix.A, Matrix.B))
        self.ui.pushButtonMul.clicked.connect(lambda: self.mul_matrix(Matrix.A, Matrix.B))

    def clear_matrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                for i in range(len(self.ui.input_a)):
                    for j in range(len(self.ui.input_a[0])):
                        self.ui.input_a[i][j].clear()
                        self.ui.input_a[i][j].setText("0")
            case 1:
                for i in range(len(self.ui.input_b)):
                    for j in range(len(self.ui.input_b[0])):
                        self.ui.input_b[i][j].clear()
                        self.ui.input_b[i][j].setText("0")
            case _:
                pass

    def redraw_matrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                input_ = self.ui.input_a
                grid = self.ui.gridLayout1_a
            case 1:
                input_ = self.ui.input_b
                grid = self.ui.gridLayout1_b
            case _:
                return
        for i in range(len(input_)):
            for j in range(len(input_[0])):
                grid.removeWidget(input_[i][j])
                input_[i][j].deleteLater()
                grid.deleteLater()
        self.ui.redraw_matrix(m)

    def read_matrix(self, m: Matrix) -> list:
        match m.value:
            case 0:
                input_ = self.ui.input_a
            case 1:
                input_ = self.ui.input_b
            case _:
                input_ = self.ui.input_a
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

    def scalarmul_matrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                n = float(self.ui.inputMultiply_a.text())
            case 1:
                n = float(self.ui.inputMultiply_b.text())
            case _:
                n = 1
        self.show_result(scalarmul(self.read_matrix(m), n))

    def power_matrix(self, m: Matrix) -> None:
        match m.value:
            case 0:
                n = int(self.ui.inputPower_a.text())
            case 1:
                n = int(self.ui.inputPower_b.text())
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
