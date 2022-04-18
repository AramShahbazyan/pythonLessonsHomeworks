# Մուտքագրեք նմական թվերի միջակայք՝ սկիզբ և վերջ, ինչպես նաև քանակ, Բնական թվերի մուտքագրված միջակայքում
# գտե՛ք նրանց, որոնց բաժանարարների թիվը մուտքագրված քանակից պակաս չէ։ Գտնված թվերի համար ցուցադրեք
# բաժանարարների և բոլոր բաժանարարների թիվը:

start_num = int(input('Please input start number: '))
end_num = int(input('Please input start end number: '))
count_num = int(input('Please input start numbers count: '))
for i in range(start_num, end_num + 1):
    j = 1
    count_divider = 0
    while j <= i:
        if i % j == 0:
            count_divider += 1
        j += 1
    if count_divider >= count_num:
        print(f'our number is, {j-1}')
        print(f'{j-1}, have a, {count_divider}, divider')
