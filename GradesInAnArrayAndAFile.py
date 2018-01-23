import random
usr = str(input('enter your name:'))
file = str(input('file name:'))
grad = []


for i in range(1,7):
    grad.append(random.randint(1,100))
    #print(grad[i])

print('Here are your randomly-selected grades(Hope you pass):')
for j in range(1,len(grad)):
    print('grade',j,':',grad[j])

print('Data saved in "{}"'.format(file))
