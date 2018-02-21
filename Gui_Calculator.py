from tkinter import *
from functools import partial
# clculator
# https://www.youtube.com/watch?v=_1tTS638xUQ
root = Tk()
root.title('First Program')
frame = Frame(root)
frame.pack(side=TOP)

num_input = Entry(frame,border=10,width=25,insertwidth=1,font=30)
num_input.pack(side=TOP)


def Calculator(num):
    if num == 'CLEAR':
        num_input.delete(0,END)
    else:
        string = num_input.get()
        if num != '=':
            num_input.insert(len(string),num)

        if num == '=':
            num1, index, num2, operator = '', 0, '', ''
            for i in range(len(string)):
                if string[i].isdigit():
                    num1 += string[i]
                else:
                    operator = string[i]
                    index = i
                    break
            num2 = string[index+1:]

            if operator == '+':
                num_input.delete(0,END)
                num_input.insert(0,int(num1)+int(num2))
            elif operator == '-':
                num_input.delete(0,END)
                num_input.insert(0,int(num1)-int(num2))
            elif operator == '*':
                num_input.delete(0,END)
                num_input.insert(0,int(num1)*int(num2))
            elif operator == '%':
                num_input.delete(0,END)
                num_input.insert(0,int(num1)%int(num2))
            else:
                num_input.delete(0,END)
                num_input.insert(0,int(num1)//int(num2))




button = Button(frame,text='0',padx=30,pady=10,bd=6,command=partial(Calculator,0))
button.pack(side=LEFT)

button = Button(frame,text='1',padx=30,pady=10,bd=6,command=partial(Calculator,1))
button.pack(side=LEFT)
button = Button(frame,text='2',padx=30,pady=10,bd=6,command=partial(Calculator,2))
button.pack(side=LEFT)

frame1 = Frame(root,bg='red')
frame1.pack()

button1 = Button(frame1,text='3',padx=30,pady=10,bd=6,command=partial(Calculator,3))
button1.pack(side=LEFT)
button1 = Button(frame1,text='4',padx=30,pady=10,bd=6,command=partial(Calculator,4))
button1.pack(side=LEFT)
button1 = Button(frame1,text='5',padx=30,pady=10,bd=6,command=partial(Calculator,5))
button1.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack()

button2 = Button(frame2,text='6',padx=30,pady=10,bd=6,command=partial(Calculator,6))
button2.pack(side=LEFT)
button2 = Button(frame2,text='7',padx=30,pady=10,bd=6,command=partial(Calculator,7))
button2.pack(side=LEFT)
button2 = Button(frame2,text='8',padx=30,pady=10,bd=6,command=partial(Calculator,8))
button2.pack(side=LEFT)

frame3 = Frame(root)
frame3.pack()

button3 = Button(frame3,text='9',padx=30,pady=10,bd=6,command=partial(Calculator,9))
button3.pack(side=LEFT)
addition_button = Button(frame3,text='+',padx=30,pady=10,bd=6,command=partial(Calculator,'+'))
addition_button.pack(side=LEFT)
subs_button = Button(frame3,text='-',padx=30,pady=10,bd=6,command=partial(Calculator,'-'))
subs_button.pack(side=LEFT)

frame4 = Frame(root)
frame4.pack()

multi_button = Button(frame4,text='*',padx=30,pady=10,bd=6,command=partial(Calculator,'*'))
multi_button.pack(side=LEFT)
divi_button = Button(frame4,text='/',padx=30,pady=10,bd=6,command=partial(Calculator,'/'))
divi_button.pack(side=LEFT)
perc_button = Button(frame4,text='%',padx=30,pady=10,bd=6,command=partial(Calculator,'%'))
perc_button.pack(side=LEFT)

frame5 = Frame(root)
frame5.pack()

resu_button = Button(frame5,text='=',width=10,padx=30,pady=10,bd=6,command=partial(Calculator,'='))
resu_button.pack(side=LEFT)

clear = Button(frame5,text='CLEAR',padx=30,pady=10,bd=6,command=partial(Calculator,'CLEAR'))
clear.pack(side=LEFT)


root.mainloop()

