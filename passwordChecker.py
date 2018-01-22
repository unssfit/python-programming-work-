

pwds = str(input('Enter Your Password: '))
usr = str(input('Enter Your Username:'))
uper = False
isDigi = False

while True:
    for j in range(len(pwds)):
        if pwds[j].isupper():
            uper = True

    for x in range(len(pwds)):
        if pwds[x].isalnum():
            isDigi = True

    if len(pwds) >= 5 and uper is True and isDigi == True:
        print('Your Password Is Valid.')
        break
    else:
        if len(pwds) < 5 and uper == False and isDigi == False:
            print('password Requirement is Faild.')
        elif len(pwds) < 5 and uper == False:
            print('password mus 1 upper Char.and leng grether then 5.')
        elif len(pwds) < 5:
            print('password must be beyond 5.')
        elif len(pwds) < 5  and isDigi == False:
            print('password must be grethre than 5 and have a digit.')






        pwds = str(input('Invalid Password! Try Again:'))

