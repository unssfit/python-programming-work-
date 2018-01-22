import random


info = []
for i in range(7):
    person = []
    person.append(random.randint(-2,30))
    person.append(random.randint(18,80))
    info.append(person)
print(info)

for j in range(len(info)):
    if info[j][0] > 7 and info[j][1] >= 55:
        info[j] = 'Senior'
    else:
        info[j] = 'Open'

print(info)



