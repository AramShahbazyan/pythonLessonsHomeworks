from random import randint


def sum_list(ls: list):
    sum_ls = 0
    for i in ls:
        sum_ls += i
    return sum_ls


def corner(num: int):
    matrix = []
    for i in range(num):
        row_1 = [randint(10, 99) for j in range(num)]
        matrix.append(row_1)
    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            if x == y:
                matrix[x][y] = sum_list(matrix[x])
    for c in matrix:
        print(c)
    return matrix


corner(10)
