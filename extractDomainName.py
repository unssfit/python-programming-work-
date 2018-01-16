

url = str(input('Enter a URL: '))

domain = ''
index = url.index('.')
for i in range(index+1,len(url)):
    if url[i] is not '/':
        domain += url[i]
    else:
        break
print('Domain Name: ',domain)

