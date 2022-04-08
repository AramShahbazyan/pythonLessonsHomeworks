# Վարժություն 3
# Հաշվեք և ցուցադրեք մուտքագրված բնական թվի զույգ և կենտ թվանշանների քանակը:
# Օրինակ, եթե մուտքագրված է 34560 թիվը, ապա այն ունի 3 զույգ թվանշան (4, 6 և 0) և 2 կենտ թվանշան (3 և 5):

num = int(input('Please input number: '))
num_list = [int(i) for i in str(num)]
pair_count = 0
odd_count = 0
for x in num_list:
    if x % 2 == 0:
        pair_count += 1
    elif x % 2 > 0:
        odd_count += 1
print('Count pair numbers is: ', pair_count)
print('Count odd numbers is: ', odd_count)