import tkinter as tk
from tkinter import filedialog as fd
from tkinter.colorchooser import askcolor
from tkinter import messagebox

def MostrarDiagolo():
    ruta = fd.askopenfilename()
    # print(ruta)
    messagebox.showinfo('Ruta del archivo', 'La ruta del archivo es: ' + ruta)

def SeleccionarColor():
    colorS = askcolor(color='#FFFFFF', title='Selecciona un color')
    # print(colorS)
    messagebox.showinfo('Configuración del color', str(colorS))


ventana = tk.Tk()

btnAbrir = tk.Button(text='Abrir archivo', command=MostrarDiagolo).pack()
btnColor = tk.Button(text='Seleccionar color', command=SeleccionarColor).pack()

ventana.mainloop()