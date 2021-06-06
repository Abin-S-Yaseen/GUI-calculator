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