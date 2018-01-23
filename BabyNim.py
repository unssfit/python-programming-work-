a,b,c = (3,4,5)
print('A: ',a,'\tB: ',b,'\tC: ',c)
print('Chose From this 3 Pile: "A" "B" "C"')
while (a != 0 or b != 0 or c != 0):
    pile = str(input('Choose a pile:'))
    rm = int(input('How many to remove from pile {}:'.format(pile)))
    if pile == 'a':
        a -= rm
    elif pile == 'b':
        b -= rm
    elif pile == 'c':
        c -= rm
    if (a == 0 and b == 0 and c == 0):
        print('All piles are empty. Good job')
    else:
        print('A: {}\t B: {}\t C: {}'.format(a, b, c))
