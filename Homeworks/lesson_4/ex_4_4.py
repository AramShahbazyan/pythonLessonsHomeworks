# վարժություն 4
#      Ստեղնաշարից մուտքագրեք երկու ոչ զրոյական ամբողջ թիվ: Ստուգեք, արդյոք առաջինը բաժանվում է երկրորդին:
# Ցուցադրեք դրա մասին հաղորդագրություն, ցուցադրեք մնացորդը բաժանումից հետո (եթե այդպիսիք կան)
# և ամբողջ թիվը բաժանումից հետո (ամեն դեպքում):
num_1 = int(input('please input number 1: '))
num_2 = int(input('please input number 2: '))
if num_2 % num_1 == 0:
    print('Number 1 is divisible by number 2')
else:
    print('the balance after division: '), print(num_2 % num_1)
    print('the whole part after the division: '), print(num_2 // num_1)
