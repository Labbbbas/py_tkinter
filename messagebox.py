import tkinter as tk
from tkinter import messagebox

def mostrarBoton():
    # Para señalar errores
    # messagebox.showerror('Error de sintaxis', 'Te faltó cerrar el paréntesis')

    # Para mostrar información
    # messagebox.showinfo('Nezahualcóyotl', '21 grados Celsius')

    # Para mostrar un advertencia
    # messagebox.showwarning('Esto es una advertencia', 'Advertencia')

    # Para preguntar yes, no, cancel
    # r = messagebox.askquestion('Pregunta', '¿Programas en Python?')
    # if r == 'yes':
    #     messagebox.showinfo('Respuesta', 'Muy bien')
    # else:
    #     messagebox.showinfo('Respuesta', 'Muy mal')

    # r = messagebox.askquestion('Pregunta', '¿Eres estudiante?')
    # if r == 'yes':
    #     messagebox.showinfo('Respuesta', 'Qué bien')
    #     r = messagebox.askquestion('Pregunta', '¿Eres universitario?')
    #     if r == 'yes':
    #         messagebox.showinfo('Respuesta', 'De pelos')
    #     else:
    #         messagebox.showinfo('Respuesta', 'Bueno')
    # else:
    #     messagebox.showinfo('Respuesta', 'Ok')
    #     r = messagebox.askquestion('Pregunta', '¿Eres empleado?')
    #     if r == 'yes':
    #         messagebox.showinfo('Respuesta', 'Muy bien')
    #     else:
    #         messagebox.showinfo('Respuesta', 'Eres nini')

    # Para preguntar si se hace algo o no
    # r = messagebox.askokcancel('Ejecutar', '¿Ejecutamos el programa?')
    # if r == True:
    #     messagebox.showinfo('Programa', 'Se ejecuta el programa')
    # else:
    #     messagebox.showinfo('Programa', 'No se ejecuta el programa')

    # Para pregunar con retry o cancel
    # r = messagebox.askretrycancel('Pregunta', '¿Ejecutamos de nuevo el programa?')
    # if r == True:
    #     messagebox.showinfo('Programa', 'Se ejecuta de nuevo')
    # else:
    #     messagebox.showinfo('Programa', 'No se ejecuta de nuevo')

    # Para preguntar yes or no
    # r = messagebox.askyesno('Pregunta', '¿Ejecutamos de nuevo el programa?')
    # if r == True:
    #     messagebox.showinfo('Programa', 'Se ejecuta de nuevo')
    # else:
    #     messagebox.showinfo('Programa', 'No se ejecuta de nuevo')

    r = messagebox.askyesnocancel('Pregunta', '¿Ejecutamos de nuevo el programa?')
    if r == True:
        messagebox.showinfo('Programa', 'Se ejecuta de nuevo')
    elif r == False:
        messagebox.showinfo('Programa', 'No se ejecuta de nuevo')
    else:
        messagebox.showinfo('Programa', 'Cancelaste la ejecución')

ventana = tk.Tk()

boton = tk.Button(text='Mostrar', command=mostrarBoton)
boton.pack()

ventana.mainloop()