

string = 'hello world sfgf im youness'
ch = ''
for i in range(len(string)-1,0-1,-1):
    if string[i] is not ' ':
        ch += string[i]
    else:
        break
print(len(ch))

