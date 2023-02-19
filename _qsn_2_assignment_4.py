# Write a Python program to triple all numbers of a given list of integers. Use Python map.


size = int(input('Enter your range : '))
list1 =[]
for i in range(size):
    element = int(input('Enter element : '))
    list1.append(element)
print(list1)

def square(list1):
    return list1*3

list_= list(map(square,list1))
print(list_)  