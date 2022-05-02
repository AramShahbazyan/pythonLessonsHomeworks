# Գրել ֆունկցիա որը կստանա մատրիցա  և կսորտավորի  սյունակների հերթականությունը,
# որպեսզի դրանց առաջին սյունակի տարրերը դասավորված լինեն աճման կարգով:

from random import randint


def matrix(mat_len: int):
    mat = []
    for i in range(mat_len):
        mat_ls = [randint(10, 99) for i in range(mat_len)]
        mat.append(mat_ls)
    for i in mat:
        print(i)
    print()
    return mat


def sort_mat(mat: list):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][0] < mat[j][0]:
                for x in range(len(mat)):
                    mat[i][x], mat[j][x] = mat[j][x], mat[i][x]

    for i in mat:
        print(i)


sort_mat(matrix(5))
