from bs4 import BeautifulSoup
import urllib.request
import resuests
#openurl = urllib.request.urlopen('https://wwww.google.com/')
#print(openurl)




string = 'yoousssgf'
dup = ()
count = 1
for i in range(len(string)):
    for j in range( i +1 ,len(string)):
        if string[i] == string[j]:
            count += 1
            #dup += string[i]
    print(string[i] ,'repeats' ,count ,'times.')
    count = 1
print(dup)
