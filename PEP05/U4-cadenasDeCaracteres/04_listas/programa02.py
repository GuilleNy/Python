"""
Escribe un programa en Python que guarde la temperatura mínima y máxima de 5 días en
una lista de dos dimensiones y a continuación muestre.
    • La temperatura media de cada día.
    • Los días con menos temperatura.
    • Se lea una temperatura por teclado y se muestran los días cuya temperatura
    máxima coincide con ella. Si no existe ningún día se muestra un mensaje
    de .información
"""

temperatura = [[12,3], [14,5], [10,3], [13,5], [15,2]]
lista_media = []

for i , valor in enumerate(temperatura):
   media = sum(valor) / len(valor)
   lista_media.append(media)
   print(f"Dia {i+1}: tiene una media de {media}")

minimo = min(lista_media)
dia = lista_media.index(minimo)

print(f"El dia con menos temperatura es el dia {dia+1} con {minimo} ºc")



temp = float(input("Introduce una temperatura: "))

encontrado = False
for i , valor in enumerate(temperatura):
    if valor[0] == temp:
      print(f"La temperatura {temp} coincide con el dia {i+1}.")
      encontrado = True

if not encontrado:
   print("No existe ningun dia con esa temperatura.")