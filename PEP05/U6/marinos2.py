from abc import ABC, abstractmethod


#una calse astracta no puede ser instanciada
class AnimalMarino(ABC):

    def __init__(self, nombre):
        self.__nombre = nombre
    
    #en esta ocasion es necesario el getter para acceder al nombre desde las clases hijas.
    #Si el @property está definido en la clase padre, las subclases heredan el getter automáticamente
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
    #Sin este metodo, al imprimir el objeto se muestra su dirección en memoria como esta <__main__.Delfin object at 0x000001C73BA286E0>
    def __str__(self):
        return f"Animal marino: {self.__nombre}" # Aquí también se usa el property
    

    
class Delfin(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)

    def saluda(self):
        print(f"Soy un delfin {self.nombre}")

    def sonido(self):
        print("Click y silbido")


    #su obetivo es sumar dos objetos de la misma clase
    #el método mágico __add__, que le indica a Python cómo debe comportarse el operador + cuando se usa entre dos objetos de la clase.
    #permite sobrecargar el operador +.
    def __add__(self, otro):
        return Delfin(self.nombre + otro.nombre) # Aquí se usa el property
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


print(animal1) # Sin el metodo __str__ habria mostrado la direccion en memoria




#devuelve un diccionario con los atributos del objeto y el valor de los mismos, no requiere el @property
print(animal1.__dict__)


"""
#python hace la suma de los dos objetos llamando al metodo magico __add__
#Si obj1 tiene definido __add__, se llama a ese método.
#Pero si obj1 no tiene __add__, Python intentará llamar a __radd__ en obj2.
#En este caso, ambos objetos son de la misma clase, por lo que se llama a __add__ de animal1.
animal3 = animal1 + animal2
print(animal3)  # Animal marino: DollyFlipper

"""