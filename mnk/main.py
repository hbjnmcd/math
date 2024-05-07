import tabulate


def input_matrix_x(m, n):
    X = []
    for i in range(m):
        X.append([0] * (n))
    for i in range(m):
        X[i][0] = 1
        X[i][1] = float(input('Введите x: '))
        for j in range(2, n):
            X[i][j] = X[i][1] ** j
    print('Матрица факторных признаков:\n', tabulate.tabulate(X))
    return X


def input_matrix_y(m):
    arr = []
    n = 1
    for i in range(m):
        arr.append([0] * n)
    for i in range(m):
        for j in range(n):
            arr[i][j] = float(input('Введите y: '))
    print('Матрица результирующих признаков:\n', tabulate.tabulate(arr))
    return arr


def transpose_matrix(array):
    trans_matrix = [[0 for j in range(len(array))] for i in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            trans_matrix[j][i] = array[i][j]
    return trans_matrix


def multiply_matrix(arr1, arr2):
    s = 0
    rows_a, cols_a = len(arr1), len(arr1[0])
    rows_b, cols_b = len(arr2), len(arr2[0])
    result_of_multiply = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    if cols_a != rows_b:
        raise ValueError("Невозможно перемножить матрицы: размеры не соответствуют.")
    else:
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result_of_multiply[i][j] += arr1[i][k] * arr2[k][j]
    return result_of_multiply


def get_matrix_minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def get_matrix_deternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*get_matrix_deternminant(get_matrix_minor(m, 0, c))
    return determinant


def get_matrix_inverse(m):
    determinant = get_matrix_deternminant(m)
    if determinant == 0:
        raise ValueError('Детерминант равен 0')
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactor_row = []
        for c in range(len(m)):
            minor = get_matrix_minor(m, r, c)
            cofactor_row.append(((-1)**(r+c)) * get_matrix_deternminant(minor))
        cofactors.append(cofactor_row)
    disjoint = transpose_matrix(cofactors)
    
    for r in range(len(disjoint)):
        for c in range(len(disjoint)):
            disjoint[r][c] = disjoint[r][c]/determinant
    return disjoint


if __name__ == '__main__':
    m = int(input('Введите количество измерений: '))
    n = int(input('Введите степень полинома: '))

    X = input_matrix_x(m,n)
    Y = input_matrix_y(m)

    print(f'По условиям задачи нужно получить матрицу коэффициентов,'
          f'которая будет являться вектор-столбцом\n')

    X_t = transpose_matrix(X)
    print('Транспонированная матрица X:\n', tabulate.tabulate(X_t))

    X_t_X = multiply_matrix(X_t,X)
    print('Результат перемножения транспонированной и обычной матрицы X, или матрица C:\n', tabulate.tabulate(X_t_X))

    C_1 = get_matrix_inverse(X_t_X)
    print('Обратная матрица для матрицы C:\n', tabulate.tabulate(C_1))

    X_t_Y = multiply_matrix(X_t, Y)
    print('Результат перемножения транспонированной матрицы X и Y:\n', tabulate.tabulate(X_t_Y))

    A = multiply_matrix(C_1, X_t_Y)
    print('Матрица искомых коэффициентов A:\n', tabulate.tabulate(A))

    res = multiply_matrix(X, A)
    print('Проверка:\n', tabulate.tabulate(res))




    






