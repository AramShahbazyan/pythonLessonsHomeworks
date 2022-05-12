num_1 = int(input('input num 1: '))
actions = str(input('input action: '))
num_2 = int(input('input num 2: '))


def calculator(num1: int, num2: int, action: str):
    calc_dict = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2
    }

    return calc_dict.get(action)


print(calculator(num_1, num_2, actions))