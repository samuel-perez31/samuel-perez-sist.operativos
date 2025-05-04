import random
import string

def random_mayus():
    return random.choice(string.ascii_uppercase)

def random_minus():
    return random.choice(string.ascii_lowercase)

def random_num():
    return random.randint(0,9)

def random_sim():
    return random.choice(string.punctuation)

caracteres = [random_mayus, random_minus, random_num, random_sim]
e = []

print("---------------------------")
print("Generador de contraseñas seguras")
print("---------------------------")

c = int(input("Cantidad de caracteres: "))

e.append(int(input("Mayúsculas (1: Sí, 0: No): ")))
e.append(int(input("Minúsculas (1: Sí, 0: No): ")))
e.append(int(input("Números (1: Sí, 0: No): ")))
e.append(int(input("Símbolos (1: Sí, 0: No): ")))

for i in range(len(e)-1, -1, -1):
    if e[i] != 1:
        caracteres.pop(i)
        
print()

for i in range(c):
    print(random.choice(caracteres)(), end="")