


def chek_word_pattern(word,pattern):
    string = word.split()
    if pattern == 'abba':
        if string[0] == string[len(string)-1] and string[1] == string[2]:
            print(pattern,True)
        else:
            print(pattern,False)
    elif pattern == 'aaaa':
        chek = True
        for i in range(len(string)):
            if string[0] != string[i]:
                chek = False
        if chek:
            print(pattern,True)
        else:
            print(pattern,False)




pattern = 'aaaa'
word = 'dog dog dog dog'
chek_word_pattern(word,pattern)

