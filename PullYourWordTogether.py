

string = 'i about you dream'
new_string = list(string)
index = 0
for i in range(len(new_string)):
    if new_string[i] is ' ':
        index = i
        break

s = string[:index]
nw = s.upper() + string[index:]+'.'
print(nw)
