
lis = []
while True:
    usr = int(input('enter a number: '))
    if usr == 0: break
    lis.append(usr)

for i in range(0,len(lis)):
    if lis[i] == 42:
        break
    else:
        print(lis[i])