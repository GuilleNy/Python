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


    #metodo magico para representar el objeto como string
    def __str__(self):
        return f"Animal marino: {self.__nombre}"
    

    
class Delfin(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)

    def saluda(self):
        print(f"Soy un delfin {self.nombre}")

    def sonido(self):
        print("Click y silbido")


    def salta(self):
        print(f"El delfin {self.nombre} está saltando fuera del agua!")

    #su obetivo es sumar dos objetos de la misma clase
    def __add__(self, otro):
        return Delfin(self.nombre + otro.nombre)
    #retorna una nueva instancia de la clase con el nombre concatenado


class Tiburon(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)

    def saluda(self):
        print(f"Soy un tiburon {self.nombre}")

    def sonido(self):
        print("NO tiene un sonido audible característico")





animal1 = Delfin("Dolly")
animal2 = Delfin("Flipper")


print(animal1)


#devuelve un diccionario con los atributos del objeto y el valor de los mismos
print(animal1.__dict__)

#python hace 
animal3 = animal1 + animal2
print(animal3)  # Animal marino: DollyFlipper