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
