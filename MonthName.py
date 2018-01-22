
user = 8
def getMonthName(user):
    months = [[1,'January'],
            [2,'February'],
            [3,'March'],
            [4,'April'],
            [5,'May'],
            [6,'June'],
            [7,'July'],
            [8,'August'],
            [9,'September'],
            [10,'October'],
            [11,'November'],
            [12,'December']]

    for i in range(len(months)):
        if months[i][0] == user:
            return months[i][1]

res = getMonthName(user)
print(res)