import math



def trait_array(mylist):
    print(mylist)

arr = [0,3,4,5]
trait_array(arr)




sm = 0
for i in range(len(arr)):
    sm += arr[i]**2
print(sm)








def get_volume_of_cuboiud(len,wit,hig):
    return len*wit*hig

res = get_volume_of_cuboiud(21,5,41)
print(res)

