
from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precios):
        self.__nombre = nombre
        self.__precios = precios

    @property
    def nombre(self):
        return self.__nombre
    

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if (isinstance(nuevo_nombre,str)):
            self.__nombre = nuevo_nombre
        else:    
            raise (TypeError("El nombre debe ser un string"))

    
    @property
    def precios(self):
        return self.__precios
            

    @abstractmethod
    def calcular_precio_final(self):
        raise NotImplementedError
    
    def añadir_precio(self, precio):
        self.__precios.append(precio)




class DiscoDuro(Producto):
    def __init__(self, nombre, precios, tipo):
        super().__init__(nombre, precios)
        self.__tipo = tipo


    @property
    def tipo(self):
        return self.__tipo
    
    def calcular_precio_final(self):
        if "HDD" in self.tipo:
            self.precios = self.precios * 0.20

    def __str__(self):
        return f"DiscoDuro(nombre={self.nombre}, tipo={self.tipo})"
    

class Memoria(Producto):
    def __init__(self, nombre, precios, capacidad):
        super().__init__(nombre, precios)
        self.__capacidad = capacidad


    @property
    def capacidad(self):
        return self.__capacidad
    
    def calcular_precio_final(self):
        if self.__capacidad == 16 :
            self.precios = self.precios * 0.50
        


    def __str__(self):
        return f"Memoria(nombre={self.nombre}, capacidad={self.capacidad})"
    



try:
    precios_discos = [500, 855, 741 ]

    discoDuro = DiscoDuro("Generico", precios_discos, "HDD")

    precios_memoria = [748, 256, 145]

    memoria = Memoria("deluxu", precios_memoria, 16)

    print(discoDuro)

    print(memoria)


   
except Exception as e:
    print(e)
    