import random
arr = []
for s in range(15):
    arr.append(random.randint(1,20))
print(arr)

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[j] % 2 == 1 and arr[i] % 2 == 1) and (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)












