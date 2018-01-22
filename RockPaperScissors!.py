import random


p1Mov = random.randint(0,2)
p2Mov = random.randint(0,2)
# 0 = sezo
# 1 = rock
# 2 = paper

def rps(p1,p2):
    if p1 == 'sezo' and p2 == 'paper':
        return 'Plaer1 Won'
    else:
        if p1 == 'paper' and p2 == 'sezo':
            return 'Player2 Won'
    if p1 == 'rock' and p2 == 'sezo':
        return 'Player1 Won'
    else:
        if p1 == 'sezo' and p2 == 'rock':
            return 'Player2 Won'
    if p1 == 'paper' and p2 == 'rock':
        return 'Player1 Won'
    else:
        if p1 == 'rock' and p2 == 'paper':
            return 'Player2 Won'
    if p1 == p2:
        return 'same Result Draw'

play1 = 'paper'
play2 = 'rock'
print(rps(play1,play2))
