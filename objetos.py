from Personaje import *
#Crear un objeto de la clase personaje


heroe= Personaje()

#2. Usar atributos

print("El personaje se llama: "+heroe.nombre)
print("pertenece a la especie: "+heroe.especie)
print("y tiene una altura de: "+heroe.altura)

#3. Usar los metodos

heroe.correr(True)
heroe.lanzargranadas()
heroe.recargarArma(87)
