import math
a = -10
if a < 0:
    print("true")

while True:
    n = int(input('Enter a number : '))
    if n > 0:
        print('The square Root of',n,'is',math.sqrt(n))
        break
    else:
        print("You can't take the square root of a negative number, silly")
          