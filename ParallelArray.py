import base64

s = 'aHR0cHM6Ly9tZWdhLm56LyMhQjNoU0ZBUUEhRjRwMFZWYU9qM2hrRy1Ub1NVQ2FzemNZeGw2S2ZsbVB2eHQ2R0M0cTRmOA=='
def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

string = base64ToString(s)

print(string)

lastName = ['josh','mandez','ragen','james']
grad = [12.55,45.22,87.55,89.65]
id = [112252,145255,454878,798989]


idNum = int(input('ID number to find:'))

idSlot = None
info = []
slot = 0
for i in range(0,len(id)):
    if idNum == id[i]:
        slot = i
        # for j in range(0,len(lastName)):
        #     if j == i:

print('Found in Slot',slot)
print(' \tName:',lastName[slot],'\n','\tAverage:',grad[slot],'\n','\tID:',id[slot])


