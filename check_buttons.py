import tkinter as tk


def Mostrar():
    mensaje = ''

    if intchk1.get() == 1:
        mensaje += ' Manzana'
    if intchk2.get() == 1:
        mensaje += '\nPera'
    else:
        mensaje += '\nNo olvide comprar pera'

    labelMessage.config(text=mensaje)


ventana = tk.Tk()


intchk1 = tk.IntVar()
intchk2 = tk.IntVar()


labelMessage = tk.Label(ventana)
labelMessage.pack()


chk1 = tk.Checkbutton(ventana, text='Manzana', variable=intchk1).pack()
chk2 = tk.Checkbutton(ventana, text='Pera', variable=intchk2).pack()


btnMostrar = tk.Button(ventana, text='Comprar', command=Mostrar).pack()


ventana.mainloop()