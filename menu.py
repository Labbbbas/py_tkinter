# -*- encoding: utf-8 -*-

import tkinter as tk
from tkinter import Menu, messagebox

ventana = tk.Tk()

def Menu1():
    messagebox.showinfo('Menú 1', 'Se ejecuta el menú 1')
    # print('Hola')

def Menu2():
    messagebox.showinfo('Menú 2', 'Se ejecuta el menú 2')
    # print('Adios')

def Salir():
    ventana.destroy()

miMenu = Menu(ventana)
ventana.config(menu=miMenu)

menuPrincipal = Menu(miMenu)
miMenu.add_cascade(label='Archivo', menu=menuPrincipal)

menuPrincipal = tk.Button(ventana, text='Accion 1', command=Menu1).pack()
menuPrincipal = tk.Button(ventana, text='Accion 2', command=Menu2).pack()
menuPrincipal = tk.Button(ventana, text='Salir', command=Salir).pack()

# menuPrincipal.add_command(label='Accion 1', command=Menu1)
# menuPrincipal.add_command(label='Accion 2', command=Menu2)
# menuPrincipal.add_command(label='Salir', command=Salir)

ventana.mainloop()