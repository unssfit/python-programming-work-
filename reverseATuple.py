tup = tuple(range(10))
#print(tup)
l = list(tup)
#print(l)
l2 = l[::-1]
#print(tuple(l2))

# replace last value of tuples in a list(my way)
tulps = []
for i in range(5):
    tulps.append(tuple(range(1,5)))
print(tulps)

for j in range(len(tulps)):
    arr = list(tulps[j])
    arr[-1] = 'gg'
    tulps[j] = tuple(arr)
print(tulps)

# replace last value of tuples in a list (simplst way to do it)
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])



