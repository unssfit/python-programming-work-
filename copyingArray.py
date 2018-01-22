import random

ar1 = []
for i in range(0,10):
    ar1.append(random.randint(1,100))

ar2 = []
for j in range(0,len(ar1)):
    ar2.append(ar1[j])

ar1[-1] = 7
print(ar1)
print(ar2)