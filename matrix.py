from numpy.linalg import matrix_rank, inv, LinAlgError
from numpy import eye


def transponse(m=None):
    if m is None:
        m = []
    try:
        if m:
            transponded = [[m[x][y] for x in range(len(m))] for y in range(len(m[0]))]
            return transponded
        else:
            return "Ошибка! Введите матрицу"
    except AttributeError:
        return "Ошибка! Введите матрицу"


def determinant(m=None, mul=1):
    if m is None:
        m = []
    try:
        if m:
            if len(m) == len(m[0]):
                width = len(m)
                if width == 1:
                    return mul * m[0][0]
                else:
                    sign = -1
                    answer = 0
                    for i in range(width):
                        minor = []
                        for j in range(1, width):
                            buff = []
                            for k in range(width):
                                if k != i:
                                    buff.append(m[j][k])
                            minor.append(buff)
                        sign *= -1
                        answer = answer + mul * determinant(minor, sign * m[0][i])
                result = answer
                return result
            else:
                return "Ошибка! Введите квадратную матрицу!"
        else:
            return "Ошибка! Введите матрицу"
    except TypeError:
        return "Ошибка! Введите матрицу"


def matrix_mul(a=None, b=None):
    if b is None:
        b = []
    if a is None:
        a = []
    if a and b:
        if len(a[0]) == len(b):
            res = []
            for i in range(len(a)):
                row = []
                for j in range(len(b[0])):
                    n = 0
                    for k in range(len(b)):
                        n += (a[i][k] * b[k][j])
                    row.append(n)
                res.append(row)
            return res
        else:
            return "Ошибка! Число столбцов первой матрицы должно совпадать с числом строк второй матрицы!"
    else:
        return "Ошибка! Введите матрицу"


def matrix_add_sub(a=None, b=None, sign=True):
    if b is None:
        b = []
    if a is None:
        a = []
    if a and b:
        if len(a[0]) == len(b[0]) & len(a) == len(b):
            res = []
            for i in range(len(a)):
                row = []
                for j in range(len(a[0])):
                    if sign:
                        row.append(a[i][j] + b[i][j])
                    else:
                        row.append(a[i][j] - b[i][j])
                res.append(row)
            return res
        else:
            return "Ошибка! При сложении или вычитании, матрицы должны иметь одинаковый размер!"
    else:
        return "Ошибка! Введите матрицу"


def rank(m=None):
    if m is None:
        m = []
    try:
        if m:
            return matrix_rank(m)
        else:
            return "Ошибка! Введите матрицу"
    except AttributeError:
        return "Ошибка! Введите матрицу"


def invert(m=None):
    if m is None:
        m = []
    try:
        if m:
            if len(m[0]) == len(m):
                return inv(m).tolist()
            else:
                return "Ошибка! Количество строк не равно количеству столбцов!"
        else:
            return "Ошибка! Введите матрицу"
    except AttributeError:
        return "Ошибка! Введите матрицу"
    except LinAlgError:
        return "Вырожденная матрица - обратной матрицы не существует!"


def scalarmul(m=None, n=1):
    if m is None:
        m = []
    try:
        if m:
            res = [[m[y][x] * n for x in range(len(m[0]))] for y in range(len(m))]
            return res
        else:
            return "Ошибка! Введите матрицу"
    except AttributeError:
        return "Ошибка! Введите матрицу"


def power(m=None, n=1):
    if m is None:
        m = []
    try:
        if m:
            if len(m[0]) == len(m):
                match n:
                    case _ if n == 0:
                        res = eye(len(m), len(m))
                    case _ if n > 0:
                        res = list(m)
                        for i in range(n - 1):
                            res = matrix_mul(m, res)
                    case _ if n < 0:
                        res = list(m)
                        for i in range(n*(-1) - 1):
                            res = matrix_mul(m, res)
                        res = invert(res)
                return res
            else:
                return "Ошибка! Количество строк не равно количеству столбцов!"
        else:
            return "Ошибка! Введите матрицу"
    except AttributeError:
        return "Ошибка! Введите матрицу"
