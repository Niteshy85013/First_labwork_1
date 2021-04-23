from tkinter import*
root=Tk()


#difining title  of  the  project
root.title(" PY. Calculator" )

#inserting the  icon
root.iconbitmap('cal.ico')


e = Entry(root,width=55,borderwidth=15,bg="sky blue")
e.grid(row=0,column=0 ,columnspan=6,padx=13,pady=19)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math="add"
    f_num=int(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num+int(second_number))
    if math=="subtract":
        e.insert(0, f_num - int(second_number))
    if math=="multiply":
        e.insert(0, f_num * int(second_number))
    if math=="division":
        e.insert(0, f_num // int(second_number))

def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math="subtract"
    f_num=int(first_number)
    e.delete(0,END)


def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiply"
    f_num=int(first_number)
    e.delete(0,END)



def button_division():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)


#defining  the buttons

button_1=Button(root,text="1", bg="gray", padx=35, pady=15, command=lambda:button_click(1))
button_2=Button(root,text="2", bg="gray", padx=35, pady=15, command=lambda:button_click(2))
button_3=Button(root,text="3",  bg="gray", padx=35, pady=15, command=lambda:button_click(3))
button_4=Button(root,text="4",  bg="gray", padx=35, pady=15, command=lambda:button_click(4))
button_5=Button(root,text="5",  bg="gray", padx=35, pady=15, command=lambda:button_click(5))
button_6=Button(root,text="6",   bg="gray",padx=35, pady=15, command=lambda:button_click(6))
button_7=Button(root,text="7",   bg="gray",padx=35, pady=15, command=lambda:button_click(7))
button_8=Button(root,text="8",  bg="gray", padx=35, pady=15, command=lambda:button_click(8))
button_9=Button(root,text="9",  bg="gray",  padx=35, pady=15, command=lambda:button_click(9))
button_0=Button(root,text="0",  bg="gray",    padx=35, pady=15, command=lambda:button_click(0))



button_equal=Button(root,text="=", bg="gray",padx=35,pady=15,command=button_equal)
button_add=Button(root,text="+" ,bg="gray",padx=35, pady=15,command=button_add)
button_clear=Button(root,text="clear", bg="red",padx=35, pady= 15,command=button_clear)
button_subtract=Button(root,text="-",bg="gray",padx=35, pady=15 ,command=button_subtract)
button_multiply=Button(root,text="*",bg="gray",padx=35,pady=15 ,command=button_multiply)
button_division=Button(root,text="/",bg="gray",padx=35,pady=15 ,command=button_division)



#putting buttons on the screen

button_1.grid(row=3,    column=0)
button_2.grid(row=3,    column=1)
button_3.grid(row=3,    column=2)

button_4.grid(row=2,    column=0)
button_5.grid(row=2,    column=1)
button_6.grid(row=2,    column=2)

button_7.grid(row=1,    column=0)
button_8.grid(row=1,    column=1)
button_9.grid(row=1,    column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=1, column=3, columnspan=1)
button_add.grid(row=2, column=3)
button_equal.grid(row=4, column=3, columnspan=1)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=4,column=2)
button_division.grid(row=4,column=0)



root.mainloop()
