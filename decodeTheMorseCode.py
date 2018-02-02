# https://www.codewars.com/kata/decode-the-morse-code
# first time work with dictionary

morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.',
         'h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.',
         'o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-',
         'v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..'
         }

def decodeMorse(string):
    space_holder,morse_ch, message = 0, [], ''
    for i in range(len(string)):
        if string[i] == ' ':
            word = string[space_holder:i]
            space_holder = i
            morse_ch.append(word)
    wrd = ''
    for j in range(len(string)-1,0,-1):
        if string[j] != ' ':
            wrd += string[j]
        else:
            break
    morse_ch.append(wrd)
    count, count2, count3, space = 0, 0, 0, ()
    for x in range(len(morse_ch)):
        string = ''
        for s in range(len(morse_ch[x])):
            if morse_ch[x][s] != ' ':
                string += morse_ch[x][s]
        if morse_ch[x] != ' ':
            count += 1
        else:
            count2 += 1
            if count2 == 2:
                space = (count,)
                count2 = 0

        for key, value in morse.items():
            if value == string:
                for n in range(len(space)):
                    if count3 == space[n]:
                        message += ' '
                count3 += 1
                message += key
    print(message)




decodeMorse('.... . -.--   .--- ..- -.. .')





