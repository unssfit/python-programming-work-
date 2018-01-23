import random
string = 'this is a test!'
space, second_char, res, new_str = ([],[],[],[])

#get spaces index in string
for i in range(len(string)):
    if string[i] == ' ':
        space.append(i)
s = len(string)-space[-1]
space.append(space[-1]+s)

#get evry second char index in string
for v in range(len(space)-1):
    if v == 0:
        for s in range(0,space[0]+1,2):
            if s is not 0:
                second_char.append(s-1)
        for h in range(space[0],space[1],2):
            if string[h] is not ' ':
                second_char.append(h)
    else:
        for r in range(space[v],space[v+1],2):
            if string[r] != ' ':
                second_char.append(r)

#Concatanation
ranCh = 0
for h in range(len(string)):
    if h == 0:
        ranCh = random.randint(0,len(string)-1)
        new_str.append(ranCh)
    else:
        ranCh = random.randint(0, len(string)-1)
        if ranCh in new_str:
            while ranCh in new_str:
                ranCh = random.randint(0, len(string)-1)
            new_str.append(ranCh)
        else:
            new_str.append(ranCh)

#print final result
for k in range(len(string)):
    res.append(string[new_str[k]])
print(string)
print(''.join(res))
