import tkinter as tk
import math 

root = tk.Tk()
root.geometry("300x400")
root.title("Scientific Calculator")

label = tk.Label(root, text = "CASIO", bg='black', fg='white', font = ('Courier Sans', 18))
label.pack(padx = 10, pady = 10)

entry = tk.Entry(root, width = 30)
entry.pack(padx = 10, pady = 10)


bframe = tk.Frame(root)
bframe.pack(padx = 10, pady = 10)
button = tk.Button(bframe, text = '9', width = 10, bg='white', fg = 'black')
button.grid(row= 0, column = 0)

root.mainloop()