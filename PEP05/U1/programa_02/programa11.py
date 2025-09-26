print("Introduce la hora de salida del punto A:")
print("HH: ")
hora_A=int(input())

print("MM: ")
min_A=int(input())

print("SS: ")
seg_A=int(input())


print("Introduce en segundos la llegada al punto B: ")
seg_B=int(input())

#Paso la hora y los minutos a segundos para sumar todo incluso con los segundos de llegada
horaSeg=hora_A * 3600
minSeg=min_A * 60
totalSeg_AB=horaSeg + minSeg + seg_A + seg_B

#Una vez sumado todos los segundos pasamos a hora , minutos y segundos
hora_llegada=totalSeg_AB // 3600 #Una hora son 3600 segundos por lo que los segundos lo pasamos a hora dividiendolo.
min_llegada= (totalSeg_AB // 60 ) % 60  #Obtenemos la división entera entre 60 y luego el resultado de esa division obtenemos el resto dividiendo a 60 para obtener los minutos.
seg_llegada= totalSeg_AB % 60 #El segundo total lo dividimos a 60 para obtener el resto que seria los segundos.

print(f"Hora de llegada: {hora_llegada}:{min_llegada}:{seg_llegada}.")

