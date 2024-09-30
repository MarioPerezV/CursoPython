from tkinter import *

raiz=Tk()

raiz.title("Primera Interfaz en Python")
# raiz.resizable(False,False) # Ancho y alto
raiz.iconbitmap("ecoma.ico")
# raiz.geometry("600x300") # ("Ancho x Alto") # Para darle tamaño al Fame se debe 
raiz.config(bg="blue")
raiz.config(bd=45) # Grosor del borde
raiz.config(relief="groove") # Tipo de relieve en el borde "groove"
raiz.config(cursor="hand2") # Tipo de cursor "hand2"


miFrame=Frame()
miFrame.pack()
# miFrame.pack(side="left", anchor="s") # Dos posiciones del Frame: izquierda, s=sur(abajo)
# miFrame.pack(fill="both", expand=True) # Para acomodar el frame a la raíz
miFrame.config(bg="orange")
miFrame.config(width="600",height="300")
miFrame.config(bd=35) # Grosor del borde
miFrame.config(relief="sunken") # Tipo de relieve en el borde "groove"
miFrame.config(cursor="pirate") # Tipo de cursor "hand2"

raiz.mainloop()