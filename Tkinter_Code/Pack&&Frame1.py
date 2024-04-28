import tkinter as tk
import ttkbootstrap as ttk
# from tkinter import ttk


# window
window = ttk.Window(themename='darkly')
# window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='Label pertama', background='red')
label2 = ttk.Label(top_frame, text='Label kedua', background='blue')

# midle widget
label3 = ttk.Label(window, text='Another label', background='green')

# buttom frame
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text='A button')
label4 = ttk.Label(button_frame, text='Last of the labels', background='orange')
button2 = ttk.Button(button_frame, text='another button')

# Exercise 
exercise_frame = ttk.Frame(button_frame)
button3 = ttk.Button(exercise_frame, text='Button3') 
button4 = ttk.Button(exercise_frame, text='Button4')
button5 = ttk.Button(exercise_frame, text='Button5')
# top layout
label1.pack(side='left', fill='both',expand=True)
label2.pack(side='left', fill='both',expand=True)
top_frame.pack(fill='both', expand=True)

# midle layout
label3.pack(expand=True)

# button layout
button.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
button_frame.pack(expand=True, fill='both', padx=20, pady=20)

# exercise layout
button3.pack(expand=True,fill='both')
button4.pack(expand=True,fill='both')
button5.pack(expand=True,fill='both')
exercise_frame.pack(fill='both',side='left', expand=True)

# Exercise
'''

create 3 more buttons and another frame
the frame should be on the right inside of the buttom framean and the buttons should be staked vertically inside of it
'''


# run
window.mainloop()