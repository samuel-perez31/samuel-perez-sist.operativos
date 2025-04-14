

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


#7

lb = float(input("Ingrese lado b: "))
lc = float(input("Ingresa lado c: "))
a = float(input("Ingresa ángulo alfa: "))

r = a * 3.1416 / 180

la = lb ** 2 + lc ** 2 - 2*lb*lc * math.cos(r) ** 0.5


#8

va = float(input("Ingrese velocidad a: "))
vb = float(input("Ingrese velocidad b: "))
d = float(input("Ingrese distancia: "))

te = d/(va+vb)

print(te)

#9
angulor = int(input("Ingrese el angulo en radianes: "))
sex = angulor * 180 / 3.1416
cen = angulor * 200 / 3.1416
print("En sexagesimal es: ", sex)
print("En cen es: ", cen)

#10
x1 = int(input("Ingrese el valor de x1: "))
y1 = int(input("Ingrese el valor de y1: "))
z1 = int(input("Ingrese el valor de z1: "))
x2 = int(input("Ingrese el valor de x2: "))
y2 = int(input("Ingrese el valor de y2: "))
z2 = int(input("Ingrese el valor de z2: "))

distancia = ((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)**0.5
print("La distancia es: ",distancia)