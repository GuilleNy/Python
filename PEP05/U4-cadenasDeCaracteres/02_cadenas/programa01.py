"""
Escribe un programa en Python que realice que extraiga el nombre de usuario y la
contraseña de la siguiente cadena: "usuario:root|contraseña:123456"

"""

cadena = "usuario:root|contraseña:123456"

separar = cadena.split('|')

usuario = separar[0].split(':')[1]
contraseña = separar[1].split(':')[1]

print(usuario)
print(contraseña)