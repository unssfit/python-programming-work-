
string = 'dfdfbugyuytbugklloobugkk'
count = 0
lis = list(string)
for i in range(len(string)):
    if string[i] == 'b':
        count += 1
    elif string[i] == 'u':
        count += 1
    elif string[i] == 'g':
        count += 1
        if count == 3:
            for x in range((i-3)+1,(i-3)+4):
                lis[x] = ''
    else:
        count = 0
print(''.join(lis))
