"""Escribir un programa que pida al usuario dos números y 
muestre por pantalla su división. Si el divisor es cero el 
programa debe mostrar un error."""


while True:

    num = input("introduce cifras para el numerador: ")
    den = input("introduce cifras para el denominador: ")

    num = float(num.replace(",","."))
    den = float(den.replace(",","."))


    if den == 0:
        print("ERROR CATASTRÓFICO")
    else:
        res = num/den
        print(round(res, 3))