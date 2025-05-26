dias30 = 0
dias = 0 
temperaturacp = 0
while dias < 7:
    temperatura = int(input("Ingresa la temperatura de este dia: "))
    temperaturacp += temperatura
    dias += 1
    if temperatura >= 30: 
        dias30 += 1
print("El promedio de temperatura es: ", round(temperaturacp/7,2))
print("Hubo ", dias30, "con mas de 30 grados")
