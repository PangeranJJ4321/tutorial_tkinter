'''Dalam konteks pembelajaran Tkinter, "Sliders" mengacu 
pada elemen GUI (Graphical User Interface) yang digunakan 
untuk memungkinkan pengguna mengatur nilai numerik dengan 
menggeser pegangan (slider) ke kiri atau ke kanan. Sliders 
sering digunakan untuk mengontrol parameter numerik seperti 
tingkat kecerahan, volume suara, ukuran font, dan sebagainya 
dalam aplikasi GUI.

Dalam Tkinter, elemen GUI ini diimplementasikan dengan 
menggunakan widget Scale. Widget Scale memungkinkan Anda 
untuk membuat slider dengan nilai awal tertentu dan menentukan 
rentang nilai yang dapat diatur pengguna.

Berikut adalah contoh sederhana penggunaan Scale 
dalam Tkinter untuk membuat slider:'''

import tkinter as tk

# fungsi
def update_value(value):
    print("Nilai yang dipilih:", value)

# window
root = tk.Tk()

# sliders
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_value)
slider.pack()


# run
root.mainloop()
