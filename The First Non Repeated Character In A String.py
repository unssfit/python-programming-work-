

string = 'test'

ch = []
c = False
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if string[i] == string[j]:
            c = True
    if c == False:
        ch.append(string[i])
    else:
        c = False

print(ch)

