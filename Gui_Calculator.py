from tkinter import *
# clculator
# https://www.youtube.com/watch?v=_1tTS638xUQ
num = 0

def buttonClick():
    print(self.fnameEntry.get())

root = Tk()
root.title('First Program')
#root.geometry('400x400')
frame = Frame(root)
frame.pack(side=TOP)

num_input = Entry(frame,border=10,width=25,insertwidth=1,font=30)
num_input.pack(side=TOP)



button = Button(frame,text='0',padx=30,pady=10,bd=6,command=buttonClick)

#button.bind('<Button-1>',result)
button.pack(side=LEFT)
#print(num)
button = Button(frame,text='1',padx=30,pady=10,bd=6)
button.pack(side=LEFT)
button = Button(frame,text='2',padx=30,pady=10,bd=6)
button.pack(side=LEFT)

frame1 = Frame(root,bg='red')
frame1.pack()

button1 = Button(frame1,text='3',padx=30,pady=10,bd=6)
button1.pack(side=LEFT)
button1 = Button(frame1,text='4',padx=30,pady=10,bd=6)
button1.pack(side=LEFT)
button1 = Button(frame1,text='5',padx=30,pady=10,bd=6)
button1.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack()

button2 = Button(frame2,text='6',padx=30,pady=10,bd=6)
button2.pack(side=LEFT)
button2 = Button(frame2,text='7',padx=30,pady=10,bd=6)
button2.pack(side=LEFT)
button2 = Button(frame2,text='8',padx=30,pady=10,bd=6)
button2.pack(side=LEFT)

frame3 = Frame(root)
frame3.pack()

button3 = Button(frame3,text='9',padx=30,pady=10,bd=6)
button3.pack(side=LEFT)
addition_button = Button(frame3,text='+',padx=30,pady=10,bd=6)
addition_button.pack(side=LEFT)
subs_button = Button(frame3,text='-',padx=30,pady=10,bd=6)
subs_button.pack(side=LEFT)

frame4 = Frame(root)
frame4.pack()

multi_button = Button(frame4,text='*',padx=30,pady=10,bd=6)
multi_button.pack(side=LEFT)
divi_button = Button(frame4,text='/',padx=30,pady=10,bd=6)
divi_button.pack(side=LEFT)
perc_button = Button(frame4,text='%',padx=30,pady=10,bd=6)
perc_button.pack(side=LEFT)

# implimenting logic code











root.mainloop()

