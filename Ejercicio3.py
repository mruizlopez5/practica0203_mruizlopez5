"""Escribir un programa que pida al usuario un número 
entero y muestre por pantalla si es par o impar."""
while True:
    num = int(input("introduce numero entero: "))

    if num%2 == 0:
        print("Es numero par")
    else:
        print("No es numero par")