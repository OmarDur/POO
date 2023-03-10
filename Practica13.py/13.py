import string
import random
import tkinter as tk

def generate_password(length, uppercase, special_chars):
    """Función para generar contraseñas aleatorias."""
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_strength(password):
    """Función para comprobar la fortaleza de la contraseña."""
    strength = 0
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    return strength

def generate_password_GUI():
    """Función para crear la interfaz gráfica."""
    window = tk.Tk()
    window.title("Generador de contraseñas")
    window.geometry("400x400")
    
    tk.Label(window, text="Longitud de la contraseña:").grid(row=0, column=0)
    length_entry = tk.Entry(window)
    length_entry.grid(row=0, column=1)
    length_entry.insert(0, "8") # Es una longitud por default pero tambien le puedes  la longitud
    
    uppercase_var = tk.IntVar()
    uppercase_checkbutton = tk.Checkbutton(window, text="Incluir mayúsculas", variable=uppercase_var)
    uppercase_checkbutton.grid(row=1, column=1, columnspan=2)
    
    special_chars_var = tk.IntVar()
    special_chars_checkbutton = tk.Checkbutton(window, text="Incluir caracteres especiales", variable=special_chars_var)
    special_chars_checkbutton.grid(row=2, column=1, columnspan=2)
    
    tk.Button(window, text="Generar contraseña", command=lambda: generate_password_callback(length_entry.get(), uppercase_var.get(), special_chars_var.get())).grid(row=3, column=1, columnspan=2)
    
    strength_label = tk.Label(window, text="Fortaleza de la contraseña:")
    strength_label.grid(row=4, column=0)
    
    strength_value_label = tk.Label(window, text="")
    strength_value_label.grid(row=4, column=1)
    
    def generate_password_callback(length, uppercase, special_chars):
        """Función para generar la contraseña y actualizar la interfaz."""
        length = int(length)
        password = generate_password(length, uppercase, special_chars)
        strength = check_password_strength(password)
        strength_value_label.config(text=str(strength))
        password_label.config(text=password)
    
    password_label = tk.Label(window, text="")
    password_label.grid(row=5, column=0, columnspan=2)
    
    window.mainloop()

generate_password_GUI()