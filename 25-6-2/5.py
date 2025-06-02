cantidad=0
gasto=0
salir=0
while salir != 2:
    print("1. Comprar")
    print("2. Salir")
    salir = int(input("> "))
    print()
    if salir == 1:
        producto = input("Ingresar producto > ")
        cantidad += int(input("Ingresar cantidad > "))
        precio = int(input("Ingresar precio > "))
        gasto += cantidad*precio
        print()
        
print("Cantidad comprada:", cantidad)
print("Cantidad gastada:", gasto)