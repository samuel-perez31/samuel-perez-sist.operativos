ltemp = []
ntemp = int(input("Cantidad de temperaturas > "))
for i in range(ntemp):
    temp = int(input("Ingresar temperatura > "))
    ltemp.append(temp)

ptemp = sum(ltemp)/len(ltemp)

print()
print(f'Promedio de temperaturas: {ptemp}')

c=0
for i in ltemp:
    if i >= ptemp:
        c+=1

print("Cantidad de temperaturas superiores a la media:", c)