from tkinter import *
from tkinter import font
root = Tk()
root.title("My Main Window")
root.geometry("1000x400+100+100")
root.configure(bg='white')
c = Canvas(root, bg='grey', height=500, width=600, cursor='pencil')
id = c.create_oval(100, 500, 101, 300, width=1, fill='cyan')
c.pack()
root.wm_iconbitmap("Python Class\ACBF_PC.ico")
root.mainloop()
