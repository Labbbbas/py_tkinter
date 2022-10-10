import tkinter as tk
from tkinter.constants import X

ventana = tk.Tk()

ventana.geometry('640x480')

l1 = tk.Label(ventana, text='Hola', bg='#FFAAAA')
l1.place(x=20, y=20, width=100, height=30)

l1 = tk.Label(ventana, text='Hey', bg='#AAFFAA')
l1.place(x=100, y=150, width=300, height=100)

l1 = tk.Label(ventana, text='Hi', bg='#AAAAFF')
l1.place(x=350, y=120, width=100, height=25)

ventana.mainloop()