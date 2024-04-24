import tkinter as tk
import ttkbootstrap as ttk

def check():
    nim_input = entry_str.get()
    if nim_input in ['H071231056', 'H071231066', 'H071231054']:
        output_str.set('Hadir')
    else:
        output_str.set('Tidak hadir')

#  window 
window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry('450x200')

# title label

title_label = ttk.Label(window, text='Aplikasi kehadiran mahasiswa', font='Calibri 18 bold')
title_label.pack()


# input field
input_frame = ttk.Frame(window)
entry_str = ttk.StringVar()
entry = ttk.Entry(input_frame, textvariable=entry_str)
# label nim
label_nim = ttk.Label(input_frame,text='Nim', font= 'Calibri 14 bold')
label_nim.pack(side='left', pady=10)
# botton check
check_buton = ttk.Button(input_frame, text='Check', command= check, bootstyle='primary')
entry.pack(side='left', padx=10)
check_buton.pack(side='right')
input_frame.pack(pady=10)

# output
output_str = tk.StringVar()
output_label = ttk.Label(
    window,
    text= 'Output',
    font= 'Calibri 24',
    textvariable= output_str
)
output_label.pack(pady=5)
# run
window.mainloop()
