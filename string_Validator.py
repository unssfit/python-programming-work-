#for i in range(6):
#s = str(input("Enter s string : "))

# if s[i].isalnum():
#     print("True alphanumerical")
# else:
#     print("False")
#
# if  s[i].isalpha():
#     print('True alpha')
# else:
#     print('False')
#
# if  s[i].isdigit():
#     print("True digit")
# else:
#     print("False")
#
# if  s[i].islower():
#     print('True lower')
# else:
#     print('False')
#
# if s[i].isupper():
#     print('True upper')
# else:
#     print("False")

for i in range(0, len(s)):
    if s[i].isalnum():
        print("True")
        break
    else:
        print("False")


    if s[i].isalpha():
        print('True')
    else:
        print('False')

    if s[i].isdigit():
        print("True")
    else:
        print("False")

    if s[i].islower():
        print('True')
    else:
        print('False')

    if s[i].isupper():
        print('True')
    else:
        print("False")



# ss = 'qA2'
# print(ss.isalpha())
# s = "qA2"
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())