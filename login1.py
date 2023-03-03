import tkinter as tk

def mostrarMensaje():
    messagebox.showinfo("Aviso", "Presione enter")

def ingresar():
    
    correo = correo_entry.get()
    contrasena = contrasena_entry.get()
    
    
    if correo == "omardc@upq.edu.mx" and contrasena == "1234":
        
        mensaje_label.config(text="¡Bienvenido!")
    else:
        
        mensaje_label.config(text="Revisa tus datos")
        

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("600x400")

#
correo_label = tk.Label(ventana, text="Correo:")
correo_label.pack()
correo_entry = tk.Entry(ventana)
correo_entry.pack()

contrasena_label = tk.Label(ventana, text="Contraseña:")
contrasena_label.pack()
contrasena_entry = tk.Entry(ventana, show="*")
contrasena_entry.pack()

boton = tk.Button(ventana, text="Ingresar", command=ingresar)
boton.pack()

mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()


ventana.mainloop()






