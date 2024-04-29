import tkinter as tk
from tkinter import ttk
import ttkbootstrap as boots

def konversi():
    try:
        nilai = float(entry_nilai.get())
        satuan_dari = satuan_dari_var.get()
        satuan_ke = satuan_ke_var.get()

        konversi_faktor = {
        "km": {"hm": 10, "dam": 100, "m": 1000, "dm": 10000, "cm": 100000, "mm": 1000000},
        "hm": {"dam": 10, "m": 100, "dm": 1000, "cm": 10000, "mm": 100000},
        "dam": {"m": 10, "dm": 100, "cm": 1000, "mm": 10000},
        "m": {"dm": 10, "cm": 100, "mm": 1000},
        "dm": {"cm": 10, "mm": 100},
        "cm": {"mm": 10, "m": 0.01, "km": 0.00001},
        "mm": {"m": 0.001, "cm": 0.1, "dm": 0.01, "m": 0.001, "km": 0.000001}  
        }


        if satuan_dari in konversi_faktor and satuan_ke in konversi_faktor[satuan_dari]:
            hasil = nilai * konversi_faktor[satuan_dari][satuan_ke]
            hasil_label.config(text=f"Hasil: {hasil:.2f} {satuan_ke}")
        else:
            hasil_label.config(text="Konversi tidak valid")
    except ValueError:
        hasil_label.config(text="Masukan tidak valid")

# Window
window = boots.Window(themename="darkly", title="Konversi Panjang")
window.geometry('400x300')

# Judul
judul_label = ttk.Label(window, text="Konversi Panjang", font="Helvetica 18 bold")
judul_label.pack(pady=(10, 20))

# Frame untuk input
input_frame = ttk.Frame(window)
input_frame.pack(pady=10)

nilai_label = ttk.Label(input_frame, text="Nilai:")
nilai_label.grid(row=0, column=0, padx=(0, 10))
entry_nilai = ttk.Entry(input_frame, font='Calibri 12')
entry_nilai.grid(row=0, column=1)

satuan_dari_label = ttk.Label(input_frame, text="Dari:")
satuan_dari_label.grid(row=1, column=0, pady=10)
satuan_dari_var = tk.StringVar()
satuan_dari = ttk.Combobox(input_frame, textvariable=satuan_dari_var, values=['km','hm','dam','m','dm','cm','mm'])
satuan_dari.set('cm')
satuan_dari.grid(row=1, column=1)

satuan_ke_label = ttk.Label(input_frame, text="Ke:")
satuan_ke_label.grid(row=2, column=0)
satuan_ke_var = tk.StringVar()
satuan_ke = ttk.Combobox(input_frame, textvariable=satuan_ke_var, values=['km','hm','dam','m','dm','cm','mm'])
satuan_ke.set('mm')
satuan_ke.grid(row=2, column=1)

# Button
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)
konversi_button = ttk.Button(button_frame, text='Konversi', command=konversi)
konversi_button.pack()

# Output
hasil_label = ttk.Label(window, text="Hasil: ")
hasil_label.pack()

window.mainloop()
