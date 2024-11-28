"""Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta.
"""

import time
import os  #librerias importadas con el fin de usar el sleep y el cls para esperar ylimpiar el terminal respectivamente.

while True: 

    contra = input("Define contraseña: ").upper()
    bit = True

    os.system("cls") 
    for i in range(5): #simula que carga algo xd
        print("guardando", end="")

        for i in range(9):
            print(".", end="")
            time.sleep(0.03)

        os.system("cls") 

    while bit != False:
        verif = input("Introduce la contraseña definida hace un breve instante\n").upper()

        os.system("cls") 

        if verif in contra:
            print("SI, coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas\n")
            bit = False
        else:
            print("NO coincide con la guardada en la variable\n")