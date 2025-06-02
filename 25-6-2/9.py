totalganado = 0
totalvendido = 0
ventas1000 = 0
producto=""
while True:
    producto = input("Producto > ")
    if producto == "salir":
        break
    else:        
        cantidad = int(input("Cantidad > "))
        preciou = int(input("Precio Unitario > "))
        
        if cantidad * preciou > 1000:
            ventas1000 +=1
        
        totalganado += cantidad * preciou
        totalvendido += 1

print("Total vendido:", totalvendido)
print("Total ganado:", totalganado)