

msg = '#textposteree errer #funny zzere #funnymemes #lol #comedy #comedian #lmfao' \
      ' #siblingsi #textposts,#textgram #text;;#words #thoughts #multifandom' \
      ' #voltron #voltronlegendarydefender fgfggf #vld #klance #aesthetic #aesthetictumblr' \
      ' #iphone #kpop #exo #shinee ererereer #onew #jonghyun #key #minho,#taemin #aestheticaccount'

hashTag = ''
for i in range(len(msg)):
    if msg[i] == '#':
        for j in range(i+1,len(msg)):
            if msg[j] != ' ':
                if msg[j] == ';' or msg[j] == ',':
                    print('hasTag:: ', '#' + hashTag)
                    hashTag = ''
                    break
                else:
                    hashTag += msg[j]
            else:
                print('hasTag:: ','#'+hashTag)
                hashTag = ''
                break


