from abc import ABC, abstractmethod
import random

class Personaje(ABC):
    def __init__(self, nombre, vida):
        self.__nombre = nombre
        self.__vida = vida

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida (self, valor):
        # Evita vida negativa
        if (valor < 0 ):
            self.__vida = 0
        else:
            self.__vida = valor

        #Tambien funcionaria asi
        #self._vida = max(0, valor)
            
    
    @property
    def vivo(self):
        return self.__vida < 0 
    
    @abstractmethod
    def atacar(self, objetivo):
        raise NotImplementedError
    

#Composición con Arma
class Arma:
    def __init__(self, nombre, danio):
        self.__nombre = nombre
        self.__danio = danio

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def danio(self):
        return self.__danio
    

class Guerrero(Personaje):
    def __init__(self, nombre, vida, arma):
        super().__init__(nombre, vida)
        self.__arma = arma


    @property
    def arma(self):
        return self.__arma

    def atacar(self, objetivo):
        """
        self.arma	Porque existe @property arma en Guerrero
        self.arma.danio	Porque Arma tiene @property danio
        ¿El atributo es privado?	Sí, pero los getters permiten acceso controlado
        """

        danio = self.arma.danio + random.randint(0,5)
        objetivo.vida -= danio

        print(f"{self.nombre} golpea con {self.arma.nombre} y causa {danio} de daño")


        

        








    
    
