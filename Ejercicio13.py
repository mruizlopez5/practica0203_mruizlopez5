"""
Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará.
"""
print("escriba lo que quiera, para salir escriba: salir")
val = True
while val != False:
    a = input()
    print(a)
    if "salir" in a:    
        val = False


        
