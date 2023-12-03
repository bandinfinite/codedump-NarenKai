import tkinter as tk
from tkinter import *
import math 



expression = ''
def press(num):
    global expression
    expression += str(num)
    equation.set(num)
    
def result():
    try:
        global expression
        if 'sin' in expression:
            expression = expression.replace('sin', '')
            expression = int(expression)
            expression = math.radians(expression)
            res = str(math.sin(expression))
            equation.set(res)
            expression = ''
        
        else:
            
            res = str(eval(expression))
            
            equation.set(res)
            
            expression = ''
        
    except:
        
        equation.set("Error.")
        expression = ''
        
    
def delete():
    global expression
    expression = ''
    equation.set('')


        
    
    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Scientific Calculator")
    root.resizable(width=False, height=False)
    equation = StringVar()

    label = tk.Label(root, text = "CASIO", bg='black', fg='white', font = ('Courier Sans', 18))
    label.pack(padx = 10, pady = 10)

    entry = tk.Entry(root, width = 30, textvariable=equation)
    entry.pack(padx = 10, pady = 10)
   
    bframe = tk.Frame(root)
    bframe.pack(padx = 10, pady = 10)

    specialframe = tk.Frame(root)
    specialframe.pack(padx = 10, pady = 10)

    button = tk.Button(bframe, text = '9', width = 6, bg='white', fg = 'black', command = lambda: press(9))
    button.grid(row= 0, column = 0)

    button1 = tk.Button(bframe, text = '8', width = 6, bg='white', fg = 'black', command = lambda: press(8))
    button1.grid(row= 0, column = 1)

    button2 = tk.Button(bframe, text = '7', width = 6, bg='white', fg = 'black', command = lambda: press(7))
    button2.grid(row= 0, column = 2)

    button3 = tk.Button(bframe, text = '6', width = 6, bg='white', fg = 'black', command = lambda: press(6))
    button3.grid(row= 1, column = 0)

    button4 = tk.Button(bframe, text = '5', width = 6, bg='white', fg = 'black', command = lambda: press(5))
    button4.grid(row= 1, column = 1)

    button5 = tk.Button(bframe, text = '4', width = 6, bg='white', fg = 'black', command = lambda: press(4))
    button5.grid(row= 1, column = 2)

    button6 = tk.Button(bframe, text = '3', width = 6, bg='white', fg = 'black', command = lambda: press(3))
    button6.grid(row= 2, column = 0)

    button7 = tk.Button(bframe, text = '2', width = 6, bg='white', fg = 'black', command = lambda: press(2))
    button7.grid(row= 2, column = 1)

    button8 = tk.Button(bframe, text = '1', width = 6, bg='white', fg = 'black', command = lambda: press(1))
    button8.grid(row= 2, column = 2)

    button9 = tk.Button(bframe, text = '0', width = 6, bg='white', fg = 'black', command = lambda:press(0))
    button9.grid(row= 3, column = 0)

    buttonplus = tk.Button(bframe, text = '+', width = 8, bg = 'white', fg = 'black', command = lambda: press('+'))
    buttonplus.grid(row = 0, column = 3)

    buttonminus = tk.Button(bframe, text = '-', width = 8, bg = 'white', fg = 'black', command = lambda: press('-'))
    buttonminus.grid(row = 1, column = 3)

    buttonprod = tk.Button(bframe, text = 'x', width = 8, bg = 'white', fg = 'black', command = lambda: press('*') )
    buttonprod.grid(row = 2, column = 3)

    buttondiv = tk.Button(bframe, text = '/', width = 8, bg = 'white', fg = 'black', command = lambda: press('/'))
    buttondiv.grid(row = 3, column = 3)

    buttonequals = tk.Button(bframe, text = '=', width = 6, bg = 'white', fg = 'black', command = result)
    buttonequals.grid(row = 3, column = 1)

    buttonclear = tk.Button(bframe, text = 'C', width = 6, bg = 'white', fg = 'black', command = delete)
    buttonclear.grid(row = 3, column = 2)

    buttonsin = tk.Button(specialframe, text = 'sin', width = 6, bg = 'white', fg = 'black', command = lambda: press('sin'))
    buttonsin.grid(row = 4, column = 0)

    buttoncos = tk.Button(specialframe, text = 'cos', width = 6, bg = 'white', fg = 'black', command = lambda: press('cos'))
    buttoncos.grid(row = 4, column = 1)

    buttontan = tk.Button(specialframe, text = 'tan', width = 6, bg = 'white', fg = 'black', command = lambda: press('tan'))
    buttontan.grid(row = 4, column = 2)


root.mainloop()