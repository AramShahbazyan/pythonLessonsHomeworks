# Գրել ֆունկցիա,որը  կստանա list: Գտե՛ք ամենամեծ ընդհանուր բաժանարարները list ում առկա ցանկացած երկու թվի համար:
# Ֆունկցիան պետք վերադարձնի list որում կլինեն ստացած list ում առկա բոլոր թվերի զույգ առ զույգ կոմբինացիայի
# ընդհանուր ամենամեծ բաժանարարները։

def my_list(first_list: list):
    mult_list = []
    for i in first_list:
        for j in range(1, i + 1):
            if i % j == 0:
                mult_list.append(j)
    print(mult_list)


my_list([12, 5, 66, 7, 10])
