print('enter a number to see something Fun:')
star = int(input())

for x in range(1, star):
    print(' ' * x, end='')
    for b in range(star, star - 1, -1):
        print('*' * (star-x), end='')

    print("\n")


#best way to do this exercice
#note man9ol mn stackoverflow
print ("Pattern C")
for e in range (11,0,-1):
    print((11-e) * ' ' + e * '*')

print ('')
print ("Pattern D")
for g in range (11,0,-1):
    print(g * ' ' + (11-g) * '*')

