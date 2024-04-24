'''
The widget is called tk.Menu, you use several of them and nest them.. a lot

contoh:

if you place a tk.Menu inside of another tk.Menu it becomes one option

for a sub menu, you would plac a menu inside of a menu inside of another menu
'''
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='darkly')
window.geometry('600x400')
window.title('Menu')

# menu

menu =tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff= False)
file_menu.add_command(label='New', command= lambda: print('New file'))
file_menu.add_command(label='Open', command= lambda: print('Open file'))
file_menu.add_separator()
menu.add_cascade(label= 'File', menu= file_menu)


# another sub menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help entry', command=lambda :print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable= help_check_string)
menu.add_cascade(label='Help', menu = help_menu)

# exersice menu
exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label='Read web', command=lambda: print('https://gemini.google.com/app'))

menu.add_cascade(label='Open web', menu = exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_sub_menu.add_command(label='some more stuff', command=lambda: print('https://gemini.google.com/app'))
exercise_menu.add_cascade(label='more stuf', menu = exercise_sub_menu)



window.configure(menu = menu)

# menu button

menu_button = tk.Menubutton(window, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label='entry 1', command= lambda: print('test 1'))
button_sub_menu.add_checkbutton(label='check 1')
menu_button.configure(menu = button_sub_menu)


# run
window.mainloop()
