#break
available_candies = 4
nCandies = int(input('how many candies do you want?\n'))
i = 1
while i<= nCandies:
    if i > available_candies:
        print('stock out!!')
        break

    print('candies')
    i+=1

print('.............................')

#continue
for i in range(1, 51):
    if i%3==0 or i%5==0:
        continue

    print(i, end=' ')

print('................................')

#pass

for i in range(21):
    if i%2!=0:
        pass
    else:
        print(i, end=' ')