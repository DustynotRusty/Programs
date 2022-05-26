from tkinter import *


def buttonClick(self):
    print('You have summoned me!!!')


root = Tk()
root.title("My Frame")
f = Frame(root, height=400, width=500, bg='yellow', cursor='cross')
f.propagate(0)
f.pack()
b = Button(f, text='My Button', width=15, height=2, bg='red',
           fg='blue', activebackground='green', activeforeground='red')
b.pack()
b.bind('<Button-3>', buttonClick)
root.mainloop()
