
quit = 0
while quit != 3:
    print('1)Find two digit numbers <= 56 with sums of digits > 10')
    print('2)Find two digit number minus number reversed which equals sum of digits')
    print('3)Quit')

    quit = int(input('>'))
    if quit == 1:
        for i in range(10,56):
            toStr = str(i)
            n1 = int(toStr[0])
            n2 = int(toStr[1])
            if (n1+n2) > 10:
                print('i = ',i,n1+n2)
    elif quit == 2:
        for j in range(10,56):
            toStr = str(j)
            reverseNum = toStr[1]+toStr[0]
            n1 = int(toStr[1])
            n2 = int(toStr[0])
            nSum = n1 + n2
            if (j - int(reverseNum)) == nSum:
                print('j = ',j)