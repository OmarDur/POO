from tkinter import *
from tkinter.ttk import *

index=Tk()
index.title("LOGIN")
index.geometry("600x400")
index.resizable(width=False, height=False)

luser=Label(index, text="Ingrese nombre de usuario:")
luser.pack()

user=StringVar()
euser=Entry(index, width=50, textvariable=user)
euser.pack()

lpas=Label(index, text="Password:")
lpas.pack()

pas=StringVar()
epas=Entry(index, width=50, textvariable=pas, show="*")
epas.pack()

def ingresar():
    if user.get()=="python" and pas.get()=="12345":
        WLOG.title("Correcto")

    else:
        WLOG.title("Incorrecto")
   
b1=Button(index, text="Entrar", command=ingresar)
b1.pack(side=BOTTOM)

index.mainloop()