class Persona:
    #Trabajar con atributos de clase.
    total = 0

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        Persona.total += 1

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad

    """
    @classmethod sirve para:
        Crear constructores alternativos.
        Trabajar con atributos de clase.
        Lógica que depende de la clase, no de la instancia.
    """
    #Crear constructores alternativos.
    #Permite crear objetos de formas diferentes a las del constructor principal (__init__).
    @classmethod
    def desde_cadena(cls, cadena):
        nombre, edad = cadena.split("-")
        return cls(nombre, int(edad)) #se crea un objeto Persona nuevo, pasando esos valores al constructor __init__. return Persona(nombre="Juan", edad=25)

#Esto permite instanciar objetos desde formatos especiales (JSON, ficheros, cadenas, etc.).
p1 = Persona.desde_cadena("Guille-25")
p2 = Persona.desde_cadena("Melanie-26")

print(p1.nombre)
print(p1.edad)

print(p2.nombre)
print(p2.edad)

print(Persona.total)



