# Վարժություն 2
# Մուտքագրեք երկու երկնիշ բնական թվեր ստեղնաշարից: Ծրագիրը պետք է որոշի տվյալ բնական
# թվի մաս կազմող ամենափոքր և ամենամեծ թվանշանները:

num_1 = int(input('Please input number 1: '))
num_2 = int(input('Please input number 2: '))
nums_1_1 = num_1 // 10
nums_1_2 = num_1 % 10
nums_2_1 = num_2 // 10
nums_2_2 = num_2 % 10
lists = [nums_1_1, nums_1_2, nums_2_1, nums_2_2]
lists.sort()
print('Minimum number is:', lists[0])
print('Maximum number is:', lists[-1])
