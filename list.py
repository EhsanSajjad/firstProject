nums = [10, 20, 30, 40]
numIndex = nums.index(30)
print(numIndex)

print(nums[2:])
print(nums[0:-2])
print(nums[1:3])
names = ['sajjad ', 'sadik ', 'nasir ']
print(names[1])
print(nums + names)
print(names[2] + str(nums[2]))
print(".................................")
nums.append(111)
print(nums)
nums.insert(0, 5)   # (index, value)
print(nums)
nums.pop(3)
print(nums)
nums.pop()      # last number is deleted
print(nums)
del nums[1:]    # for deleting any/whole
print(nums)
print(".............................")
nums.extend([231, 2, 44, 123])
print(nums)
x = min(nums)
print(x)
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)

l = [311, 143, 3, 34, 2, 234]
print('list is sorted: ', sorted(l))

#checking the elements are there or not in the list, using in operator
check = 311 in l
print(check)
print(32 in l)


