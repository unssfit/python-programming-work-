
string = 'fun time'
ch = list(string)
print(string)
for i in range(0,len(ch)):
    ch[i] = chr(ord(ch[i])+1)

print(''.join(ch))

