#arr = [20,10,-80,10,10,15,35]
arr = [1,2,3,4,3,2,1]
#arr = [1,100,50,-51,1,1]
for i in range(len(arr)):
    sum = 0
    for j in range(0,i):
        sum += arr[j]
    sum2 = 0
    for x in range(i+1,len(arr)):
        sum2 += arr[x]

    if sum == sum2:
        print('index where equality is:  ',i)
        break
