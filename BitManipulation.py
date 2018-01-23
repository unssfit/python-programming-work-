

string = '00100111010011100001'

lis = list(string)
for i in range(len(lis)):
    if lis[i] is '0':
        lis[i] = ''
print(''.join(lis))

