
data = range(35)
print([data[x:x+10] for x in range(0, len(data), 10)])

ar = ['a','b','c','d','e','f','j','i']
chunk = ar[ar.index('d'):ar.index('f')+1]
print(chunk)

string = 'hello world there'
lis = string.split()
for i in range(len(lis)-1,0-1,-1):
    print(lis[i],end=' ')

