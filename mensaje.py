import tkinter as tk

ventana = tk.Tk()

miTexto = 'Hola amigos, ¿qué tal?'

msgMensaje = tk.Message(ventana, text=miTexto).pack()

msgMensaje2 = tk.Message(ventana, text=miTexto, width=300).pack()

# msgMensaje3 = tk.Message(ventana, text=miTexto, width=300)
# msgMensaje3.config(bg='blue', fg='white', font='Times 24 bold')
# msgMensaje3.pack()

msgMensaje3 = tk.Message(ventana, text=miTexto, width=300, bg='blue', fg='white', font='Times 24 bold').pack()

ventana.mainloop()