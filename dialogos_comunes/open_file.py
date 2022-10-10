from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

raiz = Tk()

def abrirArchivo():
    text = []
    with open('Arbol_B.txt', 'r', encoding='utf-8') as f:
        for line in f:
            text.append(line)
    # print(*text)
    messagebox.showinfo('Arbol_B.txt', ''.join(text))

def abrirArchivo2():
    r = fd.askopenfilename()
    text = []
    with open(r, 'r', encoding='utf-8') as f:
        for line in f:
            text.append(line)
    messagebox.showinfo('Archivo', ''.join(text))

Button(raiz, text='Abrir archivo', command=abrirArchivo).pack()

raiz.mainloop()