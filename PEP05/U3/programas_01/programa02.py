"""
Escribe un programa en Python que haga uso de una función llamada saludar que cumpla
los siguientes requisitos:
• Entrada: Tiene 4 parámetros de entrada, que serán 4 cadenas de texto: nombre,
primer apellido, segundo apellido y curso. El parámetro curso tendrá en la
declaración de la función el valor por defecto “2DAW”
• Salida: No tiene parámetros de salida.
• Funcionalidad: Imprime por pantalla un mensaje saludando al alumno/a que se
haya pasado como parámetro de entrada.
El programa debe invocar a la función varias veces. En algunas de ellas se tiene que usar
el paso de parámetros de forma nominal (con clave valor)
"""


def saludar(name, apell_1, apell_2, curso="2DAW"):
    print(f"Hola muy buenas {name} {apell_1} {apell_2} del curso {curso}")

saludar("Guillemo", "Niebla", "Pincay")
saludar("Alex", "Rosario", "Hernandez", "1DAW")


saludar(name="Maria", apell_1="Puente", apell_2="Moreno")
saludar(name="Alejandro", apell_1="Gonzalez", apell_2="Rodriguez", curso="1ASIR")




