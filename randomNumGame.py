import random

ans = random.randint(1,10)
print('ans = ',ans)
i = 0
while i < 3:
    usr = int(input('enter a number : '))
    if usr != ans:
        if usr < ans:
            print('Wrong ! try a little higher : ')
            usr = int(input("try again : "))
            if usr == ans:
                print('good you made it!!')
        else:
            if usr > ans:
                print('Wrong! tray lower.')
                usr = int(input('try again : '))
                if usr == ans:
                    print('YEAH! you got it!')
    else:
        print('Very God at First time!')
    i += 1
