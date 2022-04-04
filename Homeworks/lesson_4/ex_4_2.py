# վարժություն 2
#      Մուտքագրեք ամսաթիվ ստեղնաշարից (օրինակ, 1986 թ.):
# Որոշեք՝ օգտագործողի մուտքագրած տարին նահանջ տարի է, թե ոչ։

year = int(input('please input year` '))
if year % 4 == 0:
    print('The year is a retreat')
else:
    print('The year is not a retreat')
