num = int(input('Starting Number: '))
list_of_numbers = []
count = 0
while num != 1:
    if num % 2 == 0:
        num = int(num/2)
        list_of_numbers.append(num)
        print(num,end='\t')
    else:
        num  = (num * 3) + 1
        list_of_numbers.append(num)
        print(num,end='\t')

    count += 1
print()
#print(list_of_numbers)
temp = 0
bigNum = list_of_numbers[0]
for i in range(1,len(list_of_numbers)):
    if list_of_numbers[i] > list_of_numbers[0]:
        #temp = list_of_numbers[0]
        list_of_numbers[0] = list_of_numbers[i]
        list_of_numbers[i] = list_of_numbers[0]


#print(list_of_numbers)
print('big number: ',list_of_numbers[0])





