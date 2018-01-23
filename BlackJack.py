import random

b1 = False
b2 = False
print('WELCOM TO MITCHELL\'S BLACKJACK')
playerSum = 0
player_card = []
dealer_card = []
count = 0
while True:
    if count == 0:
        for i in range(0, 2):
            player = random.randint(2, 11)
            player_card.append(player)
            dealer = random.randint(2, 11)
            dealer_card.append(dealer)

        playerSum = player_card[0] + player_card[1]
        print('Player you get', player_card[0], 'and', player_card[1])
        print('Your Total is:', playerSum)
        print('The dealer has a', dealer_card[0], 'and a hidden card.')
        print('His total is hidden too.')

    if count % 2 == 0:
        print('Player turn')
        hitOrNot = str(input('Would you like to "hit" or "Stay"?:'))
        while hitOrNot == 'hit':
            player = random.randint(2, 11)
            print('You drew a', player)
            playerSum += player
            print('your total is:', playerSum)
            if playerSum > 21:
                print('the player "Busts". you Lose!')
                b1 = True
                break
            hitOrNot = str(input('Would you like to "hit" or "Stay"?:'))
    else:
        print()
        print('okay, dealer\'s turn.')
        print('his hiddan card was : ', dealer_card[1])
        dealerSum = dealer_card[0] + dealer_card[1]
        print('his Total: ', dealerSum)
        hitOrNot = str(input('Would you like to "hit" or "Stay"?:'))
        while hitOrNot == 'hit':
            print('dealer chose to hit.')
            dealer = random.randint(2, 11)
            print('He drew a', dealer)
            dealerSum += dealer
            print('His Total:', dealerSum)
            if dealerSum > 16:
                print('Dealer you busted.you lose')
                b2 = True
                break
            hitOrNot = str(input('Would you like to "hit" or "Stay"?:'))

    if b1:
        print('the player "Busts". you Lose!')
        break
    elif b2:
        print('Dealer you busted.you lose')
        break
    count += 1
