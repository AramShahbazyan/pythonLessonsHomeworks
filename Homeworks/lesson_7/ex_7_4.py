# Գեներացրեք է 2-ից մեծ տասը բնական թիվ։ Հաշվիր, թե քանի պարզ թիվ կա դրանց մեջ:

from random import randint

my_list = [randint(2, 20) for i in range(10)]
print(my_list)
count_simple_nums = 0
for i in my_list:
    x = 2
    count_divisors = 0
    while x <= i:
        if i % x == 0:
            count_divisors += 1
        x += 1
    if count_divisors == 1:
        count_simple_nums += 1
print(count_simple_nums)
