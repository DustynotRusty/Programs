# A Python program to create 3 push buttons and change the background of
# the frame according to the button clicked by the user
from tkinter import *
class MyButton:
    # constructor
    def __init__(self, root):
        #create a frame as child to root window
        self.f= Frame(root, height=400, width=500)

        # let the frame will not shrink
        self.f.propagate (0)

        #attach the frame to root window
        self.f.pack()

        # create 3 push buttons and bind them to buttonclick method and pass a number
        self.b1 = Button(self.f, text='Red', width=15, height=2, command=lambda: self.buttonClick(1))
        self.b2 = Button(self.f, text='Green', width=15, height=2, command=lambda: self.buttonClick(2))
        self.b3 = Button(self.f, text='Blue', width=15, height=2, command=lambda: self.buttonClick(3))

        #attach buttons to the frame
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()

    #method to be called when the button is clicked
    def buttonClick(self, num):
        # set the background color of frame depending on the button
        # clicked
        if num==1:
            self.f["bg"]= 'red'
        if num==2:
            self.f["bg"]= 'green'
        if num==3:
            self.f["bg"]= 'blue'

# create root window
root = Tk()

#create an object to MyButton class
mb = MyButton(root)

#the root window handles the mouse click event
root.mainloop()
