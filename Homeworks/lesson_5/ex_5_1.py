# Վարժություն 1
# Օգտագործողի կողմից մուտքագրված թիվը փոխարկեք բայթերի կամ կիլոբայթների՝ կախված օգտագործողի ընտրությունից:
# ծրագիրը պետք է վերցնի արժեք և չափի (b կամ kb) և պետք է պատասխան տա միաժամանակ երկու չափման արժեքների համար:

num = int(input('Please input number: '))
b_or_kb = input('Please enter "b" or "kb": ')
if b_or_kb == 'b':
    b_to_kb = num / 1000
    print(num, 'byte = ', b_to_kb)
elif b_or_kb == 'kb':
    kb_to_b = num * 1000
    print(num, 'kilobyte = ', kb_to_b)
else:
    print('Please input true value` "b" or "kb"')
