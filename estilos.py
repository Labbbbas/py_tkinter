import tkinter as tk

ventana = tk.Tk()

labelMessage = tk.Label(ventana, text='Hola a todos', fg='blue').pack()

labelMessage2 = tk.Label(ventana, text="Nueva etiqueta", fg='red', font='Helvetica 10 bold').pack()

labelMessage3 = tk.Label(ventana, text='Another window', fg='white', bg='red', font='Times 18').pack()

ventana.mainloop()