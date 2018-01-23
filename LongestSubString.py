sub,subs,string = ('',[],'pwwkedsfgjkjjhzzazrerfvw')
for i in range(len(string)):
    sub = string[i]
    for j in range(i+1,len(string)):
        if string[i] != string[j] and string[j] not in sub:
            sub += string[j]
        else:
            subs.append(sub)
            sub = ''
            break
#print(subs)
for x in range(1,len(subs)):
    if len(subs[0]) < len(subs[x]):
        temp = subs[0]
        subs[0] = subs[x]
        subs[x] = temp
#print(subs)
print('The answer is:','"'+subs[0]+'"','with the length is:',len(subs[0]))


