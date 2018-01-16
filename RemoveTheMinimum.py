import random

arr, arr2 = ([],[])
for s in range(20):
    arr.append(random.randint(4,50))
    arr2.append(arr[s])
print('arr = ',arr,'\n','arr2 = ',arr2)
temp,index = (0,0)
for i in range(1,len(arr)):
    if arr[0] > arr[i]:
        index = i
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

arr2.pop(index)
print('arr2 = ',arr2)
