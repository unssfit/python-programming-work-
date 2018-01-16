print('MICHELL\'S TINY ADVENTURE 2!')
print('upstairs or into Kitchen?')
usr = str(input('>'))
while True:
    if usr == 'Kitchen' or usr == 'back' or usr == 'downstairs':
        print('refrigerator or go "back"')
        usr = str(input('>'))
        print('use if 1 = ', usr)
        if usr == 'refrigerator':
            print('eat some food ("Yes or No?")')
            us = str(input('>'))
            if us == 'yes':
                print('The food is slimy and foul, You have died.')
                break
            else:
                print('You die because of starvation.game over')
                break
    else:
        if usr == 'upstairs':
            print('Go bedroom or bathroom or go back downstairs')
            usr = str(input('>'))
            print(usr)
