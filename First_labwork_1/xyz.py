'''def sum(a,b=2):
    return a+b
d=int(input("enter the first number:"))
e=int(input("enter the second number:"))
print(sum(d,e))'''

'''def sum(*Nitesh):
    print(Nitesh)
sum(1,2)
sum(1,2,3,4,5,6,7,8,9)'''


'''def sum(**Kwargs):
    print(Kwargs)
    sum=0
    for i in Kwargs.values():
        sum=sum+i
        return sum

    print(sum(a=2,b=3,c=4)'''




from tkinter import*
root=Tk()
root.title("call")
Frame=LabelFrame(root,pdx=40,pdy=40)
Frame.pack(pdx=10,pdy=10)

button1=Button(Frame,text="click this")
button1.grid(row=0,column=0)
button2=Button(Frame,text="Do not click")
button2.grid(row=1,column=1)

#creating modes for radio button
MODES=[
    {"pepperoni","pepperoni"},
    {"cheese","cheese"},
    {"mushroom","mushroom"},
    {"onion","onion"}
]
pizza=StringVar()
pizza.set={"pepperoni"}

for text,mode in MODES:
    Radiobutton(root,text="text",variable=pizza,value=mode).pack()

#function clicked
def clicked(value):
    mylabel=Label(root,text=value)
    mylabel.pack()

MyButton=Button(root,text="click",command=lambda :clicked(pizza))

root.mainloop()
