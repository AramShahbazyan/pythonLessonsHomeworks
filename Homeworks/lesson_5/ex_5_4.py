# Վարժություն 4
# Գտե՛ք մուտքագրված բնական թվի թվանշանների գումարը և արտադրյալը: Օրինակ, եթե մուտքագրված է 325 թիվը,
# ապա նրա թվանշանների գումարը 10 է (3+2+5), իսկ արտադրյալը՝ 30 (3*2*5)։

num = int(input('Please input number: '))
num_sum = 0
num_multiply = 1
num_list = [int(i) for i in str(num)]
for x in num_list:
    num_sum += x
    num_multiply *= x
print(num_sum)
print(num_multiply)