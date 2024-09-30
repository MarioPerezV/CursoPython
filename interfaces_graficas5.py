from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

miNombre=StringVar()

cuadroTextoNombre=Entry(miFrame, textvariable=miNombre) # Aceptando otra variación del JTextField
cuadroTextoNombre.grid(row=0, column=1) # (Filas, columnas)
cuadroTextoNombre.config(fg="red", justify="center")
# cuadroTexto.place(x=100, y=100)

cuadroTextoApellido=Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1, padx=10, pady=10)

cuadroTextoApellidoMaterno=Entry(miFrame)
cuadroTextoApellidoMaterno.grid(row=2, column=1, padx=10, pady=10)

cuadroTextoDireccion=Entry(miFrame)
cuadroTextoDireccion.grid(row=3, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=4, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

# JTextArea
textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)

scrollVertical=Scrollbar(miFrame, command=textoComentario.yview) #Scrollbar
scrollVertical.grid(row=5, column=2, sticky="nsew") # Aquí se coloca el scrollbar en la columna siguiente
textoComentario.config(yscrollcommand=scrollVertical.set) # Con esto se completa el posicionamiento del scroll


nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) # No respeta el tamaño ingresado anteriormente
# nombreLabel.place(x=100, y=100)

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) # "e"= este (derecha)

apellidoMaternoLabel=Label(miFrame,text="A. Materno: ")
apellidoMaternoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame,text="Dirección: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10) # pad= espacio entre filas

passwordLabel=Label(miFrame,text="Password: ")
passwordLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10) # pad= espacio entre filas

comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10) # pad= espacio entre filas


def codigoBoton():
	miNombre.set("Mario")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()
