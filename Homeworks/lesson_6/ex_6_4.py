# վարժություն 4
# Մուտքագրված թվի հակադարձը կազմի՛ր դրանում ներառված թվերի հերթականությամբ և ցուցադրի՛ր այն։
# Օրինակ, եթե դուք մուտքագրել եք 3486 համարը, ապա պետք է դուրս բերեք 6843 թիվը:
# Արգելվում է օգտագործել string reverse մեթոդը


num = int(input('please input number: '))
lists = []
new_list = []
for i in str(num):
    lists.append(i)
for j in range(-1, -len(lists) - 1, -1):
    new_list.append(lists[j])
for k in new_list:
    print(f'{int(k)}', end='')
