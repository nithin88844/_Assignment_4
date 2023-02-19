# Write a Python program to create a lambda function that adds 25 to
#  a given number passed in as an argument.


my_func = lambda x : x + 25
final_out = my_func(int(input('enter the no. : ')))
print(f"final value is {final_out}")