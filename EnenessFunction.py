
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def isDivisibleBy3(n):
    if n % 3 == 0:
        return True
    else:
        return False

for i in range(1,20+1):
    if isDivisibleBy3(i) and isEven(i):
        print(i,'<=')
    else:
        if isEven(i) and isDivisibleBy3(i) == False:
            print(i,'<')

        if isDivisibleBy3(i) and isEven(i) == False:
            print(i,'=')
