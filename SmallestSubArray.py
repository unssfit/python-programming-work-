import random

num = 9
#arr = [1,3,5,6,4,3]
arr = []
for j in range(6):
    arr.append(random.randint(1,9))
print(arr)


for i in range(len(arr)-1):
    if (arr[i] + arr[i+1]) > num:
        print(arr[i],arr[i+1])
        break


