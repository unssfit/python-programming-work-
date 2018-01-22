import random

arr = []

for i in range(0,10):
    arr.append(random.randint(1,50))

print(arr)
val = int(input('Value to find:'))

for j in range(0,len(arr)):
    if val == arr[j]:
        print(val,'is in slot',j)
