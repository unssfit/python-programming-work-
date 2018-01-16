
count = 0
c = 0
str = ''
for i in range(ord('a'),ord('z')):
    c += 1
    str += chr(i)
    count += 1
    print(chr(i),end='')
    if count == 3:
        print()
        count = 0
print(str.upper())