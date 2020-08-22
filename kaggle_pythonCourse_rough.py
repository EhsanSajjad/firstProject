# to make round number
x =  3.12343
print(round(x, 2))

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3


y = to_smash(91)
print(y)
x = to_smash(1)
print(x)
y += 4j
print(y.imag)
x = 22
print(bin(x))
print('bit lenth of x: ', x.bit_length())
x = 0.125
print(x.as_integer_ratio())

"""
print(round(-2.01))
bool_check = '3'==3
print(bool_check)



def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
"""
