# Ստուգեք փակագծերը: Դուք ունեք 3 տեսակի փակագծեր ՛() [] {}՛,
# օրինակ: ՛({{}} {] []}})՛! Ստուգեք, որ յուրաքանչյուր բաց փակագիծ ունի փակ փակագիծ:
# Այսինքն ձեր ծրագիրը պետք է վերադարձնի True կամ False, Օրինակ՝ եթե մոտքագրել եք '{}()[]'
# կամ '({[]}){}()' ծրագիրը կվերադարձնի True, իսկ եթե մուտքագրել եք '([){]}'
# կամ ((()){}[] ծրագիրը կվերադարձնի False:

brackets = ')())(('
lists = []
for i in brackets:
    lists.append(i)
print(lists)
for j in lists:
    for x in lists:
        if j == x:
            print()



# for i in brackets:
#     if i == '(':
#         for j in brackets:
#             if j == ')':
#                 for x in brackets:
#                     if x == '{':
#
#                         for y in brackets:
#                             if y == '}':
#                                 for z in brackets:
#                                     if z == '[':
#                                         for w in brackets:
#                                             if w == ']':
#                                                 print('true')
