# վարժություն 3
# Ստեղծեք 20 պատահական ամբողջ թվեր, որոնք տատանվում են -5-ից մինչև 4-ը, դրանք գրեք list ի բջիջներում:
# Հաշվե՛ք, թե դրանցից քանիսն են դրական, բացասական և զրոյական արժեքներ:Ցուցադրեք զանգվածի տարրեր և հաշվված արժեքները:
from random import randint

# lists = []
# for i in range(20):
#     lists.append(randint(-5, 4))
# Նույննա ինչ ստորև գրածը

lists = [randint(-5, 4) for i in range(20)]
count_neg = 0
count_pos = 0
count_zero = 0
for i in lists:
    if i == 0:
        count_zero += 1
    elif i < 0:
        count_neg += 1
    else:
        count_pos += 1
print(f'Positive numbers count is` {count_pos}')
print(f'Negative numbers count is` {count_neg}')
print(f'zeros count is`  {count_zero}')
