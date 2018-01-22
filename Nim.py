player1 = str(input('Player 1, Enter Your name:'))
player2 = str(input('Player 2, Enter Your Name: '))

a = 4
b = 5
c = 6
count = 1
print('A:', a, '\tB:', b, '\tC:', c)
player1_count = 0
player2_count = 0

while (a != 0 or b != 0 or c != 0):
    count += 1

    # User input
    if count % 2 == 0:
        pile = str(input('{}, choose a pile:'.format(player1)))
        if (pile == 'a' and a == 0) or (pile == 'b' and b == 0) or (pile == 'c' and c == 0):
            pile = str(input('Nice try, {}. That pile is Empty.choose again: '.format(player1)))
        rm = int(input('How many to remove from pile {}:'.format(pile)))
        if rm == 0 or ((pile == 'a' and rm > a) or (pile == 'b' and rm > b) or (pile == 'c' and rm > c)) or (rm < 0):
            if rm == 0 or rm < 0:
                rm = int(input('You must choose at least 1. How many?: '))
            else:
                rm = int(input('Pile {} doesn\'t have that many. Try again:'.format(pile)))
        player1_count += 1
    else:
        pile = str(input('{}, choose a pile:'.format(player2)))
        if (pile == 'a' and a == 0) or (pile == 'b' and b == 0) or (pile == 'c' and c == 0):
            pile = str(input('Nice try, {}. That pile is Empty.choose again: '.format(player2)))
        rm = int(input('How many to remove from pile {}:'.format(pile)))
        if (rm == 0) or ((pile == 'a' and rm > a) or (pile == 'b' and rm > b) or (pile == 'c' and rm > c)) or (rm < 0):
            if rm == 0 or rm < 0:
                rm = int(input('You must choose at least 1. How many?: '))
            else:
                rm = int(input('Pile {} doesn\'t have that many. Try again:'.format(pile)))
        player2_count += 1


    # operation of counters in the piles
    if pile == 'a':
        a -= rm
    elif pile == 'b':
        b -= rm
    elif pile == 'c':
        c -= rm

        # print('A:',a,'\tB:',b,'\tC:',c)
        # print('A:','*'*a)
        # print('B:','*'*b)
        # print('C:','*'*c)

    # Sort the list to print it on console
    p_list = []
    p_list.append(a)
    p_list.append(b)
    p_list.append(c)
    temp = 0
    for i in range(0, len(p_list)):
        # print('i = ', i)
        for j in range(i, len(p_list)):
            # print('j = ', j)
            if p_list[j] > p_list[i]:
                temp = p_list[i]
                p_list[i] = p_list[j]
                p_list[j] = temp

    print(p_list)

    for f in range(p_list[0],0,-1):
        print('\t*', end='')
        if f <= p_list[2]:
            print(' *',end='')
        if f <= p_list[1]:
            print(' *',end='')
        #print(' *',end='')
        print()

    print('\tC B A')
            # Termined to game and declare the winner
    if (a == 0 and b == 0 and c == 0):
        if player1_count > player2_count:
            print('{}, there are no counters left, so you WIN!'.format(player2))
        else:
            print('{}, there are no counters left, so you WIN!'.format(player1))
