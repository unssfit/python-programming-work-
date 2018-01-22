n = [10,20,544,87,66,987,1040]

temp = 0
for i in range(1,len(n)):
    if n[i] > n[0]:
        temp = n[i]
        n[0] = temp

print("the Bigest number :{}".format(n[0]))

