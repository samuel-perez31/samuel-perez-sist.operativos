"""

#1

r = float(input("Ingrese el radio: "))
volumen = 4/3 * 3.1416 * r ** 3
print("El volumen es", volumen)


#2

h = float(input("Ingrese la altura del triangulo: "))
perimetro = 3*(2*h/3**0.5)
print("el perimetro es ", perimetro)


#3

s = float(input("Ingresar soles > "))

d = s / 3.25
e = s / 3.83

print(f'{s} soles = {round(d,2)} dólares y {round(e,2)} euros')


#4

t = float(input("Ingrese tiempo en segundos > "))
m = float(input("Ingrese distancia en metros > "))

v = m/t

print("Velocidad el móvil:", v, "m/s")



#5

precio = int(input("Ingresa el precio unitario del producto: "))
n = int(input("Ingresa el numero de docenas: "))

preciot = precio*12*n
print("El precio total es: ",preciot)


#6
millas = float(input("Ingreselas millas: "))
kilometros = 1.609344 * millas

print("La cantidad de millas en kilometros es: ",kilometros)

"""
#7

