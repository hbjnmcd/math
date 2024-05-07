import numpy as np

class Gauss:
    """
    Решение СЛАУ методом Гаусса
    """
    def __init__(self, arr):
        self.matrix = arr[0]
        self.size = arr[1]

    def classic(self):
        """
        Классический метод Гаусса при решении СЛАУ
        """
        print('Классический метод.')
        temp_matrix = np.copy(self.matrix)
        for i in range(0, self.size - 1):
            for j in range(self.size, i - 1, -1):
                temp_matrix[i, j] = temp_matrix[i, j] / temp_matrix[i, i]
                for k in range(i + 1, self.size):
                    temp_matrix[k, j] -= temp_matrix[i, j] * temp_matrix[k, i]
        print(f'Получившаяся матрица: \n {temp_matrix} \n')
        x = list(range(0, self.size))
        x[self.size - 1] = temp_matrix[self.size - 1, self.size] / temp_matrix[self.size - 1, self.size - 1]
        for i in range(self.size - 2, -1, -1):
            s = 0
            for j in range(i + 1, self.size):
                s += temp_matrix[i, j] * x[j]
            x[i] = temp_matrix[i, self.size] - s
        res = [round(ans, 3) for ans in x]
        print(f'Результат: \n {res} \n')
        return res

    def optimal(self):
        """
        Метод оптимального исключения Гаусса
        """
        print('Метод оптимального исключения Гаусса.')
        temp_matrix = np.copy(self.matrix)
        for i in range(0, self.size - 1):
            for k in range(i + 1, self.size):
                c = temp_matrix[k, i] / temp_matrix[i, i]
                for j in range(i, self.size + 1):
                    temp_matrix[k, j] -= c * temp_matrix[i, j]
        print(f'Получившаяся матрица: \n {temp_matrix} \n')
        x = list(range(0, self.size))
        x[self.size - 1] = temp_matrix[self.size - 1, self.size] / temp_matrix[self.size - 1, self.size - 1]
        for i in range(self.size-2, -1, -1):
            s = 0
            for j in range(i + 1, self.size):
                s += temp_matrix[i, j]*x[j]
            x[i] = (temp_matrix[i, self.size] - s)/temp_matrix[i, i]
        res = [round(ans, 3) for ans in x]
        print(f'Результат: \n {res} \n')
        return res

    def jordan(self):
        """
        Метод Гаусса-Жордана
        """
        print('Метод Гаусса-Жордана.')
        temp_matrix = np.copy(self.matrix)
        for i in range(0, self.size):
            for k in range(0, self.size):
                if i == k:
                    pass
                else:
                    c = temp_matrix[k, i] / temp_matrix[i, i]
                    for j in range(i, self.size + 1):
                        temp_matrix[k, j] -= c * temp_matrix[i, j]
        print(f'Получившаяся матрица: \n {temp_matrix} \n')
        x = list(range(0, self.size))
        for i in range(0, self.size):
            x[i] = temp_matrix[i, self.size]/temp_matrix[i, i]
        res = [round(ans, 3) for ans in x]
        print(f'Результат: \n {res} \n')
        return res
