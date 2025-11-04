"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""

fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
dia, mes, anio = fecha.split("/")
correcto = True
mensaje = ""
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)


#Aqui se comprueba que todo el formato este correcto
if len(dia) != 2 :
    correcto = False
    mensaje += "El dia debe ser de 2 digitos. \n"
else:
    if not (int(dia) <= 31):
        correcto = False
        mensaje += "El dia debe ser entre el 1 y 31 dias . \n"
    else:
        if  len(mes) != 2:
            correcto = False
            mensaje += "El mes debe ser de 2 digitos. \n"
        else:
            if not(int(mes) <= 12):
                correcto = False
                mensaje += "El mes debe ser entre 1 y 12 meses. \n"
            else:
                if len(anio) != 4 :
                    correcto = False
                    mensaje += "El año debe ser de 4 digitos.\n"

    
if correcto :
    match int(mes):
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if 1 <= int(dia) and int(dia) !=30:
                print("Fecha correcta")
            else:
                print("Fecha incorrecta, el dia no corresponde a su mes.")
            
        case 4 | 6 | 9 | 11:
            if 1 <= int(dia) and int(dia) !=31:
                print("Fecha correcta")
            else:
                print("Fecha incorrecta, el dia no corresponde a su mes.")
        case 2 :
            if 1 <= int(dia) <= 29:
                print("Fecha correcta")
            else:
                print("Fecha incorrecta, el dia no corresponde a su mes.")
        case _:
            print("Fecha incorrecta")
else:
    print("Fecha incorrecta")
    print(mensaje)



