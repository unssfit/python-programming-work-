import random


arr = []
for  i in range(15):
    arr.append(random.randint(4,23))
print(arr)

#get the lowest number
temp = 0
for j in range(len(arr)):
    if arr[0] > arr[j]:
        temp = arr[0]
        arr[0] = arr[j]
        arr[j] = temp
print('lower number = ',arr[0])

#get the highst number
for x in range(len(arr)):
    if arr[0] < arr[x]:
        temp = arr[0]
        arr[0] = arr[x]
        arr[x] = temp
print('high number = ',arr[0])