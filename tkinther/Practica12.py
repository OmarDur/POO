from tkinter import Tk, Button, Frame, messagebox

def mostrarMensaje():
    messagebox.showinfo("Aviso", "Presionar el boton azul")

ventana= Tk()
ventana.title("Login")
ventana.geometry("600x400")

def ingresar():
    # Obtenemos el correo y la contraseña ingresados por el usuario
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()
    
    # Verificamos si el correo y la contraseña son correctos
    if correo == "omardc@upq.edu.mx" and contrasena == "1234":
        # Si son correctos, mostramos un mensaje de bienvenida
        mensaje_label.config(text="¡Bienvenido!")
    else:
        # Si son incorrectos, indicamos que revise sus datos
        mensaje_label.config(text="Revise sus datos")





