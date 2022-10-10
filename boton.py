import tkinter as tk

class Test():
    def __init__(self):
        self.ventana = tk.Tk()
        self.texto  = tk.StringVar()
        self.texto.set('Hola Mundo')

        self.MiEtiqueta = tk.Label(self.ventana, textvariable=self.texto, font='arial 24').pack()

        self.MiBoton = tk.Button(self.ventana, text='Cambia el mensaje', font='arial 24', command=self.changeText).pack()

        self.ventana.mainloop()

    def changeText(self):
        self.texto.set('Nuevo mensaje')

app = Test()