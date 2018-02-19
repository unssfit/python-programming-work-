from tkinter import *
from tkinter import ttk
# def callButton():
#     print('Clicked!')
#
root = Tk()
button = ttk.Button(root,text='click here')
button.pack()
#
# button.config(command=callButton)
# button.invoke()
#
# button.state(['disabled'])
# check = button.instate(['disabled'])
# print(check)
#
# button.state(['!disabled'])
# print(button.instate(['!disabled']))

# logo = PhotoImage(file='C:\\Users\\unss\\Desktop\\images.jpg')
# # button.config(image=logo,compound=LEFT)
# small_logo = logo.subsample(5,5)
# button.config(image=small_logo)

# working with labels
label = ttk.Label(root,text='hello there')
label.pack()

label.config(text = 'hello again youness are you ok it have been a while since we meet')
label.config(wraplength=100)
label.config(justify=CENTER)
label.config(font = ('Courier',20,'bold'))
label.config(foreground='green',background='yellow')
logo = PhotoImage(file='C:\\Users\\unss\\Desktop\\imagesd.gif')
label.config(image=logo)
label.config(compound='text')
label.config(compound='center')
label.config(compound='left')
# small_logo = logo.subsample(5,5)
# label.config(image=small_logo)

button = ttk.Button(root,text='click here')
button.pack()










root.mainloop()






