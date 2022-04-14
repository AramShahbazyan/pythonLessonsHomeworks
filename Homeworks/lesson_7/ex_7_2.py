# Գտե՛ք թվերի հետևյալ շարքի n տարրերի գումարը՝ 1 -0,5 0,25 -0,125 ... Ստեղնաշարից մուտքագրվում է տարրերի թիվը (n):

count_n = int(input('please input n value: '))
x = 1
sum_n = 1
n = 1
while x < count_n:
    n = n / -2
    sum_n += n
    x += 1
print(sum_n)
