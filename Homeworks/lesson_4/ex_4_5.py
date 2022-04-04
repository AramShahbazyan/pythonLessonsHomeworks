# վարժություն 5
#      Մուտքագրեք երեք տարբեր թվեր ստեղնաշարից: Գտեք միջինը (մեկից մեծ, բայց մյուսից փոքր):
num_1 = int(input('input number 1: '))
num_2 = int(input('input number 2: '))
num_3 = int(input('input number 3: '))
if num_1 > num_2:
    if num_1 < num_3:
        print(num_1)
    elif num_2 > num_3:
        print(num_2)
    else:
        print(num_3)
elif num_1 > num_3:
    print(num_1)
elif num_2 > num_3:
    print(num_3)
else:
    print(num_2)

