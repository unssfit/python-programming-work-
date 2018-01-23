import random
arr = []
for i in range(200):
    arr.append(random.randint(10,1000))

count = 1
numInfo = []
for j in range(len(arr)):
    for x in range(j+1,len(arr)):
        if arr[j] == arr[x]:
            repeted = [None] * 2
            count += 1
            repeted[0] = count
            repeted[1] = arr[j]
            numInfo.append(repeted)
    count = 1
print(numInfo)
