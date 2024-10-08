from tkinter import *
from tkinter import messagebox
import sqlite3


#--------------FUNCIONES---------------

def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			#PASSWORD VARCHAR(50),
			EMAIL VARCHAR(50),
			TELEFONO VARCHAR(50),
			COMENTARIOS VARCHAR (1000))
		''')

		messagebox.showinfo("BBDD", "BBDD creada con éxito")

	except:
		messagebox.showwarning("Atencion", "La BBDD ya existe")


def salirAplicacion():
	valor=messagebox.askquestion("Salir", "Desea salir de la aplicación?")

	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miEmail.set("")
	miTelefono.set("")
	#miPass.set("")
	textoComentario.delete(1.0, END) # 1.0 Limpia desde el inicio hasta el final END

def crear():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
		#"','" + miPass.get() +
		"','" + miEmail.get() +
		"','" + miTelefono.get() +
		"','" + textoComentario.get("1.0", END) + "')") 
	
	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro ingresado con éxito")

"""	NO ME RESULTÓ CON ESTE CÓDIGO
	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
	datos=miNombre.get(),miPass.get(),miEmail.get(),miTelefono.get(),textoComentario.get("1.0", END)

	DEBERÍA REEMPLAZAR ESTE CÓDIGO
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='" + miPass.get() +
		"', EMAIL='" + miEmail.get() +
		"', Telefono='" + miTelefono.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())"""
	
	
def leer():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

	elUsuario=miCursor.fetchall()

	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		#miPass.set(usuario[2])
		miEmail.set(usuario[3])
		miTelefono.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='" + miPass.get() +
		"', Email='" + miEmail.get() +
		"', Telefono='" + miTelefono.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro Actualizado con éxito")

""" NO ME RESULTÓ CON ESTE CÓDIGO
	datos=miNombre.get(),miPass.get(),miEmail.get(),miTelefono.get(),textoComentario.get("1.0", END)
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,EMAIL=?,Telefono=?,COMENTARIOS=? " +
		"WHERE ID=" + miId.get(),(datos))
	
	DEBERÍA REEMPLAZAR ESTE CÓDIGO
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='" + miPass.get() +
		"', EMAIL='" + miEmail.get() +
		"', Telefono='" + miTelefono.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())"""


def eliminar():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro Eliminado con éxito")


#---------------BARRA DE MENU SUPERIOR---------------
root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300,height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-----------CAMPOS---------------
miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miEmail=StringVar()
miPass=StringVar()
miTelefono=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=1, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=2, column=1, padx=10, pady=10)
#cuadroNombre.config(fg="red", justify="right")

#cuadroPass=Entry(miFrame, textvariable=miPass)
#cuadroPass.grid(row=2, column=1, padx=10, pady=10)
#cuadroPass.config(show="*")

cuadroEmail=Entry(miFrame, textvariable=miEmail)
cuadroEmail.grid(row=3, column=1, padx=10, pady=10)

cuadroTelefono=Entry(miFrame, textvariable=miTelefono)
cuadroTelefono.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview) # Busca en el vertice y
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#------------------------------LABEL-----------

tituloLabel=Label(miFrame, text="Registro de Contactos")
tituloLabel.grid(row=0, column=0, sticky="e", padx=20, pady=10)

idLabel=Label(miFrame, text="ID Contacto")
idLabel.grid(row=1, column=0, sticky="e", padx=20, pady=10)
#idLabel.config(justify="right")

nombreLabel=Label(miFrame, text="Nombre Completo:")
nombreLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

#passLabel=Label(miFrame, text="Password:")
#passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

emailLabel=Label(miFrame, text="Email:")
emailLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

telefonoLabel=Label(miFrame, text="Teléfono:")
telefonoLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario:")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#---------------BOTONES-----------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)




root.mainloop()




