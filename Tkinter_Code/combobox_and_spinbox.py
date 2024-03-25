# Both need be to get a list of values
# both connected to a Tkinter variable

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')


# combobox
items = ('Ice cream','Pizza','Broccoli','Appel')
food_string = tk.StringVar(value= items[0])
combo = ttk.Combobox(
    window,
    textvariable= food_string
)
combo['values'] = items
# combo.configure(values= items)
combo.pack()


# events

combo.bind(
    '<<ComboboxSelected>>', 
    lambda event: combo_label.config(text=f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(
    window,
    text='A label'
    # textvariable=food_string
)
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value= 0)
spin = ttk.Spinbox(
    window,
    from_= 3, to=20,
    increment= 3,
    command= lambda: print(spin_int.get()),
    textvariable= spin_int
    )
# spin['value'] = (1,2,3,4,5)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()


# exercise
# create a spinbox thet contains the letters A B C D E
# and print the value whenever the is decreased
exercise_string = tk.StringVar(value = 'E')
exercise_label = tk.Label(
    window, 
    text='exercise label',
    textvariable= exercise_string
)
exercise_label.pack()


exercise_spin = ttk.Spinbox(
    window,
    textvariable= exercise_string,
    values= ('A','B','C','D','E')

)
# exercise_spin['value'] = ('A','B','C','D','E')
# exercise_spin.bind('<<Increment>>', lambda event: print('Up'))
exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_spin.get()))
exercise_spin.pack()
# run
window.mainloop()