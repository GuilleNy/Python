

from .operaciones import sumar, restar, multiplicar, dividir
from .figuras import calcular_area_rectangulo, calcular_area_triangulo, calcular_area_circulo
from .conversiones import a_binario, a_hexadecimal, a_entero

# Controla que se importa al usar 'from matematicas import'
__all__ = [
    "sumar", "restar", "multiplicar", "dividir",
    "calcular_area_rectangulo", "calcular_area_triangulo", "calcular_area_circulo",
    "a_binario", "a_hexadecimal", "a_entero"
]