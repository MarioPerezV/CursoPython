from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroTextoNombre=Entry(miFrame)
cuadroTextoNombre.grid(row=0, column=1) # (Filas, columnas)
cuadroTextoNombre.config(fg="red", justify="center")
# cuadroTexto.place(x=100, y=100)

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1)

cuadroTextoApellidoMaterno=Entry(miFrame)
cuadroTextoApellidoMaterno.grid(row=2, column=1)

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=3, column=1)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=4, column=1)
cuadroPass.config(show="*")

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) # No respeta el tamaño ingresado anteriormente
# nombreLabel.place(x=100, y=100)

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) # "e"= este (derecha)

apellidoMaternoLabel=Label(miFrame,text="Apellido Materno: ")
apellidoMaternoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame,text="Dirección de trabajo: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10) # pad= espacio entre filas

passwordLabel=Label(miFrame,text="Password: ")
passwordLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10) # pad= espacio entre filas


raiz.mainloop()
