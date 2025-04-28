saldo = int(input("Ingresa el saldo: "))
monto = int(input("Ingresa el monto a retirar: "))
if saldo >= monto:
    restante = saldo - monto
    print("El saldo restante es", restante)
else:
    print("Fondos insuficientes")