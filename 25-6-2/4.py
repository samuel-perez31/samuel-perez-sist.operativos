nota = 0 
promedio = 0
contador = 0
invalido = -1
while not nota == -1:
    nota = int(input("Ingresa la nota del alumno (-1 para finalizar): "))
    if nota >= 1 and nota <= 10:
        promedio += nota
        contador += 1
    else:
        invalido += 1

print("El promedio de notas es",promedio/contador,"entre",contador,"alumnos y las notas fuera de rango fueron",invalido)

