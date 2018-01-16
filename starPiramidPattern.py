starNum = 5

for i in range(0, starNum + 1):
    print('*' * i)

for i in range(0, starNum):
    for j in range(i, i + 2):
        print('*' * j, end='')

    print()



inc = 1
for d in range(starNum,0, -1):
    print(("#"*d)+('*'*(starNum-(starNum-inc))))
    inc += 1


