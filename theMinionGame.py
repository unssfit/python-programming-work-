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




get_player2_substring()
get_player1_substring()








#def minion_Game(string):

