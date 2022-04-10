# վարժություն 2
# Լրացրեք իրական թվերի list ը ստեղնաշարի մուտքագրմամբ: Հաշվե՛ք զանգվածի տարրերի գումարը և արտադրյալը:
# Ցուցադրել ինքնին զանգվածը, ստացված գումարը և դրա տարրերի արտադրյալը:

num_1 = int(input('input number 1: '))
num_2 = int(input('input number 2: '))
num_3 = int(input('input number 3: '))
num_4 = int(input('input number 4: '))
num_5 = int(input('input number 5: '))
num_6 = int(input('input number 6: '))
lists = [num_1, num_2, num_3, num_4, num_5, num_6]
print(lists)
sum_lists = 0
mult_lists = 1
for i in lists:
    sum_lists += i
    mult_lists *= i
print(sum_lists)
print(mult_lists)
