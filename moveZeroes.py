num = [0,1,2,0,13,44,0,56]
print(num)

index_0 = []
count = 0
for i in range(len(num)):
    if num[i] != 0:
        index_0.append(num[i])
    else:
        count += 1

for j in range(count):
    index_0.append(0)

print(index_0)



