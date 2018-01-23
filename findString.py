# s = "howold are old you jonathen"
# sub = 'wol'
# asw = sub in s
# print(asw)
# c = 0
# bool = False
# temp = 0
# x = 0
# cc = 0
# count = 0
# char = []
# print("sub lenght = ",len(sub))
# for cou in range(0,len(sub)):
#     for x in range(0,len(s)):
#         if s[x] == sub[cou]:
#             char.append(s[x])
#             s2 = ''.join(char)
#             print("s2 = ",s2)
#             print("char lengh = ",len(char))
#             if s2 == sub:
#                 print(s2)
#                 count += 1
#             #break
#             else:
#                 if len(char) >= len(sub):
#                     #tab = list(char)
#                     char[-1] = []
#
# #print("count = ",count)
# print(char)


string = str(input("Enter String to Analyse : "))
sub_string = str(input('Enter what you looking for:'))
# s = "howold are old youare are woljonathen"
# sub = 'are'
a = ""
count = 0
for x in range(0, len(string)):
    a = string[x:len(sub_string) + x]
    if a == sub_string:
        count += 1

print("count = ", count)
