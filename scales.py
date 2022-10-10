import tkinter as tk

def sumar(n):
    r = vertical.get() + horizontal.get()
    labelMessage.config(text=str(r) + ' --- ' + str(n))

ventana = tk.Tk()

vertical = tk.IntVar()
sliderv = tk.Scale(ventana, from_=0, to=50, variable=vertical, command=sumar).pack()
vertical.set(25)

horizontal = tk.IntVar()
sliderh = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL, variable=horizontal, command=sumar).pack()

labelMessage = tk.Label(ventana)
labelMessage.pack()

ventana.mainloop()