
string = 'hopeless'
cutStr = len(string)//2

s1 = string[:cutStr]
s2 = string[cutStr:]
print(s1)
# halfStr = [None]*2
#
# halfStr.append(s1)
# halfStr.append(s2)


count = 0
while True:
    chLen = len(s1)//2
    print(s1[:chLen])
    s1 = s1[:chLen]
    if len(s1) < 2:
        s1 = s2
        count += 1
    if count == 2:break















