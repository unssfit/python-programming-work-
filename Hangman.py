import random

wor = ['hello','tomato','fishman','pizzahut','gosmen']
pik = random.randint(0,4)
word,check_word = (wor[pik],'')
print('word = ',word)

for i in range(0,len(word)):
    print('- ',end='')
print()

ch_list,wrd = (list(word),word)
for v in range(0,len(ch_list)):
    if ch_list[v] != '-':
        ch_list[v] = '-'

ch_dub,ch_found = ([],[])
count,check = (0,False)

while check_word != word:
    char = str(input('Guess: '))
    for s in range(0,len(wrd)):
        if char == wrd[s]:
            count += 1
            if count >= 2 and char not in ch_found:
                ch_found.append(char)
                ch_dub.append(wrd[wrd.index(char)])
                ch_dub.append(wrd[s])
                check = True
    count = 0

    for s in range(0, len(word)):
        if char == word[s] and check != True:
            ch_list[s] = char
        else:
            if char == word[s] and check == True:
                for j in range(0, len(ch_dub)):
                    if char == ch_dub[j]:
                        ch_list[s] = char
                        ch_dub[j] = ''

    check = False
    print(' '.join(ch_list))
    check_word = ''.join(ch_list)
