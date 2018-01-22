
string = 'https://www.youtube.com/watch?v=rE7If2QIAyo'

sub = 'ube.com'
for i in range(len(string)):
    if string[i:i+len(sub)] == sub:
        print(string[i:i+len(sub)])

# if sub in string:
#     print(string.index(sub))


