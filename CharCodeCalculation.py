ch = 'ABC'
string = ''
total1 = ''
total2 = ''
for i in range(len(ch)):
    char = str(ord(ch[i]))
    if '7' in char:
        char = list(char)
        char[char.index('7')] = '1'
    string += ''.join(char)



print(string)










