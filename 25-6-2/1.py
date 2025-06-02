p=0
n=0
c=0

for i in range(20):
    l = int(input("Ingresa un número > "))
    if l > 0:
        p+=1
    elif l < 0:
        n+=1
    else:
        c+=1

print("Hay",p,"positivos,",n,"negativos y",c,"ceros")