tab = [1, 22, 54, 8, 9, 112, 4545, 87, 52, 77, 44, 45]
temp = 0
for i in range(0, len(tab)):
    for j in range(i, len(tab)):
        if tab[j] > tab[i]:
            temp = tab[i]
            tab[i] = tab[j]
            tab[j] = temp

print(tab)


# a = 3
# b = 4
# c = 6
#
# p_list = []
# p_list.append(a)
# p_list.append(b)
# p_list.append(c)
# print('list before while: ', p_list)
# # i = 0
# # j = 0
# temp = 0
# for i in range(0, len(p_list)):
#     print('i = ', i)
#     for j in range(i, len(p_list)):
#         print('j = ', j)
#         if p_list[j] > p_list[i]:
#             temp = p_list[i]
#             p_list[i] = p_list[j]
#             p_list[j] = temp
#             # j += 1
#             # i += 1
#
# print(p_list)
