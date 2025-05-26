presupuesto = 50000
totalgastado = 0
gastos = 1
while True:
    gastos = int(input("Ingrese un gasto (0 para finalizar): "))
    if gastos == 0:
        break
    totalgastado += gastos
print("El total gastado es: ", totalgastado) 
if totalgastado > presupuesto:
    print("El total gastado supera el prespuesto")   