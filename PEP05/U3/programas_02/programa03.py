import platform
import os

# Mostrar el procesador
print("Procesador:", platform.processor())

# Mostrar el sistema operativo y la versión
print("Sistema Operativo:", platform.system(), platform.version())

# Mostrar el nombre del host
print("Nombre del host:", platform.node())

# Mostrar el directorio actual
print("Directorio actual:", os.getcwd())