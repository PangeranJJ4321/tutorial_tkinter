'''
We only changed the title and size of the the window

We can change lots more: apacity, position, full screen, full screen, title bar

'''

import tkinter as tk
import ttkbootstrap as ttk

# window 
window  = ttk.Window(themename='darkly')
window.title('More on the window')
window.geometry('600x400+100+200')
# window.iconbitmap('nama file')


# window attributes

window.minsize(200, 100)
# window.maxsize(800,700)
window.resizable(True,False)


# exercise
# start window in the midle of the screen
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width/2 - window_width/2)
top  = int(display_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')



# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes

window.attributes('-alpha',1)
# window.attributes('-topmost',True)

# security event

window.bind('<Escape>', lambda event: window.quit())

# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)


# Title bar
# window.overrideredirect(True)
# run)
window.mainloop()