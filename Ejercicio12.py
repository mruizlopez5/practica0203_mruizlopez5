"""
Escribir un programa en el que se pregunte al usuario por una 
frase y una letra, y muestre por pantalla el número de veces que 
aparece la letra en la frase
"""

frase = input("introduce una frase:")
letra = input("introduce una letra:")
N = len(frase)
count = 0
for letras in range(N):
    if letra in frase[letras]:
        count += 1
print(count)