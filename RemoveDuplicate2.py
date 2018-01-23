
arr = [1,1,1,2,2,3,3,3,3,54,54,777,777,777,100,100,100,100,100]
count = 1
print(arr)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > 2:
        for x in range(count-2):
            del(arr[i])
    count = 1

print(arr)

