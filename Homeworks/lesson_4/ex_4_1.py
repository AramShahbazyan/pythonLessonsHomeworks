# վարժություն 1
# Մուտքագրված են կետի կոորդինատները (x;y) և շրջանագծի (r) շառավիղը։ Որոշեք, թե արդյոք տվյալ
# կետը պատկանում է շրջանագծին, եթե դրա շրջանագծի կենտրոնը կոորդինատային համակարգի կենտրոնն է:

r = int(input('input radius r: '))
x = int(input('input coordinate x: '))
y = int(input('input coordinate y: '))
cords_xy = x ** 2 + y ** 2
print(cords_xy)
print(r ** 2)
if cords_xy <= r ** 2:
    print('x;y coordinate is belongs to the circle')
else:
    print('x;y coordinate is belongs to the circle')
# else:
# print('xy coordinate is belongs to the circle')
