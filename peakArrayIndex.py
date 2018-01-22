#arr = [1,2,3,5,3,2,1]
#arr = [1,12,3,3,6,3,1]
arr = [10,20,30,40]
exist = False
for i in range(len(arr)):
    sm, sm2 = 0,0
    for j in range(i):
        sm += arr[j]
    for x in range(i+1,len(arr)):
        sm2 += arr[x]
    if sm == sm2:
        print(i,'is the index we need.')
        exist = True

if not exist:
    print('-1 Not Found!')
