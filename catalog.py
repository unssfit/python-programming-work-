# https://www.codewars.com/kata/catalog
# problem link

string = '''<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>

<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>

<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>'''

def catalog(string,string2):
    for i in range(len(string)):
        word = string[i:i+len(string2)]
        if word == string2:
            wrd = string[i:]
            info, count, num = [], 0, ''
            for x in range(len(wrd)):
                if wrd[x].isdigit() or wrd[x] == '.':
                    num += wrd[x]
                else:
                    if num != '':
                        count += 1
                        info.append(num)
                        num = ''
                    if count == 2:break
            #print(info)
            print(string2,'prx:',info[0],'qty:',info[1])

catalog(string,'hammer')

















