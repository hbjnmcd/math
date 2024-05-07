import fire
import numpy as np
from gauss import Gauss


def create():
    print('Введите количество уравнений:')
    lot = int(input())
    a = np.empty((lot, lot + 1), dtype='object')
    for num in range(0, lot):
        print(f'Введите коэффициенты и свободный член {num+1} строки через запятую')
        strings = input().split(',')
        b = [float(s.strip()) for s in strings]
        a[num, :] = b
    print(f'Введённая матрица: \n {a} \n')
    return a, lot


if __name__ == '__main__':
    gauss = Gauss(create())
    gauss.classic()
    gauss.optimal()
    gauss.jordan()