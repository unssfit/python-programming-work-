# https://www.codewars.com/kata/reversing-fun
# link of the problem

string = '012345'
string = ''.join(list(string)[::-1])
print(string)
for i in range(len(string)):
    string = string[:i+1] + ''.join(list(string[i+1:])[::-1])
    print(string)










