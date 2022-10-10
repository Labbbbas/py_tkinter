import tkinter as tk

def calcular():
    dias = int(edad.get())*365
    mensaje = nombre.get() + ' has vivido ' + str(dias) + ' dias'
    labelMessage.config(text=mensaje)

ventana = tk.Tk()

tk.Label(ventana, text='Nombre').pack()
nombre = tk.StringVar()
nomb = tk.Entry(ventana, textvariable=nombre).pack()

tk.Label(ventana, text='Edad').pack()
edad = tk.StringVar()
ed = tk.Entry(ventana, textvariable=edad).pack()

labelMessage = tk.Label(ventana)
labelMessage.pack()

btnCalcular = tk.Button(ventana, text='Calcular', command=calcular).pack()

ventana.mainloop()