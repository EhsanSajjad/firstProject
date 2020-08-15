# {} is used for dictionary to store both key and values
# the key may be any thing, but inmutable(uniq)

marks = {'a': 45, 'b': 100, 'c': 98}
data = {1: 'sajjad', 2: 'nasir', 4: 'maruf'}
print(data, marks)

# we may print by calling the key
print(data[4])
# print(data[3])  # as 3 n key te kichu nai tai evabe likhle error dicche
print(data.get(3)) # but evabe likhle error nai.. eta lekha better

print(data.get(3, 'not found')) # evabe key likhe express korano jay

print("....................................")

keys = ['sajjad', 'nasir', 'sadik']
values = ['loves flutter', 'loves python', 'loves c']
finalData = dict(zip(keys, values))
print(finalData)
"""
# ekhane [] brackets use korsi cz list nisi... list e [] use korte hoy.. 
jodi {} use kortm taile eta set hoye jeto.. set e {} use korte hoy..
set e sequence thik thake na element gular.. tai set nile serial thik thakto na.. sejonne list nisi..
"""


print(finalData['sajjad'])
print(finalData.get('sajjad'))

# lets add values
finalData['maruf'] = 'loves js'
print(finalData)

#lets delete data
del finalData['sajjad']
print(finalData)

print("................................")

# lets add 'list' as a value of dictionary itself
# and 'dictionay' as a value of dictionary itself
prog = {'JS':'Atom', 'C#':'VS', 'Python':['PyCharm', 'Sublime'],
        'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'} }

print(prog)
print(prog['JS'])
print(prog.get('C#'))
print(prog['C#'])
print(prog['Python'][0])
print(prog['Java'])
print(prog['Java']['JEE'])

