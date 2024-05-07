class Gauss:
    """
    Решение СЛАУ методом Гаусса
    """
    def __init__(self, arr):
        self.matrix = arr[0]
        self.size = arr[1]

    def classical(self):
        """
        Классический метод Гаусса при решении СЛАУ
        """
        print('Классический метод')
        for i in range(0, self.size - 1):
            for j in range(self.size, i - 1, -1):
                self.matrix[i, j] = self.matrix[i, j] / self.matrix[i, i]
                for k in range(i + 1, self.size):
                    self.matrix[k, j] -= self.matrix[i, j] * self.matrix[k, i]
        print(f'Матрица в результате прямого хода: \n {self.matrix} \n')
        x = list(range(0, self.size))
        x[self.size - 1] = self.matrix[self.size - 1, self.size] / self.matrix[self.size - 1, self.size - 1]
        for i in range(self.size - 2, -1, -1):
            s = 0
            for j in range(i + 1, self.size):
                s += self.matrix[i, j] * x[j]
            x[i] = self.matrix[i, self.size] - s
        res = [round(ans, 3) for ans in x]
        print(f'Результат: \n {res} \n')
        return res

    def optimal(self):
        """
        Оптимальный метод Гаусса при решении СЛАУ
        """
        print('Оптимальный метод')
        for i in range(0, self.size - 1):
            for k in range(i + 1, self.size):
                c = self.matrix[k, i] / self.matrix[i, i]
                for j in range(i, self.size + 1):
                    self.matrix[k, j] -= c * self.matrix[i, j]
        print(f'Матрица в результате прямого хода: \n {self.matrix} \n')
        x = list(range(0, self.size))
        x[self.size - 1] = self.matrix[self.size - 1, self.size] / self.matrix[self.size - 1, self.size - 1]
        for i in range(self.size-2, -1, -1):
            s = 0
            for j in range(i + 1, self.size):
                s += self.matrix[i, j]*x[j]
            x[i] = (self.matrix[i, self.size] - s)/self.matrix[i, i]
        res = [round(ans, 3) for ans in x]
        print(f'Результат: \n {res} \n')
        return res

    def jordan(self):
        """
        Метод Гаусса-Жордана при решении СЛАУ
        """
        print('Метод Гаусса-Жордана')
        for i in range(0, self.size):
            for k in range(0, self.size):
                if i == k:
                    pass
                else:
                    c = self.matrix[k, i] / self.matrix[i, i]
                    for j in range(i, self.size + 1):
                        self.matrix[k, j] -= c * self.matrix[i, j]
        print(f'Матрица в результате прямого хода: \n {self.matrix} \n')
        x = list(range(0, self.size))
        for i in range(0, self.size):
            x[i] = self.matrix[i, self.size]/self.matrix[i, i]
        res = [round(ans, 3) for ans in x]
        print(f'Результат: \n {res} \n')
        return res
