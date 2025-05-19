pos=0
cpos=0
neg=0
cneg=0
for i in range(10):
    n = int(input("Ingrese un numero: "))
    if n > 0:
        pos+=n
        cpos+=1
    elif n < 0:
        neg+=n
        cneg+=1

print("Positivos:", cpos, "promedio:", pos/cpos)
print("Negativos:", cneg, "promedio:", neg/cneg)