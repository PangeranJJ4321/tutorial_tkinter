'''
you don't really hide/reveal widgets
instead, you remove and add widgets to the layout

'''

import ttkbootstrap as ttk
def toggel_label_place():
    global label_visible
    if label_visible:
        label.place_forget()
        label_visible = False
    else:
        label_visible = True
        label.place(relx=0.5, rely=0.5, anchor='center')
        
# setup
window = ttk.Window(themename='darkly', title='Hide widgets')
window.geometry('600x400')

# place
button = ttk.Button(window, text='toggle label', command= toggel_label_place)
button.place(x=10, y=10)

label_visible = True
label = ttk.Label(window, text='Pangeran Juhrifar Jafar', font='Calibri 24 bold')
label.place(relx=0.5, rely=0.5, anchor='center')

# run
window.mainloop()