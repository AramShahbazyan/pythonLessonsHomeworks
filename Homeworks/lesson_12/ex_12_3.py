# Գրել ֆունկցիա որը կստանա,ոչ բացասական թվերի մատրիցա։ Հաշվեք յուրաքանչյուր սյունակի տարրերի գումարը:
# Որոշեք, թե որ սյունակն է պարունակում առավելագույն գումարը:
# Գտեք այդ ցյունակի ամենափոքր էլեմենտը, ֆունկցիան պետք ե վերադարձնի այդ էլեմենտի արժեքը։

from random import randint


def matrix(x: int):
    mat = []
    for i in range(x):
        list_2 = [randint(1, 100) for _ in range(10)]
        mat.append(list_2)
    for i in mat:
        print(i)
    return mat


def sum_col(my_matrix: list):
    list_sum = []
    for i in range(len(my_matrix)):
        column_sum = 0
        for j in range(len(my_matrix)):
            column_sum += my_matrix[j][i]
        list_sum.append(column_sum)
    print(list_sum)
    max_sum_column_index = (list_sum.index(max(list_sum)))
    print(max_sum_column_index)

    my_list = []
    for i in range(len(my_matrix)):
        my_list.append(my_matrix[i][max_sum_column_index])
    print(my_list)
    sort_list = sorted(my_list)
    print(sort_list[0])


sum_col(matrix(10))
