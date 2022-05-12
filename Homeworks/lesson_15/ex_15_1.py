num_1 = int(input('input num 1: '))
actions = str(input('input action: '))
num_2 = int(input('input num 2: '))


def sum(num1: int, num2: int):
    sum_nums = num1 + num2
    return sum_nums


def sbt(num1: int, num2: int):
    sbt_nums = num1 - num2
    return sbt_nums


def mult(num1: int, num2: int):
    mult_nums = num1 * num2
    return mult_nums


def divide(num1: int, num2: int):
    div_nums = num1 / num2
    return div_nums


def result(num1: int, num2: int, act: str):
    res_dict = {
        '+': sum(num1, num2),
        '-': sbt(num1, num2),
        '*': mult(num1, num2),
        '/': divide(num1, num2)
    }
    return res_dict.get(act)


print(result(num_1, num_2, actions))
