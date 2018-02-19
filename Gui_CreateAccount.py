from tkinter import *
from tkinter import ttk
from functools import partial

root = Tk()
root.geometry('600x400')

ca_lab = Label(root,text='Create Account\t\t                Student Base',width=42)
ca_lab.config(font = ('Times',15,'bold'),background='#3D79C2',relief='raised',height=2)
ca_lab.config(foreground='white')
ca_lab.place(x=50,y=30)

frame = Frame(root,width=510,height=270,bg='#B9CEE0')
frame.config(highlightbackground="#3D79C2", highlightcolor="#3D79C2",highlightthickness=6)
frame.place(x=50,y=100)

frame1 = Frame(frame,width=455,height=220)
frame1.place(x=20,y=20)

ulab = ttk.Label(frame1,text='Enter username:')
ulab.config(font = ('Courier',13,'bold'))
ulab.place(x=20,y=20)

uentry = ttk.Entry(frame1,width=33,font = ('Courier',8,'bold'))
uentry.insert(0,'Enter Your Username')
uentry.place(x=175,y=25)

plab = ttk.Label(frame1,text='Enter password:')
plab.config(font = ('Courier',13,'bold'))
plab.place(x=20,y=60)

pentry = ttk.Entry(frame1,width=33,font = ('Courier',8,'bold'))
pentry.config(show='*')
pentry.place(x=175,y=65)

def showResult(string):
    window = Toplevel(root)
    window.geometry('600x400')
    s = ttk.Style()
    s.configure('TLabel', foreground='red')
    username_check = False
    password_check = False

    if string == 'Cancel':
        root.destroy()
    else:
        if not (uentry.get() != 'Enter Your Username') or not (uentry.get() != ''):
            lab = ttk.Label(window, text='Username Required!',style='TLabel')
            lab.config(font=('Courier', 20, 'bold'))
            lab.pack()
        else:
            username_check = True

        if pentry.get() == '':
            plab = ttk.Label(window,text='Password Required!',style='TLabel')
            plab.config(font=('Courier', 20, 'bold'))
            plab.pack()
        else:
            password_check = True

        if (username_check and password_check) and string == 'Create':
            crs_lab = ttk.Label(window,text='Your Registration Complete\nWelcom '+uentry.get())
            crs_lab.config(font = ('Courier', 20, 'bold'))
            crs_lab.pack()
        else:
            if username_check and password_check and string == 'Save':
                lab = ttk.Label(window, text='Your Information Saved!')
                lab.config(font=('Courier', 20, 'bold'))
                lab.pack()


cr_button = Button(frame1,text='Create',relief=GROOVE,bg='#3D79C2',fg='white',command=partial(showResult,'Create'))
cr_button.config(font = ('Courier',15,'bold'),width=9)
cr_button.place(x=20,y=165)

s_button = Button(frame1,text='Save',relief=GROOVE,bg='#3D79C2',fg='white',command=partial(showResult,'Save'))
s_button.config(font = ('Courier',15,'bold'),width=9)
s_button.place(x=165,y=165)

c_button = Button(frame1,text='Cancel',relief=GROOVE,bg='#3D79C2',fg='white',command=partial(showResult,'Cancel'))
c_button.config(font = ('Courier',15,'bold'),width=9)
c_button.place(x=310,y=165)


root.mainloop()


