
num = 1544

if len(str(num)) == 2:
    print(" '{} + {}' ".format(int(str(num)[0])*10,str(num)[1]))
elif len(str(num)) == 3:
    hun = int(str(num)[0])*100
    ten = int(str(num)[1])*10
    sin = str(num)[2]
    print("'{} + {} + {}'".format(hun,ten,sin))
elif len(str(num)) == 4:
    tow = int(str(num)[0])*1000
    hun = int(str(num)[1])*100
    ten = int(str(num)[2])*10
    sin = str(num)[3]
    print("'{}+{}+{}+{}'".format(tow,hun,ten,sin))
