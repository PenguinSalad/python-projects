from tkinter import *
import math

#Init####################################
root = Tk()
root.title("Simple Calculator")
root.iconbitmap("./calcIcon.ico")
#########################################

#Entry text box##########################
e = Entry(root, width=50, borderwidth=5, justify=RIGHT)
e.grid(row=0, column=0, columnspan=5)
#########################################


#Button functions definition#############
def button_click(number):
    if (e.get() == '0'): #Delete leftside zeros (01234 --> 1234)
        e.delete(0,END)

    e.insert(END, number)

def button_clear():
    e.delete(0,END)
     
def button_add():
    global first_num
    global operation
    first_num = float(e.get())
    e.delete(0,END)
    operation = "ADD"
    
def button_substract():
    global first_num
    global operation
    first_num = float(e.get())
    e.delete(0,END)    
    operation = "SUBSTRACT"

def button_multiply():
    global first_num
    global operation
    first_num = float(e.get())
    e.delete(0,END)    
    operation = "MULTIPLY"

def button_divide():
    global first_num
    global operation
    first_num = float(e.get())
    e.delete(0,END)
    operation = "DIVIDE"

def button_changeSign():
    number = float(e.get())
    number = -number
    e.delete(0,END)
    e.insert(0, "{0:g}".format(number))

def button_erease():
    number = e.get()
    e.delete(0, END)
    e.insert(0, number[:-1])

def button_squared():
    number = float(e.get())
    e.delete(0,END)
    e.insert(0, "{0:g}".format(number ** 2))

def button_squareRoot():
    number = float(e.get())
    e.delete(0,END)
    e.insert(0, "{0:g}".format(math.sqrt(number)))

def button_equal():
    second_num = float(e.get())
    e.delete(0, END)
    if operation == "ADD":
        result = first_num + second_num
        e.insert(0, "{0:g}".format(result))
        
    elif operation == "SUBSTRACT":
        result = first_num - second_num
        e.insert(0, "{0:g}".format(result))

    elif operation == "MULTIPLY":
        result = first_num * second_num
        e.insert(0, "{0:g}".format(result))

    elif operation == "DIVIDE":
        result = first_num / second_num
        e.insert(0, "{0:g}".format(result))

#########################################
    


#Define buttons##########################

button_1 = Button(root, text="1", width=10, height=5, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=10, height=5, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=10, height=5, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=10, height=5, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=10, height=5, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=10, height=5, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=10, height=5, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=10, height=5, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=10, height=5, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=10, height=5, command=lambda: button_click(0))

button_add = Button(root, text="+", width=10, height=5, command= button_add)
button_equal = Button(root, text="=", width=10, height=5, command= button_equal)
button_clear = Button(root, text="Clear", width=10, height=5, command= button_clear)

button_substract = Button(root, text="-", width=10, height=5, command= button_substract)
button_multiply = Button(root, text="x", width=10, height=5, command= button_multiply)
button_divide = Button(root, text="÷", width=10, height=5, command= button_divide)

button_changeSign = Button(root, text="+/-", width=10, height=5, command= button_changeSign)
button_fraction = Button(root, text="⌫", width=10, height=5, command= button_erease)
button_squared = Button(root, text="x²", width=10, height=5, command= button_squared)
button_squareRoot = Button(root, text="√", width=10, height=5, command= button_squareRoot)

#########################################


#Print buttons###########################

button_fraction.grid(row=1, column=0)
button_squared.grid(row=1, column=1)
button_squareRoot.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_substract.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_changeSign.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_clear.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

#########################################


#Run#####################################
root.mainloop()
#########################################
