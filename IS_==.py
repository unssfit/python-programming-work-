menu = []
menu.append(["eggs","spam","bacon"])
menu.append(["eggs","sausage","bacon"])
menu.append(["eggs","spam"])
menu.append(["eggs","bacon","spam"])
menu.append(["eggs","bacon","sausage","spam"])
menu.append(["spam","bacon","sausage","spam"])
menu.append(["spam","eggs","spam","spam","bacon","spam"])
menu.append(["spam","eggs","sausage","spam"])

for meal in menu:
        if not "spam" in meal:
            for ingredient in meal:
                print(ingredient)




#
# t = [1,25,48,56,6]
#
# d = t
# print(t is d)
# print(t == d)




