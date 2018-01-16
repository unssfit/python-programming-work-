

s1 = 'hzllds'
s2 = 'dfgfhgf'
res = ''
for i in range(len(s1)):
    if s1[i] not in s2:
        res += s1[i]
res2 = ''
for j in range(len(s2)):
    if s2[j] not in s1:
        res2 += s2[j]

print(res+res2)
