from tkinter import Tk, Button, Frame, messagebox

def mostrarMensaje():
    messagebox.showinfo("Aviso", "Presione el boton azul")


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


#3.- Agregamos botones

botonAzul= Button(seccion1, text="Boton Azul", fg="blue" , command=mostrarMensaje)
botonAzul.place(x=60, y=60)

botonNegro= Button(seccion2, text="Boton Negro", fg="black", bg="white")
botonNegro.grid(row=0 , column=0)

botonAmarillo= Button(seccion2, text="Boton rojo", fg="red", bg="orange")
botonAmarillo.grid(row=1 , column=1)

botonVerde= Button(seccion3, text="Boton verde", fg="red", bg="green")
botonVerde.configure(height=2,width=10)
botonVerde.pack()


#LLamamos el Main
ventana.mainloop()