lista = []
nlista = int(input("Ingresa los numeros de la lista(200 max): "))
for i in range(nlista):
    n = int(input("Ingresa un numero: "))
    lista.append(n)

lista = list(set(lista))
lista.sort()
print(lista)