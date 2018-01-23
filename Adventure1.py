print('WELCOM TO MICHELL\'S TINY ADVENTURE!')

print('You are in a creepy house! Would you like to go "upstairs" or into the "Kitchen"?')
usrIn = str(input('>'))

if usrIn == 'Kitchen':
    print('There is a long countertop with dirty dishes everywhere.  Off to one side\
there is, as you\'d expect, a refrigerator. You may open the "refrigerator"\
or look in a "cabinet"')
    u1 = str(input('>'))
    if u1 == 'refrigerator':
        print('Inside the refrigerator you see food and stuff.  It looks pretty nasty.\
Would you like to eat some of the food? ("yes" or "no")')
        if str(input('>')) == 'no':
            print('You die of starvation.. eventually.')
    else:
        print('Your are in a cabinet "Rest" or come back or go ')
else:
    print('Upstairs you see a hallway.  At the end of the hallway is the master\
"bedroom".  There is also a "bathroom" off the hallway.  Where would you like\
to go?')
    if str(input('>')) == 'bedroom':
        print('You are in a plush bedroom, with expensive-looking hardwood furniture.  The\
bed is unmade.  In the back of the room, the closet door is ajar.  Would you\
like to open the door? ("yes" or "no")')
        if str(input('>')) == 'no':
            print('Well, then I guess you\'ll never know what was in there.  Thanks for playing,\
I\'m tired of making nested if statements')
        else:
            print('Good for you you will be a rich men.')


