
def terminatedSum(string):
    sub,sNum,digitSum = ([],[],[])
    for i in range(len(string)):
        if string[i] is not '0':
            sNum.append(string[i])
        else:
            sub.append(sNum)
            sNum = []
    for j in range(len(sub)):
        sm = 0
        for x in range(len(sub[j])):
            if sub[j][x] is not '[]':
                sm += int(sub[j][x])
        digitSum.append(sm)
    index = 0
    for s in range(len(digitSum)-1):
        if digitSum[0] < digitSum[s+1]:
            index = s+1
            temp = digitSum[0]
            digitSum[0] = digitSum[s+1]
            digitSum[s+1] = temp
    return 'Largest sum of degit is:',''.join(sub[index]),'and its Sum is:',digitSum[0]


string = '188045802220454800055440475000'
res = terminatedSum(string)
print(res)














