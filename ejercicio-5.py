#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#Pide al usuario su nombre.
#Usa if para decir si está en la lista de invitados o no.

ListaNombres = ["Ana", "Luis", "Sofía"]

Nombreusuario = input("Digita su nombre: ")

if Nombreusuario in ListaNombres:
    print("Si estas en la lista de invitados")
else:
    print("No estas en la lista de invitados")