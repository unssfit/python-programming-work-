

string = '1 2 3'


def summy(string):
    sm = 0
    for i in range(len(string)):
        if string[i] is not ' ':
            sm += int(string[i])
    return sm

res = summy(string)
print(res)