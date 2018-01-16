lis = [2, 22, 45, 'gr', 12, 'you', 54, 'done', 'are']
string = ''
for i in range(len(lis)):
    if type(string) == type(lis[i]):
        lis[i] = []
print(lis)
