import random

dirc = ['n','s','w','e']
walk = []
wereGo = []
for i in range(10):
    wereGo = []
    for j in range(4):
            direction = random.randint(0,4)
            if direction == 0:
                wereGo.append('n')
            elif direction == 1:
                wereGo.append('s')
            elif direction == 2:
                wereGo.append('w')
            else:
                wereGo.append('e')
    walk.append(wereGo)
    #wereGo[:] = []
print('walk[0] = ',walk[0])

#hadi bach ykon item 1 o tali mtsawyin drtiha bch tste for loop li that
# walk[-1] = []
# for g in range(len(walk[0])-1,0-1,-1):
#     walk[-1].append(walk[0][g])

print('walk[-1] = ',walk[-1])
street = False
for x in range(len(walk[0])):
    if walk[-1][(len(walk[-1])-1)-x] == walk[0][x]:
        print('Good Keep going in the same Street!')
        street = True
    else:
        print('Wrong Direction Try Another Route!')
        break
