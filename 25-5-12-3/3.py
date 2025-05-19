productos = -1
sumaproductos = 0
while productos != 0:
    productos = int(input("Ingresa el precio del producto: "))
    sumaproductos += productos
print(sumaproductos)
if sumaproductos > 10000:
    descuento = sumaproductos * 0.10
    sumaproductos = sumaproductos - descuento
    print("El precio con descuento es: ", sumaproductos)