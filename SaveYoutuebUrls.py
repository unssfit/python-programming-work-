from bs4 import BeautifulSoup
import requests
import pyperclip

# get the url from clipboard and get request
url = pyperclip.paste()
res = requests.get(url)
data = res.content
res.close()
soup = BeautifulSoup(data,'html.parser')
title = soup.find('title')

# get Title from Url
title = str(title)
title = title[title.index('>')+1:]
title = title[:title.index('<')]

# remove unwanted character to be able to save the file
title = list(title)
unwanted_ch = [':','¨<','>','?','|','*','/','\\','"']
for i in range(len(title)):
    if title[i] in unwanted_ch:
        title[i] = ''
title = ''.join(title)

# create the File
text_to_save = url
saveFile = open('C:/Users/unss/Desktop/'+title+'.txt','w')
saveFile.write(text_to_save)
saveFile.close()


