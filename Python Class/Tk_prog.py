from tkinter import *
from tkinter import font
from venv import create
root = Tk()
root.title("My Main Window")
root.geometry("1100x500+100+100")
root.configure(bg='white')
c = Canvas(root, bg='grey', height=500, width=600, cursor='plus')
id = c.create_line(50, 50, 200, 50, 200, 150, width=10, fill='white')
id = c.create_oval(100, 100, 600, 300, width=1, fill='cyan')
id = c.create_polygon(10, 10, 100, 200, 200, 300, fill='green',
                      outline='red', smooth=0, activefill='lightblue')  # smooth0:sharp edges,1:smooth edges
id = c.create_rectangle(500, 200, 600, 500, width=2,
                        fill='grey', outline='black', activefill='magenta')
fnt = ('Times', 40, 'bold italic underline')
id = c.create_text(300, 100, text='My Canvas', font=fnt,
                   fill='yellow', activefill='lightgreen')
c.pack()
root.wm_iconbitmap("Python Class\ACBF_PC.ico")
root.mainloop()
# DIfferent Styles of arc:
# Pie Slice, chord, arc.
