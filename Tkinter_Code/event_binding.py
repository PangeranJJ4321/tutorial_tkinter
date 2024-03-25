import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x = {event.x} y = {event.y}')


# window
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x500')

# widgets
text = tk.Text(
    window
)
text.pack()

entry = ttk.Entry(
    window)
entry.pack()

button = ttk.Button(
    window,
    text = 'A button'
)
button.pack()

# events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f'a button eas pressed ({event.char})'))
# window .bind('<Motion>', get_pos)

entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# exercise :
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))
# run
window.mainloop()