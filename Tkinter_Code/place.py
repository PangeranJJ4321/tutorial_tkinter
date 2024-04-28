'''
Berbeda dengan layout manager lain seperti pack() dan grid(), place() memungkinkan Anda untuk memposisikan widget secara absolut dengan menentukan koordinat x dan y di dalam jendela. dan ini kurang populer

ini sintaxtnya
    widget.place(x=x_offset, y=y_offset, anchor=anchor_spec)

widget: Widget yang ingin Anda posisikan.
x=x_offset: Jarak horizontal dari tepi kiri jendela.
y=y_offset: Jarak vertikal dari tepi atas jendela.
anchor=anchor_spec: (Opsional) Menentukan titik jangkar widget (NW, N, NE, W, CENTER, E, SW, S, SE).
'''
# from tkinter import Tk, Button, Label
import ttkbootstrap as ttk
from ttkbootstrap import Window, Button, Label
# window
window = Window(themename='darkly')
window.title('Place')
window.geometry('400x600')

# widgets
label1 = Label(window, text='Label 1', background='red')
label2 = Label(window, text='Label 2', background='blue')
label3 = Label(window, text='Label 3', background='green')
button1 = Button(window, text='Button 1')



# layout 
label1.place(x=300, y=100, width=100, height=200)# posisi koordinat (x,y), wedth/ height = seberapa besar bentuk labelnya, absolute
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)# ini relatif ukurannya(rel), mengikuti perubahan layar(menyesuaikan)
label3.place(x=80, y= 60, width=160, height=300)

# button1.place(relx=1, rely=1, anchor='se')# anchor controls which point is placed
button1.place(relx=1, rely=1, anchor='se')

# Frame
frame = ttk.Frame(window)
frame_label = Label(frame, text='Frame label', background='yellow')
frame_button = Button(frame, text='Frame button')

# frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


# exercise 
# create a label and place it right in the center of the window
# the label should be half as wide as the window and be 200px
exercise_label = Label(window, text='exercise label', background='brown')
exercise_label.place(x=200, rely=0.5,anchor='center', relwidth=0.5, height=200)
# run
window.mainloop()
