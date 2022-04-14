# Գրեք ծրագիր, որը կավելացնի, հանի, կբազմապատկի կամ կբաժանի երկու թվեր: Գործողության համարները և նշանը
# մուտքագրվում են օգտագործողի կողմից: Հաշվարկն ավարտելուց հետո ծրագիրը չպետք է դադարեցվի, այլ պետք է պահանջի
# նոր տվյալներ հաշվարկների համար։ Ծրագրի ավարտը պետք է իրականացվի՝ որպես գործողության նշան մուտքագրելով «0» նիշը:
# Եթե օգտագործողը մուտքագրում է անվավեր նիշ (ոչ թե «0», «+», «-», «*», «/»), ապա ծրագիրը պետք է տեղեկացնի
# նրան սխալի մասին և նորից հարցնի գործողության բնույթը։ Նաև տեղեկացրեք օգտատիրոջը զրոյի վրա բաժանելու անհնարինության
# մասին, եթե նա որպես բաժանարար մուտքագրել է 0։

while True:
    num_1 = int(input('Please input number 1: '))
    num_2 = int(input('Please input number 2: '))
    if num_2 == 0:
        print('number is not divisible by 0')
        break
    action = input('Please input action: ')
    if action == '+':
        print(num_1 + num_2)
    elif action == '-':
        print(num_1 - num_2)
    elif action == '*':
        print(num_1 * num_2)
    elif action == '/':
        print(num_1 / num_2)
    elif action == '0':
        print('END')
        break
    else:
        print('Your input action is false, please input true action')
        continue
