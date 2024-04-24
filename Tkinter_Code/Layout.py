'''
pack

grid

place

you will rely heavily on parenting and frames!
Rhatt way you can combine diferent layout easily and keep the organized
'''
import tkinter as tk
import ttkbootstrap as ttk


# window
window = ttk.Window(themename='darkly')
window.geometry('600x400')
window.title('Layout Intro')


# widgets
label1 = ttk.Label(window, text='Label 1', background='blue')
label2 = ttk.Label(window, text='Label 2', background='red')


# pack
# label1.pack(side='left', expand=True, fill='both', padx=10, pady=10)
# label2.pack(side='right')

# # grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)


# label1.grid(row=0, column=1, sticky='nsew')
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')

# place
label1.place(x=10, y=10, width=100, height=100)
# label2.place(x=50, y=50, width=100, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=0.5,relheight=1,anchor='center')
# run
window.mainloop()