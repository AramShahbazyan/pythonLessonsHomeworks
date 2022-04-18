# Գրել ծրագիր որը կգեներացնի list որի երկարությունը կլինի 10 իսկ էլեմենտներ պետք է լինեն  1000 - 9999
# միջակայքում բնական թվեր, բնական թվերից թվանշանների գումարում գտե՛ք ամենամեծը։ Ցուցադրել այս թիվը և նրա
# թվանշանների գումարը:

from random import randint

my_list = [randint(1000, 9999) for i in range(10)]
print(my_list)
max_num = 0
new_list = []
for i in my_list:
    num1 = (i // 1000)
    num2 = (i % 1000 // 100)
    num3 = (i % 100 // 10)
    num4 = (i % 10)
    sum_num = num1 + num2 + num3 + num4
    new_list.append(sum_num)
print(new_list)
print(max(new_list))
index_max_num = new_list.index(max(new_list))
print(my_list[index_max_num])