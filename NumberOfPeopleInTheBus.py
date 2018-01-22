import random
bus_info = []

for i in range(10):
    bus = []
    bus.append(random.randint(1,15))
    if i == 0:
        bus.insert(1,0)
    else:
        bus.append(random.randint(1,bus[0]+2))
    bus_info.append(bus)

for j in range(len(bus_info)-1):
    p = (bus_info[0][0]+bus_info[j+1][0]) - bus_info[j+1][1]
    bus_info[0][0] = p
print('Number of People Still On bus: ',p)
