'''
Jadi, the master was always the window,
but this isn't always what you want, A menu item should have a menu as the master

A tab entry should have a tab widget as the master

For example layouts, you can also create a container widget to organise you widgets.


ttk.Frame
id just an empty widget, You place widgets inside of it and then you place the frame

That way you can arrange widgets easily

'''

import tkinter as tk
from tkinter import ttk

# window 
window = tk.Tk()
window.geometry('600x400')
window.title('Frame and parenting')


# Frame
frame = ttk.Frame(window, width=100, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)

frame.pack(side='left')

# master seting
label = ttk.Label(frame, text='Label in frame')
label.pack()

# label in frame
button = ttk.Button(frame, text='button in frame')
button.pack()

# label in window
label2 = ttk.Label(window, text='button outside frame')
label2.pack(side='left')


# latihan

frame_ke2 = ttk.Frame(window, width=100, height=150, borderwidth=20, relief=tk.GROOVE)
frame_ke2.pack_propagate(False)
frame_ke2.pack(side='right',pady=30)

label_ke3 = ttk.Label(frame_ke2, text='new label')
label_ke3.pack()

# button
button2 = ttk.Button(frame_ke2, text='new button')

# entry
entry = ttk.Entry(frame_ke2)
entry.pack()
button2.pack()
# run
window.mainloop()