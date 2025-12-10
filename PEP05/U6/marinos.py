from abc import ABC, abstractmethod


#una calse astracta no puede ser instanciada
class AnimalMarino(ABC):

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre



    #obligo a cualquier clase hija a implementar estos métodos abstractos
    @abstractmethod
    def sonido(self):
        raise NotImplementedError
    
    @abstractmethod
    def saluda(self):
        raise NotImplementedError

    #yo implemente este método común para todas las clases hijas
    def salta(self):
        print(f"El delfin {self.nombre} está saltando fuera del agua!")


class Delfin(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)

    def saluda(self):
        print(f"Soy un delfin {self.nombre}")

    def sonido(self):
        print("Click y silbido")


    def salta(self):
        print(f"El delfin {self.nombre} está saltando fuera del agua!")



class Tiburon(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)

    def saluda(self):
        print(f"Soy un tiburon {self.nombre}")

    def sonido(self):
        print("NO tiene un sonido audible característico")





animal1 = Delfin("Dolly")
animal2 = Delfin("Flipper")
animal3 = Tiburon("Tiburon Blanco")
animal4 = Tiburon("Tiburon Martillo")


animal1.saluda()
animal3.saluda()

lista_animales = [animal1, animal2, animal3, animal4]

for a in lista_animales:
    a.saluda()
    a.sonido()
    a.salta() 