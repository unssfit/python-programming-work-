import random


num1 = random.randint(1,6)
num2 = random.randint(1,6)
print('num1 = ',num1)
print('num2 = ',num2)
if num1 == num2:
    print((num1+num2)*2)
else:
    print(num1+num2)