#arr = [1,-1,2,-2,3]
arr = [-3,1,2,3,-1,-4,-2]
#arr = [1,-1,2,-2,3,3]
for i in range(len(arr)):
    if str(arr[i])[0] != '-':
        exist = True
        for j in range(len(arr)):
            if str(arr[j])[0] == '-' and int(str(arr[j])[1]) == arr[i]:
                exist = False
        if exist:
            print(arr[i],'has only positive ocurrence.')

    if str(arr[i])[0] == '-':
        exis = True
        for x in range(len(arr)):
            if int(str(arr[i])[1]) == arr[x]:
                exis = False
        if exis:
            print(arr[i],'Has only Negative ocurrence.')

