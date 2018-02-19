from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x400')
label1 = ttk.Label(root,text='Join BettingExpert',foreground='blue')
label1.config(font = ('Courier',20,'bold'))
label1.place(x=50,y=10)

username = StringVar()
email = StringVar()
password = StringVar()
checkb = BooleanVar()

userlab = ttk.Label(root,text='Username:')
userlab.config(font = ('Courier',15,'bold'))
userlab.place(x=50,y=70)

entry1 = Entry(root,width=50,border=3,textvariable=username)
entry1.place(x=50,y=92)

emailLab = ttk.Label(root,text='Email:')
emailLab.config(font = ('Courier',15,'bold'))
emailLab.place(x=50,y=150)


emailEntry = Entry(root,width=50,border=3,textvariable=email)
emailEntry.place(x=50,y=175)


passlab = ttk.Label(root,text='Password:')
passlab.config(font = ('Courier',15,'bold'))
passlab.place(x=50,y=230)

passEntry = Entry(root,width=50,border=3,textvariable=password)
passEntry.place(x=50,y=255)

checkbx = ttk.Checkbutton(root,text='I accept the Terms and Conditions')
checkbx.config(variable=checkb)
checkbx.place(x=50,y=290)


def showResult():
    window = Toplevel(root)
    if not username.get():
        ulab = ttk.Label(window,text='Username Required!')
        ulab.pack()
    if not email.get():
        elab = ttk.Label(window,text='Email Required!')
        elab.pack()
    if not password.get():
        plab = ttk.Label(window,text='Password Required!')
        plab.pack()

    if checkb.get():
        #window = Toplevel(root)
        lab1 = ttk.Label(window, text=username.get())
        lab1.config(font = ('Courier',15,'bold'),foreground='blue')
        lab1.pack()
        lab2 = ttk.Label(window, text=email.get())
        lab2.config(font=('Courier', 15, 'bold'), foreground='blue')
        lab2.pack()
        lab3 = ttk.Label(window, text=password.get())
        lab3.config(font=('Courier', 15, 'bold'), foreground='blue')
        lab3.pack()
    else:
        #window = Toplevel(root)
        lab = ttk.Label(window, text='Please Accept Terms and Conditions.')
        lab.config(font = ('Courier',15,'bold'),justify=CENTER,foreground='red')
        lab.pack()
        #signButton.config(state='disabled')


signButton = Button(root, text='Sign up+', width=21, border=4, relief=GROOVE, command=showResult)
signButton.config(fg='white',bg='green',font = ('Courier',15,'bold'),padx=20)
signButton.place(x=50,y=340)





root.mainloop()


