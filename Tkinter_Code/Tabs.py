'''
ttk.Notebook

has a couple of children(which are frames)
each frame is one tab


'''

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Tab widgets')

# Note book
notebook = ttk.Notebook(window)

# tab1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text='button in tab 1')
button1.pack()

# tab2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='text in tab 2')
label2.pack()
button2 = ttk.Button(tab2, text='button in tab 2')
button2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()


# latihan

tab3 = ttk.Frame(notebook)
ttk.Button(tab3, text='Button 1').pack()
ttk.Button(tab3, text='Button 2').pack()
ttk.Label(tab3, text='Label').pack()

notebook.add(tab1, text= 'Tab1')
notebook.add(tab2, text= 'Tab2')
notebook.add(tab3, text='Tab3')
notebook.pack()
# run
window.mainloop()