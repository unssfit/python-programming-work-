board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]

word = 'ABCCED'
count1,count2,res = (1,0,True)
for i in range(len(word)):
    for s in range(i+1,len(word)):
        if word[i] == word[s]:
            count1 += 1

    for j in range(len(board)):
        for x in range(len(board[j])):
            if word[i] == board[j][x]:
                count2 += 1

    if count1 > count2:
        print('False')
        res = False
        break
    else:
        count1 = 1
        count2 = 0
if res:
    print('True')