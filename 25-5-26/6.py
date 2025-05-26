tr = 0
md = 0
c = 0

while True:
    d = int(input("Ingresar donación > "))
    if d == 0:
        break
    else:
        if d > md:
            md = d
        tr += d
        c += 1

print("Donadores:",c)
print("Total donado:",tr)
print("Mayor doncaión:",md)