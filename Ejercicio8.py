"""Escribir un programa que muestre por pantalla la tabla 
de multiplicar del 1 al 10 del número que introduzca el 
usuario."""

N = int(input("Que tabla de multiplicar quieres visualizar?: "))

for i in range(10):
    print(N,"x",(i+1),"=",(i+1)*N)