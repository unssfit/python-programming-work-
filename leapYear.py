year = int(input())
leap = False


if (year / 4).is_integer():
    leap = True
    if(year / 100).is_integer():
         leap = False
if (year / 100).is_integer():
    leap = False
    if (year / 400).is_integer():
        leap = True
print(leap)


n = int(input())
print(*range(1,n+1),sep='')
