import tkinter as tk
from tkinter import *
import math 



expression = ''
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
    
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
        
        elif 'cos' in expression:
            expression = expression.replace('cos', '')
            expression = int(expression)
            expression = math.radians(expression)
            res = str(math.cos(expression))
            equation.set(res)
            expression = ''
        
        elif 'tan' in expression:
            expression = expression.replace('tan', '')
            expression = int(expression)
            expression = math.radians(expression)
            res = str(math.tan(expression))
            equation.set(res)
            expression = ''
        
        elif 'eˣ' in expression:
            expression = expression.replace('eˣ', '')
            expression = int(expression)
            res = str(math.exp(expression))
            equation.set(res)
            expression = ''
        
        elif 'log10' in expression:
            expression = expression.replace('log10','')
            expression = int(expression)
            res = str(math.log10(expression))
            equation.set(res)
            expression = ''
        
        elif 'x²' in expression:
            expression = expression.replace('x²', '')
            expression = int(expression)
            res = str(math.pow(expression, 2.0))
            equation.set(res)
            expression = ''
        
        elif 'x³' in expression:
            expression = expression.replace('x³', '')
            expression = int(expression)
            res = str(math.pow(expression, 3.0))
            equation.set(res)
            expression = ''
            
        elif 'sqrt' in expression:
            expression = expression.replace('sqrt', '')
            expression = float(expression)
            res = str(math.sqrt(expression))
            equation.set(res)
            expression = ''
            
        elif 'ln' in expression:
            expression = expression.replace('ln', '')
            k = math.exp(1.0)
            expression = float(expression)
            res = str(math.log(expression, k))
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


        
    
    
root = tk.Tk()
root.configure(bg = 'grey')
root.geometry("300x400")
root.title("Scientific Calculator")
root.resizable(width=False, height=False)
equation = StringVar()

label = tk.Label(root, text = "N and K Sci Calc.", bg='grey', fg='white', font = ('Arial', 18))
label.pack(padx = 10, pady = 10)

entry = tk.Entry(root, width = 30, textvariable=equation)
entry.pack(padx = 10, pady = 10)

bframe = tk.Frame(root, bg = 'grey')
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

buttondeci = tk.Button(bframe, text = '.', width = 6, bg = 'white', fg = 'black', command = lambda: press('.'))
buttondeci.grid(row = 4, column = 0)

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

buttonexponential = tk.Button(specialframe, text = 'eˣ', width = 6, bg = 'white', fg = 'black', command= lambda: press('eˣ'))
buttonexponential.grid(row = 5, column = 0)

buttonlog = tk.Button(specialframe, text = 'log10', width = 6, bg = 'white', fg = 'black', command = lambda: press('log10'))
buttonlog.grid(row = 5, column = 1 )

buttonsquare = tk.Button(specialframe, text = 'x²', width = 6, bg = 'white', fg = 'black', command = lambda: press('x²'))
buttonsquare.grid(row = 5, column = 2)

buttoncube = tk.Button(specialframe, text = 'x³', width = 6, bg = 'white', fg = 'black', command = lambda: press('x³'))
buttoncube.grid(row = 6, column = 0)

buttonsqrt = tk.Button(specialframe, text = 'sqrt', width = 6, bg = 'white', fg = 'black', command = lambda: press('sqrt'))
buttonsqrt.grid(row = 6, column = 1)

buttonln = tk.Button(specialframe, text = 'ln', width = 6, bg = 'white', fg = 'black', command = lambda: press('ln'))
buttonln.grid(row = 6, column = 2)

buttonrightsimplebracket = tk.Button(bframe, text = '(', width = 6, bg = 'white', fg = 'black', command = lambda: press('('))
buttonrightsimplebracket.grid(row = 4, column = 2)

buttonleftsimplebracket = tk.Button(bframe, text = ')', width = 6, bg = 'white', fg = 'black', command = lambda: press(')'))
buttonleftsimplebracket.grid(row = 4, column = 3)




root.mainloop()
