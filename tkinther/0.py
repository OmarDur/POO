from tkinter import Tk, Button, Frame, messagebox

def ingreso():

    correo = correo_entry.get()
    contrasena = contrasena_entry.get()

    if correo == "omardc@gmail.com" and contrasena == 12345:
        messagebox.showinfo("Aviso", "Bienvenido")
    else:
        messagebox.showerror("Aviso", "Revise el correo o contraseña")
    
ventana= Tk()
ventana.title("Login")
ventana.geometry("600x400")







ventana.mainloop()

    