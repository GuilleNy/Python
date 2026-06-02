from os import strerror
import csv

cabeceras = ["Nombre", "Tipo", "Lunas"]

planetas = [{"Nombre": "Marte","Tipo": "Rocoso", "Lunas": 2},
            {"Nombre": "Jupiter","Tipo": "Gaseoso", "Lunas": 79},
            {"Nombre": "Venus","Tipo": "Rocoso", "Lunas": 0}]


try:
   
    with open("planetas.csv", "w", encoding="utf-8") as fichero_csv:
        writer = csv.DictWriter(fichero_csv, fieldnames=cabeceras, delimiter= ";")

        writer.writeheader()
        writer.writerows(planetas)

        print("Fichero CSV creado")
        

    with open("planetas.csv", "r", encoding="utf-8") as fichero_csv:
        reader = csv.reader(fichero_csv , delimiter=";")

        cabecera_fila = next(reader) #next(reader) devuelve la primera fila y avanza a la siguiente fila.
        #print(f"Los nombres de las columnas son {",".join(cabecera_fila)}")
        
        for fila in reader:
            print(f"El planeta de {fila[0]} es de tipo {fila[1]} y tiene {fila[2]} de lunas ")

except Exception as exc:
    print("Error", strerror(exc.errno))
