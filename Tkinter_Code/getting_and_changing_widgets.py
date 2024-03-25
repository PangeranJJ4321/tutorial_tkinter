import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    entry_text = entry.get()

    #widgets can be updated with config
    # Label.config(text = 'some new text')
    # Label['text'] = 'some new text'

    # update the label
    # label.config(text='some other text')
    label['text'] = entry_text
    entry['state'] = 'disable'
    # print(label.configure())

# window
window = tk.Tk()
window.title('Getting and setting widgets')


# widgets

    # label
label = ttk.Label(master=window, text = 'Some text')
label.pack()

    # entry
entry = ttk.Entry(master=window, text = 'The button')
entry.pack()

    # button
button = ttk.Button(master=window, text='The button', command= button_func)
button.pack()

# exercise
# add another button that changes text back to 'some text' and thet enable entry

def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

exercise_button = ttk.Button(master=window, text='exercise button', command= reset_func)
exercise_button.pack()
# run
window.mainloop()