# A Python program to creat a Text widget with vertical scroll bar attached to it.
# Also, highlight the first line of the text and display an image in the Text widget.

from tkinter import *


class MyText:
    # constructor
    def __init__(self, root):
        # create a text widget with 20 chars width and 10 lines height
        self.t = Text(root, width=20, height=10, font=(
            'Verdana', 14, 'bold'), fg='blue', bg='yellow', wrap=NONE)

        # insert some text into the Text widget
        self.t.insert(
            END, 'Text widget\nThis text is inserted into the Text widget.\nThis is second line\nand this is third line\n')

        # attach Text to the root
        self.t.pack()

        # show image in the Text_widget
        self.img = PhotoImage(file='Python Class\cat.gif')
        self.t.image_create(END, image=self.img)

        # create a tag with the name 'start'
        self.t.tag_add('start', '1.0', '1.11')

        # apply colors to the tag
        self.t.tag_config('start', background='red', foreground='white', font=(
            'Segoe Script', 20, 'bold'))

        # create a Scrollbar widget to move the text vertically
        self.s = Scrollbar(root, orient=HORIZONTAL, command=self.t.xview)

        # attach the scroll bar to the Text widget
        self.t.configure(xscrollcommand=self.s.set)

        # attach the scroll bar to the root window
        self.s.pack(side=BOTTOM, fill=X)


# create root window
root = Tk()

# create an object to MyText class
mt = MyText(root)

# the root window handles the mouse click event
root.mainloop()
