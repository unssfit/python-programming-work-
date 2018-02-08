# https://www.codewars.com/kata/decoded-string-by-the-numbers

string = 'abc\\5defghi\\2jkl'

ch_holder, spot1, spot2 = [], 0, 0
for i in range(0,len(string)):
    if string[i] == '\\':
        spot1 = i+2
        spot2 = (i+2) + int(string[i+1])
        ch_holder.append(string[spot1:spot2])
    else:
        if i >= spot1 and i < spot2:
            continue
        else:
            if not(string[i].isdigit()):
                ch_holder.append(string[i])
print(ch_holder)



