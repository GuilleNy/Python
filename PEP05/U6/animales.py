class Animal:
    def __init__(self, nombre, especie, edad, id_chip):
        self.nombre = nombre #atributo publico
        self.especie = especie #atributo publico
        self._edad = edad #atributo publico
        self.__id_chip = id_chip #atributo privado, accedo a el con un get o set

        #atributo publico: accesible cuando uso el ojeto, ._id_chip 
        #atributo protegido: es privado , .__id_chip 


    def get_id_chip(self):
        return self.__id_chip
    
    def set_id_chip(self, nuevo_id_chip):
        if (isinstance(nuevo_id_chip, str)):

            self.__id_chip = nuevo_id_chip
        else:
            raise (TypeError("EL id_chip debe ser un string"))


    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años")


    def cumplir_anios(self):
        self.edad = self.edad + 1






animal1 = Animal("Kuma", "tigre", 10, "a123")
animal2 = Animal("Miu", "gato", 5, "a234")

print(animal1.nombre)
print(animal1._edad)
print(animal1._Animal__id_chip)

#Todos los atributus son publicos

"""
print(animal1.nombre)
animal1.nombre = "Agod"
print(animal2.especie)


animal1.saludar() #Animal.saludad(animal1)
animal1.cumplir_anios()
animal1.edad = animal1.edad + 1 #puedo hacer esto porque estos atributos son publicos
animal1.saludar()

print(animal1.get_id_chip())
animal1.set_id_chip("a44544")
animal1.set_id_chip(5) #Aqui lanza la excepction porque es un entero qeu se pasa por paramentro.
print(animal1.get_id_chip())
#print(animal1.Animal.__id_chip)

"""