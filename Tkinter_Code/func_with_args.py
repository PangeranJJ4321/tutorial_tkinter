# Functions with arguments(inside a button)
# we already solved this!
# command = lambda: print('argument')

import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('a button was pressed')
    print(entry_string.get())

# ini akan sama dengan func di bawah ini
def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(entry_string.get())
    return inner_func


# setup
window = tk.Tk()
window.title('buttons, functions and arguments')

# widget
entry_string = tk.StringVar(value= 'test')
entry = ttk.Entry(
    window,
    textvariable= entry_string)
entry.pack()

button = ttk.Button(
    window,
    text= 'button', 
    command= lambda: button_func(entry_string)
    # command= outer_func(entry_string)
    )
button.pack()
# run
window.mainloop()