import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
'''
Event adalah kejadian yang terjadi dalam aplikasi Tkinter, seperti klik mouse, pencet keyboard, 
perubahan ukuran jendela, dan sebagainya.
Binding adalah proses mengaitkan event tersebut dengan sebuah fungsi atau metode

'''
def get_pos(event):
    print(f'x = {event.x} y = {event.y}')


# window
# window = tk.Tk()
window = ttk.Window(themename='darkly')
window.title('Event Binding')
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f'a button eas pressed ({event.char})'))
# window .bind('<Motion>', get_pos)

# contoh
'''
Ketika event terjadi:

1. Tkinter akan mendeteksi event tersebut.
2. Tkinter akan mencari binding yang terkait dengan event tersebut.
3. Jika binding ditemukan:
    - Tkinter akan memanggil fungsi yang terkait dengan binding tersebut.
    - Fungsi tersebut akan dieksekusi dengan membawa informasi tentang event yang terjadi (seperti koordinat mouse, tombol keyboard yang ditekan, dll.).
4. Jika binding tidak ditemukan:
    - Event tersebut tidak akan diproses lebih lanjut.

'''
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# exercise 1:
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
# text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))


# run
window.mainloop()