from tkinter import *
from tracemalloc import start
from turtle import width
root = Tk()
c = Canvas(root, bg='yellow', height=700, width=1200)
id = c.create_arc(100, 100, 400, 400, width=2, start=0,
                  extent=359.9, outline='red', style='arc')
id = c.create_arc(150, 150, 350, 350, width=2, start=200,
                  extent=140, outline='red', style='arc')
id = c.create_arc(190, 190, 230, 230, width=2, start=200,
                  extent=140, outline='red', style='arc')
file1 = PhotoImage(file='Python Class\cat.gif')
file2 = PhotoImage(file='Python Class\puppy.gif')
id = c.create_image(500, 200, anchor=NE, image=file1, activeimage=file2)

c.pack()
root.mainloop()
