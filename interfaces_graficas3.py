from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miImagen=PhotoImage(file="Stewie.gif")
Label(miFrame, image=miImagen).place(x=100, y=200)
# La primera lìnea es lo mismo que las otras dos siguientes siempre y cuando no se vuelva a utilizar la variable miLabel
# Label(miFrame, text="Felicidades campeón", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)
# miLabel=Label(miFrame, text="Felicidades campeón")
# miLabel.place(x=100, y=200)

root.mainloop()