# if canvas is paint, treeview is excel we are creating a table

import tkinter as tk
from tkinter import ttk
from random import choice

# windpw
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data
first_names = ['Bob', 'Maria', ' Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names  = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text= 'First name')
table.heading('last', text= 'Surname')
table.heading('email', text= 'Email')

table.pack(fill='both', expand=True)

table.pack()

# insert value into a table
# table.insert(parent='', index=0, values=('Joh','Doe',';John@gmail.com'))

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@gmail.com'
    data = (first, last, email)

    table.insert(parent='', index=0, values= data)

table.insert(parent='', index=tk.END, values=('Pangeran','Juhrifar','pangeranjuhrifar@gmail.com'))

# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
    # table.item(table.selection())
# table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))

def delete_item(_):
    print('delete')
    for i in table.selection():
        print(table.item(i)['values'])
        table.delete(i)
    
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_item)
# run
window.mainloop()
