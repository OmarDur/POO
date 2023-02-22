class Personaje:
    #Definimos ek constructor del personaje

    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt


    #atributos personaje

    #Metodos del personaje

    def correr(self,status):
        if(status):
            print("El personaje "+ self.nombre +" el personaje esta corriendo")
        else:
            print("El personaje "+ self.nombre+ " se detuvo")

    def lanzargranadas(self):
        print("El personaje "+self.nombre +" lanzo una granada")

    def recargarArma(self, municiones):
        cargador=10
        cargador= cargador + municiones
        print("El arma tiene " + str(cargador) +" balas")
