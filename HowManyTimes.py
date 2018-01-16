import random

arr = []

for i in range(0,10):
    arr.append(random.randint(1,50))


print(arr)
val = int(input('Value to find:'))
count = 0
for j in range(0,len(arr)):
    if val == arr[j]:
        count += 1
print(val,'was found',count,'Times.')