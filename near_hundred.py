unwanted_ch = [':','¨<','>','?','|','*','/','\\','"']
print(unwanted_ch)

string = 'football'
index = 5
string_nw = list(string)
string_nw[index] = ''
print(''.join(string_nw))




# number near to 100
usr = int(input('Enter Your Number:'))

if usr >= 100 and usr <= 200:
    print(True)
else:
    print(False)

