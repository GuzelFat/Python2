"""Напишите функцию для транспонирования матрицы"""


def trans_matrix(matr: list) -> list:
    transposed_matrix = []
    matrix_cols_count = len(matr)
    matrix_rows_count = len(matr[0])

    for i in range(matrix_rows_count):
        transposed_matrix.append([])
        for j in range(matrix_cols_count):
            transposed_matrix[i].append(matr[j][i])

    return transposed_matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5],
              [11, 22, 33, 44, 55],
              [111, 222, 333, 444, 555],
              [1111, 2222, 3333, 4444, 5555]]

    new_matrix = trans_matrix(matrix)

    for col in matrix:
        print(*col)
    print(f'{"-" * 20}>')
    for col in new_matrix:
        print(*col)