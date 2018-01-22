
string = '?how?much you cost??for this? hel? no dud?'


def remove_exclamation_mark(string):
    st = list(string)
    for i in range(len(st)):
        if st[i] == '?':
            st[i] = ''
    return ''.join(st)

res = remove_exclamation_mark(string)
print(res)
