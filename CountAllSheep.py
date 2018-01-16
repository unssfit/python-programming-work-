

shep = [[1,2],[4,5]]
tl = 15
sm = 0
for i in range(len(shep)):
    for j in range(len(shep[i])):
        sm += shep[i][j]

lost = tl - sm
print(lost)
