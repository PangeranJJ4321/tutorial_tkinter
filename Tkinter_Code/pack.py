'''
side ='left', 'right', 'top', 'bottom'
The side will be the location of the widget
Determines the direction of the widget

expand=True, fill='both', padx=10, pady=10

Determine the vertical and horizontal spacing of the widget can accupy

fill='x' or 'y'

Sets how much space the widget can take up on the x or y axis


'''

import tkinter as tk
import ttkbootstrap as ttk


# window
window = ttk.Window(themename='darkly')
window.geometry('600x400')
window.title('Pack')

# widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Last of the label', background='green')
button = ttk.Button(window, text='button')

# Layout
# label1.pack(side='top', expand=True,fill='both')
# label2.pack(side='top', fill='y')
# label3.pack(side='top')
# button.pack(side='top',expand=True, fill='y')

# example

label1.pack(side='top', fill='x', padx=10, pady=10)
label2.pack(side='top', expand=True, padx=10, pady=10)
label3.pack(side='top',expand=True, fill='both', padx=10, pady=10)
button.pack(side='top', fill='x', padx=10, pady=10)

# run
window.mainloop()