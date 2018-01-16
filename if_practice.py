ch = "d"
s = "hello there there you go"
if ch in s:
    print('{} is in String'.format(ch))
elif ch not in s:
    print('Tray again later')
else:
    print('{} is not in String'.format(ch))


s = input('enter your name:')
print('how old are you {0}'.format(s))





age = 12
if not(age < 1):
    print('NOT condition work')



tab = [10,22,33,50,51,78,15]

temp = 3
for i in tab[:temp]:
    print(i)










name = "younes"

if name is 'raj':
    print('raj is the name')
elif name is 'fatima':
    print('fatima is the name')
elif name is 'younes':
    print('youness is the name')
else:
    print("wrong name")