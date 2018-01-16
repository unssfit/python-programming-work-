import random
play = []
deal = []
for i in range(0,2):
    player = random.randint(1,10)
    dealer = random.randint(1,10)
    play.append(player)
    deal.append(dealer)

print('You drew {} and {}.'.format(play[0], play[1]))
print('Your Total is ',(play[0]+play[1]))

print('The Dealer has',deal[0],'and',deal[1])
print('Dealer\'s total is',(deal[0]+deal[1]))

if (play[0]+play[1]) > (deal[0]+deal[1]):
    print('Player WIN')
else:
    print('Dealer WIN')