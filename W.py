import tkinter as tk

inside_entry = ''

def onpress():
    global inside_entry
    inside_entry = inside_entry + text_get.get()


def guesser(Guess):
    global inside_entry
    inside_entry = int(inside_entry)
    if inside_entry >= 0 and inside_entry <= 10:
        text_get.display('Hi')
        
    

main_window = tk.Tk()
main_window.title("Future Guesser!")
main_window.geometry("400x450")
label = tk.Label(main_window, text = "98% accurate predictor!", font = ('Arial', 18), bg = 'white', fg = 'blue')
label.pack(padx = 10, pady = 10)

main_frame = tk.Frame(main_window)
main_frame.pack(padx = 10, pady = 10)

text_get = tk.Entry(main_frame, width = 10)
text_get.grid(row = 3, column = 0)

button_guess = tk.Button(main_frame, height = 3, width = 15, text = 'Check for fortune!', font = ('Courier Sans', 10), bg = 'white', fg = 'black', command = onpress)
button_guess.grid(row = 7, column = 0)

mainframe_label = tk.Label(main_frame, text = 'Enter your lucky number!' , font = ('Arial', 14), bg = 'white' , fg = 'black')
mainframe_label.grid(row = 1, column = 0)
