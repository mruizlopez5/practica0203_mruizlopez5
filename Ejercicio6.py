"""Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla todos los años que ha cumplido 
(desde 1 hasta su edad)."""
while True:
    edad = int(input("introduce tu edad: "))

    if edad > 120:
        print("introduzca un valor realista")

    else:
        for i in range(edad):
            print("Has cumplido:",i+1,"años")

