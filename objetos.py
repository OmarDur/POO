from Personaje import *
#1. Solicitar datos
print("")
print("###### Datos Heroe #")
especieH= input("Escribe la especie del Heroe: ")
nombreH= input("Escribe el nombre del heroe: ")
alturaH= float(input("Escribe la altura del Heroe: "))
recargaH= int(input("Cuantas balas recargas al Heroe: "))

print("")
print("###### Datos Villano #")
especieV= input("Escribe la especie del Villano: ")
nombreV= input("Escribe el nombre del Villano: ")
alturaV= float(input("Escribe la altura del Villano: "))
recargaV= int(input("Cuantas balas recargas al Villano: "))

#2. Cear objeto de clase Personaje
heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)

#3. Usar atributos

#Ejemplo del set para 1 atributo
heroe.setNombre(" BUZZ ")

print("")
print("###### Objeto Heroe ###")
print("El personaje se llama: "+heroe.getNombre())
print("pertenece a la especie: "+heroe.getEspecie())
print("y tiene una altura de: "+str(heroe.getAltura()))

heroe.correr(True)
heroe.lanzargranadas()
heroe.recargarArma(recargaH)

#Ejemplo de un metodo privado
#heroe.__pensar()

print("")
print("###### Objeto villano ###")
print("El personaje se llama: "+villano.getNombre())
print("pertenece a la especie: "+villano.getEspecie())
print("y tiene una altura de: "+str(villano.getAltura()))

#3. Usar los metodos

heroe.correr(False)
heroe.lanzargranadas()
heroe.recargarArma(recargaV)
