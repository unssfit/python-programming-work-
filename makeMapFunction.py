

def map(function, array):
    resul = []
    if function == 'strr':
        array = [str(array[i]) for i in range(len(array))]
        print(array)
    elif function == 'sum':
        sum = 0
        for j in range(len(array)):
            if type(array[j]) == type(0):
                sum += array[j]
            else:
                if type(array[j]) == type([]):
                    sum2 = 0
                    for x in range(len(array[j])):
                        sum2 += array[j][x]
                    resul.append(sum2)
        resul.append(sum)
        print(resul)
    elif function == 'int':
        array = [int(array[a]) for a in range(len(array))]
        print(array)




map('sum',[[12,5,48],12,100,232,[14,47,800]])
map('int', ['1','22','36','415'])

