# https://www.hackerrank.com/challenges/the-minion-game/problem
string = 'BANANA'
player1_words = {}
player2_words = {}

def get_player1_substring():
    vowels = 'AEIOU'
    count = 0
    for v in range(len(vowels)):
        if vowels[v] in string:
            word = string[string.index(vowels[v]):]
            for i in range(len(word)+1):
                wrd = word[:i]

                # count the substring in string
                if len(wrd) >= 1:
                    for item in range(0,len(word)):
                        if word[item:item+len(wrd)] == wrd:
                            count += 1

                    player1_words[wrd] = count
                    count = 0
    print(player1_words)

def get_player2_substring():
    vowels, count = 'AEIOU', 0
    for i in range(len(string)):
        if string[i] not in vowels:
            word = string[i:]
            for j in range(len(word)+1):
                wrd = word[:j]
                if len(wrd) >= 1:
                    for x in range(0,len(word)):
                        chunk = word[x:x+len(wrd)]
                        if  chunk == wrd:
                            count += 1
                    if not(player2_words.__contains__(wrd)):
                        player2_words.update({wrd:count})
                    count = 0
    print(player2_words)

def minion_Game():
    get_player2_substring()
    get_player1_substring()
    print('Game Start')
    # player 1 part
    p1_counter, p2_counter  = len(player1_words), len(player2_words)
    count, p1_word, p1_total = 0, [], 0
    while p1_counter != count:
        p1 = str(input('Enter the Word:'))
        if p1 in player1_words:
            count += 1
            p1_word.append(p1)
            p1_total += player1_words[p1]
            for key in p1_word:
                print(key, player1_words[key])

        else:
            print('Wrong Word! Tray Again!',end='')
    print('Total:',p1_total)

    # player2 part
    p2_total, p2_word, count2 = 0, [], 0
    while p2_counter != count2:
        p2 = str(input('Enter The Word:'))
        if p2 in player2_words:
            count2 += 1
            p2_word.append(p2)
            p2_total += player2_words[p2]
            for item in p2_word:
                print(item, player2_words[item])
        else:
            print('Wrong Word Tray Again! ',end='')
    print('total:', p2_total)   




minion_Game()










