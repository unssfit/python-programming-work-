string = "HackerRank.com presents \"Pythonist 2"

newString = []
for ch in string:
    newString.append(ch)

for i in range(newString.__len__()):
    if newString[i].isupper():
        newString[i] = newString[i].lower()
    else:
        newString[i].islower()
        newString[i] = newString[i].upper()

resu = ''
for j in range(newString.__len__()):
    resu += newString[j]

print(resu)





