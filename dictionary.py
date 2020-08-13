# {} is used for dictionary
# it must have a key and a value
# the key may be any thing, but inmutable(uniq)

marks = {1: 45, 2: 100, 3: 98}
data = {1: 'sajjad', 2: 'nasir', 4: 'maruf'}
print(data, marks)

# we may print by calling the key
print(data[4])
# print(data[3])  # as 3 n key te kichu nai tai evabe likhle error dicche
print(data.get(3)) # but evabe likhle error nai.. eta lekha better

print(data.get(3, 'not found')) # evabe key likhe express korano jay