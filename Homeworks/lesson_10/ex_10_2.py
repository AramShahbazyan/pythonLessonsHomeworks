# Գրել ֆունկցիա,որը  կստանա list: Գտե՛ք ամենամեծ ընդհանուր բաժանարարները list ում առկա ցանկացած երկու թվի համար:
# Ֆունկցիան պետք վերադարձնի list որում կլինեն ստացած list ում առկա բոլոր թվերի զույգ առ զույգ կոմբինացիայի
# ընդհանուր ամենամեծ բաժանարարները։

def check_mult_max(num: int):
    div_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            div_list.append(i)
    return div_list


def two_nums(num1, num2):
    max = 1
    l1 = check_mult_max(num1)
    l2 = check_mult_max(num2)
    for i in l1:
        if i in l2:
            if i > max:
                max = i
    return max


def create_max_mult_list(ls: list):
    result = []
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            element = two_nums(ls[i], ls[j])
            result.append(element)
    return result


print(create_max_mult_list([1562, 55, 45, 2222, 100, 150, 666, 98, 10]))
