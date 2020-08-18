
import math
x = math.sqrt(25)
print(x)

# floor will give you the first value
# ceil will give you the last value
print(math.floor(2.6))  # 2 will be the output
print(math.ceil(2.6))   # 3 will be the output

#for power
print(math.pow(2,3))  # 2 to the power 3 , that means ans will be 8

# constant
print(math.pi)
print(math.e)
print("...................")

#what is alais??
# An alias is a a second name for a piece of data.
# here we can import math as m (or whatever) to short the name
import math as m
print(m.pi)
print(int(m.sqrt(25)))
print(math.e)  # even we can use math as well
print("...........................")

# for specific function, we may write-
from math import sqrt, pow
print(pow(4, 3))  #even no need to write math in this case
print(math.sqrt(49))  # and you can use math too
#help(math)

