from tkinter import *


class MyButton:
    def __init__(self, root):
        self.f = Frame(root, height=200, width=300)
        self.f.propagate(0)
        self.f.pack()
        self.b = Button(self.f, text='My Button', width=15, height=2, bg='yellow',
                        fg='blue', activebackground='red', command=self.buttonClick)
        self.b.pack()

    def buttonClick(self):
        print('Thy have summoned me!!!! ')


root = Tk()
root.title('My Main Window')
mb = MyButton(root)
root.mainloop()
