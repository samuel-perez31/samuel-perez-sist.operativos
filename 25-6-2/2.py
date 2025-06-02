num = int(input("Ingresad el numero: "))
suma=0
while num > 0:
    resto = num % 10
    num = num//10
    suma += resto

print(suma)