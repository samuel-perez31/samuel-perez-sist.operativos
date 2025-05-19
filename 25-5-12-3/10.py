e=0
while e!=5:
    print("MENU")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    e = int(input("Ingrese una opcion: "))
    
    if e==1:
        print("suma")
    elif e==2:
        print("resta")
    elif e==3:
        print("multiplicacion")
    elif e==4:
        print("division")
    elif e==5:
        print("salir")
        exit()