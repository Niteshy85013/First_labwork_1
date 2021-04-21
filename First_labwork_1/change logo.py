'''from tkinter import*
root=Tk()
root.title('image insertion')
root.iconbitmap('male.ico')
root.mainloop()'''

from tkinter import*
from PIL import ImageTk, Image
root=Tk()
root.title('Image Insertion')
root.iconbitmap('male.ico')

my_image= ImageTk.PhotoImage (Image .open('female.png') )
my_label=Label(image=my_image)
my_label.pack()


Button_quite=Button(root,text="exit",command=root.quit,width=20)
Button_quite.pack()
root.mainloop()


