
num = 20
arr = []
arr.append(num)
while num != 1:
    if num % 2 == 0:
        num = num // 2
        arr.append(num)
    else:
        num = (num*3)+1
        arr.append(num)
print('Collatz Conjecture Length:',len(arr))
