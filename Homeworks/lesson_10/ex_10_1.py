# Գրեք ֆունկցիա, որը լրացնում է list պատահական թվերով օգտատիրոջ կողմից նշված տիրույթում:
# Ֆունկցիան պետք է վերցնի երկու արգումենտ՝ միջակայքի սկիզբը և դրա ավարտը, մինչդեռ ոչինչ չվերադարձնի:
# List ի տարրերի արժեքների ելքը պետք է տեղի ունենա ֆունկցիայի հիմնական մասում:

from random import randint

start_num = int(input('Please input start number: '))
end_num = int(input('Please input end number: '))


def my_list(start: int, end: int):
    new_list = [randint(start_num, end_num) for i in range(10)]
    print(new_list)


my_list(start_num, end_num)
