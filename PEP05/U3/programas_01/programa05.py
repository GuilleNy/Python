"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""



#Variables locales
print("Variables Locales")
def mostrar():
    a = 2
    print(a)
    return
a = 5
mostrar()
print(a)



#variables globales
print("Variables globales")

def mostrar2():
    global x
    print(x)
    x=1
    return

x=5
mostrar2()
print(x)


#variables no locales
print("Variables no locales")
def mostrar3():
    def sub_mostrar():
        nonlocal c
        print(c)
        c = 1
        return
    c = 3
    sub_mostrar()
    print(c)
    return
c = 4
mostrar3()
print(c)