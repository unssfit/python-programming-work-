

n = 4
sp = '  '
for i in range(n):
    if i == 3:
        sp = '--'
    print(' '*(n-i)+'/'+sp*i+'\\')
