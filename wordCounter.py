

def wordCounter(string):
    count = 1
    for i in range(len(string)):
        if string[i] == ' ' or string[i] == ',':
            count += 1
    return count


string = 'Create a function that takes a text file as input and returns the number of words contained in the text file.' \
         ' Please take into consideration that some words can be separated by a comma with no space. For example "Hi,it\'s me." ' \
         'would need to be counted as three words. For your convenience,you can use the text file in the attachment.'

print(len(string.split()))
res = wordCounter(string)
print(res)
print(len(string))
