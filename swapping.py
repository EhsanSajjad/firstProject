#one way
a = 5
b = 10
temp = a
a = b
b = temp
print(a, b)

#second way
a = 5
b = 6
a = a+b
b = a-b
a = a-b
print(a, b)

#third way using XOR symbol
#Ii is similar to the second way, but saves xtra bit.
a = 2
b = 3
a = a^b
b = a^b
a = a^b
print(a, b)

#forth way(recomanded)
a = 4
b = 5
a,b = b,a
print(a,b)