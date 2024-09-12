# Диалоговое окно поиска и открытия файла

import tkinter
import os
from tkinter import filedialog
import subprocess, sys

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
               filetypes=(("Текстовый файл", ".txt"), ("Все файлы", "*")))
    text['text'] = text['text'] + '' + filename
    if sys.platform == "linux":
       subprocess.call(["xdg-open", filename])
    elif sys.platform == "darwin":
       subprocess.call(["open", filename])
    elif sys.platform == "windows":
       os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('750x150')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл:', height=5, width=83, background='silver', foreground='blue')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', background='silver',
                               foreground='blue', command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()
