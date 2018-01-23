# https://www.codewars.com/kata/sort-array-by-string-length
# link of the problem
arr = ["Telescopes", "Glasses", "Eyes", "Monocles"]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if len(arr[i]) > len(arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)

