
lis = range(1,20)
print(max(lis))
print(min(lis))

test = [1,2,3,3,4]
test[2:2] = [12,25,10]
print(test)
del(test[1])
print(test)

cp = test.copy()
test.clear()
print(cp)
print(test)

print(cp.count(3))

user = str(input('Enter Username:'))
Pin = str(input('Enter Password:'))
userInfo = [None]*2
userInfo[0] = user
userInfo[1] = Pin
data = [['youness','loveallah'],['khalid','123456'],['jack','hello2001'],['tom','21/14/1954']]

if userInfo in data:
    print('Access Granted.')
else:
    print('Invalid UserName/Password')

