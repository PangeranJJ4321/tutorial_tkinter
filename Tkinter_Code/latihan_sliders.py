import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
root = tk.Tk()
root.title('Sliders')
# root.geometry('400x300')


# slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    root, 
    from_ = 0, 
    to = 25, 
    length=300,
    command= lambda value: progress.stop(),
    orient= 'vertical',
    variable=scale_float)
scale.pack()



# progress bar
progress = ttk.Progressbar(
    root, 
    variable= scale_float,
    maximum=25,
    orient='horizontal',
    mode='indeterminate',
    length=400)
progress.pack()

# progress.start() 

# Scrolledtext

scrolled_text = scrolledtext.ScrolledText(root)
scrolled_text.pack()
# run
root.mainloop()