# Մուտքագրել բնական թիվ, Ցուցադրել էկրանին, թե ինչ պարզ բաժանարարներից է բաղկացած մուտքագրված բնական թիվը:

nat_num = int(input('Please input number: '))
i = 1
while i <= nat_num:
    if nat_num % i == 0:
        j = 2
        sum_mult = 0
        while j <= i:
            if i % j == 0:
                sum_mult += 1
            j += 1
        if sum_mult == 1:
            print(i)
    i += 1
