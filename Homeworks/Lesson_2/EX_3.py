# ex 3
#
# Write a program that will get a string in which there are
# (for example 'asgerr5dhhf56fddd789fddfff5555hl') Will count the sum of all the counts of the digits.

str1 = 'ahsgd4f5g4h8h4'

print(str1.isdigit())
count_1 = str1.count('1') * 1
count_2 = str1.count('2') * 2
count_3 = str1.count('3') * 3
count_4 = str1.count('4') * 4
count_5 = str1.count('5') * 5
count_6 = str1.count('6') * 6
count_7 = str1.count('7') * 7
count_8 = str1.count('8') * 8
count_9 = str1.count('9') * 9

result = count_9+count_8+count_7+count_6+count_5+count_4+count_3+count_2+count_1
print(result)