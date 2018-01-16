

def addition(a,b):
    return a+b

def subsraction(a,b):
    return a-b

def division(a,b):
    return a/b

def multiplication(a,b):
    return a*b

while True:
    string = str(input('>'))

    if string[0] == '0':break
    else:
        if string[1] == '+':
            print(addition(int(string[0]),int(string[2])))
        elif string[1] == '-':
            print(subsraction(int(string[0]),int(string[2])))
        elif string[1] == '*':
            print(multiplication(int(string[0]),int(string[2])))
        else:
            print(division(int(string[0]),int(string[2])))










