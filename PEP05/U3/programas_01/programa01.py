"""
Escribe un programa en Python que haga uso de una función llamada saludar que cumpla
los siguientes requisitos:
• Entrada: Tiene 3 parámetros de entrada, que serán 3 cadenas de texto: nombre,
primer apellido, segundo apellido
• Salida: No tiene parámetros de salida.
• Funcionalidad: Imprime por pantalla un mensaje saludando a la persona en función
de los parámetros de entrada

"""
nombre = input("Introduce tu Nombre: ")
apellido1 = input("Introduce tu primer apellido: ")
apellido2 = input("Introduce tu segundo apellido: ")

def saludar(name, apell_1, apell_2):
    print(f"Hola muy buenas {name} {apell_1} {apell_2}")


saludar(nombre, apellido1, apellido2)
