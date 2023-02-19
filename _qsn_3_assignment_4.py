# Write a Python program to square the elements of a list using map() function.


size = int(input('Enter your range : '))
list1 =[]
for i in range(size):
    element = int(input('Enter element : '))
    list1.append(element)
print(list1)

def square(list1):
    return list1**2

list_= list(map(square,list1))
print(list_) 