stock = 100
stockpr = stock * 0.1
vendido = 0
while True:
    vendido = int(input("Ingrese los articulos vendidos (0 para finalizar): "))
    stock = stock - vendido
    if stock <= stockpr:
        print("Queda menos del 10% del stock")
    
    if stock <= 0:
        print("No alcanza el stock")
        break
    
    if vendido == 0:
        print("El stock restante es: ", stock)
        break

    