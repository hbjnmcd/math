import fire
import numpy as np
from gauss import Gauss


def create():
    """
    Ввод матрицы
    """
    print('Введите количество уравнений')
    lot = int(input())
    a = np.empty((lot, lot + 1), dtype='object')
    for number in range(0, lot):
        print(f'Введите коэффициенты и свободный член строки {number+1} через запятую без пробелов')
        strings = input().split(',')
        b = [float(s) for s in strings]
        a[number, :] = b
    print(f'Введённая матрица: \n {a} \n')
    return a, lot


if __name__ == '__main__':
    gauss = Gauss(create())
    fire.Fire(gauss)
