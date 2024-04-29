'''
widgets are always placed on top of other widgets when they are created(not when they are placed)

Although you ca raise widgets to be on top of all
widgets or of another widget
'''

import ttkbootstrap as ttk

# window
window = ttk.Window(themename='journal', title='Stacking order')
window.geometry('400x400')


# widgets
# label
label1 = ttk.Label(window, text='Label 1', background='green')
label2 = ttk.Label(window, text='Label 2', background='red')


# button
button1 = ttk.Button(window, text='raise label 1', command= lambda: label1.tkraise())
button2 = ttk.Button(window, text='raise label 2', command= lambda: label2.tkraise())

# layout
# label1.place(x=50, y=100, width=200, height=150)
# label2.place(x=150, y=60, width=140, height=100)

# button1.place(relx=0.8, rely=1, anchor='se')
# button2.place(relx=1, rely=1, anchor='se')



# exercise
# add a third label and button

exercise_label1 = ttk.Label(window, text='exercise label 1', background='blue')
exercise_label2 = ttk.Label(window, text='exercise label 2', background='black')
exercise_label3 = ttk.Label(window, text='exercise label 3', background='yellow')

exercise_button1 = ttk.Button(window, text='raise label 1', command= lambda: exercise_label1.tkraise()) 
exercise_button2 = ttk.Button(window, text='raise label 2', command= lambda: exercise_label2.tkraise()) 
exercise_button3 = ttk.Button(window, text='raise label 3', command= lambda: exercise_label3.tkraise()) 

# exercise layout

exercise_label1.place(x=30, y= 70, width=150, height=79)
exercise_label2.place(x=60, y= 70, width=250, height=130)
exercise_label3.place(x=90, y= 70, width=350, height=179)

exercise_button1.place(rely=1, relx=0.4, anchor='se')
exercise_button2.place(rely=1, relx=0.6, anchor='se')
exercise_button3.place(rely=1, relx=0.8, anchor='se')


# run
window.mainloop()