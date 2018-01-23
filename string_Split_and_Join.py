print("Hello %s %s! You just delved"
      " into python "
% (str(input("enter ur name :"))
   ,str(input("enter ur last name:"))))

string  = "this is a srting"
string = string.split(" ")
print("-".join(string))
#string = "-".join(string)
#print(string)


#another solution
print(*input().split(" "), sep='-')


#another solution
line = "can you do me a favor"
print("-".join(line.split(" ")))
