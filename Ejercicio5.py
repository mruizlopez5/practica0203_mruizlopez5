"""Los alumnos de Hogwarts se han dividido en dos casas, 
Gryffindor y Slytherin, de acuerdo al sexo y el nombre. 
Gryffindor está formado por las mujeres con un nombre 
anterior a la M y los hombres con un nombre posterior a 
la N y Slytheryn por el resto. Escribir un programa que 
pregunte al usuario su nombre y sexo, y muestre por 
pantalla el grupo que le corresponde."""

while True:
    nombre = input("introduce nombre: ").lower()
    nombre = list(nombre)
    sexo = input("Hombre o Mujer: ").lower()
    sexo = list(sexo)



    if (sexo[0] == "m" and nombre[0] < "m") or (sexo[0]=="h" and nombre[0] > "n"):
        print("Slytherin")
    else:
        print("Gryffindor")