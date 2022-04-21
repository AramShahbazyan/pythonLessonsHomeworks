num = int(input('Input number: '))
matrix = []
for i in range(num):
    row_1 = ['.' for _ in range(num)]
    matrix.append(row_1)
for j in range(0, int(len(matrix)/2), 2):
    for i in range(j, len(matrix)-j):

        matrix[j][i-1] = ">"
        matrix[i][-j-1] = "v"
        matrix[-j-1][i] = "<"
        if i > j + 1:
            matrix[i][j] = "^"
for i in matrix:
    print(i)