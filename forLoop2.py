string = 'hello there hw are you'
string_Lenght = len(string)
print('string LEnght : ',string_Lenght)

#always exclude the last number
print(string[4],string[0:6])
print(string[:8],string[5:])
print('item 5 = ',string[6])


num = [45,48,22,87,9,2]
num2 = num + [45,55,87,111]
print(num2)
print(num)

#asign new item to the list
num[:2] = ['you','me']
print(num)
#yla briti tjbed list kamla rir b (:)
print(num[:])
#yla briti tmhi chi item mn list
num[2] = []
print(num)
print('num = ',len(num))

#delete list kamla
num[:] = []
print('num = ',len(num))





