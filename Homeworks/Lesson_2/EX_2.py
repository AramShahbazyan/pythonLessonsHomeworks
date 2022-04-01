# Writing a program that gets a string will count the number of characters ‘a’ և ‘b’ in the line and return True if the number of ‘a’ is large - ‘b’'s False և False otherwise.
# For example:
# My_string = ‘abcbaa’
#
# Exit:
# count_a = 3:
# count_b = 2:
# True:
x = 'abbadrabbaaa'
count_a = x.count('a')
count_b = x.count('b')
print(count_a > count_b)