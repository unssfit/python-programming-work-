
#string = 'youness'
string = str(input('Enter a String: '))

def remove_char(string):
    newStr = list(string)
    newStr[0] = ''
    newStr[-1] = ''
    return ''.join(newStr)


cut = remove_char(string)
print(cut)
