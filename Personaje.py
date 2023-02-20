class Personaje:
    #atributos personaje
    especie= "Humano"
    nombre= "Master Chief"
    altura= "2.70"

    #Metodos del personaje

    def correr(self,status):
        if(status):
            print("El personaje "+ self.nombre +" el personaje esta corriendo")
        else:
            print("El personaje "+ self.nombre+ "se detuvo")

    def lanzargranadas(self):
        print("El personaje"+self.nombre +"lanzo una granada")

    def recargarArma(self, municiones):
        corgador=10
        cargador= cargador + municiones
        print("El arma tiene" + cargador +"balas")
