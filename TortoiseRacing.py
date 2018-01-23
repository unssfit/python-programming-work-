print(850/60)
print(70/14)

def repeatString(string,n):
    return string*n
print(repeatString('Hello',7))



string = '155874243'

conStr = list(string)
for i in range(len(conStr)):
    if int(conStr[i]) < 5:
        conStr[i] = '0'
    else:
        conStr[i] = '1'
print(''.join(conStr))
