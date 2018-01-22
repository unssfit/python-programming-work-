co1,co2,co3,co4,co5,co6 = (0,0,0,0,0,0)
x_cou1,x_cou2,x_cou3,x_cou4 = (0,0,0,0)
x_play,count,play_counter = (0,0,0)
arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
while True:
    if count % 2 == 0:
        location = str(input("\"O\", choose your location (row,column):"))
        arr[int(location[0])][int(location[2])] = 'O'
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                print(arr[i][j], end='')
            print()

    else:
        loc = str(input("\"X\", choose your location (row,column):"))
        arr[int(loc[0])][int(loc[2])] = 'X'
        for f in range(0, len(arr)):
            for h in range(0, len(arr[f])):
                print(arr[f][h], end='')
            print()
    count += 1

    for s in range(0,len(arr)):
        if arr[s][0] == 'O':
            print('co4 = ',co4)
            co4 += 1
            if co4 == 3:
                print('player win first loop!')
        else:
            if arr[s][0] == 'X':
                x_cou1 += 1
                if x_cou1 == 3:
                    print('x_cou1 WON ',)
        if arr[s][1] == 'O':
            co5 += 1
            if co5 == 3:
                print('co5 = ',co5)
        else:
            if arr[s][1] == 'X':
                x_cou2 += 1
                if x_cou2 == 3:
                    print('x_cou2 WON')
        if arr[s][2] == 'O':
            co6 += 1
            if co6 == 3:
                print('co6 = ',co6)
        else:
            if arr[s][2] == 'X':
                x_cou3 += 1
                if x_cou3 == 3:
                    print('x_cou3 WON')

        for x in range(0,len(arr[s])):
            if arr[s][x] == 'O':
                co1 += 1
                if co1 == 3:
                    print('Player 1 WON!')
            else:
                if arr[s][x] == 'X':
                    x_play += 1
                    if x_play == 3:
                        print('x_play WON!')
        co1 = 0
        x_play = 0
    x_cou1 = 0
    x_cou2 = 0
    x_cou3 = 0
    co6 = 0
    co5 = 0
    co4 = 0

    if (arr[0][0] == 'O') and (arr[1][1] == 'O') and (arr[2][2] == 'O') :
        print('player WON Karwa')
    else:
        if (arr[0][0] == 'X') and (arr[1][1] == 'X') and (arr[2][2] == 'X'):
            print('player x Won kerwa')
    if (arr[0][2] == 'O') and (arr[1][1] == 'O') and (arr[2][0] == 'O'):
        print('player won kerwa 2')
    else:
        if (arr[0][2] == 'X') and (arr[1][1] == 'X') and (arr[2][0] == 'X'):
            print('plyer x Won kerwa 2')

