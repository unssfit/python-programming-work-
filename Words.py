print(set('youness'))

door_key = 'nice eligal lower root terminology youness'

#count wordds on door_key
count = 1
for i in range(len(door_key)):
    if door_key[i] == ' ':
        count += 1
#get plates from user
plates = []
for j in range(count):
    plate = str(input('Plate {} enter your key: '.format(j)))
    plates.append(plate)
print(plates)


if door_key == ' '.join(plates):
    print('Enter you Room! Well Done!')



