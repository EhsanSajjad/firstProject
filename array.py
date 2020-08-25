
from array import *
vals = array('i', [2, 4, 78, 9])  # i is the datatype for int
print(vals)
#buffer_info is a function, which gives the size of an array
print(vals.buffer_info())
#typecode give the type of the array (ex. i for int)
print(vals.typecode)

print(vals[1])
print('..................')


#various way to print arrays with for
for i in range(len(vals)):
    print(vals[i])

print('another way')

for i in vals:
    print(i)

print('..................')


vals.reverse()
print(vals)

#for char
vals2 = array('u', ['q', 'a', 'b', 'r'])  # u is for unicode

for i in vals2:
    print(i, end=' ')
print()


#printing new arrray
newArr = array(vals.typecode, (a for a in vals))
print(newArr)  # its the same array as the vals

#with while loop
i = 0
while i<len(vals):
    print(vals[i], end=' ')
    i +=1
print()