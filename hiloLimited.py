import random
rNum = random.randint(1,100)
print('rNum = ',rNum)
print('I\'m thinking of a number between 1-100. you have 7 guesess.')
guess = 0
count = 0
while guess != rNum and count <= 7:
    count += 1
    guess = int(input('Enter a Guess : '))
    if guess > rNum:
        print('Too High.')
        if count == 7:
            print('Sorry, you didn\'t guess it in 7 tries.  You lose.')
    elif guess < rNum:
        print('Too Low.')
        if count == 7:
            print('Sorry, you didn\'t guess it in 7 tries.  You lose.')
    else:
        print('You Guessed it.')
        break


