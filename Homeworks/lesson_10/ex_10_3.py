# Գրե՛ք ֆունկցիա, որը որոշում է մուտքագրված ամբողջ թվի թվանշանների քանակը։

def num_elem(num: int):
    count_num_elem = 0
    for i in range(len(str(num))):
        count_num_elem += 1
    print(f'Count of input number elements = {count_num_elem}')


num_elem(5485655)
