
s1 = 'jason'
s2 = 'samson'

ch = 's'

string = ''
count = 0
while s1[count] is not ch:
    string += s1[count]
    count += 1
string += ch
string += s2[(s2.index(ch))+1:]
print(string)

