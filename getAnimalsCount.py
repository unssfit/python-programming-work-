

legs = 40
head = 11
horns = 6

# num of cows
cows = horns//2
print('cows = ',cows)
head -= horns//2
legs -= cows * 4
rabbit = legs//4
print('rabbit = ',rabbit)
legs -= (legs//4)*4
print('chikens = ',legs//2)




