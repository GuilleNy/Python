print("Introduzca un numero de bytes: ")
byte=int(input())

#Sistema decimal

GB = byte // 10**9  #Obtengo el GB
resto_GB = byte % 10**9

MB = resto_GB // 10**6  #Obtengo el MB
resto_MB = resto_GB % 10**6

KB = resto_MB // 10**3  #Obtengo el KB
resto_KB = resto_MB % 10**3 ##Obtengo el bytes

#Sistema binario

GiB = byte // 1024**3  #Obtengo el GB
resto_GiB = byte % 1024**3

MiB = resto_GiB // 1024**2  #Obtengo el MB
resto_MiB = resto_GiB % 1024**2

KiB = resto_MiB // 1024  #Obtengo el KB
resto_KiB = resto_MiB % 1024 ##Obtengo el bytes



print(f"{GB} GB, {MB} MB, {KB} KB, {resto_KB} bytes")
print(f"{GiB} GiB, {MiB} MiB, {KiB} KiB, {resto_KiB} bytes")