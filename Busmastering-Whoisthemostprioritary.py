

aces = '0011001'
bus = 7

s = ''
check = False
for i in range(len(aces)):
    if aces[i] == '1':
        s += '1'
        check = True
        for j in range(i+1,len(aces)):
            s += '0'
    else:
        s += '0'
    if check:break

print(s)
