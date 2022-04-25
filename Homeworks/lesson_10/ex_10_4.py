# Տրվում է բնական թվերից բաղկացած միաչափ list: Տրված list դասավորի՛ր թվերի թվանշանների գումարի աճման կարգով։
# Օրինակ՝ տրված է թվերի զանգված [14, 30, 103]: Տեսակավորելուց հետո կլինի այսպես՝ [30, 103, 14],
# քանի որ 30 թվի թվանշանների գումարը 3 է, 103 թիվը՝ 4, 14 թիվը՝ 5։
#
# Ցուցադրել սկզբնական list ը, տեսակավորված list ը և list որտեղ կլինեն սորտավորված list ի թվանծանների գումարը ըստ հերթականության։

my_list = [152, 132, 102, 99, 121]
print(my_list)
new_list = []
for i in my_list:
    sum_elem = 0
    for j in str(i):
        sum_elem += int(j)
    new_list.append(sum_elem)
print(new_list)
for i in range(len(new_list)):
    for j in range(len(new_list)):
        if new_list[i] < new_list[j]:
            new_list[i], new_list[j] = new_list[j], new_list[i]
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
print(new_list)