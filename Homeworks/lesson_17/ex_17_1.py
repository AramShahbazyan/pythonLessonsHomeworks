# Կա կամայական էլեմենտներով list։ Խնդիրն այն է, որ այն վերածվի set ի: Եթե որոշ տարրեր հնարավոր
# չէ հեշավորել, ապա մենք բաց ենք թողնում դրանք: List_to_set () ֆունկցիան տպում է տվյալ
# list ը և ստացված set ը:

my_list = [4, 5, 8, ['s', 5, 'turbo'], 'sisak', 'mukuch', (4, 6, 8), 45, 'sdf', {4, 5, 6}]


def list_to_set(ls: list):
    my_set = set()
    for i in ls:
        if type(i) != list and type(i) != tuple and type(i) != set:
            my_set.add(i)

    print(my_set)


list_to_set(my_list)
