import tkinter as tk;
import ttkbootstrap as ttk;


#  window
window = ttk.Window(themename='darkly')
window.title('Pack & Frame')
window.geometry('600x400')

# layout
label1 = ttk.Label(window, text='label 1', background='red')
label2 = ttk.Label(window, text='label 2', background='blue')

# Frame
frame = ttk.Frame(window, width=100, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)

label1.pack(side='top', expand=True, fill='both')
label2.pack(side='top', expand=True, fill='both')
frame.pack(side='top', expand=True, fill='both')

# lable in frame

frame_label1 = ttk.Label(frame, text='Label 1 in frame', background='green')

frame_AButton = ttk.Button(frame, text='A button')
frame_label2 = ttk.Label(frame, text='last Label of frame', background='orange')

frame_Batton2 = ttk.Button(frame, text='Another Button')
frame_Batton3 = ttk.Button(frame, text='Button 3')

frame_Batton4 = ttk.Button(frame, text='Button 4')
frame_Button5 = ttk.Button(frame, text='Button 5')

frame_label1.pack(side='top',expand=True)
frame_AButton.pack(side='left',expand=True ,fill='both',padx=20,pady=20)
frame_label2.pack(side='left',expand=True )
frame_Batton2.pack(side='left',expand=True )
frame_Batton3.pack(side='top', fill='both',expand= True,padx=5)
frame_Batton4.pack(side='top', fill='both',expand= True,padx=5)
frame_Button5.pack(side='top', fill='both',expand= True,padx=5)

# run
window.mainloop()