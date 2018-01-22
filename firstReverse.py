



string = 'coderbyte'
revers = []

li = list(string)
for i in range(len(li)-1,0,-1):
    revers.append(li[i])

revers.append(string[0])
for j in range(0,len(revers)):
    print(revers[j],end='')
