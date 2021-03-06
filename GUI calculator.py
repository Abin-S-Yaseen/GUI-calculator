from tkinter import *

root = Tk()
root.title('GUI Calculator')

check_box = Entry(root,width=47,borderwidth=5)
check_box.grid(row=0,column=0,columnspan=4,pady=10)

def button_click(number):
    current = check_box.get()
    check_box.delete(0,END)
    check_box.insert(0,str(current) + str(number))

def button_add():
    first_number = check_box.get()
    if len(check_box.get()) == 0:
        first_number = 0
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    check_box.delete(0,END)

def button_subtract():
    first_number = check_box.get()
    if len(check_box.get()) == 0:
        first_number = 0
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)  
    check_box.delete(0,END)

def button_multiply():
    first_number = check_box.get()
    if len(check_box.get()) == 0:
        first_number = 0
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    check_box.delete(0,END)

def button_divide():
    first_number = check_box.get()
    if len(check_box.get()) == 0:
        first_number = 0
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    check_box.delete(0,END)

def button_equals():
    second_number = check_box.get()
    check_box.delete(0,END)

    if math == 'addition':
        check_box.insert(0,f_num + int(second_number))
    if math == 'subtraction':
        check_box.insert(0,f_num - int(second_number))
    if math == 'multiplication':
        check_box.insert(0,f_num * int(second_number))
    if math == 'division':
        check_box.insert(0,f_num / int(second_number))


def button_clear():
    check_box.delete(0,END)

button_1 = Button(root,text='1',padx=30,pady=10,command=lambda: button_click(1))
button_2 = Button(root,text='2',padx=30,pady=10,command=lambda: button_click(2))
button_3 = Button(root,text='3',padx=30,pady=10,command=lambda: button_click(3))
button_4 = Button(root,text='4',padx=30,pady=10,command=lambda: button_click(4))
button_5 = Button(root,text='5',padx=30,pady=10,command=lambda: button_click(5))
button_6 = Button(root,text='6',padx=30,pady=10,command=lambda: button_click(6))
button_7 = Button(root,text='7',padx=30,pady=10,command=lambda: button_click(7))
button_8 = Button(root,text='8',padx=30,pady=10,command=lambda: button_click(8))
button_9 = Button(root,text='9',padx=30,pady=10,command=lambda: button_click(9))
button_0 = Button(root,text='0',padx=30,pady=10,command=lambda: button_click(0))
button_clr = Button(root,text='clr',padx=27,pady=10,command=button_clear)
button_equals = Button(root,text='=',padx=29,pady=10,command=button_equals)
button_add = Button(root,text='+',padx=29,pady=10,command=button_add)
button_subtract = Button(root,text='-',padx=30,pady=10,command=button_subtract)
button_multiply = Button(root,text='*',padx=30,pady=10,command=button_multiply)
button_divide = Button(root,text='/',padx=30,pady=10,command=button_divide)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clr.grid(row=4,column=1)
button_equals.grid(row=4,column=2)

button_add.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)

root.mainloop()