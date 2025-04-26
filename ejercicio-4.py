#Pide al usuario su edad.
#Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
#Si está en el rango correcto, imprime "Edad válida".

Edad=int(input("Digita tu edad: "))
if Edad <=0 or Edad >=120:
    print("Edad no válida") 
else:
    print("Edad válida")

