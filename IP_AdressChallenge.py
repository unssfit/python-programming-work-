
ip = "127.0.0.1"   #input(enter ip adress:)
c = 0
cou = 0
seg = 1
temp = 0
s = ""
for i in range(0,len(ip)):
    if ip[i] == '.':
       seg += 1
       s += str(cou)
       temp = seg
       cou = 0
    else:
        c += 1
        cou += 1
        if (seg == temp) and (c == (len(ip)-(seg-1))):
            s += str(cou)


print('i = ',i)
for i in range(0,len(s)):
    print("segment number ",i," = ",s[i])

print('ip have segment = ',seg)
