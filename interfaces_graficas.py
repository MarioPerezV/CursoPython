from tkinter import *

raiz=Tk()

raiz.title("Primera Interfaz en Python")
raiz.resizable(False,False) # Ancho y alto
raiz.iconbitmap("ecoma.ico")
raiz.geometry("600x300") # ("Ancho x Alto")
raiz.config(bg="orange")

raiz.mainloop()