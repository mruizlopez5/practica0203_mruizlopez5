"""Escribir un programa que pida al usuario un número 
entero y muestre por pantalla un triángulo rectángulo 
que tenga tantas líneas como el número introducido, 
como el triángulo de más abajo."""
while True:
    
    N = int(input("Introduce numero: "))

    for i in range(1,1+N):
        print("")
        for u in range(i*2-1,0,-2):
            print(u,end=" ")
    print("\n")