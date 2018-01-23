

string = '77547979754527797'

nw = list(string)

for i in range(len(nw)):
    if nw[i] == '9':
        nw[i] = ''
print(''.join(nw))
