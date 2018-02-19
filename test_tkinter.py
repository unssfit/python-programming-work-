from tkinter import *

screen = Tk()
# label = Label(screen,text='Python Gui Programming')
# label.pack()
# topFrame = Frame(screen)
# topFrame.pack()
#
# botomFrame = Frame(screen)
# botomFrame.pack(side=BOTTOM)
#
#
# bot1 = Button(topFrame,text='Click Here',bg='red')
# bot2 = Button(topFrame,text='Press Here',fg='blue')
# bot3 = Button(botomFrame,text='Bot3',fg='black',bg='green')
# bot4 = Button(botomFrame,text='Bot4',fg='yellow')
#
# bot1.pack(side=LEFT)
# bot2.pack(side=RIGHT)
# bot3.pack(side=LEFT)
# bot4.pack(side=RIGHT)
#
#
# # shrink labal size
# lb1 = Label(screen,text='chekc text',fg='pink',bg='pink')
# lb1.pack(fill=X)
# lb2 = Label(screen,text='label 2',bg='blue')
# lb2.pack(side=LEFT,fill=Y)


#work with grid layout
# lab1 = Label(screen,text='Name:')
# lab2 = Label(screen,text='Password:')
#
# lab1.grid(row=0,sticky=E)
# lab2.grid(row=1,sticky=E)
#
# user = Entry(screen)
# passwrd = Entry(screen)
#
# user.grid(row=0,column=1)
# passwrd.grid(row=1,column=1)
#
# ckeck = Checkbutton(screen,text='Keep me loged in')
# ckeck.grid(columnspan=2)

# work with (binding function)
def doSomething():
    print('hello GUI im youness')


def printSometing(event):
    print('heelo there are you ok')
    label = Label(screen,text="test Functionalety")
    label.pack()




button = Button(screen,text='youness',command=doSomething)
button.pack()


button2 = Button(screen,text='press')
button2.bind("<Button-1>",printSometing)
button2.pack()






screen.mainloop()




