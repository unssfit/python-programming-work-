
def make_negative(num):
    n_str = str(num)

    if n_str[0] == '-':
        return num
    else:
       return n_str.rjust(len(n_str)+1,'-')


#s = 'hello'
#print(s.rjust(len(s)+1,'-'))

res = make_negative(1235)
print(res)