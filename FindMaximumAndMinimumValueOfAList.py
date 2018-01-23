import random


arr1 = []
arr2 = []

for i in range(10):
    arr1.append(random.randint(1,65))
    arr2.append(random.randint(1,222))
print(arr1)
print(arr2)

#ar = [4,6,2,1,9,63,-134,566]
def get_Max(arr):
    for j in range(len(arr)-1):
        if arr[0] < arr[j+1]:
            temp = arr[0]
            arr[0] = arr[j+1]
            arr[j+1] = temp
    return arr[0]

res = get_Max(arr1)
print(res)


def get_min(arr):
    for i in range(len(arr)-1):
        if arr[0] > arr[i+1]:
            temp = arr[0]
            arr[0] = arr[i+1]
            arr[i+1] = temp
    return arr[0]

min = get_min(arr2)
print(min)

