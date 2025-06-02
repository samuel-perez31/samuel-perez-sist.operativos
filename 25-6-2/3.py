n = int(input("Ingresa el número > "))
p=True

for i in range(2,n):
    if n%i == 0:
        p=False
        break

if p == True:
    print("El número es primo")
else:
    print("El número no es primo")