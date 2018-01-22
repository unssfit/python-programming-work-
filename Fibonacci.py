n = 10
c = 0
for i in range(1,n):
    if i == 1:
        a = i
        print(a,'',end='')
        b = i+1
        print(b,'',end='')
    else:
        c = a + b
        print(c,'',end='')
        a = b
        b = c



