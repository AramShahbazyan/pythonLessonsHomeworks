# Գրել ֆունկցիա որը կստանա,ոչ բացասական թվերի մատրիցա։ Հաշվեք յուրաքանչյուր սյունակի
# տարրերի գումարը: Որոշեք, թե որ սյունակն է պարունակում առավելագույն գումարը:
# Ֆունկցիան պետք է վերագարձնի ամենամեծ գումարը և համապատասխան սյունակի հերթական համարը։
#
from random import randint


def matrix(x: int):
    mat = []
    for i in range(x):
        list_2 = [randint(1, 100) for _ in range(10)]
        mat.append(list_2)
    for i in mat:
        print(i)
    return mat


def sum_col(matrix1: list):
    list_sum = []
    for i in range(len(matrix1)):
        column_sum = 0
        for j in range(len(matrix1)):
            column_sum += matrix1[j][i]
        list_sum.append(column_sum)
    print(list_sum)
    return list_sum


def max_and_index(ls: list):
    print(max(ls))
    print(ls.index(max(ls)))


max_and_index(sum_col(matrix(10)))
