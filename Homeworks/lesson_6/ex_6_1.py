# վարժություն 1
# Մի list ը լրացրեք պատահական թվերով, մյուսը՝ ստեղնաշարից մուտքագրված թվերով,
# երրորդի list ում գրեք առաջին երկուսի համապատասխան բջիջների գումարները։
# Ցուցադրել զանգվածների բովանդակությունը էկրանին:

list_1 = [2, 6, 8, 5]

num_1 = int(input('input numbers 1: '))
num_2 = int(input('input numbers 2: '))
num_3 = int(input('input numbers 3: '))
num_4 = int(input('input numbers 4: '))
list_2 = [num_1, num_2, num_3, num_4]
print(list_1)
print(list_2)
mas = []
for i in range(0, len(list_1)):
    mas.append(list_1[i] + list_2[i])
print(mas)
