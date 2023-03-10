from tkinter import Tk, Button, Frame, messagebox, Label, Entry


def ingresar():
    
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()
    
    
    if correo == "omardc@upq.edu.mx" and contrasena == "1234":
        
        messagebox.showinfo("Aviso","¡Bienvenido!")
    else:
        
        messagebox.showerror("Revisa tus datos")
 
        
        

ventana =Tk()
ventana.title("Login")
ventana.geometry("600x400")

#
correo_label =Label(ventana, text="Correo:")
correo_label.pack()
correo_entry =Entry(ventana)
correo_entry.pack()

contrasena_label =Label(ventana, text="Contraseña:")
contrasena_label.pack()
contrasena_entry =Entry(ventana, show="*")
contrasena_entry.pack()

boton =Button(ventana, text="Ingresar", command=ingresar)
boton.pack()

mensaje_label =Label(ventana, text="")
mensaje_label.pack()


ventana.mainloop()








