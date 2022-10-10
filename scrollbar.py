import tkinter as tk

ventana = tk.Tk()

scroll = tk.Scrollbar(ventana)
texto = tk.Text(ventana, height=10, width=30)

scroll.pack(side=tk.RIGHT, fill=tk.Y)
texto.pack(side=tk.LEFT, fill=tk.Y)

scroll.config(command=texto.yview)

texto.config(yscrollcommand=scroll.set)

mensaje = 'Daredevil (también llamado Dan Defensor, Diablo Defensor o Diabólico en muchas de las traducciones al español), alter ego de Matthew Michael "Matt" Murdock, es un superhéroe ficticio que aparece en los cómics estadounidenses publicados por Marvel Comics. Daredevil fue creado por el escritor y editor Stan Lee y el artista Bill Everett, con una cantidad no especificada de aportes de Jack Kirby. El personaje apareció por primera vez en Daredevil #1 (abril de 1964) en la Edad de Plata de los cómics. La influencia del escritor y artista Frank Miller en el título a principios de la década de 1980 . Daredevil es comúnmente conocido por apodos como "El hombre sin miedo"y el "Diablo de la Cocina del Infierno".'

texto.insert(tk.END, mensaje)

ventana.mainloop()