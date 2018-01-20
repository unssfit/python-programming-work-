import random
sudoku = [	 #0  #1  #2  #3  #4  #5  #6  #7  #8
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#0
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#1
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#2
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#3
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#4
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#5
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#6
            [' ',' ',' ',' ',' ',' ',' ',' ',' '],#7
            [' ',' ',' ',' ',' ',' ',' ',' ',' '] #8
        ]
#print(sudoku)
def num_generator():
    numbers = []
    for i in range(random.randint(3,4)):
        num = random.randint(1,9)
        while num in numbers:
            num = random.randint(1,9)
        numbers.append(num)
    return numbers

def generate_random_array_indexs(arr,arr2):
    index = []
    for i in range(len(arr)):
        n = random.randint(0,9)
        while n in index:
            n = random.randint(0, 9)
        index.append(n)
        if n == 9:
            arr2[n-1] = arr[i]
        else:
            arr2[n] = arr[i]

def printSudoku(arr):
    string = ''
    for i in range(len(arr)):
            string += str(arr[i])
    return string

def sudoku_interface(string):
    #print('--'*len(string))
    print('|', end='')
    for i in range(len(string)):
        print(string[i]+'|',end='')
    print()

def check_duplicate_numbers_columns():
    columns_numbrs,duplicate_num = [],[]
# get columns numbers
    for x in range(len(sudoku)):
        temp_num = []
        for i in range(len(sudoku)):
            if sudoku[i][x] is not ' ':
                temp_num.append(('['+str(i)+']'+'['+str(x)+']',sudoku[i][x]))
        columns_numbrs.append(temp_num)

# check for duplicate numbers
    for s in range(len(columns_numbrs)):
        for a in range(len(columns_numbrs[s])):
            for b in range(a+1,len(columns_numbrs[s])):
                 if columns_numbrs[s][a][1] == columns_numbrs[s][b][1]:
                    duplicate = (columns_numbrs[s][b][0],columns_numbrs[s][b][1])
                    if duplicate not in duplicate_num:
                        duplicate_num.append(duplicate)
    return duplicate_num

def replace_duplicate_numbers_columns(dubplicate_numbrs):
    for i in range(len(dubplicate_numbrs)):
        r = dubplicate_numbrs[i][0]
        #print(r,':',sudoku[int(r[1])][int(r[4])])
        nw_num = random.randint(1,9)
        columns = []
        for j in range(len(sudoku)):
            columns.append(sudoku[j][int(r[4])])
        while nw_num in sudoku[int(r[1])] or nw_num in columns:
            nw_num = random.randint(1,9)
        sudoku[int(r[1])][int(r[4])] = nw_num

def replace_bigSquare_numbers():
    squares = []
    # divide sudoku into big square
    for i in range(len(sudoku)):
        small_arr = []
        for j in range(0,len(sudoku[i]),3):
            small_arr.append(sudoku[i][j:j+3])
        squares.append((i,small_arr))
    #print(squares)

    # get sudoku big square verticaly one at a time
    square = []
    for h in range(3):
        for x in range(len(squares)):
            square.append((squares[x][0],squares[x][1][h]))
    #print(square)

        # split squares to look for duplicate numbers
        square_holder = []
        for k in range(0,len(square),3):
                square_holder.append(square[k:k+3])
                #print(square_holder)
                for c in range(len(square_holder)):
                    for m in range(2):
                        for w in range(len(square_holder[c][m][1])):
                            for p in range(m+1,len(square_holder[c])):
                                for k in range(len(square_holder[c][p][1])):
                                    if square_holder[c][m][1][w] == square_holder[c][p][1][k] and square_holder[c][m][1][w] != ' ':
                                        #print(square_holder[c][p][0],':',square_holder[c][p][1][k])
                                        index = sudoku[square_holder[c][p][0]].index(square_holder[c][p][1][k])
                                        # change the numbers in sudoku
                                        new_num = random.randint(1,9)
                                        column = []
                                        for y in range(len(sudoku)):
                                            column.append(sudoku[y][index])

                                        # while new_num == square_holder[c][p][1][k]:
                                        #     new_num = random.randint(1,9)

                                        # while new_num in sudoku[square_holder[c][p][0]] or new_num in column:
                                        #     new_num = random.randint(1,9)
                                        #     while new_num == square_holder[c][p][1][k]:
                                        #         new_num = random.randint(1, 9)

                                        while True:
                                            new_num = random.randint(1,9)
                                            if new_num not in sudoku[square_holder[c][p][0]] and new_num not in column and new_num != square_holder[c][p][1][k]:break
                                        sudoku[square_holder[c][p][0]][index] = new_num
    
                square_holder[:] = []
        square[:] = []

def fill_sudoku():
    for j in range(len(sudoku)):
        generate_random_array_indexs(num_generator(),sudoku[j])
        string = printSudoku(sudoku[j])
        sudoku_interface(string)

# TO DO START PLAYING NEED GAME LOGIC

def get_empty_indexs():
    empty_field = []
    for i in range(len(sudoku)):
        empty_field.append((i,))
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == ' ':
                empty_field[i] = empty_field[i] + (j,)
    #print(empty_field)
    return empty_field

def start_playing_sudoku(arr):
    for i in range(len(arr)):
        print('['+str(arr[i][0])+']',end='')
        for j in range(1,len(arr[i])):
            print(arr[i][j],end='')
        print()

    row = int(input('enter wish Row:'))
    index = int(input('chose wish index you want to play:'))
    number = int(input('Enter Your Number:'))

    # get Column
    column = []
    for x in range(len(sudoku)):
        column.append(sudoku[x][index])

    # Check if the given number already exist
    while number in sudoku[row] or number in column:
        if number in sudoku[row]:
            number = int(input('Already Exist in Row Choose Another Number ("0" to exit):'))
        else:
            number = int(input('Already Exist in Column Choose Another Number ("0" to exit):'))
        if number == 0:break
    sudoku[row][index] = number


fill_sudoku()
duplicate_nm = check_duplicate_numbers_columns()
replace_duplicate_numbers_columns(duplicate_nm[:])
replace_bigSquare_numbers()
emptyIndex = get_empty_indexs()
start_playing_sudoku(emptyIndex[:])


print('*** GAME START ***')
for v in range(len(sudoku)):
    string2 = printSudoku(sudoku[v])
    sudoku_interface(string2)











