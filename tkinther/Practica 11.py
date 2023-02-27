from tkinter import Tk, Button, Frame

#1. Instanciamos la ventana
ventana= Tk()
ventana.title("Ejemplo de 3 frames ")
ventana.geometry("600x400")

#2.- Agregamos los frames
seccion1= Frame(ventana, bg="blue")
seccion1.pack(expand=True, fill="both")

seccion2= Frame(ventana, bg="yellow")
seccion2.pack(expand=True, fill="both")

seccion3= Frame(ventana, bg="green")
seccion3.pack(expand=True, fill="both")


#LLamamos el Main
ventana.mainloop()