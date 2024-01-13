from tkinter import *
 
root = Tk()
'''Author of this .py file is creating his own OS'''

root.title('Welcome!')
root.geometry('600x600')

label = Label(root, text = 'Welcome!\nThis is just a testing OS for purpose', font = ("Arial", 18))
label.pack()

root.mainloop()