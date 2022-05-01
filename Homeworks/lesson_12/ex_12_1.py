# Գրել ֆունկցիա որը կհաշվի n անդամներով ֆիբոնաչիի շարքի թվաբանական միջինը։

def fibonachi(n: int):
    list_fib = []
    x = 1
    y = 1
    for i in range(1, n + 1):
        if i == 1:
            fib_num = x
        elif i == 2:
            fib_num = y
        else:
            fib_num = x + y
            x = y
            y = fib_num
        list_fib.append(fib_num)
    return list_fib


def average_fib(ls: list):
    print(ls)
    sum_elem = 0
    for i in ls:
        sum_elem += i
    average = sum_elem/len(ls)
    return average


print(average_fib(fibonachi(6)))


