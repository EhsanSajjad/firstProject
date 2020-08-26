
from numpy import *
arr = array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype)
# even we can set the datatype like this
arr = array([12, 4], float)
print(arr)
print(arr.dtype)

# linspace()
# the gap between two elements is fix
arr = linspace(0, 5, 6)
# 0 is the starting point. 5 is the ending point
# 6 is the path division. mane 6 ta vag kora hobe 0 theke 5 k
print(arr)
# if number of path is not defined, 15 paths will be created by default
# for ex.
arr = linspace(0, 5)
print(arr)
print(".............................")


#arange()
#its like the range in array
#1 is starting point, 10 is ending point, 2 is the step
arr = arange(1, 10, 2)
print(arr)

#logspace()
arr = logspace(1, 40, 5)
print(arr)
# starts from log 10 base to 1
# ends with log 10 base to 40
# 5 is the dividing path




