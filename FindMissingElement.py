# https://www.codewars.com/kata/find-the-missing-element-between-two-arrays
# links of the problem

arr = [[1, 5, 5,5, 3], [1, 5, 3]]
#arr = [[6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]]
duplicate = []
for i in range(len(arr[0])):
    count = arr[0].count(arr[0][i])
    if arr[0][i] in arr[1]:
        if count == arr[1].count(arr[0][i]):
            pass
        else:
            if arr[1].count(arr[0][i]) < count and arr[0][i] not in duplicate:
                print('Number',arr[0][i],'Missing',count - arr[1].count(arr[0][i]),'times')
            duplicate.append(arr[0][i])
    else:
        print('missing number:',arr[0][i])

