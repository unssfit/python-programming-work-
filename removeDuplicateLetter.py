
string = 'cbacdcbc'
nw_str = list(string)
for i in range(len(nw_str)):
    for j in range(i+1,len(nw_str)):
        if nw_str[i] == nw_str[j]:
            nw_str[i] = ''

print(''.join(nw_str))

