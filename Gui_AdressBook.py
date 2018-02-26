from tkinter import *
from tkinter import ttk
import time
from functools import partial

# http://programmingbydoing.com/a/project-address-book.html

root = Tk()
root.geometry('600x500')

choice = StringVar()

title = Label(root, text='Adress Book')
title.config(font=('Courier', 20, 'bold'))
title.place(x=220, y=10)


def adressBook(string):
    lName = StringVar()
    if string == 'Load from file':

        lab = Label(root, text='Author Last Name:')
        lab.config(font=('Courier', 13, 'bold'))
        lab.place(x=10, y=130)

        load = Entry(root, textvariable=lName)
        load.place(x=200, y=133)
        def loadData():
            info = {}
            entrys = []
            fopen = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'r')
            line = fopen.readline()
            while line:
                cline = line.strip()
                if not '*' in cline and cline != '':
                    info[cline[:cline.index(':')]] = cline[cline.index(':')+1:]
                else:
                    entrys.append(info)
                    info = {}

                line = fopen.readline()
            fopen.close()

            data = {}
            for i in range(len(entrys)):
                for key in entrys[i]:
                    if entrys[i][key] == lName.get():
                        data = entrys[i]
                        break
            for item in data:
                print(item+':'+data[item])

        loadButton = Button(root,text='LOAD CONTENT',width=25,bg='#3D79C2',command=loadData)
        loadButton.config(font=('Courier', 13, 'bold'))
        loadButton.place(x=200,y=350)
    elif string == 'Save to file':
        username = StringVar()
        lastname = StringVar()
        email = StringVar()
        phone = StringVar()
        adress = StringVar()

        ulab = ttk.Label(root, text='First Name:')
        ulab.config(font=('Courier', 13, 'bold'))
        ulab.place(x=10, y=130)

        sentry = Entry(root, textvariable=username)
        sentry.place(x=200, y=130)

        llab = ttk.Label(root, text='Last Name:')
        llab.config(font=('Courier', 13, 'bold'))
        llab.place(x=10, y=180)
        lentry = Entry(root, textvariable=lastname)
        lentry.place(x=200, y=180)

        plab = ttk.Label(root, text='Phone Number:')
        plab.config(font=('Courier', 13, 'bold'))
        plab.place(x=10, y=230)
        pentry = Entry(root, textvariable=phone)
        pentry.place(x=200, y=230)

        elab = ttk.Label(root, text='Email Adress:')
        elab.config(font=('Courier', 13, 'bold'))
        elab.place(x=10, y=280)
        eentry = Entry(root, textvariable=email)
        eentry.place(x=200, y=280)

        plab = ttk.Label(root, text='Adress:')
        plab.config(font=('Courier', 13, 'bold'))
        plab.place(x=10, y=330)
        pentry = Entry(root, textvariable=adress)
        pentry.place(x=200, y=330)

        def saveInfo():
            sopen = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'a')
            sopen.write(
                'Username: ' + username.get() + '\n' + 'Lastname: ' + lastname.get() + '\n' + 'Phone: ' + phone.get() + '\n' + 'Adress: ' + adress.get() + '\n' + 'Email: ' + email.get())
            sopen.write('\n' + '*' * 20 + '\n')
            sopen.close()

        save = Button(root, text='Save', bg='#3D79C2', width=15, command=saveInfo)
        save.config(font=('Courier', 16, 'bold'))
        save.place(x=200, y=400)
    elif string == 'Add an entry':
        lastname = StringVar()
        entrydesc = StringVar()
        entrycontent = StringVar()
        # add_entry = ttk.Combobox(root,textvariable=entry)
        # add_entry.config(value=('Username','LastName',))
        # add_entry.place(x=160,y=160)

        lab = ttk.Label(root, text='Entry lastName:')
        lab.config(font=('Courier', 13, 'bold'))
        lab.place(x=10, y=160)

        add_entry = Entry(root, width=30, textvariable=lastname)
        add_entry.place(x=210, y=160)

        lab2 = ttk.Label(root,text='Entry Description:')
        lab2.config(font=('Courier', 13, 'bold'))
        lab2.place(x=10, y=220)

        entry2 = Entry(root,width=30,textvariable=entrydesc)
        entry2.place(x=210,y=220)

        lab3 = ttk.Label(root, text='Content To Add:')
        lab3.config(font=('Courier', 13, 'bold'))
        lab3.place(x=10, y=280)

        entry3 = Entry(root, width=30,textvariable=entrycontent)
        entry3.place(x=210, y=280)

        def addEntry():
            entrys = []
            info = {}
            aopen = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'r')
            line = aopen.readline()

            while line:
                cline = line.strip()
                if not '*' in cline and cline != '':
                    info[cline[:cline.index(':')]] = cline[cline.index(':') + 1:]
                else:
                    entrys.append(info)
                    info = {}
                line = aopen.readline()
            aopen.close()

            for i in range(len(entrys)):
                for item in entrys[i]:
                    if entrys[i][item] == lastname.get():
                        entrys[i].update({entrydesc.get():entrycontent.get()})
                        break
            #print(entrys)

            fh = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'w')
            for element in range(len(entrys)):
                for key, value in entrys[element].items():
                    fh.write(key+':'+value+'\n')
                fh.write('*'*30+'\n')
            fh.close()




        addButton = Button(root, text='ADD', bg='#3D79C2', width=15, command=addEntry)
        addButton.place(x=200, y=400)
    elif string == 'Remove an entry':

        lname = StringVar()
        entryToRemove = StringVar()
        lab = ttk.Label(root, text='Entry LastName:')
        lab.config(font=('Courier', 13, 'bold'))
        lab.place(x=10, y=160)

        rem_entry = Entry(root, width=30, textvariable=lname)
        rem_entry.place(x=180, y=160)

        lab2 = ttk.Label(root, text='Entry To Remove:')
        lab2.config(font=('Courier', 13, 'bold'))
        lab2.place(x=10, y=200)

        rm_entry = Entry(root, width=30, textvariable=entryToRemove)
        rm_entry.place(x=180, y=205)

        def removeEntry():
            tfile = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'r')
            entrys = []
            # read first line in the file
            info = {}
            line = tfile.readline()
            while line:
                line_clean = line.strip()
                if not '*' in line_clean:
                    info[line_clean[:line_clean.index(':')]] = line_clean[line_clean.index(':') + 1:]
                else:
                    entrys.append(info)
                    info = {}
                line = tfile.readline()
            # print(entrys)
            tfile.close()

            # remove Entry from dictionary
            for i in range(len(entrys)):
                for key in entrys[i]:
                    # print("1 = "+entrys[i][key])
                    if entrys[i][key] == lname.get():
                        # print("2 = "+entrys[i][key])
                        # print("3 = "+entrys[i][entryToRemove.get()])
                        del entrys[i][entryToRemove.get()]
                        break
            # print(entrys)

            # update the file (reupload data again)
            file2 = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'w')
            for x in range(len(entrys)):
                for keys in entrys[x]:
                    file2.write(keys + ':' + entrys[x][keys] + '\n')
                file2.write('*' * 30 + '\n')
            file2.close()

        remButton = Button(root, text='REMOVE', width=30, command=removeEntry, bg='#3D79C2')
        remButton.config(font=('Courier', 13, 'bold'))
        remButton.place(x=170, y=300)
    elif string == 'Edit an existing entry':
        entryToEdit = StringVar()
        entryLastname = StringVar()
        newContent = StringVar()
        lab = ttk.Label(root, text='Entry Lastname:')
        lab.config(font=('Courier', 13, 'bold'))
        lab.place(x=10, y=140)

        entry = Entry(root, width=30, textvariable=entryLastname)
        entry.place(x=200, y=140)

        lab2 = ttk.Label(root, text='Entry To Edit:')
        lab2.config(font=('Courier', 13, 'bold'))
        lab2.place(x=10, y=180)

        entry2 = Entry(root, width=30, textvariable=entryToEdit)
        entry2.place(x=200, y=180)

        lab3 = ttk.Label(root, text='Make Your Change:')
        lab3.config(font=('Courier', 13, 'bold'))
        lab3.place(x=10, y=220)

        entry3 = Entry(root, width=30, textvariable=newContent)
        entry3.place(x=200, y=220)

        def editData():
            f = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'r')
            line = f.readline()
            entrys = []
            info = {}
            while line:
                cline = line.strip()
                if not '*' in cline and cline != '':
                    info[cline[:cline.index(':')]] = cline[cline.index(':') + 1:]
                else:
                    entrys.append(info)
                    info = {}
                line = f.readline()
            f.close()
            print(entrys)

            for i in range(len(entrys)):
                for key in entrys[i]:
                    if entrys[i][key] == entryLastname.get():
                        entrys[i][entryToEdit.get()] = newContent.get()
                        break

            print(entrys)

            fh = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'w')
            for x in range(len(entrys)):
                for keys in entrys[x]:
                    fh.write(keys + ':' + entrys[x][keys] + '\n')
                fh.write('*' * 30+'\n')
            fh.close()

        editButton = Button(root, text='EDIT', bg='#3D79C2', width=30, command=editData)
        editButton.config(font=('Courier', 13, 'bold'))
        editButton.place(x=170, y=300)
    elif string == 'Search for a specific entry':
        lastName = StringVar()
        entryToFind = StringVar()
        lab = ttk.Label(root,text='Entry Lastname:')
        lab.config(font=('Courier', 13, 'bold'))
        lab.place(x=10,y=140)

        entry = Entry(root,width=30,textvariable=lastName)
        entry.place(x=200,y=140)

        lab1 = ttk.Label(root, text='Entry to Find:')
        lab1.config(font=('Courier', 13, 'bold'))
        lab1.place(x=10, y=180)

        entry2 = Entry(root, width=30,textvariable=entryToFind)
        entry2.place(x=200, y=180)
        def findEntry():
            f = open('C:\\Users\\unss\\Desktop\\adressBook.txt', 'r')
            info = {}
            entrys = []
            line = f.readline()
            while line:
                cline = line.strip()
                if not '*' in cline and cline != '':
                    info[cline[:cline.index(':')]] = cline[cline.index(':')+1:]
                else:
                    entrys.append(info)
                    info = {}
                line = f.readline()
            f.close()

            for i in range(len(entrys)):
                for key in entrys[i]:
                    if entrys[i][key] == lastName.get():
                        print(entrys[i][entryToFind.get()])
                        break

        findButton = Button(root,text='FIND',bg='#3D79C2',width=30,command=findEntry)
        findButton.config(font=('Courier', 13, 'bold'))
        findButton.place(x=200,y=350)
    else:
        root.destroy()

m_lab = Label(root, text='Make a Choose:')
m_lab.config(font=('Courier', 13, 'bold'))
m_lab.place(x=10, y=70)

menu = ttk.Combobox(root, width=50, textvariable=choice)
menu.config(value=('Load from file', 'Save to file', 'Add an entry', 'Remove an entry',
                   'Edit an existing entry', 'Sort the address book', 'Search for a specific entry', 'Quit'))
menu.bind('<<ComboboxSelected>>', lambda _: adressBook(choice.get()))
# menu.current(0)
menu.place(x=200, y=70)

root.mainloop()
