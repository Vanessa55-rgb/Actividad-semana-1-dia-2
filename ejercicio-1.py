#Pide tres números al usuario.
#Usa condicionales (if) para decir cuál es el más pequeño.

a = int(input("Digita primer número: "))
b = int(input("DIgita segundo número: "))
c = int(input("Digita tercer número: "))

if a!=b and a!=c and b!=c:
    if a<b:
        if a<c:
            print("El numero menor es: ",a)

if b!=a and b!=c and a!=c:
    if b<a:
        if b<c:
            print("El numero menor es: ",b)

if c!=a and c!=a and a!=b:
    if c<a:
        if c<b:
            print("El numero menor es: ",c)          