presupuesto = 20000
totalgastado = 0
gastos = 1
while True:
    gastos = int(input("Ingrese una compra (0 para finalizar): "))
    totalgastado += gastos
    if gastos == 0:
        presupuesto -= totalgastado
        print("El presupuesto restante es: ",presupuesto)
        break

    if totalgastado > presupuesto:
        print("El total gastado supera el prespuesto, no compres mas") 
        break


  