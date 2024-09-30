from tkinter import *

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guradar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)

archivoHerramientas=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Acerca de")
archivoAyuda.add_command(label="Actualizar")
archivoAyuda.add_command(label="Licecia")
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()