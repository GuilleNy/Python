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
        return self.__vida > 0 
    
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

        print(f"{self.nombre} golpea con {self.arma.nombre} y causa {danio} de daño, y lo deja con {objetivo.vida}.")


class Mago(Personaje):
    def __init__(self,nombre, vida, mana,  hechizos):
        super().__init__(nombre, vida)
        self.__mana = mana #100
        self.__hechizos = hechizos

    @property
    def hechizos(self):
        return self.__hechizos
    
    @property
    def mana(self):
        return self.__mana
    
    @mana.setter
    def mana (self, valor):
        # Evita mana negativa
        if (valor < 0 ):
            self.__mana = 0
        else:
            self.__mana = valor

        #Tambien funcionaria asi
        #self._mana = max(0, valor)
         
    
    def atacar(self, objetivo):
        """
        random.choice(list(dic.keys()))
        1. dic.keys() obtiene todas las claves del diccionario, esto NO devuelve una lista.
            Devuelve un objeto especial llamado “vista de claves” (dict_keys). entonces que se hace? se convierte la vista de claves en una lista. list()
        2. list(...) convierte esas claves en una lista real.
        3. random.choice(...) selecciona una posición aleatoria de esa lista.
        4. El resultado es una clave aleatoria del diccionario.
        """
        hechizo = random.choice(list(self.hechizos.keys()))
        danio = self.hechizos[hechizo]
        #Consumir la vida del oponente y el mana del mago
        objetivo.vida -= danio
        self.mana -= danio
        


        #Si el mana que tiene el mago es menor al poder magico que lanza enotnces poierde oportunidad y de paso recupera algo de mana
        if self.mana < danio:
            print(f"{self.nombre} se quedo sin mana y no puede lanzar {hechizo}, pierde el turno.")
            self.mana +=10
            print(f"Mana del mago sube a {self.mana}")
        
       

        #Recuperacion
        if self.mana < 100:
            self.mana +=10
            print(f"Mana del mago sube a {self.mana}")
            

        print(f"{self.nombre} lanza {hechizo} y causa {danio} de daño, y lo deja con {objetivo.vida}.")
        print(f"Mana del mago se queda en {self.mana}")
        

        
def combate(a,b):
    turno = 1
    print("\n--- COMIENZA EL COMBATE ---\n")


    while a.vivo and b.vivo:
        print(f"\n --- Turno {turno} ---")

        a.atacar(b)
        print(f"{b.nombre} queda con  {b.vida} de vida.")

        if not b.vivo:
            break
    
            
        b.atacar(a)
        print(f"{a.nombre} queda con {a.vida} de vida.")

        turno += 1
    
    print("\n--- FIN DEL COMBATE ---\n")
    if a.vivo :
        vencedor = a
    else:
        vencedor = b

    print(f"{vencedor.nombre} gana con {vencedor.vida} de vida restante.")




espada = Arma("Espada larga", 20)
guerrero = Guerrero("Arthur", 200, espada)

mago = Mago("Merlin", 200, 100,  {
    "Bola de fuego": 18,
    "Rayo": 22,
    "Hielo": 15
})

combate(guerrero, mago)


