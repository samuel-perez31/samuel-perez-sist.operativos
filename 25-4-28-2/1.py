cuenta = int(input("Ingresa el valor de la cuenta: "))
propina = int(input("Ingresa el porcentaje de propina que quieres dar: "))
total = cuenta + (propina*cuenta)/100
print(total)