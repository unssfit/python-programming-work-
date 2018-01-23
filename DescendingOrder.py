
num = 21445
nStr = str(num)
nm = list(nStr)
temp = 0
for i in range(len(nm)):
    for j in range(i+1,len(nm)):
        if int(nm[i]) < int(nm[j]):
            temp = nm[i]
            nm[i] = nm[j]
            nm[j] = temp
print(int(''.join(nm)))

