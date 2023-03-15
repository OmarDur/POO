from tkinther import *
import random, string


root=Tk()
root.geometry("400x400")
root.resinzable(0,0)
root.title("Generador de Contraseñas")

pass_label = Label(root, text = 'password lenght', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ =8, to_=32, textvariable = pass_len,width = 15).pack()

pass_str =StringVar()


