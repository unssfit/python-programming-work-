print('Enter 3 integers : ')
s1 = int(input('side 1 :'))
s2 = int(input('Side 2:'))
while s2 < s1:
    print(s2,'is smaller than',s1,' Tray Again.')
    s2 = int(input('Side 2: '))

s3 = int(input('Side 3:'))
while s3 < s2:
    print(s3,'is smaller than',s2,'Tray Again.')
    s3 = int(input('side 3: '))


print('your three Sides are : ',s1,s2,s3)
print('These sides *do* make a right triangle.  Yippy-skippy')
