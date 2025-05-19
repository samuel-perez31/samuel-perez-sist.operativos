n=int(input("Ingrese un numero: "))
p=True
for i in range(2, n):
    if n%i == 0:
        p=False
        break
if p==True:
    print("El numero es primo") 
else:
    print("El numero no es primo")