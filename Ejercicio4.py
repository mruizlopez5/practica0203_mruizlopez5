"""Para tributar un determinado impuesto se debe ser 
mayor de 16 años y tener unos ingresos iguales o 
superiores a 1000 € mensuales. Escribir un programa 
que pregunte al usuario su edad y sus ingresos mensuales 
y muestre por pantalla si el usuario tiene que tributar 
o no."""

while True:
    edad = int(input("Introduce edad: "))
    salario = input("Introduce salario mensual: ")
    salario = float(salario.replace(",","."))

    if edad >= 16 and salario >= 1000:
        print("Tributas")
    else:
        print("No tributas ")
