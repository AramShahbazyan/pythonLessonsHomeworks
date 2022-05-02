# Գրել ֆունկցիա որը կստանա երկու հավասար չափի մատրիցա: Նույն չափի երրորդ մատրիցայի բջիջներում
# գրեք ավելի մեծ տարրեր առաջին երկու մատրիցների համապատասխան բջիջներից:
# Օրինակ, եթե առաջին մատրիցայի երրորդ շարքի երկրորդ բջիջը պարունակում է 89 թիվը,
# իսկ երկրորդ մատրիցայի նույն ցուցիչով բջիջը պարունակում է 10 թիվը,
# ապա երրորդի նույն բջիջում պետք է գրվի 89 թիվը։ Ֆունկցիան պետք է վերադարձնի երրորդ մատրիցան։


from random import randint


def first_matrix(mat_range: int):
    mat_1 = []
    for i in range(mat_range):
        mat_1_list = [randint(10, 99) for _ in range(mat_range)]
        mat_1.append(mat_1_list)
    for j in mat_1:
        print(j)
    print()
    return mat_1


def second_matrix(mat_range: int):
    mat_2 = []
    for i in range(mat_range):
        mat_2_list = [randint(10, 99) for _ in range(mat_range)]
        mat_2.append(mat_2_list)
    for j in mat_2:
        print(j)
    print()
    return mat_2


def third_mat(mat1: list, mat2: list):
    mat_3 = []
    for i in range(len(mat1)):
        mat_3_list = []
        for j in range(len(mat1)):
            if mat1[i][j] > mat2[i][j]:
                mat_3_list.append(mat1[i][j])
            else:
                mat_3_list.append(mat2[i][j])
        mat_3.append(mat_3_list)
    for i in mat_3:
        print(i)


third_mat(first_matrix(10), second_matrix(10))
