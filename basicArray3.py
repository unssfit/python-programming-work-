import random

arr = []

for i in range(0,1000):
    arr.append(random.randint(10,99))
count = 0
for j in range(0,len(arr)):
    print(arr[j],end=' ')
    count += 1
    if count == 20:
        count = 0
        print()

