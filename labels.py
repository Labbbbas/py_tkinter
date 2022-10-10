import tkinter as tk

ventana = tk.Tk()

mensaje = """Hola a todos
¿Cómo están?
Adiós"""

labelMessage = tk.Label(ventana, text=mensaje, justify=tk.CENTER).pack()

ventana.mainloop()