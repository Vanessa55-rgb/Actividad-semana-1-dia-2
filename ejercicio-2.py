#Crea una lista con 5 números.
#Pide un número al usuario y verifica si está en la lista usando in.

Lista = [1, 2, 3, 4,  5]

numerousuario = int(input("Digita un número: "))

#in verificar si un valor está presente en una secuencia

if numerousuario in Lista:
    print("Si está en la lista") 
else:
    print("No está en la lista usando ")

