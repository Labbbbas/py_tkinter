import tkinter as tk


def Mostrar():
    if seleccion.get() == 1:
        mensaje = 'Has seleccionado Python'
    elif seleccion.get() == 2:
        mensaje = 'Has seleccionado C#'
    elif seleccion.get() == 3:
        mensaje = 'Has seleccionado Java'

    labelMessage.config(text=mensaje)


ventana = tk.Tk()
seleccion = tk.IntVar()


rbnPython = tk.Radiobutton(ventana, text='Python', variable=seleccion, value=1, command=Mostrar).pack(anchor=tk.W)

rbnCSharp = tk.Radiobutton(ventana, text='C#', variable=seleccion, value=2, command=Mostrar).pack(anchor=tk.W)

rbnJava = tk.Radiobutton(ventana, text='Java', variable=seleccion, value=3, command=Mostrar).pack(anchor=tk.W)


labelMessage = tk.Label(ventana)
labelMessage.pack()


ventana.mainloop()