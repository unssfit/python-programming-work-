import random

# dec symbol (33-47)
key = ''
for j in range(6):
    key += chr(random.randint(97, 121)) + str(j) + chr(random.randint(33, 47))
print(key)

usr = str(input('Activate The Sftware:'))
if usr == key:
    print('Valid Key. Your Product Expire From 1 Year.')
else:
    print('Invalid Key.')
