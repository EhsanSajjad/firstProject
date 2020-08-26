
from array import *

arr = array('i', [])

n = int(input('Enter the lenth of the array: '))

for i in range(n):
    x = int(input('enter the next value: '))
    arr.append(x)

print(arr)

# get the index number (menually)
element = int(input("Enter any element from the above array to get the index no: "))
count = 0
for e in arr:
    if element == e:
        print('the index number of your given element is:', count)
        break
    count += 1
else:
        print('not found')

# get the index number (with built-in function)
check = element in arr
if check == True:
    print("with built-in function, index number is:", arr.index(element))
else:
    print('with built-in function, not found')




