"""
x = int(input("enter first number: "))
y = int(input("enter second number: "))
print("Output is: " + str(x+y))

ch1 = input("enter a char: ")
print(ch1)
print(type(ch1))


#or (both are sasme in the below)
ch2 = input("enter a char: ")
print(ch2[0])
print(type(ch2))

#or
ch3 = input("enter a char: ")[0]
print(ch3)
print(type(ch3))
"""

#now to evaluate an expresion, we can write
result = eval(input('enter an expresion: '))
print(result)