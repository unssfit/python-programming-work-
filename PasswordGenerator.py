import random


string = 'abcdefghijklmnopqrstuvwxy0123456789ABCDEFGHIJKLMNOPQRSTUVWXY!@#$%^&*()'
password = ''
for i in range(6):
    index = random.randint(0,len(string))
    password += string[index]
print(password)
