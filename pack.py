import tkinter as tk
from tkinter.constants import BOTTOM, CENTER, LEFT, TOP

ventana = tk.Tk()

# Pack básico
# l1 = tk.Label(ventana, text='Hola', bg='#FFAAAA').pack()
# l2 = tk.Label(ventana, text='Hello', bg='#AAFFAA').pack()
# l3 = tk.Label(ventana, text='Bonjour', bg='#AAAAFF').pack()

# Para ocupar todo el width disponible
# l1 = tk.Label(ventana, text='Hola', bg='#FFAAAA')
# l1.pack(fill=tk.X)
# l2 = tk.Label(ventana, text='Hello', bg='#AAFFAA')
# l2.pack()
# l3 = tk.Label(ventana, text='Bonjour', bg='#AAAAFF')
# l3.pack(fill=tk.X)

# Para agregar marco exterior
# l1 = tk.Label(ventana, text='Hola', bg='#FFAAAA')
# l1.pack(fill=tk.X, padx=20, pady=20)
# l2 = tk.Label(ventana, text='Hello', bg='#AAFFAA')
# l2.pack(fill=tk.X)
# l3 = tk.Label(ventana, text='Bonjour', bg='#AAAAFF')
# l3.pack(fill=tk.X)

# Para agregar marco interior
# l1 = tk.Label(ventana, text='Hola', bg='#FFAAAA')
# l1.pack(fill=tk.X, ipadx=20, ipady=20)
# l2 = tk.Label(ventana, text='Hello', bg='#AAFFAA')
# l2.pack(fill=tk.X)
# l3 = tk.Label(ventana, text='Bonjour', bg='#AAAAFF')
# l3.pack(fill=tk.X)

# Para acomodar elementos en base de posiciones relativas
l1 = tk.Label(ventana, text='Hola', bg='#FFAAAA')
l1.pack(fill=tk.X, side=tk.RIGHT)
l2 = tk.Label(ventana, text='Hello', bg='#AAFFAA')
l2.pack(fill=tk.X, side=LEFT)
l3 = tk.Label(ventana, text='Bonjour', bg='#AAAAFF')
l3.pack(fill=tk.X, side=TOP)

ventana.mainloop()