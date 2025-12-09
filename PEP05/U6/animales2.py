class Animal:


    def __init__(self, nombre, especie, edad, id_chip, peso=60):
        self.nombre = nombre #atributo publico
        self.especie = especie #atributo publico
        self.edad = edad #atributo publico
        self.__id_chip = id_chip #atributo privado, accedo a el con metodo get o set
        self.__peso = peso

        #atributo publico: accesible cuando uso el ojeto, ._id_chip 
        #atributo protegido: es privado , .__id_chip 


    #getter
    @property
    def id_chip(self):
        return self.__id_chip
    
    #setter
    @id_chip.setter
    def id_chip(self, nuevo_id_chip):
        if (isinstance(nuevo_id_chip, str)):

            self.__id_chip = nuevo_id_chip
            print("Se ha cambiado el chip")
        else:
            raise (TypeError("EL id_chip debe ser un string"))

    #getter
    @property
    def peso(self):
        return self.__peso

    #setter
    @peso.setter
    def perso(self, nuevo_peso):
        if(nuevo_peso < 0):
            raise ValueError("El peso debe ser positivo.")
        else:
            self.__peso = nuevo_peso



    def saludar(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años")


    def cumplir_anios(self):
        self.edad = self.edad + 1


try:
    animal1 = Animal("Kuma", "tigre", 10, "a123")
    animal2 = Animal("Miu", "gato", 5, "a234")

    print(animal1.id_chip)
    animal1.id_chip = "a5556" 
    print(animal1.id_chip)
    animal1.id_chip = 5
    print(animal1.id_chip)


    animal1.peso = "99"
    print(animal1.peso)



except Exception as e:
    print(e)