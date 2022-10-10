import tkinter as tk

ventana = tk.Tk()

logo = tk.PhotoImage(file='rickroll.png')

labelMessage = tk.Label(ventana, image=logo).pack()

labelMessage2 = tk.Label(ventana, image=logo).pack(side='right')

mensaje = """Ahora colocamos texto
junto con la imagen
y experimentamos como
va a lucir juntos"""

labelMessage3 = tk.Label(ventana, text=mensaje).pack(side='left')

labelMessage4 = tk.Label(ventana, text=mensaje, image=logo, compound=tk.CENTER).pack()

ventana.mainloop()