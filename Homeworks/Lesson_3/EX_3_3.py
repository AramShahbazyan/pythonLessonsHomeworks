digit_num = int(input('Please input digit number: '))
num_1 = digit_num // 10000
num_2 = digit_num % 10000 // 1000
num_3 = digit_num % 1000 // 100
num_4 = digit_num % 100 // 10
num_5 = digit_num % 10
lists_5_num = [num_1, num_2, num_3, num_4, num_5]
lists_5_num.sort()
print(lists_5_num)
